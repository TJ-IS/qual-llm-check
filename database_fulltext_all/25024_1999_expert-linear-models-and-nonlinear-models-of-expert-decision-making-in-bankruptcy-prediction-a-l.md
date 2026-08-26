---
otero_id: 25024
otero_key: "Z9N64QV6"
title: "Expert, Linear Models, and Nonlinear Models of Expert Decision Making in Bankruptcy Prediction: A Lens Model Analysis"
authors: "Choong Nyoung Kim; Raymond McLeod"
year: "1999"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1999.11518239"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Expert, Linear Models, and Nonlinear Models of Expert Decision Making in Bankruptcy Prediction: A Lens Model Analysis

Choong Nyoung Kim & Raymond McLeod Jr.

To cite this article: Choong Nyoung Kim & Raymond McLeod Jr. (1999) Expert, Linear Models, and Nonlinear Models of Expert Decision Making in Bankruptcy Prediction: A Lens Model Analysis, Journal of Management Information Systems, 16:1, 189-206, DOI: 10.1080/07421222.1999.11518239

To link to this article: http://dx.doi.org/10.1080/07421222.1999.11518239

![](/api/attachments/Z9N64QV6/fulltext/images/9241f4aa0510d2a400d0a32345a0bd81ca03a24fee4082c58bfcef94483f2514.jpg)

Published online: 02 Dec 2015.

![](/api/attachments/Z9N64QV6/fulltext/images/1c3381139ec04618d5971d9fbad6aa5673145da3011cf76be2fa628105194dc9.jpg)

Submit your article to this journal ↗

![](/api/attachments/Z9N64QV6/fulltext/images/943aac897dba4c7e4a4a1fbc8b1b537ded8279080f55883e28029f41f5731bda.jpg)

Article views: 9

![](/api/attachments/Z9N64QV6/fulltext/images/439e3f4084c3bc7681cacc7e37ef774eb96ff91422d14f2771923973e58e9c08.jpg)

View related articles ↗

![](/api/attachments/Z9N64QV6/fulltext/images/7ba88411580e204e899a76c37f391069de53a19e9dd877f35d4f03562921a43e.jpg)

Citing articles: 1 View citing articles ↗

# Expert, Linear Models, and Nonlinear Models of Expert Decision Making in Bankruptcy Prediction: A Lens Model Analysis

CHOONG NYOUNG KIM AND RAYMOND MCLEOD, JR.

CHOONG NYOUNG KIM is an Associate Professor in the Business Department at Hallym University. He received his M.B.A. from the University of Missouri at Columbia and his Ph.D. from Texas A&M University. His research interests include decision support systems and expert systems, human information processing, machine learning, and data mining. His research findings have been published in the Proceedings of the 1996 PRIISM Conference and the Journal of Global Information Management.

RAYMOND MCLEOD, JR. is a Visiting Professor at the University of Texas at Austin. His research interests include executive information systems, marketing information systems, and human resources information systems. His research findings have appeared in California Management Review, Communications of the ACM, and Journal of Management Information Systems, and MIS Quarterly. He has also written textbooks on the introduction to computing, systems analysis and design, decision support systems, and management information systems.

ABSTRACT: Analysis of human judgment and decision making provides useful methodologies for examining the human decision process and substantive results. One such methodology is a lens model analysis. We used such a model to study how well a model of expert decisions can capture a valid strategy in the decision process. The study also addresses whether a model of an expert can be more accurate than the expert.

The predictive accuracy (predictive validity) of two linear (statistical) models and two nonlinear models of human experts is compared. The results indicate that nonlinear models can capture factors (valid nonlinear strategy) that contribute to the experts' predictive accuracy. However, linear models cannot capture the valid nonlinear strategy as well as nonlinear models.

One linear model and two nonlinear models performed as well as the overall average of a group of experts. However, all of the models were outperformed by the most accurate expert. By combining validity of decision strategy with characteristics of modeling algorithms, it is possible to explain why certain algorithms perform better than others.

KEY WORDS AND PHRASES: decision strategy, human expert, inductive learning, lens model, linear model, nonlinear model, predictive validity.

HUMAN DECISION MAKING HAS BEEN STUDIED FOR A LONG TIME, both normatively and descriptively. One of the major efforts, performed primarily by psychologists, has been the construction of decision models that describe, mimic, and/or replace human judgment. In attempting to construct the models, there are two dominant paradigms: output analysis and process tracing. The former focuses on finding relationships between relevant cues and resulting decisions reached by humans, and developing a decision model simulating the relationships. The latter paradigm focuses on the process of making judgments and developing various methodologies for the analysis of the decision process.

With the advancement of computer technology, interest in modeling human judgment has been revisited in artificial intelligence, with a different name—expert modeling. In expert modeling, the task is to extract knowledge from an expert so as to build a reliable knowledge base for an expert system. Although computer scientists have pursued the same goal as decision researchers in judgment modeling, the computer scientists have typically failed to properly consider the behavioral aspects of human decision making $[20]$ . Because of this omission, certain valuable methodologies of behavioral decision research have never been incorporated into expert-modeling research.

This paper extends the behavioral decision research to expert modeling by (1) using a valuable method of decision research to examine the validity of the decision strategy of human experts, (2) comparing predictive validity between two linear (statistical) models and two well-known inductive learning methods, and (3) examining the contingent relationship between the validity of the decision strategy and predictive validity of the four different models of the experts.

## Literature Review

THIS SECTION REVIEWS KEY LITERATURE IN BEHAVIORAL DECISION research and empirical studies in expert modeling as an extension of judgment modeling. Two research questions are also raised based on the literature review.

## Lens Model Studies

First proposed by Brunswick [2], the lens model has been described by others [14, 35] to investigate the use of nonlinearity in human decision-making behavior. Many behavioral accounting researchers have discussed the use of the lens model with regard to the examination of a judgment situation in which a human makes decisions [22].

The three basic elements of the lens model (figure 1) are the cues (variables: $x_{1}, x_{2}, \ldots, x_{k}$ ), actual outcomes observed in the environment ( $Y_{e}$ ), and the decisions of the decision maker ( $Y_{s}$ ). It is possible to derive two linear regression models on both sides of the lens. One equation represents a linear relationship between cues and the actual outcomes ( $Y_{e}$ ) and generates the linear predictions ( $Y_{t}$ ) of the actual outcomes.

Independent Variables (Cues)  
![](/api/attachments/Z9N64QV6/fulltext/images/8cbd68fa3112d3e525733a650b7775aecf74975931dffc902ba0bd4c222b68fe.jpg)  
Where :  
(1) $Y_{t} = \text{Sum}(B_{i} * X_{i})$ Linear Regression of Actual Outcomes  
(2) $Y_{f} = \text{Sum}(C_i * X_i)$ Linear Regression of Expert Decisions

Figure 1. Lens Model

The other represents a linear relationship between the cues and the human decisions $(Y_{s})$ and generates the linear predictions $(Y_{f})$ of the human decisions.

The resulting four sets of Y values $(Y_{e}, Y_{s}, Y_{p}, Y_{f})$ can be used to obtain five correlation indices, each of which is useful for evaluating a particular aspect of a decision maker's performance. Tucker [35] showed that five indices are functionally related in a general equation:

$$
r _ {a} = G ^ {*} R _ {t} ^ {*} R _ {f} + C (1 - R _ {t} ^ {2}) ^ {1 / 2} (1 - R _ {f} ^ {2}) ^ {1 / 2},
$$

where

$C =$ correlation coefficient of residuals corresponding to $Y_{t}$ and $Y_{f}$ ;

$Y_{e} =$ actual (normative) outcomes in the environmental database;

$$
Y _ {s} = \text { the   human   expert's   decisions };
$$

$Y_{t} =$ predicted values (outcomes) from a linear regression of actual outcomes on cues;

$Y_{f}=$ predicted values (decisions) from a linear regression of decisions of the

$$
r _ {a} = \text { correlation   of } Y _ {s} \text { and } Y _ {e};
$$

$$
G = \text { correlation   of } Y _ {t} \text { and } Y _ {f};
$$

$$
R _ {t} = \text { correlation   of } Y _ {e} \text { and } \dot {Y} _ {t}; \text { and }
$$

$$
R _ {f} = \text { correlation   of } Y _ {s} \text { and } Y _ {f}
$$

The index C is defined as the correlation between the variance not accounted for by the regression model of actual outcomes and the variance not accounted for by the human expert's regression model. The index can also be considered the partial correlation coefficient of $Y_{e}$ and $Y_{s}$ when the linear effects of all the cues are totally removed [20]. This index can take on values between 1.00 and -1.00.

Therefore, the residual index $(C)$ can be used as a general measure of nonlinearity in the decision behavior of a human expert. If either of the residual variances of the two linear regression models is random or there is no systematic relationship between them, the correlation coefficient C approaches zero (insignificant level of nonlinearity). This condition indicates that the decision strategies being used by experts are close to linear and that the decision behavior of a human expert may be modeled well by a linear model.

If the C index shows a positive correlation, there are significant levels of nonlinear components in the decision strategies of the expert. Thus, the expert uses valid nonlinear strategies during his or her decision-making process that cannot be captured by a linear model. In this case, it can be inferred that, if nonlinear algorithms are applied to capture the valid strategies, more accurate decision models can be built.

On the other hand, if C shows a negative correlation, then the nonlinear strategies being used by the experts seem to be diminishing their predictive accuracy.

## Output Analysis

Output analysis is also called bootstrapping, which is the replacement of a decision maker by the simple linear model of his or her judgment $[1, 5, 21]$ . Linear (logistic) regression and discriminant analysis (DA) have been used primarily to build the linear models. Many studies $[3, 13, 37]$ provide evidence on the applicability of bootstrapping, supporting the robustness of the linear models. The results of these studies show that the linear models of human subjects outperform the human subjects in predicting the actual outcomes in the environment.

Other studies, however, have been critical of bootstrapping $[21, 31]$ , claiming that human decision behavior basically follows a nonlinear strategy that can never be modeled well by linear models. Rather, all that the linear models can do is approximate the decision behavior. Einhorn et al. $[10]$ and Larker and Lessig $[18]$ showed in their protocol analysis that human decision making follows nonlinear strategies, although these studies did not exclude the possibility of bootstrapping by linear models.

Libby [21] also argued that, as the quality of human knowledge improves, nonlinearity of human decision behavior becomes obvious and difficult to be modeled by linear models. In other words, if a real expert with a high quality of knowledge is to be modeled by a linear model, the valid nonlinearity of the expert should be approximated. This means that the linear model may not appropriately represent the valid nonlinearity, and its performance (predictive validity) may deteriorate and be worse than the performance of the expert. To support his argument, Libby [21] reviewed the previous studies that reported successful bootstrapping by linear models and found that these studies used novices rather than domain experts as subjects. The novices' knowledge was considered to be more inconsistent and less valid than that of experts.

An interesting issue in decision research is whether, in predicting the actual outcomes, the model of the human expert's judgment would be more valid or less valid than the expert's judgment [20, 21]. To the extent that the model fails to capture the valid nonlinear decision strategy of an expert, it should perform worse than the expert. To the extent that the model eliminates the inconsistency component in the expert decision-making behavior, it should perform better. Therefore, the success of modeling judgment of an expert depends on how well a model can capture the valid nonlinear strategy of the expert.

## Expert Modeling and Inductive Learning

Expert modeling involves the use of various mechanical algorithms to capture human expertise, knowledge, and heuristics. This approach is also called inductive learning or machine learning, since it produces decision rules from the example cases a human expert provides $[25]$ . A number of different inductive learning methods have been developed. Among them, the ID3 and neural network approaches are most popular $[17]$ .

The ID3 method developed by Quinlan [28] is a simple but effective rule-based method for learning by example (LBE). The ID3 approach consists of a procedure for generating an efficient discrimination tree for classifying patterns that have common attributes or features. When it is given a training set of examples, ID3 constructs a decision tree for classifying examples into two classes [26].

The inductive learning method is based on information theory and uses an information-theoretic measure called entropy. Entropy can be defined as the amount of information carried by a message in communication $[32]$ . Based on the entropy concept, information on each attribute (independent variable) is processed sequentially and combined logically (conjunctively or disjunctively) along the decision tree $[11]$ . Therefore, a linear combination of input information and other properties of linear models cannot be expected in the method. Rather, the logical information processing in ID3 seems to be very similar to a nonlinear decision strategy. For this reason, ID3 is considered a typical nonlinear algorithm.

Another inductive learning algorithm is the neural network. A neural network is a dynamic model consisting of nodes, connections between the nodes, and layers associated with each node $[30]$ . There are three types of nodes: input, output, and hidden layer. The input nodes receive input values from sources external to the neural network, the output nodes produce output of the neural network, and the hidden layer nodes serve to detect features, regularities, and generalizations in the data. The hidden layers enable neural networks to perform flexible information processing. This capability guarantees that neural networks can solve nonlinearly separable problems that simple linear problems cannot solve. Therefore, the neural networks are considered a typical nonlinear model $[23]$ . This ability to model nonlinear decision strategy has enabled them to perform successfully in a number of business applications $[34, 36]$ , including stockmarket investments $[24]$ , commercial loan approval $[12]$ , and bankruptcy prediction $[19]$ .

In a comparison of custom-developed neural networks and logistic regression models in a credit union environment, Desai, Crook, and Overstreet [6] found the neural nets better able to classify bad loans correctly. However, when the task involved correct classification of both good and bad loans, the logistic regression model performed in a comparable manner.

Because of their nonlinear processing capability, inductive learning approaches using both ID3 and neural networks are different from linear approaches. In the case of both ID3 and neural networks, it is assumed that the nonlinear information capability can appropriately model the nonlinear decision behavior of a human expert.

## Problems

In spite of the algorithmical difference, the inductive learning algorithms were used to achieve the same goals as bootstrapping by linear models. For that reason, in order to validate models built by inductive learning algorithms, such linear models as linear regression and discriminant analysis were compared as a benchmark.

While the inductive learning algorithms performed well in general $[8, 29, 33]$ , some conflicting results $[4, 7]$ make it difficult to generalize the relative performance of the inductive learning approaches. Moreover, the results of most comparative studies tend to be dependent on the data or task because they simply compare performance of the two approaches without considering other exogenous factors than the algorithms. Thus, the data dependency makes it more difficult to generalize the empirical results.

The study reported here starts from a conjecture that, in comparing performance of models of human judgment, the characteristics of judgment behavior (for example, decision strategy and validity of the human judgment) should be analyzed. Then, the more reliable and generalizable interpretation of the results can be achieved.

## Research Objectives

This study focuses on decision strategy and the validity of human decision-making behavior. More specifically, linear and nonlinear strategies are differentiated and the validity of each strategy is examined. To do this, the C index of lens model analysis is used, which is intended to represent the valid nonlinearity in decision-making behavior.

This study has two main objectives. First, it aims to support the usefulness of the C index in expert modeling by examining the relationship between the C index and the predictive validity of models. A high C index value indicates the existence of valid nonlinearity in decision-making behavior. Since the nonlinearity should be captured more successfully by nonlinear information-processing algorithms, a high C index value should be correlated with the predictive validity of nonlinear algorithms.

Second, this study examines Libby's argument [21] concerning the performance of the model and the human expert: "The more valid (accurate) human subject is modeled, the less bootstrapping by linear models is likely because linear models cannot capture the valid nonlinear decision behavior of the human subject."

Two hypotheses concerned with the objectives are:

1. There is a significant relationship between the C index and the predictive validity of models with nonlinear information-processing capability, but not a significant relationship between the C index and the predictive validity of linear models.

2. There is a significant negative relationship between the predictive validity of the human expert to be modeled and the effect of bootstrapping of linear models. In other words, bootstrapping is not achievable if the human subject is a real expert who has highly accurate predictive validity.

By testing these two hypotheses, we can determine whether bootstrapping by linear models is possible in all situations. Otherwise, the results of this study may support the use of nonlinear algorithms in certain situations.

## Methodology

## Subjects

SUBJECTS CONSISTED OF EIGHT LOAN OFFICERS FROM TWO COMMERCIAL banks, one in California and one in Texas, who were contacted through their senior administrators. Based on predictive validity and reliability, only three of the experts were selected and asked to complete the experiment. The average work experience in their positions was approximately ten years. In addition, a decision scheme was used as the fourth expert, the composite expert. The decisions of the composite expert consisted of the majority decisions among the decisions on each case made by the experts.

The study spanned three months, beginning with interviews of the lending officers.

Each interview was prearranged and was conducted individually in the office of the expert. In the instructions given to the experts, the objective of the experiment was explained as an investigation of the decision strategy in forming decisions about whether a firm would be bankrupt or would default on the payment of its debt within two years from the date on which its financial information was prepared. The experts were informed that (1) all the cases in the sample were real, (2) about half of the firms had actually become bankrupt or defaulted on the payment of the debt, and (3) the cases were presented in a random order. The experts were also informed that all of the financial information was derived from audited financial statements two years before the default or bankruptcy date.

## Data Sets and Firms in the Sample

There were three groups of firms, which were categorized by the size of total assets. In this experiment, the loan amount was determined as about 7 percent of the average total assets in each group. Thus, a situation was created by assuming that each firm requested credit of 7 percent of the average total assets as a commercial loan, and expert loan officers were expected to make a decision, based on the prediction of bankruptcy.

The first group of firms consisted of 55 organizations that had average total assets of about \$344 million. The 55 firms included 28 failed and 27 nonfailed cases. The second group consisted of 60 firms that had average total assets of about \$44 million, with 30 failed and 30 nonfailed cases. In the first and second groups, a firm was classified as “failed” if it experienced bankruptcy or was liquidated for the benefit of creditors within two years of the date of the financial statements.

Data for failed (bankrupt) firms in the first and second groups were chosen from listings in the Wall Street Journal Index for the years 1981–85 and from listings of deleted firms (due to liquidation) in Moody's Industrial Manual. Data for nonfailed firms in the two groups were obtained from the same sources for the same period as that of the corresponding bankrupt firms. These nonfailed firms were comparable with the failed firms in terms of asset size and type of business. The financial information about each firm (case) was gathered from such publicly announced sources as Moody's Industrial Reports and Moody's OTC Manual.

The third group was composed of 59 small business firms that were mostly collected from real loan cases of a large commercial bank in California. The 59 firms included 28 failed and 31 nonfailed cases. In this group, a case was classified as “failed” if the loan case was a rejected case, or initially approved but later evaluated as a bad loan. A case was defined as “nonfailed” if the loan was approved and later evaluated as a good loan.

To distinguish this group from the other two, relatively small loan cases were collected. The average loan amount of \$318,000 was equivalent to 7 percent of the average total assets of firms in this group. This ratio (7 percent) of loan amount to average total assets was comparable with those of the other two groups. In addition, in order to make the third group comparable with the other two, commercial loans with sufficient financial information were collected and all the qualitative data of each loan were ignored.

In this field setting, it was assumed that the size of the total assets reflected the stability and credibility of a firm and indirectly represented a firm's default risk. The default risk as a control variable is appropriate for such a naturalistic setting as bankruptcy prediction. However, the primary purpose of using the control variable is to create different risky situations in which different decision strategies could be triggered in the decision-making behavior of loan officers.

To isolate the possible effect of economic condition from the experiments, this study collected data mostly from the period of 1981 through 1985 because, according to the report of the U.S. Department of Commerce, the economic condition of the period was average. Utilities, transportation, and financial companies were excluded because these companies have different financial structures and environments [16].

## Tasks

Each expert was provided with financial profiles of real but disguised industrial companies. The companies were represented by ten commonly used financial ratios computed from the firms' financial statements. The first five ratios were chosen through a factor analysis $[21]$ ; the remaining five were the most commonly cited ratios for bankruptcy prediction in the risk analysis literature $[16]$ . Selection of the ten ratios (cues) was also approved by the expert lending officers during the first interview. They agreed that the ratios would provide sufficient quantitative information for bankruptcy prediction and would not cause any information overload. In addition, by presenting the financial profiles in ratios rather than real numbers, the research design of the three groups could avoid any possible effects from real numbers.

The experts evaluated the financial profiles of each firm and were asked to judge whether each of the firms in the sample would be able to repay the loan requested or would default. Based on the judgment, each expert made a decision on each case in the sample: approve or reject. This is a binary classification task based on the experts' judgment, typical of a business environment.

To examine the experts' usage of financial ratios in the loan evaluation task, the loan officers were asked to indicate the degree of importance of each ratio after they had made decisions on all the sample cases. Based on the degree (weight), a final set of cues (ratios) was determined for building decision models. These ratios are defined in Table 1.

## Procedure

The study consisted of two steps: (1) examining the experts' decision strategies with the lens model, and (2) building decision models and evaluating model performance in predicting both the decisions of the experts (simulation capability) and the actual outcomes (predictive validity). By uniting the results of these two steps on the same task, the relationships between decision strategy and model performance could be explained.

Table 1 Selection of Financial Ratios (Percentage Weights)

<table><tr><td></td><td>Expert 1</td><td>Expert 2</td><td>Expert 3</td></tr><tr><td>NI/TA</td><td>10</td><td>30</td><td>15</td></tr><tr><td>CA/Sales</td><td>10</td><td>20</td><td>15</td></tr><tr><td>CA/CL</td><td>20</td><td>30</td><td>20</td></tr><tr><td>Cash/TA</td><td>0</td><td>0</td><td>20</td></tr><tr><td>TD/TA</td><td>25</td><td>0</td><td>5</td></tr><tr><td>(CA/CL)/TA</td><td>10</td><td>10</td><td>5</td></tr><tr><td>RE/TA</td><td>25</td><td>10</td><td>20</td></tr><tr><td>Total</td><td>100</td><td>100</td><td>100</td></tr></table>

NI = net income; TA = total assets; CA = current assets; CL = current liability; TD = total debt; RE = retained earnings.

In the first step, the experts were given all of the cases without the actual case outcomes and were asked to provide a decision for each one. In this way, there were two criteria for each case: actual outcomes and the expert's decisions. With the cases, various correlation coefficients between the variables $(Y_{e}, Y_{s}, Y_{t}, \text{and } Y_{f} \text{ in figure 1})$ on both sides of the lens model were computed, showing the valid nonlinear components in the individual decision-making process.

In the second step, decision models using four different algorithms were built and their performance was evaluated in the two modeling situations; (1) simulating the experts' judgment to predict the judgment itself (simulation capability) and (2) modeling the judgment to predict the actual outcomes (predictive validity).

In examining the simulation capability, decision models were evaluated in predicting the same cases used to build them. Hence, decision models should be cross-validated to reduce the biases. In cross-validation, samples were randomly split into a training subset and a validation subset. The training subset was used to develop decision models while the other subset was used to evaluate the predictive validity of developed decision models. However, such a split-sample method has the unfortunate effect of reducing the effective sample size. To increase the sample size, this research used a special type of cross-validation method that applies the bootstrapping concept. In this research, n–10 out of n cases in each group were selected to build decision models, and the ten cases left out were used to test the performance of the models. This process was repeated for each ten cases of n cases until all of the cases in the group had been used as a validation subset. This method achieved a nearly unbiased estimate and maintained a sample size of n for validation.

In examining predictive validity, decision models were built using the judgment as their dependent variable rather than the actual outcomes. Hence, their predictions of the actual outcomes were independent from how they were built, and they did not need to be cross-validated.

## Model Building

To generate rule-based nonlinear decision models, a commercial package (Rule Master) applying the ID3 method $[28]$ was used. For the ID3 method, the financial ratios were transformed into categorical data. The categories (four classes) for the transformation were provided by an expert who showed the best predictive accuracy in loan evaluation. During interviews with the experts, they indicated that they preferred to use categorical data for reasons of simplicity and convenience. Even though the data were provided in the form of raw values, the experts interpreted them in a categorical manner, with the interpretation usually falling into four or five such categories as bad, below average, average, good, and very good.

To generate network-based models, a commercial package (Neural Works Professional II), applying the back-propagation paradigm, was used. The network used in this study was a three-layer configuration with one hidden layer of fourteen processing units. The learning coefficients of the generalized-delta rule were selected (0.9 and 0.6 for learning rate and momentum rate) because they were reported to yield fast learning [30].

Since this study was concerned with binary classification, only a single output processing element was needed. This configuration was applied for constructing all networks. Learning was completed after 100,000 iterations in most networks, but about 400,000 iterations were required in a few nets. The decision was stated as:

Output element > 0.65 → nonfailed (accepted);

Output element < 0.35 → failed (rejected).

If the value of the output element was between 0.35 and 0.65, the decision was considered undefined and considered incorrect.

To construct linear discriminant analysis (DA) models, the seven ratios in a numeric form were used. As in building neural nets, the original numeric data were used without transformation. The DA models were implemented using SAS.

Given that both the response and criterion were dichotomous, SAS, a statistical package that includes the logistic regression method, was used to generate the logistic models. The decision of the logistic model was classified as:

The value of the dependent variable $\geq 0.5 \rightarrow$ accepted;

The value of the dependent variable $<0.5 \rightarrow$ rejected.

## Results

TABLE 2 SUMMARIZES THE PREDICTIVE VALIDITY OF THE EXPERT loan officers. The level of accuracy is about the same as in previous studies. For example, in Libby [21], the accuracy was 74 percent; in Zimmer [37], it was 77 percent. In this study, it was 75 percent.

Table 2 Predictive Validity of Loan Officers (in Percent)

<table><tr><td></td><td>Group 1(n = 55)</td><td>Group 2(n = 60)</td><td>Group 3(n = 59)</td><td>Mean accuracy</td></tr><tr><td>Expert 1</td><td>72.7%</td><td>75.0%</td><td>81.4%</td><td>76.4%</td></tr><tr><td>Expert 2</td><td>72.7</td><td>76.7</td><td>78.0</td><td>75.8</td></tr><tr><td>Expert 3</td><td>65.5</td><td>73.3</td><td>78.0</td><td>72.3</td></tr><tr><td>Expert 4</td><td>78.2</td><td>83.3</td><td>81.4</td><td>81.0</td></tr><tr><td>Mean of experts 1, 2, and 3</td><td>70.3</td><td>75.0</td><td>79.1</td><td></td></tr></table>

## Analysis of Decision Strategy

Table 3 summarizes two key correlation coefficients of the lens model framework. Based on the coefficients in this table, the validity of nonlinear strategy used by each expert is determined.

The C indices show that valid nonlinearity exists in the decision strategies of both expert 2 and expert 4 in group 2, and in the strategies of expert 3 in group 3. In the three cells, the existence of nonlinearity should contribute to the predictive validity of the expert. This result is consistent with the high values of $r_{a}$ in the three cells, which is another indicator of each expert's predictive validity. The fourth expert has the best achievement as shown in Table 2.

In predicting true outcomes, superior performance of nonlinear models of the experts is expected in the three cells, because the valid nonlinearity strategy should be better captured by nonlinear models. Later it will be examined by analyzing correlation between the C index and performance of each decision model.

On the other hand, negative C index values can be interpreted to mean that use of the nonlinear strategies by the experts deteriorates their predictive validity. Relatively better performance of linear models is expected where the C index has a negative value.

## Simulation Capability of the Models

This section describes a prediction situation in which the decisions of each expert are modeled and the same decisions are used as a criterion to validate the simulation capability of each model. Table 4 summarizes the mean accuracy of each model in simulating the decisions of the experts in each group.

The independent test using chi-square statistics and hit ratio showed that all of the decisions were generally well simulated by the four algorithms. The chi-square measures indicated the presence of structural dependency between the expert and the model decisions.

The relatively poor performance of ID3 in the two experiments was due to the undefined decision problem. This problem occurs when ID3 decision rules face a case that does not exist in the training set used in generating the decision rules. In such a case, the rules generate the undefined decision, which is counted as an incorrect prediction. In this study, since data were cross-validated and the training sample size was small (n = 50), this problem was unavoidable. The number of undefined cases was averaged at 4.4 out of 60 cases in each experiment (7.3 percent loss in simulation accuracy in percentage).

Table 3 A Summary of Lens Analysis

<table><tr><td rowspan="2"></td><td colspan="2">Group 1</td><td colspan="2">Group 2</td><td colspan="2">Group 3</td></tr><tr><td> $R_a$ </td><td>C index (test-stat.)</td><td> $R_a$ </td><td>C index (test-stat.)</td><td> $R_a$ </td><td>C index (test-stat.)</td></tr><tr><td>Expert 1</td><td>0.467</td><td>-0.057 (-0.424)</td><td>0.5</td><td>0.212 (1.642)</td><td>0.627</td><td>0 (0)</td></tr><tr><td>Expert 2</td><td>0.467</td><td>0.066 (0.486)</td><td>0.582</td><td>** 0.363 (2.814)</td><td>0.57</td><td>0.207 (1.588)</td></tr><tr><td>Expert 3</td><td>0.331</td><td>-0.108 (-0.802)</td><td>0.495</td><td>-0.002 (-0.02)</td><td>0.559</td><td>** 0.282 (2.169)</td></tr><tr><td>Expert 4</td><td>0.491</td><td>0.128 (0.95)</td><td>0.7</td><td>** 0.352 (2.726)</td><td>0.631</td><td>0 (0)</td></tr></table>

\*\* Phi test statistics: $P_{\text{critical at 0.05}} = 1.96$ .

Table 4 Simulation Capability

<table><tr><td></td><td>Logistic regression</td><td>Discriminant analysis</td><td>ID3</td><td>Neural networks</td></tr><tr><td>Group 1</td><td>70.0%</td><td>79.1%</td><td>67.3%</td><td>79.1%</td></tr><tr><td>Group 2</td><td>70.0</td><td>71.7</td><td>69.1</td><td>76.3</td></tr><tr><td>Group 3</td><td>77.6</td><td>80.1</td><td>69.1</td><td>81.0</td></tr><tr><td>Mean</td><td>72.5</td><td>77.0</td><td>68.5</td><td>78.7</td></tr></table>

However, the undefined decision problem of ID3 did not occur in evaluating predictive validity because all the sample cases were defined in the training set. This effect might enable ID3 to regain its predictive validity. Therefore, all of the models are considered appropriate for further analysis of predictive validity.

## Predictive Validity

Predictive validity is measured by evaluating model performance in modeling the decisions of experts and then predicting the actual outcomes. As in the previous studies, the following measurements are made: (1) the expert's validity: the number (in percent) of correct predictions of the actual outcomes made by the expert; (2) the validity of the model of the expert: the number (in percent) of correct predictions of the actual outcomes made by the model of the expert; and (3) the incremental validity of the model of the expert over the expert's decision itself: the validity of the model of the expert minus the validity of the expert (this validity is summarized in Table 5).

Table 5 Predictive Validity of Experts and Models of Experts

<table><tr><td></td><td>Predictive validity</td><td>Rank in predictive validity</td><td>Simulation accuracy</td></tr><tr><td>Most accurate expert</td><td>81.0%</td><td>(1)</td><td>—</td></tr><tr><td rowspan="2">Linear models of most accurate expert</td><td>LR model: 78.6%</td><td>(4)</td><td>LR model: 73.5%</td></tr><tr><td>DA model: 77.5%</td><td>(5)</td><td>DA model: 78.1%</td></tr><tr><td rowspan="2">Nonlinear models of most accurate expert</td><td>ID3 model: 80.9%</td><td>(2)</td><td>ID3 model: 70.1%</td></tr><tr><td>NN model: 80.4%</td><td>(3)</td><td>NN model: 76.5%</td></tr><tr><td>Experts&#x27; average</td><td>76.3%</td><td>(9)</td><td>—</td></tr><tr><td>LR models&#x27; average</td><td>76.5%</td><td>(7)</td><td>72.5%</td></tr><tr><td>DA models&#x27; average</td><td>74.8%</td><td>(10)</td><td>77.0%</td></tr><tr><td>ID3 models&#x27; average</td><td>76.4%</td><td>(8)</td><td>68.5%</td></tr><tr><td>NN models&#x27; average</td><td>76.9%</td><td>(6)</td><td>78.7%</td></tr></table>

LR = logistic regression; DA = discriminant analysis; NN = neural network.

In general, all the models generated by the four algorithms predicted the actual outcomes quite well. In the previous studies $[5]$ , the validity of the linear models proved higher than that of the human judge in most cases. However, in the present study there was no significant difference in mean validity between the human experts and the linear models, or between linear models and nonlinear models. Human experts slightly outperformed DA models.

When the most accurate expert was modeled, bootstrapping was not achieved because the two linear models were surpassed in predictive validity by the expert. The two nonlinear models of the most accurate expert performed better than linear models of the expert.

To shed light on this analysis, two lens model components and validity of models in the twelve experiments were combined to compute correlations among the variables. The variables were: (1) validity of the expert at each experiment (VE), (2) correlation between the decisions of experts and the actual outcomes ( $r_{a}$ ), (3) residual correlation as an index of valid nonlinearity (C), (4) validity of logistic regression (VLR), (5) validity of discriminant analysis (VDA), (6) validity of ID3 (VID3), (7) validity of neural network (VNN), (8) incremental validity of logistic regression over the validity of an expert (INVLR) (computed by subtracting the validity of an expert from the validity of the model of the expert), (9) incremental validity of discriminant analysis over the validity of an expert (INVDA), (10) incremental validity of ID3 (INVID3) over the validity of an expert, and (11) incremental validity of neural network over the validity of an expert (INVNN). The correlations among the eleven variables are presented in Table 6.

The significant correlations at the 0.05 or 0.1 significance level) were (a) between

Table 6 A Summary of Correlation Coefficients

<table><tr><td></td><td>(1) VE (validity of expert)</td><td> $r_a$ </td><td>C</td></tr><tr><td>(2)  $r_a$ </td><td>0.9538* (&lt;0.001)</td><td>1</td><td>0.5653 (0.055)</td></tr><tr><td>(3) C</td><td>0.5160**(0.085)</td><td>0.5653**(0.055)</td><td>1</td></tr><tr><td>(4) VLR</td><td>0.7856* (0.002)</td><td>0.8100* (0.001)</td><td>0.4245 (0.169)</td></tr><tr><td>(5) VDA</td><td>0.7619* (0.004)</td><td>0.7789* (0.002)</td><td>0.3385 (0.281)</td></tr><tr><td>(6) VID3</td><td>0.9499* (&lt;0.001)</td><td>0.9056*(&lt;0.001)</td><td>0.5374**(0.071)</td></tr><tr><td>(7) VNN</td><td>0.8518* (&lt;0.001)</td><td>0.8750*(&lt;0.001)</td><td>0.6271*(0.029)</td></tr><tr><td>(8) INVLR</td><td>-0.6516* (0.021)</td><td>—</td><td>—</td></tr><tr><td>(9) INVDA</td><td>-0.4901**(0.100)</td><td>—</td><td>—</td></tr><tr><td>(10)INVID3</td><td>-0.3571 (0.250)</td><td>—</td><td>—</td></tr><tr><td>(11) INVNN</td><td>-0.3201 (0.310)</td><td>—</td><td>—</td></tr></table>

\* Critical value: $|r| = 0.58$ at 0.05 level and $n = 12$ .  
\*\* Critical value: $|r| = 0.50$ at 0.1 level and $n = 12$ .

VE (validity of expert) and $r_{a}$ , (b) between VE and validity of all four algorithms (logistic regression, discriminant analysis, ID3, and neural network), (c) between $r_{a}$ and validity of all four algorithms, (d) between the C index (residual correlation) and validity of nonlinear models (ID3 and neural network), and (e) between VE and incremental validity of linear models (logistic regression and discriminant analysis).

Correlation (a) $(r=0.9538)$ implies that $r_{a}$ (achievement index) is a reliable indicator of the validity of the expert. Correlations (b) $(r=0.7856, 0.7619, 0.9499, 0.8518)$ and (c) $(r=0.81, 0.7789, 0.9056, 0.875)$ show that model validity is significantly dependent on expert validity. Since the models are approximations of the decisions of experts, it is not surprising that the validity of models and the validity of experts are closely correlated. The results suggest that the better the quality of expertise modeled, the more accurate the models become. Especially for the ID3 algorithm, the validity of experts is crucial for model performance $(r=0.9499)$ .

Significant correlations (d) $r = 0.5374, 0.6271$ also indicate that valid nonlinearity (measured as C) can be well modeled by the neural network and ID3. Correlation between C and validity of ID3 approach the critical value $r = 0.5374, p = 0.071$ . These results imply that, when valid nonlinear strategies are modeled, model performance improves with the employment of such nonlinear models as ID3 or the neural network. The C index also proves quite useful in determining valid nonlinearity in decision behavior.

Finally, significant negative correlations (e) $r = -0.6516, -0.4901$ between incremental validity of linear models (LR and DA) and VE (expert's validity) imply that, as the expert's validity increases, linear models are less likely to outperform the experts. In other words, bootstrapping using logistic regression or discriminant analysis would be less achievable. This result supports the early argument of Libby [21] that pointed out the limitation of linear models in expert modeling. Bootstrapping by nonlinear algorithms may be achievable only when valid nonlinear strategy (indicated by a high $C$ index) dominates the expert's decision behavior.

Negative correlations between incremental validity of all models and VE showed the limitation of using a modeling algorithm, especially linear algorithms, in modeling expert decision making. When a true expert is to be modeled, the advantage of using a modeling algorithm decreases, and inductive modeling should be carried out with caution. The negative correlations also showed the risk of separating the analysis of decision-making behavior of an expert from modeling the expert. They necessitate a more comprehensive use of multiple methodologies in expert modeling that include process tracing of decision behavior as well as a variety of decision analysis techniques.

## Discussion

The major finding of this study centers on the significant negative correlation between the validity of the expert and the incremental validity of the linear models (logistic regression and discriminant analysis). The negative correlation could present a possible explanation for the conflicting results concerning bootstrapping by linear models. The negative correlation supports Libby's argument [21] that, as the expert validity increases, the advantage of using linear models decreases. This finding implies that, if the subjects are not domain experts, bootstrapping can improve the performance of models over nonexpert subjects by getting rid of inconsistency in human decision-making behavior.

The second finding concerns the significant correlations between the valid nonlinear index (C) and the validity of two nonlinear algorithms: the neural network $r=0.6271, p<0.029$ and ID3 $r=0.5374, p<0.071$ . The significant correlations support the use of nonlinear algorithms to capture the valid nonlinear strategy as a means of improving predictive validity of the model. This finding implies that the valid nonlinear index (C) can be useful as an indicator of the limitations of linear algorithms as well as of the feasibility of using nonlinear algorithms.

In comparing the two linear algorithms, the LR models performed almost as well as DA models. Statistically, the difference between the two is insignificant. This result is consistent with a previous comparative study by Harrell and Lee [15].

## Conclusion

THE RESULTS OF THIS STUDY BROUGHT AN IMPORTANT CONCEPT, the validity of decision strategy, to expert modeling. The inclusion of the new concept, when combined with characteristics of modeling algorithms, offers a clear explanation of why a certain algorithm performs better than another. Therefore, the contingent relationship among validity of decision strategy, modeling algorithm, and model performance will be useful for further refinements of future expert-modeling research.

However, two limitations of the study design should be noted. First, the study greatly simplified the task of bankruptcy prediction by using only ten financial ratios. Also, it did not include such qualitative variables as management reputation. In reality, such qualitative information can play a major role. Second, the evaluation of the case examples by the experts was extremely time-consuming, limiting the number of experts who participated. This limitation constrains the generalizability of the results. In order to overcome these limitations, future studies should include qualitative variables and a large number of experts.

In modeling human experts, many factors must be considered. Previous studies using process-tracing approaches identified task characteristics, modeling situations, and individual difference as key factors $[9, 17, 27]$ . For further research, it may prove worthwhile to expand the contingent relationship to a framework that will be able to explain the relationships between model performance and these key factors.

Acknowledgments: The authors wish to acknowledge the financial support of the Korea Research Foundation made in the 1997 program year, and to thank the reviewers and also Professor William Stein of Texas A&M University for their suggestions and assistance in preparing the final manuscript.

## REFERENCES

1. Bowman, E.H. Consistency and optimality in managerial decision making. Management Science, 9 (1963), 310–321.

2. Brunswick, E. The Conceptual Framework of Psychology. Chicago: University of Chicago Press, 1952.

3. Casey, C.J. Prior probability disclosure and loan officers' judgments: some evidence of the impact. Journal of Accounting Research, 21, 1 (1983), 300–307.

4. Chung, H.M., and Silver, M.S. Rule-based expert systems and linear models: an empirical comparison of learning-by-examples methods. Decision Sciences, 23, 3 (1992), 687–707.

5. Dawes R., and Corrigan, B. Linear models in decision making. Psychological Bulletin, 81, 2 (1974), 95–106.

6. Desai, V.S.; Crook, J.N.; and Overstreet, Jr., G.A. A comparison of neural networks and linear scoring models in the credit union environment. European Journal of Operational Research, 95, 1 (1996), 24–37.

7. Duliba, K. Contrasting neural nets with regression in predicting performance in the transportation industry. Proceedings of the Twenty-Fourth Hawaii International Conference on System Sciences, 1991, pp. 163–170.

8. Dutta, S., and Shekhar, S. Bond ratings: a non-conservative application of neural networks. Proceedings of the Second International Conference on Neural Networks, vol. 2, 1988, pp. 443–450.

9. Einhorn, H. Expert measurement and mechanical combination. Organizational Behavior Human Performance, 20, 2 (1972), 86–96.

10. Einhorn, H.; Kleimuntz, D.; and Kleimuntz, B. Linear regression and process-tracing models of judgment. Psychological Review, 86, 5 (1979), 465–485.

11. Fisher, D.H., and McKusick, K.B. An empirical comparison of ID3 and back-propagation. Technical Report CS-88-14, Department of Computer Science, Vanderbilt University, 1989.

12. Glorfeld, L.W., and Hardgrave, B.C. An improved method for developing neural networks: the case of evaluating commercial loan creditworthiness. Computers and Operations Research, 23, 10 (1996), 933–944.

13. Goldberg, L.R. Man versus model of man: just how conflicting is that evidence? Organizational Behavior Human Performance, 16, 1 (1976), 13–22.

14. Hammond, K.; Hursch, C.; and Todd, F. Analyzing the components of clinical inference. Psychological Review, 71, 6 (1964), 438–456.

15. Harrell, Jr., F.E., and Lee, K.L. A comparison of the discrimination of discriminant analysis and logistic regression under multivariate normality. In P.K. Sen (ed.), Biostatistics: Statistics in Biomedical, Public Health and Environmental Sciences. Amsterdam: North-Holland, 1985, pp. 333–343.

16. Harris, C.R. An expert decision support system for auditor going concern evaluation. Ph.D. dissertation, University of Texas, Arlington, 1989.

17. Kim, C.N. Modeling expert decision making in bankruptcy prediction: a decision strategy perspective. Ph.D. dissertation, Texas A&M University, 1992.

18. Larker, D., and Lessig, P. An examination of the linear and retrospective process tracing approaches to judgment modeling. Accounting Review, 58, 1 (1983), 58–89.

19. Lee, K.C.; Han, I.; and Kwon, Y. Hybrid neural network models for bankruptcy predictions. Decision Support Systems, 18, 1 (1996), 63–72.

20. Levi, K. Expert systems should be more accurate than human experts. IEEE Transactions on Systems, Man, and Cybernetics, 19, 3 (1989), 647–657.

21. Libby, R. Man versus model of man: some conflicting evidence. Organizational Behavior Human Performance, 16, 1 (1976), 1–12.

22. Libby, R. Accounting and Human Information Processing: Theory and Applications. Englewood Cliffs, NJ: Prentice-Hall, 1981.

23. Lippmann, R. An introduction to computing with neural nets. IEEE ASSP Magazine, 4, 2 (1987), 4–22.

24. Longo, J.M., and Long, M.S. Using neural networks to differentiate between winner and loser stocks. Journal of Financial Statement Analysis, 2, 2 (1997), 5–15.

25. Michalski, R. A theory and methodology of inductive learning. In R. Michalski, J. Carbonell, and T. Mitchell (eds.), Machine Learning: An Artificial Intelligence Approach. Palo Alto, CA: Tioga, 1983, pp. 83–134.

26. Michie, D. Current developments in expert systems, In J. Quinlan (ed.), Applications of Expert Systems. New York: Addison-Wesley, 1987, pp. 137–156.

27. Olshavsky, R.W. Task complexity and contingent processing in decision making: a replication and extension. Organizational Behavior Human Performance, 24, 3 (1979), 300–316.

28. Quinlan, J. Discovering rules by induction from large collections of examples. In D. Michie (ed.), Expert Systems in the Microelectronic Age. Edinburgh: Edinburgh University Press, 1979, pp. 169–201.

29. Raghupathi, W.; Schkade, L.; and Raju, B. A neural network application for bankruptcy prediction. Proceedings of the Twenty-Fourth Hawaii International Conference on System Sciences, 1991, pp. 147–155.

30. Rumelhart, D.; Hinton, G.; and Williams, R. Learning internal representations by error propagation. In D. Rumelhart and J. McClelland (eds.), Parallel Distributed Processing Explorations in the Microstructure of Cognition, vol. 1, Foundations. Cambridge, MA: MIT Press, 1986, pp. 318–362.

31. Schepanski, A. Tests of theories of information processing behavior in credit judgment. Accounting Review, 58, 3 (1983), 581–599.

32. Shannon C. A mathematical theory of communications. Bell Systems Technical Journal, 27 (1948), 379–423.

33. Tam, K.Y., and Kiang, M. Managerial applications of neural networks: the case of bank failure predictions. Management Science, 38, 7 (1992), 926–947.

34. Tauhert, C. Neural networks: not just a black box. Insurance and Technology, 22, 4 (1997), 30–32.

35. Tucker, L.R. A suggested alternative formulation in the development of Hursch, Hammond, and Hursch, and by Hammond, Hursch, and Todd. Psychological Review, 71, 6 (1964), 458–530.

36. Wong, B.K.; Bodnovich, T.A.; and Selvi, Y. Neural network applications in business: a review and analysis of the literature. Decision Support Systems, 19, 4 (1997), 301–320.

37. Zimmer, I. A lens study of the prediction of corporate failure by bank loan officers. Journal of Accounting Research, 18, 2 (1980), 629–636.

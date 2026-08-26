---
otero_id: 10030
otero_key: "ZZE9FFGW"
title: "Predicting going concern opinion with data mining"
authors: "David Martens; Liesbeth Bruynseels; Bart Baesens; Marleen Willekens; Jan Vanthienen"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.01.003"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Predicting going concern opinion with data mining

David Martens <sup>a,⁎</sup>, Liesbeth Bruynseels <sup>b</sup>, Bart Baesens a,c Marleen Willekens <sup>b,d</sup>, Jan Vanthienen <sup>a</sup>

<sup>a</sup> Department of Decision Sciences and Information Management, K.U. Leuven, Belgium <sup>b</sup> Department of Accountancy, K.U.Leuven, Belgium

<sup>c</sup> School of Management, University of Southampton, United Kingdom <sup>d</sup> Department of Accountancy, Tilburg University, The Netherlands

Received 16 February 2007; received in revised form 22 January 2008; accepted 24 January 2008 Available online 4 February 2008

## Abstract

The auditor is required to evaluate whether substantial doubt exists about the client entity's ability to continue as a going concern. Accounting debacles in recent years have shown the importance of proper and thorough audit analysis. Since the 80s, many studies have applied statistical techniques, mainly logistic regression, as an automated tool to guide the going concern opinion formulation. In this paper, we introduce more advanced data mining techniques, such as support vector machines and rulebased classifiers, and empirically investigate the ongoing discussion concerning the sampling methodology. To provide specific audit guidelines, we infer rules with the state-of-the-art classification technique AntMiner+, which are subsequently converted into a decision table allowing for truly easy and user-friendly consultation in every day audit business practices. © 2008 Elsevier B.V. All rights reserved.

Keywords: Going concern opinion; Audit; Data mining; Classification

## 1. Introduction

Statement on Auditing Standards (SAS) No. 59 [1] requires that on every audit the auditor evaluates whether substantial doubt exists about the client entity's ability to continue as a going concern. In particular, the auditor has to assess the client's going concern status for a reasonable period of time, not to exceed one year beyond the date of the financial statements being audited. Relevant information with respect to the continuation of an entity as a going concern is generally obtained from the application of auditing procedures that are planned and performed to achieve audit objectives. Examples of conditions and events that cast doubt on the entity's ability to survive include negative financial trends, defaults on loans or similar agreements, and nonfinancial internal and external matters such as work stoppages or substantial dependence on the success of a particular project. When the identified conditions and events in the aggregate lead to substantial doubt about the continued existence of the entity as a going concern, the auditor should identify and evaluate management's plans to mitigate the effects of these adverse conditions or events. If the auditor believes that there exist management plans that overcome this substantial doubt, a going concern audit report is not required. However, if the auditor decides that substantial doubt exists, the audit report should be modified by adding an explanatory paragraph following the opinion paragraph.

Although the assessment of a company's viability is not the main objective of an audit, bankruptcies without a prior going concern report are often viewed by the public as audit reporting failures [35,13,22]. The high frequency of this type of audit reporting failures is indicative of the fact that the auditor's going concern decision is highly complicated and involves a high level of judgment.

The complexity of the going concern decision has prompted the development of numerous models to predict the issuance of a going concern opinion (see, for example, [37,30,17,36,6]). The focus of these studies has been the development of going concern prediction models, proposing a variety of financial and non-financial variables that might be indicative of the auditor's going concern decision.

Most of these prediction models were developed using regression analysis, a technique which is well suited for investigating the determinants of going concern decisionmaking but less appropriate for developing user-friendly going concern decision models that can be used in everyday auditing. In this paper, we address this gap in the going concern literature by building a comprehensible rule-based classification model which allows for easy consultation by auditors to assess their client's viability. The classification model developed in this study is particularly useful to auditors to screen potential clients or as a decision aid to identify severely distressed clients that might require further consideration. Moreover, auditors may use this model in the final stages of the audit engagement as a quality control device or as a benchmark to represent auditor judgment under similar circumstances.

Furthermore, we will address the appropriateness of the methodology of recent going concern research. In particular, we will evaluate the performance of various data mining techniques including logistic regression and the rule-based classification technique used in this study. In addition, we will examine empirically potential estimation biases induced by the choice-based sampling methodology used in recent going concern research. We compare estimation results from a “complete data” sample with estimation results from choice-based sampling techniques currently used in going concern research. In sum, we contribute to existing going concern research by (a) developing a practical and user-friendly going concern decision-aid for audit practitioners and (b) critically reviewing the methodology of recent going concern research.

## 2. Predicting the going concern opinion

In this section, we provide an overview of some relevant prior studies that have investigated the auditor's going concern judgment. Most of these studies investigated the influence of the quantifiable and nonquantifiable factors identified by SAS No. 34 and SAS No.59 on the issuance of a qualified opinion (e.g. [37,17,13,25,5,20]). An overview of related papers is shown in Table 1, where the columns describe the sampling technique and methodology used.

Of the included companies, a distinction is made between companies that received a going concern opinion, and companies that did not receive a going concern opinion. The latter category can be divided further into healthy and distressed companies, where a distressed company is defined as a company fulfilling at least two of the following six conditions [38,13]:

(1) Negative retained earnings

(2) Negative operating income

(3) Negative net income

(4) Negative working capital

(5) Negative net worth

(6) Negative cash flows

Note that some studies (such as [17] and [20]) make a distinction between companies that received a qualified and a clean opinion, which is closely related to the going concern opinion.

The sampling technique is categorized as matched, balanced or other. With a matched sample, as many nongoing concern companies are chosen as there are companies with a going concern opinion. For each company that was issued a going concern opinion, a nongoing concern opinion company is chosen from the set of distressed companies that is as similar as possible (e.g. same sector, opinion being issued in the same year, total assets as close as possible). For a balanced sample the number of going concern and non-going concern opinion companies is equal as well, but the non-going concern opinion companies are chosen randomly among all available companies. The final other sample encompasses following sampling methodologies:

• A selection of bankrupt companies is made, since these should have been issued a going-concern opinion. The aim is to describe why certain bankrupt companies are issued a going-concern opinion, while others are not. This sampling is used in the study by [36].

Table 1  
Literature table of previous studies on going concern opinion prediction

<table><tr><td>Study</td><td>Sample</td><td>Technique</td><td>Sampling</td></tr><tr><td>Mutchler (1985) [37]</td><td>Going concern: 119Distressed: 119</td><td>MDA</td><td>Balanced</td></tr><tr><td>Levitan and Knoblett (1985) [31]</td><td>Going concern: 32Non-going concern: 32</td><td>MDA</td><td>Matched</td></tr><tr><td>Menon and Schwartz (1987) [37]</td><td>Bankrupt: 89Going concern: 37Non-going concern: 52</td><td>Logit</td><td>Other</td></tr><tr><td>Dopuch et al. (1987) [17]</td><td>Qualified: 275Non-qualified: 411</td><td>Probit</td><td>Other</td></tr><tr><td>Mutchler and Williams (1990) [38]</td><td>Going concern: 87Distressed: 612Healthy: 1171</td><td>Logit</td><td>Other</td></tr><tr><td>Bell and Tabor (1991) [6]</td><td>Qualified: 131 non-Qualified: 1217</td><td>Logit</td><td>Other</td></tr><tr><td>Chen and Church (1992) [13]</td><td>Going concern: 127Distressed: 127</td><td>Logit</td><td>Matched</td></tr><tr><td>Hopwood et al. (1994) [28]</td><td>Bankrupt: 134Distressed: 80Healthy: 80</td><td>Logit</td><td>Other</td></tr><tr><td>Carcello et al. (1995) [8]</td><td>Bankrupt: 446Going concern: 231Non-going concern: 215</td><td>Logit</td><td>Other</td></tr><tr><td>Raghunandan and Rama (1995) [45]</td><td>Bankrupt: 175Going concern: 90Non-going concern: 85Non-bankrupt: 362Going concern: 105Non-going concern: 257</td><td>Logit</td><td>Other</td></tr><tr><td>Mutchler et al. (1997) [39]</td><td>Bankrupt: 208Going concern: 107Non-going concern: 101</td><td>Logit</td><td>Other</td></tr><tr><td>Carcello et al. (2000) [9]</td><td>Going concern: 52Distressed: 264</td><td>Logit</td><td>Other</td></tr><tr><td>Carcello and Neal (2000) [10]</td><td>Going concern: 83Distressed: 140</td><td>Logit</td><td>Balanced</td></tr><tr><td>Reynolds and Francis (2000) [46]</td><td>Going concern: 224Distressed: 2215</td><td>Logit</td><td>Balanced</td></tr><tr><td>Geiger and Raghunandan (2001) [21]</td><td>Bankrupt: 365Going concern: 198Non-going concern: 167</td><td>Logit</td><td>Other</td></tr><tr><td>Behn et al. (2001) [5]</td><td>Going concern: 148Distressed: 148</td><td>Logit</td><td>Matched</td></tr><tr><td>Geiger and Raghunandan (2002) [22]</td><td>Bankrupt: 117Going concern: 59Non-going concern: 56</td><td>Logit</td><td>Other</td></tr><tr><td>DeFond et al. (2002) [16]</td><td>Going concern: 96Distressed: 1158</td><td>Logit</td><td>Other</td></tr><tr><td>Geiger and Rama (2003) [23]</td><td>Going concern: 66Distressed: 66</td><td>Logit</td><td>Matched</td></tr><tr><td>Gaeremynck and Willekens (2003) [20]</td><td>Terminated firms: 114Continued firms: 114</td><td>Logit</td><td>Matched</td></tr></table>

Table 1 (continued)

<table><tr><td>Study</td><td>Sample</td><td>Technique</td><td>Sampling</td></tr><tr><td>Geiger et al. (2005) [24]</td><td>Bankrupt: 226Going concern: 121Non-going concern: 105</td><td>Logit</td><td>Other</td></tr><tr><td>Carey and Simnett (2006) [11]</td><td>Going concern: 66Distressed: 493</td><td>Logit</td><td>Other</td></tr></table>

• All available companies (both going-concern as nongoing concern) are included in the sample, which can be described as a complete sample. Such a sample is used in [38,6].

• A sample similar to balanced sample as the non-going concern opinions are randomly chosen, but the number of non-going concern opinion companies is not equal to the number of going-concern opinion companies, and in that sense is not balanced (e.g. [17,28]).

The first going concern studies used multiple discriminant analysis (MDA) to develop models explaining going concern judgment [37,30]. Subsequent research regarding going concern decision-making mainly used logistic regression (logit) to test going concern predictor variables (see, for example, [36,6,13,45,39,21,5,20]).

With respect to the latter, we document a wide variety of sample selection methodologies used in prior going concern research. Early going concern research (see, for example, [30,17,6]) was mainly conducted on mixed samples of distressed and healthy companies.

From the early nineties onwards, going concern research included only distressed companies (see, for example, [13,45,39,5,23,20]). This is based on research by [28] which suggests that investigations of auditors' going concern opinion decisions should be conducted on samples that have been partitioned into stressed and nonstressed categories because auditors' decision problem is inherently different for stressed and non-stressed companies. As stated in SAS No. 59, auditors first identify a company as experiencing financial or other problems before considering issuing a going concern opinion. From this point of view, it seems perfectly defendable to restrict the sample to distressed companies.

A final issue related to going concern research sampling which received a lot of attention lately is the appropriateness of using a matched sample design.

A matched sample design has been used frequently in previous going concern research, especially when the

research design necessitated manual data collection (see, for example, [5,23,20]). One of the main advantages of the matched sampling technique is that it reduces data collection costs because going concern qualifications occur infrequently in the population and a random sample would produce relatively imprecise parameter estimates unless extremely large samples were used [17]. However, this sampling approach is currently being questioned because of potential estimation biases resulting from choice-based sampling, which is a nonrandom sample where the probability of an observation entering the sample depends on the value (e.g., firms entering bankruptcy or receiving a qualified audit opinion) of the dependent variable. This bias is due to the fact that these datasets generally oversample the proportion of going concern companies, which may potentially bias the regression coefficients and result in predictions that over-estimate the proportion of going concern firms. However, according to [31], the use of logistic regression analysis neutralizes potential problems resulting from this oversampling of going concern companies. In this paper, we contribute to this debate by empirically investigating potential biases induced by the matched sampling approach and comparing prediction accuracy across sampling techniques.

As Table 1 clearly indicates, past research was largely focused on the logistic regression method. An introduction of more advanced data mining models to this domain imposes itself, and will be addressed in the next sections.

## 3. Inferring rules for going concern opinion prediction

## 3.1. Data mining

Over the past decades we have witnessed an explosion of data. Although much information is available in this data, it is hidden in the vast collection of raw data. Data mining entails the overall process of extracting knowledge from this data.

Different types of data mining are discussed in the literature (see a.o. [2]), such as regression, classification and clustering. The task of interest here is classification, which is the task of assigning a data point to a predefined class or group according to its predictive characteristics. The result of a classification technique is a model which makes it possible to classify future data points based on a set of specific characteristics in an automated way, as described in a simplified audit example in Fig. 1. In the literature, there is a myriad of different techniques proposed for this classification task, some of the most commonly used being C4.5, logistic regression, linear and quadratic discriminant analysis, k-nearest neighbor, Artificial Neural Networks (ANN) and Support Vector Machines (SVM) [2,26].

![](/api/attachments/ZZE9FFGW/fulltext/images/60cf72f61d4bc7a347a902024b2fc64b192fcbdda146a596937d7cfddf62792a.jpg)  
Fig. 1. Building classification models with data mining.

Classification techniques are often applied for credit scoring [3,4,49,51], medical diagnostic, such as for the prediction of dementia [42], classifying a breast mass as benign or malignant and selecting the best in-vitro fertilized embryo [41]. Many other data mining applications have been put forward recently, such as the use of data mining for bio-informatics [29], marketing [43] and election campaigns [27] and counter-terrorism [47].

The generated classification model has to fulfill several requirements in order to be acceptable for implementation. Accuracy is the most straightforward performance requirement for classification models, but comprehensibility of the generated model is of key importance as well in domains as credit scoring and medical diagnosis. Justifiability concerns the extent to which the induced model is in line with existing domain knowledge, and is crucial as well. As the ant-based classification technique, AntMiner+, is able to generate such accurate, comprehensible and justifiable classification models [32–34], this technique is used to induce a model predicting going concern opinion. A short overview of this data mining technique follows next.

## 3.2. AntMiner+

We made use of a data mining technique to build a classification model to distinguish the companies with going concern opinion from the ones without going concern opinion. The technique used, AntMiner+, is based on artificial ant systems and builds rule sets with proven predictive capabilities [14,32]. We will first shortly discuss the artificial ant systems, followed by a brief overview of the AntMiner+ technique.

## 3.2.1. Ant colony optimization

Artificial ant systems are inspired on the behavior of real ant colonies and are part of a relatively new concept in artificial intelligence, called swarm intelligence [7]. Swarm Intelligence is the property of a system whereby the collective behaviors of simple agents interacting locally with their environment cause coherent functional global patterns to emerge. A biological ant is a simple insect with limited capabilities but an ant colony is able to behave in complex manners and come to intelligent solutions for problems such as the transportation of heavy items and finding the shortest path between the food source and the nest. This complex behavior emerges from self-organization and indirect communication between the ants. The indirect way of communication, through the environment rather than directly between the individuals, is also known as stigmergy [48]. More specifically, ants communicate through a chemical substance called pheromone that each ant drops on its path. When an ant finds a pheromone trail it is likely to follow this path and reinforce the pheromone. The pheromone trail intensity is increased and the path will become more likely to be followed by other ants. In turn, when no ants follow the same path the pheromone trail intensity decreases, this process is called evaporation.

These principles are illustrated in Fig. 2. Two ants start from their nest (left) and looking for the shortest path to a food source (right). Initially no pheromone is present on either trails, so there is a 50–50 chance of choosing either of the two possible paths. Suppose one ant chooses the lower trail, and the other one the upper trail. The ant that has chosen the lower (shorter) trail will have returned faster to the nest, resulting in twice as many pheromone on the lower trail as on the upper one, as seen in the right part of Fig. 2. As a result, the probability that the next ant will choose the lower, shorter trail will be twice as high, resulting in more pheromone and thus more ants that will choose this trail, until eventually (almost) all ants will follow the shorter path.

![](/api/attachments/ZZE9FFGW/fulltext/images/c4cd89e9e952675622ea48cdb715197ff2b4e37dfa063970f214c33f2533754b.jpg)  
Fig. 2. Path selection through indirect communication.

These principles have been applied to create multiagent systems, mimicking their biological counterparts. This approach has shown to be a viable method for attacking hard combinatorial optimization problems, like the Traveling Salesman Problem [18], routing packages through the Internet [12] and Traffic Light Control [40]. Next follows a brief discussion of the principles and workings of AntMiner+.

## 3.2.2. AntMiner+

First of all, an environment needs to be defined in which the ants operate. When an ant moves through the environment from Start to Stop vertex, it should incrementally construct a solution to the problem at hand, in this case the classification problem. In order to build a set of classification rules, we define the construction graph in such a way that each ant's path will implicitly describe a classification rule. For each variable $V _ { i }$ a vertex $\nu _ { i , j }$ is created for each of its values ${ \mathrm { V a l u e } } _ { i , j } .$ The set of vertices for one variable is defined as a vertex group. To allow for rules where not all variables are involved, hence shorter rules, an extra dummy vertex is added to each variable whose value is unspecified, meaning it can take any of the values available. Although only discrete variables are allowed, we make a distinction between nominal (no apparent ordering in its values, e.g. auditor is Big 5 company) and ordinal variables (a clear ordering of the values, e.g. current ratio). Each nominal variable has one vertex group (with the inclusion of the mentioned dummy vertex), but for the ordinal variables however, we build two vertex groups to allow for intervals to be chosen by the ants. The first vertex group corresponds to the lower bound of the interval and should thus be interpreted as $V _ { i } { \geq } \mathrm { V a l u e } _ { i , k } ,$ the second vertex group determines the upper bound, giving $V _ { i + 1 } \leq \mathrm { V a l u e } _ { i + 1 , 1 }$ (of course, the choice of the upper bound is constrained by the lower bound). This allows to have less, shorter and actually better rules. To extract a rule set that is exhaustive, such that all future data points can be classified, the majority class is not included in the vertex group of the class variable, and will be the predicted class for the final else clause.

A simplified example AntMiner+ construction graph for a audit mining dataset with only three variables (Big 5 auditor, current ratio (CR) and net income over total assets (NI/TA)) is shown in Fig. 3. The path denoted in bold describes the rule $\mathbf { \widetilde { u } f }$ Big ${ 5 } \mathrm { { = Y e s } }$ and $\ \mathrm { C R \ \in }$ [0.05,1) then going concern opinion=yes”. Note that the variable NI/TA is not included in the rule, as the condition NI/TA in [−1,infty) does not restrict the rule any further and is therefore omitted. A formal illustration of the construction graph is provided in [34].

Now that the environment is defined, we can explain the workings of the technique, which is described in pseudo-code in Algorithm 1. All ants begin in the Start vertex and walk through their environment to the Stop vertex, gradually constructing a rule. Only the ant that describes the best rule will update the pheromone of its path, as imposed by the MAX–MIN Ant System approach. Evaporation decreases the pheromone of all edges by multiplication with $\rho$ (a real number typically in the range of [0.8,0.99]), while the pheromone levels are constrained to lie within the given interva $[ \tau _ { m i n } ,$ $\tau _ { m a x } ]$ . Then another iteration occurs with ants walking from Start to Stop. Convergence occurs when all the edges of one path have a pheromone level $\tau _ { m a x }$ and all other edges have pheromone level $\tau _ { m i n } .$ . Next, the rule corresponding to the path with $\tau _ { m a x }$ is extracted and added to the rule set. Finally, training data covered by this rule are removed from the training set. This iterative process will be repeated until an early stopping criterion is met. More details on the algorithm can be found in [34].

![](/api/attachments/ZZE9FFGW/fulltext/images/87e05e3a5b5f42f81514a42b6d143581e2f960e73364d69fe015895d6349a220.jpg)  
Fig. 3. Example of a path described by an ant for a software construction graph defined by AntMiner+. The rule corresponding to the chosen path is “if Big 5=Yes and $\mathrm { C R } \in [ 0 , 1 )$ then going concern opinion=yes”.

<table><tr><td>Algorithm 1 Pseudo-code of AntMiner+ algorithm</td></tr><tr><td>1: construct graph</td></tr><tr><td>2: while not early stopping or minimum percentage data covered do</td></tr><tr><td>3: initialize heuristics, pheromones and probabilities of edges</td></tr><tr><td>4: while not converged do</td></tr><tr><td>5: create ants</td></tr><tr><td>6: let ants run from source to sink</td></tr><tr><td>7: evaporate pheromone on edges</td></tr><tr><td>8: prune rule of best ant</td></tr><tr><td>9: update path of best ant</td></tr><tr><td>10: adjust pheromone levels if outside boundaries</td></tr><tr><td>11: kill ants</td></tr><tr><td>12: update probabilities of edges</td></tr><tr><td>13: end while</td></tr><tr><td>14: extract rule corresponding to converged path</td></tr><tr><td>15: flag data points covered by the extracted rule</td></tr><tr><td>16: end while</td></tr><tr><td>17: evaluate performance on test set</td></tr></table>

Advantages of AntMiner+ are not only the accuracy and comprehensibility of the generated models, but also the possibility to demand intuitive predictive models [33], which is crucial whenever comprehensibility is required. For example, when a classification rule is induced, the rule “if CRN 1 then going concern opinion=yes”, is an unintuitive rule, as we would expect that higher current ratios will be less subject to going concern opinions, making the expected sign for this example “b”. The rule “if CRb 1 then going concern opinion = yes” on the other hand, is intuitive. By stating constraints on these inequality signs, such domain knowledge can be incorporated, resulting in intuitive, justifiable classification models.

## 3.3. Visualization and validation with decision tables

Decision tables are a tabular representation used to describe and analyze decision situations [53] and consist of four quadrants, separated by double-lines, both horizontally and vertically. The vertical line divides the table into a condition part (left) and an action part (right), while the horizontal line separates subjects (above) from entries (below). The condition subjects are the problem criteria (the variables) that are relevant to the decision-making process. The action subjects describe the possible outcomes of the decision-making process; i.e., the classes of the classification problem: going concern opinion =yes or no. Each condition entry describes a relevant subset of values (called a state) for a given condition subject (variable), or contains a dash symbol (‘–’) if its value is irrelevant within the context of that row. Subsequently, every action entry holds a value assigned to the corresponding action subject (class). Every row in the entry part of the decision table thus comprises a classification rule, indicating what action(s) apply to a certain combination of condition states. For example, in Fig. 4a, the final row tells us to predict a going concern opinion if Negative Net Income = no, Current Ratio ≤ 0.5 and Retained Earnings/Total Assets b 0. Decision tables can be contracted by combining logically adjacent (groups of) rows that lead to the same action configuration, as shown in Fig. 4b. It is obvious that such a decision table with a minimal number of rows is to be preferred since it provides a more efficient representation of the underlying knowledge.

We deliberately restrict ourselves to single-hit tables, wherein rows have to be mutually exclusive, because of their advantages with respect to verification and validation [53]. As can be seen from Fig. 4, the representation of a decision table is closely related to that of a decision tree.

<table><tr><td>Negative Net Income</td><td>Current Ratio</td><td>Ret.Earnings/TotalAssets</td><td>report = 1</td><td>report = 0</td></tr><tr><td rowspan="4">yes</td><td rowspan="2">&gt;0.5</td><td>≥0</td><td>-</td><td>×</td></tr><tr><td>&lt;0</td><td>×</td><td>-</td></tr><tr><td rowspan="2">≤0.5</td><td>≥0</td><td>×</td><td>-</td></tr><tr><td>&lt;0</td><td>×</td><td>-</td></tr><tr><td rowspan="4">no</td><td rowspan="2">&gt;0.5</td><td>≥0</td><td>-</td><td>×</td></tr><tr><td>&lt;0</td><td>×</td><td>-</td></tr><tr><td rowspan="2">≤0.5</td><td>≥0</td><td>-</td><td>×</td></tr><tr><td>&lt;0</td><td>×</td><td>-</td></tr></table>

(a) Expanded decision table

<table><tr><td>Negative Net Income</td><td>Current Ratio</td><td>Ret.Earnings/TotalAssets</td><td></td><td>report = 1</td><td>report = 0</td></tr><tr><td rowspan="3">yes</td><td rowspan="2">&gt;0.5</td><td>≥0</td><td></td><td>-</td><td>×</td></tr><tr><td>&lt;0</td><td></td><td>×</td><td>-</td></tr><tr><td>≤0.5</td><td>-</td><td></td><td>×</td><td>-</td></tr><tr><td rowspan="2">no</td><td rowspan="2">-</td><td>≥0</td><td></td><td>-</td><td>×</td></tr><tr><td>&lt;0</td><td></td><td>×</td><td>-</td></tr></table>

(b) Contracted decision table  
Fig. 4. Minimizing the number of columns of a lexicographically ordered decision table.

## 3.4. Experimental set-up

## 3.4.1. Data acquisition & sampling

We identified all firms from the Worldscope database that are listed on AMEX, NASDAQ and NYSE in the period 2002–2004, resulting in an initial sample of 11,575 US listed companies. Minimum data requirements were imposed on this initial selection of listed firms. In particular, firms were excluded if they did not have sufficient Worldscope data to compute all going concern predictor variables included in the research design. Imposing this criterium yielded a dataset of 10,318 company–year observations, consisting of 271 going concern modified opinions and 10,047 clean audit opinions. This proportion of going concern modified opinions is consistent with the proportion of going concern audit opinions identified in prior going concern research (see, for example, [16]).

One of the research objectives of this study is to empirically evaluate the appropriateness of different choice-based sampling techniques used in recent going concern research. Therefore, we conducted our experiments on both a matched and a balanced sample, as well as on the complete dataset. In the matched pair design, we matched companies receiving a clean audit report to going concern firms based on year, size (proxied by total assets) and two-digit SIC classifications. These matching criteria are consistent with prior going concern research adopting this sampling methodology (e.g. [30,20]). In the balanced sample, we included all 271 firms receiving a going concern report and a random selection of 271 firms receiving a clean audit report.

## 3.4.2. Variable specification

The dependent variable in our research design is the dummy variable REPORT, which equals one if the auditor issued a going concern report, and zero otherwise. As independent variables we include a wide variety of financial performance indicators used in prior going concern research, as shown in Table 2. In particular, we include the current ratio (CR), cash flow from operations divided by total liabilities (CFO/TL) and change in working capital divided by total assets (ΔWC/TA) as liquidity measures. These variables have been used extensively in previous going concern research (e.g. [37,36,6,13,45,5]) and were identified as important determinants of the decision to issue a going concern opinion. In addition, we include total liabilities divided by total assets (TL/TA) and net worth divided by total liabilities (NW/TL) as indicators of a company's solvency (e.g. [37,45]). Other variables included in the research model reflect company profitability and include net income divided by total assets (NI/TA), retained earnings divided by total assets (RE/TA) and dummy variables indicating current year loss (NEG NI) or operating loss (NEG OI). These going concern i n d i c a t o r s h a v e b e e n u s e d p r e v i o u s l y b y [37,36,17,13,5]. Following [6], we also include a number of change variables such as the change in total liabilities divided by total assets (ΔTL/TA), change in net income divided by total assets (ΔNI/TA) and change in retained earnings divided by total assets (ΔRE/TA).

Size is also included as a test variable because it has been shown to be significantly associated with going concern decision-making [13,39,5,20–24]. Following [13,20], the natural log of total assets (LNTA) is used as a measure of company size. Finally, based on [15] we include a dummy variable reflecting auditor firm size (BIG 4) as Big 4 audit firms are likely to issue more conservative audit reports than non-Big 4 audit firms.

## 3.4.3. Discretization

In a first pre-processing step, the data was discretisized in order to obtain discrete variables. This discretization process occurred in an automatic manner, with the criterion of [19]; although for the variables CR, TL/TA and NET WORTH/TL our own discretizations were used.

Table 2

<table><tr><td colspan="2">Independent and dependent variables</td></tr><tr><td>Variable</td><td>Definition</td></tr><tr><td colspan="2">Dependent variable</td></tr><tr><td>REPORT</td><td>1 if going concern report issued, 0 otherwise</td></tr><tr><td colspan="2">Independent variables</td></tr><tr><td>CR</td><td>Current ratio</td></tr><tr><td>LNTA</td><td>Natural log of total assets</td></tr><tr><td>CFO/TL</td><td>Cash flow from operations divided by total liabilities</td></tr><tr><td>TL/TA</td><td>Total liabilities divided by total assets</td></tr><tr><td>ΔTL/TA</td><td>One year change in total liabilities divided by total assets</td></tr><tr><td>NITA</td><td>Net income divided by total assets</td></tr><tr><td>ΔNI/TA</td><td>One year change in net income divided by total assets</td></tr><tr><td>NEG NI</td><td>1 if negative net income, 0 otherwise</td></tr><tr><td>NEG OI</td><td>1 if negative operating income, 0 otherwise</td></tr><tr><td>BIG 4</td><td>1 if a big 4 auditor performs the audit, 0 otherwise</td></tr><tr><td>RE/TA</td><td>Retained earnings divided by total assets</td></tr><tr><td>ΔRE/TA</td><td>One year change in retained earnings divided by total assets</td></tr><tr><td>ΔWC/TA</td><td>One year change in working capital divided by total assets</td></tr><tr><td>NW/TL</td><td>Net worth divided by total liabilities</td></tr></table>

Table 3  
Average out-of-sample performances

<table><tr><td></td><td></td><td>Matched</td><td>Balanced</td><td>Original</td></tr><tr><td rowspan="5">Accuracy</td><td>AntMiner+</td><td>68.2</td><td>76.2</td><td>97.16</td></tr><tr><td>C4.5</td><td>72.3</td><td>78.2</td><td>97.34</td></tr><tr><td>Logit</td><td>72.5</td><td>81.0</td><td>97.21</td></tr><tr><td>SVM</td><td>73.7</td><td>80.7</td><td>97.22</td></tr><tr><td>Majority vote</td><td>52.32</td><td>51.16</td><td>97.23</td></tr><tr><td rowspan="2">Number of rules</td><td>AntMiner+</td><td>13.9</td><td>4.1</td><td>5.1</td></tr><tr><td>C4.5</td><td>22.9</td><td>13.2</td><td>12.6</td></tr></table>

## 3.4.4. Included techniques

To compare the results of AntMiner+, a benchmarking study is performed that includes commonly used state-ofthe-art classification techniques. Logistic regression provides linear classifiers, for which the regression coefficients are determined with a maximum likelihood procedure. C4.5 is the popular decision tree builder [44] where each leaf assigns class labels to observations. Each of these leaves can be represented by a rule and therefore C4.5 also builds comprehensible classifiers. Note that we used the Weka implementation [55] with standard pruning factor. Majority prediction simply always predicts the majority class. As the majority of the data instances are non-going concern opinions, all predictions will be ‘no going concern opinion’. Support vector machines (SVMs) are currently state-of-the-art for the classification task and generally speaking exhibit good predictive performance, due to its ability to capture non-linearities [54]. We report the results of the SVM with Radial Basis Function (RBF) kernel and hyperparameters set by a gridsearch procedure [50].

To eliminate any chance of having unusually good or bad training and test sets, 10 runs are conducted where the data is first randomized before the training, validation and test set are chosen, as is common practice in data mining [26,55,32].

## 3.5. Results

The results are shown in Table 3, with the best results underlined and in boldface, the ones that are not significantly different at a 5% level in boldface, results significantly different at 5% level, but not at 1% level in normal script, and those that are significantly different at 1% in italic.

A first observation is that the non-linear SVM classification models are not able to perform significantly better than the linear logistic regression models, suggesting that the data is only weakly non-linear.<sup>1</sup> The advantage of the rule-based classification technique AntMiner+, is that interpretable rule sets are induced. Such a rule set is provided in Table 4.

The form of respectively the SVM and logistic regression classifiers are described by Eqs. (1) and (2) and clearly indicate the opacity problem of these models.

$$
y _ {\mathrm{SVM}} (x) = \operatorname{sign} \left[ \sum_ {i = 1} ^ {N} \alpha_ {i} y _ {i} \exp \left\{- \frac {| | x - x _ {i} | | _ {2} ^ {2}}{\sigma^ {2}} \right\} + b \right]\tag{1}
$$

$$
y _ {\text { logit }} (x) = \left[ 1 / \left(1 + \exp \left\{- \left(w _ {0} + w ^ {T} x\right) \right\}\right) \right].\tag{2}
$$

Although AntMiner+ underperforms in terms of accuracy on this dataset, the model it generates is still preferred to the other techniques because:

• Comprehensibility: auditors are often rather skeptical to the use of statistical, rather incomprehensible models, therefore rule based models are preferred. Both C4.5 and AntMiner+ produce such user friendly models, however, AntMiner+ produces less rules, resulting in increased understandability.

• Intuitiveness: An intuitive model is preferred to a more accurate, yet less intuitive model. The ability to include domain knowledge in AntMiner+, guarantees such intuitive models. Furthermore, validation by a domain expert (senior audit partner at a Big 4 company) revealed that this is the most important aspect for acceptance of the model. This guarantee for intuitive models is not included in C4.5.

Table 5  
Decision table predicting going concern opinion

<table><tr><td>RE/TA</td><td>NEG NI</td><td>LNTA</td><td>CR</td><td>TL/TA</td><td>ΔWC/TA</td><td>ΔTL/TA</td><td></td><td>report = 1</td><td>report = 0</td></tr><tr><td rowspan="9">&lt; 0.05</td><td rowspan="8">= 0</td><td rowspan="5">&lt; 10.813</td><td>&lt; 1</td><td>-</td><td>-</td><td>-</td><td></td><td>x</td><td>-</td></tr><tr><td rowspan="4">≥ 1</td><td rowspan="3">&lt; 1</td><td rowspan="2">&lt;-0.241</td><td>&lt; 0.094</td><td></td><td>-</td><td>x</td></tr><tr><td>≥ 0.094</td><td></td><td>x</td><td>-</td></tr><tr><td>≥ -0.241</td><td>-</td><td></td><td>-</td><td>x</td></tr><tr><td>≥ 1</td><td>-</td><td>-</td><td></td><td>x</td><td>-</td></tr><tr><td rowspan="3">≥ 10.813</td><td rowspan="3">-</td><td rowspan="3">-</td><td rowspan="2">&lt;-0.241</td><td>&lt; 0.094</td><td></td><td>-</td><td>x</td></tr><tr><td>≥ 0.094</td><td></td><td>x</td><td>-</td></tr><tr><td>≥ -0.241</td><td>-</td><td></td><td>-</td><td>x</td></tr><tr><td>= 1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td></td><td>x</td><td>-</td></tr><tr><td rowspan="7">≥ 0.05</td><td rowspan="7">-</td><td rowspan="4">&lt; 10.813</td><td rowspan="4">-</td><td rowspan="3">&lt; 1</td><td rowspan="2">&lt;-0.241</td><td>&lt; 0.094</td><td></td><td>-</td><td>x</td></tr><tr><td>≥ 0.094</td><td></td><td>x</td><td>-</td></tr><tr><td>≥ -0.241</td><td>-</td><td></td><td>-</td><td>x</td></tr><tr><td>≥ 1</td><td>-</td><td>-</td><td></td><td>x</td><td>-</td></tr><tr><td rowspan="3">10.813</td><td rowspan="3">-</td><td rowspan="3">-</td><td rowspan="2">&lt;-0.241</td><td>&lt; 0.094</td><td></td><td>-</td><td>x</td></tr><tr><td>≥ 0.094</td><td></td><td>x</td><td>-</td></tr><tr><td>≥ -0.241</td><td>-</td><td></td><td>-</td><td>x</td></tr></table>

• Accuracy: even though AntMiner+ achieves a less predictive accuracy measure than C4.5, the difference is not significant at a 1% level.

Mainly because of the ability to introduce domain knowledge, and the fact that AntMiner+ induces a limited amount of rules which are still quite accurate, the AntMiner+ rules are the most suitable.

When the rule set induced by AntMiner+, shown in Table 4, is converted to a decision table,<sup>2</sup> the output, as shown in Table 5, is obtained. As we are able to incorporate domain knowledge into the AntMiner+ classification technique, the automatically generated classifier satisfies our expectations about the correlation between the variables and the going concern opinion variable, as being either positive or negative.

From the large number of possible going concern predictors included in this study, the decision model selected the seven most predictive going concern variables: one measuring company size (LNTA), two measuring profitability (RE/TA, LOSS), two measuring liquidity (CR, ΔWC/TA) and two measuring solvency (TL/TA, ΔTL/TA).

As can be seen, the two most important variables (as show by the top two levels of the decision table) are the two profitability indicators RE/TA and NEG NI. This is consistent with previous going concern prediction research which confirms that profitability ratios are an important determinant of going concern decisionmaking (e.g. [36,17,6,45,5]). The decision model furthermore indicates that a company is more likely to receive a going concern modified audit report if it has lower total assets, lower current ratio, decreasing working capital to total assets, and increasing total liabilities to total assets. The choice of predictor variables and the directional impact of the variables are consistent with previous going concern research, which adds to the acceptability and potential usefulness of the decision model as a decision aid in everyday auditing.

The model has an overall correct classification rate of 68.2% for the matched sample, 76.2% for the balanced sample and 97.2% for the full sample. Note that although the performance of the decision model is comparable to logistic regression, the decision table provides auditors with a user-friendly and intuitively sensible decision model that can be used in everyday auditing.

## 4. Conclusions

The relevance and success of data mining for the going concern decision is driven by a number of factors. First of all, much data of previously audited firms is available, a prerequisite for any data mining application. Secondly, the going concern decision is a complex task with widespread consequences to both the company being audited and the auditor, for which decision support systems are more than welcome. This has prompted the development of numerous models to predict the issuance of a going concern opinion in the past. Finally, recent accounting debacles only stress the importance of good auditing practices, increasing the relevance of such predictive data mining models even further. In the existing literature body, the automated prediction of such opinions is commonly done with logistic regression. Although more advanced data mining techniques — which have been widely researched and applied in domains such as credit scoring, bio-informatics and marketing — were largely missing from the audit domain, we have shown the applicability and usefulness of such approaches.

Decision support tools can be very helpful, though user friendliness is a key requirement as auditors are often rather skeptical to the use of statistical, rather incomprehensible models. An intuitive decision table on the other hand, can very easily be incorporated into the auditor's guidelines, assuring that going concern opinions are expressed more consistently. The rule sets induced by the ant-based classification technique AntMiner+, provide such interpretability, allowing for truly easy and user-friendly consultation in every day audit practices.

Further, we empirically tested the ongoing academic discussion on sampling methodologies. Although the experiments show differences in accuracies over the different sampling methodologies, as could be expected, more interestingly the ranking among the included techniques did not change.

Of course, the search for more predictive variables and more relevant data is a continuous process. For example, as the auditing firm typically has a long term relationship with its customer, it will have more data at its disposal than publicly available. The decision table proposed here can surely be complemented by the private information available, as to obtain an even more accurate model.

## Acknowledgments

We extend our gratitude to the editor and the anonymous reviewers, as their constructive remarks certainly contributed much to the quality of this paper. Further, we would like to thank the Flemish Research Council (FWO, Grant G.0615.05) for the financial support.

## References

[1] AICPA, The auditor's consideration of an entity's ability to continue in existence, statement on auditing standards no. 59, 1988.

[2] B. Baesens. Developing intelligent systems for credit scoring using machine learning techniques. PhD thesis, K.U.Leuven, 2003.

[3] B. Baesens, T. Van Gestel, S. Viaene, M. Stepanova, J. Suykens, J. Vanthienen, Benchmarking state-of-the-art classification algorithms for credit scoring, Journal of the Operational Research Society 54 (6) (2003) 627–635.

[4] B. Baesens, R. Setiono, C. Mues, J. Vanthienen, Using neura network rule extraction and decision tables for credit-risk evaluation, Management Science 49 (3) (2003) 312–329.

[5] B.K. Behn, S.E. Kaplan, K.R. Krumwiede, Further evidence on the auditor's going-concern report: the influence of management plans, Auditing: A Journal of Practice and Theory 20 (1) (2001) 13–29.

[6] T.B. Bell, R.H. Tabor, Empirical analysis of audit uncertainty qualifications, Journal of Accounting Research 29 (2) (1991) 350–370.

[7] E. Bonabeau, M. Dorigo, G. Theraulaz, Swarm intelligence: from natural to artificial systems, Journal of Artificial Societies and Social Simulation 4 (1) (2001).

[8] J.V. Carcello, T.L. Neal, Audit committee composition and auditor reporting, The Accounting Review 75 (4) (2000) 453–467.

[9] J.V. Carcello, D.R. Hermanson, H.F. Huss, Temporal changes in bankruptcy-related reporting, Auditing: A Journal of Practice and Theory 14 (2) (1995) 133–143.

[10] J.V. Carcello, D.R. Hermanson, H.F. Huss, Going-concern opinions: the effects of partner compensation plans and client size, Auditing: A Journal of Practice and Theory 19 (1) (2000) 67–77.

[11] P. Carey, R. Simnett, Audit partner tenure and audit quality, The Accounting Review 81 (3) (2006) 653–676.

[12] G. Di Caro, M. Dorigo, Antnet: distributed stigmergetic control for communications networks, Journal of Artificial Intelligence Research 9 (1998) 317–365.

[13] K.C.W. Chen, B.K. Church, Default on debt obligations and the issuance of going-concern opinions, Auditing: A Journal of Practice and Theory 11 (2) (1992) 30–50.

[14] M. De Backer, R. Haesen, D. Martens, B. Baesens, A stigmergy based approach to data mining, Proceedings of the18th Australian Joint Conference on AI, Lecture Notes in Computer Science, Springer, 2005, pp. 975–978.

[15] L.E. DeAngelo, Auditor size and audit quality, Journal of Accounting & Economics 3 (3) (1981) 183–199.

[16] M.L. DeFond, K. Raghunandan, K.R. Subramanyam, Do nonaudit service fees impair auditor independence? Evidence from going concern audit opinions, Journal of Accounting Research 40 (4) (2002) 1247–1274.

[17] N. Dopuch, R.W. Holthausen, R.W. Leftwich, Predicting audit qualifications with financial and market variables, The Accounting Review 62 (3) (1987) 431–455.

[18] M. Dorigo, L.M. Gambardella, Ant colony system: a cooperative learning approach to the traveling salesman problem, IEEE Transactions on Evolutionary Computation 1 (1) (April 1997) 53–66.

[19] U.M. Fayyad, K.B. Irani, Multi-interval discretization of continuous-valued attributes for classification learning, Proceedings of the International Joint Conference on Uncertainty in AI, 1993, pp. 1022–1027.

[20] A. Gaeremynck, M. Willekens, The endogenous relationship between audit— report type and business termination: evidence on private firms in a non-litigious environment, Accounting and Business Research 33 (1) (2003) 65–79.

[21] M.A. Geiger, K. Raghunandan, Bankruptcies, audit reports, and the reform act, Auditing: A Journal of Practice and Theory 20 (1) (2001) 187–197.

[22] M.A. Geiger, K. Raghunandan, Auditor tenure and audit reporting failures, Auditing: A Journal of Practice and Theory 21 (1) (2002) 67–80.

[23] M.A. Geiger, D.V. Rama, Audit fees, nonaudit fees, and auditor reporting on stressed companies, Auditing: A Journal of Practice and Theory 22 (2) (2003) 53–69.

[24] M.A. Geiger, K. Raghunandan, D.V. Rama, Recent changes in the association between bankruptcies and prior audit opinions, Auditing: A Journal of Practice and Theory 24 (1) (2005) 21–35.

[25] B. Goodman, D.N. Braunstein, Explaining auditors going concern decisions: assessing management's capability, Journa of Applied Business Research 11 (3) (1995) 82–95.

[26] D. Hand, Pattern detection and discovery, in: D. Hand, N. Adams, R. Bolton (Eds.), Pattern Detection and Discovery, Lecture Notes in Computer Science, vol. 2447, Springer, 2002, pp. 1–12.

[27] D. Hand, Protection or privacy? Data mining and personal data, Proceedings of the 10th Pacific-Asia Conference, PAKDD, Lecture Notes in Computer Science, vol. 3918, Springer, 2006, pp. 1–10.

[28] W. Hopwood, J.C. McKeown, J.F. Mutchler, A reexamination of auditor versus model accuracy within the context of the goingconcern opinion decision, Contemporary Accounting Research 10 (2) (1994) 409–431.

[29] J. Huysmans, B. Baesens, D. Martens, K. Denys, J. Vanthienen, New trends in data mining, Tijdschrift voor economie en Management, vol. L, 2005, pp. 697–711.

[30] A.S. Levitan, J.A. Knoblett, Indicators of exceptions to the going-concern assumption, Auditing: A Journal of Practice and Theory 5 (1) (1985) 26–39.

[31] G.S. Maddala, A perspective on the use of limited-dependent and qualitative variables models in accounting research, The Accounting Review 66 (4) (1991) 788–807.

[32] D. Martens, M. De Backer, R. Haesen, B. Baesens, T. Holvoet, Ants constructing rule-based classifiers, Swarm Intelligence and Data Mining, Studies in Computational Intelligence, chapter 2, Springer, 2006.

[33] D. Martens, M. De Backer, R. Haesen, B. Baesens, C. Mues, J. Vanthienen, Ant-based approach to the knowledge fusion problem, Proceedings of the Fifth International Workshop on Ant Colony Optimization and Swarm Intelligence, Lecture Notes in Computer Science, Springer, 2006, pp. 85–96.

[34] D. Martens, M. De Backer, R. Haesen, M. Snoeck, J. Vanthienen, B. Baesens, Classification with ant colony optimization, IEEE Transaction on Evolutionary Computation 11 (5) (2007) 651–665.

[35] J.C. McKeown, J.F. Mutchler, W. Hopwood, Towards an explanation of auditor failure to modify the audit opinion of bankrupt companies, Auditing: A Journal of Practice and Theory (1991) 1–13 (supplement).

[36] K. Menon, K.B. Schwartz, An empirical investigation of audi qualification decisions in the presence of going-concern uncertainties, Contemporary Accounting Research 3 (2) (1987) 302–315.

[37] J.F. Mutchler, A multivariate analysis of the auditors goingconcern opinion decision, Journal of Accounting Research 23 (2) (1985) 668–682.

[38] J.F. Mutchler, D.D. Williams, The relationship between audit technology, client risk profiles, and the going-concern opinion

decision, Auditing: A Journal of Practice and Theory 9 (3) (1990) 39–54.

[39] J.F. Mutchler, W. Hopwood, J.C. McKeown, The influence of contrary information and mitigating factors on audit opinion decisions on audit opinion decisions on bankrupt companies, Journal of Accounting Research 35 (2) (1997) 295–310.

[40] D. Oliveira, P. Ferreira, A.L.C. Bazzan, Reducing traffic jams with a swarmbased approach for selection of signal plans, Proceedings of Fourth International Workshop on Ant Colony Optimization and Swarm Intelligence — ANTS 2004, Lecture Notes in Computer Science, vol. 3172, Springer, 2005, pp. 416–417.

[41] L. Passmore, J. Goodside, L. Hamel, L. Gonzales, T. Silberstein, J. Trimarchi, Assessing decision tree models for clinical in-vitro fertilization data. Technical Report TR03-296, Dept. of Computer Science and Statistics, University of Rhode Island, 2003.

[42] M. Pazzani, S. Mani, W. Shankle, Acceptance by medical experts of rules generated by machine learning, Methods of Information in Medicine 40 (5) (2001) 380–385.

[43] A. Prinzie, D. Van den Poel, Predicting home-appliance acquisition sequences: Markov/Markov for discrimination and survival analysis for modeling sequential information in NPTB models, Decision Support Systems 44 (1) (2007) 28–45.

[44] J.R. Quinlan, C4.5: Programs for Machine Learning, Morgan Kaufmann Publishers Inc., San Francisco, CA, USA, 1993.

[45] K. Raghunandan, D.V. Rama, Audit reports for companies in financial distress: before and after SAS no. 59, Auditing: A Journal of Practice and Theory 14 (1) (1995) 50–64.

[46] J.K. Reynolds, J.R. Francis, Does size matter? The influence of large clients on office-level auditor reporting decisions, Journal of Accounting and Economics 30 (3) (2000) 375–400.

[47] J.W. Seifert, Data mining and homeland security: An overview, CRS Report for Congress, 2006.

[48] G. Theraulaz, E. Bonbeau, A brief history of stigmergy, Artificial Life 5 (2) (1999) 97–116.

[49] L. Thomas, D. Edelman, J. Crook (Eds.), Credit Scoring and its Applications, SIAM, 2002.

[50] T. Van Gestel, J.A.K. Suykens, B. Baesens, S. Viaene, J. Vanthienen, G. Dedene, B. De Moor, J. Vandewalle, Benchmarking least squares support vector machine classifiers, Machine Learning 54 (1) (2004) 5–32.

[51] T. Van Gestel, B. Baesens, P. Van Dijcke, J. Garcia, J.A.K. Suykens, J. Vanthienen, A process model to develop an internal rating system: sovereign credit ratings, Decision Support Systems 42 (2) (2006) 1131–1151.

[52] J. Vanthienen, E. Dries, Illustration of a decision table tool for specifying and implementing knowledge based systems, International Journal on Artificial Intelligence Tools 3 (2) (1994) 267–288.

[53] J. Vanthienen, C. Mues, A. Aerts, An illustration of verification and validation in the modelling phase of KBS development, Data and Knowledge Engineering 27 (3) (1998) 337–352.

[54] V.N. Vapnik, The nature of statistical learning theory, Springer– Verlag New York, Inc., New York, NY, USA, 1995.

[55] I.H. Witten, E. Frank, Data mining: practical machine learning tools and techniques with Java implementations, Morgan Kaufmann Publishers Inc., San Francisco, CA, USA, 2000.

David Martens received a PhD in Applied Economic Sciences from the Department of Decision Sciences and Information Management of K.U.Leuven, Belgium, in 2008. He also received a Master's degree in civil engineering at the Computer Science Department from K.U.

Leuven, Belgium in 2003; and a Master of Business Administration in 2005 from Reims Management School, France. His research is mainly focused on the development of comprehensible data mining techniques, with main application the building of Basel II-compliant credit scoring systems.

Liesbeth Bruynseels received the M.Sc. and Ph.D. degree in Applied Economic Sciences from the K.U.Leuven (Belgium) in 2001 and 2006, respectively. She is currently working as an assistant professor of accounting at the University of Tilburg (The Netherlands). Her research interests include auditor reporting, auditor judgment and decision making and audit quality.

Bart Baesens received the M.Sc. and Ph.D. degree in Applied Economic Sciences from the K.U.Leuven (Belgium) in 1998 and 2003, respectively. He is currently working as an assistant professor at K.U.Leuven (Belgium) and as a lecturer at the University of Southampton (United Kingdom). His research interests include classification, rule extraction, neural networks, support vector machines, data mining, and credit scoring.

Marleen Willekens is professor of financial accounting and auditing at the K.U.Leuven (Belgium) and the University of Tilburg (the Netherlands). She has earned a PhD from the University of Warwick Business School. Her research is focused on economical aspects of auditing and the information value of financial reporting. Marleen Willekens teaches financial accounting and auditing courses both in graduate and undergraduate programmes.

Jan Vanthienen received the M.Sc. and Ph.D. degree in Applied Economic Sciences from the K.U.Leuven (Belgium). He is professor at the Department of Decision Sciences and Information Management of K.U.Leuven. His main research themes are business rules and information management.

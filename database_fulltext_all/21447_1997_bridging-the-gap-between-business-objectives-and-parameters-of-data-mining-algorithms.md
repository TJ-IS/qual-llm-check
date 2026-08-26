---
otero_id: 21447
otero_key: "A5XATF4E"
title: "Bridging the gap between business objectives and parameters of data mining algorithms"
authors: "F. Özden Gür Ali; William A. Wallace"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(97)00010-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Bridging the gap between business objectives and parameters of data mining algorithms

F. Özden Gür Ali \*, William A. Wallace $^{1}$

Rensselaer Polytechnic Institute, Decision Sciences and Engineering Systems, Troy, NY 12180-3590, USA

## Abstract

Data mining is being touted as having potential for discovering information that will contribute toward resolving business problems or creating business opportunities. However, before this potential can be realized, one needs to be able to relate the strategic objectives of a business to the use of the data mining technology. In this paper we focus on one aspect of that requirement, the translation of managerial goals into parameters of the algorithm being used to analyze the data. The first step in the process is to define a mapping from managerial goals to the performance measures of the algorithm. We then propose and apply an experimental approach using a classification algorithm, Probabilistic Inductive Learning, to develop a mapping between the performance measures and the parameters of the algorithm. The experimental results are analyzed and guidelines are given for setting the bias of the algorithm to meet managerial goals. We conclude by recommending that an experimental analysis similar to what we proposed be conducted for all data mining algorithms and provided along with documentation as an aid to the user. © 1997 Elsevier Science B.V.

Keywords: Machine learning; Data mining; Managerial decision making; Probabilistic inductive learning; Business objectives; Algorithm parameters

## 1. Introduction

We are constantly being reminded (and rightly so) that data mining must be more than just discovering knowledge for its own sake. The knowledge must provide insights into a business problem or opportunity and guidelines for action, i.e., support for decision making. What does this mean for the data mining analyst? As noted in IBM's overview [1], he or she must (1) understand the business problem; (2)

select and structure the dataset; (3) select and run the appropriate tools; (4) analyze the output; and (5) present results to management. Our focus is on step (3), and its relationship to steps (1) and (2). Work exists on choice of algorithms [6], and choice of the parameters of an algorithm where the objective is overall accuracy [5].

In a recent attempt at a framework for knowledge discovery and data mining, nine steps were proposed [2]: (1) understanding the application and 'identifying the goal of the KDD process from customer's viewpoint,' (2)-(4) developing a useful dataset, (5) 'matching the goals of the KDD process to the particular data mining method,' (6) selecting the data mining algorithm, as well as setting parameters, (7) data mining, (8) interpretation, and (9) documentation and utilization of the discovered knowledge. In choosing the algorithm (step 6) consideration must be given to the relationship between the business objective (noted in step 1), the knowledge representation scheme selected and search algorithms employed. The selection process must not forget that accuracy, the criterion typically used in selecting an algorithm and setting its parameters, is not the only criterion used in the business world—and may not be the most important one. We will discuss different criteria in Section 2.

In this paper, we focus on the selection of parameters for a particular algorithm, i.e., tuning the algorithm to have the biases needed to achieve the business objective. We propose that guidelines for parameter settings for algorithm performance measures, e.g., overall accuracy, specificity of rules, or category specific accuracy, be developed by algorithm developers and researchers.

Different application domains will have different business objectives which map into the algorithm performance measures. Although the mapping between the business objectives and algorithm performance measures must be done on a case-by-case basis (link A in Fig. 1), there is not the time nor resources available to map the algorithm performance measures into parameter settings (Link B in Fig. 1) for all the KDD algorithms that one might use in an actual business application. In Section 4, we provide a rigorous procedure for performing the mapping, illustrated by its application to a tree induction algorithm, Probabilistic Inductive Learning (PrIL) algorithm [4]. However, the procedure is applicable to other algorithms with tuning parameters.

The paper is organized as follows. Managerial goals that can be supported by classification are illustrated in the context of a manufacturing organization's quality objective. The map from the managerial goals to classification performance measures for this particular objective is established. The PrIL algorithm is briefly described. Next, a procedure involving an experiment with parameter settings and representative datasets is proposed to establish the second map. The proposed procedure is applied to PrIL algorithm. Results from the designed experiment are discussed, including the effects of changes in the parameters on the performance measures. Specific recommendations for tuning PrIL are given, thus establishing the map between performance measures and algorithm parameters. The paper concludes with a summary and a recommendation that analyses similar to the one proposed be conducted for all data mining algorithms and provided to the user as part of the documentation.

![](/api/attachments/A5XATF4E/fulltext/images/fdb4d594605a93e055dd724b4eba141faa1c6281ac5d7021c6ed3a5ef8c8d70b.jpg)  
Fig. 1. Business objectives determine algorithm parameters.

## 2. Managerial goals and measures of performance

In this section, we introduce managerial goals and discuss their relationship to the performance of a classification algorithm. We illustrate them in the context of manufacturing quality. As noted, the mapping from managerial goals to algorithm performance measures must be done on a case-by-case basis. However, guidance can be provided to the business analyst doing the mapping, by the development of templates for specific application domains, e.g., marketing, fraud detection, quality, etc. The templates would specify for each relevant managerial goal in that application domain (1) generic data items to be used, (2) appropriate data mining method, e.g., clustering, classification, etc., (3) and the algorithm performance measures that meet the managerial goals.

One of the major objectives for a manufacturing organization is improving the cost of quality, including cost of lost business, scrap and rework, as well as cost of quality control and design for quality programs.

For our illustrative example, we will assume the production process can be divided into two phases, with a semi-finished part produced after phase 1 that can be inspected and reworked if necessary before entering the second and final phase of production, where the resulting product is tested and either shipped or scrapped (see Fig. 2). In this example of manufacturing quality, a generic data item would be production parameters; the data mining method is classification; and an algorithm performance measure is overall accuracy.

![](/api/attachments/A5XATF4E/fulltext/images/90cb7a247f66c58b0b65ddd864ef9e535da3100feb6c5ff062694c4bd88cb6b0.jpg)  
Fig. 2. Illustrated production process.

'A managerial goal to achieve the business objective of reducing the cost of quality is to be very certain of a decision that considers a part good. Because if a bad part passes the first inspection, scrapping the final product is very expensive. Management wants to rework the parts that would have failed the final inspection.'

Overall accuracy, defined as (number of cases correctly classified/number of cases classified) × 100, is an appropriate performance measure for classification. However, it does not take into account what percent of the cases have been left undecided; neither does it consider unequal costs and benefits among classification categories.

‘After some thought, management realizes that a mistake made by reworking a good part is not as costly as letting a faulty part go on to the second phase and then be scrapped. They want to have higher confidence in the decision which predicts that a part is going to be acceptable after the second phase. The tolerance for mistakes on such a decision is lower than on a decision requiring rework for the part; it involves the cost of the lost production. The managerial objective is to focus on the accuracy of one category, predicting that the part will be acceptable after second phase.’

Category specific accuracy, defined as (number cases correctly classified into category k/number of cases classified into category k) × 100; is the performance measure.

‘Management would like to automate as much of the decision making process as possible, and only call the operator to look at a part when it cannot be classified with confidence.’

Percent undecided tallies the percent of cases the induced tree does not cover. We would like to find the parameter settings that increase the coverage of the rules. However, one should be cautioned that decreasing the ‘undecideds’ to zero is very easy if one is willing to sacrifice accuracy. The real quest is finding settings with fewer mistakes and fewer ‘undecideds’.

‘Management would like to be proactive and head off quality problems before they occur. They would like to provide engineers (design and development personnel) with feedback on the causes of defects in the production process in order to help them decide on choice of materials, and product and process design.’

Number of rules, a performance measure, describes how general (few rules) vs. specific (many rules) a tree is. General rules are useful in providing holistic views leading to fundamental changes in product or process design, while specific rules are desirable when only incremental changes are envisioned. More rules for the same dataset mean smaller sample size per rule. Therefore, the variability in the correct classification rates of individual rules will be larger for the same overall sample size if we have more rules. The variance of the correct classification proportion changes inversely with the rule sample size. If the overall volume of cases is not large enough, management should be careful about inducing too many rules.

‘Management needs a defensible measure of confidence in an automated procedure, e.g., decision rules, in order to determine when the operator should intervene. In addition they would like to assign severity to the causes of defects as a guide to the engineers responsible for design and development.’

To our knowledge, PrIL is the only decision tree classification technique that provides statistically sound performance measure for individual rules, as we will be describing in Section 3. The average p-value of the rules refers to the p-value under the null hypothesis that the observed proportion of correct classification is greater than or equal to the reliability measure associated with each rule, a measure of performance for trees induced with PrIL. The higher the p-value, the more assurance we have that the proportion of correctly classified cases is at least as much as the specified reliability. The advantage of the p-value is that it takes into account the sample size of the test set and the deviation from the reliability level.

We have mapped the goals of management in the context of a business objective to performance measures for a data mining algorithm. We will propose and apply an experimental approach to develop the mapping to the parameters of the algorithm. First, we will briefly describe the algorithm to be used for illustrating the proposed approach.

## 3. An overview of probabilistic inductive learning (PrIL)

PrIL [5] induces decision rules that ‘individually’ satisfy the minimum reliability requirements set by the user with a prespecified confidence. Categories may have different amounts of risk associated with them giving rise to different maximum tolerable misclassification levels.

The algorithm induces a classification tree from a history of cases. It branches enough to account for the important attribute dependencies and main effects without diminishing the sample size to such an extent that probabilistic statements cannot be made. Rules are induced so as to at least satisfy the user's category specific minimum acceptable correct classification percentage. If no such rules are found for a subset of data they are explicitly left unclassified.

The tree resulting from using PrIL has a prescriptive value, i.e., rules will be used to guide or make a decision. The cost/benefit and risk tradeoffs are represented in terms of minimum reliability levels, $R_{k}$ . Setting $R_{1}=0.90$ would mean that we cannot tolerate any rule that classifies a case into category 1 to be wrong more than 10% of the time. These requirements can be different for different categories. The misclassification costs and correct classification benefits can be used to calculate them.

Fig. 3 shows a hypothetical PrIL tree where Ai are the attributes that describe a case; the boxes with different shadings represent the classification categories. The box with the question mark indicates that no rule applies to such cases. The numbers on the arcs correspond to the values of the attributes in the parent node and indicate the branch to follow according to the attribute value of a case. The numbers in italics next to the boxes are the goodness measures of the rules: the correct classification proportion for the rule will equal or exceed this figure with a stated confidence level.

![](/api/attachments/A5XATF4E/fulltext/images/42907019e536a05f64b1f00dc027b4351df249b7c6c3f755abb8aed7285b41a6.jpg)  
Fig. 3. Tree structure of the Probabilistic Inductive Learning approach.

Taking the right-most branch in Fig. 3 would establish the following rule: 'If attribute 1 has value 2, attribute 2 has value 2, attribute 6 does not have value 1, and attribute 4 has value 4, then classify the case into the category with dots.'

As can be seen from Fig. 3, the PrIL tree can be considered as consisting of a number of independent (subset elimination) subtrees, one for each value combination of the branching attributes. The effect of the attribute(s) in the branching phase (represented by the round nodes) is taken into account in every rule. Therefore, significant main effects or partners in most of the interaction effects are chosen to become branching attributes.

Subset elimination tries to find subsets of the data where one category has more than the required proportion of examples with the stated confidence. If multiple subsets are found the rule set that gives the highest confidence is posted, all examples covered by it (the subset) are eliminated from further consideration.

The algorithm can be summarized as follows. Set $\{r_{k}\}$ at maximum levels; Repeat (1)-(5) while there are cases in the subset and we can find rules satisfying $\{r_{k}\}$ : (1) set m=1, while $m\leq M$ , for each m-way combination of attributes, (2) 'build the rule set' and 'compute its significance', (3) post the rule set with the maximum significance and eliminate all cases that are covered by the posted rule set; (4) if no rules are found increase m by one. (5) Reduce $\{r_{k}\}$ , until $\{r_{k}\}$ is less than $\{R_{k}\}$ or no case is left.

The required reliability levels, $r_{k}s$ , are set at high levels and successively reduced to the minimum required reliability levels, $R_{k}s$ . The subsets are defined by the values of an attribute or combination of attributes. For each set of reliability requirements $\{r_{k}\}$ , first a rule with one attribute is searched for, if there is no attribute that satisfies the current requirements, rules consisting of combination of two attributes are considered. This process is continued until all combinations of M attributes are considered.

The ‘reliability requirement function’ dictates the reductions in the reliability requirements of categories at each step. There is no restriction on the shape of this function imposed by the PrIL method, as long as it is monotonic and includes the points $(R_{1}, R_{2}, \ldots, R_{K})$ and $(1, 1, 1, \ldots, 1)$ .

Building the rule set for m attributes amounts to identifying all rules defined by the values of the attribute(s) that would pass the following hypothesis test: the p parameter of the binomial distribution is greater than the required reliability level for this category, $r_{k}$ , with a prespecified a level. Here, p is defined as probability of classification category k vs. all others. The precondition to the hypothesis test is that the sample size defined by the values of the attribute is at least n.

The significance of the rule set is a measure that combines how much greater p is from its corresponding $r_{k}$ for each rule in the rule set that passed the above test. Formulating the problem in terms of lack of fit, we arrive at a measure that has a $\chi^{2}$ distribution with the degrees of freedom equal to the number of rules in the rule set. (When $r_{k}$ is too large, we resort to Poisson approximation). The significance of this measure for each rule set is used to select the best rule set.

PrIL will be used throughout the remainder of the paper to illustrate the experimental approach. In addition, we will show how the parameters of an algorithm can be tuned to satisfy managerial goals using performance measures.

## 4. Mapping the algorithm performance measures into parameter settings: an experimental approach

In this section, we present a procedure to map the algorithm performance measures to parameter settings regardless of the particular data at hand. This map should be prepared by the developer of the algorithm or other researchers to be used by practitioners in the context of their problem. In the proposed procedure an experiment is conducted with the algorithm of choice on a multitude of datasets, chosen such that they resemble a wide variety of contexts that are likely to be used with this algorithm. The results of the experimentation will provide guidance to the analyst in meeting the goals of management.

Assuming that an algorithm has been chosen, we suggest the following procedure to map the algorithm performance measures to parameter settings.

(1) Identify the parameters of the algorithm and their possible settings; (2) Select the datasets that resemble a wide variety of potential problems; (3) Design the experiment where:

\- the ‘factors’ in the experiment are the algorithm parameters, and the different datasets,

\- the different performance measures are the ‘response functions’ that are investigated by the experiment, and

\- the runs of the algorithm on each dataset constitute the ‘experiments’.

(4) v-Fold verification is used to generate replications of the experiment. (In v-fold verification, 1/v of the dataset is set aside as the test set while the rest is used as training data. By systematically choosing a totally different test set each time, v replications of the algorithm run on the same dataset are generated.)

(5) An ANOVA analysis is carried out for each performance measure that indicates the significance of the parameters for each performance measure as well as the direction and magnitude of the effect. (The analysis shows how much of the variation in each performance measure is due to the parameter settings, the dataset, and their interaction.)

(6) Tabulate the results in terms of significant parameters for each performance measure and the suggested setting for use by practitioners. Furthermore, the results give algorithm developers insight to the behavior of the algorithm.

In the remainder of this section, we apply this procedure to PrIL algorithm. We illustrate our approach with PrIL and six datasets from the data repository at UC Irvine: mushroom, vote, credit, wave, LED, LED + 17. They have been chosen to represent different domains and data characteristics like amount of noise, nonlinear effects, number of classification categories, number of attributes, continuous vs. categorical attributes. These are among the datasets frequently used in the machine learning and data mining community to compare the accuracy of different classification algorithms.

The PrIL parameters involved in the experiment and their settings are discussed next.

The ‘reliability requirement function’, described in Section 3, has the following three components.

(i) The ‘symmetry’ element refers to unequal minimum reliability requirements ( $R_{k}s$ ) for categories. We expect that asymmetric functions will increase the accuracy of category 1 at the expense of category 2.

(ii) The ‘shape’ element investigates the effect of the sequence in which the reliability requirements are reduced to the minimum levels. First reducing $r_{2}$ down to $R_{2}$ while keeping $r_{1}$ at maximum yields convex shape. The concave shape is obtained by reducing $r_{1}$ and $r_{2}$ simultaneously until $R_{1}$ is reached and then reducing $r_{2}$ further down to $R_{2}$ . Reducing both reliability requirements proportionally produces the linear shape.

(iii) The frequency element is to examine the effect of the number of steps in the reliability requirement function, i.e., the difference between the $r_{k}$ s of two successive hypothesis tests for a subset. It is set at 3 and 5.

Fig. 4 shows six asymmetric reliability requirement functions as applied to datasets. We will explain the above elements in terms of the reliability requirement function 1 as follows. With reliability requirement function 1, PrIL first tries to induce rules with reliability requirements of 0.99 for both categories. When all possible rules have been induced at that level the reliability requirements are reduced to $r_{1}=0.90$ and $r_{2}=0.80$ . Similarly, when no more rules can be induced at this level, $r_{1}$ is reduced to 0.80 and $r_{2}$ to 0.60. From this point on, the reliability requirement for category 1 is kept at 0.80 as $r_{2}$ is reduced successively to 0.40 and 0.20. Here, $R_{1}$ (minimum reliability requirement for category 1) is 0.80 and $R_{2}$ is 0.20, since $R_{1}\neq R_{2}$ this reliability requirement function is asymmetric. It is concave in shape since we reduce $r_{1}$ to $R_{1}$ before $r_{2}$ reaches its minimum. The only difference between function 1 and 4 is that function 4 skips the points $r_{1}=0.90$ , $r_{2}=0.80$ and $r_{1}=0.80$ , $r_{2}=0.40$ ; thus function 1 is considered to have high frequency.

![](/api/attachments/A5XATF4E/fulltext/images/62efe9320ddba06a647aa9ed55f1853f399cf7de65aa3591cee64a0efc728fd9.jpg)  
Fig. 4. Asymmetric reliability requirement functions for datasets mushroom, vote, credit and waveform the encircled functions refer to only encircled points.

At any point in the induction process, the sum of all required reliability levels should be $\geq 1$ . In the case of symmetric reliability requirement functions, the minimum reliability level has been set as 1/number of classification categories, which has been rounded to 35% in case of 3 categories. For the datasets with 2 categories (mushroom, credit and vote), the first set consists of edible, +, republican, respectively. In the waveform dataset, categories 1 and 2 comprise the first set, in LED and LED + 17 datasets, the first set consists of the first 5 digits, and the second consists of the rest. For asymmetric reliability requirement functions, first set of categories has a minimum required reliability of 0.80, and the second set 0.20. The asymmetric minimum reliability levels have been set at 0.70 and 0.10 for the LED and LED + 17 datasets.

For each dataset, 12 reliability requirement functions have been used corresponding to all combinations of the three elements [3].

M, Maximum number of attributes in a subset elimination rule, has been set at one and two. We consider this a parameter of specificity, because it determines how PrIL can partition the search space to find purer subsets. M is not increased beyond two since the complete enumeration of M-way combinations of attribute values would be computationally expensive.

n, Minimum number of cases required to post a rule in subset elimination, has been set at 5, 10 and 20. The purpose of such a restriction is to prevent rules from being formed when the sample size is too small to distinguish among the different reliability levels we would like to test. Higher n gives finer granularity in terms of reliability levels. Another expected effect of requiring high sample size is that we get a less specific tree with broader rules.

The number of attributes in the branching module has been set at 0, 1 and 2. Branching accounts for significant main effects and significant interaction effects. Beyond two branching attributes the PrIL tree will become too bushy, reducing the sample size in the branches. The marginal change in PrIL performance when going from one to two attributes as opposed to zero to one attribute will supply us with insights into the possible ‘diminishing returns’ feature of the branching attributes.

The branching attributes were determined according to their significance in the main effects logit model. Proc Catmod of SAS version 6 has been used for the logit analyses.

Option to disregard the minimum number of cases requirement to post a rule $(n)$ is initiated when there are less than n cases left in a branch and causes PrIL to classify them to the most likely classification category. It may increase the coverage of rules by undoing the effect of n but it may also reduce the accuracy.

We used a full factorial design where the factors are the PrIL parameters as shown in Table 1 [7]. The dataset constitutes the block beyond our control, in the context of design of experiments. Table 1 summarizes the settings of the factors in the experiment. Each dataset has five training and test sets, where training and test sets are mutually exclusive. A discussion of the datasets and the generation of training and test sets can be found in [4]. The experiment involves 12,960 runs and evaluation of the induced tree on the test set.

Table 1  
The experimental design

<table><tr><td>Factors</td><td>Settings</td><td>Levels</td></tr><tr><td>M (max. no attributes in a rule)</td><td>1, 2</td><td>2</td></tr><tr><td>n (min. no cases required for a rule)</td><td>5, 10, 20</td><td>3</td></tr><tr><td>Shape of reliability requirement function</td><td>convex, linear, concave</td><td>3</td></tr><tr><td>Symmetry of reliability requirement function</td><td>symmetric, asymmetric</td><td>2</td></tr><tr><td>Frequency of reliability requirement function</td><td>3, 5</td><td>2</td></tr><tr><td>Number of branching attributes</td><td>0, 1, 2</td><td>3</td></tr><tr><td>Option to disregard n</td><td>yes, no</td><td>2</td></tr><tr><td>Dataset (block)</td><td>mushroom, vote, credit, wave, LED, LED + 17</td><td>6</td></tr><tr><td>Replications</td><td></td><td>5</td></tr><tr><td>Total number of PrIL runs</td><td></td><td>12,960</td></tr></table>

Table 2
Summary of main effects for ANOVA models of different performance measures

<table><tr><td rowspan="2">Performance measures</td><td rowspan="2">M</td><td rowspan="2">n</td><td colspan="3">Reliability requirement function</td><td rowspan="2">Branching attributes</td><td rowspan="2">n Option</td><td rowspan="2">Mean</td></tr><tr><td>Shape</td><td>Symmetry</td><td>Frequency of points</td></tr><tr><td>Overall accuracy</td><td>↑ by 5.0</td><td>↓ by 0.4, 5 to 10; 0.4, 10 to 20</td><td>↓ by 2.7 lin to conc, 4.9 conc to conv</td><td>↑ by 3.0</td><td>↑ by 4.3</td><td>↑ by 6.8, 0 to 1; by 3.2, 1 to 2</td><td>↓ by 0.5</td><td>70.55</td></tr><tr><td>Accuracy of category 1</td><td>↑ by 9.1</td><td>↓ by 0.1, 5 and 10 to 20</td><td>↓ by 4.7 lin to conc, 3.6 conc to conv</td><td>↓ by 4.7</td><td>↑ by 3.7</td><td>↑ by 16.5, 0 to 1; by 7.4, 1 to 2</td><td>-</td><td>74.58</td></tr><tr><td>Accuracy of category 2</td><td>↑ by 4.3</td><td>↓ by 0.5, 5 to 10; 0.4, 10 to 20</td><td>↓ by 3.5 lin to conc, 4.1 conc to conv</td><td>↑ by 4.7</td><td>↑ by 5.0</td><td>↑ by 6.6, 0 to 1; by 2.0, 1 to 2</td><td>↓ by 0.7</td><td>69.41</td></tr><tr><td>Percent of undecided cases</td><td>↑ by 0.4</td><td>↑ by 0.3, 5 to 10; 0.2, 10 to 20</td><td>↓ by 0.2 lin to conc, 0.1 conc to conv</td><td>↓ by 0.5</td><td>↑ by 0.4</td><td>↑ by 0.2, 0 to 1; by 1.2, 1 to 2</td><td>↓ by 1.1</td><td>0.80</td></tr><tr><td>No. rules in the tree</td><td>↑ by 6.6</td><td>↓ by 5.3, 5 to 10; 3.3, 10 to 20</td><td>↓ by 1.0 lin to conc, 1.1 conc to conv</td><td>↓ by 0.2</td><td>↑ by 2.9</td><td>↓ by 7.1, 0 to 1; by 6.6, 1 to 2</td><td>↑ by 1.1</td><td>16.07</td></tr><tr><td>Average p-value</td><td>↓ by 0.08</td><td>↑ by 0.01, 5 to 10; 0.02, 10 to 20</td><td>↓ by 0.01 lin to conc, 0.01 conc to conv</td><td>↑ by 0.01</td><td>↓ by 0.02</td><td>↑ by 0.01, 0 and 1 to 2</td><td>-</td><td>0.87</td></tr></table>

## 5. Results of the experiment

An ANOVA was run for each of the performance measures described in Section 2, (1) overall accuracy, (2) category specific accuracy (divided into categories with high and lower $R_{k}$ ), (3) percent of undecided cases, (4) number of rules in the tree, and (5) average p-value. Proc ANOVA of SAS version 6 was used for the calculations. The model consists of the factors given in Section 4, namely:

(i) $M$ (maximum number of attributes in a rule), (i) n (maximum number of attributes in a rule), (ii) n (minimum number of cases required for a rule),

(iii) number of branching attributes,

(iv) shape of reliability requirement function,

(v) symmetry of reliability requirement function,

(vi) frequency of reliability requirement function,

(vii) option to disregard $n$ , and

(viii) dataset as main effects, two way effects and three way effects.

In each analysis, the dataset represented a major portion of the sum of squares. Many parameter settings and their interactions turned out to be significant at the 0.0001 level. We summarize the main effects in Table 2 where the columns represent the PrIL parameters, and the rows correspond to the performance measures. The mean value for each performance measure is given in the last column. The entries in the table are the differences between the effects of the values of PrIL settings, where the effects have been found significant at the 0.05 level according to the nonparametric Duncan test. The cells for the first row read as follows. When M is increased from 1 to 2 the overall accuracy goes up by 5.0, when n is increased from 5 to 10 overall accuracy drops by 0.4, and it drops another 0.4 points when n is increased to 20. Overall accuracy drops by 2.7 when shape of reliability requirement function is changed from linear to concave and drops another 4.9 points if it is changed from concave to convex. Symmetric functions give rise to an overall accuracy 3.0 higher than asymmetric ones. Specifying 5 points on the reliability requirement function (high frequency) increases overall accuracy by 4.4 over having 3 points in the function. An increase of 6.8 in overall accuracy is observed when number of branching attributes is increased from 0 to 1, another 3.2 increase is explained by increasing the branching attributes from 1 to 2. The option to disregard n decreases the overall accuracy by 0.5. The mean overall accuracy for all 12,960 runs was 70.55.

Effects that account for more than 1% of the corrected total sum of squares have been summarized in Fig. 5. An effect that is not underlined with dotted line indicates an ‘important’ main effect. The ‘important’ two-way interaction effects have been indicated by a line joining the two effects. A three-way interaction effect is pictured through an oval joining the three effects. If there is a dashed line under the effect, the main effect is not ‘important’ but its interactions are worthy of being in the figure. For example, the first diagram, depicting the important effects for overall accuracy, is explained as follows. Three main effects, shape, number of branching attributes and the dataset, each account for more than 1% of the corrected total sum of squares. The important two-way interactions are those between dataset and shape, dataset and number of branching attributes, dataset and M, and dataset and frequency of the reliability requirement function. There are no three-way effects that explain more than 1% of the corrected total sum of squares.

![](/api/attachments/A5XATF4E/fulltext/images/c8de67b26c5f15245a60081e11852803572e6849e702e5e4014cf0dca0265d6e.jpg)  
Fig. 5. Important effects for each performance measure.

The breakdown of the $R^{2}$ for the ANOVA models among the sources

<table><tr><td> $R^2$  attributed to</td><td>Up to 3-way interaction of PrIL settings</td><td>Dataset alone</td><td>Interaction of PrIL settings and dataset</td><td>Total model</td></tr><tr><td>Overall accuracy</td><td>8.1</td><td>78.6</td><td>9.5</td><td>96.2</td></tr><tr><td>Average p-value</td><td>19.3</td><td>5.8</td><td>23.5</td><td>48.6</td></tr><tr><td>% Undecided cases</td><td>30.0</td><td>4.5</td><td>26.4</td><td>60.9</td></tr><tr><td>Accuracy of category 1</td><td>23.5</td><td>36.4</td><td>26.4</td><td>79.0</td></tr><tr><td>Accuracy of category 2</td><td>7.9</td><td>73.9</td><td>11.9</td><td>93.7</td></tr><tr><td>No. rules in the tree</td><td>36.1</td><td>34.2</td><td>25.6</td><td>95.9</td></tr></table>

We see in Fig. 5 that M, number of branching attributes, symmetry and n (in order) are present in most of the diagrams. Viewing Table 3, which shows the various components of $R^{2}$ for the ANOVA models, we see that their effect is small compared to that attributed to the dataset and its interactions with the PrIL settings. For example, the dataset contributed 78.6% of the total model $R^{2}$ which was 96.2%. This result substantiates the fact that no matter how good the parameter settings are, the dataset imposes a limit on the attainable performance of the algorithm (as depicted in Fig. 1). Kohavi and John [5] present a method of setting algorithm parameters for a given dataset assuming that the performance measure is overall accuracy. The Statlog Project [6] has also studied the characteristics of datasets and the performance of algorithms.

## 6. Measures of performance and algorithm parameters

In Section 2, we mapped managerial goals into performance measures. In this section we map the performance measures into the parametric settings of the algorithm, PrIL, based upon experimental results. We do this by first summarizing the results in terms of the performance measures, and then providing in Table 4, guidelines to setting parameters.

As previously noted, M, the maximum number of attributes allowed in a rule in subset elimination, acts as the specificity parameter. By increasing M from 1 to 2, the number of rules increased since each rule identifies a more closely defined set of cases. And the accuracy, both overall and category specific also increases substantially when M is increased. However, as rules become more specific, the percentage of undecideds increases. The increase is very modest; however, it indicates that more specific and accurate rules result in larger subsets of cases as undecided. Also, the average p-value drops slightly, by 0.08, when M is increased. Note that the p-value takes the number of cases classified by the rule into account, since the variance of the correct classification rate is $[r(1-r)/\text{number of cases classified}]$ for a rule with reliability r. Therefore, the p-value it will be higher for a rule with fewer cases, the result of more rules and a higher M.

Increasing the minimum number of cases required to post a rule, n, has a decreasing effect on all accuracies, since it forces a bigger sample size for each rule during induction. This effect may not be important for large training sets, since n will constitute a small portion of the sample size. Also, n has greater effect on the accuracy of category 2 (the category with lower required reliability) than on accuracy of category 1. Larger n, as expected, increases the percent of undecided cases. This effect again is dependent on the training set sample size; for a large sample, the worst case of 20 undecided cases in each branch can be disregarded. Higher n also has a modest positive effect on the average p-value. Since higher n results in substantially fewer rules, the variances of individual correct classification percentages for each rule are smaller.

The form of the reliability requirement function does effect the performance measures. The linear form is associated with higher accuracy of all types. It gives rise to more rules but also to slightly more undecideds. The average p-value does not seem to be affected.

The requirement of equal minimum reliability, i.e., symmetric reliability requirement function, is a good feature unless one is focusing on the accuracy of one category. It decreases the number of undecideds, increases overall accuracy, and decreases effect on the number of rules modestly. Asymmetric reliability requirement functions, in which minimum reliability requirements for different classification categories, increase the accuracy of the categories with high $R_{k}$ at the expense of that for categories with low $R_{k}$ .

More points on the reliability requirement function, i.e., higher frequency, increases accuracy in general with a larger positive effect on the accuracy of category 2 (which has the lower reliability requirement if asymmetric function is used). However, this requirement increases the percentage of undecideds, fitting into the pattern of parameter effects that result in more partitioning of the population. But it does not increase number of rules as much as high M (up to two attributes in a rule) or as a low n (less number of cases required to post a rule).

Increasing the number of the branching attributes increases accuracy. However, the increase from 1 to 2 is much less than that from 0 to 1. The percentage of undecideds increases with more branching attributes, with a large increase from 1 to 2, due to the shrinking sample size of the training set for each branch. More branching consistently increases number of rules substantially. Everything said about more rules applies here as well. The average p-value does not seem to be affected by the number of branching attributes either.

The n option, i.e., the option to disregard n if number of cases left is less than n, reduces undecideds and slightly ‘waters down’ overall accuracy. It increases the number of rules, but does not have an effect on the average p-value.

Table 4 summarizes our findings as recommendations for parameter settings to satisfy performance measures, which are in turn linked to managerial goals. These settings are based on the main effects and the important interactions among PrIL parameters. The parameters that have an important main effect or were part of an important interaction have been typed in bold. The impact of the dataset affected only setting the number of branching attributes. The number of significant main effects from the logit analysis resulted in highest mean overall accuracy and category 2 accuracy levels for 5 out of 6 datasets. Therefore, we recommend that the results of a logit analysis results be used as a starting point. Note that mushroom dataset was not at all affected by the change of number of branching attributes in terms of the accuracies of all kind.

If two or more objectives are pursued at the same time, conflicting parameter settings can result. Objectives, for example, of a high overall accuracy and high average p-value objectives would lead to different settings for M, n, shape and frequency parameters. Although there appears to be a tradeoff, we should consider another aspect before deciding.

Table 4  
Parameter settings mapped to managerial goals

<table><tr><td rowspan="2">Performance measures</td><td rowspan="2">Desired</td><td rowspan="2">M</td><td rowspan="2">n</td><td colspan="3">Reliability requirement function</td><td rowspan="2">Branching attributes</td><td rowspan="2">n Option</td></tr><tr><td>Shape</td><td>Symmetry</td><td>Frequency of points</td></tr><tr><td>Overall accuracy</td><td>high</td><td>2</td><td>5</td><td>linear</td><td>1</td><td>5</td><td>as from logit analysis</td><td>0</td></tr><tr><td>Accuracy of category 1</td><td>high</td><td>1</td><td>5 or 10</td><td>convex</td><td>0</td><td>5</td><td>2</td><td>0 or 1</td></tr><tr><td>Accuracy of category 2</td><td>high</td><td>2</td><td>5</td><td>linear</td><td>1</td><td>5</td><td>as from logit analysis</td><td>0</td></tr><tr><td>% Undecided cases</td><td>low</td><td>1</td><td>5</td><td>convex</td><td>1</td><td>3</td><td>0</td><td>1</td></tr><tr><td>No. rules in the tree</td><td>low</td><td>1</td><td>20</td><td>convex</td><td>1</td><td>3</td><td>0</td><td>0</td></tr><tr><td>No. rules in the tree</td><td>high</td><td>2</td><td>5</td><td>linear</td><td>0</td><td>5</td><td>2</td><td>1</td></tr><tr><td>Var (correct classification)</td><td>low</td><td>1</td><td>20</td><td>convex</td><td>1</td><td>3</td><td>0</td><td>0</td></tr><tr><td>Average p-value</td><td>high</td><td>1</td><td>20</td><td>convex</td><td>0 or 1</td><td>3</td><td>0 or 1</td><td>0 or 1</td></tr></table>

A large sample from the training set will result in high accuracy even if the minimum number of cases needed to establish a rule, n is set at 20, because the specific niches that comprise only a small fraction of the dataset, will be represented by more cases in a large sample. If the sample size of the test data (or in a business setting the case volume to be processed by the tree) is large, the sample size per rule will keep the variance of proportion of correctly classified cases per rule small, regardless of the number of rules. Thus, we can set M at 2 and increase number of branching attributes, if necessary, without worrying about the variance of proportion of correctly classified cases for each rule.

## 7. Conclusions

A framework for translating managerial goals to the parameters of a data mining algorithm through performance measures has been established. The framework has been applied to a tree-induction algorithm, Probabilistic Inductive Learning, in the context of classification.

Fundamental to the process of linking performance measures to algorithm parameters is an experimental approach. The experiment was designed to explore the effect of different parameter settings on various aspects of performance, e.g., tree structure and confidence in the reliability of the rules. The experimentation employed datasets from the open literature with varying characteristics such as amount of noise, number of attributes and non-linear effects. The result was a set of guidelines for the user that mapped measures of performance into parameter settings, in this application for PrIL.

We have demonstrated that a business objective, cost of quality for a manufacturing process, could be expressed in terms of managerial goals. These goals in turn were translated into measures of performance for a data mining algorithm in the context of classification. However, we recognize that this process is a craft in the sense that it must be conducted by the manager and the analyst artfully and with ingenuity.

On the other hand, linking the parameters of a data mining algorithm to measures of performance can be done rigorously with statistical methods. We have proposed in Section 4 a set of performance measures that are general and not algorithm-specific. We have also discussed an experimental procedure using datasets from the open literature that can be replicated. This approach can be used on any data mining algorithm since they all have parameters.

When a manufacturer brings a product to market, we can expect that it will be tested in a variety of environments and an operating manual provided that guides the user in setting its controls, i.e., parameters for different measures of performance. We strongly recommend that developers of KDD software that is made available to the public either through the open literature or commercially, perform analyses such as we have described, and provide guidelines like we did for PrIL. It is much easier for the developers to provide the information than the potential user. In addition, software documentation that includes such an operating manual should provide a competitive advantage for the algorithm being marketed.

## References

[1] Data mining: Extending the information warehouse framework, IBM white paper on http://www.almaden.ibm.com/cgi-bin/stss/get/data-mining.

[2] U. Fayyad, G. Piatetsky-Shapiro, P. Smyth, Knowledge discovery and data mining: Towards a unifying framework, in: E. Simoudis, J. Han, U. Fayyad (Eds.), Proceedings of the 2nd International Conference on Knowledge Discovery and Data Mining, AAAI Press, Menlo Park, CA, 1996.

[3] F.Ö. Gür Ali, Probabilistic inductive learning: Induction of rules with reliability measures for decision support. PhD diss., Decision Sciences and Engineering Systems Department, Rensselaer Polytechnic Institute, 1994.

[4] F.Ö. Gür Ali, W.A. Wallace, Are we losing accuracy while gaining confidence in induced rules—an assessment of PrIL, in: Proceedings of the 1st International Conference on Knowledge Discovery and Data Mining, AAAI Press, Menlo Park, CA, 1995.

[5] R. Kohavi, G.H. John, Automatic parameter selection by minimizing estimated error, in: Prieditis, Russell (Eds.), Machine Learning: Proceedings of the 12th International Conference, Morgan Kaufmann Publishers, San Francisco, CA, 1995.

[6] D. Michie, D.J. Spiegelhalter, C.C. Taylor, Machine Learning, Neural and Statistical Classification, Ellis Horwood, London, UK, 1994.

[7] D.C. Montgomery, Design and Analysis of Experiments, Wiley, New York, 1991.

![](/api/attachments/A5XATF4E/fulltext/images/05f0f4a750956986dc1e9815af7a54fe286c28ff3af22ac3262d76590a58863d.jpg)

Dr. Özden Gür Ali recieved her BS in Industrial Engineering from Bosphorus University, Turkey (1989), and her MS (1990) and PhD (1994) degrees from Decision Sciences and Engineering Systems Dept. of Rensselaer Polytechnic Institute. Currently, she is working at GE Corporate Research and Development Center in Schenectady. Her research interests are data mining, its applications, learning quality functions from data, reliability of rules.

William A. Wallace is Professor of Decision Sciences and Engineering System at Rensselaer Polytechnic Institute, Troy, New York. He has over 20 years experience in research and development in management science and decision support systems with particular emphasis on crisis management. He was recently appointed Vice-Chair of the National Research Council's Committee on Advanced Information Technology for the Maritime Industry. He is presently engaged in research on intelligent decision aids, and the process of modelling.

---
otero_id: 4414
otero_key: "7ZAKQ6MF"
title: "A multi-objective genetic programming approach to developing Pareto optimal decision trees"
authors: "Huimin Zhao"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.12.011"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# A multi-objective genetic programming approach to developing Pareto optimal decision trees

Huimin Zhao <sup>⁎</sup>

Sheldon B. Lubar School of Business, University of Wisconsin-Milwaukee, P. O. Box 742, Milwaukee, WI 53201, United States

Received 1 March 2006; received in revised form 5 December 2006; accepted 15 December 2006 Available online 28 December 2006

## Abstract

Classification is a frequently encountered data mining problem. Decision tree techniques have been widely used to build classification models as such models closely resemble human reasoning and are easy to understand. Many real-world classification problems are cost-sensitive, meaning that different types of misclassification errors are not equally costly. Since different decision trees may excel under different cost settings, a set of non-dominated decision trees should be developed and presented to the decision maker for consideration, if the costs of different types of misclassification errors are not precisely determined. This paper proposes a multi-objective genetic programming approach to developing such alternative Pareto optimal decision trees. It also allows the decision maker to specify partial preferences on the conflicting objectives, such as false negative vs. false positive, sensitivity vs. specificity, and recall vs. precision, to further reduce the number of alternative solutions. A diabetes prediction problem and a credit card application approval problem are used to illustrate the application of the proposed approach. © 2006 Elsevier B.V. All rights reserved.

Keywords: Data mining; Binary classification; Decision tree; Cost-sensitive classification; Genetic programming; Multi-objective optimization; Pareto optimality

## 1. Introduction

As modern organizations can nowadays collect and maintain huge volumes of data, many of them have started to employ data mining techniques to mine their operational data for interesting patterns and decision models that could be used to support their decision making. Classification is a frequently encountered predictive data mining problem where a categorical dependent variable needs to be predicted based on a set of independent variables. Various classification techniques have been developed in such fields as multivariate statistical analysis, machine learning, and artificial neural networks [56,22] and applied to solve a variety of classification problems, such as workplace Web usage profiling [1], purchase behavior prediction [23], sales profile forecasting [52], deception detection [62], credit evaluation [18,48], bankruptcy prediction [45,51], bank failure prevention [46], intrusion detection [28,63], and medical diagnosis [33]. These classification techniques automatically induce prediction models, called classifiers, based on training examples with known outcomes. The trained classifiers can then be applied to predict the outcomes of new problem instances in the future.

Decision tree techniques have been widely used in building classification models as such models closely resemble human reasoning and are easy to understand [56]. Decision trees are sequential models, which logically combine a sequence of simple tests; each test compares a numeric attribute against a threshold value or a nominal attribute against a set of possible values. Such symbolic classifiers have an advantage over “black-box” models, such as neural nets, in terms of comprehensibility. The logical rules followed by a decision tree are much easier to interpret than the numeric weights of the connections between the nodes in a neural network. Decision makers tend to feel more comfortable to use models that they can understand.

Many real-world classification problems are costsensitive, meaning that different types of misclassification errors (false positive and false negative in a binary classification problem) are not equally costly [9,39,48]. For example, to a bank, approving a potentially bad loan is more costly than denying a good loan. Similarly, to a banking regulatory agent, leaving a problem bank unnoticed has more serious consequences than predicting a healthy bank as being problematic and thus scheduling unnecessary on-site examination. Such asymmetric costs need to be incorporated into the classifier training process such that the expected misclassification cost, rather than plain error rate, is sought to be minimized. A general method for cost-sensitive classifier training is to weight the different classes of training examples according to the costs such that more costly errors are penalized more heavily [6,53,58]. Using this method, different cost settings tend to result in very different decision trees, each of which may be superior to others in a particular range of cost settings.

It is often very difficult for decision makers to precisely pinpoint the costs of different types of misclassification errors, although they may be more confident in specifying a reasonable range for the cost ratio between false positive and false negative. For example, a banker may consider approving a bad loan to be between ten and twenty times more costly than denying a good loan. It is also possible that a decision maker's assessment of the cost ratio is dependent on the context of decision making. For example, a banking regulatory agent may assign a more extreme cost ratio when scheduling on-site examinations to prevent likely bank failures than when preparing for the consequences of eventual bank failures. Although bank failures are very costly, most of them can be prevented via supervision actions and only a few of them do occur. Thus, the decision maker may need to consider a range of possible cost ratios.

Since different decision trees may excel under different cost ratios, a set of decision trees should be developed and presented to the decision maker for consideration, if the costs of different types of misclassification errors are not precisely determined. In this paper, we propose a multi-objective genetic programming approach to developing such alternative decision trees. These alternatives are said to be nondominated or Pareto optimal, in that each of them is better than any other on at least one of two conflicting objectives, e.g., minimizing false negative rate vs. minimizing false positive rate. The system we have implemented also allows the decision maker to specify partial preferences on the two conflicting objectives to further reduce the number of alternative solutions. The preference (or tradeoff) can be similarly made on other pairs of performance measures, such as sensitivity vs. specificity and recall vs. precision, which have been typically employed in some domains, such as medical diagnosis and information retrieval. We have applied the system on several binary classification datasets publicly available from the UCI machine learning repository [37] and will present the results on two of these datasets. This paper makes a unique contribution by formulating costsensitive classification as a multi-objective optimization problem and providing an evolutionary computation approach.

The rest of the paper is organized as follows. We first briefly review the background and related literature on cost-sensitive classification and multi-objective evolutionary computation in the next section. We then present a diabetes prediction problem and a credit card application approval problem as motivational examples in Section 3. We then propose a multi-objective genetic programming approach to developing Pareto optimal decision trees and illustrate its application in the diabetes prediction and credit card application approval examples in Sections 4 and 5. Finally, we summarize the contributions of this work and discuss future research directions in Section 6.

## 2. Background and related work

In this section, we briefly review the background and related literature on cost-sensitive classification and multi-objective evolutionary computation.

## 2.1. Cost-sensitive classification

In this paper, we consider binary classification, where a binary dependent variable $y ,$ referred to as the class, needs to be predicted based on a vector of independent variables (also called attributes) $\mathbf { x } { = } ( x _ { 1 } , x _ { 2 } { , . . . , \ x _ { m } } )$ . A problem instance is considered positive (or negative) if its class y = 1 (or 0). A classification algorithm learns a prediction model, $f { \boldsymbol { : } } \mathbf { X } \longrightarrow y ,$ known as a classifier, from a training dataset consisting of previously solved problem instances, whose class values are known. The classifier is then applied to make classification decisions on other problem instances not present in the training dataset.

Table 1 Confusion matrix of a classifier

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Predicted class</td></tr><tr><td>1</td><td>0</td></tr><tr><td rowspan="2">Actual class</td><td>1</td><td>True Positive (TP)</td><td>False Negative (FN)</td></tr><tr><td>0</td><td>False Positive (FP)</td><td>True Negative (TN)</td></tr></table>

A probabilistic classifier makes the classification decision based on an estimated odds ratio, $\operatorname* { P r o b } ( y = 1 | \mathbf { x } = a ) /$ Prob( y= 0|x =a) [56]. By assuming conditional independence among the attributes given the class value, Naïve Bayes [7] simplifies the estimation of the odds ratio to Prob( y = 1) $\Pi _ { i = 1 } ^ { m }$ Prob $( x _ { i } { = } a _ { i } | y { = } 1 ) / \mathrm { P r o b } ( y { = } 0 )$ $\Pi _ { i = 1 } ^ { m } \mathrm { P r o b } ( x _ { i } { = } a _ { i } | y { = } 0 )$

A decision tree classifier follows a sequence of simple tests (at intermediate nodes) to reach a final classification decision (at a leaf.) Usually, the test at each intermediate node involves a single attribute. Since constructing optimal decision trees is NP-complete [19], heuristic approaches are needed. A typically used heuristic is greedy recursive partitioning, which selects the best branching attribute at each intermediate node based on some goodness measure evaluated using only the training instances reaching that node. Different decision tree learning algorithms mainly differ in their attribute selection methods. For example, the ID3, C4.5, and C5 family of algorithms uses information gain and gain ratio as criteria for selecting the splitting attribute [40,42], while other measures, such as G-statistic and Gini index, have been used in other algorithms [36].

The performance of a classifier can be assessed based on a confusion matrix (see Table 1) summarizing the numbers of different prediction outcomes. Without considering misclassification costs, the overall performance of a classifier is usually measured by its error rate (or inversely, accuracy,) defined as $\frac { \mathrm { F } \mathrm { \bar { P } } + \mathrm { F N } } { \mathrm { T P } + \mathrm { T N } + \mathrm { F P } + \mathrm { F N } } \ [ 5 7 ]$ However, when the two types of misclassification errors, false positive and false negative, have different costs, error rate is not an appropriate performance measure [9,39,48]. Then, the tradeoff between the two types of errors needs to be incorporated into the performance measure. One of such cost-sensitive performance measures is the average misclassification cost, defined as $\begin{array} { r } { \frac { \mathrm { F N } } { \mathrm { T P + T N + F P + F N } } \ C _ { \mathrm { F N } } + \frac { \mathrm { F P } } { \mathrm { T P + T N + F P + F N } } \ ( } \end{array}$ C<sub>FP</sub>, where $C _ { \mathrm { F N } } \left( \mathrm { o r } \ C _ { \mathrm { F P } } \right)$ is the unit cost of a false negative (or positive) error. There are also other ways to make tradeoffs. For example, a tradeoff between sensitivity and specificity is often made in medical problem diagnoses and communications, while information retrieval applications often consider a tradeoff between recall and precision [57]. The definitions of these alternative measures are listed in Table 2. Note that the term false positive has also been used to refer to 1 specificity in the literature [57].

The tradeoffs can be visualized, for example, on a Receiver Operating Characteristic (ROC) curve [12]. ROC was invented in the signal detection field to visualize the tradeoff between hit rate and false alarm rate over a noisy channel and has been widely applied in many domains (e.g., medical diagnosis) ever since. An ROC curve draws sensitivity against 1 specificity (see examples later.) If a classifier predicts an odds ratio between the two classes, a binary decision can be made by comparing the predicted odds ratio to a selected threshold, resulting in one point on the ROC curve. By varying the decision threshold, multiple points can be obtained to form an entire curve. The area under the curve (AUC) is sometimes used as an aggregate performance measure. A recall–precision curve, or a false negative–false positive curve, can be similarly generated.

There are two major approaches to building costsensitive classifiers: post hoc threshold tuning [48] and instance weighting [6,53,58]. In post hoc threshold tuning, a classifier is first trained as usual and then adjusted to account for the costs. This is equivalent to selecting a particular point on the ROC curve. In instance weighting, different types of instances in the training dataset are weighted according to the misclassification costs during classifier learning, such that the classifier strives to make fewer errors of the more costly type, resulting in lower average cost. For inherently cost-sensitive probabilistic classifiers, such as Naïve Bayes, instance weighting has no effect on the estimation of the conditional probabilities [57]. In other words, instance weighting based on a different cost ratio does not change the ROC curve and only results in a different point on the curve being selected (i.e., equivalent to post hoc threshold tuning).

Different measures for evaluating the false positive versus false negative tradeoff

<table><tr><td>Measures</td><td>Definition</td><td>Typical visualization method</td></tr><tr><td>False negative</td><td> $\frac{FN}{TP+TN+FP+FN}$ </td><td>False negative–false</td></tr><tr><td>False positive</td><td> $\frac{FP}{TP+TN+FP+FN}$ </td><td>positive curve</td></tr><tr><td>Sensitivity</td><td> $\frac{TP}{TP+FN}$ </td><td rowspan="2">ROC curve (sensitivity versus 1 – specificity)</td></tr><tr><td>Specificity</td><td> $\frac{TN}{TN+FP}$ </td></tr><tr><td>Recall (same as sensitivity)</td><td> $\frac{TP}{TP+FN}$ </td><td>Recall–precision curve</td></tr><tr><td>Precision</td><td> $\frac{TP}{TP+FP}$ </td><td></td></tr></table>

However, instance weighting has significant effects on decision trees. The structure of a decision tree may experience substantial changes, with different sets of attributes being selected, when the cost ratio varies. Previous experiments have shown that very different decision trees are learned via instance weighting under different cost ratios [53]. While it has been shown that Naïve Bayes tends to significantly outperform decision trees in terms of AUC [17], this does not mean decision trees are inferior to Naïve Bayes in dealing with cost-sensitive problems. When the tradeoff between the different types of misclassification errors is determined, competitive cost-sensitive decision trees can be learned via instance weighting, which has little effect on Naïve Bayes. When the tradeoff can not be precisely made, a set of decision trees needs to be learned using different possible cost ratios, such that each tree excels within a small range of the tradeoff. The full capacity of decision trees for dealing with a costsensitive classification problem should be assessed not by the ROC curve of a single tree, but by the convex hull of the ROC curves of multiple alternative trees [57].

## 2.2. Multi-objective evolutionary computation

Evolutionary computation is a heuristic search approach that simulates Darwin's principle of natural selection. Genetic algorithms [16] and genetic programming [2,26] are two of many techniques for such simulation of evolution. They have been widely applied to solve difficult optimization problems. These techniques evolve a population of individuals, which are candidate solutions to a problem, from generation (iteration) to generation, seeking to gradually converge towards the best possible individuals. This procedure usually employs several key ingredients, including selection, crossover, and mutation, which mimic aspects of natural evolution, natural selection, and differential reproduction [2]. Individuals are assessed by a goodness measure, referred to as fitness. A selection mechanism is then used to give fitter individuals better chances to survive and to produce descendants (i.e., survival of the fittest). Crossover exchanges some characteristics across multiple (usually two) selected individuals (parents) to generate new ones (children). Mutation brings in innovation by changing some characteristics of a selected individual. Fig. 1 illustrates a basic evolutionary algorithm.

Genetic algorithms and genetic programming follow essentially the same procedure, but differ in their representations of individuals. Genetic algorithms usually represent an individual with a fixed-length binary string. Genetic programming systems are much more flexible and powerful and are capable of representing a candidate solution to a problem with any possible (variablesize) computer program [2]. Some frequently used representations are trees, lists, and graphs. The area of genetic programming has grown very rapidly in the few years since 1992 [2]. Some recent applications of genetic programming include negotiation policy discovery [8], financial forecasting [54], and personalized Web search ranking functions [10,11], just to name a few.

![](/api/attachments/7ZAKQ6MF/fulltext/images/6be4e258431bc48a748b6e7beae03e8befba2dec4d4996daac61e62e40cb5402.jpg)  
Fig. 1. Basic evolutionary algorithm.

As genetic programming can represent a solution with a variable-size tree, it has been applied to induce decision trees for classification problems. Koza [25] first used genetic programming in learning decision trees for a particular classification problem, the weather problem from Quinlan [40]. Since then, several genetic programming systems have been proposed for general decision tree learning [5,27,29,31,32,47,55,60]. Tür and Güvenir [55] proposed a simple representation for a binary classification problem that has only binary attributes. Shirasaka et al. [47] and Zhao and Shirasaka [60] proposed a binary tree representation, where an intermediate node branches into two sub-trees based on a simple test involving a single attribute. Bot and Langdon [5] proposed a linear classification tree representation, where an intermediate node is a linear combination of multiple attributes. Loveard and Ciesielski proposed and compared several ways to represent a multi-class classification problem [31] and later extended the representations to include nominal attributes [32]. Li et al. [29] have applied genetic programming in a cost-sensitive classification problem by consolidating the two types of misclassification errors into a single objective. This requires the decision maker to precisely specify the costs of false positive and false negative errors.

As evolutionary computation is a population-based approach, it is suitable for simultaneously evolving towards multiple alternative Pareto optimal solutions for a multi-objective optimization problem [50,64,65]. In such a problem, multiple conflicting objectives, $f _ { 1 } , f _ { 2 } , . . . ,$ $f _ { M } ,$ need to be minimized (or maximized) simultaneously [3]. A solution $x _ { 1 }$ is said to dominate another solution $x _ { 2 } ,$ if $x _ { 1 }$ is at least as good as $x _ { 2 }$ on every objective and is better than $x _ { 2 }$ on at least one objective; formally, ∀i = 1, $2 , . . . , M : f _ { i } \left( x _ { 1 } \right) \leq f _ { i } \left( x _ { 2 } \right) \land \exists i { = } 1 , 2 , . . . , M : f _ { i } ( x _ { 1 } ) < f _ { i } ( x _ { 2 } )$ . A solution x is said to be non-dominated or Pareto optimal if there is no other feasible solution that dominates x. The set of all Pareto optimal solutions is referred to as the Pareto front. If the decision maker can precisely weight the relative importance of the objectives, the multiple objectives can be consolidated such that the problem reduces into a single-objective one [29]. Otherwise, multiple alternative solutions should be presented to the decision maker for consideration. The set of alternatives is reduced if the decision maker has approximate preferences (tradeoffs) on the objectives [14].

Several multi-objective evolutionary algorithms and systems have been proposed in recent years [50,64,65]. Some examples are MultiGen [34], RAND (a random search algorithm), FFGA (Fonseca and Fleming's multiobjective EA), NPGA (the Niched Pareto Genetic Algorithm), HLGA (Hajela and Lin's weighted-sum based approach), VEGA (the Vector Evaluated Genetic Algorithm), NSGA (the Nondominated Sorting Genetic Algorithm), SOEA (a single-objective evolutionary algorithm using weighted-sum aggregation), and SPEA (the Strength Pareto Evolutionary Algorithm) [65]. The major difference between a single-objective evolutionary algorithm and a multi-objective evolutionary algorithm is in the fitness evaluation mechanism. In a singleobjective genetic algorithm, the fitness function is a simple function (e.g., identity) of the objective function. In a multi-objective evolutionary algorithm, the fitness function accounts for all objectives simultaneously and is related to the relative non-dominance of a candidate solution. More recently, some of the fitness evaluation methods developed for multi-objective evolutionary algorithms have been applied in genetic programming [4,43]. Recent applications of multi-objective evolutionary computation include software component and Web services design [20] and market segmentation [30], just to name a few. The application of multi-objective evolutionary computation in building Pareto optimal decision trees to capture the tradeoff between different types of misclassification errors in a cost-sensitive classification problem has not been explored yet.

## 3. Motivational examples

We will use a diabetes prediction problem [49] and a credit card application approval problem [41] for illustration and empirical evaluation purposes. We choose these examples as they have been widely used in the data mining literature for evaluating classification techniques and are good examples of cost-sensitive classification problems.

## 3.1. Pima Indians diabetes

This dataset was originally donated by Vincent Sigillito (Applied Physics Laboratory, John Hopkins University) and is publicly available from the UCI machine learning repository [37]. The data were collected by the National Institute of Diabetes and Digestive and Kidney Diseases. The dataset contains data about 768 female patients, who were at least 21 years old, had Pima Indian heritage, and lived near Phoenix, Arizona. Each patient is characterized by eight physiological measurements and medical test results, listed in Table 3. The diagnostic task is to predict whether the patient shows signs of diabetes according to the World Health Organization criteria. This is therefore a binary (positive or negative) classification problem.

Table 3  
Attributes of the Pima Indians diabetes problem

<table><tr><td rowspan="2">No.</td><td rowspan="2">Name</td><td rowspan="2">Description</td><td colspan="2">Range</td></tr><tr><td>Min</td><td>Max</td></tr><tr><td>1</td><td>Preg</td><td>Number of times pregnant</td><td>0</td><td>17</td></tr><tr><td>2</td><td>Plas</td><td>Plasma glucose concentration in an oral glucose tolerance test</td><td>0</td><td>199</td></tr><tr><td>3</td><td>Pres</td><td>Diastolic blood pressure (mm/Hg)</td><td>0</td><td>122</td></tr><tr><td>4</td><td>Skin</td><td>Triceps skin fold thickness (mm)</td><td>0</td><td>99</td></tr><tr><td>5</td><td>Insu</td><td>2-Hour serum insulin (mu/U/ml)</td><td>0</td><td>846</td></tr><tr><td>6</td><td>Mass</td><td>Body mass index  $(kg/m^2)$ </td><td>0</td><td>67.1</td></tr><tr><td>7</td><td>Pedi</td><td>Diabetes pedigree function</td><td>0.078</td><td>2.42</td></tr><tr><td>8</td><td>Age</td><td>Age (years)</td><td>21</td><td>81</td></tr></table>

This problem is cost-sensitive, as the two types of misclassification errors (false positive and false negative) are not equally costly. In disease diagnosis, ROC curve is often used to visualize the performance of a classifier and the tradeoff is usually made between sensitivity and specificity. Fig. 2 shows the ROC curves [12] generated by Naïve Bayes [7] and the C4.5 decision tree learner [42] with instance weighting under three cost ratios using the Weka data mining software [57]. The ROC curve generated by Naïve Bayes remains the same under different cost ratios, indicating that Naïve Bayes is insensitive to the cost ratio and therefore instance weighting has the same effect as post hoc threshold adjustment on Naïve Bayes. However, the ROC curves generated by C4.5 under different cost ratios are significantly different. Each decision tree dominates others in a particular range and is dominated by others elsewhere. The decision trees have significantly different structures. If a physician has difficulty in precisely pinpointing the cost ratio, or needs to change the tradeoff depending on the context of decision making, a set of alternative decision trees should be provided to the physician for consideration.

## 3.2. Credit card application approval

This dataset was introduced by Quinlan [41]. It contains 690 records (307 positive and 383 negative) and 15 attributes (6 numerical and 9 nominal). The source is confidential. All attribute names and values have been changed to meaningless symbols to protect confidentiality of the data. The problem is costsensitive, as approving a potentially bad credit card application is more costly than denying a potentially good credit card application.

## 4. A multi-objective genetic programming approach

We consider a multi-objective genetic programming (MOGP) approach for two major reasons. First, an evolutionary computation approach has the potential to approach global optimal solutions over time. It has been shown that genetic programming tends to generate accurate decision trees within reasonable time periods [5,29,31,32,55]. Second, as genetic programming is a population-based methodology, it can simultaneously evolve towards multiple alternative non-dominated solutions [50,64,65] and is thus particularly suitable for cost-sensitive problems where a range of tradeoffs needs to be explored. Evolutionary computation is typically time consuming. However, for developing alternative Pareto optimal decision trees, this disadvantage of genetic programming over other greedy approaches lessens. With a greedy, recursive partitioning algorithm, training needs to be repeated many times with instance weighting under numerous possible tradeoffs, thus the training time dramatically increases. The proposed MOGP system simultaneously evolves towards multiple Pareto optimal trees and does not dramatically increase the training time as compared to a single-objective genetic programming system. In this section, we present in detail the proposed MOGP system, which has been implemented in Java and tested on several classification problems.

![](/api/attachments/7ZAKQ6MF/fulltext/images/0080e79fc5dfab165cd7f3225f9dd0fd28e32c878cea8c7df8f9117a63e5a53d.jpg)

![](/api/attachments/7ZAKQ6MF/fulltext/images/ed7a93a3a6b6c72eef223f965093e51dc834be96170fa845743eb874625a75c2.jpg)  
Fig. 2. ROC curves generated by Naïve Bayes and C4.5 under three cost ratios for the Pima Indians diabetes problem. (a) Naïve Bayes (b) C4.5.

Table 4  
Types, terminals, and functions of the MOGP system

<table><tr><td>Type</td><td>Terminal</td><td>Function</td></tr><tr><td>Integer</td><td>Attribute</td><td></td></tr><tr><td>Real</td><td>Value</td><td></td></tr><tr><td>Binary</td><td>Class</td><td>Node</td></tr></table>

## 4.1. Solution encoding

We apply strongly typed genetic programming [35] in the solution encoding. The basic genetic programming has no mechanism to restrict the programs (solutions) it generates to only valid ones, where the functions operate on appropriate data types, and can result in unnecessarily long search times and/or unnecessarily poor generalization performance, if the programs manipulate multiple data types and contain functions designed to operate on particular data types [35]. Strong typing enforces data type constraints and ensures that only valid solutions may be generated.

A decision tree can be naturally represented with a tree structure. There are two kinds of tree nodes, terminals and functions. Table 4 lists the terminals and functions, along with their data types. Terminals are either attributes (integer), values (real), or classes (binary.) Recall that a binary classification problem is described by a binary class y and a vector of attributes $\mathbf { x } { = } ( x _ { 1 } , x _ { 2 } { , . . . , x _ { m } } )$ . An attribute terminal is an integer number in the range [1, m], representing an attribute number. A value terminal is a real number in the range [0, 1), representing a threshold value (after a linear transformation) for a numeric attribute or the index (after a conversion into integer) of a possible value for a nominal attribute. A class terminal is binary, representing a leaf node in a decision tree.

The node function represents an intermediate node of a decision tree. It takes four arguments and returns a binary result; its signature is N: integer × real × binary × binary → binary. It can be represented as a four-tuple, $N { = } ( a , \nu , L , R )$ , where a is an attribute terminal, v is a value terminal, and L and R are class terminals or node functions. Note that since both the type of a class terminal and the output type of a node function are binary (see Table 4), L and R can be either class terminals or node functions. $\operatorname { I f } \mathbf { X } _ { a }$ is a numeric attribute with a domain [l, u],

$$
N = \left\{ \begin{array}{l l} L & \text { if } x _ {a} \leq (u - l) v + l; \\ R & \text { otherwise }. \end{array} \right.
$$

If $\mathbf { X } _ { a }$ is a nominal attribute with an array V of k possible values,

$$
N = \left\{ \begin{array}{l l} L & \text { if } x _ {a} = V [ k v ]; \\ R & \text { otherwise }. \end{array} \right.
$$

Fig. 3 illustrates the MOGP representation of a subtree for the Pima Indian diabetes problem. The attributes Preg, Skin, and Mass are numbered 1, 4, and $^ { 6 , }$ while their threshold values 5, 29, and 34.5 are transformed into 0.29, 0.29, and 0.51 after the [0, 1) linear normalization (see Table 3). This representation leads to binary univariate decision trees [47,60]. It can be easily shown that any univariate decision tree can be represented with an equivalent binary tree.

![](/api/attachments/7ZAKQ6MF/fulltext/images/5abe0d77cf1b16e582a35ebc8db6f8aacc60d96291e4333e230814b9e0953944.jpg)  
Fig. 3. MOGP representation of a sub-tree for the Pima Indians diabetes problem. (a) Sub-tree (b) MOGP representation.

## 4.2. Fitness evaluation and objective tradeoffs

We formulate cost-sensitive classification as a multiobjective optimization problem, where two conflicting $_ \mathrm { o b j e c t i v e s } , f _ { 1 }$ and $f _ { 2 } ,$ need to be minimized (or maximized) simultaneously. Some examples of objective pairs are false negative and false positive, sensitivity and specificity, and recall and precision, described in Table 2. Without loss of generality, we assume $f _ { 1 }$ and $\mid f _ { 2 }$ to be sensitivity and specificity in the following discussion.

In the MOGP system, the fitness of an individual (a candidate decision tree) is assigned on the basis of its relative non-dominance. Since the tournament selection method (described in the next sub-section) is used in the evolution procedure, what is essential is not the absolute value, but the rank, of the fitness [43]. Thus, all nondominated individuals in the current population are assigned rank one, while individuals dominated by one or more others are assigned rank two or higher.

The decision maker often needs to focus on a particular region of the Pareto front by providing (partial) preference information on the two objectives [14]. Assuming that the decision maker considers the ratio between the relative importance $\operatorname { o f } f _ { 1 }$ and that of $f _ { 2 }$ to be in the range $[ l _ { 1 : } \ l _ { 2 } , \ u _ { 1 : } \ u _ { 2 } ]$ , where $l _ { 1 } { \geq } 0 , \ l _ { 2 } { > } 0 .$ $u _ { 1 } > 0 , u _ { 2 } \geq 0$ , and $l _ { 1 } / l _ { 2 } \leq u _ { 1 } / u _ { 2 } .$ , a decision tree $t _ { 1 }$ dominates another decision tree $t _ { 2 }$ if and only if

$$
\begin{array}{l} (l _ {1} f _ {1} (t _ {1}) + l _ {2} f _ {2} (t _ {1}) \geq l _ {1} f _ {1} (t _ {2}) + l _ {2} f _ {2} (t _ {2}) \wedge u _ {1} f _ {1} (t _ {1}) \\ \quad + u _ {2} f _ {2} (t _ {1}) > u _ {1} f _ {1} (t _ {2}) + u _ {2} f _ {2} (t _ {2})) \vee (l _ {1} f _ {1} (t _ {1}) \\ \quad + l _ {2} f _ {2} (t _ {1}) > l _ {1} f _ {1} (t _ {2}) + l _ {2} f _ {2} (t _ {2}) \wedge u _ {1} f _ {1} (t _ {1}) \\ \quad + u _ {2} f _ {2} (t _ {1}) \geq u _ {1} f _ {1} (t _ {2}) + u _ {2} f _ {2} (t _ {2})). \end{array}
$$

Some special scenarios are:

• Case $1 \colon l _ { 1 } = 0 , \ u _ { 2 } = 0 . \ t _ { 1 }$ dominates $t _ { 2 }$ if and only if $( f _ { 2 } ( t _ { 1 } ) \ge f _ { 2 } ( t _ { 2 } ) \land f _ { 1 } ( t _ { 1 } ) > f _ { 1 } ( t _ { 2 } ) ) \lor ( f _ { 2 } ( t _ { 1 } ) > f _ { 2 } ( t _ { 2 } ) \land$ $f _ { 1 } ( t _ { 1 } ) \geq f _ { 1 } ( t _ { 2 } ) )$

This is the scenario where the decision maker provides no information on the tradeoff between sensitivity and specificity. All Pareto optimal decision trees will be sought and presented to the decision maker for consideration.

• Case $2 \colon l _ { 1 } { > } 0 , u _ { 2 } { = } 0 . t _ { 1 }$ dominates $t _ { 2 }$ if and only if $\begin{array} { r } { ( l _ { 1 } f _ { 1 } ( t _ { 1 } ) + l _ { 2 } f _ { 2 } ( t _ { 1 } ) \ge l _ { 1 } f _ { 1 } ( t _ { 2 } ) + l _ { 2 } f _ { 2 } ( t _ { 2 } ) \land f _ { 1 } ( t _ { 1 } ) > f _ { 1 } ( t _ { 2 } ) ) \lor } \end{array}$ $( l _ { 1 } f _ { 1 } ( t _ { 1 } ) + l _ { 2 } f _ { 2 } ( t _ { 1 } ) > l _ { 1 } f _ { 1 } ( t _ { 2 } ) + l _ { 2 } f _ { 2 } ( t _ { 2 } ) \land f _ { 1 } ( t _ { 1 } ) \geq f _ { 1 } ( t _ { 2 } ) )$

This is the scenario where the decision maker considers sensitivity to be at least $l _ { 1 } / l _ { 2 }$ times more important than specificity.

• Case 3: $l _ { 1 } { = } 0 , u _ { 2 } { > } 0 . t _ { 1 }$ dominates $t _ { 2 }$ if and only if $( f _ { 2 } ( t _ { 1 } ) \geq f _ { 2 } ( t _ { 2 } ) \land u _ { 1 } f _ { 1 } ( t _ { 1 } ) + u _ { 2 } f _ { 2 } ( t _ { 1 } ) > u _ { 1 } f _ { 1 } ( t _ { 2 } ) +$ $u _ { 2 } f _ { 2 } ( t _ { 2 } ) ) \vee ( f _ { 2 } ( t _ { 1 } ) > f _ { 2 } ( t _ { 2 } ) \wedge u _ { 1 } f _ { 1 } ( t _ { 1 } ) + u _ { 2 } f _ { 2 } ( t _ { 1 } ) \geq$ $u _ { 1 } f _ { 1 } ( t _ { 2 } ) + u _ { 2 } f _ { 2 } ( t _ { 2 } ) )$ This is the scenario where the decision maker considers specificity to be at least $u _ { 2 } / u _ { 1 }$ times more important than sensitivity.

• Case 4: $l _ { 1 } { > } 0 , u _ { 2 } { > } 0 , l _ { 1 } / l _ { 2 } { < } u _ { 1 } / u _ { 2 } . t _ { 1 }$ dominates $t _ { 2 }$ if and only if $( l _ { 1 } f _ { 1 } ( t _ { 1 } ) + l _ { 2 } f _ { 2 } ( t _ { 1 } ) \ge l _ { 1 } f _ { 1 } ( t _ { 2 } ) + l _ { 2 } f _ { 2 } ( t _ { 2 } ) \land$ $u _ { 1 } f _ { 1 } ( t _ { 1 } ) + u _ { 2 } f _ { 2 } ( t _ { 1 } ) > u _ { 1 } f _ { 1 } ( t _ { 2 } ) + u _ { 2 } f _ { 2 } ( t _ { 2 } ) ) \lor ( l _ { 1 } f _ { 1 } ( t _ { 1 } ) +$ $l _ { 2 } f _ { 2 } ( t _ { 1 } ) > l _ { 1 } f _ { 1 } ( t _ { 2 } ) + l _ { 2 } f _ { 2 } ( t _ { 2 } ) \land u _ { 1 } f _ { 1 } ( t _ { 1 } ) + u _ { 2 } f _ { 2 } ( t _ { 1 } ) \ge$ $u _ { 1 } f _ { 1 } ( t _ { 2 } ) + u _ { 2 } f _ { 2 } ( t _ { 2 } ) )$ This is the scenario where the decision maker considers sensitivity to be between $l _ { 1 } / l _ { 2 }$ and $u _ { 1 } / u _ { 2 }$ times more (or less) important than specificity.

• Case 5: $l _ { 1 } { > } 0 , u _ { 2 } { > } 0 , l _ { 1 } / l _ { 2 } { = } u _ { 1 } / u _ { 2 } . t _ { 1 }$ dominates $t _ { 2 }$ if and only if $l _ { 1 } f _ { 1 } ( t _ { 1 } ) + l _ { 2 } f _ { 2 } ( t _ { 1 } ) > l _ { 1 } f _ { 1 } ( t _ { 2 } ) + l _ { 2 } f _ { 2 } ( t _ { 2 } )$ This is the scenario where the decision maker considers sensitivity to be exactly $l _ { 1 } / l _ { 2 }$ times more (or less) important than specificity. The MOGP system then reduces into a single-objective genetic programming system [29]. A single best decision tree is sought and recommended to the decision maker.

## 4.3. Genetic operations

There are three major genetic operations: reproduction, crossover, and mutation. These operations all require a selection mechanism. The selection mechanism selects parents based on their fitness values such that fitter individuals get better chances to survive and to produce descendants. As described above, the fitness value of an individual is its rank of relative nondominance. The tournament selection method has been found to generally perform well in other genetic programming systems [2,15] and is thus adopted in MOGP. When a tournament is held to select a parent, a small number of participants are randomly drawn from the current population and the winner, the fittest individual in the tournament, is selected. The selection mechanism of MOGP also takes the size of a candidate tree into account. If two trees have identical fitness value, the smaller tree is preferred. This preference of smaller trees helps alleviate potential overfitting problem (i.e., a model has unnecessarily high complexity and relatively low generalizability [56]).

As a previous study [65] has found that incorporating elitist selection significantly improves the performance of a multi-objective evolutionary algorithm, we also incorporate this mechanism in MOGP. It can be viewed as a special selection and reproduction mechanism, where a selected individual on the current Pareto front, rather than a winner of the tournament selection, reproduces itself. MOGP can also maintain an external archive of all Pareto optimal solutions found so far over all generations, as some of the current Pareto optimal solutions may not survive through later generations.

![](/api/attachments/7ZAKQ6MF/fulltext/images/a314d8272acb476af6277ad4c4fc81f582ddc56847f64a1d456b69ab1576a8cd.jpg)  
Fig. 4. Crossover in MOGP.

Crossover operates on two individuals. It combines the characteristics of two parents by swapping a selected sub-tree of one parent with a selected sub-tree of the other. Mutation operates on one individual. It randomly selects a point in the tree and replaces the sub-tree starting at that point with a new randomly generated sub-tree. The crossover operation is illustrated in Fig. 4. The mutation operation is illustrated in Fig. 5. Note that the sub trees still remain valid trees after the crossover and mutation operations in Figs. 4 and 5.

![](/api/attachments/7ZAKQ6MF/fulltext/images/b2b3e43a825aa9af197d721133162ffd08d7a32563c62d16b55910e1b35aa068.jpg)  
Fig. 5. Mutation in MOGP.

## 4.4. Major parameters

Table 5 describes the major parameters of the MOGP system (the program and the Java source code are available from the author.) The system can run under one of two evolution engines, generational and steady state. A generational engine creates an entire new generation before replacing the current generation. A steady state engine immediately replaces an individual with a newly created one, which is then available for creating the next individual; the notion of a new generation is when the entire population has been refreshed. Other parameters defining the evolution procedure include the population size, the termination criteria (e.g., number of generations to be evolved,) the tournament size used in the tournament selection, and the probabilities a new individual is to be generated via reproduction, elitist, crossover, or mutation. The system also allows the user to choose whether to maintain a global archive of the Pareto optimal solutions generated during all generations so far.

Parameters of the MOGP system

<table><tr><td>Parameter</td><td>Description</td></tr><tr><td>Evolution engine</td><td>The type of evolution engine. A generational engine creates an entire new generation to replace the old generation. A steady state engine immediately replaces an individual when a new individual is created.</td></tr><tr><td>Max depth</td><td>The maximum depth of any evolved decision tree.</td></tr><tr><td>Max depth at creation</td><td>The maximum depth of an initially created decision tree.</td></tr><tr><td>Max depth at mutation</td><td>The maximum depth of a sub-tree created as a result of mutation.</td></tr><tr><td>Elitist rate</td><td>The probability of creating a new individual via reproduction of an elitist (i.e., an individual on the current Pareto front.)</td></tr><tr><td>Mutation rate</td><td>The probability of creating a new individual via mutation based on a selected individual. The selection method is tournament.</td></tr><tr><td>Reproduction rate</td><td>The probability of creating a new individual via reproduction of a selected individual. The probabilities of elitist, mutation, reproduction, and crossover sum to 1.</td></tr><tr><td>Tournament size</td><td>The number of individuals in the tournament selection.</td></tr><tr><td>Population size</td><td>The number of individuals in the entire population.</td></tr><tr><td>Generations</td><td>The number of generations during the evolution.</td></tr><tr><td>Random seed</td><td>The starting seed of the pseudo random number generator used. The system clock in milliseconds is given as the default.</td></tr><tr><td>Display interval</td><td>The interval between generations to be visualized.</td></tr><tr><td>Display</td><td>The visualization method: ROC, recall–precision, or false negative–false positive.</td></tr><tr><td>Preference on</td><td>Preference is specified between sensitivity and specificity, between recall and precision, or between false negative and false positive.</td></tr><tr><td>Preference range</td><td>The range of preference ratio between the selected pair of performance measures.</td></tr><tr><td>Archiving</td><td>Whether to maintain a global archive of the Pareto optimal solutions generated during all generations so far.</td></tr><tr><td>Training dataset</td><td>The classification dataset used for training.</td></tr><tr><td>Load from</td><td>The prefix of the file for loading a previously saved generation as the starting population.</td></tr><tr><td>Load generation</td><td>The generation to be loaded.</td></tr><tr><td>Save to</td><td>The prefix of the file for saving intermediate generations.</td></tr><tr><td>Save interval</td><td>The interval between generations to be saved.</td></tr></table>

There are parameters that control the maximum possible depth of a tree (or sub-tree) created initially, at any generation, or as a result of mutation. These parameters set constraints on the complexity of resulting decision tree classifiers and constitute another mechanism that helps prevent serious overfitting. The system supports three ways for specifying objective preferences (tradeoffs) and three typical visualization methods. The Pareto front will be visualized periodically. The user can also choose to periodically save the evolution results, which can be used as starting populations in subsequent runs.

Fig. 6 shows the recommended default parameter values. These recommendations are based on our pilot testing and are in general consistent with previous guidelines. For example, small mutation and reproduction rates and large crossover rates have been found to be generally effective [2].

![](/api/attachments/7ZAKQ6MF/fulltext/images/a4a3bf7500228345ffe899196a5c2f6f99046137f24f2b0fd6fd56c49754a413.jpg)  
Fig. 6. Default parameter values of the MOGP system.

## 5. Applications

We have applied the proposed methodology in developing Pareto optimal decision trees for several binary classification problems collected in the UCI machine learning repository [37], including ionosphere, breast cancer, Wisconsin breast cancer, chess king– rook-vs-king–pawn, credit card application approval, congressional voting records, hepatitis, horse colic, labor relations, sonar, German credit (Statlog project), heart disease (Statlog project), and Pima Indians diabetes. In this section, we describe the application to the Pima Indians diabetes and the credit card application approval problems introduced earlier only, in the interest of space. Detailed results on these and other problems are available from the author. All results presented below were generated using the default parameter values shown in Fig. 6. The machine used is a Dell Optiplex/GX260 workstation with a Pentium 4 CPU running at 2.27 GHz and 512 Mb RAM.

## 5.1. Pima Indians diabetes

The MOGP system provides three ways, false negative–false positive curve, recall–precision curve, and ROC curve, to visualize the performance of the alternative non-dominated decision trees found so far. Fig. 7 shows some examples. On the ROC curve (Fig. 7(c)), for example, each alternative decision tree is represented by one point, with its vertical and horizontal coordinates corresponding to sensitivity and 1 specificity of the decision tree, respectively. These visualization methods are conventionally employed in different domains. For example, ROC is typically used in medical diagnosis while recall–precision is typically used in information retrieval. The decision maker can choose a familiar visualization method.

To compare MOGP with other classification methods, we have run C4.5 (J4.8) decision tree [42], backpropagation neural network [44], and support vector machine [21,38] in the Weka data mining software [57] using the default parameter settings. The AUCs of the classifiers generated by the methods are, in descending order, 0.925 (MOGP), 0.888 (C4.5), 0.872 (backpropagation neural network), and 0.719 (support vector machine).

The evolution of MOGP is illustrated in Fig. 8. The Pareto front formed by the non-dominated decision

(b)

(a)  
![](/api/attachments/7ZAKQ6MF/fulltext/images/0d1f6b4fb801c0e018e6c7d92363597264caa74f2462730c8f9bee21d51fd07a.jpg)  
Fig. 7. Three visualization methods. (a) False negative–false positive curve (b) Recall–precision curve (c) ROC curve.

trees found so far moves towards the upper left corner on the ROC curve over time. The evolution is dramatic during the early generations and then gradually slows down. The Pareto front gradually stabilizes. We observed little improvements after 1000 generations for the Pima Indians diabetes problem. 73 alternative nondominated decision trees were found after 1000 generations (Fig. 7(c)).

(a)  
(b)  
![](/api/attachments/7ZAKQ6MF/fulltext/images/72d36cbc3a703b96ae53a43d26c1bd190b89af85ec027328bdb6af19efce9de1.jpg)  
Fig. 8. Evolution of MOGP. (a) After 1 generation (b) After 10 generations (c) After 100 generations.

The MOGP system allows the decision maker to specify (partial) tradeoffs to reduce the number of alternatives that need to be considered. The tradeoff can be made between false negative and false positive, between sensitivity and specificity, or between recall and precision, depending on the decision maker's familiarity. Fig. 9 shows some examples of tradeoff between sensitivity and specificity for the Pima Indians

![](/api/attachments/7ZAKQ6MF/fulltext/images/74ca39cde8ce73822b60b6d467a14de83de70ccc77e8e1b90d311b44c43f9659.jpg)

(a)  
(b)  
![](/api/attachments/7ZAKQ6MF/fulltext/images/00a35c7b9f49c44fe540574f7f9a4355d0f8e16fc4a3f7da9749b8fdfa29531f.jpg)  
Fig. 9. Tradeoff between sensitivity and specificity. (a) Specificity is at least as important as sensitivity. (b) Specificity is between one and five times more important than sensitivity. (c) Specificity is as important as sensitivity.

diabetes problem. The tradeoff may be open on one side. For example, if a physician feels that specificity is at least as important as sensitivity, the number of alternative decision trees that should be considered reduces to 16. The tradeoff may be restricted to a closed range. For example, if a physician feels that specificity is

(a)

between one and five times more important than sensitivity, the number of alternatives further reduces to only four. The tradeoff may also be precisely specified. The MOGP system then reduces into a single-objective genetic programming system and recommends only one best decision tree to the decision maker. For example, if a physician considers sensitivity and specificity to be equally important, a single tree is recommended. Fig. 10 shows two sample decision trees generated under different tradeoffs between sensitivity and specificity. They share some common nodes and differ in other parts.

![](/api/attachments/7ZAKQ6MF/fulltext/images/1c638a00a8ee1fcd58b0d5615f0bad062e8f4ae369cc762201b84146daca13a2.jpg)  
Fig. 10. Sample decision trees generated under different tradeoffs between sensitivity and specificity. (a) When specificity is as important as sensitivity. (b) When specificity is five times more important than sensitivity.

## 5.2. Credit card application approval

Just as for the Pima Indians diabetes problem, the MOGP system provides three ways to visualize the performance of the alternative non-dominated decision trees found so far. The decision maker can choose a familiar visualization method. To compare MOGP with other classification methods, we have run C4.5 (J4.8) decision tree, back-propagation neural network, and support vector machine in the Weka data mining software using the default parameter settings. The AUCs of the classifiers generated by the methods are, in descending order, 0.988 (MOGP), 0.974 (backpropagation neural network), 0.938 (C4.5), and 0.868 (support vector machine).

As MOGP evolves, the Pareto front formed by the non-dominated decision trees found so far moves towards the upper left corner on the ROC curve over time. The evolution is dramatic during the early generations and then gradually slows down. The Pareto front gradually stabilizes. We observed little improvements after 1000 generations for the credit card application approval problem. 33 alternative nondominated decision trees were found after 1000 generations.

The MOGP system allows the decision maker to specify (partial) tradeoffs to reduce the number of alternative decision trees that need to be considered. The tradeoff can be made between false negative and false positive, between sensitivity and specificity, or between recall and precision, depending on the deci sion maker's familiarity. The tradeoff may be open on one side. For example, if a decision maker feels that false positive is at least as important as false negative, the number of alternative decision trees that should be considered reduces to 14. The tradeoff may be restricted to a closed range. For example, if a decision maker feels that false positive is between one and five times more important than false negative, the number of alternatives further reduces to seven. The tradeoff may also be precisely specified. The MOGP system then reduces into a single-objective genetic programming system and recommends only one best decision tree to the decision maker.

## 6. Conclusion and future research

Decision tree classifiers are widely used in classification applications due to their high comprehensibility. Real-world classification problems are often cost-sensitive and the decision maker often needs to explore the tradeoff between different types of misclassification errors within a reasonable range. Different decision trees may excel in different ranges of the tradeoff. Hence, a cost-sensitive classification problem should be treated as a multi-objective optimization problem and multiple alternative solutions, rather than a single solution, should be provided to the decision maker for consideration. We have presented a multi-objective genetic programming system for developing such Pareto optimal decision trees. The system allows the decision maker to make tradeoffs in several ways based on his/her best estimation and recommends a set of alternative solutions accordingly. As an evolutionary approach, the system visualizes the progress of the evolution of solutions such that the decision maker can decide to stop the procedure when satisfactory solutions have been found or when the solutions on the front appear to have stabilized. Thus, this paper makes a novel contribution by formulating cost-sensitive classification as a multi-objective optimization problem and providing an evolutionary computation approach.

This study opens up several avenues for future research. First, while we have focused on developing nondominated decision trees, the resulting classifiers can be validated using various methods, such as holdout, crossvalidation, leave-one-out, and bootstrap [24].

Second, while our current system induces univariate trees (also called orthogonal trees) only, it can be extended to learn multivariate trees (also called oblique trees) [5,59,61]. It has been shown that constructing multivariate tests, usually involving linear combinations of the original attributes, at the intermediate nodes of decision trees alleviates the representational bias of decision tree models and may improve classification accuracy. It would be interesting to investigate the effect of incorporating multivariate tests on the performance of genetically evolved Pareto optimal decision trees.

Third, while we have focused on binary classification problems, the proposed approach can be extended to deal with multiple-class problems [31,32]. For such problems, the system needs to allow the decision maker to specify a matrix of pair-wise tradeoffs between objectives and provide methods for visualizing Pareto optimal solutions in a multi-dimensional space.

Fourth, while we have proposed a general methodology and focused on demonstrating the usefulness of multi-objective genetic programming in developing Pareto optimal decision trees, more elaborate engineering effort may be devoted to optimizing the efficiency and scalability of the system to develop practical tools in the future. Such tools may then be applied in real-world largescale data mining projects to further validate the real utility of the proposed methodology. There are a variety of techniques for improving the efficiency and scalability of genetic programming. For example, as a populationbased methodology, genetic programming is amenable to parallel implementations [13]. There are also techniques, such as dynamic subset selection and limited error fitness, which have been developed specifically for improving the efficiency and scalability of genetic programming for supervised learning [15]. With an efficient and scalable MOGP tool, it will then be feasible to conduct large-scale experiments to empirically compare MOGP and other greedy decision tree learning algorithms in building Pareto optimal trees. Such empirical evaluation wil provide valuable insights into the relative merits of different approaches.

## Acknowledgements

The multi-objective genetic programming system presented in this paper was implemented by extending the single-objective GPsys system developed by Adil Qureshi. The author is also grateful to the anonymous referees for their valuable suggestions.

## References

[1] M. Anandarajan, Profiling Web usage in the workplace: a behavior-based artificial intelligence approach, Journal of Management Information Systems 19 (1) (2002) 243–266.

[2] W. Banzhaf, P. Nordin, R.E. Keller, F.D. Francone, Genetic Programming: An Introduction, Morgan Kaufman, San Francisco, CA, 1998.

[3] A. Ben-Tal, Characterization of Pareto and lexicographic optimal solutions, Multiple Criteria Decision Making, Theory and Applications, Lecture Notes in Economics and Mathematical Systems, vol. 177, Springer-Verlag, Berlin, Germany, 1980, pp. 1–11.

[4] S. Bleuler, M. Brack, L. Thiele, E. Zitzler, Multiobjective genetic programming: reducing bloat using SPEA2, Proceedings of the 2001 Congress on Evolutionary Computation, 2001, pp. 536–543.

[5] M.C.J. Bot, W.B. Langdon, Application of genetic programming to induction of linear classification trees, Proceedings of the Third European Conference on Genetic Programming, 2000, pp. 247–258.

[6] P. Domingos, MetaCost: A general method for making classifiers cost sensitive, Proceedings of the Fifth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 1999, pp. 155–164.

[7] P. Domingos, M. Pazzani, Beyond independence: conditions for the optimality of the simple Bayesian classifier, Proceedings of the Thirteenth International Conference on Machine Learning, 1996, pp. 105–112.

[8] G. Dworman, S.O. Kimbrough, J.D. Laing, On automated discovery of models using genetic programming: bargaining in a three-agent coalitions game, Journal of Management Information Systems 12 (3) (1996) 97–125.

[9] C. Elkan, The foundations of cost-sensitive learning, Proceedings of the Seventeenth International Joint Conference on Artificial Intelligence, 2001, pp. 973–978.

[10] W. Fan, M.D. Gordon, P. Pathak, Genetic programming-based discovery of ranking functions for effective Web search, Journal of Management Information Systems 21 (4) (2005) 37–56.

[11] W. Fan, P. Pathak, L. Wallace, Nonlinear ranking function representations in genetic programming-based ranking discovery for personalized search, Decision Support Systems 42 (3) (2006) 1338–1349.

[12] T. Fawcett, ROC Graphs: Notes and Practical Considerations for Data Mining Researchers, HPL-2003-4, Intelligent Enterprise Technologies Lab, Hewlett-Packard, Palo Alto, CA, 2003.

[13] G. Folino, C. Pizzuti, G. Spezzano, Improving induction decision trees with parallel genetic programming, Proceedings of the Tenth Euromicro Workshop on Parallel, Distributed and Network-based Processing, 2002, pp. 181–187.

[14] C.M. Fonseca, P.J. Fleming, Multiobjective optimization and multiple constraints handling with evolutionary algorithms. Part 1: A unified formulation, IEEE Transactions on Systems, Man, and Cybernetics 28 (1) (1998) 26–37.

[15] C. Gathercole, An Investigation of Supervised Learning in Genetic Programming, PhD Dissertation, University of Edinburgh, 1998.

[16] J. Holland, Adaptation in Natural and Artificial Systems, MIT Press, Cambridge, MA, 1975.

[17] J. Huang, C.X. Ling, Using AUC and accuracy in evaluating learning algorithms, IEEE Transactions on Knowledge and Data Engineering 17 (3) (2005) 299–310.

[18] Z. Huang, H. Chen, C. Hsu, W. Chen, S. Wu, Credit rating analysis with support vector machines and neural networks: a market comparative study, Decision Support Systems 37 (4) (2004) 543–558.

[19] L. Hyafil, Construction optimal binary decision trees is NPcomplete, Information Processing Letters 5 (1) (1976) 15–17.

[20] H. Jain, H. Zhao, N.R. Chinta, Web service identification — a multi-objective genetic algorithm based approach, Proceedings of the Second Workshop on e-Business, 2003, pp. 351–361.

[21] S.S. Keerthi, S.K. Shevade, C. Bhattacharyya, K.R.K. Murthy, Improvements to Platt's SMO Algorithm for SVM Classifier Design, Technical Report, vol. CD-99-14, Control Division, Department of Mechanical and Production Engineering, National University of Singapore, 1999.

[22] M.Y. Kiang, A comparative assessment of classification methods, Decision Support Systems 35 (4) (2003) 441–454.

[23] E. Kim, W. Kim, Y. Lee, Combination of multiple classifiers for the customer's purchase behavior prediction, Decision Support Systems 34 (2) (2003) 167–175.

[24] R. Kohavi, A study of cross-validation and bootstrap for accuracy estimation and model selection, Proceedings of the Fourteenth International Joint Conference on Artificial Intelligence, 1995, pp. 1137–1143.

[25] J.R. Koza, Concept formation and decision tree induction using the genetic programming paradigm, Proceedings of the First Workshop on Parallel Problem Solving from Nature, 1991, pp. 124–128.

[26] J.R. Koza, Genetic Programming: On the Programming of Computers by Means of Natural Selection, The MIT Press, Cambridge, MA, 1992.

[27] J. Li, FGP: a Genetic Programming Based Tool for Financial Forecasting, PhD Thesis, University of Essex, 2001.

[28] X.-B. Li, A scalable decision tree system and its application in pattern recognition and intrusion detection, Decision Support Systems 41 (1) (2005) 112–130.

[29] J. Li, X. Li, X. Yao, Cost-sensitive classification with genetic programming, Proceedings of the 2005 Congress on Evolutionary Computation, vol. 3, 2005, pp. 2114–2121.

[30] Y. Liu, S. Ram, R. Lusch, A unified market segmentation method for generating Pareto optimal solution sets, Proceedings of the Fifteenth Workshop on Information Technologies and Systems, 2005, pp. 219–224.

[31] T. Loveard, V. Ciesielski, Representing classification problems in genetic programming, Proceedings of the 2001 Congress on Evolutionary Computation, 2001, pp. 1070–1077.

[32] T. Loveard, V. Ciesielski, Employing nominal attributes in classification using genetic programming, Proceedings of the Fourth Asia-Pacific Conference on Simulated Evolution and Learning, 2002, pp. 487–491.

[33] P. Mangiameli, D. West, R. Rampal, Model selection for medical diagnosis decision support systems, Decision Support Systems 36 (3) (2004) 247–259.

[34] S.K. Mirrazavi, D.F. Jones, M. Tamiz, MultiGen: an integrated multiple-objective solution system, Decision Support Systems 36 (2) (2003) 177–187.

[35] D.J. Montana, Strongly typed genetic programming, Evolutionary Computation 3 (2) (1995) 199–230.

[36] S.K. Murthy, Automatic construction of decision trees from data: A multi-disciplinary survey, Data Mining and Knowledge Discovery 2 (4) (1998) 345–389.

[37] D.J. Newman, S. Hettich, C.L. Blake, C.J. Merz, UCI Repository of Machine Learning Databases, http://www.ics.uci.edu/\~mlearn/ MLRepository.html, 1998.

[38] J. Platt, Fast training of support vector machines using sequential minimal optimization, in: B. Schölkopf, C. Burges, A. Smola (Eds.), Advances in Kernel Methods — Support Vector Learning, MIT Press, 1998.

[39] F. Provost, T. Fawcett, R. Kohavi, The case against accuracy estimation for comparing induction algorithms, Proceedings of the Fifteenth International Conference on Machine Learning, 1998, pp. 445–453.

[40] J.R. Quinlan, Induction of decision trees, Machine Learning 1 (1) (1986) 81–106.

[41] J.R. Quinlan, Simplifying decision trees, International Journal of Man-Machine Studies 27 (1987) 221–234.

[42] J.R. Quinlan, C4.5: Programs for Machine Learning, Morgan Kaufmann, San Francisco, 1993.

[43] K. Rodríguez-Vázquez, C.M. Fonseca, P.J. Fleming, Identifying the structure of nonlinear dynamic systems using multiobjective genetic programming, IEEE Transactions on Systems, Man and Cybernetics: Part A. Systems and Humans 34 (4) (2004) 531–545.

[44] D.E. Rumelhart, G.E. Hinton, R.J. William, Learning representations by back-propagating errors, Nature 323 (1986) 533–536.

[45] Y.U. Ryu, W.T. Yue, Firm bankruptcy prediction: experimental comparison of isotonic separation and other classification approaches, IEEE Transactions on Systems, Man and Cybernetics: Part A. Systems and Humans 35 (5) (2005) 727–737.

[46] S. Sarkar, R.S. Sriram, Bayesian models for early warning of bank failures, Management Science 47 (11) (2001) 1457–1475.

[47] M. Shirasaka, Q. Zhao, O. Hammarmi, K. Kuroda, K. Saito, Automatic design of binary decision trees based on genetic programming, Proceedings of the Second Asia-Pacific Conference on Simulated Evolution and Learning, 1998.

[48] A.P. Sinha, J.H. May, Evaluating and tuning predictive data mining models using receiver operating characteristic curves, Journal of Management Information Systems 21 (3) (2005) 249–280.

[49] J.W. Smith, J.E. Everhart, W.C. Dickson, W.C. Knowler, R.S. Johannes, Using the ADAP learning algorithm to forecast the onset of diabetes mellitus, Proceedings of the Symposium on Computer Applications and Medical Care, 1988, pp. 261–265.

[50] N. Srinivas, K. Deb, Multiobjective optimization using nondominated sorting in genetic algorithms, Evolutionary Computation 2 (3) (1994) 221–248.

[51] T.K. Sung, N. Chang, G. Lee, Dynamics of modeling in data mining: interpretive approach to bankruptcy prediction, Journal of Management Information Systems 16 (1) (1999) 63–86.

[52] S. Thomassey, A. Fiordaliso, A hybrid sales forecasting system based on clustering and decision trees, Decision Support Systems 42 (1) (2006) 408–421.

[53] K.M. Ting, An Instance-weighting method to induce costsensitive trees, IEEE Transactions on Knowledge and Data Engineering 14 (3) (2002) 659–665.

[54] E. Tsang, P. Yung, J. Li, EDDIE-automation, a decision support tool for financial forecasting, Decision Support Systems 37 (4) (2004) 559–565.

[55] G. Tür, H.A. Güvenir, Decision tree induction using genetic programming, Proceedings of the Fifth Turkish Symposium on Artificial Intelligence and Neural Networks, 1996.

[56] S.M. Weiss, C.A. Kulikowski, Computer Systems That Learn — Classification and Prediction Methods from Statistics, Neural Nets, Machine Learning, and Expert System, Morgan Kaufmann, 1991.

[57] I.H. Witten, E. Frank, Data Mining: Practical Machine Learning Tools and Techniques, 2nd EditionMorgan Kaufmann, 2005.

[58] B. Zadrozny, J. Langford, N. Abe, Cost-sensitive learning by cost-proportionate example weighting, Proceedings of the IEEE International Conference on Data Mining, 2003, pp. 435–442.

[59] H. Zhao, S. Ram, Constrained cascade generalization of decision trees, IEEE Transactions on Knowledge and Data Engineering 16 (6) (2004) 727–739.

[60] Q. Zhao, M. Shirasaka, A study on evolutionary design of binary decision trees, Proceedings of the 1999 Congress on Evolutionary Computation, 1999, pp. 1988–1993.

[61] H. Zhao, A.P. Sinha, An efficient algorithm for generating generalized decision forests, IEEE Transactions on Systems, Man, and Cybernetics: Part A. Systems and Humans 35 (5) (2005) 754–762.

[62] L. Zhou, J.K. Burgoon, D.P. Twitchell, T. Qin, J. Nunamaker, A comparison of classification methods for predicting deception in computer-mediated communication, Journal of Management Information Systems 20 (4) (2004) 139–165.

[63] D. Zhu, G. Premkumar, X. Zhang, C. Chu, Data mining for network intrusion detection: A comparison of alternative methods, Decision Sciences 32 (4) (2001) 635–660.

[64] E. Zitzler, Evolutionary Algorithms for Multiobjective Optimization: Methods and Applications, PhD thesis, ETH Zurich, Switzerland, 1999.

[65] E. Zitzler, K. Deb, L. Thiele, Comparison of multiobjective evolutionary algorithms: empirical results, Evolutionary Computation 8 (2) (2000) 173–195.

![](/api/attachments/7ZAKQ6MF/fulltext/images/12a2d19cdc145f3243c05bb7bc6cc256c05116cea2fe12b5dec9f293224e4962.jpg)

Huimin Zhao is an Assistant Professor of Management Information Systems at the Sheldon B. Lubar School of Business, University of Wisconsin-Milwaukee. He earned his Ph. D. in Management Informa tion Systems from the Uni versity of Arizona in 2002. His current research interests are in the areas of data mining and data integration. His research has been published in several journals, including Communications of the ACM, IEEE Transac-

tions on Knowledge and Data Engineering, IEEE Transactions on Systems, Man, and Cybernetics, Information Systems, Data and Knowledge Engineering, and Journal of Management Information Systems.

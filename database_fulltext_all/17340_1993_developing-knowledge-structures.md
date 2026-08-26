---
otero_id: 17340
otero_key: "SBZV5GCF"
title: "Developing knowledge structures"
authors: "James V. Hansen; Gary J. Koehler; William F. Messier; Jane F. Mutchler"
year: "1993"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)90040-a"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Developing knowledge structures

# A comparison of a qualitative-response model and two machine-learning algorithms

James V. Hansen

Brigham Young University, Provo UT, USA

Gary J. Koehler

William F. Messier, Jr.

University of Florida, Gainesville FL, USA

Jane F. Mutchler

University of Arizona, Tucson AZ, USA

Many unstructured decision-making problems are too complex to be solved by existing analytical methods. Organizations commonly rely on human expertise to solve such prob-

![](/api/attachments/SBZV5GCF/fulltext/images/490c88e31725c318df5dbcb7dd99d087fb39e0f1d3061d6cd8941ff40ed3254c.jpg)

James V. Hansen received a B.S. degree in mathematics from Brigham Young University and a Ph.D in Computer and Information systems from the Graduate School of Business at the University of Washington, Seattle.

He was formerly a Senior Research Scientist at Battelle Institute and member of the faculty at Indiana University. He is currently a Professor in the Marriott School of Management at Brigham Young University.

His research interests are in data modeling, machine learning and information and control.

Dr. Hansen is a member of the Association for Computing Machinery, the IEEE Computer Society, TIMS and the American Association for Artificial Intelligence.

![](/api/attachments/SBZV5GCF/fulltext/images/b399815931f42ca1721c3b8517d11337d9648bc2d729713c17529d24b65e8b92.jpg)

Gary J. Koehler is a Professor in the Department of Decision and Information Sciences at the University of Florida. He received his Ph.D. at Purdue University in 1973. In 1979 he co-founded Micro Data Base Systems, Inc. and was its President and CEO until 1987. He has published in a number of journals including Management Science, Decision Sciences, Operations Research, the SLAM Journal of Control and Optimization, Discrete Applied Mathematics, Naval Re search Logistics, European Journal of Operations Research, the Journal of Finance and Managerial and Decision Economics.

Correspondence to: Professor James V. Hansen, Marriott School of Management, Brigham Young University, Provo, UT 84602, USA.

lems. Human expertise is presumed to utilize specialized knowledge structures, and recent research in artificial intelligence has sought to devise machine-learning procedures that can derive knowledge structures from sets of data that represent problem-domain exemplars. Concurrently, research in statistical methods has resulted in the development of qualitative-response models that can be applied to some of the same kinds of problems addressed by machine-learning models—especially those that involve a classification decision. Using a difficult audit decision problem requiring expertise, this paper reports on a study comparing performance of two machine-learning algorithms and logistic regression, a widely-used qualitative-response method for classification analysis. A recently-developed machine-learning algorithm, NEWQ, is found to yield the best performance characteristics.

Keywords: Machine learning; Knowledge structures; Qualitative-response models; Artificial intelligence.

![](/api/attachments/SBZV5GCF/fulltext/images/3e822fd699b75048a60d6257b2a6b521cadedd83f348d5734b6f286575e5e4dc.jpg)

William F. Messier, Jr. is Professor of Accounting at the Fisher School of Accounting, University of Florida. He received his B.B.A. from Siena College, M.S. from Clarkson University and M.B.A. and D.B.A. from Indiana University. Dr. Messier has been a visiting professor at the University of Michigan and the Norwegian School of Economics and Business Administration. He is currently the Co-Editor of the Journal of Accounting Literature. Dr Messier's research interests

include studying auditors' judgment processes and various issues related to audit decision aids. He has published in numerous journals including The Accounting Review, Journal of Accounting Research, Auditing: A Journal of Practice and Theory, Management Science, Decision Sciences, Communications of the ACM, and other accounting and computer science journals.

![](/api/attachments/SBZV5GCF/fulltext/images/b78b8d990289d536c9feedae0648a81599453dc0b48eb368c65d3df4890f01d4.jpg)

Jane F. Mutchler received her undergraduate and Master's degrees from the University of South Florida. In 1983 she received her Ph.D. in accountancy from the University of Illinois at Urbana-Champaign. Professor Mutchler has taught at The Ohio State University, the University of Arizona and is currently an associate professor of accounting and MIS at Pennsylvania State University. Her research interests center on auditors' going-concern opinion decisions. She has published in Journal of Accounting Research, The Accounting Review, Contemporary Accounting Research, Auditing: A Journal of Practice and Theory, and Journal of Expert Systems.

## 1. Introduction

The study of decision making has long been the central focus of management science. Routine, structured decision making has often been modeled successfully by applying quantitative optimization methods such as linear programming. Unstructured decision making, on the other hand, has generally been found to be too complex to be representable by existing analytic methods $[25]$ . Consequently, organizations typically rely on human experts to handle complex decision making. This is a limitation because such experts are a scarce resource. It would be useful to find ways of making their expertise more widely available.

Because of the potentially large payoffs, finding methods for supporting complex decision making has become a major area of research. Recent developments in artificial intelligence (AI) have generated interest in the potential of expert systems for dealing with complexity by representing the knowledge structures used by experts. Yet experience has shown that capturing those knowledge structures can be very time consuming and difficult $[2]$ .

## 1.1. Knowledge acquisition

Knowledge-acquisition methods have basically followed two approaches: Direct elicitation and machine learning. Direct elicitation has generally relied on techniques such as structured interviews or protocol analysis. Direct methods have been widely used and have achieved some important successes (cf. [2]). There are, however, difficulties associated with direct elicitation methods. They are often tedious and time-and-effort consuming [22]. Moreover, difficulties accrue because the expert often does not know exactly how he makes decisions, or is not experienced in thinking about the structure and process used. As a result, the knowledge base captured from the expert is likely to suffer from omissions and inconsistencies that must then be laboriously tracked down and rectified.

In an effort to mitigate these problems, intelligent editors such as ACQUINAS [25], MOLE [9], and ASTEK [12] have been devised to aid in the direct elicitation of expert knowledge.

An alternative is suggested by the development of machine-learning algorithms. Algorithms that induce production (“if-then”) rules from analyzing sets of examples from the problem domain have been proposed by several researchers. These algorithms include the concept learning system [11], genetic algorithm [10], inductive dichotomizer [26,27], AQ15 [23], CART [4], BACON [18], CRIS [19], and CONIS [30]. While these algorithms differ substantively, they commonly invoke the following procedures:

(1) identification of a set of information that human experts use in performing a decision-making tasks;

(2) gathering a set of example cases, where each case consists of values for attributes used in the analysis (hypothesized or real), as well as the decision made by the experts;

(3) selecting a subset of the set of example cases, called the training set, as input to the machine-learning algorithm, which then generates a model;

(4) testing the model on data sets not included in the training set, in order to measure its performance.

Statistical methods such as regression, discriminant analysis, and pattern recognition are also inductive in nature and have realized widespread use in predicting phenomena based on analysis of historical data. Sample mean and variance commonly form the nucleus of statistical models, and their output is usually in the form of mathematical expression as opposed to sets of decision rules.

## 1.2. Recent research

A number of recent research studies have examined the performance of machine-learning algorithms. Michalski et al. [23] applied the AQ15, an induction algorithm to data sets on breast cancer recurrence data. Results showed an accuracy rate of 68% for AQ15, as compared to 64% for expert physicians. A pruned-tree procedure improved the accuracy of the algorithm to 72%.

Braun and Chandler [3] used ACLS to derive a set of rules to predict an expert stock market analyst's predictions of the market and to predict the actual movement of the stock market. This study found that, on average, the rule set correctly predicted the expert's predictions and the market's movements at levels of $51.5\%$ and $64.4\%$ , respectively. Results were not compared to any alternative technique.

Messier and Hansen [21] compared predictions of an inductive algorithm (ID3) with individual and group judgments, as well as discriminant analysis. Using two sets of training data, one on bankruptcy and one on loan default, it was found that the induction algorithm performed best in terms of predicting the outcome on holdout data.

More recently, the results of broader testing have been reported by Weiss and Kapouleas [32]. These analysts compared methods from statistical pattern recognition, neural nets, as well as “machine-learning”. The authors define machine learning – as we do – as any computerized method that produces solutions in the form of production rules or decision trees. The results of testing on sets of data from three different medical problem domains showed dominance by the machine-learning methods.

Chandler et al. [5] compared ID3 with a qualitative-response model, PROBIT, in two experiments. Mixed results were found.

Tam [30] developed an induction system, CONIS, which is based on the principles of q-morphism developed by Holland [10]. CONIS performance Is compared to that of discriminant analysis and logistic regression using a single data set. CONIS was able to predict with 94% accuracy on holdout data, versus 88% for a clustering algorithm and 84% for logistic regression.

While these studies do not comprise an exhaustive list, they are representative of recent efforts to empirically evaluate machine-learning algorithms.

An important limitation of the type of study reported above is worth noting. With the exception of the Weiss and Kapouleas [32] work, these studies generally relied on a single train-and-test experiment. The single-test-and-train method has the advantage of simplicity and can work well for large samples. Yet, for small and moderate-size sample sets – which tend to be the rule – the computed error rate can vary significantly from the true error rate. Better estimates are achieved by multiple train-and-test experiments using cross-validation or bootstrapping methods [7,4].

The use of different algorithms, varying problem domains, and different methodologies can, in the short run, make general assessments as to what algorithms work best inconclusive, and even confusing. Yet, over the long run continuing empirical work should make the answers to those questions more tractable as results begin to converge and more replication of methods and problem domains is found in reported studies. Moreover, improvements to inductive algorithms are often suggested by limitations that are observed in completing empirical studies.

Our report is intended to contribute to this learning process. In particular, our study uses a set of data on an important audit-decision making problem to compare the performance of a machine-learning algorithm (ID3) with a widely-used qualitative response algorithm (LOGIT), as well as a newly developed hybrid algorithm (NEWQ).

ID3 was selected to represent that class of algorithm that produces a decision tree based on production rules. It has been used in several previous studies, and has been the subject of much of the work on pruning of decision trees. ID3 and CART have had a significant influence on machine-learning research, and the two algorithms are quite similar. A major difference is that the CART algorithm yields strictly binary trees, while ID3 partitions on attribute values.

Logistic regression was selected to represent a class of qualitative-response models emanating from statistics. The choice of logistic regression was also influenced by the fact that it has been used in a number of research studies on audit decision making. It was deemed of interest to determine if a machine-learning model might improve on the results of the Mutchler [24] study.

The principal contribution in the development of NEWQ is that it utilizes discriminant analysis and machine-learning techniques. It can be viewed as a hybrid in that it can use the same partitioning procedures as ID3, as well as conventional discriminant functions. The remainder of our paper is outlined as follows: Section 2 presents a discussion of the two machine-learning algorithms used in this study. Section 3 briefly summarizes logistic regression. Section 4 discusses performance measures as a foundation for motivating the research methodology used in this study. Section 5 outlines the problem domain used for testing, along with the testing methodology. Section 6 provides a discussion of the results, and section 7 includes a summary.

## 2. Machine-learning algorithms: Fundamentals

An inductive algorithm may be formally described as follows: Let S be a set of k-dimensional vectors. If $s \in S$ and $s_{i}$ is the ith component of s, $s_{i}$ is identified as the value of attribute i. Further, let T be a non-empty, finite subset of S, and let P and N represent a partition of T consistent with the concept to be learned. T provides a training set of observed examples of some concept to be learned, where P represents positive examples of the concept and N consists of negative examples of the concept.

The induction process seeks to construct a classification rule set that properly assigns $t \in T$ to P or N based on the attributes of t. The rule set produces a partitioning of S into cases classified as positive or negative. If the partitioning of S is correct (i.e., given P and N), the general concept has been determined.

A number of machine learning programs (algorithms) have been developed with this structure. These include ID3 [26], PLS1 [28], NEWQ [16], and AQ15 [23].

Two types of inductive operators characterize most of the algorithms that have been developed: Specialization operators and generalization operators [28]. A specialization operator manipulates the entire set of training examples by splitting them into two or more parts – those that have a greater likelihood of containing positive events and those that have a greater likelihood of containing negative ones. The splitting continues (using one attribute for each split) until some stopping criterion is satisfied. Both probabilistic and information-theoretic methods of choosing the next attribute have been used. A generalization operator works in an opposite fashion. It starts with a single event or subset of events and modifies its structure until the set has been correctly classified. Rendell et al. [28] found that algorithms using generalization operators were less effective in terms of predictive accuracy than those using specialization operators. Consequently, we focus on two algorithms that use specialization operators: ID3 and NEWQ. ID3 is widely known. NEWQ was developed by Koehler and Majthay [17].

ID3 ID3, which generates decision trees based on an information-theoretic approach, has been well described in the literature (cf. [3,21,26,27]). Therefore, we only briefly summarize its algorithm here.

Let the set S contain p cases of class P and n cases of class N. Assuming that a given example belongs to class P with probability $p/(p+n)$ and to class N with probability $n/(p+n)$ , the amount of information required to yield the message “P” or “N” is measured by

$$
\begin{array}{r l} F (p, n) = & - [ p / (p + n) ] \log_ {2} [ p / (p + n) ] \\ & - [ n / (p + n) ] \log_ {2} [ n / (p + n) ]. \end{array}
$$

Let $I = \{1, 2, \ldots, k\}$ and let $V_{v}$ be the set of all possible values of attribute i for $i \in I$ . Without loss of generality, assume each $V_{i}$ has at least two elements. When $V_{i}$ contains numerical data, we assume $V_{i}$ is ordered. An ID3 rule, R, is a non-empty set of tuples where, if $(i, A) \in R$ then:

(1) $i \in I$ and $A$ is a subset of $V_{i}$ ; or (2) $i = 0$ and $A = \{0\}$ or $A = \{1\}$ .

A rule applied to an observation $y$ is interpreted as

$$
\begin{array}{l l} \text {IF} & y _ {i} \in A \text {for each} (i, A) \in R, \text {with} i \in I \\ \text {THENs} & y \in P \text {if} (0 \{0 \}) \in R \\ & y \in N \text {if} (0, \{1 \}) \in R. \end{array}
$$

The basic algorithm is as follows.

Begin

1. Create the root node;

2. if all examples at the current node are of the same class, then stop;

3. for each attribute $A_{i}$ , compute the value of gain (A);

4. choose the attribute with the highest gain (A) to branch the current nodes;

5. for each branch node go to step 2.

End

ID3 makes no assumption concerning the data distribution. The algorithm treats continuous variables of the type that dominates the data tested here, as discrete: A recursive decomposition process divides continuous data into several discrete ranges.

NEWQ Koehler and Majthay [17] developed an algorithm, NEWQ, which combines the ideas of ID3 with discriminant analysis. NEWQ operates as follows: Assume that T consists of discrete or continuous numerical data. Here a rule, R, is defined as a non-empty set of 3-tuples of the form $(w, z, \approx)$ , where w is an n-dimensional vector; z is a scalar; $\approx$ is one of $\geqslant$ or <. A rule applied to an example y is interpreted as

IF $w^{\prime}y\approx z$ for each $(w,z,\approx)\in R$ where $w$ is non-zero

THEN $y\in P$ if $(0,0, - )\in R$

$$
y \in N \text {   if   } (0, 1, -) \in R,
$$

where “-” means “don’t care”.

When w is non-zero, $(w, z)$ can be thought of as defining a hyperplane, $\{x : w' x = z\}$ , which attempts to separate elements of P from elements of N. Discriminant analysis procedures can be used to generate $(w, z)$ values.

The algorithm proceeds as follows:

Begin

1. if all $T$ consist of positive or negative cases, the current rule is completed;

2. else generate a hyperplane $(w, z)$ that strictly separates at least one point of $T$ from its remaining elements (this ensures that the open half-space, $\{y : w' y < z, y \in T\}$ and the closed half-space $\{y : w' y \geqslant z, y \in T\}$ are non-empty);

3. use the hyperplane to partition $T$ into $\{y : w'y < z, y \in T\}$ and $\{y : w'y \geqslant z, y \in T\}$ . A new rule is created, the old augmented, and NEWQ called with each resulting partition.

End

The process used to generate a hyperplane in step 2 can be any procedure that yields a hyperplane strictly separating at least two points of T. In this study we use the PMM procedure of Koehler and Erenguc [16] to generate the hyperplane. Any of a large number of other procedures could be used.

## 3. Logistic regression

Logistic regression (LOGIT) techniques are also well-described in the literature (cf. [1,13,14,20,31]). The logistic specification of linear regression arose out of the need to analyze categorical data in the context of the general linear model. The general log-linear form of the model is as follows.

$$
\ln \frac {\mathrm{P} (E \mid x _ {i} , \dots , x _ {n})}{\mathrm{P} (\overline {{{E}}} \mid x _ {i} , \dots , x _ {n})} = a + b _ {i} x _ {i} + \dots + b _ {n} x _ {n}.
$$

The ratio on the left-hand side is the log-odds ratio where the numerator is the probability of E (that a given event occurred) given $x_{i}$ through $x_{n}$ . The denominator is the probability $\overline{E}$ (that a given event did not occur) given $x_{i}$ through $x_{n}$ . On the right-hand side, $x_{i}$ through $x_{n}$ represent the independent variables of interest, a is the intercept, and $b_{i}$ through $b_{n}$ are the coefficients for the respective independent variables.

The LOGIT form of the model can be derived by solving the log-linear model for the numerator of the log-odds ratio. Its general form is as follows.

$$
\begin{array}{l} \mathrm{P} (E \mid x _ {i}, \dots , x _ {n}) \\ = \frac {\exp (a + b _ {i} x _ {i} , + \cdots + b _ {n} x _ {n})}{1 + \exp (a + b _ {i} x _ {i} , + \cdots + b _ {n} x _ {n})}. \end{array}
$$

An important difference between machine-learning algorithms and LOGIT is that the former methods can model contingent interactions. For example, variable $x_{i}$ may be specified as an important variable, but only if at the same time and for the same observation variable $x_{2}$ has a value larger than, say, 0.5.

## 4. Performance measures

## 4.1. Caveats

The principal problem in empirical studies of the type we address is that of determining whether it is possible to extrapolate from error rates computed from small sample results to the true error rate for the total population of domain instances. Much of the work that has appeared in the literature seems to report estimators of error rates that are subject to significant error themselves. We treat this issue in more detail in the subsection that follows.

Of lesser concern is the observation that nearly every research study has ignored the relative costs of type I and type II errors. This omission is more understandable – and less methodological – since there is often a difficult measurement problem involved. In the data used in the study reported here, there are potential costs associated with issuing an unqualified audit opinion when a qualified opinion should have been expressed. Similarly, there are likely costs associated with issuing a qualified opinion when an unqualified opinion should have been given. In the former case, major losses may accrue to investors and creditors. In the second case the firm may be hindered in its ability to issue stock and to borrow money. Ascertaining these costs awaits further research. Consequently, we have treated the costs of type I and type II errors as being equal.

## 4.2. Estimating error rates

Weiss and Kapouleas [32] distinguish between apparent error rates and true error rates. Apparent error rates are the result of testing a model on the data used to train that model. Apparent error rates are not often used by researchers, as they can result from an overfitting of the model to the data in the training set. If the training set is not a fair representation of the problem domain's universe, the resulting error rates can be misleading.

True error rates are nearly always the objective of empirical research of the type presented in this paper. Researchers seek to divine the representative power of a set of sample data, as revealed in a model that is trained on that data. The simplest technique for estimating error rates is the single train-and-test experiment. The sample cases are randomly assigned to a training set or to a test set. A model is developed from the training set, and the error estimate is determined by testing the model's performance on the test set.

While the single train-and-test method is economical, it has been shown that nearly 1000 test cases are required to be assured (95% confidence level) that the estimated error rate is nearly equal to the true error rate. Few studies have the luxury of this number of test cases. It is more common to find less than 100 cases available for training and testing.

A more satisfactory approach is to use a resampling method, such as k-fold cross-validation or bootstrapping. In our study we have used the preferred special case of the k-fold cross-validation method, with k = n - 1 (where n is the number of cases). The resulting error estimate is nearly unbiased, since every case is used in training the model, and every case is used as a test case, as well. The disadvantage is that the process must be iterated n times, which can be very time consuming and expensive. Further details of these methods can be found in Efron [7].

## 5. Problem domain and research method

To test the applicability of the two machine-learning algorithms as compared to LOGIT, we used data from the going-concern studies conducted by Mutchler [24]. A basic assumption used in preparing financial statements is that an entity will continue as a “going-concern”. When there is doubt about the entity’s continued existence, the entity’s auditor will issue a modified auditor’s report. The study of auditor’s going-concern decisions provides a useful topical area to test the induction algorithms, since there is a substantial body of research in this area that examines the use of statistical models such as LOGIT.

The sample is a subset of data from the Mutchler [24] study. The source of the sample was the Disclosure II Database which reported on all publicly-traded companies whose fiscal year ended between March 31, 1981 and February 28, 1982. The entire population of publicly-traded manufacturing companies was sampled and classified into three categories. The three categories were: (1) companies exhibiting financial-distress signals that received a going-concern qualification; (2) companies exhibiting financial stress signals that did not receive the going-concern qualification; and (3) companies that are distress free and that did not receive the going-concern qualification. Only categories (1) and (2) were used in this research. We eliminated the distressed companies because previous research has indicated that auditors will not consider issuing the going-concern report unless the company exhibits a problem of some sort [15,24,33].

The distress classification is based upon a company experiencing one of the financial distress signals described in table 1. The set of problem-company criteria shown in table 2 was developed through interviews and responses to a questionnaire by auditors [24].

As noted in the previous section, we used repeated train-and-test partitions to estimate comparative error rates. We applied a special case of cross-validation known as leaving one out. For a given algorithm and sample size n, a model is generated using n - 1 cases. Then the model is tested on the single held-out case and the success or failure of the prediction is recorded. This procedure is repeated n times, with every case used for one test. At the completion of the experiment, we have an estimate of the performance of an algorithm as measured by its error rate on holdout cases. The leaving-one-out method is nearly unbiased and is particularly useful when small samples are being examined.

<table><tr><td>Table 1Problem company criteria used for selecting sample companies</td></tr><tr><td>1. Negative net worth2. Negative cash flow3. Negative income from operations4. Negative working capital5. Current year loss including cases where there were two and three straight loss years.6. Current years retained earnings deficit including cases where there are two and three straight retained earnings deficit years.</td></tr></table>

## 6. Results and discussion

The comparative error rates are compiled in table 3. We see that NEWQ produced the fewest errors - 15, or an error-rate estimate of $18.25\%$ . LOGIT produced 16 errors $(20\%)$ . ID3 yielded 18 errors $(22.5\%)$ . We also generated a naive model by randomly classifying each firm into one of two groups, then measuring the total number of firms correctly classified. This procedure was repeated 80 times. As shown in table 1, the naive model yielded 42 errors, or 52.5%.

<table><tr><td>Attribute variables included for sample companies</td></tr><tr><td>1. Cash flow/total liabilities</td></tr><tr><td>2. Current assets/current liabilities</td></tr><tr><td>3. Net worth total liabilities</td></tr><tr><td>4. Total long-term liabilities/total assets</td></tr><tr><td>5. Total liabilities/total assets</td></tr><tr><td>6. Net income before tax/net sales</td></tr><tr><td>7. Good news (1 = any good news factor, 0 = otherwise)a</td></tr><tr><td>8. Bad news (1 = any bad news factor, 0 = otherwise)</td></tr><tr><td>9. Change in net income/total assets ratio</td></tr><tr><td>10. Ln (sales)</td></tr><tr><td>11. Change in current ratio</td></tr><tr><td>12. Big 8 auditor = 1, non big 8 auditor = 0</td></tr></table>

$^{a}$ See Mutchler [24] for a list of good/bad news variables.

Table 3  
Comparative results of testing

<table><tr><td rowspan="2"></td><td rowspan="2">Predicted class</td><td colspan="2">True class</td></tr><tr><td>Qualified</td><td>Unqualified</td></tr><tr><td rowspan="2">NEWQ</td><td>Qualified</td><td>32</td><td>7</td></tr><tr><td>Unqualified</td><td>8</td><td>33</td></tr><tr><td rowspan="4">LOGIT</td><td rowspan="2">Predicted class</td><td colspan="2">True class</td></tr><tr><td>Qualified</td><td>Unqualified</td></tr><tr><td>Qualified</td><td>32</td><td>8</td></tr><tr><td>Unqualified</td><td>8</td><td>32</td></tr><tr><td rowspan="4">ID3</td><td rowspan="2">Predicted class</td><td colspan="2">True class</td></tr><tr><td>Qualified</td><td>Unqualified</td></tr><tr><td>Qualified</td><td>32</td><td>10</td></tr><tr><td>Unqualified</td><td>8</td><td>30</td></tr><tr><td rowspan="4">Naive model</td><td rowspan="2">Predicted class</td><td colspan="2">True class</td></tr><tr><td>Qualified</td><td>Unqualified</td></tr><tr><td>Qualified</td><td>20</td><td>22</td></tr><tr><td>Unqualified</td><td>20</td><td>18</td></tr></table>

Efron [8] suggests the following one-standard-error rule for model choice: Select the simplest model that falls within one standard error of the minimum-error-rate algorithm, where the standard-error measurement is

$$
\mathrm{SE} = \sqrt {E (1 - E) / n}.
$$

Thus, for NEWQ, we have

$$
\mathrm{SE} = \sqrt {0 . 1 8 7 5 (0 . 8 1 2 5) / 8 0} = 0. 0 4.
$$

Either LOGIT or ID3 could be chosen by the one-standard-error rule. However, testing on two versions of both LOGIT and ID3 suggest that NEWQ is much simpler to apply.

We have observed that the leaving-one-out method of resampling produces results that are nearly unbiased estimators of the true error rate, yet it is often too expensive or time consuming to be used. NEWQ, however, required only two hours to complete the entire experiment. We tried two versions each of LOGIT and ID3. LOGIT averaged six hours to complete the experiment, and ID3 averaged 7 hours. Even if the latter times are idiosyncratic, dramatic reductions would be necessary to equal the operating performance of NEWQ.

We did not pursue possible improvements to ID3 by using heuristic methods to prune branches of its decision tree. One reason is that there are

80 of them to consider; and since ID3 constructs its decision tree to correctly classify every training example, there are marked differences among some trees. A second reason is that some pruning heuristics are flawed in that they amount to indirect training on holdout cases.

We also used only the PMM method for generating the separating hyperplanes in NEWQ. Improvements may be possible by using other methods, including the splitting algorithm of ID3.

## 7. Summary

We have reported here the results of a study comparing the performance of three contrasting algorithms for generating decision models from sets of data that include diagnostic attributes, their values, and the resulting decision. The three algorithms are of interest for the following reasons: Machine-learning is an active area of artificial intelligence research; ID3 has been a seminal algorithm in this research; LOGIT is prominent in the class of qualitative-response models developed in the field of statistics. While we have classified NEWQ as a machine-learning algorithm, it is a hybrid in that it incorporates ideas from machine-learning, as well as from statistics.

Machine-learning algorithms are themselves too complex to measure comparative performance from a theoretical standpoint. Consequently, well-conceived and executed empirical studies will continue to guide our progress in understanding algorithms that are designed to derive decision structures from data.

## References

[1] E. Altman,, R. Avery, R. Eisenbeis and J. Sinkey, Application of classification Techniques in Business, Banking and Finance. (JAI Press, Inc., 1981).

[2] D.D. Bobrow,, S. Mittal and M.J. Stefik, Expert Systems: Perils and Promise, Communications of the ACM (1986) 880–894.

[3] H. Braun and J.S. Chandler. Predicting Stock Market Behavior Through Rule Induction: An Application of the Learning-From-Example Approach, Decision Sciences (1987) 415–429.

[4] L. Brieman, J. Friedman, R. Olshen and C. Stone, Classification and Regression Trees (Wadsworth) 1984.

[5] J.S. Chandler, T. Liang and I. Han, An Empirical Investi-

gation of Some Date Effects on the Classification Accuracy of PROBIT and ID3, formcoming in Journal of Contemporary Accounting.

[6] E.L. Denna,, J.V. Hansen and R.L. Mservy, Development and Application of Expert Systems in Audit Services, IEEE Transactions on Knowledge and Data Engineering, Vol 3. No. 2 (June 1991) 1–13.

[7] B. Efron,, The Jacknife, the Bootstrap and other Resampling Plans (SIAM, Philadelphia, PA, 1982).

[8] B. Efron., Estimating the Error Rate of a Prediction Rule, Journal of the American statistical Association, Vol. 78 (1983) 316–333.

[9] L. Eshelman,, MOLE: A Knowledge Acquisition Tool That Buries Certainty Factors, Second AAAI Workshop on Knowledge Acquisition for Knowledge-Based Systems, Banff (October 1987).

[10] J. Holland,, Adaptation in Natural and Artificial Intelligence (University of Michigan Press, 1975).

[11] E.J. Hunt, and P. Stone, Experiments in Induction (Academic Press, New York, 1966).

[12] C. Jacobson and M.J. Freiling,, ASTEK: A Multi-Paradigm Knowledge-Acquisition Tool for Complex Structured Knowledge, Second AAAI Workshop on Knowledge Acquisition for Knowledge-Based Systems, Banff (October 1987).

[13] J. Johnston, Econometric Methods, 2nd Edition (McGraw-Hill, New York, NY, 1972).

[14] G.G. Judge, W.E. Griffiths, R.C. Hill and T-C. Lee, The Theory and Practice of Econometrics (John Wiley and Sons, New York, NY, 1980).

[15] T. Kida, An Investigation Into Auditor's Continuity and Related Qualifications, Journal of Accounting Research (Autumn 1980) 506–23.

[16] G. Koehler and S. Erenguc, Minimizing Miclassifications in Linear Discriminant Analysis, Decision Science 21, No. 1, 63–85.

[17] G. Koehler, and A. Majthay, Generalization of Quinlan's Induction Algorithm, working paper, University of Florida (August 1988).

[18] Pl. Langley, Data-Driven Discovery of Physical Laws, Cognitive Science, Vol. 5 (1981) 31–54.

[19] T. Liang, A Composite Approach to Inducing Knowledge for Expert Systems Design, BEBR Working Paper No. 89-1534, University of Illinois (1989).

[20] G.S. Maddala, Limited-Dependent and Independent Variables in Econometrics (Cambridge University Press, New York, 1983).

[21] W.F. Messier, Jr. and J.V. Hansen, Inducing Rules for Expert System Development: An Example Using Default and Bankruptcy Data Management Science (December 1988) 1403–1415.

[22] R.S. Michalski, A Theory and Methodology of Inductive Learning, Artificial Intelligence (1983) 111–161.

[23] R.S. Michalski, I. Mozetic, J. Hong and N. Laurac, The Multipurpose Incremental Learning System AQ15 and Its Testing Application to Three Medical Domains, Proceedings of the Fifth National Conference on Artificial Intelligence (August 1986) 1041–1045.

[24] J.F. Mutchler, A Multivariate Analysis of the Auditor's Going-Concern Opinion Decision, Journal of Accounting Research (Autumn 1985) 668–682.

[25] A. Newell and H.A. Simon, Human Problem Solving (Prentice Hall, Inc., Englewood Cliffs, NJ, 1972).

[26] J.R. Quinlan, Discovering Rules by Induction from Large Collections of Examples, in: D. Michie Ed., Expert Systems in the Micro Electronic Age (Edinburgh University Press, Edinburgh, 1979).

[27] J.R. Quinlan, Induction of Decision Trees, Machine Learning (1986) 81–106.

[28] L.A. Rendell, P. Benedict, H. Cho and R. Seshu, Improving the Design of Rule-Learning Systems, Report No. UIUCDCS-R-87-1395, Department of Computer Science, University of Illinois, December 1987.

[29] D.B. Shema and J.H. Boose, Refining Problem-Solving Knowledge in Repertory Grids Using a Consultation Mechanism, Second AAAI Workshop on Knowledge Ac-

quisition for Knowledge-Based Systems, Banff (October 1987).

[30] K.Y. Tam, Automated Construction of Knowledge-Bases from Examples, Information Systems Research, Vol. 1, No. 2 (June 1990) 144–167.

[31] H. Theil, Principles of Econometrics (John Wiley and Sons, New York, NY, 1971).

[32] S.M. Weiss and I. Kapouleas, An Empirical Comparison of Pattern Recognition, Neural Nets, and Machine-Learning Classification Methods, International Joint Conference on Artificial Intelligence, Detroit (1989).

[33] J.E. Wilkerson, Jr., Selecting Experimental and Comparison Samples for Use in Studies of Auditor Reporting Decisions, Journal of Accounting Research (Spring 1987) 161–167.

---
otero_id: 16960
otero_key: "RAVEXP39"
title: "Applying inductive learning to enhance knowledge-based expert systems"
authors: "Michael J Shaw"
year: "1987"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(87)90103-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Applying Inductive Learning to Enhance Knowledge-based Expert Systems \*

Michael J. SHAW

University of Illinois, Champaign, IL 61820, USA

This paper describes the use of inductive learning in MAR-BLE, a knowledge-based expert system I have developed for assisting business loan evaluation. Inductive learning is the process of inferring classification concepts from raw data; I use this technique to generate loan-granting decision rules based on historical and proforma financial information. A learning method is presented in this paper that can induce decision rules from training examples.

Keywords: Expert Systems for Business Loan Evaluation, Knowledge Acquisition, Inductive Learning.

![](/api/attachments/RAVEXP39/fulltext/images/a5ed0585ff271926ce5693bca324c3901187453af8f46b9dc230639115e453c4.jpg)  
Michael J. Shaw is an Assistant Professor of Business Administration at the University of Illinois, Urbana/Champaign. His current research interests are concerned with the applications of artificial intelligence in management and intelligent manufacturing.

\* This research is supported in part by a grant from the Office of Information Management.

## 1. Introduction

A major issue in designing knowledge-based expert systems for decision support is the process of knowledge acquisition: the encoding of human expertise into decision rules that can be incorporated in the expert system. The knowledge acquisition process is the main bottleneck in building expert systems for several reasons. First, even an expert of the given problem domain may not be aware of exactly what decision rules he/she has been applying; usually it would take a knowledge engineer to spend tedious interview sessions with the expert to identify a useful set of rules that can capture the necessary expertise and experience in the given domain. Second, there may not be experts in some domains or, when there are several experts specialized in the same area, it is often difficult to get consensus on the set of decision rules to use. Third, even when the decision rules have been determined and employed in the knowledge base, the expert system still needs to have a means to refine the rules continuously.

This paper describes a method aimed at automating the knowledge acquisition process for knowledge-based decision support. The principal objective is to investigate machine learning techniques for deriving decision rules in the expert systems. Specifically, an inductive learning method that can extract concepts or decision rules from raw data is described; such a method can be characterized as learning by example because the set of raw data provides decision examples made by human experts. Throughout this paper, I shall describe the application of inductive learning in MARBLE, a knowledge-based expert system for business loan evaluation.

The remainder of the paper is organized as follows. Section 2 reviews the knowledge-based approach to decision support and describes a prototype I have developed for business loan evaluation, emphasizing the importance of machine learning in such a system. Section 3 introduces concepts acquisition by inductive learning. Section

4 describes an algorithm for inductive learning. Section 5 describes an example on commercial loan evaluation using the approach presented in sections 3 and 4. Finally, section 6 discusses such related issues as probabilistic reasoning and conceptual clustering in the context of inductive learning and knowledge-based decision support.

## 2. MARBLE: A Knowledge-based Decision-Support System

## 2.1. An Overview of the System

The research described in this paper is part of an ongoing effort to develop a knowledge-based expert system specializing in financial decision support for commercial banks. The system, referred to as MARBLE (standing for ‘an expert system for Managing And Recommending Business Loan Evaluation), is a rule-based system [7] consisting of decision rules for evaluating commercial loans. It applies the judgment exercised by experienced loan officers in arriving at lending decisions for commercial loans. It currently consists of around 80 decision rules.

MARBLE's architecture consists of three major program modules: the Consultation Module, the Explanation Module, and the Knowledge Acquisition Module, as shown in fig. 1. The Consultation Module interacts with the user to obtain factual information about the problem, so as to generate decision information.

In the process of decision support, the Explanation Module can provide justifications for the rules taken or explain the question posed by the user. The Knowledge-Acquisition Module is used to derive decision rules or to refine MARBLE's knowledge base. The inductive learning method described in this paper is to be embedded in this module.

Characterized by the often large amount of data and program modules (models) involved, a decision-support system is usually linked with an external database and a model base [2]. It has been shown that the knowledge-based expert system provides a very good environment for this type of decision support [25]. The system's problem-solving process, then, consists of a sequence of operations utilizing information from the knowledge-base, external database, dynamic database (sometimes referred to as working memory), and model base. In the case of MARBLE, the model base can contain program modules for financial analysis, forecasting, simulation, or regression. The external database typically contains the historical loan data and financial information of companies applying loans. Therefore, special care has been taken to handle the interface between the system's knowledge-base, model base, and database [26].

![](/api/attachments/RAVEXP39/fulltext/images/0a32110558447f948ab853a86a95687e6b7e651b4260993346067e422c055b02.jpg)  
Fig. 1. The Organization of MARBLE.

## 2.2. Modeling the Loan-evaluation Decision

Typically, the evaluation of a business-loan application is a subjective decision process made independently by loan officers, bank controllers, auditory, and bank examiners. The loan-granting decision usually relies on examining a large amount of historical and pro forma financial information and on judgmental evaluation on the company's market characteristics, industry performance, management competence, and accuracy of the information obtained.

The loan-evaluation decision is traditionally analyzed by statistical linear models, such as regression analysis $[22]$ or multivariate discriminant analysis $[13]$ . As pointed out by Haslem and Longbrake $[12]$ and Kaplan and Dietrich $[13]$ , statistical analysis with linear models cannot capture the subjective judgments and the qualitative evaluation so important in the lending decision. In essence, the expert-system approach used by MARBLE is akin to the heuristic simulation method employed by Cohen, Gilmore and Singer [6]; they both simulate the decision process of loan officers. MARBLE, however, employs production rules as the basic knowledge representation, which has been pointed out as an effective model of the human decision-making process [21]. In addition, the recent knowledge-based technology enables MARBLE to be equipped with uncertainty reasoning, explanation, and incremental refinement capabilities. As will be shown, inductive learning can be applied to enhance MARBLE's performance by automatically acquiring decision rules for loan classification.

## 2.3. Knowledge Acquisition in MARBLE

Knowledge acquisition is the transformation of problem-solving expertise from some knowledge source to a program. Potential sources of knowledge include domain experts, textbooks, and raw data. It is widely recognized that knowledge acquisition is a crucial process in the construction of knowledge-intensive systems because of the difficulty of truthfully incorporating all specialized facts, procedures, and judgmental rules about the problem domain [7]. Currently, the knowledge-acquisition process in MARBLE is primarily achieved through the transformation of explicit domain knowledge into the representation form used by the expert system, sometimes referred to as ‘knowledge engineering’.

The ability to learn has long been recognized as an essential feature of intelligence. Dietterich et al. [9] categorizes learning methods into four areas: rote learning, learning by being told, learning from examples, and learning by analogy. This paper describes an inductive learning method that would help MARBLE augment its knowledge base through 'learning by examples'. The use of inductive learning to generate knowledge has been an important area of AI research. The work by Winston [29] pioneered the application of inductive learning to deriving conceptual descriptions for classifying block-world structures. Buchanan and Mitchell [3] developed a rule-learning method for discovering domain-specific knowledge used in inferring chemical structures from mass spectrum. Michalski and Chilausky [18] described PLANT, an expert system for soybean disease diagnosis; they performed an empirical study showing that the combination of learning by being told and learning from examples in PLANT can improve

![](/api/attachments/RAVEXP39/fulltext/images/0759ca2692c4a0b08a9beb0596dc1a2a8a71276de5f05107f9ce95e1e9888296.jpg)  
(a) Learning from Examples  
(b) Rule Refinement  
Fig. 2. Interactions Between the Learning and Knowledge-Acquisition Module and Other Components of MARBLE.

the diagnosis accuracy.

The primary application of inductive learning in MARBLE is to determine decision rules form examples of classification decisions done by domain experts (fig. 2). This capability would be very valuable in credit analysis, where the problem is to extract the classification knowledge from a large amount of historical financial data. The widely used traditional data analysis techniques, such as factor analysis or discriminant analysis, only provide a scoring function with little interpretation. Inductive learning, on the other hand, can help detect interesting conceptual patterns or reveal structure in the data. The other application of machine learning shown in fig. 2 is to refine the decision rules based on past performance; this needs to be done empirically by analyzing the performance trace, and will not be included in the discussion of this paper.

## 3. Concept Acquisition by Inductive Learning

## 3.1. Inductive Learning: A Review

Inductive learning can be defined as the process of inferring the description of a class from the description of some individual objects of the class.

Each class can be viewed as a concept which is described by a concept recognition rule as a result of inductive learning; if an input data object satisfies this rule, then it represents the given concept. For example, a recognition rule for the concept ‘good customer’ might be

'A customer whose asset exceeds \$1,000,000.00, total-debt is less than \$250,000.00, and whose annual growth-rate is more than 10%.'

Using first-order predicate calculus (FOPC) as the knowledge representation, such a concept can be represented by a conjunction of attribute descriptions:

$$
\begin{array}{l}\text {   customer   } (t) \land (\text { asset   } (t) > 1, 0 0 0, 0 0 0) \land\\(\text { total - debt   } (t) <   2 5 0, 0 0 0) \land (\text { AGR } (t) >\\0. 1 0) \rightarrow (\text { class   } (t) = ^ {\prime} \text { GOOD } ^ {\prime}).\end{array}
$$

An alternative way to represent such a concept is to use the variable-valued logic (VL) proposed by Michalski [16,17]. The VL language is an extended form of if-then rules where many-valued variables are involved. The premise section of each rule is a conjunction of multivalued attribute variables; each variable is enclosed by a bracket with the corresponding attribute values. The aforementioned concept recognition rule can be represented by the VL formalism as follows:

$$
[ \text { assets } > 1, 0 0 0, 0 0 0 ] [ \text { total - debt } <   2 5 0, 0 0 0 ] [ \text { AGR } > 0. 1 0 ] \rightarrow [ \text { class:   `GOOD' } ].
$$

I shall use the VL formalism for knowledge representation throughout this paper for its simplicity and clarity.

In performing concept formation tasks, an induction program is presented with objects, usually consisting of a set of attribute-value pairs as object descriptions. The program is expected to generalize from these examples and derive the common concept so as to accurately classify new objects. Sometimes negative examples – i.e., objects which fail to exhibit the concept – are presented to facilitate the process and to improve the accuracy of the learning. Angluin and Smith [1] used the following specifications to define an inductive inference problem.:

(1) the class of rules being considered,

(2) the hypothesis space, sometimes referred to as the description space, which consists of a set of concept descriptions such that each rule in the class has at least one description in the hypothesis space,

(3) for each rule, its set of examples, and the sequences of examples that constitute admissible presentations of the rule,

(4) the class of inference methods under consideration,

(5) the criteria for successful inference.

Essentially, inductive learning is an inference process executed in the hypothesis space; this inference process reads in examples and outputs concept descriptions taken from the hypothesis space. The successful implementation of the inference process depends largely on the adequate handling of the following design issues:

(1) Organization of the hypothesis space.

(2) Representation of the inference rules.

(3) The inference method.

(4) Criteria for evaluating hypothesis.

(5) Criteria for successful inference.

The remainder of this section will give a more detailed look at each of these issues.

## 3.2. Hypothesis Space

Since the major step in inductive learning is concerned with the process of generalization, it is useful to organize the hypothesis space in such a fashion that the generalization relation is explicitly represented. The subsumption relation in predicate logic can provide such a structure. the subsumption relation formally represents the relative generality (or specificity, for that matter) between two logic descriptions. If A and B are two well-formed-formulas (wffs), A subsumes B if and only if there exists a substitution $\sigma$ such that the descriptions in $\sigma(A)$ are a subset of those in B. For example, RED-HAIR(x) & TALL(x) & TEACHER(y) subsumes RED-HAIR(a) & TALL(a) & TEACHER(g(a)) & ENGLISH(g(a)) with the substitution $\sigma=\{a/x, g(a)/y\}$ . If A subsumes B, then A is more general than B, which implies that A can apply in more situations than B. Based on this subsumption relation, the descriptions in the hypothesis space can be placed in a particular order according to the generality of each description. This type of hypothesis space is used in [20], [28] and [17].

Another structure used for organizing the hypothesis space is the decision-tree structure where a node with b branches in the tree represents the corresponding attribute has b different values in the example set. Quinlan [23] and Lee and Ray [14] used decision tree to structure the hypothesis space of their learning programs.

## 3.3. Inference Rules

In the general AI problem-solving process, rules are used as state-transformations in the effort to achieve the desired goal, which then provides the solution to the problem. In the same vein, inductive learning can be viewed as a process of transforming initial concept descriptions to intermediate concept description to, ultimately, the inductive concept descriptions. The transformations are achieved by using inference rules.

There are different types of inference rules used in inductive learning. Michalski [17] developed a set of generalization rules to facilitate the searching of the inductive concept descriptions and to guide the movement in the hypothesis space. The AM system described in [15] used roughly 40 heuristic rules to create new concepts; the rules are used to achieve such learning functions as generalization, specialization, permutation of function arguments, and reasoning by analogy. These types of inference rules serve as ‘refinement operators’ to improve hypothesis.

## 3.4. The Inference Method

The process of inductive learning is often implemented as a heuristic searching procedure $[15,20,24]$ . Concept descriptions are derived through a sequence of transformations to generate the goal descriptions in the hypothesis space. Descriptions satisfying the training examples provide the initial condition; negative examples provide constraints to reduce the search space. Because there are enormous amounts of concept descriptions contained in the hypothesis space, successful inference methods often utilize heuristic information to guide the search and bypass unnecessary searching paths.

It is important to choose a representation for the rule space in which generalization can be accomplished by inexpensive operations. Mitchell's version-space algorithm takes advantages of the partial ordering of the hypothesis space. He defines the version space as the set of all concept descriptions that are consistent with all the training examples so far. Initially, the version space is the complete set of possible concepts. The version space is progressively reduced when more training examples are presented. Positive examples force the program to generalize and, consequently, the more specific concept descriptions are eliminated. Conversely, negative examples force the program to specialize, so the more general concept descriptions are removed from consideration. The version space gradually shrink in this manner until only the desired description remains.

Another approach for facilitating the process of generalization is to use the set of negative examples as constraints to rule out undesirable points. The central methodology underlying the learning programs in [17,18,19] is based on the concept of a star. A star of the example e against the set E, denoted $G(e/E)$ , is defined as the set of all maximally general expressions that satisfy the positive example e and that do not satisfy any of the negative examples in E. This methodology essentially decomposes the problem of finding a complete description of a concept into subproblems with each subproblem aimed at finding the star that covers one positive example but none of the negative examples. In the process of generating the states, the descriptions can be generalized and simplified by the aforementioned transformation rules or refinement operators. The rule-learning algorithm described in section 4 is based on this star methodology.

As previously stated, a classification rule can be represented in the form of a decision tree. The inference procedure to form classification rules in this context is then the construction of decision trees. typically, the decision tree can be generated by a branch-and-bound procedure and a branching criterion is needed to determine the attribute-value to be included in the rule. In [23] and [14] a branching criterion is employed based on the expected information content of each node. The information content of a node is measured by $-p^{+}\log_{2}p^{+}-p^{-}\log_{2}p^{-}$ , where $p^{+}$ is the proportion of positive examples and $p^{-}$ is the proportion of negative examples. The algorithm selects the next attribute to include in the rule based on the principle of maximizing expected information gain.

## 3.5. Criteria for Evaluating Hypothesis

In the searching of inductive concept descriptions, the movement in the hypothesis space needs to be guided by some criteria which establish a basis for evaluating the hypothesis. Such criteria are used in selecting the most promising concept among a group of candidates. The possible criteria include:

(a) Simplicity of hypothesis. This criterion states that, while everything else being equal, the hypotheses (a concept description) with the least number of attributes should be selected.

(b) The set-theoretical goodness of fit. This criterion stems from the research in language learning. It states that given the example set S, the best learned concept description should satisfy every element in S and as few additional elements as possible.

(c) The decision theoretical measure. Based on Bayes' Theorem, this criterion looks for a hypothesis that has the maximal conditional probability given the set of examples. That is, for the given set of examples $S$ , the best hypothesis $h$ maximizes the conditional probability of $h$ given $S$ , $\Pr(h/S)$ . Since by Bayes' Theorem, $\Pr(h/S) = (\Pr(h) \cdot \Pr(S/h)) / (\Pr(S))$ , it suffices to maximize $\Pr(h) \cdot \Pr(S/h)$ . This criterion can combine both criteria (a) and (b). That is, $\Pr(h)$ represents the degree of simplicity of $h$ and $\Pr(S/h)$ can be treated as a measure of the goodness-of-fit of $h$ to the set of examples $S$ – in other words, higher $\Pr(h)$ means simpler hypotheses and higher $\Pr(S/h)$ means a better fit of $h$ to $S$ .

## 3.6. Inference Criteria

The inference criteria are used to evaluate the inference procedure to derive inductive concept descriptions. Two such criteria are especially important: (a) the convergence of the inference procedure and (b) the solution quality of the inference procedure as measured by ‘completeness’ and ‘consistency’ of the procedure.

(a) Convergence. This criterion is typically used in the theoretic study of language learning [1]. Conceptually, suppose an inference procedure is run on a large collection of examples with the examples presented in a sequence. The inference procedure is said to converge correctly if it always derives the correct rules after some finite number of iterations.

(b) Completeness and consistency. Inductive learning of concepts is essentially a process of generalization such that the resulting concept description for each class can correctly describe the individual examples of that class; the description is typically a conjunction of attribute-value pairs shared by all objects in the class. The completeness condition says that the concept description generated by the inductive learning process must correctly describe all positive examples; the consistency condition states that the concept description generated must not describe any of the negative examples.

## 4. An Inductive Learning Algorithm

In terms of algorithmic design, the process of inductive learning for multiple concepts begins with the separation of positive and negative decision examples among the whole set of training examples. Let the set of positive examples be $S_{P}$ and the set of negative examples be $S_{n}$ , the goal of the algorithm is then to determine a conjunction of attribute values as the concept description that satisfies the completeness condition, the consistency condition, and the criterion of the induction.

The learning program would iteratively choose an element $e^{j}$ in $S_{P}$ and, for every element $f^{k}$ in $S_{N}$ , generate a discriminant $d(e^{j}/f^{k})$ , or $d^{jk}$ for short. Mathematically, let

$$
\begin{array}{l} e ^ {j} = a _ {1} ^ {j} \cdot a _ {2} ^ {j} \dots a _ {i} ^ {j} = \underset {i = 1, n} {\Lambda} a _ {i} ^ {j} \quad \text { and } \\ f ^ {k} = f _ {1} ^ {j} \cdot f _ {2} ^ {k} \dots f _ {i} ^ {k} = \underset {i = 1, n} {\Lambda} f _ {i} ^ {k}, \end{array}
$$

where $a_{i}^{j}$ and $f_{i}^{j}$ are attributes in $e^{j}$ and $f^{k}$ , respectively. Then $d^{jk}=d(e^{j}/f^{k})=\Lambda_{i\in Q}a_{i}^{j}$ , where $Q=\{i:a_{i}^{j}\neq f_{i}^{k}\}$ and $d^{jk}=\Lambda_{i=1,l_{jk}}d_{i}^{jk}$ . That is, $d(e^{j}/f^{k})$ is a conjunction of attribute values that can be described by $e^{j}$ but not $f^{k}$ .

Next, the program will generate a set of all consistent complexes $C^{j}$ associated with $e^{j}$ ; each element $C_{i}^{j}$ in $C^{j}$ is a conjunction of attributes not described by any of the negative examples in $S_{N}$ . Algorithmically, $C_{i}^{j}$ is generated by taking an attribute out of each $d^{jk}$ , for $k=1,\ldots,n$ , and form a conjunction, that is,

$$
C ^ {j} = \left\{\left(\underset {l = 1, n} {\Lambda} C _ {i l} ^ {j}\right): C _ {i 1} ^ {j} \in d _ {k 1} ^ {j}, \right.
$$

$$
\left. C _ {i 1} ^ {j} \in d _ {2} ^ {j k}, \dots , C _ {i n} ^ {j} \in d _ {n} ^ {j k} \right\}.
$$

Thus, there are a total of $l_{j1} \cdot l_{j2} \ldots l_{jn} = \Pi_{k=1,n} l_{jk}$ consistent complexes for $e^j$ (remember that $l_{jk}$ is the number of attributes contained in the discriminant $d^{jk}$ ). Each of the complexes is consistent, since it does not cover any negative example.

The induction criterion should then be applied to choose the best complex $C_{*}^{j}$ in $C_{i}^{j}$ 's based on a utility function,

$$
f \left(C _ {i} ^ {j}\right) = w _ {1} P _ {1} + w _ {2} P _ {2} + \dots + w _ {r} P _ {r},
$$

where $P_{1}, P_{2}, \ldots, P_{r}$ are the induction criteria chosen by the user, $w_{1}, w_{2}, \ldots, w_{r}$ show the degree of importance the user gives to the preference criterion. $C_{*}^{j}$ is chosen by selecting the highest $f(\cdot)$ value.

For example, the induction criterion - 'to satisfy as many positive examples as possible while not covering any of the negative examples' can be translated to the utility function

![](/api/attachments/RAVEXP39/fulltext/images/1db84d1f8fec88e043461247a1e784280a4a5ecb46e6a340ba793bb15efe3df1.jpg)  
Fig. 3. Flowchart for the Inductive Learning Algorithm.

$\max f(c_i^j) = N_P - W * N_N,$

where $N_{P}$ is the number of positive examples satisfied by $C_{i}^{j}$ and $N_{N}$ is the number of negative examples that can describe $C_{i}^{j}$ . W is a very large number used to discourage $N_{N}$ from taking any positive value.

Positive examples covered by $C_{*}^{j}$ will be removed from $S_{P}$ , and the same procedure will be applied to the remaining $S_{P}$ and the original $S_{N}$ again until all positive examples, $e^{j}$ , are covered. All the complexes thus produced will be combined to form a complete disjunctive description which covers every positive examples. This algorithm is described by the flowchart shown in fig. 3.

Decision rules derived from this algorithm satisfy both the completeness and the consistency conditions defined in section 3.1. A simple proof is described here according to the algorithm displayed in fig. 3. The algorithm is complete because the algorithm uses steps 2–5 to generate new complexes to describe uncovered positive examples until every positive example is covered by the disjunctive concept description, D, produced in step 9. The algorithm is also consistent because the concept is generated based on the discriminants $d(e^{j}/f^{k})$ in step 3, which ensures that none of the negative examples are covered by the inductive description represented by D.

## 5. An Example: Applying Inductive Learning in the MARBLE System

I shall now use the loan evaluation as an example to illustrate the application of inductive learning in MARBLE. The objective is to determine the risk classification of commercial bank loans. In order to describe the default risk on a given commercial loan, a bank usually would use a five-category classification scheme $[13]$ . Here, for the sake of simplicity, only three classes, represented by I, IA, II, are actually used in the set of training examples. There are a total of nine training examples: customers A, B, C for class I; D, E, F for class IA; and G, H, I for class II. The inductive procedure for learning classification rules can be described as follows:

## (i) Choosing the relevant attributes for training examples

An initial set of attributes using historical and pro forma financial information are selected to be included in each input data case as training examples. As shown in fig. 4, this set of attributes includes nominal, linear, and structured attributes. In the more traditional data analysis techniques, such as regression or discriminant analysis, only linear and nominal attributes can be considered. The ability to process structural information constitutes one of the advantages of symbolic processing (as characterized by most AI programs) over numerical calculation (as characterized by statistical analysis). The domain of each structured attribute usually can be represented by a hierarchy of attribute values, corresponding to a generalization tree. Two structured attributes used in this example are shown in fig. 5. The tree structure will be used to apply appropriate generalization rules in the induction process.

## (ii) Specifying the data description and the domain-specific knowledge

After choosing the relevant attributes, a set of data descriptions $\{e_{k}^{i}\}$ , i=1,2,3, and the corresponding class $\{K_{i}\}$ . $(K_{i}=I, K_{2}=IA, K_{3}=II)$ are used as training examples, as shown in fig. 6. The values used in each attribute are defined in fig. 4.

The domain-specific knowledge, represented by the generalization trees, can be specified by the following transformation rules:

$$
\mathrm{R1}: [ \text { past - account - eval } = \text { one - year } ] \mathrm{V} [ \text { past - account - eval } = \text { two - year } ] \mathrm{V}
$$

$$
[ \text { past - account - eval } = \text { three - year } ] \to [ \text { past - account - eval } = \text { present } ],
$$

$$
\mathrm{R2}: [ \text { account - type } = \text { commission } ] \mathrm{V} [ \text { account - type } = \text { fees } ]
$$

$$
\rightarrow [ \text { account - type } = \text { other - businesses } ].
$$

Fig. 4.  
Relevant Attributes for Credit Rating.

<table><tr><td>Name</td><td>Description</td><td>Type</td></tr><tr><td>F1</td><td>the rating of management performance</td><td>nominaldomain = {high, average marginal, reject}</td></tr><tr><td>F2</td><td>the outside credit rating</td><td>nominaldomain = {high, average marginal, reject}</td></tr><tr><td>Current-assets</td><td>the amount of current assets, calculated from the pro forma balance sheet</td><td>linear</td></tr><tr><td>Net-worth</td><td>the amount of net worth</td><td>linear</td></tr><tr><td>Total-debt</td><td>the amount of total debt</td><td></td></tr><tr><td>Funds</td><td>the funds for debt service to funds provided by operations (three-year average)</td><td>linear</td></tr><tr><td>Cash</td><td>the amount of cash</td><td>linear</td></tr><tr><td>Currentliabilities</td><td>the amount of current liabilities</td><td>linear</td></tr><tr><td>Current-inventory</td><td>the amount of current inventory</td><td>linear</td></tr><tr><td>Average-inventory</td><td>the amount of three-year average inventory</td><td>linear</td></tr><tr><td>Avg-profits</td><td>three-year average of net profits</td><td>linear</td></tr><tr><td>Past-account-evaluation</td><td>the evaluation of past account</td><td>structured</td></tr><tr><td>Customer-status</td><td>the applicant&#x27;s status with the bank</td><td>nominaldomain = {current, new}</td></tr><tr><td>Account-type</td><td>the applicant&#x27;s account type either in this bank or from other banks</td><td>structured</td></tr></table>

## (iii) Forming a induction criterion

The induction criteria are (1) to maximize the number of positive examples covered, while not covering any of the negative examples, and (2) to include the least number of attributes.

## (iv) Applying the inductive learning algorithm

To derive the classification decision rule for class I, we start with the first positive example, corresponding to customer A, in class I.

![](/api/attachments/RAVEXP39/fulltext/images/8df35eff2bca47c43ade44fa48f04381b26d1dc9c9174568e86373f01655e4ec.jpg)  
Fig. 5. Examples of Structured Attributes.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
- The program produces the discriminant $d^{jk}$ of customer A against each negative examples one by one, starting with customer D in the negative example set. This process generated the following conjunctive description:
    [F1 = H][F2 = H][current-assets &gt; $42,000][net-worth &gt; $37,000]
    [total-debt &gt; $19,000][funds &gt; $8,000][cash &lt; $6,000]
    [cur-liability &lt; $55,000][inventory &gt; $12,000]
    [avg-inventory &gt; $6,000][avg-profits &gt; $8,000][past-acc-eval &lt; 2Y]
    [account-type = C].
- Repeat the same procedure to the remaining negative examples, against customer E:
    [F2 = H][current-assets &gt; $38,000][net-worth &gt; $46,000]
    [total-debt &lt; 28,000][inventory &gt; $14,000][avg-inventory &gt; $6,000]
    [avg-profits &gt; $9,000][account-type = T]
against customer F:
    [F1 = H][current-assets &gt; $52,000][net-worth &gt; $40,000]
    [total-debt &lt; $25,000][funds &gt; $6,000][cash &lt; $5,000]
    [cur-liability &lt; $45,000][inventory &gt; $11,000]
    [avg-inventory &gt; $5,00][avg-profits &gt; $9,000]
    [past-acc-eval = present][cust-status = N][account-type = E]
against customer G:
    [F1 = H][F2 = H][current-assets &gt; $45,000][net-worth &gt; $38,000]
    [total-debt &lt; $36,000][funds &gt; $0][cash &lt; $6,000]
    [cur-liability &lt; $57,000][inventory &gt; $7,000]
    [avg-inventory &gt; $3,000][avg-profits &gt; $9,000][past-acc-eval = 1Y]
    [cust-status = C][account-type = C]
</div>

Fig. 6.  
Data of 9 Customers (all figures in \$1,000).

<table><tr><td></td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td><td>H</td><td>I</td></tr><tr><td>F1</td><td>H</td><td>H</td><td>H</td><td>A</td><td>H</td><td>A</td><td>A</td><td>M</td><td>A</td></tr><tr><td>F2</td><td>H</td><td>H</td><td>A</td><td>A</td><td>A</td><td>A</td><td>M</td><td>A</td><td>A</td></tr><tr><td>Current assets</td><td>57</td><td>39</td><td>43</td><td>42</td><td>38</td><td>52</td><td>45</td><td>37</td><td>46</td></tr><tr><td>Net worth</td><td>57</td><td>55</td><td>49</td><td>37</td><td>46</td><td>40</td><td>38</td><td>29</td><td>36</td></tr><tr><td>Total debt</td><td>23</td><td>17</td><td>20</td><td>19</td><td>28</td><td>25</td><td>36</td><td>27</td><td>35</td></tr><tr><td>Funds</td><td>9</td><td>8</td><td>7</td><td>8</td><td>9</td><td>6</td><td>-9</td><td>7</td><td>5</td></tr><tr><td>Cash</td><td>4</td><td>3</td><td>5</td><td>6</td><td>4</td><td>5</td><td>6</td><td>6</td><td>5</td></tr><tr><td>Cur. liability</td><td>39</td><td>28</td><td>47</td><td>55</td><td>39</td><td>45</td><td>57</td><td>53</td><td>57</td></tr><tr><td>Inventory</td><td>21</td><td>15</td><td>18</td><td>12</td><td>14</td><td>11</td><td>7</td><td>13</td><td>14</td></tr><tr><td>Avg inventory</td><td>9</td><td>14</td><td>11</td><td>6</td><td>6</td><td>5</td><td>3</td><td>5</td><td>6</td></tr><tr><td>Avg-profits</td><td>12</td><td>15</td><td>13</td><td>8</td><td>9</td><td>9</td><td>9</td><td>9</td><td>-0.8</td></tr><tr><td>Past-acc-eval</td><td>1Y</td><td>2Y</td><td>3Y</td><td>2Y</td><td>1Y</td><td>1Y</td><td>3Y</td><td>2Y</td><td>NA</td></tr><tr><td>Cust-status</td><td>C</td><td>C</td><td>N</td><td>C</td><td>C</td><td>N</td><td>N</td><td>C</td><td>C</td></tr><tr><td>Account-type</td><td>C</td><td>E</td><td>D</td><td>D</td><td>T</td><td>E</td><td>E</td><td>T</td><td>T</td></tr></table>

```txt
(i) [avg-inventory > $6,000][net-worth > $46,000]
[avg-inventory > $5,000][avg-inventory > $3,000]
[net-worth > $29,000][net-worth > $36,000],
⋮
```

```txt
against customer H:
```

```txt
[F1 = H][F2 = H][current-assets > $37,000][net-worth > $29,000]
```

```txt
[total-debt < $27,000][funds > $7,000][cash < $6,000]
```

```txt
[cur-liability < $53,000][inventory > 13,000]
```

```json
[avg-inventory > $5,0C] [avg-profits > 8,000] [past-acc-eval = 1Y]
```

```ini
[account-type = T]
```

```txt
against customer I:
```

```txt
[F1 = H][F2 = H][current-assets > $46,000][net-worth > $36,000]
```

```txt
[total-debt < $35,000][funds > $5,000][cash < $5,000]
```

```json
[cur-liability < $57,000][inventory > $14,000]
```

```txt
[avg-inventory > $6,000][avg-profits > $0][past-acc-eval = 1Y]
```

```txt
[account-type = C].
```

Generalization rules as the extension-against rule and the climbing generalization tree rule have been applied in the foregoing process in deriving these discriminants.

## Step 2

\- For a set of complexes $C^j$ s by taking an attribute out of each discriminant $d^{jk}$ generated in Step 1. For example, by taking out the first attribute in each discriminant generated above and alternatively taking the attribute of the discriminant against customer I, $d^{\mathrm{AI}}$ , the following 13 complexes ( $C_i^j$ s) are generated:

(1) $[\mathbf{F}1 = \mathbf{H}][\mathbf{F}2 = \mathbf{H}][\mathbf{F}1 = \mathbf{H}][\mathbf{F}1 = \mathbf{H}][\mathbf{F}1 = \mathbf{H}][\mathbf{F}1 = \mathbf{H}],$

(2) $[\mathbf{F1} = \mathbf{H}][\mathbf{F2} = \mathbf{H}][\mathbf{F1} = \mathbf{H}][\mathbf{F1} = \mathbf{H}][\mathbf{F1} = \mathbf{H}][\mathbf{F2} = \mathbf{H}],$

(3) [F1 = H][F2 = H][F1 = H][F1 = H][F1 = H][current-assets > \$46,000],

(13) $[\mathbf{F1} = \mathbf{H}][\mathbf{F2} = \mathbf{H}][\mathbf{F1} = \mathbf{H}][\mathbf{F1} = \mathbf{H}][\mathbf{F1} = \mathbf{H}][\text{account - type} = \mathbf{C}]$

Another example of the complex generated in this step would be

This process continues until all the consistent complexes are generated. These complexes can be simplified by removing redundant components or applying generalization rules. For example, complex (3) can be simplified to $[F1 = H][F2 = H][current-assets > \$46,000]$ and complex (i) can be generalized to $[avg-inventory \geqslant \$7,000][net-worth \leqslant \$47,000]$ by applying the closing interval rule described in [17] (note that the unit of input data is \$1,000).

## Step 3

\- Choose the best complex description from the set of complexes generated in Step 2 according to the preference criterion. The preference criteria used in the example include (1) to maximize the number of positive examples covered, j (2) to minimize the number of negative examples covered, and (3) to minimize the number of attributes. Then the complex selected is

$$
[ \text { avg - inventory } \leqslant 7, 0 0 0 ] [ \text { net - worth } \leqslant 4 7, 0 0 0 ],
$$

which covers customers A, B, and C in the set of positive examples.

## Step 4

\- Remove the covered positive examples from the list of positive examples by the resulting description in Step 3, and apply the algorithm to the remaining positive examples. Since, in this case, all the positive examples have been covered by the single complex, the decision rule for class I is

$$
[ \text {avg - inventory} \geqslant 7, 0 0 0 ] [ \text {net - worth} \geqslant 4 7, 0 0 0 ] \rightarrow [ \text {class} = I ].
$$

The same procedure produces the following decision rule for class IA:

$$
\begin{array}{r l}&[ 3 7, 0 0 0 \leqslant \text { net - worth } \leqslant 4 8, 0 0 0 ] [ \text { inventory } > 8, 0 0 0 ]\\&\rightarrow [ \text { class } = \text { IA } ];\end{array}
$$

and for class II

$$
\begin{array}{r l}&{\left[ \mathrm{F1} = \mathrm{H}, \mathrm{A} \right] \left[ \text {total - debt} \geqslant 2 6, 0 0 0 \right]}\\&{\rightarrow \left[ \text {class} = \mathrm{II} \right].}\end{array}
$$

For the given set of training examples, the three classification rules thus generated covered all the positive examples but none of the negative examples, i.e., the induction process is both complete and consistent. These decision rules not only can be used for credit classification, each of the rules is also a description of a ‘concept’ learned from observed the classification examples. The set of decision rules generated by the inductive learning program can then be added to the expert system. For this example, the three decision rules just generated can then be stored in MARBLE.

## 6. Other Important Aspects of Inductive Learning

## 6.1. Probabilistic Learning

In inductive learning, if the training examples are highly distinct in the attribute space and occur in separable clusters, then the generalization procedure may result in concepts which are unambiguous in characterizing the classes. However, in real life, the training examples given as input data are usually not perfect but, rather, are contaminated by a variety of 'noise', thus causing errors. In the case of business loan evaluation, for example, the noise may be cause by incorrect financial information or inconsistent granting decisions made by loan officers. The inductive learning method just described would derive generalized descriptions even from the erroneous examples and generate decision rules accordingly. To account for the possible noise in input examples, the learning system should be able to recognize the imperfection of the data and exploit the converging evidence for the conceptual descriptions. An easy approach to resolve this problem is to relax the preference criterion specified for the induction procedure so that the description of a class is allowed to cover some negative examples under a specified limit. Alternatively, rather than taking a deterministic view, the inductive learning system can derive concept descriptions probabilistically.

Most of the AI inductive learning research to date has been focused on the deterministic aspect, although uncertainty reasoning has always been an important issue in designing expert systems. The research efforts in $[10, 14, 24, 27]$ represent some recent developments dealing with probabilistic learning. The probabilistic learning system (PLS) developed by Rendell $[24]$ adopted an information theoretical model to determine the probability associated with each candidate concept description. PLS uses a splitting algorithm which repeatedly dichotomizes the attribute space (sometimes referred to as the feature space) into smaller cells based on a dissimilarity measure. The splitting process continues until the training examples in each cell are as homogeneous as possible. The most relevant conceptual description can then be derived. The probabilistic rule generator (PRG) developed by Lee and Ray uses a modified branch-and-bound strategy to extract relevant attribute/value pairs for inclusion in the concept description. At each node of the search tree, PRG uses the information entropy as an evaluation function for selecting the branching attributes. An interesting aspect of PRG is that it can progressively select the most relevant concept for configuring the decision rules, and thus is shown to be computationally more efficient than prior inductive learning methods [17].

Theoretically, a learning system that derives decision rules probabilistically should be, in general, more efficient computationally than the deterministic counterpart because the completeness and consistency conditions (section 3) are relaxed; instead, a probabilistic learning system carries out statistical tests to determine the significance of various concept descriptions. This computational advantage becomes important when the amount of data is getting larger. If a deterministic approach such as the one described in this paper is used, the set of training examples needs to be preprocessed so that the most representative examples are extracted to serve as input to the induction algorithm.

## 6.2. Conceptual Clustering

As pointed out by Clancey [5], classification is a process critical to most problem-solving processes. The method for learning from examples described in sections 3 and 4 is concerned with forming conceptual descriptions for a set of predetermined classes, assuming that a set of data/class examples has been supplied by an external source (i.e., a domain expert). A different type of inductive learning can be achieved through ‘learning from observation’, where the input data set consists of data cases without any associated classification. This type of learning process would create classes (clusters) among the data cases and then generate conceptual descriptions to characterize each class. Such a machine-learning method is sometimes referred to as conceptual clustering [4,11,19].

In general, clustering is a procedure applied to classifying a set of data into mutually exclusive groups such that the data in the same group are similar while data of different groups are dissimilar to each other. Unlike the numerical taxonomy methods previously used for clustering, however, the conceptual clustering method characterizes each derived class by a conjunction of conceptual description, thus providing better interpretation of the classes. Moreover, as opposed to using a single similarity measure, conceptual clustering is also characterized by its ability to take into account nominal and structural attributes as well as linear numerical attributes.

Conceptual clustering can be used for knowledge acquisition in decision-support situations where the domain expert is either hard to find or is unreliable. In talking to several managers of commercial banks, for example, I found a general feeling existing among them that there are no agreed-upon criterion for classifying loan applications and the decision is often ad hoc. Thus, using historical loan data and the associated granting decision a training examples does have its shortcoming in that the input data may not be adequate examples for the classification decision. By contrast, conceptual clustering provides a method for grouping the input data into classes based on the inherent characteristics of the data. A conjunctive conceptual description is then generated to characterize each class, as to what can be achieved by the method described in sections 3 and 4. Thus, conceptual clustering can be viewed as 'learning without a teacher'.

## 7. Conclusion

Features such as explanation ability, heuristic inference, reasoning with uncertainty, and capabilities for incremental refinement make the knowledge-based expert system an effective tool for decision support. In this paper I have described another aspect in designing such knowledge-based decision support systems: an inductive learning method that can help automate the knowledge-acquisition process and generate decision rules.

Although the inductive learning process described in this paper is primarily related to classification, because classification is a plausible paradigm for human problem solving, the inductive learning method is, therefore, applicable to general decision support problems as well. Moreover, inductive learning can help discover the structure and concepts associated with the data, enabling the decision support system to refine its knowledge base continuously. As an extension to this work, I am currently working on learning probabilistic rules and the integration of learning from examples with conceptual clustering.

## References

[1] D. Angluin and C. Smith, Inductive Inference: Theory and Methods, Computing Surveys 15, nr. 3 (1983) 237–269.

[2] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, Future Directions for Developing Decision Support Systems, Decision Science 11 (1980) 616–631.

[3] G.B. Buchanan and T.M. Mitchell. Model-Directed Learning of Production Rules, Pattern-Directed Inference Systems, in: D. Waterman and F. Hayes-Roth, eds. (Academic Press, New York, 1978).

[4] Y. Cheng and K.S. Fu, Conceptual Clustering in Knowledge Organization, IEEE Trans. on Pattern Analysis and Machine Intelligence PAMI-7, Nr. 5 (Sept., 1985).

[5] W.J. Clancey, Heuristic Classification, Artificial Intelligence 27 (1985) 289–350.

[6] K.J. Cohen, T.C. Gilmore and F.A. Singer, Bank Procedures for Analyzing business Loan Applications, in: K.J. Cohen, F.S. Hammer eds., Analytical Methods in Banking (1966) 219–249.

[7] R. Davis, Interactive Transfer of Expertise: Acquisition of New Inference Rules, Artificial Intelligence 12 (1979) 121–157.

[8] T. Dietterich, Description of Inductive Program INDUCE 1.1, Technical report, Urbana-Champaign, Department of Computer Science, University of Illinois (Oct., 1978).

[9] T.G. Dietterich, R. Lonclon, K. Clarkson and R. Dromey, Learning and Inductive Inference, in: D. Cohen and E. Feigenbaum, eds., Handbook of Artificial Intelligence (Kaufman, Los Altos, 1981) 323–525.

[10] R.O. Duda, P.E. Hart and N.J. Nilsson, Subjective Bayesian Methods for Rule-Based Inference Systems, in: Proc. of the 1976 National Computer Conference (AFIPS Press, 1976).

[11] D. Fisher and P. Langley, Approaches to Conceptual Clustering, Proceedings of Ninth International Joint Conference of Artificial Intelligence (1985) 691–697.

[12] J.A. Haslem and W.A. Longbrake, A Credit Scoring Model for Commercial loans, A Comment, Journal of Money, Credit and Banking (Aug., 1972) 733–734.

[13] R.S. Kaplan and J.R. Dietrich, Empirical Analysis of the Commercial Loan Classification Decision, Accounting Review 58, Nr. 1 (Jan., 1982) 18–38.

[14] W. Lee and S. Ray, Probabilistic Rule Generator, Report

No. U10CDCS-R-86-1263, Urbana-Champaign, University of Illinois, Department of Computer Science (1986).

[15] D.B. Lenat, AM: An Artificial Intelligence Approach to Discovery in Mathematics as Heuristic Search, Ph.D. dissertation, Stanford University (1976).

[16] R.S. Michalski, Pattern Recognition as Rule-Guided Inductive Inference, IEEE Transactions on Pattern Analysis and Machine Intelligence PAMI-2, Nr. 2 (1980) 249–361.

[17] R. Michalski, A Theory and Methodology of Inductive Learning, in: R. michalski, J. CArbonell and T. Mitchell, eds., Machine Learning (Tioga, Palo Alto, 1983).

[18] R. Michalski and R.L. Chilausky, Learning by Being Told and Learning from Examples: An Experimental Comparison of the Two Methods of Knowledge Acquisition in the Context of Developing an Expert System for Soybean Disease Diagnosis, Policy Analysis and Information Systems 4, Nr. 2 (June, 1980) 125–260.

[19] R.S. Michalski and R. Stepp, Learning from Observation: Conceptual Clustering, in: R.S. Michalski, J.G. Carbonell and T.M. Mitchell, eds., Machine Learning (Tioga, Palo Alto, 1983).

[20] T. Mitchell, Generalization as Search, Artificial Intelligence 18 (1982) 203–226.

[21] A. Newell and H.A. Simon, Human Problem Solving (Prentice-Hall, Englewood Cliffs, 1972).

[22] Y.E. Orgler, A Credit Scoring Model for Commercial Loans, Journal of Money, Credit and Banking (Nov., 1970) 435–445.

[23] J.R. Quinlan, Discovering Rules from Large Collection of Examples: A Case Study, in: D. Michie, ed., Expert Systems in the Micro Electronic Age (University Press, Edinburgh, 1979).

[24] L. Rendell, A New Basis for State-Space Learning Systems and a Successful Implementation, Artificial intelligence 20 (1983) 369–392.

[25] M. Shaw, A Knowledge-Based Framework for Distributed Decision Support, Simulation and Modeling 16, in: W. Vogt and M. Mickle, eds. (The Instrument Society of America, 1985).

[26] M. Shaw and P.L. Tu, An Integrated Framework for Knowledge-Based Decision Support, Working paper, University of Illinois, Department of Business Administration (1986).

[27] E.H. Shortliffe and B.G. Buchanan, A Model of Inexact Reasoning in Medicine, Mathematical Biosciences 23 (1975) 351–379.

[28] S.A. Vere, Induction of Concepts in the Predicate Calculus, Fourth International Joint Conference on Artificial Intelligence, Tbilisi, USSR (1975) 281–287.

[29] P.H. Winston, Learning Structural Descriptions From Examples, in: The Psychology of Computer Version (McGraw-Hill, New York, 1975).

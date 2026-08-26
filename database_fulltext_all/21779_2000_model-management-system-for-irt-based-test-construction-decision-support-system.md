---
otero_id: 21779
otero_key: "DEGKJ6MK"
title: "Model management system for IRT-based test construction decision support system"
authors: "Ing-Long Wu"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00047-0"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Model management system for IRT-based test construction decision support system

Ing-Long Wu )

Department of Management Information Systems, National Yunlin UniÕersity of Science and Technology, 123 UniÕersity Road, Touliu, Yunlin, Taiwan

Accepted 18 August 1999

## Abstract

Decision support system DSS has become widespread for some specific domains in recent years. However, DSS forŽ . IRT-based item response theory test construction has not yet been developed. This domain basically imposes aŽ . semi-structured or unstructured decision and, therefore, involves a very complex modeling process. This study develops a model management system MMS architecture to assist a non-expert user in manipulating test construction processŽ . efficiently and effectively. This architecture consists of four components: problem analysis, model type selection, model formulation and solver. The model type selection subsystem is further organized into three levels of hierarchy, i.e., environment, structure and parameter. A prototype is presented to demonstrate the feasibility of this architecture. The results indicate that this approach can be applied for providing an integrated, flexible and user-friendly DSS environment for producing better quality of results in less solution time. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: Model management system; Decision support system; Relational data base; Item response theory; Test construction

## 1. Introduction

There have been considerable studies on automated item selection methods in test construction based on item response theory IRT . These meth-Ž . ods, frequently implemented on microcomputers, provided several potential benefits to test specialists, including reducing labor costs and increasing the efficiency of test construction. However, the computerized implementation was made only for the individual test construction method. A complete information system, which can integrate all the different purposes of test construction methods discussed in the literature, does not exist in the test construction domain. It is because the process for developing such an information system is very complex. Two considerations are involved in the solution process of these methods, namely mathematical model formulations and solution algorithms. The combination of these two considerations will produce large varieties of the solution processes for these methods.

First, there were considerable test construction methods for special types of test construction problems. An instance of these methods for solving a test construction problem is as follows. For the problem of a minimum-length test while fulfilling test specifications, Knapsack model can be applied to model this problem 34 , and a particular solution algorithm<sup>w</sup> <sup>x</sup> or a standard integer programming IP algorithmŽ . can be used to solve this model 25 . Second, test<sup>w</sup> <sup>x</sup> construction problems could be very general in terms of the structures of mathematical formulations for test specifications. The standard IP algorithms or the available heuristics are the possible ways to solve these general IP models. Finally, a couple of computerized programs non-mathematical programmingŽ solution procedures have been developed to target. some test construction problems. As a result, the solution processes for test construction problems truly impose very complex decision choices for test specialists. Furthermore, test construction problems also involve single or multiple test construction for traditional or adaptive testing. Besides, end-user computing is the future trend for organizations to develop information systems by themselves. In other words, tests are most likely to be assembled by test specialists rather than by technical experts.

In practice, test specialists are not technical experts for test construction and they often assume that a predetermined method can be duplicately employed to solve all the similar problems. However, a good practice should have different decision processes for test construction problems in order to obtain more satisfactory results in less solution time. The reasons underlying this practice are as follows. A test construction problem may have alternative ways to formulate mathematical models, and in turn, solution algorithms will be different. The solution algorithms for a mathematical model formulation may be multiple 38 . In ‘‘what-if’’ analysis, test specialists constantly review the psychometric and content-related properties of assembled tests, refine the test specifications as needed, and repeat the process until a satisfactory test is assembled.

In sum, test construction basically imposes semistructured or unstructured decisions and a series of ‘‘what-if’’ analyses for refining the results. Thus, an information system for test construction is imperative for supporting the complex decision process. The main purpose of a decision support system Ž . DSS is recognized to support these features. However, little has been done on developing a DSS for IRT-based test construction. Therefore, this study aims to develop a DSS for test construction TCDSSŽ . with a flexible, dynamic environment to assist test specialists in manipulating the complex process. In particular, the focus of this study is on the design of model management system MMS . In fact, the mostŽ . important factor for making this design process feasible is due to the specific domain of IRT-based test construction. Some of the helpful features for simplifying the design of MMS will be discussed in the following sections.

In here, for the purpose of clarity in the following discussion, model instance and model type are distinguished. Model instance is a specific formal representation of a problem instance. Model type is a collection of model instance characterized by a set of rules and<sup>r</sup>or properties that distinguish instances of a model type from those of other model types. For instance, Knapsack problem represents a model type and ‘‘Min. $3 x _ { 1 } + 5 x _ { 2 }$ subject to $3 x _ { 1 } + 5 x _ { 2 } \geq 1 0 ~ x _ { 1 }$ and $x _ { 2 } = 0$ or $1 ^ { \circ \bullet }$ is a model instance of Knapsack problem. In the rest of this paper, model type and model are sometimes used interchangeably to be consistent with traditional definition.

## 2. Problem domain

## 2.1. IRT

The following introduction of IRT is a synopsis of results from Refs. 18,22 . The probability of a cor-<sup>w</sup> <sup>x</sup> rect response to a test item is modeled as a function of the examinee’s ability and certain characteristics of the item. Several kinds of IRT-models have been proposed for dichotomously, multi-chotomously and continuously scored responses. For the sake of illustration, a three-parameter logistic model for dichotomous response is considered. Let be a scalar representing the examinee’s ability and $a _ { i } , ~ b _ { i } .$ , and $c _ { i }$ be the discrimination, difficulty, and guessing parameters of item i, respectively. The probability of a correct response for an examinee with ability value is modeled as

$$
P _ {i} (\theta) = c _ {i} + (1 + c _ {i}) \frac {\mathrm{e} ^ {D a _ {i} (\theta - b _ {i})}}{1 + \mathrm{e} ^ {D a _ {i} (\theta - b _ {i})}}
$$

where D is the scaling factor equal to 1.7 and $\theta \in ( - \infty , + \infty ) . \ P _ { i } ( \theta )$ represents an item characteristic function. The usual procedure for estimating item parameters in an item bank is to use response data from a sample of examinees. Common estimation methods are maximum likelihood and Bayesian estimation. Once their parameters are known, the items can be used to estimate the ability of each new examinee. The maximum likelihood estimation is used to illustrate this.

Let $U _ { 1 } , \dots , U _ { n }$ denote the response variables of a new examinee to a n-item test from the item bank. Under local independence, that is, independence between the response variables for a fixed value of $\theta ,$ the likelihood function associated with a response value vector $u _ { 1 } , \ldots , u _ { n }$ is equal to

$$
L \left(u _ {1}, \dots , u _ {n} \mid \theta ; \mathbf {a}, \mathbf {b}, \mathbf {c}\right) = \prod_ {i = 1} ^ {n} P _ {i} (\theta) ^ {u _ {i}} \left[ 1 - P _ {i} (\theta) ^ {1 - u _ {i}} \right]
$$

where $\mathbf { a } = ( a _ { 1 } , \ldots , a _ { n } ) , \mathbf { b } = ( b _ { 1 } , \ldots , b _ { n } ) ,$ , and $\mathbf { c } =$ $( c _ { 1 } , \ldots , c _ { n } )$ . The maximum of the likelihood function $L ( u _ { 1 } , \dots , u _ { 2 } | \theta ; \mathbf { a } , \mathbf { b } , \mathbf { c } )$ or, equivalently, ln $L ( u _ { 1 }$ $\qquad \cdots \mathbf { , } u _ { 2 } | \theta ; \mathbf { a , b , c } ) ,$ , is attained when satisfies the likelihood equation

$$
\frac {\partial}{\partial \theta} \ln L (u _ {1}, \dots , u _ {n} | \theta ; \mathbf {a}, \mathbf {b}, \mathbf {c}) = 0.
$$

The likelihood equation can be solved, for instance, by the Newton–Raphson procedure.

A well-known measure for the information in a sample of response values $u _ { 1 } , \ldots , u _ { n } \ { \mathrm { ( } n { \mathrm { - i t e m ~ t e s t ) } } }$ is Fisher’s 19<sup>w</sup> <sup>x</sup>

$$
\begin{array}{r l} I _ {u _ {1} \dots u _ {n}} (\theta) & = - E \left[ \frac {\partial^ {2}}{\partial \theta^ {2}} \ln L \right] \\ & = \sum_ {i = 1} ^ {n} \frac {\left[ P _ {i} ^ {\prime} (\theta) \right] ^ {2}}{P _ {i} (\theta) [ 1 - P _ {i} (\theta) ]} \end{array}
$$

Because local independence is assumed in IRT, the information in $u _ { 1 } , \ldots , u _ { n }$ is additive on the individual response. Therefore, it follows that

$$
\begin{array}{l} I (\theta) = I _ {u _ {1} \dots u _ {n}} (\theta) = \sum_ {i = 1} ^ {n} I _ {i} (\theta) \\ = \sum_ {i = 1} ^ {n} \frac {\left[ P _ {i} ^ {\prime} (\theta) \right] ^ {2}}{P _ {i} (\theta) [ 1 - P _ {i} (\theta) ]}. \end{array}
$$

IŽ . and $I _ { i } ( \theta )$ denote test information function Ž . TIF and item information function, respectively. The reason for using maximum likelihood scoring is the availability of $I ( \theta )$ as an asymptotic measure for the accuracy by which the test measures the examinee’s ability. That is, the reciprocal of $I ( \theta )$ is the asymptotic variance of maximum likelihood estimator ${ \bar { \theta } } .$ The mathematical notation is expressed as $\operatorname { V a r } ( { \hat { \theta } } | \theta ) = [ I ( \theta ) ] ^ { - 1 }$ The smaller the asymptotic variance of ${ \widehat { \theta } } ,$ the higher the accuracy of ability measured at . Accordingly, Birnbaum 9 proposed<sup>w</sup> <sup>x</sup> using TIF to create a test based on IRT. Lord 22<sup>w</sup> <sup>x</sup> further presented iterative steps for a heuristic method to match a predetermined TIF with values at specific ability levels. In addition, item information function is the comprising element of TIF and thus it is the building block for a test. In general, an item information function is bell-shaped. Thus, the contribution and impact of each item on a test can be predetermined during the test construction process.

## 2.2. Test construction

Test construction in IRT involves a relatively broad domain. The following will discuss the intrinsic and extrinsic properties of test construction.

Intrinsically, test specifications and objective functions are basic inputs for test construction. Test specifications are rules for including items in a test. These rules invariably include constraints on both psychometric and content-related properties, and may also include consideration of other properties not related to the above. Psychometric constraints are relevant to TIF 22 . For instance, a test might satisfy<sup>w</sup> <sup>x</sup> the specified heights of TIF at certain ability levels. Content-related constraints can be of many types <sup>w</sup> <sup>x</sup> 14 . Content restrictions set boundaries on the number of items with a particular content classification that may be included in a test. For instance, a mathematics test might include a specified number of geometry, algebra and trigonometry items. Item format or item type restrictions constrain the number of items having each of the possible formats in a test. For instance, a verb test might include specifications for the number of sentence completion, word matching and sentence correction items to be administered. Other restrictions such as administration time may also be imposed in a test 15 .<sup>w</sup> <sup>x</sup>

Objective functions target forms as test specifi- Ž . cations also have alternative formats, for instance, maximization of relative shape TIF, minimization of test length, maximization of TIF at specific ability levels, minimization of the sum of absolute deviation from a target test, and so forth 36 . In other cases,<sup>w</sup> <sup>x</sup> the objective function intends to match a target test <sup>w</sup> <sup>x</sup> <sup>w x</sup> 6,23 or TIF at specific ability levels 38 as close as possible. All of these test specifications and objective functions can be expressed mathematically as linear functions in the traditional IP forms. Therefore, these properties could produce large varieties of IP models for test construction problems.

As for the extrinsic properties, they can be explored from the following aspects. First, there are two testing settings, i.e., traditional testing 6,14, <sup>w</sup> 15,34,36 and adaptive testing 3,31,35,38 . Tradi-<sup>x</sup> <sup>w x</sup> tional testing is to administer the same test to all examinees, while some forms of adaptive testing are to administer a battery of tests with various ability levels to one examinee. Adaptive testing can be used in many testing situations. One example is the need for presenting each examinee with a second test adapted to his<sup>r</sup>her individual latent ability after the ability is estimated through the first routing test in a two-stage testing procedure. Another would be to provide progressively more difficult tests in ability to measure test progress longitudinally. Therefore, test construction methods for these settings are quite deviated and need different treatments.

Second, test construction methods from an item bank can be classified into two types, i.e., sequential approach 33–36 and simultaneous approach<sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> 6,13,14,23,38 . Obviously, the sequential approach can also be used to accomplish the construction of multiple tests from an item bank. However, the sequential approach does not obtain the satisfactory results 13 , because the test construction procedure<sup>w</sup> <sup>x</sup> cannot optimally distribute items from an item bank to these tests that are sequentially generated. In other words, an item is considered to be fitted into the first test while it would be better fitted into one of the other tests. The larger the number of generated tests, the greater the disadvantage. However, the simultaneous approach often creates more difficult situation than the sequential approach in terms of computational complexities. Therefore, test specialists need to decide which approach is more suitable for the test construction problems with respect to its strength and weakness.

Finally, recent developments on solution approaches have been focused on two major categories. The first category involves the development for special types of IP models with solution algorithms based on a simplex search 4,6,14,15,35,36,38 . In<sup>w</sup> <sup>x</sup> general, it could not be solved in a reasonable solution time. Therefore, some specialized algorithms and heuristics of the standard IP algorithms are hereafter developed in order to reduce the computational efforts. One of the heuristic instances is the relaxation of decision variable discreteness to be LP model that can be solved quickly by simplex algorithm and rounding of results. The second category consists of heuristic methods to search the item bank in a systematic manner to create tests in less solution time. However, it may not formally search for an optimal solution 1,23,31,33 . This creates a trade-off<sup>w</sup> <sup>x</sup> between quality of tests and solution time for decision choices. Furthermore, test construction problems are typically formulated as general IP models on the basis of various test specifications and objective functions 3,5,7,34 . The standard IP algorithms <sup>w</sup> <sup>x</sup> are often used, or in some cases, heuristics of the standard IP algorithms are available to solve these models.

## 3. Design of MMS

From the previous discussion, the best solution to such a complex process of test construction is to develop a specific MMS to provide decision support for test specialists. This section is organized as follows. First, an example of mathematical models is presented to describe what comprises a model in the test construction domain in order to facilitate the following discussion of the design of MMS. Second, a schematic framework of MMS and a detailed MMS architecture for TCDSS are proposed. Finally, the model management theories underlying each portion of the MMS architecture and their implications to the MMS design of TCDSS are discussed. In addition, as each portion of the MMS architecture is discussed, an appropriate detail of the prototyping system is designed for each portion.

## 3.1. The mathematical model

The following model involves the simultaneous generation of K multiple tests from an item bank by matching a target test. This model generates tests through an item-matching process Item-MatchingŽ model , which optimally matches items in the item. bank to items in the target test. This model has the special network structure named transportation network. The target test also contains G content areas and each area has a required number of items. A more detailed description of this model can be found in Ref. 6 .<sup>w</sup> <sup>x</sup>

Minimize $Z = \sum _ { i = 1 } ^ { N } \sum _ { j = 1 } ^ { n } d _ { i j } x _ { i j }$

subject to

$$
\begin{array}{l} \sum_ {j = 1} ^ {n} x _ {i j} + y _ {i} = 1 \qquad i = 1, \ldots , N \\ \sum_ {i = 1} ^ {N} x _ {i j} = K \qquad j = 1, \ldots , n \\ \sum_ {i \in C _ {g}} y _ {i} = N _ {g} - K \times c _ {g} \qquad g = 1, \ldots , G \\ x _ {i j} \text { and } y _ {i} \in \{0, 1 \} \end{array}
$$

where $x _ { i j } { \mathrm { . } }$ decision variable, equal to 1 if item i in the item bank is matched to item j with the same content area and equal to 0 otherwise; $y _ { i } { \mathrm { : } }$ decision variable, equal to 1 if item i is assigned to the set of unused items and equal to 0 otherwise; $d _ { i j } \colon$ the distance between item i and item $j ; N ;$ the number of items in the item bank; n: the number of items in the target test; G: the number of content areas in the target test; K: the number of the generated tests from the item bank; $C _ { g }$ : the set of all items with the same content area g in the item bank; $N _ { g }$ : the cardinality of $C _ { g } ; c _ { g } \mathrm { . }$ the required number of items for content area g in a test.

## 3.2. Architecture of MMS

In this section, the schematic framework of MMS for TCDSS is presented in Fig. 1, while the detailed MMS architecture for TCDSS is presented in Fig. 2. This architecture comprises four subsystems: problem analysis, model type selection, model formulation and solver. The model type selection subsystem is further organized into three levels of hierarchy, i.e., environment, structure and parameter 8 .<sup>w</sup> <sup>x</sup>

![](/api/attachments/DEGKJ6MK/fulltext/images/7291869164753248cf6c79606fb1c83ff9d0aa9118a5b180a328475f097e1180.jpg)  
Fig. 1. Schematic framework of MMS.

## 3.3. Problem analysis subsystem

The problem analysis subsystem is mainly based on the problem structuring concept 28,29,37 . The<sup>w</sup> <sup>x</sup> main purpose of the concept is to gain intellectual control over a complex problem. That is, a complex problem can be decomposed into smaller, more manageable subproblems. The decomposing process will be continuously elaborated until each subproblem description is simple enough for further processing. The implication to the design of this subsystem is described as follows. As mentioned in Section 2.2, the design of MMS for such a relatively broad and unspecific domain cannot proceed until the complex problem is divided into more specific and concrete subproblems. After that, it will be much easier to design more specific model type selection modules and solver modules for these subproblems. A feasible approach is to apply the problem structuring concept under which test construction domain can be decomposed according to some domain-related criteria. In this case, such criteria can be explored such a way that they are able to progressively<sup>r</sup>hierarchically break down the complex structure into smaller, simpler structures. Accordingly, these criteria can be determined as testing settings, types of test construction method, and types of target form. The detailed explanation of these criteria can be found in Section 2.2.

This subsystem is designed according to the upper part of the MMS architecture in Fig. 2. Therefore, the physical prototype for this subsystem provides the following three functions to analyze test construction problems hierarchically.

<sup>Ø</sup> A choice menu for listing traditional testing or adaptive testing.

![](/api/attachments/DEGKJ6MK/fulltext/images/26a46ebeb75e24c809671a9659fb3c480de1c5a2bd53e20b81cbe986dc722f37.jpg)  
Fig. 2. MMS architecture for TCDSS.

<sup>Ø</sup> A choice menu for listing single or multiple test construction method.

<sup>Ø</sup> A choice menu for listing all possible types of target test forms. Alternately, a menu for manually inputting types of target test forms.

## 3.4. Model type selection subsystem

As the above discussion, it will be much easier to design more specific model type selection modules and solution procedures after problem structuring. The model type selection subsystem presented here is built on the concept of Banerjee and Basu 8 .<sup>w</sup> <sup>x</sup> They organize different model types in a four-level abstraction scheme, i.e., environment, structure, parameter and solver. The major difference between Banerjee and Basu’s work and our framework is that the former defines the solver level as one of the model type selection scheme, whereas the latter defines it as an independent subsystem since its purpose is mainly to differentiate between different algorithmic approaches rather than choosing a model type. The following first discusses the three levels of abstraction scheme, and then a general model management framework is presented for this subsystem.

## 3.4.1. EnÕironment leÕel

The environment level is the highest level of abstraction in the classification scheme. A potential model type is determined by matching broad problem-solving characteristics of the problem and its environment. Information required is mainly from environmental factors which help define the objective or goal of the problem. The implication to the design of this level can be described as follows. The main purpose of test construction is to generate more satisfactory results in less solution time while satisfying various test specifications. These factors resultsŽ and solution time are mainly for identifying the goal. of test construction and are not involved in any specific matters about the problem itself. Therefore, they can be classified as the environmental factors. As a result, the classification of potential model types for this level is defined as mathematical programming approach MPA and non-mathematicalŽ . programming approach NPA since these two ap- Ž . proaches are the major determinants of quality of results and solution time. The discussion related to these two approaches can be found in Section 2.2.

From the above discussion, the prototype for this level supports the following features:

<sup>Ø</sup> An automated suggestion for choosing NPA or MPA based on an existing knowledge base. This knowledge base summarizes past experience for linking solution approaches NPA or MPA to variousŽ . choices during problem analysis process, i.e., three hierarchically analyzing choices.

<sup>Ø</sup> User’s own choice for NPA or MPA.

<sup>Ø</sup> A ‘‘what-if’’ function provided to try alternative solution approaches in the environment level for comparison.

## 3.4.2. Structure leÕel

The second level of model type classification is based on the structural characteristics of the parameters of the problem instances in order to define the class of model types. Such structural information about a problem instance is usually captured in the state description of its systematic solution procedure Žstate variable properties or relationships between state variables . For instance, in linear programming. models the relationship between all the variables must be linear, whereas, in non-linear programming models the relationship between them is non-linear for at least one set of variables. These state descriptions, in turn, determine the types of solution techniques used for solving these models. The concept for distinguishing the three views of models in Chang et al. 16 , i.e., the procedure, data and problem <sup>w</sup> <sup>x</sup> statement view, is similar to the structural characteristics discussed above for defining the classes of model types.

The implication of the distinguishing concept to the design of this level can be explained as follows. From the discussion in the test construction subsection, the solution processes for MPA and NPA appear to be totally different. Accordingly, NPA is further defined as the procedure view of models since both classifications imply similar structural characteristics. The class of model types is treated as the computerized procedures that can process queries for data retrieval and program execution. Examples of this class can be found from Fig. 2 1,23,31,33 .<sup>w</sup> <sup>x</sup> For MPA, the existing literature has proposed some special types of IP models along with the particular solution algorithms for test construction. The class of model types presents similar structural characteristics as that of the problem statement view of models and can be defined as a separate class of model types. Examples of this class can be found from Fig. 2 <sup>w</sup> <sup>x</sup> 4,6,14,15,35,36,38 . The others for general IP models, which are usually solved by the standard IP algorithms, are defined as the data view of models. Examples of this class can be found from Refs. <sup>w</sup> <sup>x</sup> 3,5,7,34 . Finally, the prototype for this level will be presented in Section 3.4.4.

## 3.4.3. Parameter leÕel

The final level of this classification is based on the specific parameter values for a given problem instance to differentiate model types in a class. The distinguishing characteristics of model types at this level are mainly in terms of the domains of their different parameters, such as inputs and outputs. For instance, the difference between transportation model and assignment model can be found on the right hand side of the constraint matrix, i.e., the b vector for the mathematical model: Min. CX, subject to AX <sup>G</sup> b, X <sup>G</sup> 0. It must be integer values for transportation model and unity for assignment model. Therefore, it is possible that the specific characteristics of a problem instance allow it to be matched with multiple model types at the parameter level, provided that they occur within the same structural class of model types.

The implication to the design of this level can be explained as follows. From the discussion in Section 2.2, the same structural class each view of modelsŽ .

will comprise multiple model types due to different input<sup>r</sup>output parameter values. For instance, Item-Matching model and Knapsack model are mainly differentiated from different input parameter values. Finally, the prototype for this level will be presented in Section 3.4.4.

## 3.4.4. Model management framework

After the discussion of the three levels of abstract scheme, the following presents a general model management framework for the three views of models. The model management framework contains two parts. The first part is built on Blanning’s concept <sup>w</sup> <sup>x</sup> 10–12 , which uses relational data base to store and manipulate model information. The second part involves the design of a searching mechanism for model selection and input data retrieval. The basic concept for the searching mechanism is similar to Liang’s technique 20 . The major difference be- <sup>w</sup> <sup>x</sup> tween Liang’s technique and the proposed mechanism is that the former is designed for a graph-based structure, whereas the latter is focused on the application of relational data base structure.

The process of designing the model management framework is described as follows. First, a relation contains the following attributes: CONDITION, MODEL, INPUT1 . . . INPUTn, and OUTPUT. CONDITION attribute stores condition of model usage such as matching a target test a type of target Ž form . MODEL stores model types for usage such as. Item-Matching model. INPUT1 . . . INPUTn stores input data for objective functions, psychometric constraints, content-related restriction, item format and so forth. OUTPUT stores output data from model instance execution. Next, the searching mechanism framework is listed as follows and is shown in Fig. 3.

1. Search CONDITION to find whether there is a match between condition and user requirement.

2. If a match is not found, then stop searching. The system may ask user to try alternative searching mechanisms.

![](/api/attachments/DEGKJ6MK/fulltext/images/d80c9fd83410f55a034d469458b26fb9fcc0e965dcefa2c3e92df799d94b82fa.jpg)  
Fig. 3. Searching mechanism framework.

3. If a match is found, then search MODEL to find an appropriate model from organized knowledge or user experience.

4. Pick up consecutive input data from INPUT 1 . . . INPUT n until all input data are obtained for further processing.

4.1. If input data are available, then retrieve it and go back to Step 4 .Ž .

4.2. If input data are not available, then find related relation relational architecture ,Ž . where a calculation procedure is stored to produce output data from the corresponding input data i.e., output data of related rela- Ž tion is input data of original relation , to get. input data from OUTPUT of related relation and go back to Step 4 .Ž .

4.3. If both of the above are not available, then interact with user to specify input data and go back to Step 4 . Ž .

5. The process can be re-started from Step 3 if userŽ . needs to see more comparisons among different models what-if function .Ž .

According to the above design of a general model management framework, the physical prototype for the three views of models provides the following features:

<sup>Ø</sup> An automated switch to procedure view of models if NPA is selected in the environment level.

<sup>Ø</sup> An automated suggestion for choosing data or problem statement view of models based on an existing knowledge base. This knowledge base is created from past experience for selecting a more appropriate view of models if MPA is selected in the environment level.

<sup>Ø</sup> A relation data base created for each view of models to store model information.

<sup>Ø</sup> A searching mechanism for each view of models as in Fig. 3 developed for automating selection of an appropriate model and retrieving input data.

<sup>Ø</sup> The ‘‘what-if’’ function provided to try alternative models in the same class for comparison.

After an appropriate model type is selected and the corresponding input data is retrieved, a model formulation subsystem for the three views of models is used to prepare model instances for further solver execution. For the procedure view of models, the class of model types is considered as the computerized procedures that can process queries for data retrieval and program execution. Model formulation is primarily focused on input data retrieval and, therefore, is part of the searching mechanism. For the data view of models, the class of model types is defined as general IP models since it treats the constraint matrix as data<sup>r</sup>inputs to describe<sup>r</sup>model a problem. Model formulation basically comprises three steps: input data retrieval, constraint matrix generation and model instance formulation 17,<sup>w</sup> 24,32 . For the problem statement view of models,<sup>x</sup> the class of model types is categorized as special types of IP models since the mathematical forms are predefined in advance. One of the examples is the Item-Matching model. Model formulation is primarily focused on input data retrieval and model instance formulation. In sum, the essential features for the three views of models are summarized in Table 1.

From the above discussion, the prototype for this subsystem provides the following features:

<sup>Ø</sup> A model formulation module for procedure view of models. The purpose of this module is mainly to retrieve input data for further solver execution. Therefore, this module is part of the searching algorithm.

<sup>Ø</sup> A model formulation module for data view of models. This module includes three functions: input data retrieval, constraint matrix generation from input data, and model instance formulation from constraint matrix. Here, the function of input data retrieval is part of the searching algorithm.

## 3.5. Model formulation subsystem

<sup>Ø</sup> A model formulation module for problem statement view of models. This module contains two functions: input data retrieval and model instance formulation from input data. Here, the function of input data retrieval is part of the searching algorithm.

## 3.6. SolÕer subsystem

This subsystem involves a selection process of solution algorithms for the above selected model in a class. Basically, the decision criteria can be classified into two categories: 1 the problem parametersŽ . Ž .i.e., number of decision variables and constraints and 2 the availability and the economic feasibility.Ž . In contrast to the first category, the second category is not problem specific but is a representation of the environment within which the problem is being solved. The implication to the design of this subsys tem can be explained as follows.

Table 1  
Essential features for three views of models

<table><tr><td>Model view</td><td>Model type</td><td>Model management</td><td>Model formulation</td></tr><tr><td>Procedure</td><td>Computerized procedures</td><td>(1) Focus on input data retrieval(2) Use of relational data base(3) A searching mechanism</td><td>(1) Input data direct for execution</td></tr><tr><td>Data</td><td>General IP models</td><td>(1) Focus on coefficient of objective function and constraints(2) Use of relational data base(3) A searching algorithm</td><td>(1) Input data(2) Constraint matrix generation(3) Model instance formulation</td></tr><tr><td>Problem statement</td><td>Special type of IP models</td><td>(1) Focus on predefined structure of mathematical form(2) Use of relational data base(3) A searching mechanism</td><td>(1) Input data(2) Model instance formulation</td></tr></table>

For the procedure view of models, no problem arises since the models are the solution procedures. For the data view of models, the general IP models in this class can be regularly solved by the standard IP algorithms. However, many of the cases involve relatively large item bank i.e., decision variablesŽ . and large number of constraints for test specifications. The standard IP algorithms may be impractical in terms of solution time. Much research has been carried out in this area to develop approximations. A comprehensive review of this research is given in Ref. 26 . However, many of the heuristics aim at<sup>w</sup> <sup>x</sup> special types of problems and are not applicable to test construction.

Recently, the feasible approaches for this domain have been proposed by Adema 2 and van der <sup>w</sup> <sup>x</sup> Linden and Boekkooi-Timminga 36 . They pro- <sup>w</sup> <sup>x</sup> duced quite satisfactory results. Examples of the heuristics are: 1 relaxing the assumption of deci-Ž . sion variable discreteness in the model and rounding the result, 2 stopping a branch-and-bound algo- Ž . rithm after a number of steps e.g., first 0–1 solu-Ž tion , and 3 using a branch-and-bound algorithm. Ž . for remaining fractional decision variables after LP solution of the relaxed 0–1 programming model.

For the problem statement view of models, some of the special IP models in this class have the special network structures such as Item-Matching model, and could be solved by the specialized network algorithms with better quality of tests in less solution time 6 . The others in this class could be solved by <sup>w</sup> <sup>x</sup> either the standard IP algorithms or the above discussed heuristics. In sum, the decision criteria for selecting solution algorithms on this domain are dependent on the solution time, quality of results, availability and convenience.

From the above discussion, the prototype for this subsystem supports the following features:

<sup>Ø</sup> A solver module for procedure view of models to pick up an appropriate solution algorithm. Actually, this module is part of the searching algorithm since the model is the computerized procedure.

<sup>Ø</sup> A solver module for data view of models to pick up an appropriate solution algorithm based on an existing knowledge base. This knowledge base stores a comparison table for listing weakness and strength of various solution algorithms to these solved models.

<sup>Ø</sup> A solver module for problem statement view of models to pick up an appropriate solution algorithm based on an existing knowledge base. This knowledge base contains rules for linking the specialized algorithms to the special IP models and a comparison table as the above one for the other solution algorithms in the class.

<sup>Ø</sup> The ‘‘what-if’’ function provided to try alternative solution algorithms for comparison.

## 4. Experimental run for the prototype

The above prototype is implemented by Delphi for Windows 95 development tool. The reasons for this choice are as follows. First, it provides a powerful environment to create windowed user interface and various features to connect with other software system, such as ODBC Open Data Base Connectiv-Ž ity for accessing data from heterogeneous data bases. and DDE Dynamic Data Exchange for exchangingŽ . data or transmitting data between different application programs. In particular, user interface subsystem Ž . dialog subsystem is considered as a major component of DSS because much of the power, flexibility and ease-of-use characteristics are derived from this subsystem 30 . Next, Delphi is developed by Pascal<sup>w</sup> <sup>x</sup> source code and thus, this causes no problem with compatibility for embedding Pascal code into Delphi procedures. This is because the major functional components of the prototype, i.e., the searching algorithms and the knowledge bases, are developed in Pascal code.

The item bank used in this experiment consists of 520 items on 13 previously administered mathematics tests from the American College Testing Program distributed over six content areas with 104, 182, 52, 104, 52 and 26 items in each content area. Besides, a target test associated with the item bank consists of 40 items distributed over the corresponding content areas with 8, 14, 4, 8, 4 and 2 in each content area. The item bank includes the discrimination, difficulty and guessing parameters for each item, and so does the target test.

Two test construction problems are presented for illustration purpose. The first problem involves the simultaneous generation of six multiple tests from an item bank by matching a target test as close as possible. These tests are termed as weakly parallel tests. Two or more tests are weakly parallel if they have identical TIFs and they measure the same trait <sup>w</sup> <sup>x</sup> 21,27 . The second problem considers a discrete point-wise matching to five predetermined TIFs at three specified ability levels as close as possible to generate five tests with progressively more difficulty in ability levels.

The first sample consultation process of the prototype for producing six multiple tests is illustrated as follows.

Problem analysis subsystem:

<sup>Ø</sup> Choice for testing settings. Select traditional testing.

<sup>Ø</sup> Choice for types of test construction methods. Select multiple test construction.

<sup>Ø</sup> Choice for types of target forms. Select matching a target test as the type of target form. Model type selection subsystem:

<sup>Ø</sup> Choice for categories of solution approaches in the environment level. The prototyping system searches the knowledge base based on the previous premises to suggest a decision to the user, i.e., MPA decision.

<sup>Ø</sup> Choice for model views in the structure level. The prototyping system searches the knowledge base based on the previous premises to choose either data or problem statement view of models. Suggest problem statement view of models.

<sup>Ø</sup> Choice for model types in the parameter level. The prototyping system starts the searching algorithm of problem statement view of models. Pick up Item-Matching model and retrieve the corresponding input data.

Model formulation subsystem:

<sup>Ø</sup> Model instance formulation. The prototyping system executes the model formulation module of problem statement view of models. Formulate this model instance from input data and predefined mathematical structure of this model.

Solver subsystem:

<sup>Ø</sup> Choice for solution algorithms. The prototyping system searches the knowledge base based on the previous premises to suggest a decision. Pick up a specialized network algorithm since this model has a special network structure. The specialized network algorithm is implemented by Pascal code. Measuring results:

<sup>Ø</sup> The results are stored in the model base and some of the results are graphically presented on the screen as Fig. 4 for user review.

<sup>Ø</sup> To make a comparison, the user can try other categories of solution approaches through ‘‘whatif’’ function. The NPA is selected. The prototyping system then follows the searching algorithm of procedure view of models, and picks up L–H solution procedure along with the corresponding inputs. The solution procedure is implemented by Pascal code.

![](/api/attachments/DEGKJ6MK/fulltext/images/b5dc59f31ab7a05fe869f1be7fad4a4bcc1ad5b498ffab8deca6a8602bdf7614.jpg)  
Fig. 4. Results of item-matching model.

<sup>Ø</sup> The results are stored in the model base and some of the results are graphically shown on the screen as Fig. 5 for user review.

At this point, the user has the opportunity to review the different results and may decide whether to proceed with the modeling process or not. If yes, ‘‘what-if’’ functions can re-start the alternative modeling process at any portion of the MMS and present more results for comparisons in terms of quality and solution time. In this illustration, the result in Fig. 4 is slightly better than that in Fig. 5 in terms of matching closeness.

![](/api/attachments/DEGKJ6MK/fulltext/images/b8f61a9b883a5e6d8b56a9463fbeba7fef04e2974fde7ed6c47fcafe446cd1d1.jpg)  
Fig. 5. Result of L–H method.

Table 2  
Five adaptive tests generated from test specifications

<table><tr><td>Test number</td><td>Test specification</td><td>Generated TIF</td></tr><tr><td rowspan="3">1</td><td> $I(-0.5) = 15$ </td><td>15.2</td></tr><tr><td> $I(0.0) = 20$ </td><td>18.5</td></tr><tr><td> $I(0.5) = 15$ </td><td>14.6</td></tr><tr><td rowspan="3">2</td><td> $I(-0.2) = 15$ </td><td>15.4</td></tr><tr><td> $I(0.3) = 20$ </td><td>18.4</td></tr><tr><td> $I(0.8) = 15$ </td><td>15.7</td></tr><tr><td rowspan="3">3</td><td> $I(0.1) = 15$ </td><td>16.4</td></tr><tr><td> $I(0.6) = 20$ </td><td>20.0</td></tr><tr><td> $I(1.1) = 15$ </td><td>16.0</td></tr><tr><td rowspan="3">4</td><td> $I(0.4) = 15$ </td><td>16.2</td></tr><tr><td> $I(0.9) = 20$ </td><td>19.3</td></tr><tr><td> $I(1.4) = 15$ </td><td>15.9</td></tr><tr><td rowspan="3">5</td><td> $I(0.7) = 15$ </td><td>15.8</td></tr><tr><td> $I(1.2) = 20$ </td><td>19.1</td></tr><tr><td> $I(1.7) = 15$ </td><td>15.1</td></tr></table>

The second sample consultation process of the prototype for producing five multiple tests with progressively more difficulty in ability levels is illustrated as follows.

Problem analysis subsystem:

<sup>Ø</sup> Choice for testing settings. Select adaptive testing.

<sup>Ø</sup> Choice for types of test construction methods. Select multiple test construction.

<sup>Ø</sup> Choice for types of target forms. Select matching TIFs at specified ability levels as the type of target form.

Model type selection subsystem:

<sup>Ø</sup> Choice for categories of solution approaches in the environment level. The prototyping system searches the knowledge base based on the previous premises to suggest a decision to the user, i.e., MPA decision.

<sup>Ø</sup> Choice for views of models in the structure level. The prototyping system searches the knowledge base based on the previous premises to choose either data or problem statement view of models. Suggest problem statement view of models.

<sup>Ø</sup> Choice for model types in the parameter level. The prototyping system starts the searching algorithm of problem statement view of models. Pick up Quasi-Item-Matching model for adaptive testing and retrieve the corresponding input data.

![](/api/attachments/DEGKJ6MK/fulltext/images/e6cc99e756fd577fb0d4371e21faa27c59a48ed0a8293f1fe4f9fedfc8682894.jpg)  
Ability  
Fig. 6. Result of five adaptive test.

Model formulation subsystem:

<sup>Ø</sup> Model instance formulation. The prototyping system executes the model formulation module of problem statement view of models. Formulate this model instance from input data and predefined mathematical structure of this model.

Solver subsystem:

<sup>Ø</sup> Choice for solution algorithms. The prototyping system searches the knowledge base based on the previous premises to suggest a decision. Pick up a specialized network algorithm since this model has a special network structure. The specialized network algorithm is implemented by Pascal code. Measuring results:

<sup>Ø</sup> The results are stored in the model base, and some of the results are shown in Table 2 and graphically presented on the screen as Fig. 6 for user review.

<sup>Ø</sup> To make a comparison, the user can try other categories of solution approaches through ‘‘whatif’’ function. The NPA is selected. The prototyping system then starts the searching algorithm of procedure view of models, but cannot find any suitable model to solve this problem.

At this point, the user is willing to stop the modeling process since the five generated adaptive tests, in general, are closely matched to the five predetermined TIFs at the three specified ability levels.

In sum, the above processes are just two sample illustrations of the prototype for solving two frequently arising problems. However, as a whole, the illustrations indicate that the user can interactively operate the modeling process in a flexible and userfriendly way to construct tests without any expertise and the results are also satisfactory.

## 5. Conclusion

The goal of this study is to develop a MMS architecture for TCDSS to support test specialists in manipulating the complex IRT-based test construction process. In particular, increased use of end-user computing has resulted in test specialists wanting to address test construction themselves rather than employing technical experts as intermediaries. The MMS framework comprises four subsystems: problem analysis, model type selection, model formulation and solver. The model type selection subsystem is further organized into three levels of hierarchy, i.e., environment, structure and parameter, and implemented based on the concept of relational data base. Then, a prototype is presented for demonstrating the feasibility of automating the modeling process.

The results indicate that the MMS architecture provides users with an integrated, flexible and userfriendly TCDSS environment in operating the modeling process without any expertise. In particular, the ‘‘what-if’’ function presents a significant impact on test construction for refining the choices and repeating the process until more satisfactory results are obtained. By contrast, the existing approaches may assume that a familiar and fixed method is predetermined for solving all the similar problems. However, a good practice should have different decision processes for test construction problems in order to obtain more satisfactory results in less solution time. Although subjective factors can influence the modeling process, the impact of such subjective factors are reduced as the process moves down the hierarchy of the MMS architecture. In fact, it may be desirable to have more subjective factors if the user does not compromise the results seriously, since these factors with the aid of ‘‘what-if’’ function can enhance the user’s confidence in the results.

To build a real and complete system, follow-up researches are necessary to be conducted. For the model type selection process, the development of more exhaustive model classification knowledge base for each view of models plays an important role on differentiating between the large and growing number of models in an effective and efficient way. For those problems classified as the data view of models, they are lack of any initial knowledge about the LP structure. Therefore, it is necessary for those problems to develop more intelligent formulation classification knowledge base in aiding the model formulation process.

## Acknowledgements

The author gratefully acknowledges the support of the National Science Council of Taiwan under contract NSC 88-2413-H-224-001. The author would also like to thank the anonymous referees for their valued comments.

## References

<sup>w</sup> <sup>x</sup> 1 T.A. Ackerman, An alternative methodology for creating parallel test forms using the IRT information function, Paper presented at the Annual Meeting of the National Council on Measurement in Education, San Francisco, CA, March, 1989.

<sup>w</sup> <sup>x</sup> 2 J.J. Adema, A note on solving large-scale zero–one programming problems Research Report 88-4 , University of Twente,Ž . Enschede, The Netherlands, 1988.

<sup>w</sup> <sup>x</sup> 3 J.J. Adema, The construction of customized two-stage tests, Journal of Educational Measurement 27 1990 241–253.Ž .

<sup>w</sup> <sup>x</sup> 4 J.J. Adema, Methods and models for the construction of weakly parallel tests, Applied Psychological Measurement 16 Ž . 1992 53–63.

<sup>w</sup> <sup>x</sup> 5 J.J. Adema, E. Boekkooi-Timminga, W.J. van der Linden, Achievement test construction using 0–1 linear programming, European Journal of Operational Research 55 1991Ž . 103–111.

<sup>w</sup> <sup>x</sup> 6 R. Armstrong, D. Jones, I.-L. Wu, An automated development of parallel tests from a seed test, Psychometrika 57 Ž .1992 271–288.

<sup>w</sup> <sup>x</sup> 7 F.B. Baker, A.S. Cohen, B.R. Barmish, Item characteristics of tests constructed by linear programming, Applied Psychological Measurement 12 1988 189–199.Ž .

<sup>w</sup> <sup>x</sup> 8 S. Banerjee, A. Basu, Model type selection in an integrated DSS environment, Decision Support Systems 9 1993 75–89.Ž .

<sup>w</sup> <sup>x</sup>9 A. Birnbaum, Some latent trait models, in: F.M. Lord, M.R. Novick Eds. , Statistical Theories of Mental Test Scores,Ž . Addison-Wesley, Reading, MA, 1968.

<sup>w</sup> <sup>x</sup> 10 R.W. Blanning, Conversing with management information systems in natural language, Communications of the ACM 27 3 1984 201–207.Ž . Ž .

<sup>w</sup> <sup>x</sup> 11 R.W. Blanning, A relational framework for joint implementation in model management system, Decision Support Systems 1 1 1985 69–81.Ž . Ž .

<sup>w</sup> <sup>x</sup> 12 R.W. Blanning, An entity-relationship approach to model management, Decision Support Systems 2 1986 65–72. Ž .

<sup>w</sup> <sup>x</sup> 13 E. Boekkooi-Timminga, Simultaneous test construction by zero–one programming, Methodika 1 1987 101–112.Ž .

<sup>w</sup> <sup>x</sup> 14 E. Boekkooi-Timminga, The construction of parallel tests from IRT-based item banks, Journal of Educational Statistics 15 1990 129–145.Ž .

<sup>w</sup> <sup>x</sup> 15 E. Boekkooi-Timminga, A cluster-based method for test construction, Applied Psychological Measurement 14 1990Ž . 341–354.

<sup>w</sup> <sup>x</sup> 16 A.-M. Chang, C.W. Holsapple, A.B. Whinston, Model management issues and directions, Decision Support Systems 9 Ž .1993 19–37.

<sup>w</sup> <sup>x</sup>17 H.J. Greenberg, A functional description of ANALYZE: a computer-assisted analysis system for linear programming models, ACM Transactions on Mathematical Software 9 1Ž . Ž .1983 18–56.

<sup>w</sup> <sup>x</sup> 18 R.K. Hambleton, H. Swaminathan, Item Response Theory: Principles and Applications, Kluwer-Nijhoff, Boston, 1985.

<sup>w</sup> <sup>x</sup> 19 M. Kendall, A. Stuart, The Advanced Theory of Statistics, Vol. 2, Griffin, London, 1979.

<sup>w</sup> <sup>x</sup> 20 T.-P. Liang, Development of a knowledge-based model management system, Operations Research 36 6 1988 849–863.Ž . Ž .

<sup>w</sup> <sup>x</sup> 21 F.M. Lord, Practical application of items characteristics curve theory, Journal of Educational Measurement 14 1977 117–Ž . 138.

<sup>w</sup> <sup>x</sup> 22 F.M. Lord, Applications of Item Response Theory to Practical Testing Problems, Lawrence Erlbaum, Hillsdale, NJ, 1980.

<sup>w</sup> <sup>x</sup> 23 R.M. Luecht, T.M. Hirsch, Item selection using an average growth approximation of target information functions, Applied Psychological Measurement 16 1992 41–51.Ž .

<sup>w</sup> <sup>x</sup> 24 F. Murphy, E.A. Stohr, An intelligent system for formulating linear programs, Decision Support Systems 2 1 1986 Ž . Ž . 39–47.

<sup>w</sup> <sup>x</sup> 25 G.L. Nemhauser, L.A. Wolsey, Integer and Combinatorial Optimization, Wiley, New York, NY, 1988.

<sup>w</sup> <sup>x</sup> 26 M. O’hEigeartaigh, J.K. Lenstra, A.H.G. Rinnooy Kan, Combinatorial Optimization: Annotated Bibliographies, Wiley, New York, 1985.

<sup>w</sup> <sup>x</sup> 27 F. Samejima, Weakly parallel tests in latent trait theory with some criticisms of classical test theory, Psychometrika 50 Ž . 1977 411–420.

<sup>w</sup> <sup>x</sup> 28 H.A. Simon, The structure of ill structured problems, Artificial Intelligence 4 1973 181–201. Ž .

<sup>w</sup> <sup>x</sup> 29 G.F. Smith, Defining managerial problems: a framework for perspective theorizing, Management Science 35 8 1989Ž . Ž . 963–981.

<sup>w</sup> <sup>x</sup> 30 R.H. Sprague, E.D. Carlson, Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs, NJ, 1982.

<sup>w</sup> <sup>x</sup> 31 M. Stocking, L. Swanson, A method for severely constrained item selection in adaptive testing, Applied Psychological Measurement 17 1993 277–292.Ž .

<sup>w</sup> <sup>x</sup> 32 E.A. Stohr, A mathematical programming generator system in APL, Working Paper 96, Center for Research Information Systems, Graduate School of Business Administration, New York University, New York, 1985.

<sup>w</sup> <sup>x</sup> 33 L. Swanson, M. Stocking, A model and heuristics for solving very large item selection problems, Applied Psychological Measurement 17 1993 151–166.Ž .

<sup>w</sup> <sup>x</sup> 34 T.J.J.M. Theunissen, Binary programming and test design, Psychometrika 50 1985 411–420.Ž .

<sup>w</sup> <sup>x</sup> 35 T.J.J.M. Theunissen, Some applications of optimization algorithms in test design and adaptive testing, Applied Psychological Measurement 10 1986 381–389.Ž .

<sup>w</sup> <sup>x</sup>36 W.J. van der Linden, E. Boekkooi-Timminga, A maximin model for test design with practical constraints, Psychometrika 12 1989 237–247.Ž .

<sup>w</sup> <sup>x</sup> 37 R.N. Woolley, M. Pidd, Problem structuring: a literature review, Journal of Operational Research Society 32 1981 Ž . 197–213.

<sup>w</sup> <sup>x</sup> 38 I.-L. Wu, A new method for simultaneous test construction of two-stage and multistage testing, submitted to Journal of Educational and Behavioral Statistics for second round review.

![](/api/attachments/DEGKJ6MK/fulltext/images/8efcea99c2b534dfc26f56d02230cad3121081556ca14d2d5cccbbbf4985664a.jpg)

Ing-Long Wu is an Associate Professor in the Department of MIS at National Yunlin University of Science and Technology. He gained a Bachelor in Industrial Management Science from National Cheng-Kung University, a MS in Computer Science from Montclair State University, and a PhD in Management from Rutgers, the State University of New Jersey. He has published a number of papers in Psychometrika, Applied Psychological Measurement, Journal of

Educational and Behavioral Statistics, Journal of the Chinese Institute of Industrial Engineers, and Journal of the Chinese Management Science. His current research interests are in the area of Decision Support Systems, System Development Methodology, Strategic Information Systems, and Business Process Reengineering.

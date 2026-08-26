---
otero_id: 1964
otero_key: "9A5UU395"
title: "An evolution strategy-based multiple kernels multi-criteria programming approach: The case of credit decision making"
authors: "Jianping Li; Liwei Wei; Gang Li; Weixuan Xu"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.11.022"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An evolution strategy-based multiple kernels multi-criteria programming approach: The case of credit decision making

Jianping Li <sup>a,</sup>⁎, Liwei Wei <sup>c,a</sup>, Gang Li <sup>a,b</sup>, Weixuan Xu <sup>a</sup>

<sup>a</sup> Institute of Policy and Management, Chinese Academy of Sciences, Beijing 100190, P.R. China

<sup>b</sup> Graduate University of Chinese Academy of Sciences, Beijing 100039, P.R. China

<sup>c</sup> National Library of Standards, China National Institute of Standardization, Beijing 100088, P.R. China

## a r t i c l e i n f o

Available online 25 November 2010

Keywords: Multi-criteria programming Multiple kernels Evolution strategies Credit risk Decision making

## a b s t r a c t

Credit risk analysis has long attracted a great deal of attention from both academic researchers and practitioners. However, because of the recent <sup>fi</sup>nancial crisis, this <sup>fi</sup>eld continues to draw ever increasingly attention. A multiple kernels multi-criteria programming approach based on evolution strategy (ES-MK-MCP) is proposed for credit decision making in this study. We introduce a linear combination of kernel functions to enhance the interpretability of credit classi<sup>fi</sup>cation models, and propose an alternative to optimize the parameters based on the evolution strategy. For illustration purpose, two UCI credit card data sets are used to verify the effectiveness and feasibility of the proposed model. As the experimental results reveal, the proposed ES-MK-MCP model is an ef<sup>fi</sup>cient tool for credit risk analysis, especially for decision makers to identify the most relevant features.

© 2010 Elsevier B.V. All rights reserved

## 1. Introduction

The subprime mortgage crisis in the United States, the credit crisis that followed, and the still lingering apprehensions about the future of economies across the whole world are factors that have resulted in credit risk attracting increasing concern in both industry and academia. Numerous methodologies have been introduced into this <sup>fi</sup>eld, considering the challenge and importance of credit risk analysis and evaluation, and risk management. Statistical and neural network based approaches are among the most popular paradigms [1,2,13,40].

As a promising credit decision making approach, many mathematical programming methods have been proposed in extant literature to address credit risk classi<sup>fi</sup>cation problem in the last few decades. Support vector machines (SVMs), an analytical tool developed from programming techniques and <sup>fl</sup>ourishing recently, have successfully been applied in this <sup>fi</sup>eld in recent years [8,15]. SVMs were <sup>fi</sup>rst proposed by Vapnik [36]. The basic idea of the SVM is to separate data with a maximal margin classi<sup>fi</sup>er, which can be solved via constrained quadratic programming. Recently, multiple criteria programming techniques, as a group of data mining techniques [26], have attracted much interest due to their vigorous development. Multiple criteria programming methods can be divided into two broad categories:

multiple criteria linear programming (MCLP) and multiple criteria quadratic programming (MCQP). Shi et al. [33] developed the multiple criteria linear programming model for credit card portfolio management. Kou et al. [12] modi<sup>fi</sup>ed the multiple criteria linear programming model for behavior analysis of credit cardholders. On the basis of multiple criteria linear programming, Shi et al. [32] proposed multiple criteria quadratic programming (MCQP) to classify credit card accounts from a nonlinear perspective, because both the objective functions and the constraints in credit card accounts classi<sup>fi</sup>cation may be nonlinear. Peng et al. [27] modi<sup>fi</sup>ed the multiple criteria convex quadratic programming (MCQP) model for credit classi<sup>fi</sup>cation and tried to address the speed and scalability of programming methods. Other multiple criteria programming methods and their applications included in literature are [11,23,34,39,41], etc.

However, these multiple criteria programming models also face many challenges, similar to SVMs. The data structures in real life are complicated; most original data sets are not linearly separated. Therefore, the problem of data not linearly separated needs to be solved. A good choice is to map the input space into a higher dimensional feature space for making data linearly separable. Specially, with the increasing attention being put on learning kernel functions from data structures, kernel functions are introduced for improving classi<sup>fi</sup>cation accuracy of nonlinear data. For example, kernel functions were introduced to solve nonlinear problems with multiple criteria programming methods in Peng et al. [27].

Furthermore, the opacity of these models prevents them from being applied in many real-life applications such as credit decision making and medical diagnosis, because both accuracy and comprehensibility are required. Rule extraction and kernel techniques, which are developing rapidly, have been introduced to enhance the interpretability for SVMs [14,19,38]. Specially, feature selection, a process to identify the powerful predictive subset of the features set, has a great effect on computational performance of the models. There are two categories of methods for feature selection: the preprocessing methods and the wrapper methods. The former is independent of accuracy as preprocessing does not take the performance of the models into account, and the latter is just the opposite. The commonly used methods for feature selection are preprocessing methods like PCA and rough set. The wrapper methods, such as genetic algorithm and immune algorithm, combine feature selection with the search process for classi<sup>fi</sup>ers, relating to the performance of the classi<sup>fi</sup>ers. Thus, comprehensible multiple criteria programming, based on the wrapper methods, is proposed for credit classi<sup>fi</sup>cation in our study, given that the optimal kernel is always obtained as a convex combination of <sup>fi</sup>nitely many basic kernels [21]. It is a two-stage iterated method for feature selection and just requires solving a linear equation and a quadratic programming, namely, multiple kernels multi-criteria programming method.

In addition, parameters optimization needs to be considered in most of these methods. Grid search is the conventional but exhaustive search method, which examines the search space entirely. Furthermore, for many programming methods, computation time increases as the size of training data increases and performance is, therefore, degraded. Moreover, the wrapper method incorporated in our proposed model is expensive in terms of computation time; thus some new methods, such as the evolutionary algorithms (EAs), should be introduced to lower computational complexity. EAs have received much attention in recent years. Inspired by the neo-Darwinian paradigm of natural evolution, EAs are a very rich class of multiagent stochastic search algorithms [5]. There are three main streams, $\mathrm { i . e . , }$ evolution strategy (ES), evolutionary programming (EP), and genetic algorithm (GA). These techniques are all probabilistic optimization algorithms, which start with searching a population of feasible solutions generated stochastically and then incorporate stochastic variations into the parameters of the population to evolve the solution to a global optimum. Since they are general and powerful for search, optimization and learning, EAs have been widely employed in a broad range of problems [6,17,25,37]. In some works [25,37], researchers have proven that EAs are suitable for hyper-parameters and features selection for kernel-based learning algorithms. Moreover, it has been shown that ES, as one branch of EAs, needs no coding and encoding processes and has good computing ef<sup>fi</sup>ciency [4,24] to reduce the computation time. Specially, it has self-adaptation search capacity which helps it guide the process quickly and nicely to optimal points; that is, ES is suitable to <sup>fi</sup>nd the optimal hyper-parameters [18,20]. Thus, we introduce ES for parameters optimization and lowering the computation complexity in our study.

The remainder of this paper is organized as follows. Section $^ 2$ elaborates the multiple kernels multi-criteria programming model. Section 3 then introduces the proposed ES-based multi-criteria programming approach for credit classi<sup>fi</sup>cation. Experimental results of credit risk analysis of two UCI credit card data sets are presented in Section 4. Finally, conclusions are drawn in Section 5, with recommendations for future research areas.

## 2. Multiple kernels multi-criteria programming model

## 2.1. Multi-criteria programming model

The basic multi-criteria programming model was proposed by Peng et al. [27]. It is introduced as follows.

Consider a standard binary credit classi<sup>fi</sup>cation problem. Given a set of data points $G = \{ \left( \vec { A } _ { i } , \vec { y } _ { i } \right) \} _ { i = 1 } ^ { n }$ , where $\stackrel {  } { A } _ { i } \in R ^ { m }$ is the $i ^ { \mathrm { { t h } } }$ input sample, and $y _ { i } \in \{ 1 , - 1 \}$ is the corresponding observed result. Let

$A = \left( \vec { A } _ { 1 } , \vec { A } _ { 2 } , \cdots , \vec { A } _ { n } \right) ^ { T }$ , and de<sup>fi</sup>ne two groups: the group of good credit cases denoted by $G _ { 1 }$ and the group of bad credit cases denoted by $G _ { - 1 } .$ The aim of this model is to <sup>fi</sup>nd the optimal separating coef<sup>fi</sup>cients denoted as $\vec { X } = ( x _ { 1 } , x _ { 2 } , \cdots , x _ { m } ) ^ { T }$ , and a boundary value b to separate the cases into two classes, $G _ { 1 }$ and $G _ { - 1 }$ . Considering all samples are linearly separable, that is:

$$
\vec {A} _ {i} ^ {T} \vec {X} \geq b, \forall \vec {A} _ {i} \in G _ {1} \text { and } \vec {A} _ {i} ^ {T} \vec {X} <   b, \forall \vec {A} _ {i} \in G _ {- 1}.
$$

De<sup>fi</sup>ne that $\alpha _ { \mathrm { i } }$ is the distance from $\vec { A } _ { i }$ to hyper plane $b ,$ where $\alpha _ { i } \ge 0 ,$ if sample i is correctly classi<sup>fi</sup>ed; $\beta _ { \mathrm { i } }$ is the distance from $\vec { A } _ { i }$ to hyper plane $b ,$ where $\beta _ { i } \ge 0 ,$ , if sample i is improperly classi<sup>fi</sup>ed. Introduce a parameter δ to get the equation constraints of this model:

$$
\begin{array}{l} \vec {A} _ {i} ^ {T} \vec {X} = b + \delta + \alpha_ {i} - \beta_ {i}, \forall \vec {A} _ {i} \in G _ {1}, \\ \vec {A} _ {i} ^ {T} \vec {X} = b - \delta - \alpha_ {i} + \beta_ {i}, \forall A _ {i} \in G _ {- 1}, \end{array}
$$

where $\underline { { \boldsymbol { \cdot } } } \underline { { \boldsymbol { \delta } } }$ is scalar, $b - \delta$ and $b + \delta$ are two adjustable hyper planes.

Let $\vec { X } / \delta$ be replaced with X, b/δ with $b , \alpha _ { i } / \delta$ with α and $\beta _ { i } / \delta$ with $. \beta _ { i } .$ De<sup>fi</sup>ne Y as a diagonal matrix where the label $y _ { i }$ is along its diagonal. Then, the constraints of this model can be transformed into the following equation:

$$
Y \left(A ^ {T} \vec {X} - b \vec {e}\right) = \vec {e} + \vec {\alpha} - \vec {\beta},
$$

where, $\vec { e } = ( 1 , 1 , \cdots , 1 ) ^ { T } , \vec { \alpha } = ( \alpha _ { 1 } , \alpha _ { 2 } , \cdots , \alpha _ { n } ) ^ { T } \mathrm { a n d } \vec { \beta } = ( \beta _ { 1 } , \beta _ { 2 } , \cdots , \beta _ { n } ) ^ { T } .$

<sup>ð Þ ð Þ ð Þ</sup>To separate the two prede<sup>fi</sup>ned groups as accurately as possible, three optimization problems need to be solved: maximize the distance between hyper planes $b - \delta$ and $b + \delta ;$ minimize the distance between misclassi<sup>fi</sup>ed samples and separation hyper plane $b ;$ and maximize the distance of properly classi<sup>fi</sup>ed samples and separation hyper plane b. Thus, the model is integrated as follows:

$$
\begin{array}{l} \min \frac {1}{2} | | \vec {X} | | _ {s} ^ {s} + w _ {\alpha} | | \vec {\alpha} | | _ {p} ^ {p} - w _ {\beta} | | \vec {\beta} | | _ {q} ^ {q}, \\ s. t. Y \Big (A ^ {T} \vec {X} - b \vec {e} \Big) = \vec {e} + \vec {\alpha} - \vec {\beta}. \end{array}\tag{1}
$$

Considering the situation tha $s = 2 , p = 2$ and $q = 1$ , model (1) can be changed to:

$$
\begin{array}{l} \min \frac {1}{2} | | \vec {X} | | _ {2} ^ {2} + w _ {\alpha} \sum_ {i = 1} ^ {n} \alpha_ {i} ^ {2} - w _ {\beta} \sum_ {i = 1} ^ {n} \beta_ {i}, \\ s. t. Y \Big (A ^ {T} \vec {X} - b \vec {e} \Big) = \vec {e} + \vec {\alpha} - \vec {\beta}. \end{array}\tag{2}
$$

De<sup>fi</sup>ne $\eta _ { i } = \alpha _ { i } - \beta _ { i }$ and notice that when sample i is misclassi<sup>fi</sup>ed, we get $\eta _ { i } = - \beta _ { i } ;$ otherwise, $\eta _ { i } = \alpha _ { i }$ . Therefore, we can replace $\alpha _ { i }$ and $\beta _ { i }$ with $\eta _ { i }$ and $- \eta _ { i }$ in model (2); moreover, to easily solve the optimization problem, we change model (2) into model (3) as follows:

$$
\begin{array}{l} \min \frac {1}{2} | | X | | _ {2} ^ {2} + \frac {w _ {\alpha}}{2} \sum_ {i = 1} ^ {n} \eta_ {i} ^ {2} + w _ {\beta} \sum_ {i = 1} ^ {n} \eta_ {i} + \frac {w _ {b}}{2} b ^ {2}, \\ s. t. Y \left(A ^ {T} \vec {X} - b \vec {e}\right) = \vec {e} + \vec {\eta}. \end{array}\tag{3}
$$

The above quadratic optimization problem can be solved by the Lagrange function:

$$
L (\vec {X}, b, \vec {\eta}, \vec {\theta}) = J (\vec {X}, b, \vec {\eta}) - \vec {\theta} ^ {T} (Y (A ^ {T} \vec {X} - b \vec {e}) - \vec {e} - \vec {\eta}),
$$

where $\vec { \theta }$ denotes Lagrange multipliers, hence $\theta _ { i } \ge 0 .$

At the optimal point, constraints in model (3) can be rewritten as the following equation:

$$
Y <   A, A > Y \vec {\theta} + \frac {1}{w _ {b}} Y \vec {e} \vec {e} ^ {T} Y \vec {\theta} + \frac {1}{w _ {a}} (\vec {\theta} - w _ {\beta} \vec {e}) - \vec {e} = 0.\tag{4}
$$

Thus, model (3) can be easily solved by the equation below:

$$
\vec {\theta} = \left(\frac {1}{w _ {\alpha}} I + Y \left(<   A, A > + \frac {1}{w _ {b}} \vec {e} \vec {e} ^ {T}\right) Y\right) ^ {- 1} \left(1 + \frac {w _ {\beta}}{w _ {\alpha}}\right) \vec {e}.\tag{5}
$$

The corresponding optimal decision function is

$$
f \left(\vec {A} _ {i}\right) = \operatorname{sgn} \left(\vec {A} _ {i} ^ {T} \vec {X} ^ {*} - b ^ {*}\right).\tag{6}
$$

where ${ \vec { X } } ^ { * } = A Y { \vec { \theta } } ^ { * }$ and $\begin{array} { r } { b ^ { * } = - { \frac { 1 } { w _ { b } } } { \vec { e } } ^ { T } Y { \vec { \theta } } ^ { * } } \end{array}$

## 2.2. Feature selection and kernel functions

In recent years, kernel methods have become very popular for learning from data [22], and a number of powerful kernel-based machine learning methods have been proposed [3,29,30].

The main idea of kernel methods is to map original data into a potentially much higher dimensional feature space via a nonlinear mapping:

$$
\begin{array}{c} \Phi : \mathrm{R} ^ {N} \to \mathrm{F} \\ X \to \Phi (X). \end{array}
$$

The data $X = ( x _ { 1 } , x _ { 2 } , . . . , x _ { 2 } )$ in original feature space $\mathsf { R } ^ { N }$ may be linearly inseparable and, therefore, nonlinear mapping makes it linearly separable in a higher dimensional feature space F.

Commonly used kernel functions include linear, polynomial, radial basis function (RBF) and sigmoid kernel, which are:

$$
\begin{array}{l} \text { linear } \quad K (\vec {x}, \vec {y}) = \vec {x} ^ {T} \cdot \vec {y}, \\ \text { polynomial } \quad K (\vec {x}, \vec {y}) = (\vec {x} \cdot \vec {y} + c) ^ {d}, \quad \text { for } d \in N, c \geq 0, \\ \text { radial   basis   function   (RBF) } \quad K (\vec {x}, \vec {y}) = \exp (- \gamma | | \vec {x} - \vec {y} | | ^ {2}), \text { for } \gamma > 0, \\ \text { sigmoid } \quad K (\vec {x}, \vec {y}) = \tanh (\gamma (\vec {x} \cdot \vec {y}) + c), \text { for } \gamma > 0, c \geq 0. \end{array}
$$

We employ radial basis function to make the optimization problem simple in our study. Moreover, the linear kernel is a special case of RBF and the sigmoid kernel behaves like RBF for certain parameters in previous studies [10,16].

Introducing the radial basis function into Eq. (4), we get that:

$$
Y K (A, A) Y \vec {\theta} + \frac {1}{w _ {b}} Y \vec {e} \vec {e} ^ {T} Y \vec {\theta} + \frac {1}{w _ {a}} \left(\vec {\theta} - w _ {\beta} \vec {e}\right) - \vec {e} = 0.\tag{7}
$$

Then,

$$
\vec {\theta} = \left(\frac {1}{w _ {\alpha}} I + Y \left(K (A, A) + \frac {1}{w _ {b}} \vec {e} \vec {e} ^ {T}\right) Y\right) ^ {- 1} \left(1 + \frac {w _ {\beta}}{w _ {\alpha}}\right) \vec {e}.\tag{8}
$$

However, we face the problem that it is still dif<sup>fi</sup>cult to make the model more comprehensible. To tackle this problem, we adopt the conclusion that the optimal kernel is obtained as a convex combination of <sup>fi</sup>nitely many basic kernels, i.e., m+2 basic kernels, where m is the number of data samples [21]. Thus, a linear combination of radial basis functions with kernel coef<sup>fi</sup>cients is proposed in our study to solve the explanatory problem as follows:

$$
K \left(\vec {A} _ {i}, \vec {A} _ {j}\right) = \sum_ {d = 1} ^ {m} \gamma_ {d} k \left(A _ {i, d}, A _ {j, d}\right), \gamma_ {d} \geq 0,\tag{9}
$$

where $A _ { i , d }$ denotes the $d ^ { \mathrm { t h } }$ component of input vector $\stackrel {  } { A } _ { i }$

When kernel coef<sup>fi</sup>cients are not equal to zero, it shows that these features play important roles in credit classi<sup>fi</sup>cation; otherwise, it illustrates that these features do not work, and can be removed. Thus, the issue of feature selection is transformed into an ordinary parameters optimization problem.

Introducing Eq. (9) into (8), we can obtain:

$$
\vec {\theta} = \left(\frac {1}{w _ {\alpha}} I + Y \left(\left(\sum_ {d = 1} ^ {m} \gamma_ {d} k (A _ {i, d}, A _ {j, d})\right) _ {n \times n} + \frac {1}{w _ {b}} \vec {e} \vec {e} ^ {T}\right) Y\right) ^ {- 1} \left(1 + \frac {w _ {\beta}}{w _ {\alpha}}\right) \vec {e}.\tag{10}
$$

However, there are two parameters that need to be optimized in this model: the Lagrange coef<sup>fi</sup>cients $\theta _ { i }$ and the feature coef<sup>fi</sup>cient $\gamma _ { d } .$ We employ a two-stage iterative learning process to solve this problem, similar to the sparse kernel and Bayesian method [9]. Fixing the feature coef<sup>fi</sup>cient $\gamma _ { d } ,$ the Lagrange coef<sup>fi</sup>cient $\theta _ { i }$ can be obtained by Eq. (10); <sup>fi</sup>xing the Lagrange coef<sup>fi</sup>cient $\theta _ { i } ,$ the feature coef<sup>fi</sup>cient γ can be computed by minimizing the following score function:

$$
\min J (\vec {\gamma}, \vec {\eta}) = \sum_ {i = 1} ^ {n} \eta_ {i} ^ {2} + \lambda | | \vec {\gamma} | | _ {1}, \lambda > 0, \gamma_ {d} \geq 0\tag{11}
$$

The <sup>fi</sup>rst term in Eq. (11) presents the square error loss, which has two functions: controlling empirical risk and the smoothness. The regularized parameter λ in the second term determines the tradeoff between square error loss and feature coef<sup>fi</sup>cients. Considering the sparseness of the feature set, we adopt 1-norm in this score function.

Replacing η<sub>i</sub> in model (11), the following quadratic optimization problem can be obtained:

$$
\begin{array}{l} \min J (\gamma , \eta) = \sum_ {i = 1} ^ {n} \eta_ {i} ^ {2} + \lambda | | \gamma | | _ {1} \\ \qquad = \sum_ {i = 1} ^ {n} \left(1 + y _ {i} b - y _ {i} \sum_ {d = 1} ^ {m} \gamma_ {d} \vec {K} _ {i, d} \cdot \vec {\theta}\right) ^ {2} + \lambda \sum_ {d = 1} ^ {m} \gamma_ {d} \\ \qquad = \sum_ {d _ {1} = 1} ^ {m} \sum_ {d _ {2} = 1} ^ {m} \gamma_ {d _ {1}} \gamma_ {d _ {2}} \left(\sum_ {i = 1} ^ {n} y _ {i} ^ {2} \left(\vec {K} _ {i, d _ {1}} \cdot \vec {\theta}\right) \left(\vec {K} _ {i, d _ {2}} \cdot \vec {\theta}\right)\right) ^ {2} \\ \qquad + \sum_ {d = 1} ^ {m} \gamma_ {d} \left(\lambda - 2 \sum_ {i = 1} ^ {n} (1 + y _ {i} b) y _ {i} \vec {K} _ {i, d} \cdot \vec {\theta}\right) + \sum_ {i = 1} ^ {n} (1 + y _ {i} b) ^ {2}, \end{array}\tag{12}
$$

where $\vec { K } _ { i , d } = [ k ( A _ { i , d } , A _ { 1 , d } ) , \cdots , k ( A _ { i , d } , A _ { n , d } ) ]$

## 2.3. The algorithm

Thus, the procedures of multiple kernels multi-criteria programming model can be summarized as follows:

1) Initializing: set the parameters $w _ { \alpha } , w _ { \beta } , w _ { \ b } , \sigma ^ { 2 }$ and λ according to some criteria; the feature coef<sup>fi</sup>cients $\gamma _ { \mathrm { i } }$ is set to $\{ \gamma _ { d } ^ { ( 0 ) } = 1 \}$ $d = 1 , 2 , \cdots , m \}$

2) Solving the Lagrange coef<sup>fi</sup>cient $\theta _ { d } ^ { ( t ) }$ : solve the equation to get $\theta _ { d } ^ { ( t ) }$ according to (10), where feature coef<sup>fi</sup>cient $\gamma _ { d } ^ { ( t - 1 ) }$ is <sup>fi</sup>xed.

3) Solving the feature coef<sup>fi</sup>cient $\gamma _ { d } ^ { ( t ) } \mathrm { : }$ : solve the quadratic optimization problem (12) to get $\gamma _ { d } ^ { ( t ) }$ based on Lagrange coef<sup>fi</sup>cient $\theta _ { d } ^ { ( t ) }$ solved in step 2).

4) Calculating errors: calculate some prede<sup>fi</sup>ned measures according to coef<sup>fi</sup>cients $\theta _ { d } ^ { ( t ) }$ and $\gamma _ { d } ^ { ( t ) }$ solved in steps 2) and 3). If the measures do not satisfy stop criteria, turn to step 2) to implement this twostage iterated algorithm.

5) Output: calculate $X ^ { * }$ and $b ^ { * }$ to get the classi<sup>fi</sup>ers according to (6). This algorithm is illustrated in Fig. 1.

## 3. Evolution strategy for parameters optimization of MK-MCP

## 3.1. Evolution strategy

There are several parameters that need to be optimized in the MK-MCK model shown above. We adopt the evolution strategy for parameters optimization.

Evolution strategy was proposed by students at the Technical University of Berlin [28,31]; it is an optimization technique based on ideas of adaptation and evolution. There are three basic operations in ES: mutation, recombination and selection. As is common with EAs, these operators are applied in a loop. An iteration of the loop is called a generation. The basic evolution cycle is depicted in Fig. 2. The sequence of generations is continued until a termination criterion is met.

1) Mutation. In this step, making perturbations is the key of the mechanism of ES, where random numbers following a distribution are added to its variable vector (chromosome). Let $( p _ { 1 } , . . . , p _ { n } )$ be the chromosome involving n variables, and random numbers follow a Gaussian distribution. Then a mutation operator is de<sup>fi</sup>ned by formulation:

$$
p _ {t} ^ {g + 1} = p _ {t} ^ {g} + N \left(0, \varepsilon_ {t} ^ {g + 1}\right),
$$

where strategy parameters $\varepsilon _ { t }$ are actually step sizes or mutation strengths of mutations and g is the number of generations. The ε is also governed by self-adaptation in their own way:

$$
\varepsilon_ {t} ^ {g + 1} = \varepsilon_ {t} ^ {g} e x p (\tau , N (0, 1)),
$$

where τ is the learning rate controlling the self-adaptation speed of $\varepsilon _ { t } .$

2) Recombination. Mutation is based on the information of only one parent, while recombination shares several parents’ information. It reproduces one offspring from ρ parents in this step. There are two versions of recombination technique: discrete recombination and intermediate recombination. The discrete recombination selects every component randomly for the offspring from relevant components of $\rho$ parent individuals. In contrast, the intermediate recombination allows an equal right to all ρ parents for reproduction. The offspring takes the average of $\rho$ parent vectors as its value.

![](/api/attachments/9A5UU395/fulltext/images/1fb73e6bcd2bae3697c57e2fcfb6f34f68db9022ebe85f8e92e6178264bd6ba1.jpg)  
Fig. 1. Flow diagram of MK-MCP

![](/api/attachments/9A5UU395/fulltext/images/c1504a779c2d076c32bbb3c8587a058a738f528cc86802dd7e0219b70ce5d378.jpg)  
Fig. 2. ES basic evolution cycle

3) Selection. In this step, the selection operation directs the search to the promising range of the object parameters space and gives a result of optimization. There are two versions of selection technique, i.e., comma selection, denoted by (μ, θ), and plus selection, denoted by $( \mu + \theta )$ . For (μ, θ) selection, only θ offspring individuals can be selected, while parent individuals are not in the selected set. This selection technique will forget the information of parent generation to avoid pre-converging on local optimal points. However, the plus selection (μ+θ) gives a choice from the selection set, which consists of parents and offsprings, which can help select and preserve the best individuals.

In addition, the <sup>fi</sup>tness function is a criterion for evaluating search results and is also very important to the ES. Only if the mutant's <sup>fi</sup>tness is at least as good as the parent does it become the parent of the next generation. In other words, the chromosome with high <sup>fi</sup>tness value has high probability to be preserved to the next generation.

## 3.2. ES-based multiple kernels multi-criteria programming model

The ES-based multiple kernels multi-criteria programming algorithm is shown as follows, where $\left( \mu , \theta \right)$ criteria is used for selection, and the test's overall hit rate is used as the <sup>fi</sup>tness.

Input: input data vector $\dot { A _ { i } } \mathrm { { \in } } R ^ { m }$ , observed result $y _ { i } \in \{ + 1 , - 1 \}$ , and form the matrix A and Y.

## Stage 1 Initialization.

Set the number of iterations, g, the number of parents for reproduction, $\rho ,$ the size of parent pool, μ, and the number of offsprings selected, θ. Initialize parameters $\delta _ { t } ^ { ( g ) } =$ $\{ \Bigl ( \vec { p } _ { m } ^ { ( 0 ) } , \varepsilon _ { m } ^ { ( 0 ) } , F \Bigl ( \vec { p } _ { m } ^ { ( 0 ) } \Bigr ) \Bigr ) , m = 1 , . . . , \theta \}$ , where $\vec { p } _ { m } ^ { ( 0 ) }$ is a vector that consists of <sup>fi</sup>ve parameters: the <sup>fi</sup>rst three are the regularization parameters in model $( 3 ) , \ p _ { m } ^ { ( 0 ) } ( 1 ) = w _ { \alpha } , \ p _ { m } ^ { ( 0 ) }$ $( 2 ) = w _ { \beta }$ , and $p _ { m } ^ { ( 0 ) } ( 3 ) = w _ { b } ;$ the fourth is the regularization parameter in model $( 1 2 ) , p _ { m } ^ { ( 0 ) } ( 4 ) = \lambda ;$ and the last one is the kernel parameter $p _ { m } ^ { ( 0 ) } ( 5 ) = \sigma ^ { 2 } .$ Set the strategy parameter $\varepsilon _ { t } ^ { ( 0 ) }$ , the self-adaptation learning rate τ, and the <sup>fi</sup>tness $F ( p _ { m } ^ { ( 0 ) } )$ tage 2 Repeat.

For l=1 to θ

(1) The marriage selection process is independent of parental objective values F. A parent family ς of size $\rho$ is randomly chosen from the parent pool of size $\mu , \varsigma _ { l } = \mathrm { m a r r i a g e } ( \delta _ { t } ^ { ( g ) } , \rho )$

(2) Parameter recombination. The endogenous strategy parameters and object parameters are recombined by calculating $\varepsilon _ { l } =$ εrecombination(ς ) and $p _ { l } = p { \mathrm { r e c o m b i n a t i o n } } ( \varsigma _ { l } )$ respectively.

(3) Parameter mutation. Mutations of strategy parameters and object parameters are obtained by solving $\tilde { \varepsilon } _ { l } = \mathrm { \varepsilon { m u t a t i o n } } ( \mathfrak { s } _ { l } )$ and $\tilde { p } _ { l } = p \mathrm { m u t a t i o n } ( p _ { l } , \tilde { \varepsilon } _ { l } )$ , respectively.

(4) Calculating <sup>fi</sup>tness $\tilde { F } _ { l } = F ( \tilde { p } _ { l } )$ .

Step 1 set the feature coef<sup>fi</sup>cients γ to $\{ \gamma _ { d } ^ { ( 0 ) } = 1 | d = 1 , 2 , \cdots , m \} ;$

Step 2 solve the equation to get Lagrange coef<sup>fi</sup>cients $\theta _ { d } ^ { ( t ) }$ according to (10) where feature coef<sup>fi</sup>cient $\gamma _ { d } ^ { ( t - 1 ) }$ is used;

Step 3 solve the quadratic optimization problem (12) to get feature coef<sup>fi</sup>cien $\gamma _ { d } ^ { ( t ) }$ based on Lagrange coef<sup>fi</sup>cient $\cdot \theta _ { d } ^ { ( t ) }$ <sup>)</sup> solved in step 2;

Step 4 Calculating errors: calculating some prede<sup>fi</sup>ned measures according to coef<sup>fi</sup>cients $\theta _ { d } ^ { ( t ) }$ and $\gamma _ { d } ^ { ( t ) }$ solved in steps 2 and 3, respectively. If the measures do not satisfy stop criteria, turn to step 2 to implement this two-stage iterated algorithm;

Step 5 calculate $X ^ { * }$ and $b ^ { * }$ to get the classi<sup>fi</sup>ers according to (6), then the output and the <sup>fi</sup>tness of the ES is obtained.

(5) End.

Stage 3 Complete offspring population. Then, this will generate a complete offspring population $\delta _ { o } ^ { ( g ) }$ as follows:

$$
\delta_ {o} ^ {(g)} = \left\{\left(p _ {l} ^ {(g)}, \varepsilon_ {l} ^ {(g)}, F \left(p _ {l} ^ {(g)}\right)\right), l = 1, \dots , \theta \right\}.
$$

Stage 4 Selection. After having a complete offspring population $\delta _ { o } ^ { ( g ) }$ selection is performed, with the result of a new parent population $\delta _ { o } ^ { ( g + 1 ) }$ . We adopt the $\left( \mu , \theta \right)$ selection criteria.

$$
(\mu , \theta): \delta_ {t} ^ {(g + 1)} = \text { selection } \left(\delta_ {o} ^ {(g)}, \mu\right).
$$

Stage 5 Update the iterative number, $g = g + 1$

Stage 6 Evolve and go back to stage 2 until the outputs are optimal or the termination criteria are satis<sup>fi</sup>ed.

Stage 7 End.

Output: output the optimal hyper-parameters, and classi<sup>fi</sup>cation results.

Fig. 3 shows the detailed process of parameters optimization of ES-MK-MCP.

## 4. Experiments

## 4.1. Experiment description

In this section, two widely used UCI [35] credit data sets are used to check the performance of our model: an Australian credit card data set (ACD) and a German credit card data set (GCD).

To guarantee valid results for making predictions, the data sets are randomly partitioned into training sets and independent test sets via a k-fold cross validation. The 5-fold cross validation method is used in our experiments when training our models for choosing the parameters for the binary-class credit data sets. With 5-fold cross validation, a training dataset is further randomly divided into <sup>fi</sup>ve subsets of equal size. Each of the <sup>fi</sup>ve subsets is used only one time, for validating the model trained with the four other subsets. Therefore, for each data set and each parameter combination, <sup>fi</sup>ve models are trained with <sup>fi</sup>ve reduced over-lapped subsets to acquire the corresponding average validation accuracy and avoid over-<sup>fi</sup>tness.

The performance is measured by type 1 accuracy (T1), type 2 accuracy (T2) and total accuracy (T), representing percent of correctly classi<sup>fi</sup>ed good samples, percent of correctly classi<sup>fi</sup>ed bad samples, and percent of correctly classi<sup>fi</sup>ed samples in total, respectively. They are:

Total $\mathrm { a c c u r a c y ( T ) } = \frac { \mathrm { T N } + \mathrm { T P } } { \mathrm { T N } + \mathrm { F P } + \mathrm { T P } + \mathrm { F N } } ,$

TN Type 1 accuracy T1 TN FP <sup>;</sup>

$$
\text { Type   2   accuracy(T2) } = \frac {\mathrm{TP}}{\mathrm{TP} + \mathrm{FN}},
$$

![](/api/attachments/9A5UU395/fulltext/images/a1e96055ba07c5c41e0648b4ca7f2b6c9a71c93595db0eaae038d906038af615.jpg)  
Fig. 3. Flow diagram of ES-MK-MCP.

where, TN is the number of good credit samples that are correctly classi<sup>fi</sup>ed; TP is the number of bad credit samples that are correctly classi<sup>fi</sup>ed; FP is the number of good credit samples that are misclassi<sup>fi</sup>ed, and FN is the number of misclassi<sup>fi</sup>ed bad credit samples.

Our model is tested on a PC with AMD Athlon(tm) 7750 processor, 2.65 GHz and 3.25 GB of main memory in Windows Server XP environment. MATLAB 7.6 is used to perform all computations.

## 4.2. Experiment results of two UCI credit datasets

In this section, an Australian credit card data set and a German credit card data set are used.

The <sup>fi</sup>rst data set, Australian credit card data, contains 690 credit card applications of which 383 are good credit cases and 307 are bad credit cases. There are 14 features in this data set: A1–A7, A9–A15, of which six are numerical and eight are categorical; all names and attribute values have been changed to meaningless symbols to protect con<sup>fi</sup>dentiality of the data. Furthermore, this dataset is a good mix of attributes: continuous, nominal with small numbers of values, and nominal with larger numbers of values.

The second one is a German credit card dataset which contains 1000 samples, with 700 cases granted credit cards and 300 cases refused. In this dataset, there are 20 decision attributes, 7 numerical and 13 categorical.

First, consider the in<sup>fl</sup>uence of the regularization parameter λ on the number of features. Based on the multiple kernels multi-criteria programming model, we change the regularization parameter λ to observe the changes of the number of features selected, when other parameters are <sup>fi</sup>xed.

Fig. 4 shows the number of selected features as the regularization parameter changes.

From Fig. 4, <sup>fi</sup>rst, the number of selected features is decreasing as the regularization parameter increases; however, the number starts gradually increasing with increase of the regularization parameter. The larger the regularization parameter is, the larger is the number of features. When the regularization parameter equals to zero, we have to use all attributes to train the classi<sup>fi</sup>er. Therefore, when the regularization parameter equals to zero, no features are left out or discarded. As the <sup>fi</sup>gure illustrates, there may be some point where the number of features reaches the optimum; however, the accuracy is as important as the interpretability.

Then, we further consider the accuracy of our ES-based multiple kernels multi-criteria programming model to check the in<sup>fl</sup>uence of other parameters, since the accuracy and interpretability are both important.

We compare our model with 10 other major credit analysis models, i.e., linear discriminant analysis (LDA), quadratic discriminant analysis (QDA), decision based See5, logistic regression (LogR), decision tree (DT), k-nearest neighbour classi<sup>fi</sup>er (k-NN) with k=10, MCCQP, SVM light, DS-LSSVM and GA-based SVM; results of these 10 models are from [7,27,42]. All the results of Australian and German credit card datasets are listed in Table 1 and Table 2, respectively.

![](/api/attachments/9A5UU395/fulltext/images/6bd2e1494e45fa8a1ac59253c813fdea5346e34e08b7ea90889017a1b7e2d373.jpg)  
Fig. 4. Number of selected features as the regularization parameter changes.

Table 1  
Results of the Australian credit card dataset.

<table><tr><td>Model</td><td>T (%)</td><td>T1 (%)</td><td>T2 (%)</td><td>Number of features</td></tr><tr><td>LDA</td><td>85.80</td><td>80.68</td><td>92.18</td><td>-</td></tr><tr><td>QDA</td><td>80.14</td><td>91.38</td><td>66.12</td><td>-</td></tr><tr><td>See5</td><td>86.52</td><td>87.99</td><td>84.69</td><td>-</td></tr><tr><td>LogR</td><td>86.09</td><td>86.32</td><td>85.90</td><td>-</td></tr><tr><td>DT</td><td>84.06</td><td>80.13</td><td>87.21</td><td>-</td></tr><tr><td>k-NN</td><td>69.57</td><td>54.4</td><td>81.72</td><td>-</td></tr><tr><td>MCCQP</td><td>86.38</td><td>87.00</td><td>85.52</td><td>-</td></tr><tr><td>SVM light</td><td>44.83</td><td>18.03</td><td>90.65</td><td>-</td></tr><tr><td>DS-LSSVM</td><td>86.96</td><td>89.25</td><td>85.12</td><td>-</td></tr><tr><td>GA-based SVM</td><td>88.10</td><td>84.72</td><td>92.18</td><td>3</td></tr><tr><td>ES-MK-MCP</td><td>89.01</td><td>90.27</td><td>88.39</td><td>2</td></tr></table>

From Table 1, our model gets the best average total accuracy of classi<sup>fi</sup>cation, the second best type 1 accuracy, and uses a smaller number of features to train the classi<sup>fi</sup>er on the Australian credit card dataset. Though type 2 accuracy is not the best, our model gets balanced classi<sup>fi</sup>cation accuracies. From Table 2, the German credit card data set is not very separable in our model but still achieves permissible performance. Among these eleven models, on the German credit card data set, GA-based SVM model performs the best, providing the best total classi<sup>fi</sup>cation accuracy, and our model achieves the second best accuracy but with fewer features.

In general, the proposed ES-based multiple kernels multi-criteria programming model is an ef<sup>fi</sup>cient tool for credit risk evaluation.

## 5. Conclusion

As an important application of credit decision making techniques, this paper presents a multiple criteria programming model for credit risk analysis. This model is proposed to address a major drawback other credit decision making techniques face, i.e., the need for improving interpretability while not reducing the classi<sup>fi</sup>cation performance. In our study, we introduce the linear combination of kernel functions into the multiple criteria programming model, and try to solve the nonlinear problem and the interpretability problem. By a two-stage iterated algorithm, we can get the signi<sup>fi</sup>cant features that really work for classi<sup>fi</sup>cation and remove several others that do not. Furthermore, considering that there are several parameters that need to be optimized, we propose the ES-based multiple kernels multicriteria programming model, which optimizes the parameters based on the idea of natural evolution.

Through some practical data experiments, our model achieves successful results in terms of both of the classi<sup>fi</sup>cation accuracy and the number of features selected. It shows that the model proposed is ef<sup>fi</sup>cient for credit classi<sup>fi</sup>cation problem and the evolution strategy is a good tool for parameters optimization. The selected features play important roles in credit analysis and can help decision makers. Although classi<sup>fi</sup>cation results are satisfactory, there are still some problems unsolved. Considering the data in real life are generally imbalanced, adaptive determination of the penalty function needs to be further explored. Furthermore, the penalty function in our model is <sup>fi</sup>xed, whereas different penalties should be considered to <sup>fi</sup>t different complex data constructions.

Table 2  
Results of the German credit card dataset.

<table><tr><td>Model</td><td>T (%)</td><td>T1 (%)</td><td>T2 (%)</td><td>Number of features</td></tr><tr><td>LDA</td><td>72.20</td><td>72.57</td><td>71.33</td><td>-</td></tr><tr><td>QDA</td><td>67.40</td><td>69.33</td><td>66.57</td><td>-</td></tr><tr><td>See5</td><td>72.20</td><td>84.00</td><td>44.67</td><td>-</td></tr><tr><td>LogR</td><td>76.80</td><td>88.14</td><td>50.33</td><td>-</td></tr><tr><td>DT</td><td>68.80</td><td>77.43</td><td>48.67</td><td>-</td></tr><tr><td>k-NN</td><td>71.50</td><td>90.57</td><td>27.00</td><td>-</td></tr><tr><td>MCCQP</td><td>73.50</td><td>74.38</td><td>72.00</td><td>-</td></tr><tr><td>SVM light</td><td>66.50</td><td>77.00</td><td>42.00</td><td>-</td></tr><tr><td>DS-LSSVM</td><td>77.10</td><td>88.86</td><td>49.67</td><td>-</td></tr><tr><td>GA-based SVM</td><td>85.60</td><td>89.60</td><td>76.62</td><td>13</td></tr><tr><td>ES-MK-MCP</td><td>78.92</td><td>87.13</td><td>73.50</td><td>12</td></tr></table>

## Acknowledgement

The research is partially supported by a grant from National Science Foundation of China (NSFC) under the grant No. 70531040 and No. 71071148.

## References

[1] H. Abdou, J. Pointon, A. El-Masry, Neural nets versus conventional techniques in credit scoring in Egyptian banking, Expert Systems with Applications 35 (3) (2008) 1275-1292

[2] E. Angelini, G. di Tollo, A. Roli, A neural network approach for credit risk evaluation, The Quarterly Review of Economics and Finance 48 (4) (2008) 733–755.

[3] G. Baudat, F. Anouar, Generalized discriminant analysis using a kernel approach, Neural Computation 12 (10) (2001) 2385–2404.

[4] H.G. Beyer, H.P. Schwefel, Evolution strategies—a comprehensive introduction, Natural Computing 1 (1) (2002) 3–52.

[5] D. Fogel, Evolutionary computation: towards a new philosophy of machine learning, IEEE Press, Piscataway, MJ, 1996.

[6] H. Frohlich, O. Chapelle, B. Scholkopf, Feature selection for support vector machines using genetic algorithm, International Journal on Arti<sup>fi</sup>cial Intelligence Tools 13 (4) (2004) 791–800.

[7] C.L. Huang, C.J. Wang, A GA-based feature selection and parameters optimization for support vector machines, Expert Systems with Applications 31 (2) (2006) 231–240.

[8] Z. Huang, H.C. Chen, C.J. Hsu, W.H. Chen, S.S. Wu, Credit rating analysis with support vector machines and neural networks: a market comparative study, Decision Support Systems 37 (4) (2004) 543–558.

[9] J.S. Kandola, Interpretable modeling with sparse kernels, PhD, the University of Southampton, 2001.

[10] S.S. Keerthi, C.J. Lin, Asymptotic behaviors of support vector machines with Gaussian kernel, Neural Computation 15 (7) (2003) 1667–1689.

[11] G. Kou, Y. Peng, Z.X. Chen, Y. Shi, Multiple criteria mathematical programming for multi-class classi<sup>fi</sup>cation and application in network intrusion detection, Information Sciences 179 (4) (2009) 371–381.

[12] G. Kou, Y. Peng, Y. Shi, M. Wise, W.X. Xu, Discovering credit cardholders’ behavior by multiple criteria linear programming, Annals of Operations Research 135 (1) (2005) 261–274.

[13] A. Laha, Building contextual classi<sup>fi</sup>ers by integrating fuzzy rule based classi<sup>fi</sup>cation technique and k-nn method for credit scoring, Advanced Engineering Informatics 21 (3) (2007) 281–291.

[14] J.P. Li, Z.Y. Chen, L.W. Wei, W.X. Xu, G. Kou, Feature selection via least squares support feature machine, International Journal of Information Technology & Decision Making 6 (4) (2007) 671–686.

[15] J.P. Li, J.L. Liu, W.X. Xu, Y. Shi, Support vector machines approach to credit assessment, Lecture Notes in Computer Science 3039 (2004) 892–899.

[16] H.T. Lin, C.J. Lin, A study on sigmoid kernels for SVM and the training of non-PSD kernels by SMO-type methods, Technical report, Department of Computer Science, National Taiwan University, 2003.

[17] B. Liu, J. Lu, Y. Wang, Y. Tang, An effective parameter extraction method based on memetic differential evolution algorithm, Microelectronics Journal 39 (12) (2008)1761-1769

[18] R. Liu, E. Liu, J. Yang, M. Li, F.L. Wang, Optimizing the hyper-parameters for SVM by combining evolution strategies with à grid search. Lecture Notes in Control and Information Sciences 344 (2006) 712-721.

[19] D. Martens, B. Baesens, T.V. Gestel, J. Vanthienen, Comprehensible credit scoring models using rule extraction from support vector machines, European Journal of Operational Research 183 (3) (2007) 1466–1476.

[20] B. Mersch, T. Glasmachers, P. Meinicke, C. Igel, Evolutionary optimization of sequence kernels for detection of bacterial gene starts, International Journal of Neural Systems 17 (5) (2007) 369–381.

[21] C.A. Micchelli, M. Pontil, Learning the kernel function via regularization, Journal of Machine Learning Research 6 (2005) 1099–1125.

[22] K.R. Müller, S. Mika, G. Rätsch, K. Tsuda, B. Schölkopf, An introduction to kernelbased learning algorithms, IEEE Transaction on Neural Networks 12 (2) (2001) 181–201.

[23] Y.P. Ou Yang, H.M. Shieh, J.D. Leu, G.H. Tzeng, A vikor-based multiple criteria decision method for improving information security risk, International Journal of Information Technology & Decision Making 8 (2) (2009) 267–287.

[24] M. Papadrakakis, N.D. Lagaros, Soft computing methodologies for structural optimization, Applied Soft Computing 3 (3) (2003) 283–300.

[25] E.I. Papageorgiou, P.P. Groumpos, A new hybrid method using evolutionary algorithms to train fuzzy cognitive maps, Applied Soft Computing 5 (4) (2005) 409–431.

[26] Y. Peng, G. Kou, Y. Shi, Z. Chen, A descriptive framework for the <sup>fi</sup>eld of data mining and knowledge discovery, International Journal of Information Technology and Decision Making 7 (4) (2008) 639–682

[27] Y. Peng, G. Kou, Y. Shi, Z.X. Chen, A multi-criteria convex quadratic programming model for credit data analysis, Decision Support Systems 44 (4) (2008) 1016–1030.

[28] I. Rechenberg, Evolutionsstrategie - Optimierung technischer Systeme nach Prinzipien der biologischen Evolution (PhD thesis), Reprinted by Fromman-Holzboog, Stuttgart, Germany, 1973.

[29] B. Schölkopf, C.J.C. Burges, A.J. Smola, Advances in kernel methods—support vector learning, MIT Press, Cambridge, MA, 1999.

[30] B. Schölkopf, A.J. Smola, K.R. Müller, Nonlinear component analysis as a kernel eigenvalue problem, Neural Computation 10 (5) (1998) 1299–1319.

[31] H.P. Schwefel, Evolutions strategie und numerische optimierung (PhD thesis), TU Berlin, Germany, 1975.

[32] Y. Shi, Y. Peng, G. Kou, Z.X. Chen, Classifying credit card accounts for business intelligence and decision making: a multiple-criteria quadratic programming approach, International Journal of Information Technology & Decision Making 4 (4) (2005) 581–599.

[33] Y. Shi, Y. Peng, W. Xu, X. Tang, Data mining via multiple criteria linear programming: applications in credit card portfolio management, International Journal of Information Technology and Decision Making 1 (1) (2002) 131–151.

[34] C. Stummer, E. Kiesling, W.J. Gutjahr, A multi-criteria decision support system for competence-driven project portfolio selection, International Journal of Information Technology & Decision Making 8 (2) (2009) 379–401.

[35] UCI Machine Learning Repository, Irvine, CA: University of California, School of Information and Computer Science, (2009), [Online]. Available: http://archive.ics. uci.edu/ml/datasets.html

[36] V.N. Vapnik, The nature of statistical learning theory, Springer, New York, 1995.

[37] Y.P. Wang, C.Y. Dang, An evolutionary algorithm for dynamic multi-objective optimization, Applied Mathematics and Computation 205 (1) (2008) 6–18.

[38] Y.X. Yang, Adaptive credit scoring with kernel learning methods, European Journal of Operational Research 183 (3) (2007) 1521–1536.

[39] L. Yu, S.Y. Wang, K.K. Lai, An intelligent-agent-based fuzzy group decision making model for <sup>fi</sup>nancial multicriteria decision support: the case of credit scoring, European Journal of Operational Research 195 (3) (2009) 942–959.

[40] L. Yu, S.Y. Wang, K.K. Lai, Credit risk assessment with a multistage neural network ensemble learning approach, Expert Systems with Applications 34 (2) (2008) 1434–1444.

[41] J.L. Zhang, Y. Shi, P. Zhang, Several multi-criteria programming methods for classification. Computers & Operations Research 36 (3) (2009) 823–836

[42] L.G. Zhou, K.K. Lai, L. Yu, Credit scoring using support vector machines with direct search for parameters selection, Soft Computing 13 (2) (2009) 149–155.

Jianping Li is an associate professor at Institute of Policy and Management, Chinese Academy of Sciences, China. He received his Ph.D. from University of Science and Technology of China. He has been visiting the Rutgers Business School, Rutgers University, USA. His current research interests include risk management and optimization based data mining.

Liwei Wei is an assistant researcher in the China national institute of standardization. She received his Ph.D. from Graduate University of Chinese Academy of Sciences. Her primary research interests include various issues in AI, standard information resource management, knowledge management, multiple criteria decision making, and data mining.

Gang Li is Master Degree Candidate in Institute of Policy and Management, Chinese Academy of Sciences and Graduate University of Chinese Academy of Sciences. His research interests include <sup>fi</sup>nancial risk management in commercial banks and multicriteria decision making.

Weixuan Xu is a professor at Institute of Policy and Management, Chinese Academy of Sciences, China. He received his Ph.D. from University of Maryland, USA. His research interests include industry engineering, optimization and mathematical programming.

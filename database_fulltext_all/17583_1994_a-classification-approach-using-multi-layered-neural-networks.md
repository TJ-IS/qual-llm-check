---
otero_id: 17583
otero_key: "UVDA8W92"
title: "A classification approach using multi-layered neural networks"
authors: "Selwyn Piramuthu; Michael J. Shaw; James A. Gentry"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90022-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A classification approach using multi-layered neural networks

Selwyn Piramuthu and Michael J. Shaw
University of Illinois, Urbana, IL 61801, USA

James A. Gentry

University of Illinois, Urbana, IL 61801, USA

There has been an increasing interest in the applicability of neural networks in disparate domains. In this paper, we describe the use of multi-layered perceptrons, a type of neural-network topology, for financial classification problems, with promising results. Back-propagation, which is the learning algorithm most often used in multi-layered perceptrons, however, is inherently an inefficient search procedure. We present improved procedures which have much better convergence properties. Using several financial classification applications as examples, we show the efficacy of using multi-layered perceptrons with improved learning algorithms. The modified learning algorithms have better performance, in terms of classification/prediction accuracies, than the methods previously used in the literature, such as probit analysis and similarity-based learning techniques.

Keywords: Back-propagation; Classification; Gradient-search; Neural networks

![](/api/attachments/UVDA8W92/fulltext/images/30306631414b32ea89aa5c835151e3f32abaf31bcaf69e8157727693bd294ed5.jpg)

Selwyn Piramuthu is an Assistant Professor of Decision and Information Sciences at the University of Florida. He is currently also in the process of completing his Ph.D. in MIS at the University of Illinois at Urbana-Champaign. He holds a B. Tech. from the Indian Institute of Technology, Madras, India and an M.S. from the University of Arizona. His research and teaching interests are in Machine Learning, AI, Human-Computer Interaction, Data-Simulations

Correspondence to: Selwyn Piramuthu, Department of Business Administration, University of Illinois, Urbana, IL 61801, USA.

## 1. Introduction

The need for classification or separation of data consisting of patterns or examples into their respective categories is an ubiquitous problem in business applications. Classification problems arise in such situations as credit or loan evaluation ([9], [32]), bond rating [17], consumer choice [10], tax planning [28], and prediction of bankruptcy of firms [16], among others.

Statistical procedures such as multiple discriminant analysis [1], probit [14], logit, and regression

base Management and Simulation.  
![](/api/attachments/UVDA8W92/fulltext/images/d1af647a27f717aede211928a51d132a32b70bd4ef240ca26923f47d45786e4a.jpg)

Michael J. Shaw is an Associate Professor of Information Systems at the Department of Business Administration. He also has been a research faculty member at the Beckman Institute for Advanced Science and Technology since it's inception in January 1989. His research interests include machine learning, intelligent scheduling, distributed artificial intelligence and their applications to developing flexible manufacturing and information management methods. He is cur-

rently coordinating the research program studying decision support systems at the Beckman Institute, with intelligent manufacturing, financial management, and organizational coordination technology for enterprise integration as the targeted applications. He is guest editing a special issue of IIE Transactions on Design and Manufacturing on system integration.

![](/api/attachments/UVDA8W92/fulltext/images/0791696efa4d82a5e5de56e96c8137f44501167714248a939c1f21751acb2045.jpg)

James A. Gentry is the IBE distinguished Professor of Finance at the University of Illinois, with A.B., Indiana State University; M.B.A. and D.B.A., Indiana University. He joined the faculty at the University of Illinois in 1966. From 1975–1979, he served as Associate Dean of the College of Commerce and Business Administration. He is the author of several articles on predicting bankruptcy, bond ratings and loan risks. Gentry has received numerous teaching awards and

in May 1985, he was honored to be one of three university faculty to receive the Burlington Northern Foundation Faculty Achievement Award. He has been a visiting professor at Louvain, Belgium, Melbourne, Australia, Bangalore, India and the University of Stellenbosch in South Africa. He is past president of the Midwest Finance Association, Vice President of Program for the 1986 Financial Management Association meetings and President of the Illinois State Universities Retirement System and a President of the University of Illinois Athletic Board.

have been widely used [4] in business for classification purposes. Parametric statistical methods require the data to have a specific distribution, which is usually Gaussian. In addition to the restriction on the distributions involved, missing (omitted) variables, multi-collinearity, autocorrelation, linear versus quadratic model assumptions, and qualitative variables could lead to problems with the estimated model when statistical methods are used. Inductive learning [29] and learning by using artificial neural networks [36] are two recent developments in the AI domain that have potentially promising applications for classification in business applications. Researchers ([7], [27], [30], [38]) have studied various inductive learning algorithms along with appropriate statistical methods with results favoring inductive learning algorithms over statistical methods. Inductive learning methods have better knowledge representational structure in the sense that the decision tree that is induced can be used to derive (production) rules which can be implemented in an expert system, thus facilitating in automating the classification process.

Neural networks, which learn by modifying weights in the connections in the network, are potentially advantageous over both inductive learning and statistical methods. Characteristics of a neural network are its inherent parallelism and its tolerance to noise, which is achieved by distributing knowledge across the network [26]. Neural networks are capable of learning incrementally, which eases the process of updating knowledge as new examples are added to the system. The topology of a neural network that is most suitable for classification purposes is the multi-layered perceptron along with back-propagation algorithm, which is discussed in detail in section 4. Back-propagation utilizes steepest-descent method for searching in the problem space. The method of steepest-descent is the most simplistic of all gradient descent methods, and does not take the curvature of the search space into consideration. In this paper, we present a modified back-propagation algorithm with the Newton-Raphson algorithm, which utilizes information on the curvature of the search space for efficient convergence to the final solution, for gradient search.

Comparing neural-net methods with other classification methods, a number of prior studies ([12], [15], [31], [42]) have found that the back-propagation algorithm achieves higher asymptotic accuracy levels, is better able to handle noise, but requires a larger training data set. It is also commonly acknowledged that a major problem with the back-propagation algorithm is that it is too slow.

The main objectives of this paper are: (1) to develop modified learning algorithms for improving the back-propagation procedure, and (2) to show the effectiveness of using neural networks, specifically, multi-layered perceptrons, as a tool for classification problems, focussing specifically on financial management and credit analysis. As will be discussed in subsequent sections, the results are very encouraging, showing definite value in using neural networks for financial classification applications such as loan evaluation and credit analysis.

When implemented in the back-propagation algorithm, the modified (Newton-Raphson) method performed consistently better than the regular back-propagation algorithm, in terms of efficiency and classification/prediction accuracy. The hybrid-method, a combination of the regular as well as the Newton-Raphson type algorithms, performed the best overall. In addition to backpropagation, we use two inductive learning algorithms and probit to analyze two real-world financial data sets. Overall, the back-propagation algorithms performed at least as good as the other methods used in the literature for analyzing financial classification data.

In the next section, we present a brief overview of various methods that have been used for financial classification. The Newton-Raphson algorithm is discussed in section 3. The modified back-propagation with Newton-Raphson algorithm and corresponding gradient derivations are discussed in section 4. Further improvements in performance of the algorithm are considered by combining the strengths of both Newton-Raphson and steepest-gradient methods as implemented in the Hybrid algorithm which is given in section 5. Simulation results using a financial classification example, comparing the performances of the three algorithms (SG, NR, and NR-SG) as incorporated in back-propagation algorithm in multi-layered perceptrons, are given in section 6. In section 7, two real-world financial classification examples are used to compare the performances of neural-net method with two similarity-based learning algorithms and probit. Section 8 concludes with insights gained through this study and its contributions.

## 2. Background

Traditionally, researchers interested in financial classification applications have applied parametric methods such as multiple discriminant analysis (MDA), probit, logit, and regression. Most of these statistical methods assume the data being used to be distributed Gaussian. In addition to assumptions of the distributions involved, statistical methods are restricted by the following potential problems. While using qualitative variables in probit, when the probit regression lines that correspond to the different values of the qualitative variables are not parallel, interpretation of any comparison between them is difficult [14]. Omitted variables, unless their regression coefficients are zero, could be a cause for non-zero mean value of error terms in regression analysis which in turn could lead to erroneous results. Multi-collinearity, a major problem when analyzing real-world data, arises due to interdependencies among attributes. Auto-correlation is due to correlations between residual or error terms of two or more observations. Finally, assumption of regression functions to be linear or quadratic might induce additional bias in estimating parameters.

Recent advancements in artificial intelligence have spurred interest both among practitioners and researchers to evaluate some of the methods that have been developed under the rubric of AI as compared to statistical methods. Mingers [30] compared the performances of a modified version of ID3 [34] and multiple regression and concluded in favor of induction. Messier and Hansen [27] used loan default and bankruptcy data to compare the effectiveness of ID3, discriminant analysis, individual judgements, and group judgements in discovering predictive knowledge structures. After extensive analysis they concluded that (similarity-based) inductive learning methods may be useful for small highly-structured problem domains, and also for expert system development. An advantage of similarity-based learning is its representation of causal relationships which are more informative for identifying the relative importance of attributes that are used in the study.

Theoretically artificial neural-network systems are capable of acquiring any arbitrary mapping function $[21]$ , by means of appropriate number of nodes and links among them, and therefore have no inherent representational or learning advantages or disadvantages as compared to traditional machine learning systems. Both back-propagation algorithm and induction are independent of assumptions of the distributions of the sample of training data that are used in the learning process. Most of the shortcomings that are associated with statistical analyses are hence of less concern while using either back-propagation or inductive learning algorithms.

In addition to similarity-based learning methods, artificial neural networks are being widely used for similar purposes. Neural networks have the following inherent advantages over inductive learning methods:

\- Incremental learning-induction of decision trees [34], is done probabilistically based on the number of positive examples that are present at a given node, and as such necessitates a need for all the examples to be present simultaneously, whereas back-propagation does not have this restriction – examples are included and learning occurs in the network as and when new examples are added to the network. This facilitates the process of incremental learning in neural networks by learning to modify current knowledge incrementally as new examples are added to the system.

\- Tolerance to noise-classification analyses using real-world data entails a certain amount of immunity toward noise present in the data. Neural networks are inherently noise tolerant due to its distributed representation where knowledge is represented across all the nodes in the network. Since a single piece of information is distributed and stored in an aggregate manner among different nodes in the network, noise in a processing unit does not affect the overall behavior of the network significantly. Similarly, when only partial or incomplete information is available, the network provides immunity by attempting to complete the respective patterns by utilizing available partial information.

\- Polythetic learning / interaction effects—given a set of observations, information can be obtained by considering each of the variables that are included in the observations as well as by considering the effects of variables on one another in influencing the final decision. Interaction between variables thus play a crucial role in providing a more complete information in addition to those from the individual variables themselves. These interactive effects are naturally captured in neural networks by means of connections from different variables that end up at a single node at a higher node, thus aiding in an efficient use of the information that is present in the input variables. In the inductive learning process, for splitting at a node each of the variables are evaluated one at a time, thus ignoring the effects of variable combinations (to account for interactive effects) explicitly. This could lead to a loss of information that could have otherwise been retrieved from the examples. The process of considering all the variables together (polythetic) in back-propagation [15], as opposed to one at a time as in inductive learning, fosters an improvement in performance of the back-propagation algorithm over inductive learning algorithms.

\- Concept representation–knowledge is represented as strengths of weights in links in a neural-network thus leading to tolerance of noise, whereas in inductive learning, explicit rules are formed for a given class, which need not represent the actual state of affairs in the data set of interest. A single wrong example can lead to a misleading rule while using inductive learning, which is avoided in neural-networks by diffusing the same across units in the network leading to severity of a lesser order. Whereas the induced rules are informative as to the knowledge they represent, it is very difficult, if not impossible, to derive meaning from the weights in the links in a neural-network.

\- Finer granularity–inductive learning algorithms are characterized by their coarser granularity due to the mode in which examples are covered. Neural networks, on the other hand, are relatively fine-grained due to distributed knowledge representation. The finer granularity of search in neural-networks enables the search process to be focused more on the structure of the search space, thus leading to better learning.

As shown in Figure 1, the classification process in statistical, inductive learning, and neural-network classifiers are done in two stages. In the statistical classifier, input values are used sequentially to evaluate the function value using the estimated parameter values. During the second stage, the best among different functional values is used to determine the (maximum likelihood) class of a given pattern. In the inductive learning classifier, input values are used sequentially to be passed on from the root of the decision tree toward its leaf nodes. The input class is deduced as per the leaf node to which the pattern belongs. In the neural-network classifier, input values are propagated in parallel through the $N_{o}$ input connections toward the output layer. Depending on the network configuration, the output values from the M units in the output layer are used appropriately to determine the class of a given input pattern.

![](/api/attachments/UVDA8W92/fulltext/images/f9909e9067d9cbaefad53e01f9f3c641c739dd26597fa1ec8730a18f3f0d0a69.jpg)

(b) inductive learning classifier  
![](/api/attachments/UVDA8W92/fulltext/images/b53fbb32278dab8c17ae0529b0714071f725023d4da4a450e645d7eb3acf77bf.jpg)

(c) neural network classifier  
![](/api/attachments/UVDA8W92/fulltext/images/0c25924fa152b17bee5f98dc2789f2cba0c79a32b4aebe651e317e3b30bb23dc.jpg)  
Fig. 1. Block diagrams of classifiers.

Artificial neural networks have shown promising results for a number of problem areas including content addressable memory, pattern recognition and association, category formation, speech production and global optimization ([23], [36], [3], [37], [20]). It has also been tried with fairly good results in financial [12] as well as in manufacturing applications [35].

Back-propagation algorithm uses an iterative method to feed the activation values from lower layers to the layers above and to propagate the error values backward from layers above to the next layer below. There are three broad classes of iterative methods that are used for optimization problems $[40]$ : (1) quadratic methods, that use the first and second derivatives of the objective function in the neighborhood of the current trial solution, (2) linear methods that use first but not second derivatives, and (3) directional methods that use no derivatives.

Researchers ([6], [13], [33], [41]) have studied second order functions (quadratic method) with promising results. The primary motivation behind this study is to improve the performance of the classical back-propagation algorithm by utilizing better gradient search methods than the simplistic steepest-gradient method that is being currently used.

Recently, several researchers ([12], [15], [31], [42]) have studied the comparative performances of symbolic, connectionist, and statistical methods. Dutta and Shekhar ([12]) used bond-rating data to compare the performances of back-propagation and regression, in which back-propagation out-performed regression in predicting bond ratings from a given set of financial ratios. Singleton and Surkan ([39]) compared the classification performances of back-propagation and linear discriminant analysis on ratings by Moody's and Standard and Poor's indices and concluded in favor of back-propagation. Fisher and McKusick ([15]) compared the performances of ID3 and back-propagation in which back-propagation performed consistently better in terms of asymptotic accuracy in classification. Mooney, Shavlik, Towell, and Gove ([31]) used ID3, perceptron, and back-propagation in their study using four realworld data sets and concluded that back-propagation performs better on noisy complex environments. Weiss and Kapouleas ([42]) used four real-world data sets to compare the performances of statistical classifiers such as linear/quadratic, Bayes, nearest-neighbor, CART ([8]), ID3, and back-propagation and concluded that back-propagation performed at least as well as the other methods in terms of classification accuracy.

## 3. Newton-Raphson (NR) algorithm

For non-linear functional optimization problems, gradient descent methods are used for finding the best (if possible, optimal) solution by searching (reverse hill-climbing) the solution space iteratively. Initially, an arbitrary point in the search space is chosen, from which the final solution is approached iteratively by descending along the direction which provides improved solutions. The Newton-Raphson algorithm is one of the several classes of methods that are based on a quadratic model of the objective function, in contrast to the scaled linear model function of the classical steepest-gradient method. There are two major justifications for choosing a quadratic model: its simplicity and, more importantly, the success and efficiency in practice of methods based on it [18].

A quadratic model of the objective function is obtained by taking the first three terms of the Taylor-series expansion about the current point.

$$
f (x _ {k} + p) \approx f (x _ {k}) + g _ {k} ^ {T} p + \frac {1}{2} p ^ {T} G _ {k} p,
$$

where, $x_{k}$ is the current estimate of $x^{*}$ , the minima; p is the direction of search; $g_{k}(=g(x_{k}))$ is the first derivative of f, and $G_{k}(=G(x_{k}))$ is the second derivative.

The quadratic function is then formulated in terms of the step to the minimum (p) rather than the predicted minimum itself. The minimum of the above function is achieved if $p_{k}$ is a minimum of the quadratic function:

$$
\Phi = g _ {k} ^ {T} p + \frac {1}{2} p ^ {T} G _ {k} p.
$$

Suppose that $\Phi$ takes its minimum value corresponding to $p = p_{k}$ , then, $\nabla p_{k}\Phi = 0$ . i.e., $G_{k}p_{k} + g_{k} = 0$ , which yields $p_{k} = -G_{k}^{-1}g_{k}$ . The Newton-Raphson method uses $p_{k}$ as the current direction of search which is updated iteratively.

In the simplest problem of unconstrained minimization of the univariate function f:

$$
\min _ {x \in R ^ {\prime}} f (x),
$$

if a function is everywhere twice-continuously differentiable, and a local minima of the function exists at a finite point $x^{*}$ , then the following two necessary and sufficient conditions for an unconstrained minimum must hold at $x^{*}$ :

$$
f ^ {\prime} (x ^ {*}) = 0, \tag {1}
$$

and

$$
f ^ {\prime \prime} (x ^ {*}) \geq 0\tag{2}
$$

The local convergence properties of Newton-Raphson method make it an exceptionally attractive algorithm for unconstrained minimization. A further benefit of the availability of the second derivatives is that the sufficient conditions for optimality can be verified as stated above.

The Newton-Raphson algorithm can be summarized as follows:

1. initialize-for any starting point $x_{k}$ , Taylor-series expansion (first 3 terms) about the current point:

$$
f (x _ {k} + p) \approx f (x _ {k}) + g _ {k} ^ {T} p + \frac {1}{2} p ^ {T} G _ {k} p,
$$

2. minimize:

$$
\Phi = g _ {k} ^ {T} p + \frac {1}{2} p ^ {T} G _ {k} p,
$$

3. obtain gradient

$$
\nabla_ {p _ {k}} \Phi = 0, g i v i n g G _ {k} p _ {k} + g _ {k} = 0,
$$

4. search in direction:

$$
p _ {k} = - G _ {k} ^ {- 1} g _ {k}.
$$

Gill, Murray, and Wright ([18], p 286) rank different methods for solving unconstrained problems based on the confidence that can be placed in the methods' success in finding an acceptable solution. Newton-type algorithms with second derivatives is ranked first, followed by Newton-type without second derivatives, Quasi-Newton with first derivatives, Quasi-Newton without first derivatives, Conjugate-Gradient type with first derivatives, conjugate-gradient without first derivatives, and polytope. The superiority of the Newton-Raphson type method reflects the use of the second order properties of the function to improve algorithmic efficiency as well as to provide qualitative information about the computed solution space ([18], p. 320). An additional benefit using the Newton-Raphson type method is that there are certain problem classes (e.g., those with saddle points) where only a Newton-type method is assured of being able to proceed.

Local minima, which is a problem with all gradient search methods, is still a problem with the Newton-Raphson method. But, it can still be used for finding local minima when there are saddle points, or when the problem is known to be convex, since the local minimum must then be a global minimum. Many real-world problems are not convex, but one may still be content with a local minimum because the non-convex elements in the problem are in the nature of small perturbations (which are probably saddle points), so that it seems unlikely that they could introduce unwanted local minima or, because the only practical alternative to a local minima is a completely arbitrary solution.

## 4. Modified BP with NR type algorithm

Multi-layered perceptrons consist of a set of processing units (Figure 2), with corresponding activation functions $(a_{i})$ , links among the processing units, weights (W) corresponding to the links, and threshold $(\theta)$ values for each of the processing units. The processing units are arranged in layers and are connected to one another by restricted links. Each unit in a layer is connected to units in the immediate next and previous layers and not to any of the units in the same layer. Each unit acts as an integrator of the signals which it receives from the units in the layer which is immediately below the layer in which the unit of interest is located. The links between the units are all assigned weights as per the activation of the unit in the lower layer from which the link originates. Each of the units, except those in the input layer, are also assigned a threshold value $(\theta)$ , which is used in deciding to propagate the units' activation forward. As shown in Figure 2, a processing unit j receives its input from all the units in the previous layer $(X_{0}, X_{1}, \cdots, X_{N-1})$ , which is used to determine its output. The output from an unit (j) is a function (usually sigmoidal) of the difference between its threshold $(\theta_{j})$ and the sum of weighted activations from previous layer.

![](/api/attachments/UVDA8W92/fulltext/images/26a18a4a6b220c4e580dcd19574f169423fd8d332a28263eedac33734f535f58.jpg)  
Fig. 2. An artificail neural unit, j, and its activation function.

## 4.1. Back-Propagation (BP) algorithm

1. Initialize-Set number of units in input $(N_o)$ , output (M), and hidden $(N_k; k = 1 \ldots h)$ layers, where $h$ is the number of hidden layers. Specify links between units with no links between two units in the same layer. Set random values for weights in all the threshold levels for all the units (except those in the input layer)

2. Input–Present input/output vectors $i_{1},\ldots,$ $i_{N-1}, o_{1},\ldots,o_{M-1}.$

3. Update weights: $w_{ij}(n + 1) = w_{ij}(n) + \eta \delta_j a_i + \alpha(w_{ij}(n) - w_{ij}(n - 1))$ where $w_{ij}(n + 1)$ is the weight in the link from unit i to unit j in the $n^{\text{th}}$ iteration (epoch), $\eta$ the learning rate, and $\alpha$ the momentum term. The weights during the initial pass are set at random.

## 4. Calculate actual outputs:

for hidden layers $(x_{i} = i_{i}$ if unit $i$ is an input unit):

$$
a _ {j} = f \left(\sum_ {i = 0} ^ {N _ {k - 1}} w _ {i j} x _ {i} - \theta_ {j}\right), 0 \leq j \leq N _ {k},
$$

for output layer:

$$
a _ {j} = f \left(\sum_ {i = 0} ^ {M - 1} w _ {i j} x _ {i} - \theta_ {j}\right), 0 \leq j \leq N _ {h},
$$

where $\theta_{j}$ is the threshold in the $j^{\mathrm{th}}$ unit in the layer under consideration.

## 5. Update δ-values:

if unit (j) is an output unit:

$$
\delta_ {j} = \left(o _ {j} - a _ {j}\right) f ^ {\prime} \left(n e t _ {j}\right),
$$

if unit(j) is a hidden unit:

$$
\delta_ {j} = f ^ {\prime} \left(n e t _ {j}\right) \sum_ {k} \delta_ {k} w _ {j k}.
$$

## 6. Repeat: Go to step 2.

Initially, weights to the links are assigned randomly and the resulting (actual) output is compared with the target output provided by the teacher (steps 1–5). The difference between the actual and the target output is the error, which is summed over all the output units. Since the purpose here is to minimize the error that results from the weights that are assigned to the links, the objective function for this optimization problem is taken to be the total sums-of-squares (tss) of the differences between the actual and the target values for the output nodes. Weights in the links are then modified by means of a function that takes the gradient of the objective function into account (step 3). Steps 1–6 are repeated until the pre-specified tss value (ecrit) is reached or the pre-specified number of epochs (iterations) are reached. Step 5 incorporates the gradient search information by means of $\delta$ , the step length in the direction of descent. Since this is a gradient search method, it has all the pitfalls that are associated with gradient descent methods such as finding a local minima or a saddle point. The Newton-Raphson algorithm discussed in the previous section avoids saddle points although local minima would still remain a problem.

The classical back-propagation algorithm, as discussed above, utilizes the steepest-gradient descent method. In the steepest-gradient method [36], the objective (error) function that is minimized is

$$
E = \sum_ {p} E _ {p} = \frac {1}{2} \sum_ {p} \sum_ {j} \left(o _ {p j} - a _ {p j}\right) ^ {2},\tag{1}
$$

where p corresponds to the pattern that is currently under consideration, $o_{pj}$ is the target output value of the $j^{th}$ unit in the output layer when pattern p is input, $a_{pj}$ is the actual output value of the $j^{th}$ unit in the output layer when pattern p is input, and E is the sum of errors over all the patterns that are input. Once the threshold( $\theta$ ) values are set, the $\theta$ terms can be ignored for further analysis. For unit j receiving input from unit i's in the lower layer

$$
n e t _ {j} = \sum_ {i} w _ {i j} a _ {i},\tag{2}
$$

where

$$
a _ {i} = f (n e t _ {i}) = \frac {1}{1 + e ^ {- n e t _ {i}}},\tag{3}
$$

a sigmoid (squashing) function. Since the change in weight in a link is directly (negatively) proportional to the rate of change of the error function with respect to a change in weight in the link of interest

$$
\Delta_ {p} w _ {i j} \propto - \frac {\partial E _ {p}}{\partial w _ {i j}}.
$$

By the chain rule, the derivative can be written as the product of two parts: the derivative of the error with respect to the output of the unit times the derivative of the output with respect to the weight.

$$
\frac {\partial E _ {p}}{\partial w _ {i j}} = \frac {\partial E _ {p}}{\partial n e t _ {p j}} \frac {\partial n e t _ {p j}}{\partial w _ {i j}},\tag{4}
$$

from equation 2, we get

$$
\frac {\partial n e t _ {p j}}{\partial w _ {i j}} = \frac {\partial}{\partial w _ {i j}} \sum_ {k} w _ {k j} a _ {p k} = a _ {p i},\tag{5}
$$

define

$$
\delta_ {p j} = - \frac {\partial E _ {p}}{\partial n e t _ {p j}} = - \frac {\partial E _ {p}}{\partial a _ {p j}} \frac {\partial a _ {p j}}{\partial n e t _ {p j}},\tag{6}
$$

from equation 3,

$$
\frac {\partial a _ {p j}}{\partial n e t _ {p j}} = f ^ {\prime} \left(n e t _ {p j}\right),\tag{7}
$$

which is the derivative of the squashing function f for the $j^{th}$ unit, evaluated at the net input $net_{pj}$ to that unit.

If $j$ is an unit in the output layer of the network, from equation 1

$$
\frac {\partial E _ {p}}{\partial a _ {p j}} = - \left(o _ {p j} - a _ {p j}\right),\tag{8}
$$

from equations 6, 7, and 8, we get

$$
\delta_ {p j} = \left(o _ {p j} - a _ {p j}\right) f ^ {\prime} \left(n e t _ {p j}\right).\tag{9}
$$

In the proposed method, the idea of optimizing a quadratic function as in the Newton-Raphson method is utilized. The original objective function, in the classical steepest-gradient method, of minimizing the squares of the differences between the actual and the desired output values summed over the output units and all pairs of input/output vectors is replaced by an equivalent exponential function. This is done in order to allow for the second derivative to be derived from the objective function and also to take advantage of the properties of exponential functions, specifically for altering the step-lengths appropriately. The rate of change of an exponential function (e.g., $e^{(o_{j}-a_{j})^{2}}$ ) is the most for higher values of $(o_{j}-a_{j})^{2}$ , and the rate drops precipitously for lower values of $(o_{j}-a_{j})^{2}$ . We take advantage of this characteristic in the proposed algorithms. The direction of descent which minimizes $(o_{j}-a_{j})^{2}$ is equivalent to the direction of descent which minimizes $e^{(o_{j}-a_{j})^{2}}$ , and the transformation is justified since both the exponential of a nonnegative function and the function itself are monotonically increasing. By taking the exponential, the granularity of search is increased as the step-size is increased.

The function to be minimized (ignoring the subscript p) is:

$$
f (a) = e ^ {(o _ {j} - a _ {j}) ^ {2}},\tag{10}
$$

where $o_{j}$ and $a_{j}$ are the target and actual outputs (active values) of the $j^{th}$ unit in the output layer. Instead of taking the second order gradient direction $p_{k}$ as in previous attempts using second-order methods for back-propagation, we use the gradient $G_{k}p_{k} + g_{k}$ . This avoids the inversion of the Hessian matrix $G_{k}$ , although it is only a scalar because we are only dealing with one output unit at a time. The corresponding gradient, with respect to $a_{j}$ , of the quadratic function, as per the Taylor's series expansion in the Newton-Raphson algorithm can be derived as follows:

$$
\begin{array}{l} g _ {j} = - 2 (o _ {j} - a _ {j}) e ^ {(o _ {j} - a _ {j}) ^ {2}}, \\ G _ {j} = 2 e ^ {(o _ {j} - a _ {j}) ^ {2}} + 4 (o _ {j} - a _ {j}) ^ {2} e ^ {(o _ {j} - a _ {j}) ^ {2}}, \end{array}
$$

from which we derive the gradient to be

$$
G _ {j} \left(o _ {j} - a _ {j}\right) + g _ {j} = 4 \left(o _ {j} - a _ {j}\right) ^ {3} e ^ {\left(o _ {j} - a _ {j}\right) ^ {2}},\tag{11}
$$

substituting equation 11 for the gradient (equation 8) and equation 7 in equation 6 (ignoring the subscript), we get

$$
\delta_ {j} = 4 \left(o _ {j} - a _ {j}\right) ^ {3} e ^ {\left(o _ {j} - a _ {j}\right) ^ {2}} f ^ {\prime} \left(n e t _ {j}\right),\tag{12}
$$

which is the corresponding modification in step 5 of the back-propagation algorithm if unit j is an output unit. Here, $f'(net_{j})$ is the derivative of the activation function with respect to a change in the net input to unit j. If unit j is a hidden unit, the modified delta values are propagated from the output units downward to the hidden units. Hence the activations of the hidden units are indirectly affected by the modified delta values of units in the output layer. Since the second order derivative of the objective function is taken into consideration here, the algorithm is insensitive to saddle points in the solution space. Convergence is also much faster since a quadratic function (as opposed to a linear function as in the steepest-gradient method) is utilized in the solution procedure.

## 5. The hybrid (SG-NR) algorithm

By using the second-order gradient, the NR algorithm search through the weight space would demonstrate the following behavior: during the initial stages in the search process, when the differences between the actual and target classes are large, the NR algorithm tends to take larger step sizes due to the exponential transformation. This could lead to undesirable effects such as thrashing since the curvature of the search space is not effectively taken into consideration by the NR algorithm unless the starting point is closer to the optimal solution. Once the search reaches the proximity of the optimal solution, the step size taken by the NR algorithm decreases drastically and is thus more effective in converging to the final solution faster. The motivation for using the hybrid (SG-NR) algorithm is the relative good performances of SG and NR algorithms farther and closer to the optimal solution respectively. Both steepest-gradient descent and Newton-Raphson methods were incorporated in this algorithm. The steepest-gradient (SG) method is used to get closer to the final solution and then the Newton-Raphson (NR) method is initiated from that point to converge to the final solution. The final solution thus reached would be at least as good as that which is reached by the NR or SG method alone, and the convergence is also faster in the hybrid method than in the SG and NR methods alone. The hybrid algorithm is as follows:

1. initialize—steps 1 and 2 as in the back-propagation algorithm as given in section 4.

2. calculate the initial tss value

$$
t s s _ {i n i t i a l} = \sum_ {p} \sum_ {j} \left(o _ {p j} - a _ {p j}\right) ^ {2},
$$

where, p is over all the input patterns, and j is over all the units in the output layer.

3. SG algorithm-follow the back-propagation algorithm as given in section 2 until

$$
t s s = \left(t s s _ {i n i t i a l} - 0. 0 4\right) * 0. 8.
$$

4. NR algorithm—apply NR (modified BP) algorithm as given in section 4 until the tss value becomes less than or equal to 0.04 (the prespecified ecrit value).

In this study, the steepest-descent algorithm was used during the initial period until 80 percent of the difference between the final tss (total sums-of-squares for all the input patterns – tss is the sums of squares of the differences between the actual and the target activation values of the units in the output layer) value (ecrit, was set at 0.04) and the initial tss value, was reached. Hence, by using the NR method only for the last 20 percent of the values of tss a better performance of the NR algorithm is guaranteed than otherwise.

## 6. A financial classification example

For financial classification, the input patterns are taken to be the independent variables, and the output patterns are the dependent variables. Learning in the network takes place by encoding the input patterns (independent variables) in the hidden layer(s), which is then decoded to map to the output patterns (dependent variables). In this section, we use a loan evaluation data set to go through the mapping of classification problems on to multi-layered perceptrons. A brief description of the loan evaluation data is given in appendix-B, and the data is used for detailed analyses in the next section. In addition to the 12 continuous (cash flow components) variables, 3 qualitative components (nominal variables) were also included in this data set. The three qualitative variables are guarantee, collateral, and secured – both guarantee and collateral are boolean

variables which take values of either yes or no, and secured takes values 0 or 1 depending on whether a firm is secured or not respectively. Each of the 15 independent variables are assigned a separate input unit in the multi-layered perceptron network. Since there are 5 classes, we have 5 output units, one for each of the classes. The output unit with the highest activation value is taken to represent the class of a given example. The number of hidden units in the only hidden layer used is taken to be 10 (half of the total number of input and output units). The network configuration for this example is given in Figure 3. Convergence of the network for SG, NR, and SG-NR are given in Figure 4. As can be seen from Figure 4, for the SG algorithm, the tss value remains at around 7 for a wide range of the number of epochs, and still did not converge after 30,000 epochs.

For the network, the learning rate parameter $(\eta)$ was set at 0.25. The momentum term $(\alpha)$ was set at 0.9 to allow for faster learning by filtering out high curvatures and by allowing the effective weight steps to be larger. The tss value to be reached for convergence (ecrit) was randomly assigned a value of 0.04 as per Rumelhart et al. ([36]). The input units are numbered from 0 through 14, hidden units numbered from 15 through 24, and the output units from 25 through 29. The bias terms for both hidden units and output units are given in brackets next to the appropriate units. Both continuous as well as

![](/api/attachments/UVDA8W92/fulltext/images/a2ce757a4648243e836fc2a1a3510c06a5458da8fad37362efddc74e40bb82d8.jpg)  
Fig. 3. Network for loan evaluation data.

![](/api/attachments/UVDA8W92/fulltext/images/56b8c912694fdd42a0571b7966fa8d5cf894c3b674658b78f6e7ef03c17a9936.jpg)  
Fig. 4. Convergence rates of SG, NR, and SG-NR for the example problem.

nominal variables were used as input without any additional pre-processing such as by using dummy variables.

## 7. Applications

Two real-world financial risk classification data sets are used to compare the performances of different algorithms. Data used in [1] and a loan evaluation data are used to compare the relative performances of different algorithms under varying conditions of noise present in real-world data. The different risk classification data sets (for evaluating loan payments and loan evaluation respectively) were used due to their differences in data structure. The Abdel-Khalik and El-Sheshai ([1]) data consists of ratios and trends, and the loan evaluation data set consists of 12 real-valued continuous variables and 3 nominal variables.

![](/api/attachments/UVDA8W92/fulltext/images/8d092926cf61ab504e0c5fcab393816784e39eac1d6565a11fa0737bf6db74f2.jpg)  
Fig. 5. Convergence speed dynamics with varying number of hidden units (default classification data).

Summary of results using Abdel-Khalik, et al. data

<table><tr><td></td><td>SG</td><td>NR</td><td>SG-NR</td><td>ID3</td><td>NEWQ</td><td>PROBIT</td></tr><tr><td>epochs</td><td>30000</td><td>151.7</td><td>86.2</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td>time (sec.)</td><td>9024</td><td>86.2</td><td>50.4</td><td>46 *</td><td>12 *</td><td>11 **</td></tr><tr><td>tss</td><td>1.001</td><td>0.04</td><td>0.04</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td>classification (%)</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td><td>78.1</td></tr><tr><td>prediction (%)</td><td>87.5</td><td>87.5</td><td>87.5</td><td>87.5</td><td>87.5</td><td>37.5</td></tr></table>

(\* both ID3 and NEWQ were run using IBM-PC/AT-286).  
(\*\* probit was run using an IBM 3081).

Also the number of classes were 2, and 5 in the loan payments and loan evaluation data sets respectively.

The performances of different methods are compared with respect to their prediction/classification accuracies, and the time and number of epochs taken by each to converge to a pre-specified tss value (=0.04). In addition to back-propagation, performances of ID3 and NEWQ - two similarity-based learning algorithms, and probit [14], a standard statistical procedure are also studied. ID3 and NEWQ are briefly discussed in appendix-A, and a brief description of the two real-world data are given in appendix-B.

## 7.1. Loan-payment default classification

For the Abdel-Khalik and El-Sheshai ([1]) data set, the learning rate parameter ( $\eta$ ) was set at 0.25, momentum term ( $\alpha$ ) was set to 0.9, and the final convergence value for tss (ecrit) was set at 0.04. The network consisted of 18 input units (corresponding to the 18 input attributes), 1 output unit and a hidden layer with 10 hidden units.

![](/api/attachments/UVDA8W92/fulltext/images/fe130a8a4364d0558fc5bdcb7d14357d24b5dfc4273798ea224366bfbf002f48.jpg)  
Fig. 6. Convergence speed dynamics with varying number of hidden units (bankruptcy prediction data).

Mooney et al. ([31]) used 10% of the total number of input and output units as the number of units in the hidden layer, which they found empirically to work well. Fisher and McKusick ([15]) tried 0, 10, and 20 hidden units using their data sets from three domains. They reported results only using 10 hidden units which was the best over all domains. In Mooney et al. and Fisher and McKusick's study, the input variables were all represented in binary form. Effects on convergence using different number of hidden units using this data is given in Figure 5.

From Figure 5, the convergence remains stable around 150 epochs over a wide range of number of hidden units. So, we decided on 10 hidden units, which is about half of the total number of input and output units. Ten separate simulation runs were done for all three back-propagation algorithms and the average values are reported in Table 1.

In addition to the SG, NR, and SG-NR backpropagation algorithms, analyses of the ID3, NEWQ, and probit were also done using the same data set for comparison purposes. The 32 examples were used for training the network, or decision tree, or to obtain the discriminant function as the case may be. There was a significant decrease in the number of epochs required as well as the time taken for NR and SG-NR as compared to those for SG. Simulations were stopped either when the tss value was less than 0.04 or when the number of epochs reached 30,000. Even after 30,000 epochs, the tss for SG remained at 1.001 (on an average), and presumably would have taken many more epochs to converge to 0.04. The classification accuracy was a 100 percent in all the neural-network algorithms, ID3, and NEWQ. The classification accuracy of probit was just 78.1%, which probably is due to the fact that probit uses just a single

Table 3

hyper-plane (which severely limits its ability to separate the examples belonging to different classes effectively) to separate the two classes, whereas this is not the case with the other methods.

Surprisingly, both classification and prediction results for SG, NR, SG-NR, ID3, and NEWQ turned out to be the same, possibly due to the size of the data set. This could also be because the points corresponding to the examples in the example space are possibly scattered such that only 14 of the 16 testing examples fall under hyper-planes belonging to specific classes. The results using ID3 are similar to those reported in [27]. This prompted us to utilize other data sets, with different characteristics, in this study for more conclusive results.

Although different machines were used for running the different programs, run times are given in Table 1 for comparing those of the back-propagation algorithms. Since the different programs were run on different machines under different environments (SG, NR, and SG-NR on a Convex-C240 under UNIX, ID3 and NEWQ on IBM-PC/AT-286 under DOS, and probit on IBM-3081 under VM/CMS), the run-times cannot be compared directly. The NR-type algorithms performed much better than SG in terms of speed of convergence. Due to the inherent parallelism in the back-propagation algorithm, speed-ups in multiple orders of magnitude can be achieved by vectorizing the code.

## 7.2. Credit-worthiness

The purpose of the loan evaluation process is to evaluate the credit-worthiness of firms, as a measure of their abilities to repay loans. As noted by Shaw and Gentry ([38]), in addition to information available from financial statements, qualitative information play a vital role in the loan evaluation process. The loan evaluation data set was partitioned into a training and a testing set, each consisting of 50 examples. NEWQ was not used since NEWQ only uses binary class values and the data has 5 classes. For the same reason, polytomous probit was used instead of the regular binary probit in which the dependent variable can take on only binary values. Ten different random sets of training and testing examples were used, and the average values from ten different analyses are summarized in Table 2. The individual values for classification/prediction are given in Table 3.

Table 2  
Summary of results using loan evaluation data

<table><tr><td></td><td>SG</td><td>NR</td><td>SG-NR</td><td>ID3</td><td>PROBIT</td></tr><tr><td>epochs</td><td>30000</td><td>1880</td><td>1276</td><td>N/A</td><td>N/A</td></tr><tr><td>time (sec.)</td><td>13764</td><td>1218</td><td>634</td><td>73</td><td>16</td></tr><tr><td>tss</td><td>3.989</td><td>0.04</td><td>0.04</td><td>N/A</td><td>N/A</td></tr><tr><td>classification (%)</td><td>100</td><td>100</td><td>100</td><td>100</td><td>58.2</td></tr><tr><td>prediction (%)</td><td>53.4</td><td>58.1</td><td>60</td><td>38</td><td>49.8</td></tr><tr><td>total (%)</td><td>76.7</td><td>79.1</td><td>80</td><td>69</td><td>54</td></tr></table>

The parameters $\eta$ was set at 0.25, $\alpha$ was set at 0.9, and ecrit at 0.04. The multi-layered perceptron network for this data consisted of 15 input units, 10 hidden units in a hidden layer, and 5 output units corresponding to the five risk classification categories. The classification performance using probit was much lower than those using other (similarity-based learning or backpropagation) methods. Polytomous probit, which was used for this data set, classified all the examples to be in class 3 (there were 54 examples in class 3). Hence, the percent classification/prediction using probit is proportional to the number of examples belonging to class 3 which happened to be used in the training and testing sets respectively. This reason could be attributed to the poor performance of ID3 as compared to probit.

Individual classification/prediction results using loan evaluation data

<table><tr><td></td><td>SG</td><td>NR</td><td>SG-NR</td><td>ID3</td><td>PROBIT</td></tr><tr><td colspan="6">classification (%)</td></tr><tr><td>1</td><td>100</td><td>100</td><td>100</td><td>100</td><td>68</td></tr><tr><td>2</td><td>100</td><td>100</td><td>100</td><td>100</td><td>52</td></tr><tr><td>3</td><td>100</td><td>100</td><td>100</td><td>100</td><td>56</td></tr><tr><td>4</td><td>100</td><td>100</td><td>100</td><td>100</td><td>66</td></tr><tr><td>5</td><td>100</td><td>100</td><td>100</td><td>100</td><td>60</td></tr><tr><td>6</td><td>100</td><td>100</td><td>100</td><td>100</td><td>58</td></tr><tr><td>7</td><td>100</td><td>100</td><td>100</td><td>100</td><td>54</td></tr><tr><td>8</td><td>100</td><td>100</td><td>100</td><td>100</td><td>46</td></tr><tr><td>9</td><td>100</td><td>100</td><td>100</td><td>100</td><td>60</td></tr><tr><td>10</td><td>100</td><td>100</td><td>100</td><td>100</td><td>62</td></tr><tr><td colspan="6">prediction (%)</td></tr><tr><td>1</td><td>44</td><td>53</td><td>56</td><td>40</td><td>40</td></tr><tr><td>2</td><td>58</td><td>62</td><td>64</td><td>34</td><td>56</td></tr><tr><td>3</td><td>60</td><td>64</td><td>64</td><td>40</td><td>52</td></tr><tr><td>4</td><td>44</td><td>56</td><td>62</td><td>38</td><td>42</td></tr><tr><td>5</td><td>50</td><td>60</td><td>62</td><td>48</td><td>48</td></tr><tr><td>6</td><td>50</td><td>54</td><td>60</td><td>36</td><td>50</td></tr><tr><td>7</td><td>58</td><td>58</td><td>58</td><td>36</td><td>54</td></tr><tr><td>8</td><td>64</td><td>68</td><td>68</td><td>30</td><td>62</td></tr><tr><td>9</td><td>52</td><td>52</td><td>52</td><td>46</td><td>48</td></tr><tr><td>10</td><td>54</td><td>54</td><td>54</td><td>32</td><td>46</td></tr></table>

## 8. Review of results and conclusions

The modified back-propagation algorithms (NR and SG-NR) performed better than the regular back-propagation (SG) algorithm in terms of prediction accuracy and speed of convergence. This could be attributed to the increase in granularity of the search process by means of the exponential transformation of the objective function, and also due to the second-order gradient search procedure. The increase in granularity increases the step-size taken during search through the solution space, hence increasing the speed of convergence of NR algorithm. The second-order gradient search process in NR utilizes information about curvatures in the search space thus modifying the search process appropriately leading to faster convergence to the final value, whereas the SG method did not converge to the final solution. The SG algorithm had problems converging because once in the vicinity of the final solution the process started vacilating between a few values resulting in a movement further away from the final solution.

The SG-NR algorithm, due to its combination of NR and SG algorithms when they are at their best, performed the best overall even among the back-propagation algorithms. Becker and LeCun ([6]), Fahlman ([13]), Parker ([33]), and Waltrous ([41]), among others, have suggested the use of second-order gradient methods for accelerating the back-propagation procedure. However these methods rely on matrix inversion and thus are more costly computationally. The NR method uses an exponential objective function along with modifications to the SG algorithm avoiding matrix inversion at the same time taking advantage of second-order process, thus making the computation tasks in the learning process easier. Even while taking advantage of the benefits of a second-order method, the computational process was simplified, in NR and SG-NR, by avoiding matrix inversions in the process.

The back-propagation algorithm in a multilayered perceptron is versatile and can be used for learning ratios, continuous, as well as nominal variables with any number of classes resulting in lesser degradation in performance than inductive learning algorithms and probit. For continuous variables, ID3 has problems finding the best split at a node due to the problem of combinatorial explosion as the range of values that a continuous variable takes increases. Since the number of discriminant functions required increases with the number of classes, probit analysis becomes extremely difficult as the number of classes increases.

Once implemented (learning occurs), the process of prediction of newer examples is faster in back-propagation as compared to other methods since speed of prediction using back-propagation does not depend on the number of patterns that are stored in multi-layered perceptrons. Time required for prediction in multi-layered perceptrons is just the time required for activations to traverse from the input to the output nodes, which is negligible.

Overall, the back-propagation algorithms performed better than inductive learning algorithms and probit in terms of both prediction and classification accuracies. One of the advantages of using back-propagation in a multi-layered perceptron is that the network can be configured so as to increase the performance, which is not possible with inductive learning or probit. Also, incremental learning ability of back-propagation facilitates knowledge acquisition process where new knowledge can be added to the system as they are obtained.

One of the major problems with back-propagation algorithm is that it is very slow to converge. This could be remedied either by improving the algorithm itself and/or utilizing parallel computer architecture for faster processing. In this paper, we have attempted to improve the performance of the algorithm. Even with the improved learning procedure, the computation performances of multi-layered perceptrons in our study are still slow for three reasons – the computation is simulated using serial processing computers, it takes many iterations of adjustment by each unit before the whole network reaches equilibrium, and it takes a large number of searching steps to find the right set of connection weights. To speed up the training time parallel computers are necessary. Currently, there are VLSI implementations of neural-networks such as Intel's AK 107, Fujitsu's MB4442, NEC's UPD7281, among others, in addition to implementations in connection machines ([19], [43], [11]). Kung, Vlontos, and Hwang ([25]) describe a VLSI architecture for implementing multi-layered perceptrons using a programmable systolic array. Because of the parallel processing nature of neural-network computing, the use of parallel computers is necessary to take advantage of the inherent parallelism. Similar observations can be made of the information processing characteristics of human brain. Even though the individual neurons are slow, the brain processes information expeditiously through massive parallelism. Recent technological advances in VLSI and computer aided design have made it possible to build massively parallel computers, making the neural-network computing method described in this paper practical for commercial applications.

Probit is inefficient relative to back-propagation and inductive learning algorithms since it utilizes only one hyperplane to separate two classes, whereas the former two methods utilize as many hyper-planes as is necessary. In back-propagation using multi-layered perceptrons, the hidden layer aids in avoiding the problem of forming linear hyperplanes.

Both back-propagation and ID3 algorithms do not assume any distributions that the input data should possess, unlike probit. Since probit depends on the distribution of the input data for analyses, violation of the same could lead to gross inaccuracies in the results that are obtained.

Although Baum and Haussler ([5]) formulate a lower bound on the number of examples that are required for a given prediction accuracy, the small size of our data sets precluded us from applying the same in this study. Researchers ([2], [24]) have resorted to experimentation with different numbers of hidden units before resorting to final analysis. To this end, future research should be directed toward studying the number of hidden units that are both sufficient and feasible given a certain input-output data set.

## Acknowledgement

The authors wish to thank Professors Gary J. Koehler and Kar Yan Tam and three anonymous reviewers for their insightful comments on a previous draft of this paper. This project was supported in part by the Research Opportunities in International Business Information award from the KPMG Peat Marwick Foundation and by the Collaborative Research Grants of the NATO International Scientific Exchange Programme.

## References

[1] A.R. Abdel-Khalik and K.M. El-Sheshai, Information Choice and Utilization in an Experiment on Default Prediction, Journal of Accounting Research, Autumn (1980) 325–342.

[2] S. Ahmad, Scaling and Generalization in Neural Networks: A Case Study, in: D. Touretzky, G.E. Hinton, T.J. Sejnowski, Eds., Proceedings of the 1988 Connectionist Models Summer School, Palo Alto, CA: Morgan Kaufmann, 1988.

[3] J.A. Anderson, Neural Models with Cognitive Implications, in: Laberge and Samuels Eds., Basic Processes in Reading, Lawrence Erlbaum, Hillsdale, NJ 1977.

[4] R.B. Alterman, R.A. Avery, R.A. Eisenbeis and J.F. Sinkey, jr., Application of Classification Techniques in Business, Banking and Finance, Greenwich, CT: JAI Press 1981.

[5] E.B. Baum and D. Haussler, What Size Net Gives Valid Generalization, Neural Computation, 1 (1989) 151–160.

[6] S. Becker and Y. le Cun, Improving the Convergence of Back-Propagation Learning with Second Order Methods, Proceedings of the 1988 Connectionist Models Summer School, Pittsburgh (1988).

[7] H. Braun and J. Chandler, Predicting Stock Market Behavior through Rule Induction: An Application of the Learning-from-examples Approach, Decision Sciences (1987) 415–429.

[8] L. Breiman, J. Friedman, R. Olshen and C. Stone, Classification and Regression Trees, Monterey, CA: Wadsworth 1984.

[9] C. Carter and J. Cartlett, Assessing Credit Card Applications Using Machine Learning, IEEE Expert, Fall (1987) 71–79.

[10] I.S. Currim, R.J. Meyer and N.T. Le, Disaggregate Tree-Structured Modeling of Consumer Choice Data, Journal of Marketing Research, August (1988) 253–265.

[11] E. Deprit, Implementing Recurrent Back-Propagation on the Connection Machine, Neural Networks, 2 (1989) 295–314.

[12] S. Dutta and S. Shekhar, Bond Rating: A Non-conservative Application of Neural Networks, International Joint Conference on Neural Networks, Vol. II (1988) 443–450.

[13] S.E. Fahlman, Faster-Learning Variations on Back-Propagation: An Empirical Study, Proceedings of the 1988 Connectionist Models Summer School, Pittsburgh (1988).

[14] D.J. Finney, Probit Analysis, 3rd. edition, Cambridge University Press 1971.

[15] D.H. Fisher and K.B. McKusick, An Empirical Comparison of ID3 and Back-propagation, Proceedings of the

Eleventh International Joint Conference on Artificial Intelligence, Detroit, MI, August (1989).

[16] J. Gentry, P. Newbold and D. Whitford, Classifying Bankrupt Firms with Funds Flow Components, Journal of Accounting Research, 20, 1, Spring (1985) 146–160.

[17] J. Gentry, P. Newbold and D. Whitford, Predicting Industrial Bond Ratings with a Probit Model and Funds Flow Components, Financial Review (1988).

[18] P.E. Gill, W. Murray and M.H. Wright, Practical Optimization, Academic Press 1981.

[19] G.E. Hinton, Learning in Parallel Networks, BYTE, April (1985) 265–273.

[20] J.J. Hopfield and D. Tank, Computing with Neural Circuits: A Model, Science, 233 (1986) 624–633.

[21] K. Hornik, M. Stinchcombe and H. White, Multilayer Feedforward Networks are Universal Approximators, Neural Networks, 2 (1989) 359–366.

[22] G.J. Koehler and A. Majthay, Generalization of Quinlan's Induction Method, Technical Report, Department of Decision and Information Sciences, The University of Florida, Gainesville, FL., August 14 (1988).

[23] T. Kohonen, Self-Organization and Associative Memory, Springer-Verlag, Berlin 1984.

[24] S.Y. Kung and J.N. Hwang, An Algebraic Projection Analysis for Optimal Hidden Units Size and Learning Rates in Back-Propagation Learning, Proceedings of the IEEE International Conference on Neural Networks, July (1988).

[25] S.Y. Kung, J. Vlontzos and J.N. Hwang, VLSI Array Processors for Neural Network Simulation, Journal of Neural Network Computing, Spring (1990) 5–20.

[26] C.J. Matheus and W.E. Hohensee, Learning in Artificial Neural Systems, Computational Intelligence Journal, 3, 4 (1987).

[27] W.F. Messier, jr. and J.V. Hansen, Inducing Rules for Expert System Development: An Example Using Default and Bankruptcy Data, Management Science, 34, 12 (1988) 1403–1415.

[28] R.H. Michaelsen, An Expert System for Tax Planning, Expert Systems, October (1984) 149–167.

[29] R.S. Michalski, A Theory and Methodology of Inductive Learning, Artificial Intelligence, 20 (1983) 111–161.

[30] J. Mingers, Rule Induction with Statistical Data - A Comparison with Multiple Regression, Journal of Operations Research Society, 38, 4 (1987) 347-351.

[31] R. Mooney, J. Shavlik, G. Towell and A. Gove, An Experimental Comparison of Symbolic and Connectionist Learning Algorithms, Proceedings of the Eleventh International Joint Conference on Artificial Intelligence, August, Detroit, MI, (1989).

[32] Y.E., Orgler, A Credit Scoring Model for Commercial Loans, Journal of Money, Credit and Banking, 2, 4 (1970) 435–445.

[33] D.B. Parker, Optimal Algorithms for Adaptive Networks: Second Order Back-Propagation, Second Order Direct Propagation and Second Order Hebbian Learning, Proceedings of the IEEE International Conference on Neural Networks, San Diego (1987) 593–600.

[34] J.R. Quinlan, Induction of Decision Trees, Machine Learning, 1 (1986) 81–106.

[35] S.S. Rangwala and D.A. Dornfeld, Learning and Opti-

mization of Machining Operations using Computing Abilities of Neural Networks, IEEE Transactions on Systems, Man and Cybernetics, 19, 2 (1989) 199–214.

[36] D. Rumelhart, J.L. McClelland and the PDP Research Group, Parallel Distributed Processing – Explorations in the microstructure of Cognition, Volume I: Foundations The MIT Press, 1986.

[37] T.J. Sejnowski and C.M. Rosenberg, Parallel Networks that Learn to Pronounce English Text, Complex Systems, 1, 1 (1987) 145–168.

[38] M.J. Shaw and J. Gentry, Inductive Learning for Risk Classification, IEEE Expert, February (1990) 47–53.

[39] J.C. Singleton and A.J. Surkan, Modeling the Judgement of Bond Rating Agencies: Artificial Intelligence Applied to Finance, 1990 Midwest Finance Association Meetings, Chicago, IL, February, (1990).

[40] G.R. Walsh, Methods of Optimization, John Wiley, 1975.

[41] R.L. Watrous, Learning Algorithms for Connectionist Networks: Applied Gradient Methods of Nonlinear Optimization, Proceedings of the IEEE International Conference on Neural Networks, San Diego (1987) 619–627.

[42] S.M. Weiss and I. Kapouleas, An Empirical Comparison of Pattern Recognition, Neural Nets and Machine Learning Classification Methods, Proceedings of the Eleventh International Joint Conference on Artificial Intelligence, Detroit, MI, August (1989).

[43] X. Zhang, M. McKenna, J.P. Mesirov. and D. Waltz, An Efficient Implementation of the Backpropagation Algorithm on the Connection Machine CM-2, Technical Report, Thinking Machines Corporation, (August 29, 1989).

## Appendix-A: ID3 and NEWQ

The two inductive learning systems (ID3 and NEWQ) as well as probit are briefly discussed in this section.

ID3

ID3 (Quinlan, 1986) uses information-theoretic measures to generate a decision tree with the classifications at the leaf-nodes.

Let the number of classes in the instance space of interest be $C(C_{1}, C_{2}, \ldots, C_{c})$ . At any given node, the expected information that is required to classify the instances at that node as belonging to class $C_{i}$ or otherwise is given by

$$
\begin{array}{r l} I (p, n) & = - \frac {p}{(p + n)} * \log_ {2} \left[ \frac {p}{(p + n)} \right] \\ & - \frac {n}{(p + n)} * \log_ {2} \left[ \frac {n}{(n + p)} \right], \end{array}
$$

where p is the proportion of the instances at that node that belong to class $C_{i}$ and $n (=1-p)$ is the proportion of instances at that node that do not belong to class $C_{i}$ .

Let the attributes in the instance space be $A_{j}$ ( $j = 1 \ldots m$ ) where each of the attributes take on $V_{j}$ values. At a given node let the number of instances that take on the different values for $A_{j}$ for class $C_{i}$ be $p_{i}$ and let $n_{i} = 1 - p_{i}$ . The expected information required for that branch of the tree with $A_{j}$ as the root node is

$$
E (A _ {j}) = \sum_ {i} \frac {(p _ {i} + n _ {i})}{(p + n)} * I (p _ {i}, n _ {i}),
$$

a weighted average of the proportion of instances that are present at the node of interest. The information that is gained by branching on $A_{j}$ is

$$
\operatorname{gain} \left(A _ {j}\right) = I (p, n) - E \left(A _ {j}\right).
$$

The attribute which gains the most information at a node is chosen as the one based on which the branching is performed. The process is used recursively at each node of the tree until all the terminal nodes (leaves) are reached.

## NEWQ

NEWQ (Koehler and Majthay, 1988) uses discriminant analysis procedures to produce a decision tree in which a discriminant function (Fisher, 1936) is used at each node for splitting.

Let w be a n-dimensional vector (corresponding to n attributes), and z be a scalar (class value). For w non-zero, (w, z) defines a hyper-plane $\{x: w' x = z\}$ .

The algorithm begins by generating a hyperplane (w, z) that strictly separates at least one point from the remaining points in the example set (T). For a 2-class problem, a hyper-plane is used to partition T into $\{x: w'x < z, x \in T\}$ and $\{x: w'x \geq z, x \in T\}$ . A new rule is created which augments the old rule set and NEWQ is recursively called with each resulting partition. The reader is referred to Koehler and Majthay (1988) for an elaborate discussion of the NEWQ algorithm.

## Appendix-B

## Abdel-Khalik and El-Sheshai (1980) data

Abdel-Khalik and El-Sheshai (1980) had previously used this data set to classify a set of firms into those that would default and those that wouldn't default on loan payments. This data set has 32 examples, for training, of which 16 belong to the default class and the other 16 examples belong to the non-default class and 16 examples for testing, all of which belong to the non-default class. The 18 attributes in the example set are: (1) Net income/total assets, (2) Net income/sales, (3) Total debt/total assets, (4) Cash flow/total debt, (5) long-term debt/net worth, (6) Current assets/current liabilities, (7) Quick assets/sales, (8) Quick assets/current liabilities, (9) Working capital/sales, (10) Current year equity/total debt, (11) Sales trend, (12) Earnings trend, (13) Current ratio trend, (14) Working capital/sales trend, (15) Cash flow/total debt trend, (16) Long-term debt/net worth trend, (17) Net income/total assets trend and (18) Net income/sales trend.

## Loan evaluation data

The loan evaluation data set was used to classify the riskiness involved with firms' abilities to pay back loan. The riskiness is rated from 1 (very risky) to 5 (safe), which form the 5 classes in the study using this data set. There are 15 variables – 12 continuous and 3 nominal – total net flow/total assets, operations, accounts receivable, inv, othca, accounts payable, othcl, otha&1, financial, fcexp, invest, dividend and three nominal variables guarantee, collateral and secured. There are 100 examples in this data set with 5 classes.

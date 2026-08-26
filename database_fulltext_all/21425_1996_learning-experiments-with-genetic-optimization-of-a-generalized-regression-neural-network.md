---
otero_id: 21425
otero_key: "M827B4JF"
title: "Learning experiments with genetic optimization of a generalized regression neural network"
authors: "James V. Hansen; Rayman D. Meservy"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(96)80007-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Learning experiments with genetic optimization of a generalized regression neural network

James V. Hansen $^{*}$ , Rayman D. Meservy

Marriott School of Management, Brigham Young University, 540 N. Eldon Tanner Building, P.O. Box 23068, Provo, UT 84602-3068, USA

## Abstract

This paper reports a study unifying optimization by genetic algorithm with a generalized regression neural network. Experiments compare hill-climbing optimization with that of a genetic algorithm, both in conjunction with a generalized regression neural network. Controlled data with nine independent variables are used in combination with conjunctive and compensatory decision forms, having zero percent and 10 percent noise levels. Results consistently favor the GRNN unified with the genetic algorithm.

Keywords: Genetic algorithm; Generalized regression neural network; Radial basis function

## 1. Introduction

This paper contributes to the literature on unification of artificial intelligence with optimization methods by demonstrating the use of a genetic algorithm to optimize the smoothing parameter used in a generalized regression neural network. Our study is similar in spirit to that of Kim and Lee [15], who unify a neural network with an optimization model in order to make it adaptive to changing information. Within the unified programming taxonomy, our study can be classified as an experimental application.

We first outline the structure and process of our model. We then report results from experiments on conjunctive, compensatory, and mixed learning structures having zero and 10 percent classification noise. The results show that the incorporation of a genetic algorithm generates models that perform significantly better than those produced by traditional hill-climbing optimization methods.

By way of motivation, a neural network (NN) is characterized by an architecture in which operations are distributed among many relatively simple processors. NNs have been applied to such diverse areas as pattern classification, function approximation, optimization, prediction, and automatic control. (For a survey of applications, see Kemsley et al. [14].) While such applications have led to the proliferation of NN variants, such as backpropagation networks, recurrent networks, probabilistic networks, and others, all NNs perform essentially the same function: they accept a vector of inputs and produce an output vector through a process of vector mapping.

The most widely applied NN to decision problems is the backpropagation network (BP) [14]. Perhaps the reason for this is that with just two hidden layers of computational units, arbitrarily complex problems can be solved - at least in theory [18]. Consequently, a BP network can be a strong candidate for learning functions of interest.

There are some limitations, however. BP and its variations can be slow in yielding problem solutions and are susceptible to training obstacles such as local minima and failure to converge. Apart from these algorithmic limitations, results can be unsatisfactory because of insufficient training on an insufficient number of hidden neurons, or an attempt to learn a function that is not deterministic. The latter condition can impede the performance of other machine-learning methods, as well.

As an alternative, so-called radial basis function (RBF) NNs are attracting interest because of their ability to train rapidly while yielding robust results. It has been proved that with sufficient hidden layer neurons, RBFs can approximate functions with arbitrary accuracy [24]. Specht [21] has recently developed a radial-basis NN called a Generalized Regression Neural Network (GRNN) that can approximate any arbitrary function between input and output vectors. The function estimate is computed directly from the training data.

To recapitulate, in this paper we report on an experiment that unifies a genetic algorithm (GA) with a GRNN. In particular, we use a GA to optimize the smoothing factor used to find the optimal regression surface of the GRNN. We show comparative performance on several sets of problems that present learning data in conjunctive, compensatory, and mixed forms.

The paper proceeds as follows: Section 2 outlines the architecture and procedures of the GRNN. In Section 3 we present the fundamentals of the GA that is used in conjunction with the GRNN. In Section 4 we describe the structure of the decision problems that are used to test performance. Section 5 describes an empirical test of comparative performance. Section 6 discusses the results, and Section 7 is a brief summary.

## 2. GRNN structure

GRNN is based on the following formulation and parameters from statistics:

$$
\operatorname{E} [ y | x ] = \int y f (x, y) \mathrm{d} y / \int f (x, y) \mathrm{d} y
$$

GRNN Architecture -- XOR Problem  
![](/api/attachments/M827B4JF/fulltext/images/0269b41a91eadda21a80c561537119707f8d12b7f6dc6c11d5384d9528052840.jpg)  
Fig. 1. GRNN architecture: XOR problem.

where y is output of the estimator, x is the estimator input vector, $E(y|x)$ is the expected value of output, given the input vector x, $f(x,y)$ is the joint probability density function of x and y.

GRNN estimates $f(x, y)$ from the set of training data and optimally estimates $y_{j}$ as

$$
y _ {j} = \sum_ {i} h _ {i} o _ {i j} / \sum_ {i} h _ {i}
$$

where $o_{ij}$ is the target output corresponding to input pattern $x_{i}$ and output j, $h_{i} = \exp[-D_{i}^{2}/2\sigma^{2}]$ , the output of pattern unit i, $D_{i}^{2} = (x - w_{i})^{\mathrm{T}}(x - w_{i})$ , the squared distance between the input pattern x and the weight vector w, x is an input pattern, $w_{i}$ is the weight vector for pattern unit i, $\sigma$ is a smoothing constant that controls the size of the receptive region, the field over which the output has a significant response to input x.

The GRNN architecture is comprised of four layers as illustrated in Fig. 1. One hidden-layer unit is created for each input pattern, and its corresponding input vector is stored there in the form of a weight vector w. These vectors are shown on the arcs between the input units and the hidden-layer units. Fig. 1 shows four input patterns, or vectors, for the XOR problem, resulting in the creation of four hidden-layer units. The input units are fully connected to the hidden layers, thereby distributing a complete input pattern to each of the hidden layer's computational units.

Each hidden-layer unit i computes $h_{i}$ as its activation function. Then the product of $h_{i}$ times $o_{ij}$ (j=1 in our example and is suppressed) is summed over all i, with the result being divided by the summation over i of $h_{i}$ , as shown in Fig. 1. We have not computed values for the output vectors, since they depend on the choice of $\sigma$ .

The GRNN explicitly recognizes the close relationship between feed-forward neural networks like BP and stochastic multiple regression [27]. Specht [21] has shown that the GRNN converges to an optimal regression surface. An important advantage over standard nonlinear multiple regression is that no hypothesized model need be specified in advance. All that is required is a data set of dependent and independent variables. When the GRNN performs well, it does so efficiently, since it requires only one pass through the network structure. We earlier conducted tests of GRNN compared to BP with varying numbers of hidden layers and found that the time requirements of the GRNN were less by as much as an order of magnitude.

A critical consideration in the effectiveness of GRNN is the determination of an optimal value for $\sigma$ . As $\sigma$ becomes very large GRNN output approaches the mean of the training set outputs; and as $\sigma$ becomes very small GRNN output approaches the output pattern of the training set, which may not generalize well. Intermediate values typically result in the best generalization.

An approach that has been suggested for finding a suitable $\sigma$ is as follows: Build the network using all but one sample from the training set of size n and an assign an arbitrary value for $\sigma$ . Apply the resulting GRNN to the holdout sample and record the error. Repeat this procedure n times and compute the mean squared error. Change the value of $\sigma$ and repeat the procedure. If the mean squared error increases, change the value of $\sigma$ in the other direction and repeat. If the mean squared error decreases, increment the value of $\sigma$ in the same direction. If $\sigma$ changes only minutely, select the current value of $\sigma$ . [1].

Hill-climbing methods such as these can be effective and they are commonly used, but they are subject to being caught in local minima, as well as producing false minima. A hill-climbing approach was used here as the method of comparison with a GA in seeking optimal values of $\sigma$ .

## 3. Genetic algorithm

GAs have become increasingly popular in recent years as a method for solving complex search problems in a large number of different disciplines. There is a growing recognition that GAs have a close relationship with neural networks. This has resulted in significant efforts to unify these techniques in a system where each compliments the other (cf. [10]). Future applications may be expected in which the techniques are seamlessly integrated into systems [24].

Since many readers will be familiar with GAs, we will only cover the rudiments here, along with the special elements of our application.

A GA is a probabilistic search method due to Holland [11] that is based on the concept of adaptive efficiency in natural organisms. In nature, the members of a species that are best suited to the environment are likely to survive and produce offspring. Since the offspring are likely to inherit these survival traits, the succeeding generation will contain more fit individuals. If the environment can only support a limited population then the standards of fitness rise and each successive generation should contain better individuals.

In like manner, a GA commences with a set of initial possible structures $\{p_{i}\}$ , which are bit strings of length L. The bit strings represent values for variables that are relevant to solving a problem of interest. These constitute the initial population $(P(0))$ . A second generation population $(P(1))$ is determined from the first population by survival of members of $P(0)$ combined with crossover mating, inversion, and random mutations.

Selection of surviving members from $P(t)$ is determined randomly according to member fitness as determined by their relative performance in achieving a prespecified goal. The higher the member fitness, the more likely is its selection. In optimization problems, fitness is determined from the objective function.

Our genetic algorithm seeks to Minimize $\pi(\sigma) =$ the average squared $e$ on predicting repeated holdout samples, subject to $\sigma\in[0.01,6]$ .

We use the general algorithm described in Koehler [16], with modifications outlined as follows:

## BEGIN

(1) Randomly generate an initial population, $P(0)$ , of $k$ structures, $p_i$ , $i = 1, \ldots, k$ . These structures, or chromosomes, are strings that are 16 bits long. We treat this as a continuous chromosome, in that it allows 65,536 values over the range of values for $\sigma \in [0.01, 6]$ . This range was selected based on prior work on selecting optimal values of $\sigma$ [20]. The decoding transformation is given by

$$
D (s) = 0. 0 1 + d (s) / 2 ^ {1 6} (1 0 - 0. 0 1)
$$

where $d(s)$ is the ordinary decimal representation of the 16-bit binary string $s$ . For example, the decimal representation of 0000000000001111 is 15, so $D(0000000000001111) \approx 0.0123$ . The two endpoints are $D(0000000000000000) = 0.01$ and $D(1111111111111111) = 6$ , as expected.

(We selected a gene pool size of 100 (k) chromosomes for each iteration. This was based on prior work by the authors examining the trade-off between computation time and the need for diversity in the gene pool.)

(2) For each $p_{i}$ in $P(0)$ , input the value to GRNN as a trial $\sigma$ and save its performance measure, $\pi$ .

(3) Set the stopping criterion as 20 iterations beyond the last minimal average error without improvement.

(4) WHILE stopping criterion is not satisfied DO

BEGIN

For each $p_i$ in $P(t)$ , compute its selection probability, as

$$
\operatorname{Prob} \left(p _ {i}\right) = \pi \left(p _ {i}\right) / \sum_ {j = 1} ^ {k} \pi (P j);
$$

Generate the next population, $P(t+1)$ by selecting structures from $P(t)$ with replacement by means of the selection probability distribution and applying genetic operators to them;

For each $p_i$ in $P(t+1)$ , compute and save $\pi(p_i)$ ;  
END;

END;

To gain insight into the search strategy behavior, consider the selection probability, $\text{Prob}(p_{i})$ . If k structures from $P(t)$ are selected to participate in the generation of new elements for $P(t+1)$ , the expected number of new elements to be derived from any given structure in the current set $(P(t))$ is

$$
\begin{array}{r l} & k * \pi (p _ {i} (t)) / \sum_ {j = 1} ^ {k} \pi (p _ {i} (t)) \\ & \quad = \pi (p _ {i} (t)) / (1 / k) \sum_ {j = 1} ^ {k} \pi (p _ {i} (t)) \\ & \quad = \pi (p _ {i} (t)) / \overline {{\pi}} (P (t)), \end{array}\tag{1}
$$

where $\overline{\pi}$ represents the average fitness of its argument. This means that structures exhibiting average performance will produce one offspring, structures having above average performance will tend to produce more than one, and structures having below average performance will tend to produce none. Consequently, the probabilities invoke a selective bias in favor of above-average performing elements,

By itself, this selective bias will cause the best-performing element in the initial set to occupy a growing proportion of the knowledge set over time. This is not sufficient, however, since simply propagating the best elements through succeeding generations of populations does little to improve the search for better-performing sets. Genetic search operators overcome this limitation by transforming the most promising structures as measured by (1) into new, untested structures. The genetic-search operators perform transformations on the best-performing structures that exhibit highly parallel effects.

## 4. Learning decision problems

The performance of various machine learning strategies may be influenced by differences in decision characteristics. Some of these characteristics include the decision strategy, complexity, and noise [13]. Since machine learning algorithms vary considerably in how they learn from the data, some algorithms will perform better when presented with a particular decision characteristic than will other algorithms.

Decision strategies are often represented in the form of compensatory or noncompensatory models. In the model representation, the decision is portrayed as a result of considering all available information in a single global judgement. Compensatory models are typical of those used in regression studies. Regression studies usually represent the decision process as a linear additive regression model of the form

$$
Y = a + b _ {1} X _ {1} + b _ {2} X _ {2} + \dots + b _ {k} X _ {k} + \epsilon .
$$

This represents a type of compensatory model, where the high score of one attribute offsets the low score of another. The degree of offset is determined by the relative weights $(b_{i})$ placed on the attributes $(X_{i})$ . This process of trading off attributes has been found to be integral to many day-to-day decisions such as selecting a home or automobile [6,7,17]. The strength of traditional statistical methods that use compensatory models is their robustness or effectiveness across a wide variety of problem conditions [4]. However, most traditional statistical methods assume continuous tradeoffs among attributes, a distribution which frequently does not hold among real-world problems [2] and often results in serious errors [3,12,23].

In noncompensatory models, the high score of one attribute cannot compensate for the low score of another. One type of noncompensatory model often found in the literature is conjunctive [6]. Conjunctive models involve multiple cutoffs, requiring that some minimal level of performance be achieved or exceeded by all variables

$$
X _ {i} > X _ {c} \quad \text { for } \quad \text { all   } i.
$$

This results in a choice that is actually based on the level of the worst attribute. Many police academies use this model for minimum physical admittance standards. No matter how strong or able a person is, if he has a bad knee, that person will not be admitted. Previous research suggests that conjunctive models are used to prescreen alternatives [17]. Research also suggests that many decisions are made using a combination of these models, such as conjunctive for prescreening and compensatory for final choices [19].

## 5. Experimental design

To investigate how decision strategy affects GRNN with hill-climbing methods of finding $\sigma$ , and GRNN with GA methods of determining $\sigma$ , a simulation with controlled data was used. Data were created for each of the above-described decision strategies: compensatory, conjunctive, and mixed.

Compensatory data for a given decision consisted of randomly generated attributes of the following form:

$$
\text { decision } = \left\{ \begin{array}{l l} \text { true } & \text { if } (X _ {1} + X _ {2} + \dots + X _ {n}) / n \leq t _ {1}, \\ \text { false } & \text { otherwise }. \end{array} \right.
$$

If the average of all attributes was less than some constant then the appropriate decision is set to true, otherwise to false.

Conjunctive decision data required generating random data that matched the following decision:

$$
\text { decision } = \left\{ \begin{array}{l l} \text { true } & \text { if } (X _ {1} \leq t _ {2}) \\ & \text { and } (X _ {2} \leq t _ {2}) \text { and } \dots (X _ {n} \leq t _ {2}), \\ \text { false } & \text { otherwise }. \end{array} \right.
$$

If each attribute is less than some constant then the appropriate decision is set to true, otherwise false.

Mixed decision data involved generating data such that for each set of attributes

$$
\text { decision } = \left\{ \begin{array}{l l} \text { true } & \text { if   } ((X _ {1} \leq t _ {3}) \\ & \text { and   } (X _ {2} + X _ {3} + \ldots + X _ {n}) / n \leq t _ {4}), \\ \text { false } & \text { otherwise. } \end{array} \right.
$$

The decision is true if the first attribute is less than some constant $t_{3}$ and the average of the rest of the attributes are less than constant $t_{4}$ .

## 5.1. Noise

Real-world data may contain varying degrees of noise. Noise may occur in the attributes (attribute noise) or in the class labels (classification noise). When noise is present, constructing models that cover all the training set may produce an idiosyncratic decision structure that can perform poorly on unseen problem instances. It follows that models for practical use should exhibit some tolerance for noise.

While attribute noise is of interest, in a comprehensive experimental study of learning from noisy data, Quinlan [20] found that classification noise was more significant than attribute noise. We, therefore, limited our study to classification noise.

Classification noise was introduced into the simulation data by changing the decision of any alternative in the set with a probability of 10 percent. This represents a severe form of error since similar attribute patterns may now be associated with opposite classification labels [9].

## 5.2.Data

Data for the simulation was provided by four tables, where each X was a randomly generated number between 0 and 99. A decision was then determined for each row of the table based on decision strategy. Each table contained 100 examples (50 true and 50 false) in random order.

For decision strategy the following values were used: $t_{1}$ was 50; $t_{2}$ was 7; with $t_{3}$ and $t_{4}$ equal to 60. The population for each data set generated (6 data sets in all) was 100 examples. Setting $t_{i}$ allowed exactly 50 true decisions and 50 false decisions (after several tries) to be generated for each data set without restricting X. A selected level of noise was then introduced into the data randomly switching the selected choice on 0% or 10% of the rows.

## 5.3. Estimating error rates

Weiss and Kapouleas [25] distinguish between apparent error rates and true error rates. Apparent error rates are the result of testing a model on the data used to train that model. Apparent error rates are not often used by researchers, as they can result from an overfitting of the model to the data in the training set. If the training set is not a fair representation of the problem domain's universe, the resulting error rates can be misleading.

True error rates are nearly always the objective of empirical research of the type presented here. Researchers seek to discover the representative power of a set of sample data, as revealed in a model that is trained on that data. The simplest technique for estimating error rates is the single train-and-test experiment. The sample cases are randomly assigned to a training set or to a test set. A model is developed from the training set, and the error estimate is determined by testing the model's performance on the test set.

While the single train-and-test method is economical, it has been shown that nearly 1000 test cases are required to be assured (95 percent confidence level) that the estimated error rate is nearly equal to the true error rate. Few studies have the luxury of this number of test cases. It is more common to find less than 100 cases available for training and testing.

A more reliable approach is to use a resampling method, such as k-fold cross-validation or bootstrapping. In our test, we used the special case of the k-fold cross-validation method with k=10. With 100 test cases, 10 repetitions are used. In each repetition 90 cases are used for the training set, and 10 cases are used as a holdout set for testing. Holdout sets are selected so that their union over all repetitions is the entire training set. In this way every case is guaranteed to participate in training and testing the GRNN. The resulting error estimate provides a reliable estimate of the true error rate [26]. and every case is used as a test case as well. Further details on this and alternative methods can be found in [5].

## 6. Results and discussion

Table 1 shows results for GRNN with hill-climbing optimization of $\sigma$ , and GRNN with genetic optimization of $\sigma$ . The GA method of optimizing $\sigma$ shows average accuracy rates for holdout samples equal to or better than hill-climbing in every case. Are these differences significant? Weiss and Kulikowski [26] have suggested the following method of estimating whether the average error between two competing models is significant.

Step 1. Compute the standard error for each model as follows:

$$
S E = \left(E (1 - E) / n\right) ^ {1 / 2}.
$$

where SE is standard error, E is the average sampling error, n is the total number of patterns in the training set.

Step 2. If the average error for the two models on the holdout samples differs by more than one SE, go to Step 3. Otherwise choose the model that is simplest.

Step 3. Choose the model with the lowest SE.

For our models (see Table 1), the evidence is consistent that GRNN with the unification of GA performs better than hill-climbing in terms of generalizing the resulting network to problems that it has not seen in training.

This has not been a universal finding, however. Tanese [22] found that hill-climbing outperformed GA on maximizing Walsh polynomials, which have been used in some GA research because of their regularities. The key point in deciding whether or not to use GAs for a particular problem centers around the question: what is the space to be searched? If that space is well understood and contains structure that can be exploited by special-purpose search techniques, the use of GAs is often computationally less efficient. This seems to be true of Walsh polynomials. If the space to be searched is not so well understood and relatively unstructured, and if an effective GA representation of that space can be developed, then GAs provide a surprisingly powerful search heuristic for large, complex spaces.

By way of intuitive argument for this claim, a population of structures can be thought of as points in an L-dimensional space defined by the L string positions of the structures. The genetic algorithms perform the search for better structures by focusing on hyperplanes in this space that are associated with good performance. In particular, a point in the L-dimensional space is specified by assigning values to the L string positions. An rth-order hyperplane $(0 \leq r \leq L)$ is defined as a $(L - r)$ -dimensional subspace and is specified by assigning values to only r of the L string positions. A single structure in the population is an instance of $2^{L}$ distinct hyperplanes $(\sum_{r}[\frac{L}{k}]T)$ . Consequently, the performance measure for $p_{i}$ provides information about all of its related $2^{L}$ hyperplanes.

If we let $S_{j}(t)$ denote the subset of structures in $P(t)$ that lie in hyperplane j at time t, and let $s_{j}(t)=|S_{j}(t)|$ . By the previously defined selection probabilities, the expected number of offspring produced by structures in $S_{j}(t)$ is

$$
s _ {j} (t) * \pi \left(S _ {j} (t) / \pi (P (t))\right).
$$

Then, if the resulting offspring lie in hyperplane j, we havemeaning that instances of a given hyperplane in the population increase (decrease) at a rate proportional to its performance with respect to the rest of $P(t)$ . Holland [11] has shown that this sampling rate rapidly approaches the optimal strategy for allocating trials to sample points with respect to the observed best in an unknown, but well defined space.

In our set of experiments, the global optimum for $\sigma$ is not known, so we are unable to determine the nearness-to-optimum of hill-climbing and GA solutions. In some cases, hill-climbing and GA produced the same solution; but on average the superior results of the GA/GRNN models suggest that the hill-climbing method encounters local minima from which it cannot escape.

In our experiments, both hill-climbing and GA methods converged to the same value of $\sigma$ about one-third of the time, suggesting that local minima are prevalent. This was not unexpected, since Gori and Tesi [8] have shown that local minima arise easily, even in simple problems. When hill-climbing and GA methods did not converge to the same value of $\sigma$ , we re-ran the GA algorithm with the hill-climbing value of $\sigma$ ( $\sigma_{\mathrm{HC}}$ ) to see if the GA would converge to it. In every case, the value of $\sigma$ moved away from $\sigma_{\mathrm{HC}}$ to the value of $\sigma$ that it had originally computed ( $\sigma_{\mathrm{GA}}$ ).

Effectiveness of GA and HC

<table><tr><td colspan="7">Methods of finding σ</td></tr><tr><td rowspan="2">Strategy</td><td rowspan="2">Noise %</td><td colspan="2">Optimization method: Resulting average error</td><td rowspan="2">Difference in average error</td><td colspan="2">SE evaluation</td></tr><tr><td>GA</td><td>HC</td><td>SE</td><td>Preferred method</td></tr><tr><td>Conjunctive</td><td>0</td><td>0.32</td><td>0.38</td><td>0.06</td><td>0.046</td><td>GA</td></tr><tr><td>Conjunctive</td><td>10</td><td>0.38</td><td>0.56</td><td>0.18</td><td>0.048</td><td>GA</td></tr><tr><td>Compensatory</td><td>0</td><td>0.16</td><td>0.26</td><td>0.10</td><td>0.037</td><td>GA</td></tr><tr><td>Compensatory</td><td>10</td><td>0.52</td><td>0.53</td><td>0.01</td><td>0.050</td><td>-</td></tr><tr><td>Mixed</td><td>0</td><td>0.02</td><td>0.19</td><td>0.17</td><td>0.014</td><td>GA</td></tr><tr><td>Mixed</td><td>10</td><td>0.25</td><td>0.46</td><td>0.21</td><td>0.043</td><td>GA</td></tr></table>

We also reversed the process, re-running GRNN with hill-climbing computation of $\sigma$ , with $\sigma_{GA}$ entered as an initial value. Typically, there was no movement away from that value. In about 10 percent of the cases, a new value for $\sigma_{HC}$ resulted. This seems to suggest that the GA may have produced a good, but not optimal $\sigma$ , and that the hill-climbing method is able to find improvement nearby.

## 7. Concluding remarks

GAs offer a robustness in searching for optima that may have advantages over more traditional methods, at least for ill-defined search spaces. An exciting possibility that is already the subject of research is the unifying of GAs with NNs to achieve machine learning power that cannot be accomplished by either paradigm alone. Most current research in this area has focused on the use of GAs to determine optimal architectures or weights for multilayer feedforward networks (cf. [24]).

In this paper, we have experimented with unifying GA with GRNN - in which the architecture is fixed. The principal problem in GRNN is finding the best smoothing factor. Our experiments showed relatively good performance for the GA, although the introduction of noise resulted in diminished performance, as is expected [13].

Our results are a first approximation, and there are many potentially fruitful avenues of research to pursue. Among these are testing of different levels of noise with varying levels of complexity, as measured by the number of descriptive attributes.

## References

[1] M. Caudill, GRNN and bear it, AI Expert (May 1993) 28–33.

[2] P. Cohen and E. Feigenbaum, Handbook of Artificial Intelligence, Vol. II (Morgan-Kaufmann, 1982).

[3] D. Curry, J. Louviere, and M. Augustine, On the sensitivity of brand-choice simulations to attribute importance weights, Decision Sciences, 12 (1981) 502–516.

[4] R. Dawes, The robust beauty of improper linear models in decision making, American Psychologist, 34 (1979) 571–582.

[5] B. Efron, Estimating the error rate of a prediction rule, Journal of the American Statistical Association, 78 (1983) 316–333.

[6] H. Einhorn, The use of nonlinear, noncompensatory models in decision making, Psychological Bulletin, 73 (1970) 221-230.

[7] H. Einhorn, D. Kleinmuntz, and B. Kleinmuntz, Linear regression and process tracing models of judgement, Psychological Review, 86 (1979) 465–485.

[8] M. Gori and A. Tesi, Some examples of local minima during learning with back-propagation, Proceedings of the Third Italian Workshop on Parallel Architectures and Neural Networks (1990).

[9] D. Greene, R. Meservy, and S. Smith, Learning Audit Selection Rules from Data: A Genetic Algorithms Approach, In: D. O'Leary and P. Watkins, Eds., Expert Systems in Finance (Amsterdam, Elsevier Science Publishers, 1992).

[10] M. Hassoun, Fundamentals of Artificial Neural Networks (Cambridge MA, MIT Press, 1995).

[11] J. Holland, Adaptation in Natural and Artificial Systems (Ann Arbor MI, University of Michigan Press, 1992).

[12] E. Johnson, R. Meyer, and S. Ghose, When choice models fail: Compensatory models in efficient sets, Working paper (Pittsburgh PA, Graduate School of Industrial Administration, Carnegie Mellon University, 1985).

[13] M. Kearns and U. Vazirani, An Introduction to Computational Learning Theory (Cambridge MA, MIT Press, 1994).

[14] D. Kemsley, T. Martinez, and D. Campbell, A survey of neural network research and fielded applications, Journal of Neural Networks 2 (1991) 123–133.

[15] W. Kim and J. Lee, UNIK-OPT/NN: Neural network based adaptive optimal controller on the optimization models, Decision Support Systems, forthcoming (1995).

[16] G. Koehler, Linear discriminant functions determined by genetic search, ORSA Journal on Computing, 3 (1991) 345-357.

[17] R. Libby, Accounting and Human Information Processing: Theory and Applications (Englewood Cliffs NJ, Prenctice-Hall, 1981).

[18] T. Masters, Practical Neural Network Recipes in C++ (New York, Academic Press, 1994).

[19] J. Payne, Task complexity and contingent processing in decision making: An information search and protocol analysis, Organizational Behavior and Human Performance, 16 (1994) 366–387.

[20] J. Quinlan, The effect of noise on concept learning, Machine Learning II (1986).

[21] D. Specht, A generalized regression neural network, IEEE Transactions on Neural Networks, 2 (1991) 568–576.

[22] R. Tanese, Distributed genetic algorithms for function optimization, Ph.D thesis (Ann Arbor MI, The University of Michigan, 1989).

[23] L. Valiant, Learning disjunctions of conjunctions, Proceedings of the Ninth International Joint Conference on Artificial Intelligence (1985).

[24] P. Wasserman, Advanced Methods in Neural Computing (New York, Van Nostrand Reinhold, 1993).

[25] S. Weiss and I. Kapouleas, An empirical comparison of pattern recognition, neural nets, and machine-learning classification methods, Proceedings of the International Joint Conference on Artificial Intelligence (1989).

[26] S. Weiss and C. Kulikowski, Computer Systems That Learn (San Mateo CA, Morgan-Kaufmann Publishers, 1991).

[27] H. White, Learning in artificial neural networks: A statistical perspective, Neural Computation, 1 (1989) 425–464.

![](/api/attachments/M827B4JF/fulltext/images/2fde8553c431243e828f4a0e4960cde3aaf3b0b79b661e78d4aeb958629e97e8.jpg)

James Hansen is with the Information Systems Group of the Marriot School of Management at Brigham Young University, where he holds the William F. Edwards Professorship. Professor Hansen received his Ph.D from the University of Washington, Seattle. He was formerly on the faculty at Indiana University and a research scientist at Battelle Institute. He is a member of INFORMS, the IEEE Society for Computing, ACM, AAAI and is currently serving on the editorial

board of Intelligent Systems in Accounting, Finance and Management. His research interests are in mathematical models of learning and distributed artificial intelligence.

![](/api/attachments/M827B4JF/fulltext/images/0b5cc231d9e653ea8f2a3d7b738ac55b516909fec011ca85d6a82734f7d93034.jpg)

Rayman Meservy received his Ph.D from the University of Minnesota and is currently on the faculty of the Marriott School of Management at Brigham Young University. Prior to coming to Brigham Young University, Professor Meservy taught at Carnegie-Mellon University. He has also had work experience as an internal auditor and as an entrepreneur, starting and developing a small business. Professor Meservy's research has centered on applying artifi-

cial intelligence methods to judgement and decision-making problems. His research has been published in numerous journals and several books. He is currently serving as Chair of the IS/MAS Section of the American Accounting Association.

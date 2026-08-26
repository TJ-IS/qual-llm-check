---
otero_id: 8410
otero_key: "BWHX3Z5A"
title: "Automatic trading method based on piecewise aggregate approximation and multi-swarm of improved self-adaptive particle swarm optimization with validation"
authors: "Rodrigo C. Brasileiro; Victor L.F. Souza; Adriano L.I. Oliveira"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.10.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Automatic trading method based on piecewise aggregate approximation and multi-swarm of improved self-adaptive particle swarm optimization with validation

Rodrigo C. Brasileiro, Victor L.F. Souza, Adriano L.I. Oliveira\*

Universidade Federal de Pernambuco, Centro de Informática, Av. Jornalista Aníbal Fernandes, s/n, Recife 50740-560, PE, Brazi

A R T I C L E I N F O

Article history: Received 18 January 2017 Received in revised form 11 October 2017 Accepted 12 October 2017 Available online xxxx

Keywords: Multi-swarm optimization Pattern discovery Data mining Time series representation Stock market Particle swarm optimization

## A B S T R A C T

Financial time series represent the stock prices over time and exhibit behavior similar to a data stream. Many works report on the use of data mining techniques to predict the future direction of stock prices and to discover patterns in the time series data to provide decision support for trading operations. Traditional optimization methods do not take into account the possibility that the function to be optimized, namely, the final financial balance for operations considering some stock, may have multiple peaks, i.e., be represented by multimodal functions. However, multimodality is a known feature of real-world financial time series optimization problems. To deal with this issue, this article proposes the PAA-MS-IDPSO-V approach (Piecewise Aggregate Approximation - Multi-Swarm of Improved Self-adaptive Particle Swarm Optimization with Validation). The proposed method aims to find patterns in financial time series to support investment decisions. The approach uses multi-swarms to obtain a better particle initialization for the final optimization phase since it aims to tackle multimodal problems. Furthermore, it uses a validation set with early stopping to avoid overfitting. The patterns discovered by the method are used together with investment rules to support decisions and thus help investors to maximize the profit in their operations in the stock market. The experiments reported in this paper compare the results obtained by the proposed model with the Buy-and-Hold, PAA-IDPSO approaches and another approach found in the literature. We report on experi ments conducted with S&P100 index stocks and using the Friedman Non-Parametric Test with the Nemenyi post-hoc Test both with 95% confidence level. The results show that the proposed model outperformed the competing methods and was able to considerably reduce the variance for all stocks.

© 2017 Elsevier B.V. All rights reserved

## 1. Introduction

A time series is a set of observations ordered according to some parameter [1]. Financial time series, for example, represent stock prices in the financial market and follow a chronological order [2]. This kind of data can be used for analyzing and understanding the past and forecasting the future, allowing information users to improved their decision-making. Besides, time series analysis also aims to identify patterns in the data and distinguish them from random variations. These tasks of time series analysis combined with the high computing power available nowadays, have made it a tool widely used in several economic sectors, such as government, industry and commerce [3].

Data mining is the process of “making better use of data” and is founded on the theory that historical data store information that can be used to predict future behavior [4]. In the financial market scenario, data mining can be used to discover hidden patterns in historical data time series, which can represent their behavior, including trends, seasonality and other information. Thus, these patterns can be used to advise on purchase and sale of stocks and thereby assist investors in their decision-making [2].

High dimensionality (a large number of data points) and continuous updating are among the main features of financial time series data. As a consequence of the high dimensionality, the increase in runtime and storage space are some of the main problems that data mining techniques must tackle. One of the most common approaches to dimensionality reduction is to transform the time series to another domain. This transformation may enable a faster computation of the similarity among processed data as if they were the original time series data, yet at a lower computational cost [5].

We have recently proposed PAA-PSO, a data mining technique applied to time series for stock trading [6]. This approach is a model that combines Piecewise Aggregate Approximation (PAA) and Particle Swarm Optimization (PSO) to discover the best representative pattern of time series, which is, the pattern that obtains the best financial results in trading. This pattern is used in conjunction with trade rules to automate the decision on buying, selling or keeping the stock. We have shown that PAA-PSO obtains equal or better results with a lower computational cost when compared to SAX-GA, which combines Symbolic Aggregate Approximation (SAX) with Genetic Algorithm (GA) for trading stocks [7]. We have also shown that PAA-PSO outperformed the Buy-and-Hold strategy, in which an investor buys the stock and keeps it in his investment portfolio for a long period. This strategy is widely used as a reference for comparison with proposed models in studies applied to the financial market [7–11].

However, both PAA-PSO and SAX-GA produce a high variance in their results, i.e., when running n times the same experiment, the results vary significantly. In practice, this generates poor results for a decision support system since such variability in the results represents a high risk in the transactions carried out automatically by the system or indicated to the investors. Thus, the primary objective of this paper is to introduce a method that reduces the variance, in addition to providing profits better than those obtained by PAA-PSO [6].

To this end, this paper proposes the PAA-MS-IDPSO-V technique. PAA-MS-IDPSO-V combines (i) the Piecewise Aggregate Approximation (PAA), for time series representation and dimensionality reduction, (ii) a Multi-Swarm of Improved Self-adaptive Particle Swarm Optimization algorithm (IDPSO) with the early stopping criterion [12] (iii) and the use of validation set [13].

The PAA-MS-IDPSO-V is responsible for discovering patterns that are used by the proposed business rules as investment strategies serving as a decision support system to automate operations in the stock market (decisions about the best moments for buying and selling stocks) and help investors maximize their profits with controlled risk.

The proposed method utilizes (i) multi-swarms and (ii) validation set aiming to control the risk (reduce the variance of the results). Multi-swarm is a technique that uses various swarms simultaneously to deal with multiple peaks (often used in multimodal functions, typical of real-world problems) [14]. The validation set and early stopping criterion are used to avoid the overfitting of the model [15].

We report on experiments carried out using stocks from the S&P100 aimed at evaluating the effectiveness of the proposed model. Friedman Non-Parametric Tests with the Nemenyi post-hoc Test with 95% confidence level were performed on the results to compare the proposed method to the PAA-IDPSO [6] and the approach introduced by Teixeira and Oliveira [9] regarding profitability.

This paper is organized as follows: Section 2 discusses decision support systems, time series, optimization algorithms - specifically PSO, IDPSO and multi-swarms approaches - validation and the early stopping criterion. Section 3 presents the proposed method. In Section 4 the experiments are reported, and the results are analyzed. Section 5 presents the conclusions.

## 2. Fundamentals

This section briefly reviews the main areas of research of this paper (i) decision support systems, (ii) representation technique used in time series data mining, i.e., the PAA approach, (iii) optimization based on PSO algorithms, and also (iv) use of validation set and early stopping criterion.

## 2.1. Decision Support Systems for stock trading and data streams

Decision Support Systems (DSSs) are computer systems that analyze and compile a significant amount of data and are used to assist users in their decision-making [16]. DSSs are used in many areas, including financial and stock trading systems [16–21].

Zhang et al. [17] proposed a DSS based on an aggregate ensemble learning framework used for mining noisy data streams without preprocessing the data. Kao et al. [18] proposed a DSS for forecasting stock prices based on a hybrid approach integrated by wavelet-based feature extraction with Multivariate Adaptive Regression Splines (MARS) and Support Vector Regression (SVR). Geva and Zahavi [19] proposed an automated intraday stock recommendation system that incorporates both market data and textual news. Oliveira et al. [20] proposed an automatic approach, called Lexicon acquisition, to perform sentiment analysis in financial market through microblogging messages. According to Shynkevich et al. [21], the market changes when new information is disclosed, e.g., information derived from news articles, which affect the decisions made by investors. In this context, Shynkevich et al. proposed a decision support system capable of reading these news articles simultaneously, providing different degrees of relevance to the information based on the sector of the financial market that one wishes to operate.

## 2.2. Time series data mining

## 2.2.1. Piecewise Aggregate Approximation (PAA)

Piecewise Aggregate Approximation (PAA), proposed by Keogh et al. [22], is an approach used for data representation and dimensionality reduction in time series data mining. In this method, a time series window of size n is divided into k segments of equal length, and the average value of the data of the segments is then used as the representative value of each segment. Hence, a time series PAA representation will be a k-dimensional vector of the means values of each segment. Fig. 1 depicts an example of a PAA representation.

PAA is performed in two steps [22]. Initially, the original time series window data must be standardized. The purpose of this step is to convert the data to the same relative amplitude, keeping the original form of the data. The statistical standardization is computed via Eq. (1).

$$
x _ {i} ^ {\prime} = \frac {x _ {i} - \mu_ {x}}{\sigma_ {x}}\tag{1}
$$

![](/api/attachments/BWHX3Z5A/fulltext/images/bac1ca33aa0387bc8fbe9099c45f674d1c4dacb3d76fc2245d55cb18af61bc07.jpg)  
Fig. 1. PAA representation of a time series Q. In this example, PAA parameters ar $\mathfrak { n } = 1 5 , \mathrm { k } = 5$

Please cite this article as: R. Brasileiro et al., Automatic trading method based on piecewise aggregate approximation and multi-swarm of improved self-adaptive particle swarm optimization..., Decision Support Systems (2017), https://doi.org/10.1016/j.dss.2017.10.005

![](/api/attachments/BWHX3Z5A/fulltext/images/933c311118afffece53d8325b951649dd06b1138af52d67e0f575aabb938ffd0.jpg)

![](/api/attachments/BWHX3Z5A/fulltext/images/86b216f16fc051e31c59eec6a42845d0820ffc66017cb6bb1b9963c881cadc6b.jpg)  
Fig. 2. Statistical standardization of the time series data.

where $x _ { i }$ represents a point in the time series window, $\mu _ { x }$ and $\sigma _ { x }$ are, respectively, the average and standard deviation considering all points in the window, and $x _ { i } ^ { \prime }$ is a point in the standardized series window. Fig. 2 depicts an example of the data standardization.

The next step is the dimensionality reduction carried out by PAA. Let the time series size be m, a window of this series has size $n ( n < <$ m), and k be the number of segments to which the time window will be reduced. Let $\bar { x } _ { i }$ be the representative value of the ith segment and $\vec { x } _ { i } ^ { \prime }$ be the vector of elements of the segment. Then, if the relationship $\dot { n } / k$ is an integer value, the dimensionality reduction operation can be computed by Eq. (2).

$$
\bar {x} _ {i} = \frac {k}{n} \sum_ {j = \frac {n}{k} (i - 1) + 1} ^ {\frac {n}{k} i} x _ {j} ^ {\prime}\tag{2}
$$

However, if the relationship $n / k$ does not result in an integer, the border points between the segments should contribute to the formation of the final value for both segments. In this case, PAA carries out the operation as shown in Fig. 3.

As can be seen in Fig. 3, in which there are 12 points and five segments, this means that each segment must have 2.4 points of the contribution to the average. Thus, points 1 and two entirely belong to segment S1 and to complete it its value should have 40% of point 3. Segment S2 is formed by the other 60% of point 3, the whole point 4 and 80% of point $^ { 5 , }$ to complete the 2.4 points for computing its average. PAA fills the rest of the segments as explained and depicted in Fig. 3.

PAA has some advantages: facility to implement; very speedy execution; generates a flexible model; indexing values may be done in linear time; the proximity between two time series can be easily computed by the minimum distance (MINDIST) between their respective PAA representations [22,23]. Given $\bar { Q }$ and C¯ PAA representations of two time series, MINDIST is computed by Eq. (3). Fig. 4 illustrates the computation of MINDIST between Q¯ and C¯ (PAA representations of two time series).

![](/api/attachments/BWHX3Z5A/fulltext/images/2bb061a7e865c5a31bfad32fe6f16797d36146ca3fcc48d9585f7058630e5d77.jpg)  
Fig. 3. PAA segments when the relationship n/k does not result in integer. In this example, PAA parameters are $\mathbf { n } = 1 2 , \mathbf { k } = 5 ,$ which means that each segment must have 2.4 points of the contribution to the average.

$$
M I N D I S T (\bar {Q}, \bar {C}) = \sqrt {\frac {n}{k}} \sqrt {\sum_ {i = 1} ^ {k} (d i s t (\bar {q} _ {i} , \bar {c} _ {i})) ^ {2}}\tag{3}
$$

A relevant feature of MINDIST is that it represents the lower limit of the Euclidean distance. This feature allows the method (i) to carry out data mining using the representation eficiently and (ii) to produce identical results to those obtained if one operates on the original data.

However, as is the case for all dimensionality reduction methods, PAA can lose useful information for time series data analysis. An example is the loss of information about peak values (extreme values) that occur within the segment because PAA representation uses mean values [22]. However, the correct choice of PAA parameters can control the amount of information loss.

![](/api/attachments/BWHX3Z5A/fulltext/images/d4ce311ec66efb0e8e9d924e539bbecd08f95e7a7ea9c842c079b1d73dd2213e.jpg)  
Fig. 4. Computing MINDIST between two PAA time series representations, Q¯ and C¯ .

Please cite this article as: R. Brasileiro et al., Automatic trading method based on piecewise aggregate approximation and multi-swarm of improved self-adaptive particle swarm optimization..., Decision Support Systems (2017), https://doi.org/10.1016/j.dss.2017.10.005

R. Brasileiro et al. / Decision Support Systems xxx (2017) xxx–xxx

## 2.3. Optimization algorithms

## 2.3.1. Particle Swarm Optimization (PSO)

Particle Swarm Optimization (PSO) is a stochastic optimization algorithm used to find the global optimum of an objective function, by simulating the behavior and the movement of a flock of birds. Compared with other nature-inspired optimization methods, like Genetic Algorithm (GA), PSO has some advantages. Some of the advantages are (i) simple structure, (ii) simple parameters setting, (iii) fast convergence, and (iv) a good trade-off between exploration (ability to explore all the search space) and exploitation (ability to refine the solutions).

In PSO, each possible solution (particle) is initially positioned randomly in a multidimensional search space. Each particle has two associated values, position and speed, which PSO updates at each iteration. The position is its place in space. PSO computes the velocity considering the following factors: inertia, cognitive component, and social component. Inertia attempts to keep the particle motion in the direction that it had been following. The cognitive element influences the particle motion in the direction of its better position. The social component attracts the particle toward the best solution found by the whole population. Thus, each particle adjusts its position according to its own experience and that of other individuals in the population, combining local search with global search. PSO uses a fitness function to compute the quality of the positions obtained by each particle.

For the algorithm definition, given a search space with D dimensions and a swarm with N particles, for each particle of the swarm the position in the space is a D-dimensional vector, $x _ { i } = [ x _ { i 1 } , x _ { i 2 } , \dotsc , x _ { i D } ] ;$ the particle velocity is the vector $\nu _ { i } = [ \nu _ { i 1 } , \nu _ { i 2 } , \ldots , \nu _ { i D } ] ;$ the particle best position (local best) $p _ { i } = [ p _ { i 1 } , p _ { i 2 } , \dotsc , p _ { i D } ]$ and the best position obtained by the swarm (global best) $p _ { g } = [ p _ { g 1 } , p _ { g 2 } , \dotsc , p _ { g D } ]$ . Then, for each iteration, the particle speed and position updating are given by Eqs. (4) and (5) [12].

$$
v _ {i} (t + 1) = w \cdot v _ {i} (t) + c _ {1} \cdot r a n d \cdot \left(p _ {i} - x _ {i} (t)\right) + c _ {2} \cdot R a n d \cdot \left(p _ {g} - x _ {i} (t)\right)\tag{4}
$$

$$
x _ {i} (t + 1) = x _ {i} (t) + v _ {i} (t + 1)\tag{5}
$$

where, $c _ { 1 }$ and $c _ { 2 }$ represent acceleration factors and are positive constants, rand and Rand are two random variables with uniform distribution within the range [0,1], and w is the inertia factor. In the velocity equation, the first term represents the inertia, the second represents the cognitive component, and the third represents the social component [12]. Algorithm 1 presents the pseudocode of PSO.

## Algorithm 1. PSO pseudocode.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1 begin
2 Generate an initial population of particles: P
3 Randomly initialize the starting position (x) and the initial velocity (v) of each particle i of P.
4 for each particle i of P do
5 Compute fitness  $f_{i}$  through the chosen fitness function
6 Compute the best particle position i so far:  $p_{ibest}$ 
7 end
8 Select the particle with best fitness of the swarm:  $p_{gbest}$ 
9 for each particle i of P do
10 Update particle velocity: Eq. 4
11 Update particle position: Eq. 5
12 end
13 if stopping criteria is not reached then
14 Return to line 4.
15 end
</div>

## 2.3.2. Improved Self-Adaptive Particle Swarm Optimization (IDPSO)

Research and practical applications of PSO have shown that the three parameters w, $c _ { 1 }$ and $c _ { 2 }$ have a significant impact on the algorithm performance. A greater weight of inertia facilitates global exploration (exploration of new areas), while a smaller inertia weight tends to facilitate local exploration to refine the solution in the current search area (exploitation). For the values of the cognitive and social components, higher values for $c _ { 1 }$ give greater weight to local search, while higher values for $c _ { 2 }$ promotes global search.

In general, parameters w, $c _ { 1 }$ and $c _ { 2 }$ are fixed for all PSO iteration. The dynamic adjustment of these parameters could improve performance by promoting global search in the beginning and local search in the final iterations. To this end, Zhang et al. [12] have proposed the Improved Self-Adaptive Particle Swarm Optimization Algorithm (IDPSO). In this variation of PSO, the algorithm itself adjusts w, c and $c _ { 2 }$ dynamically, over iterations, through the computation of the detection function v(t). The detection function v(t) is defined by Eq. (6).

$$
\varphi (t) = \left| \left(p _ {g} - x _ {i} (t - 1)\right) / \left(p _ {i} - x _ {i} (t - 1)\right) \right|\tag{6}
$$

where $| ( p _ { g } - x _ { i } ( t - 1 ) ) |$ is the Euclidean distance between the best position found by the swarm and the previous position of the particle i; and $| ( p _ { i } - x _ { i } ( t - 1 ) ) |$ is the Euclidean distance between the best position found by the particle i and its previous position.

The values of $c _ { 1 }$ and $c _ { 2 }$ are dynamically modified according to the detection function v(t). Inertia weight variation is based on both v(t) and a variable Sigmoid Function, to find the best solution. The variables of IDPSO are updated according to Eqs. (7), (8), (9), (10) and (11) [12].

$$
w (t) = \frac {w _ {i n i t i a l} - w _ {f i n a l}}{1 + e ^ {\varphi (t) \cdot (t - ((1 + l n (\varphi (t))) \cdot k _ {\max}) / \mu)}} + w _ {f i n a l}\tag{7}
$$

$$
c _ {1} = c _ {1} \cdot \varphi (t) ^ {- 1}\tag{8}
$$

$$
c _ {2} = c _ {2} \cdot \varphi (t)\tag{9}
$$

$$
v _ {i} (t + 1) = w \cdot v _ {i} (t) + c _ {1} \cdot r a n d \cdot \left(p _ {i} - x _ {i} (t)\right) + c _ {2} \cdot R a n d \cdot \left(p _ {g} - x _ {i} (t)\right)\tag{10}
$$

$$
x _ {i} (t + 1) = x _ {i} (t) + v _ {i} (t + 1)\tag{11}
$$

where, $w _ { i n i t i a l }$ and $w _ { f i n a l }$ represent, respectively, the initial and final values of inertia w (values in the range $0 \textless w < 2 ) , K _ { \operatorname* { m a x } }$ is the maximum number of iterations used in the algorithm, t is the current iteration of the algorithm, v(t) is the detection function and l is an adjustment factor [12].

The use of detection function v(t) in IDPSO provides the algorithm with the ability to perform a smooth transition from “exploration” to “exploitation” adaptively based on the Sigmoidal Function.

In initial iterations, when $\varphi ( t ) \ \geq \ 1 \qquad $ , the algorithm emphasizes the global search and strengthens the ability of “exploration” and the weight of the social component (Eq. (9)) increases to improve the exchange of information and cooperation of the particles, so the value of $c _ { 1 }$ is reduced and value of $c _ { 2 }$ is increased. In later iterations, when $\varphi ( t ) ~ < ~ 1$ , the algorithm emphasizes local search capability and strengthens the ability of “exploitation” and the weight of the cognitive component (Eq. (8)) increases to improve the influence of the particle itself, so the value of $c _ { 1 }$ is increased and value of $c _ { 2 }$ is reduced.

Thus, IDPSO displays all PSO advantages and also improves both the ability of exploration and exploitation. Another advantage is

Please cite this article as: R. Brasileiro et al., Automatic trading method based on piecewise aggregate approximation and multi-swarm of improved self-adaptive particle swarm optimization..., Decision Support Systems (2017), https://doi.org/10.1016/j.dss.2017.10.005

that IDPSO is not dependent on the parameters w, c and c [12]. Algorithm 2 presents IDPSO Pseudocode.

## Algorithm 2. IDPSO pseudocode.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1 begin
2 Generate an initial population of particles: P
3 Randomly initialize the starting position (x) and the initial velocity (v) of each particle i of P.
4 for each particle i of P do
5 Compute fitness  $f_{i}$  through the chosen fitness function
6 Compute the best particle position i so far:  $p_{ibest}$ 
7 end
8 Select the particle with best fitness of the swarm:  $p_{gbest}$ 
9 for each particle i of P do
10 Compute detection function  $\varphi(t)$ . Eq. 6
11 Update inertia. Eq. 7
12 Update the variables  $c_{1}$  and  $c_{2}$ . Eq. 8 e Eq. 9
13 Update particle velocity: Eq. 3.10
14 Update particle position: Eq. 3.11
15 end
16 if stopping criteria is not reached then
17 Return to line 4.
18 end
</div>

## 2.3.3. Multi-swarm

Multi-swarms optimization algorithms are algorithms that keep multiple sub-swarms working simultaneously. Each sub-swarm can handle a specific area of the search space and take on different responsibilities. For example, some sub-swarms may focus on refining the gbest solution, while others focus on searching new promising areas on space. Moreover, different sub-swarms can communicate and exchange information or be independent of each other [14,24].

In this way, the sub-swarms can be classified into two types: concurrent and collaborative. In concurrent multi-swarms, the subswarms compete against each other and do not exchange information among themselves. Also, they do not work in the same search area. In collaborative multi-swarms, the sub-swarms cooperate with each other, being able to exchange information and search in the same area of the search space.

In the scenario where each sub-swarm works independently, that is, without sharing information, a sub-swarm that tends to the global maximum solution may not be influenced by sub-swarms that go towards local peaks. Fig. 5 presents this situation, where sub-swarms 2 and 3 deal with local peaks, while sub-swarm 1 tends to the global maximum solution of the function. Since each sub-swarm works independently, several different gbests are generated, and they do not share information.

Other types of multi-swarm algorithms divide the search operations (exploration) and refinement of optimal solutions (exploitation) between their sub-swarms, respectively, $P _ { s e a r c h }$ and $P _ { t r a c k }$ subswarms. In this case, there is information sharing between them.

![](/api/attachments/BWHX3Z5A/fulltext/images/45909423b1fc09d41329fdfd798556a5908e55560753564a0a1b880fd039dc78.jpg)  
Fig. 5. Representation of multimodal function.

When a new promising area of the search space is identified, $P _ { s e a r c h }$ will inform the $P _ { t r a c k }$ of the new location, which will subsequently be refined. The information will then be shared between all subswarms [14].

In general, multi-swarms algorithms are used as more flexible approaches to problems where multiple peaks are encountered, i.e., in problems represented by multimodal functions [14]. The literature shows that, in general, real-world problems are multimodal. Such problems are complex, and that is why several recent studies try to combine different approaches to solve them [14].

## 2.4. Validation and early stopping criterion

Overfitting occurs when the model adjusts too much to the training dataset. When this situation occurs, the trained model obtains high precision in training set but does not present a good generalization to other data, which can result in reduced predictive performance in test sets. That is why it is crucial to avoid overfitting [13].

Several are the reasons why overfitting may occur. For example, (i) the small number of samples used in training, (ii) the existence of a reasonable number of noisy samples in the training set, and (iii) any other form of bias the training data [13].

The main techniques to avoid overfitting are: (i) penalizing complexity or biasing towards simplicity, (ii) limiting the number of models considered, (iii) using a validation dataset [15]. Each technique has advantages and disadvantages, for instance, (i) may involve the use of complex algorithms such as post-pruning of models or generating and hypothesizing models. Even so, some studies showed that this kind of technique had not improved performance [15]. On the other hand, in (iii) the validation set can be used to test generalization errors and contribute to the decision of which model to use, avoiding too complex algorithms [15].

The early stopping criterion is also a method used to avoid overfitting considering a validation set. In this scenario, training is interrupted if there is no fitness improvement of the model in the validation set over a given number of iterations [13].

## 3. The proposed method

The PAA-MS-IDPSO-V algorithm (Piecewise Aggregate Approximation - Multi-Swarm of Improved Self-Adaptive Particle Swarm Optimization with Validation) combines (i) the PAA approach for representation and data mining of financial time series, (ii) IDPSO algorithm for global optimization (iii) a multi-swarm variation to improve both local and global search, and (iv) the use of a validation set along with the early stopping criteria to avoid overfitting. The proposed method is used to discover typical patterns of financial time series that will be used together with the proposed decision rules to serve as a decision support system to automate operations in the stock market.

Four stages compose the algorithm: training1, training2, validation, and test. In the training1 stage, several sub-swarms are initialized to find their respective global optimum. In the training2 stage, the best particles of each sub-swarm are shared with the main swarm. Next, the main swarm is initialized, and another optimization process is performed. In the validation stage, a filter is used to choose the best particle of the main swarm. This particle is the one that defines the values of the parameters to be used by the decision rules and the pattern that represents the time series. In the test stage, with the pattern and parameters already set, the algorithm is used to BUY and SELL orders according to the decision rules. Performance of the system is measured in the test set.

The PAA approach for time series representation and dimensionality reduction was chosen due to its advantages: (i) be fast, simple and surprisingly competitive when compared to other more sophisticated processing techniques; (ii) may be applied directly without further processing of the original data available; and (iii) facilitates indexing of the representation since each segment has the same length [23].

![](/api/attachments/BWHX3Z5A/fulltext/images/53bb8b5fa2076d9769a20eaddc044dd97ffff75a6155a1f22d6f22d84f78ed9e.jpg)  
Fig. 6. Representation of the particle structure.

![](/api/attachments/BWHX3Z5A/fulltext/images/27bc0bb5acdaec3218b02dbb374ab2728c748fd7f0b1e665cfa5ed2eb4e2afe7.jpg)  
Fig. 7. Decision rules.

The fact that PAA works with continuous variables was decisive for the choice of IDPSO for optimization in the proposed method. The reason is that, according to the literature, PSO shows good computational eficiency when used to solve problems with continuous variables. Furthermore, PSO still has the advantage of being an algorithm with a simple structure, easy adjustment parameters, fast convergence, and capacity to combine local and global search. Finally, the choice of IDPSO occurred mainly because of its improvements in the exploration and exploitation capabilities of PSO. Another advantage of IDPSO for our algorithm is that it is not dependent on the parameters: inertia w, cognitive acceleration component $c _ { 1 }$ and social acceleration component $c _ { 2 }$ .

In the proposed method, PAA parameters are set by the user. The method uses a sliding window with size one to navigate over the financial time series, i.e., each iteration of the algorithm moves one day in the time series (daily prices of stocks).

Fig. 6 shows the structure of the particle for the decision rules (adapted from [7]). The proposed method operates only long positions; this means that the system supports investors buying stocks with the expectation that their prices will increase.

The number of dimensions, D of the particle, depends on the number of segments (k) in the PAA representation. The representation uses one dimension for “Distance to buy”, one dimension for “Distance to Sell”, one dimension for “Days to sell”, and k dimensions for the pattern that will be discovered using IDPSO (PAA representation).

The IDPSO fitness function to be optimized is the total profit obtained by operating in the market using the decision rules depicted in Fig. 7. The algorithm returns the parameters values obtained by the best particle of the swarms (Fig. 6). “Distance to Buy” is how close the discovered pattern and the PAA representation of a time series window must be to trigger a BUY order. “Distance to Sell” how far the discovered pattern and the PAA representation of a time series window must be to trigger a SELL order if any stock is bought. “Days to sell” represents the maximum number of days that the system will maintain stocks in Buy position. Finally, the algorithm also returns the PAA representation found by IDPSO as the best representative pattern.

## 3.1. Multi-swarm architecture

Each time series is divided into three parts: the training set (used in training steps 1 and 2), the validation set (used in validation step), and the test set (used in the test step). This division is necessary to fit the stages of the proposed model. Fig. 8 depicts the architecture of the proposed model.

![](/api/attachments/BWHX3Z5A/fulltext/images/07545a2a02c81f1060c6ce0c203a6335be216a996dc9761dec8fae1edbed3b61.jpg)  
Fig. 8. Architecture of the proposed approach.

Please cite this article as: R. Brasileiro et al., Automatic trading method based on piecewise aggregate approximation and multi-swarm of improved self-adaptive particle swarm optimization..., Decision Support Systems (2017), https://doi.org/10.1016/j.dss.2017.10.005

In training1 stage, n independent sub-swarms are initiated, where n is the number of particles in the main-swarm. This phase is characterized by the use of the early stopping criteria and by the independence between the sub-swarms. The early stopping method is used to avoid local peaks, to ensure the population diversity and to prevent possible premature convergence of the sub-swarm. As the proposed approach operates in multimodal problems, the independence between sub-swarms is used so that there is no information exchange between them. This independence enables the system to guarantee that poor solutions do not influence a promising solution. At the end of the optimization process, each sub-swarm provides its best particle, obtained considering the fitness function.

In training2 stage, after the sub-swarms provide their most promising particles (from the training1 stage), the main-swarm runs a new optimization, aiming to refine the particles provided by the sub-swarms. During this new process, the particles that have fallen in regions of local bests tend to migrate to regions where the best solutions lie (global best) since now all particles exchange information through gbest. It is relevant to do this because one of the fundamental features of the PSO algorithm is that it is fast to find regions of optimal solutions, but slow to refine them [25]. In the proposed approach, the main-swarm is responsible for the solutions refinement, supplying this deficiency of the PSO algorithm. The early stopping criterion is also used in this phase.

In the validation stage, all main-swarm particles pass through a validation filter, where each particle is tested using the validation set. At this stage, the goal is to find the best particle (the one with the best fitness), discarding the others to avoid overfitting; this practice has been adopted in optimization problems [13]. At the end of this step, the structure of the particle that obtained the best fitness in validation set is chosen to operate in the decision support system.

In the test phase, the first step is to compute the PAA representation for sliding windows resulting from the original time series (test set). Next, the algorithm computes the distance (variable “Distance” in Fig. 7) between this representation and the best pattern learned from the training phase (Fig. 6), by using MINDIST (Eq. (3)). This distance is then compared to the values obtained in the training phase (Distance\_to\_buy and Distance\_to\_sell) to decide whether to buy stocks or sell them. The algorithm also computes the maximum number of days in Buy position, then, when it reaches the limit of days obtained in training phase (Days\_to\_sell), all the stocks are sold, regardless of the distance (Fig. 7).

## 3.2. Reducing the variance

It has been observed that one of the main problems of the PAA-PSO approach [6] is its high variance. To tackle this problem, this paper proposed the use of a multi-swarm and a validation set together with the early stopping criterion.

The multi-swarm is designed to generate useful solutions, avoiding local peaks. In this case, sub-swarms, which are independent of each other and do not exchange information, seek promising solutions that can be improved later in the main swarm. The use of sub-swarms in the method is essential to avoid falling into local peaks [14].

As discussed in Subsection 2.4, particles that obtained powerful results in the training set are not always guaranteed to produce good results in the test set. This may be a result of overfitting training data. The proposed approach attempts to avoid this scenario through the validation step, where a filter is created to avoid overfitting. As a consequence, the variance of the results obtained by the proposed model is expected to be reduced.

The early stopping criterion adopted in this work monitors the lack of improvement of the gbest of the IDPSO algorithm [15]. In this case, the optimization algorithm stops running after n iterations without improvement in the best fitness. Thus, the number of iterations may be reduced considerably to avoid local peaks in the solutions generated by the sub-swarms.

## 4. Experimental evaluation

The experiments used the following stocks:

All stocks from S&P100 index, except the following: ABBV, FB, GM, GOOG, GOOGL, KHC, KMI, MA, PM, PYPL, V, VZ. They were excluded because they do not have all the necessary data for the analyzed period.

Data from daily stocks prices were obtained from Yahoo Finance, S&P100 index<sup>1</sup>. The period used was January 2000 to June 2010. Data from January 2000 to December 2004 formed the training set whereas data from January 2005 to June 2010, the test period.

The training1 and training2 stages used data from the period from January 2000 to November 2003. The validation stage used data from December 2003 to December 2004. For each stock, simulations were performed 50 times; for each execution, the initial cash balance was \$100,000.00 (one hundred thousand American dollars) [6].

For a better simulation, a market impact factor of 0.1% of the total balance was used as transaction cost (both in purchase and sales operations), the same approach used by Feuerriegel and Prendinger [26]. Thus, in each transaction made, 0.1% of all available money is accounted for as transaction cost.

To analyze the influence of each stage of the proposed architecture, we considered four variations of the proposed models. All models are based on the PAA and IDPSO methods and operate according to the proposed decision rule (Fig. 7).

PAA-IDPSO: does not use any additional components;

PAA-IDPSO-V: uses the validation component;

PAA-MS-IDPSO: uses the multi-swarm component;

PAA-MS-IDPSO-V: uses both the multi-swarm and validation components.

The parameters used for PAA-MS-IDPSO-V, PAA-MS-IDPSO, PAA-IDPSO-V and PAA-IDPSO are as follows [6]: distances are float type values in the range [0, 40]; days are integer type values in the range [1, 50], each value x of the PAA pattern $P A A = [ \bar { x } _ { 1 } , \bar { x } _ { 2 } , \ldots , \bar { x } _ { k } ]$ is a float type value in the range [ 6.0, 6.0]. For days parameters, during optimization, this value is worked as floating point and converted to integer values when used by the model decision rule.

The settings used for the PAA, window size values (n) and the number of segments (k), were, for all stocks: $n = 1 8 0 { \mathrm { ~ e ~ } } k = 1 8 .$

In order to analyze the influence of the number of particles, experiments using 25, 50 and 100 particles for each swarm, subswarm and main swarm were performed. As in the original IDPSO method, $\mu = 1 0 0 , w _ { i n i c i a l } = 0 . 9$ and $w _ { f i n a l } = 0 . 4 [ 1 2 ]$

For PAA-MS-IDPSO-V and PAA-MS-IDPSO, in the training1 stage, the maximum number of iterations was 900, with an early stopping criterion of 300 iterations without fitness improvement. In the training2 stage, as the goal is to refine the solutions, the maximum number of iterations was 20,000, and the early stopping criterion was 2000 iterations without improvement of fitness.

For PAA-IDPSO-V and PAA-IDPSO, the experiments used a maximum number of iterations of 20,000 with the early stopping criterion of 2000 iterations without improvement of fitness. The same values that were adopted in PAA-MS-IDPSO-V and PAA-MS-IDPSO in training2 step.

The experiments also analyzed the influence of using additional risk control methods by investigating the use of the maximum drawdown with stop-loss techniques. Thus, in the model with the risk control, if the maximum drawdown calculated during the training is reached during the test, then the stop-loss will be activated. In this case, when the stop-loss is active if the stock price falls 5% [9] of the purchase value, then a sale will be made, regardless of any decision of the algorithm.

Also, the results obtained by the proposed approaches were compared to those of the PAA-IDPSO [6], the Buy-and-Hold and the model proposed by Teixeira and Oliveira [9].

Teixeira and Oliveira have proposed an automatic system for forecasting price trends in the stock market. In this work, they used a classifier to decide on the optimal points of buying and selling stocks. The data used by the classifier were some technical indicators created from the stock price time series [9].

Moreover, to test whether there is a statistical difference in the results, the Friedman Non-Parametric Test with 95% confidence level was used, as presented by [27]. If the null hypothesis is rejected, i.e., there is a significant difference between the methods, then the Nemenyi post-hoc Test is performed with 95% confidence level.

Fig. 9 presents the boxplots of the results obtained by each model in their 50 runs for the ALL stock. The buy-and-hold result, obtained by buying the stocks on the first day (using the initial cash balance, \$100,000.00) and selling in the last day, is also shown.

As can be seen, PAA-MS-IDPSO-V obtained the best result, followed by PAA-MS-IDPSO. The final balance obtained by these methods were much better than the buy-and-hold. It can also be observed that, in the models that used the multi-swarm concept, the variance over the 50 runs was zero. This result shows that the multi-swarm can avoid local minima (which would lead to a high variance). The PAA-MS-IDPSO-V method obtained zero variance in 30 of the 88 stocks from the S&P100 used in the experiments. Considering all 88 stocks, the mean percent variance-to-mean ratio was 6.97%. In contrast, the mean percent variance-to-mean ratio obtained by PAA-IDPSO was 34.30%, and this method has not obtained zero variance in any stock.

Fig. 10 presents the return on investment (ROI) of the analyzed test period for the ALL stock, for the PAA-MS-IDPSO-V model without the drawdown, using 50 particles. In the figure, it can be observed that during the first 30 months the value of the stock remained stable, then the value began to oscillate. While there were no significant changes in the stock value, the PAA-MS-IDPSO-V remained out of the market, without making any purchase operations. When the changes began to occur, PAA-MS-IDPSO-V immediately entered the market and started to conduct sales and purchase operations, earning profits. As can be seen, while Buy-and-Hold showed a decline in its investments, the PAA-MS-IDPSO-V made significant profits, taking advantage of the best buying and selling opportunities.

![](/api/attachments/BWHX3Z5A/fulltext/images/ea0cf3a667d6be856a4a4d9b12b4eed9a5682e1a32bf22140252bc75ebb5b9b7.jpg)  
Fig. 9. Boxplot of the results obtained by the models in their 50 runs without drawdown, using 50 particles, for the ALL stock.

![](/api/attachments/BWHX3Z5A/fulltext/images/549523ca82b4a9ba7a5db46197c8bea01c418db85abf8418c00b50bd22d4bf82.jpg)  
Fig. 10. Comparison of the monthly return on investment between Buy-and-hold and PAA-MS-IDPSO-V ALL stock without drawdown, using 50 particles.

Fig. 11 depicts a histogram which shows the profits/losses from the purchase and sale operation accumulated over the 50 runs of the GS stock experiment using the PAA-MS-IDPSO-V. The figure shows that, in most operations, the model made profits (positive returns). In this experiment, there was an average of 23.92 buy and sell operations, of which 16.56 were operations with profits, and only 7.36 were operations with losses. The average cost of the transactions was \$3830.12 obtaining a balance of \$260,646.31 at the end of the experiment. Considering all 88 stocks used in the experiments, the mean and standard deviation for (i) the number of buying and selling operations was 94.58(130.64), (ii) the number of profit operations was 54.06(34.82), and (iii) the number of losses operations was 41.51(30.82).

Figs. 12 to 19 present the Nemenyi post-hoc test of the results obtained by all models, grouping all the 88 stocks used in the experiments. In these graphs, there is a significant difference when the results border of one model does not cross with the others. When this happens, the best model is represented in red color. The models that obtained the best results are presented from left to right. If there is no difference, all the model’s representations will be in blue,

![](/api/attachments/BWHX3Z5A/fulltext/images/4d74853b6efcc1bf34e768d54a652abf2f877b23b65577d07f66720fc546ad12.jpg)  
Fig. 11. Histogram of the profits/losses of the GS stock over the 50 runs of the model PAA-MS-IDPSO-V without drawdown with 50 particles.

Please cite this article as: R. Brasileiro et al., Automatic trading method based on piecewise aggregate approximation and multi-swarm of improved self-adaptive particle swarm optimization..., Decision Support Systems (2017), https://doi.org/10.1016/j.dss.2017.10.005

Friedman p-value: 2.3e-20● Different ● CritDist: 0.8

## R. Brasileiro et al. / Decision Support Systems xxx (2017) xxx–xxx

Friedman p-value: 4.5e-20 • Different • CritDist: 0.8  
![](/api/attachments/BWHX3Z5A/fulltext/images/2d617785b55544e17fe01de91abad3fdc929bf7f22c7c7dd97c0e6b668429b69.jpg)  
Fig. 12. Nemenyi post-hoc test for the models PAA-MS-IDPSO-V, PAA-MS-IDPSO, PAA-IDPSO-V, PAA-IDPSO (all using 25 particles without risk control), Buy-and-Hold and Teixeira and Oliveira [9] for all analyzed stocks.

and once again the best ones are presented from left to right, even if there is no statistical difference.

Figs. 12, 13, 14 depict the Nemenyi post-hoc test results for the experiments performed without the risk control through drawdown, with 25, 50 and 100 particles, respectively. The results show that for the analyzed S&P100 stocks, PAA-MS-IDPSO-V was significantly better than the other variations of the models of the proposed architecture. PAA-MS-IDPSO-V has also significantly outperformed both Buy-and-Hold and the method proposed by Teixeira and Oliveira [9].

Figs. 15, 16, 17 present the results of the Nemenyi post-hoc test for the models with risk control via the drawdown, with 25, 50 and 100 particles, respectively. Again, the PAA-MS-IDPSO-V approach obtained significantly better results than the others for the analyzed scenario.

These results demonstrate that PAA-MS-IDPSO-V was the best in all scenarios analyzed, i.e., with and without drawdown risk control and using 25, 50 and 100 particles. We also analyzed the influence of the number of particles in the results obtained by the model. The Nemenyi post-hoc tests, depicted in Figs. 18 (a) (with risk control) and 18(b) (without risk control), show that the number of particles does not influence the result of the proposed architecture, in both cases with and without risk control. It is important to note that using fewer particles implies a lower computational cost since the number of sub-swarms also decreases, as explained in the Proposed Method Sub-section 3.1.

The influence of risk control based on drawdown and stop loss was also analyzed. Fig. 19 depicts the comparison between the model PAA-MS-IDPSO-V with and without risk control, using 50 particles.

![](/api/attachments/BWHX3Z5A/fulltext/images/627ab505337819e487dbc625d6bb84e18a7f43506edf6fb4a2091e7b9d52f6ef.jpg)  
Fig, 13. Nemenvi post-hoc test for the models PAA-MS-IDPSO-V PAA-MS-IDPSO PAA-IDPSO-V PAA-IDPSO (all using 50 particles without risk control). Buv-and-Hold and Teixeira and Oliveira [9] for all analyzed stocks.

Please cite this article as: R. Brasileiro et al., Automatic trading method based on piecewise aggregate approximation and multi-swarm of improved self-adaptive particle swarm optimization..., Decision Support Systems (2017), https://doi.org/10.1016/j.dss.2017.10.005

![](/api/attachments/BWHX3Z5A/fulltext/images/973a60a61b72d510cf0ea54ada49bb632182588efde1da650ef2d3bfbe04b118.jpg)  
Fig. 14. Nemenyi post-hoc test for the models PAA-MS-IDPSO-V, PAA-MS-IDPSO, PAA-IDPSO-V, PAA-IDPSO (all using 100 particles without risk control), Buy-and-Hold and Teixeira and Oliveira [9] for all analyzed stocks.

The result shows that there was no significant difference. Thus, the risk control does not represent a differential for the results obtained by the proposed approach.

Thus, the experiments reported show that the proposed method based on multi-swarm and validation produced much better results than PAA-IDPSO [6], buy-and-hold and Teixeira and Oliveira [9] for the analyzed scenario using the S&P100 stocks.

Furthermore, there was a significant reduction of the variance of the results, which is very important since it represents a decrease of risk in the operations performed by the proposed decision support system.

## 5. Conclusions

This paper presented a new method named PAA-MS-IDPSO-V, used to discover patterns in financial time series to support investment decisions. The method combines Piecewise Aggregate Approximation (PAA), as a representation method of time series, with Improved Self-Adaptive Particle Swarm Optimization (IDPSO). The method uses multi-swarms to obtain a better particle initialization, as well as a validation set together with early stopping to avoid over fitting and minimize variance. The patterns found are then used by the proposed decisions rules to support the investor decision about

![](/api/attachments/BWHX3Z5A/fulltext/images/d590cbdaefb83c3d55ec3ee6297f4ffa8748f33a2fa27a71b06a473a106d242a.jpg)  
Fig. 15. Nemenyi post-hoc test for the models PAA-MS-IDPSO-V, PAA-MS-IDPSO, PAA-IDPSO-V, PAA-IDPSO (all using 25 particles with risk control), Buy-and-Hold and Teixeira and Oliveira [9] for all analyzed stocks.

Please cite this article as: R. Brasileiro et al., Automatic trading method based on piecewise aggregate approximation and multi-swarm of improved self-adaptive particle swarm optimization..., Decision Support Systems (2017), https://doi.org/10.1016/j.dss.2017.10.005

## R. Brasileiro et al. / Decision Support Systems xxx (2017) xxx–xxx

![](/api/attachments/BWHX3Z5A/fulltext/images/1c440140386794de9b2bbbc741fceaffb914e5aef8062be92504eb08a1745db6.jpg)  
Fig. 16. Nemenyi post-hoc test for the models PAA-MS-IDPSO-V, PAA-MS-IDPSO, PAA-IDPSO-V, PAA-IDPSO (all using 50 particles with risk control), Buy-and-Hold and Teixeira and Oliveira [9] for all analyzed stocks.

the best moments for buying and selling stocks, aiming to maximize their profits with a controlled risk.

One of the main advantages of the proposed method over competing methods published in the literature is the use of multi-swarm and validation. These features have enabled our method to better tackle the nature of the financial market, which, in general, gives rise to multimodal fitness functions.

The experiments presented in this paper showed that the proposed method obtained significantly better results (using the Friedman Non-Parametric Test and the Nemenyi post-hoc Test with 95% confidence level) than PAA-IDPSO [6], Buy-and-Hold and the approach proposed by Teixeira and Oliveira [9] for the S&P100 index stocks used.

Four variations of the proposed method were investigated (PAA-MS-IDPSO-V, PAA-MS-IDPSO, PAA-IDPSO-V and PAA-IDPSO [6]) to analyze the influence of each stage independently. As expected, the use of multi-swarm significantly decreased the variance of the results obtained when compared to models that use only one swarm (PAA-IDPSO-V and PAA-IDPSO [6]). In the S&P100 index stocks used in the experiments, the variance was zero or almost zero for the PAA-MS-IDPSO-V approach (as depicted, for instance, in Fig. 9). This represents a reduction in the investor operations

![](/api/attachments/BWHX3Z5A/fulltext/images/d112da78bfad9363f2a7a476a5ab5fbe64f618322f94f38d55d2ac8dcf7852e8.jpg)  
Fig. 17. Nemenyi post-hoc test for the models PAA-MS-IDPSO-V, PAA-MS-IDPSO, PAA-IDPSO-V, PAA-IDPSO (all using 100 particles with risk control), Buy-and-Hold and Teixeira and Oliveira [9] for all analyzed stocks.

Please cite this article as: R. Brasileiro et al., Automatic trading method based on piecewise aggregate approximation and multi-swarm of improved self-adaptive particle swarm optimization..., Decision Support Systems (2017), https://doi.org/10.1016/j.dss.2017.10.005

![](/api/attachments/BWHX3Z5A/fulltext/images/bee7aca2ecd3497c8f9c216dec81a7a185b5875f9e7121e1ab8c474e29888339.jpg)  
(a) With risk control.

![](/api/attachments/BWHX3Z5A/fulltext/images/cd011e9d2027a1cd54b7633ff7ad464e8acb1e3078e8295658116d04212c6477.jpg)  
(b) Without risk control.  
Fig. 18. Nemenyi post-hoc test for the models PAA-MS-IDPSO-V using 25, 50 and 100 particles for all analyzed stocks.

risk when compared to other models, including PAA-IDPSO and SAX-GA [6].

According to Nguyen et al. [14], several variations of optimization algorithms have been proposed in the literature, but most of them do not present a real improvement. However, different approaches have both positive and negative aspects. Therefore, Nguyen et al. [14] advocate that working with hybrid and multi-swarms approaches is probably the best strategy. In a recent article [28], the multi-swarms algorithms were classified into two types: collaborative and concurrent. Thus, the primary contribution of this work was to investigate the use the multi-swarm approach with a hybrid architecture. In its training1 stage, the sub-swarms work concurrently (not sharing the information between the particles), whereas in the training2 stage they work in a collaborative way.

Furthermore, the validation set was used in the validation stage to avoid overfitting. The use of a validation set is frequent in classification tasks, but little used and investigated in the swarm optimization area [13]. Still, Nguyen et al. state that few works in the swarm optimization area are used in real-world problems, leaving a gap that was explored in this work, using real S&P100 stocks.

As future works, we intend to investigate the optimization of PAA parameters (the size of the window and the number of segments) and the use of new and more sophisticated decision rules. We also suggest investigating the use of portfolio optimization to allow the system to operate in multiple stocks and the use of dynamic optimization algorithms for recognizing and tackling changes in the market [14].

## Acknowledgments

The authors would like to thank CNPq, FACEPE (Brazilian Research Agencies) and QS Intelligence - Attendance<sup>®</sup> for their financial support.

![](/api/attachments/BWHX3Z5A/fulltext/images/790a45fa3918964c3018c41e1e31ddf4dde45c51023406bf993f575754d819ca.jpg)  
Fig. 19. Nemenyi post-hoc test for the PAA-MS-IDPSO-V with and without risk control, using 50 particles

Please cite this article as: R. Brasileiro et al., Automatic trading method based on piecewise aggregate approximation and multi-swarm of improved self-adaptive particle swarm optimization..., Decision Support Systems (2017), https://doi.org/10.1016/j.dss.2017.10.005

## References

[1] G.E. Box, G.M. Jenkins, G.C. Reinsel, Time Series Analysis: Forecasting and Control, vol. 734. John Wiley & Sons. 2011.

[2] K.S. Kannan, P.S. Sekar, M. Sathik, P. Arumugam, Financial stock market forecast using data mining techniques, Proceedings of the International Multiconference of Engineers and Computer Scientists, IMECS 2010 vol. 1, 2010. pp. 555–559.

[3] P.S. Cowpertwait, A.V. Metcalfe, Introductory Time Series with R, Springer Science & Business Media. 2009.

[4] T. chung Fu, A review on time series data mining, Eng. Appl. Artif. Intel. 24 (2011).164-181

[5] M.M.M. Fuad, P.-F. Marteau, Towards a Faster Symbolic Aggregate Approximation Method, 2013, arxiv:1301.5871.

[6] V.L.F. Souza, R.C. Brasileiro, A.L.I. Oliveira, A PAA-PSO technique for investment strategies in the financial market, Neural Networks (IJCNN), 2015 International Joint Conference On, 2015. pp. 1–8.

[7] A. Canelas, R. Neves, N. Horta, A new SAX-GA methodology applied to investment strategies optimization, Proceedings of the 14th Annual Conference on Genetic and Evolutionary Computation, GECCO ’12, ACM. 2012, pp. 1055–1062.

[8] R.C. Brasileiro, V.L.F. Souza, B.J.T. Fernandes, A.L.I. Oliveira, Automatic method for stock trading combining technical analysis and the artificial bee colony algorithm, Evolutionary Computation (CEC), 2013 IEEE Congress On, IEEE. 2013, pp. 1810–1817.

[9] L.A. Teixeira, A.L.I. Oliveira, A method for automatic stock trading combining technical analysis and nearest neighbor classification, Expert Syst. Appl. 37 (2010) 6885–6890.

[10] A. Canelas, R. Neves, N. Horta, A SAX-GA approach to evolve investment strategies on financial markets based on pattern discovery techniques, Expert Syst. Appl. 40 (2013) 1579–1590.

[11] R.C. Cavalcante, R.C. Brasileiro, V.L. Souza, J.P. Nobrega, A.L.I. Oliveira, Computational intelligence and financial markets: a survey and future directions, Expert Syst. Appl. 55 (2016) 194–211.

[12] Y. Zhang, X. Xiong, Q. Zhang, An improved self-adaptive PSO algorithm with detection function for multimodal function optimization problems, Math. Probl. Eng. 2013 (2013)

[13] C. Tuite, A. Agapitos, M. ONeill, A. Brabazon, Tackling overfitting in evolutionary-driven financial model induction, Natural Computing in Computational Finance, Springer. 2011, pp. 141–161.

[14] T.T. Nguyen, S. Yang, J. Branke, Evolutionary dynamic optimization: a survey of the state of the art, Swarm Evol. Comput. 6 (2012) 1–24.

[15] L.A. Becker, M. Seshadri, Comprehensibility & overfitting avoidance in genetic programming for technical trading rules, Technical Trading Rules, Worcester Polytechnic Institute, Comp. 2003.

[16] D. Cabrera-Paniagua, C. Cubillos, R. Vicari, E. Urra, Decision-making system for stock exchange market using artificial emotions, Expert Syst. Appl. 42 (2015) 7070–7083.

[17] P. Zhang, X. Zhu, Y. Shi, L. Guo, X. Wu, Robust ensemble learning for mining noisy data streams, Decis. Support. Syst. 50 (2011) 469–479.

[18] L.-J. Kao, C.-C. Chiu, C.-J. Lu, C.-H. Chang, A hybrid approach by integrating wavelet-based feature extraction with MARS and SVR for stock index forecasting, Decis. Support. Syst. 54 (2013) 1228–1244.

[19] T. Geva, J. Zahavi, Empirical evaluation of an automated intraday stock recommendation system incorporating both market data and textual news, Decis. Support. Syst. 57 (2014) 212–223.

[20] N. Oliveira, P. Cortez, N. Areal, Stock market sentiment lexicon acquisition using microblogging data and statistical measures, Decis. Support. Syst. 85 (2016) 62–73.

[21] Y. Shynkevich, T. McGinnity, S.A. Coleman, A. Belatreche, Forecasting move ments of health-care stock prices based on different categories of news articles using multiple kernel learning, Decis. Support. Syst. 85 (2016) 74–83.

[22] E. Keogh, K. Chakrabarti, M. Pazzani, S. Mehrotra, Dimensionality reduction for fast similarity search in large time series databases, Knowl. Inf. Syst. 3 (2001) 263–286.

[23] K. Chakrabarti, E. Keogh, S. Mehrotra, M. Pazzani, Locally adaptive dimensionality reduction for indexing large time series databases, ACM Trans. Database Syst. 27 (2002) 188–228.

[24] M. Kamosi, A.B. Hashemi, M.R. Meybodi, A hibernating multi-swarm optimization algorithm for dynamic environments, Nature and Biologically Inspired Computing (NaBIC), 2010 Second World Congress On, IEEE. 2010, pp. 363–369.

[25] A. Khan, M. Sadeequllah, et al. Rank based particle swarm optimization, International Conference on Swarm Intelligence, Springer. 2010, pp. 275–286.

[26] S. Feuerriegel, H. Prendinger, News-based trading strategies, Decis. Support. Syst. 90 (2016) 65–74

[27] J. Demšar, Statistical comparisons of classifiers over multiple data sets, J. Mach. Learn. Res. 7 (2006) 1–30

[28] M. Mavrovouniotis, C. Li, S. Yang, A survey of swarm intelligence for dynamic optimization: algorithms and applications, Swarm Evol. Comput. 33 (2017) 1–17.

Rodrigo C. Brasileiro received the B.S. in Information Systems from Integrated College of Recife in 2009 and the M.Sc. degree in Computer Science from Federal University of Pernambuco, Recife, Brazil in 2013. Currently, he is a Ph.D. candidate in Computer Science at Federal University of Pernambuco. His research interests include Swarm Intelligence, Concept Drift, Time Series Forecasting, and Data Mining.

Victor L.F. Souza received the B.S. and M.Sc. degrees in Computer Science from Federal University of Pernambuco, Recife, Brazil in 2013 and 2015, respectively. Currently, he is a Ph.D. candidate in Computer Science at Federal University of Pernambuco. His research interests include Artificial Neural Networks, Deep Learning, Concept Drift Time Series Forecasting, Swarm Intelligence and Data Mining.

Adriano L.I. Oliveira obtained his B.Sc. degree in Electrical Engineering and M.Sc. and Ph.D. degrees in Computer Science from the Federal University of Pernambuco, Brazil, in 1993, 1997 and 2004, respectively. In 2011 he joined the Center for Informatics at Federal University of Pernambuco as an Assistant Professor. He was an Assistant Professor at Federal Rural University of Pernambuco from 2009 to 2011 and at the Department of Computing Systems of Pernambuco State University from 2002 to 2009. He has published over 110 articles in scientific journals and conferences and one book. He is a Senior Member of the IEEE. His current research interests include neural networks, machine learning, pattern recognition, data mining, and applications of these techniques to time series analysis and forecasting, information systems, software engineering, and biomedicine.

Please cite this article as: R. Brasileiro et al., Automatic trading method based on piecewise aggregate approximation and multi-swarm of improved self-adaptive particle swarm optimization..., Decision Support Systems (2017), https://doi.org/10.1016/j.dss.2017.10.005

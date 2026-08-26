---
otero_id: 17735
otero_key: "RQ2YE4WH"
title: "An intelligent approach to time series identification by a neural network-driven decision tree classifier"
authors: "Kun Chang Lee; Sang Bong Oh"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(95)00031-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An intelligent approach to time series identification by a neural network-driven decision tree classifier $^{1}$

Kun Chang Lee $^{a}$ , Sang Bong Oh $^{b}$

$^{a}$ School of Business Administration, Sung Kyun Kwan University, Myung Ryun-Dong, 3-53, Jongno-Ku, Seoul 110-745, South Korea $^{b}$ Department of Information and Communication Engineering, Taejon University, Taejon 300-716, South Korea

## Abstract

The objective of this paper is to suggest a new intelligent approach to classifying a time series into one of autoregressive moving-average (ARMA) models, which is named time series identification (TSI), by using a neural network-driven decision tree classifier. The main recipe of our approach is to apply two pattern recognition concepts for solving the TSI problem. The first pattern recognition concept is an extended sample autocorrelation function which is derived from a given times series data and is used as an important feature for solving the TSI problem. The second pattern recognition concept is a neural network-driven decision tree classifier which is a main vehicle for reducing the complexities involved in TSI problems and, finally, providing the most promising ARMA model for a given time series. The neural network-driven decision tree classifier consists of a set of nodes at which neural network-driven decision making is made whether the connecting subtrees should be pruned or not. To enhance the performance of our proposed classifier, we suggest a neural pruning search algorithm which is used to find the promising paths. The proposed search algorithm essentially results in a neural network-driven search through the space of possible terminal nodes of the classifier. Experimental results with a set of real time series data show that the proposed approach can efficiently identify the time series patterns with high precision compared to other approaches.

Keywords: Time series identification; ARMA model; Extended sample autocorrelation function; Pattern matching; Decision tree classifier; Neural pruning search algorithm

## 1. Introduction

A great deal of data arising in business is observed in the form of a time series which is a collection of observations made sequentially in time. The special features of a time series are that the data are ordered with respect to time, and that successive observations are usually expected to be dependent. It will be helpful to distinguish between a time series process and a time series realization. The observed time series is an actual realization of an underlying time series process. By a realization we mean a sequence of observed data points, and not just a single observation. In this paper, we will analyze a discrete type of time series that is composed of measurements or readings made at predetermined and equally or almost equally spaced time intervals. The objectives of analyzing a time series are as follows:

1. Understanding the features of a particular time series process.

2. Constructing a model to explain the time series behavior.

3. By using the results of (1) or (2), forecasting the behavior of the series in the future.

4. Controlling the time series process by examining either what might happen when we alter some of the parameters or when the process deviates from a target by more than a prescribed amount.

In this paper, we primarily focus on the objectives specified in (1) and (2), both of which are based on the assumption that there is a sufficient momentum in the time series process to ensure that past and future behavior will be the same. Recently, connectionist researchers proved that recurrent neural network approaches for robust time series forecasting can outperform conventional ARMA method [26]. However, they cannot deny the usefulness of the TSI problem because the result of TSI task can be used as a starting point for selecting the context vector size of recurrent neural networks [26].

In this paper, major emphasis will be placed on the univariate modeling which models a time series process with a single variable. The ARMA process or model proposed by Box and Jenkins [7] is a typical one of univariate time series models. The ARMA model is made up of two linear filters: autoregressive (AR) filter and moving average (MA) filter. Indeed, finding the nature of the filters is equivalent to constructing an appropriate model for a particular time series, which is termed TSI hereafter. Many time series actually encountered in industry or business exhibit nonstationary behavior and do not vary about a fixed mean. In particular, although the level about which fluctuations occur may be different at different times, the broad behavior of the time series may be similar when differences in level are allowed for. Such stationary behavior may be obtained by differencing the autoregressive operator. In this paper, any time series is assumed to be differenced into a stationary time series. In view of the arguments so far, it is self-evident that TSI indicates determining order p and q of ARMA(p,q) model by considering statistical properties of the time series under consideration. A stationary time series process $Z_{t}$ following ARMA $(p,q)$ model can be denoted as follows:

$$
\begin{array}{r l} Z _ {t} & = \phi_ {1} Z _ {t - 1} + \dots + \phi_ {p} Z _ {t - p} + a _ {t} - \theta_ {1} a _ {t - 1} \\ & \quad - \dots - \theta_ {q} a _ {t - q}, \end{array}\tag{1}
$$

where $a_{t}$ represents normally distributed, mutually independent, random variables with zero mean and variance $\sigma^{2}$ , and $\phi$ and $\theta$ are parameters to be estimated, respectively. To date, many researchers in the field of statistics have proposed a wide variety of TSI methods [1,4,7,22,24,36,38,48,49,54]. It cannot be denied that their studies have substantially contributed for the development of methodologies usable for solving TSI. However, considering the fact that decision rules developed in these approaches are based on complicated statistics, it seems natural that they are lack of user-friendliness or practicability which is essential for modern managerial decision making.

To overcome this drawback, we suggest the use of pattern recognition techniques because TSI problem consists of a lot of pattern recognition procedures [7]. In this sense, we propose a neural network-driven decision tree classifier in which two pattern recognition techniques are tightly coupled: (1) neural network, and (2) decision tree classifier (DTC). These two pattern recognition techniques are all based on the notion of pattern matching. A time series can be appropriately assigned to one of the ARMA models whose prototype pattern best matches with the pattern of the time series. We obtain the pattern of the time series via the extended sample autocorrelation function (ESACF) approach [48] which can yield an operative pattern specific to the time series being considered.

Neural network has been applied to a wide range of information-processing activities, such as associative memory, pattern classification, pattern clustering, and function approximation $[37]$ . In this paper, neural network is utilized as a tool for providing neural decision values to each node in DTC. The DTC approach divides the complex decision processes of TSI into a set of simple and local decisions in a hierarchical manner. The DTC technique has been widely used as an efficient tool for solving various problems of pattern recognition, such as geoscience and remote sensing [47,55], speech analysis [16], biomedical applications [13,42], and recognition of a large set of characters [23,50,51]. However, it appears that few studies have applied DTC to classifying time series patterns [33].

Based on the arguments so far, the objectives of this paper are as follows:

1. To propose neural network-driven DTC for solving TSI problem.

2. To suggest a tree search algorithm for finding the best path in the classifier.

In the neural network-driven DTC, the TSI problem can be stated as solving a set of local decisions at nodes. Neural decision values are computed at each node to find the promising path in the neural network-driven DTC. Many researches exist which have tried to find the best path in a DTC $[27,28,30]$ . For this purpose, we develop a neural network-driven decision function to compute decision values at each node in a neural network-driven DTC. Based on those decision values, a tree search algorithm is developed to prune unlikely paths at an early stage of the tree search, which is named a neural pruning search (NPS) algorithm. Therefore, our proposed neural network-driven DTC is activated by the NPS algorithm to find the promising path and solve the given TSI problem.

This paper is structured as follows. Section 2 presents the characteristics of the pattern recognition-based approach to TSI problem. Details of the neural network-driven DTC are shown in section 3. Section 4 presents theoretical parts of NPS algorithm. Experimental results with a set of real and simulated time series data are described in Section 5. In Section 6, this paper is ended with some concluding remarks.

## 2. Pattern recognition

## 2.1. Previous studies

The extension of classical pattern recognition techniques to experimental time series data has been a problem of great practical interest. A series of observations indexed in time often produces a pattern which may form a basis for discriminating between different classes of events. Typical applications of pattern recognition to the classification of time series patterns can be found initially in geophysical and acoustic applications covering mostly either seismic or speech pattern recognition problems [2,5,6,12,35,40,43,53]. The problem of discriminating between a pattern generated by signal plus noise and a pattern generated by noise alone has been analyzed extensively in the engineering literature [17,41]. An important application in medicine is to the problem of discriminating between different classes of brain wave recordings. Electroencephalogram (EEG) time series have been used to discriminate among sleep stages or to predict the onset of epileptic seizures. Gevins et al. [21] have summarized the applications of discriminant analysis to EEG data. Gersh et al. [20] have investigated EEG classification methods based on characterizing group differences in terms of autoregressive models. Studies on parsing the waveforms derived from biomedical fields have been made in Refs. [45,46,52]. Special pattern recognition application to time series data is found in Ref. [18], where a method of classifying objects is reported based on the autoregressive model parameters which represent the shapes of boundaries detected in digitized binary images of the objects. The work is not a direct application of pattern recognition to time series data, but the original intent is focused on recognizing some complicated objects via transforming the shapes of those objects into relevant time series data and obtaining AR parameters.

As discussed above, most of pattern recognition applications to time series data have been concentrated on engineering studies such as seismology, speech recognition, EEG pattern recognition, waveform analysis, biomedical recognition, and object recognition, etc. However, there exist a few studies applying pattern recognition to OR/MS decision problems $[3,19,25–27,33–35]$ . Fogler $[19]$ applied pattern recognition techniques to pre-classify economic time series data into more homogeneous groups so as to obtain better economic forecasting and planning. Major emphasis was placed on regression analysis. Basilevsky and Hum $[3]$ have utilized the Karhunen–Loeve technique, one of pattern recognition techniques for extracting relevant features, in order to decompose a Jamaican plantation births series into trend, cycle, and seasonality. Therefore, Fogler [19] and Basilevsky and Hum [3] have nothing to do with the TSI problem which basically deals with ARMA model identification.

Our approach differs from Lee and Jhee [31] in the sense that the neural network-driven DTC is used a major inference engine for solving TSI problem, while they apply a two-staged training procedure for enhancing the generalization capability of backpropagation neural networks. Collopy and Armstrong [15] used a rule-based approach for the more robust combination of forecasts, whose research interest is different from ours. Chu and Widjaja [14] and Chakraborty et al. [10] have used backpropagation neural networks for forecasting method selection and multivariate forecasting, respectively. However, our neural network-driven DTC approach is applied to the TSI problem, and uses a backpropagation neural network as a decision-making function to find the promising paths in DTC.

## 2.2. Two phases of pattern recognition

Two phases of pattern recognition are: (1) feature extraction phase, and (2) pattern classifier (or classification) phase. Fig. 1 depicts the two phases of pattern recognition when applied to the TSI problem.

In the feature extraction phase, features are extracted from the original data via statistical approaches or algorithmic approaches. Then those features are organized into forming a pattern vector. The use of features reduces the dimensionality of the original data and consequently the amount of memory required for storing the prototype patterns. In this sense, we apply statistical methods to extract features from a given time series. We select features statistically via iterative optimization method, called ESACF [48]. The features obtained are organized into a pattern which is to be classified appropriately. To understand the property of extracted features more clearly, it seems necessary to investigate the nature of ESACF extraction approach.

The ESACF extraction approach begins with the assumption that the time series data $Z_{t}$ are generated by an ARMA $(p,q)$ process, where p and q are unknown. For p=q, the value of the kth ESACF at lag j is defined as the sample autocorrelation of an estimate of the moving average portion of the ARMA $(k,q)$ process under the assumption q=j. The approach yields consistent estimates of the true autoregressive parameters for $j\geq q$ and p=k. Through iterative OLS (Ordinary Least Squares) procedures, the ESACF extraction approach can be characterized by arranging the set of extended sample autocorrelations corresponding to various values of p and q in a two-dimensional table. The extended sample autocorrelations in each row correspond to a fixed value of p, and those in each column correspond to a fixed value of q. If the row of the ESACF table is numbered 0, 1, 2, ..., to specify the order of AR process and the column is similarly numbered to specify the order of MA process, then the ESACF values within two standard deviations will form a triangle with boundaries given by the lines k=p and j-k=q. The row and column coordinates of the triangle vertex correspond to tentative estimates of the AR order p and MA order q, respectively. In TSI problem, a pattern class represents one of the ARMA models. A pattern is also a vector whose elements are composed of binary numbers transformed from the ESACF values. The ESACF value is transformed into 1 when it lies between two standard deviations and otherwise transformed into 0. A triangular shape is observed in Table 1 where the prototype ESACF of ARMA $(2,2)$ model is illustrated. The underlined numbers represent the boundary points of the corresponding triangular pattern. It is noted that in Table 1 there exists only one triangular pattern. However, in practice, such an ideal case rarely occurs. Specifically, a time series with seasonality often yields a number of triangular patterns. However, the ESACF pattern has been proved to be very useful for resolving TSI problems with pattern recognition-based decision support schemes [25,31-34].

![](/api/attachments/RQ2YE4WH/fulltext/images/c888b4f3a5735ac108aff44a6a03ecf1a4dbd13228a3a2d01a9ebe4846b4ead8.jpg)  
Fig. 1. Two phases of pattern recognition.

Table 1

<table><tr><td>MAR</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td> $\underline{0}$ </td><td> $\underline{0}$ </td><td> $\underline{0}$ </td><td> $\underline{0}$ </td><td> $\underline{0}$ </td><td> $\underline{0}$ </td><td> $\underline{0}$ </td><td> $\underline{0}$ </td><td> $\underline{0}$ </td></tr><tr><td>2</td><td>0</td><td> $\underline{0}$ </td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>3</td><td>0</td><td>0</td><td> $\underline{0}$ </td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>4</td><td>0</td><td>0</td><td>0</td><td> $\underline{0}$ </td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>5</td><td>0</td><td>0</td><td>0</td><td>0</td><td> $\underline{0}$ </td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>6</td><td>0</td><td>0</td><td>0</td><td>C</td><td>0</td><td> $\underline{0}$ </td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>7</td><td>0</td><td>0</td><td>0</td><td>C</td><td>0</td><td>0</td><td> $\underline{0}$ </td><td>1</td><td>1</td><td>1</td></tr><tr><td>8</td><td>0</td><td>0</td><td>0</td><td>C</td><td>0</td><td>0</td><td>0</td><td> $\underline{0}$ </td><td>1</td><td>1</td></tr><tr><td>9</td><td>0</td><td>0</td><td>0</td><td>C</td><td>0</td><td>0</td><td>0</td><td>0</td><td> $\underline{0}$ </td><td>1</td></tr></table>

In the pattern classifier phase, the ESACF pattern derived from input time series is classified into an appropriate pattern class or ARMA model. For this purpose, we suggest a neural network-driven DTC in which neural network functions play the role of providing decision values at each node. Based on the decision value, optimal path from a root node to a terminal node can be found in such a manner that only likely paths are tried by pruning unlikely paths at an early stage of the search. To formalize this sort of search process, we develop a NPS algorithm. In the following Sections 3 and 4, we discuss the detail of the neural network-driven DTC followed by the rigorous formalization of the proposed NPS algorithm.

## 3. Neural network-driven DTC

## 3.1. Basics of DTC

In order to facilitate the subsequent discussions, we first state a few frequently used definitions about DTC.

Definition 1. A decision function $f$ at node $x$ is a $k$ -tuple neural network function $k \geq 2$ ,

$$
f _ {x} \colon X \to [ 0, 1 ] ^ {k},
$$

where X is the input and the k-tuple is decision values $v(x_{i})$ of the outgoing branches $(x, x_{i})$ , i = 1, $\ldots, k$ , where $x_{i}$ is the ith son of node x.

Definition 2. A decision tree $T(\text{root})$ is a tree with root such that an internal node i has a corresponding k-tuple decision function $f_{i}$ .

![](/api/attachments/RQ2YE4WH/fulltext/images/70d5d81afe2086f9f3ed45ea10f22ff8588784e1e50980d0278c2b1cf515589c.jpg)  
Fig. 2. DTC for solving the TSI problem.

Definition 3. A decision path $(x,y)$ in a tree is the path from node x to node y. A decision path x is the decision path $(\text{root},x)$ . A decision path $(w,x,\ldots,y,z)$ is the path from node w via nodes $x,\ldots,y$ to node z.

Definition 4. Decision value at node x or $v(x)$ is given by a neural network function attached to that node.

Definition 5. The (decision) value $V(x)$ of a decision path x is the same as a decision value at node x. That is, $V(x) = v(x)$ .

## 3.2. Extension into the neural network-driven DTC

Decision value $V(x)$ of a decision path x depends on the decision function $f_{x}$ at node x. Lee and Park [33] proposed the use of a fuzzy decision function in DTC. However, such approach does not have the capability of learning the given patterns, which results in the lack of robustness when faced with the unknown patterns. In this respect, we propose using the neural network as a decision function at each node of DTC. The neural network model we used in this paper is based on the backpropagation learning [39] with bipolar input. That is, 0 and 1 are transformed into -0.5 and 0.5, respectively. Neural decision values play the role of providing intelligence to the tree search algorithm. In this respect, we suggest the following DTC depicted in Fig. 2.

There are 10 internal nodes such as $T(\text{root})$ , $T(\text{pure})$ , $T(\text{mixed})$ , $T(\text{MA})$ , $T(\text{AR})$ , and $T(\text{ARMA}^*)$ . There exist 35 terminal nodes. For example, terminal nodes AR(1), AR(2), AR(3), AR(4), AR(5) are attached to the internal node $T(\text{AR})$ . Similarly, terminal nodes MA(1), ..., MA(5) are connected to the internal node $T(\text{MA})$ . Terminal nodes ARMA(1,1), ARMA(1,2), ARMA(1,3), ARMA(1,4), ARMA(1,5) are linked to the internal node $T(\text{ARMA1}^*)$ . Similar explanation may be applied to the remaining internal nodes $T(\text{ARMA2}^*)$ , $T(\text{ARMA3}^*)$ , $T(\text{ARMA4}^*)$ , $T(\text{ARMA5}^*)$ . Therefore, each terminal node represents one of ARMA models considered. As an ESACF pattern of unknown time series passes through the DTC above, promising paths are selected based on the neural decision values at internal nodes.

Finally, when the ESACF pattern is reached at some terminal nodes, evaluation process is performed to select the most possible terminal node on the basis of the neural decision values computed at each terminal node. In case that a certain neural decision value is largest at a terminal node ARMA(1,1), the unknown time series is then classified into ARMA(1,1) model. Based on the neural network-driven DTC above, we propose a NPS algorithm and prove its theoretical rigorousness in the following Section 4.

## 4. Neural pruning search algorithm

In this section, we will describe the theoretical aspects of the proposed NPS algorithm which is a DTC search algorithm to find the promising paths in a given DTC for TSI problem.

## 4.1. Background

Two types of DTC search algorithm have been defined in [27,28,30], in which search algorithms depend on the risk function $r$ . In the first type called S-admissible search [50], $r(s^{*})$ of a terminal node $s^{*}$ is a function of only those features measured along the path from root to $s^{*}$ . In the second type called B-admissible search, $r(s^{*})$ is a function of all the measurements from the sample. There are two problems associated with these two algorithms:

1. Many paths have to be tried before the optimal terminal node $s^{*}$ is found. This is because the algorithms investigate the paths until they are found nonoptimal.

2. Since tight bounds for the risk function $r(s^{*})$ are not easily found, the number of paths which have to be tried in the early stage may be very large, making the tree search very inefficient.

Another DTC search algorithm, branch-bound-backtrack (BBB), was proposed in [11], where a decision function $f_x$ is assigned to each internal node $x$ . BBB search algorithm was proposed to search for the terminal node $s^*$ with the largest decision value which exceeds a given threshold S. The DTC model used in [11] is characterized by flexibility of the number of internal and terminal nodes. The primary advantage of BBB search algorithm is that it has an effective backtracking mechanism leading to the optimal solution while requiring only $O(\log n)$ time, where n is the number of terminal nodes. However, the BBB search algorithm is also inefficient in the sense that it searches a path until proving it nonoptimal before backtracking.

## 4.2. Content

The essence of the NPS algorithm lies in the fact that nonoptimal or unlikely paths are pruned at an earlier stage of the tree search based on the neural decision values. Assume that a decision value at root node, $v(\text{root})$ , equals one. Detailed procedures of the NPS algorithm are presented in the following:

Algorithm: Neural Pruning Search.

Goal: To find the best path and corresponding decision values with a given neural network-driven DTC.

Input: I (ESACF pattern of an unknown time series), T(root).

Output: Potential terminal node.

1. Create a potential node list PNL and a terminal node list TNL that are initially empty.

2. Compute neural decision values at internal nodes “pure” and “mixed”, that is, $v(\text{pure})$ and $v(\text{mixed})$ .

3. If $v(\text{pure}) > v(\text{mixed})$ , then do begin search $T(\text{pure})$ ; prune $T(\text{mixed})$ ; end; Else if $v(\text{pure}) < v(\text{mixed})$ , then do begin search $T(\text{mixed})$ ; prune $T(\text{pure})$ ; end;

4. Calculate the neural decision values for nodes in PNL.

5. Put into TNL the terminal node with the most neural decision value computed in Step 4.

Procedures for searching the subtrees $T(\text{pure})$ and $T(\text{mixed})$ are as follows:

Procedure SearchPureSubtree:

Input: ESACF pattern I and T(pure).

Output: Potential AR or MA terminal node.

1. Compute $v(\mathrm{MA})$ and $v(\mathrm{AR})$ .

2. If $v(\mathrm{MA}) > v(\mathrm{AR})$ , then do
begin
    search $T(\mathrm{MA})$ for a terminal node with the
    most neural decision value;
    prune $T(\mathrm{AR})$ ;
end;
Else if $v(\mathrm{MA}) < v(\mathrm{AR})$ , then do
begin
    search $T(\mathrm{AR})$ for a terminal node with the
    most neural decision value;
    prune $T(\mathrm{MA})$ ;

end;

3. Put the selected terminal node into PNL.

Procedure SearchMixedSubtree:
Input: ESACF pattern I and T(mixed).
Output: Potential ARMA terminal node.

1. Compute $v(\mathrm{ARMA1}^*)$ , ..., $v(\mathrm{ARMA5}^*)$ .

2. If $v(\text{ARMAp}^{*})$ is the most, $(p = 1, \ldots, 5)$ search $T(\text{ARMAp}^{*})$ ;
prune $T(\text{ARMAk}^{*})$ , where $p \neq k$ ;

3. Put the selected terminal node into PNL.

It is necessary to investigate the correctness of the NPS algorithm given above, where the correctness means that the proposed algorithm terminates within a limited number of iterations, yielding a desired and intended output for a correct input [11]. The correctness of a tree search algorithm can be therefore proved by investigating whether the algorithm satisfies the three criteria of Termination, Completeness, and Validity [11]. To prove the correctness of NPS algorithm, we propose the following theorem:

Theorem: The NPS algorithm is correct.

Let us prove this theorem by the following three criteria.

1. Termination: Since $T(\text{root})$ is finite as is shown in Fig. 2, the algorithm terminates in a finite number of steps.

2. Completeness: Every correct input yields an output. By examining all the exits of NPS, some value is always returned when exiting. Hence, the algorithm satisfies the criterion of completeness.

3. Validity: Every output is the output intended.

The proof of validity can be broken down into a few lemmas for clarity.

Lemma 1: For a path x, $V(x)$ is always defined by a neural decision function assigned to node x.

Proof: By definition 5, $V(x)$ is a decision value at node x, indicating that $V(x)$ exists for any path x. Therefore, $V(x)$ is always defined.

Lemma 2: At any time before NPS algorithm terminates, there exists a node $n'$ on an optimal path from node $x$ to a potential terminal node $n_k$ .

Proof: Let the ordered sequence $n_{0}, n_{1}, \ldots, n_{k}$ be an optimal path from x to $n_{k}$ . We know that NPS algorithm has already found an optimal path to $n'$ since $n'$ is on an optimal path $(x, n_{k})$ . Therefore, terminal node $n_{k}$ exists on the optimal path $(x, n_{k})$ .

Lemma 3: If there exists a path from x to a potential terminal node $n_{k}$ , NPS terminates by finding an optimal path.

Proof: Suppose that NPS algorithm does not terminate even when there exists a path $(x,n_{k})$ . This indicates that there does not exist $n'\in\text{path}(x,n_{k})$ , contradicting lemma 2. Therefore, lemma 3 is proved.

As a result, NPS algorithm is correct since the three lemmas above are proved.

## 5. Experiments

In this section, both experimental procedures and results are presented in detail. In Section 5.1, the design of the neural network models is extensively discussed. Section 5.2 shows how we prepared a set of training data and test data for our experiments. Training procedures are described in Section 5.3, including the test results and comparative results with other approach recently published. Section 5.4 summarizes performance of our proposed approach to TSI problems. While all the experimental results in Sections 5.3 and 5.4 are obtained by using a large number of simulated time series data, experimental results with a set of real time series data are shown in Section 5.5. Additional topics related to our approach are discussed in Section 5.6.

## 5.1. Neural network design

As shown in Fig. 2, there exist 10 internal nodes including the root node $T(\text{root})$ in our proposed DTC. Therefore, 10 neural networks have to be trained so that neural decision values may be appropriately provided at each node. The architecture of neural network for each node is summarized in Table 2.

The issues involved in the architecture of neural networks are handled in the following way:

(1) We adopt one hidden layer. This is based on our notion that one hidden layered neural network can provide the sufficient classification power needed at each node.

(2) Since most time series data observed in the real world falls within the ARMA(5,5) model, we use 6 by 6 ESACF patterns. The number of input nodes for all the neural networks is then equal to 36. Meanwhile, the number of output nodes depends on the number of subpaths emanating from the corresponding node. For example, both PMNET and PURENET have 2 output nodes because they have two subpaths. Contrarily, the other neural networks possess 5 output nodes because they all have 5 subpaths or terminal nodes.

Table 2  
The architecture of neural network

<table><tr><td>Neural network alias</td><td>Corresponding node in DTC</td><td>Number of input nodes</td><td>Number of hidden nodes</td><td>Number of output nodes</td></tr><tr><td>PMNET</td><td> $T(\text{root})$ </td><td>36</td><td>36</td><td>2</td></tr><tr><td>PURENET</td><td> $T(\text{pure})$ </td><td>36</td><td>36</td><td>2</td></tr><tr><td>MIXEDNET</td><td> $T(\text{mixed})$ </td><td>36</td><td>36</td><td>5</td></tr><tr><td>ARNET</td><td> $T(\text{AR})$ </td><td>36</td><td>36</td><td>5</td></tr><tr><td>MANET</td><td> $T(\text{MA})$ </td><td>36</td><td>36</td><td>5</td></tr><tr><td>MIX1NET</td><td> $T(\text{ARMA1}^{*})$ </td><td>36</td><td>36</td><td>5</td></tr><tr><td>MIX2NET</td><td> $T(\text{ARMA2}^{*})$ </td><td>36</td><td>36</td><td>5</td></tr><tr><td>MIX3NET</td><td> $T(\text{ARMA3}^{*})$ </td><td>36</td><td>36</td><td>5</td></tr><tr><td>MIX4NET</td><td> $T(\text{ARMA4}^{*})$ </td><td>36</td><td>36</td><td>5</td></tr><tr><td>MIX5NET</td><td> $T(\text{ARMA5}^{*})$ </td><td>36</td><td>36</td><td>5</td></tr></table>

(3) We adopt 36 hidden nodes, which is equal to the number of input nodes unless the performance of each neural network does not seriously deteriorate below the predetermined level.

(4) Bipolar sigmoid function is used as an activation function.

Since real time series data are usually contaminated by a wide variety of noise, it is necessary to train the neural networks to the degree of being robust against unexpected noise in the test data. In this sense, noises are added into a prototype ESACF pattern by randomly inverting 3, 5, 10 binary values, which are respectively corresponding to 10%, 20%, and 30% noise level. The prototype ESACF pattern is considered to have 0% noise level. Also we restrict the number of noise in the triangle of ESACF pattern representing ARMA $(p,q)$ model to be less than or equal to MAX $(0,5-p-q)$ so that we may not break the triangular shape of the prototype ESACF pattern too much.

## 5.2.Data

For each of 10 neural networks, we prepared the following four sets of training data:

1. The 1st training data set is solely composed of prototype ESACF patterns which are free from noise.

2. The 2nd training data set consists of the 1st training data set plus three 10% noisy patterns for each of the 1st training patterns.

3. The 3rd training data set is composed of the 2nd training data set plus three 20% noisy patterns for each of the 1st training patterns.

4. The 4th training data set is composed of the 3rd training data set plus three 30% noisy patterns for each of the 1st training patterns.

It is noteworthy that the number of training patterns for each of 10 neural networks varies because each neural network must be trained to solve its own local problem in DTC. For example, the number of 1st training patterns (i.e., prototype patterns) for PMNET is 35 because those training patterns are generated from ESACF patterns related with 35 ARMA models (ARMA(0,0) model is excluded since it is a trivial model). Similarly, the number of 1st training patterns for PURENET is 10 because the training patterns are derived from ESACF patterns with respect to 5 AR models and 5 MA models. The number of 1st training patterns for MIXEDNET is 25 because MIXEDNET must train those ESACF patterns originating from 25 mixed ARMA models. Table 3 summarizes the number of training patterns for each of 10 neural networks.

Two types of test will be performed after training the 10 neural networks: (1) the individual neural network test, and (2) the global DTC test. The first type of test, named local test, is to check the performance of each neural network and see whether it can yield an appropriate neural decision value at each node of DTC or not. The second type of test, named global test, is to investigate the performance of the global DTC and ascertain whether it can correctly classify unknown time series pattern or not.

Table 3  
Number of training patterns for each of 10 neural networks

<table><tr><td>Neural network alias</td><td>1st training data set</td><td>2nd training data set</td><td>3rd training data set</td><td>4th training data set</td></tr><tr><td>PMNET</td><td>35</td><td>140</td><td>245</td><td>350</td></tr><tr><td>PURENET</td><td>10</td><td>40</td><td>70</td><td>100</td></tr><tr><td>MIXEDNET</td><td>25</td><td>100</td><td>175</td><td>250</td></tr><tr><td>ARNET</td><td>5</td><td>20</td><td>35</td><td>50</td></tr><tr><td>MANET</td><td>5</td><td>20</td><td>35</td><td>50</td></tr><tr><td>MIX1NET</td><td>5</td><td>20</td><td>35</td><td>50</td></tr><tr><td>MIX2NET</td><td>5</td><td>20</td><td>35</td><td>50</td></tr><tr><td>MIX3NET</td><td>5</td><td>20</td><td>35</td><td>50</td></tr><tr><td>MIX4NET</td><td>5</td><td>20</td><td>35</td><td>50</td></tr><tr><td>MIX5NET</td><td>5</td><td>20</td><td>35</td><td>50</td></tr></table>

60 test data sets are prepared for each individual neural network so that we perform the local test. Those 60 test data sets are sum of 20 test data sets generated from the three noise levels 10%, 20%, 30%. The number of test patterns in each test data set is equal to that of the 1st training data set. To perform the global test, 5 test data sets are prepared for each of the three noise levels, totalling 15 test data sets for the global test. Each test data set consists of 35 test patterns for 35 ARMA models which are considered in this paper.

## 5.3. Results I (local training and tests)

The binary values of 0 or 1 in the ESACF patterns were transformed into -0.5 and 0.5, respectively, since our learning algorithm is based on the bipolar input form and the bipolar sigmoid function. Learning rate and momentum were set to 0.25 and 0.9, respectively. We terminated training process when the mean squared error (MSE) becomes below the predetermined error bound of 0.005. We suggest an iterative training strategy, which is similar to the step-by-step training strategy [31]. Its three steps are as follows:

Step 1) Let training data set index i = 1, where i = 1,2,3,4. Train each neural network with the ith training data set until MSE reaches the predetermined error bound.

Step 2) Calculate performance of the trained neural network by testing with 60 test data sets generated from the three noise levels. Stop training when classification accuracy of the trained neural network reaches about 95% for the three noise levels. If fails, goto step 3.

Step 3) Train again the neural network trained in step 1 with the $(i+1)$ th training data set. If i=4, then terminate training process. Otherwise, goto step 2.

By adopting this iterative training approach, we are able to not only reduce the ambiguities inherent in the ESACF patterns, but also increase the robustness of the trained neural network against unknown test patterns. Our training performance in the local tests is summarized in Table 4. To help readers understand the meaning of our experiments, let us focus on the training and test phases in Table 4. PMNET was iteratively trained with all the four training data sets, until test performance is over about 95%. Neural networks with asterisk indicate that it converges above the predetermined error bound. Nevertheless, test performance is very satisfactory as shown in Table 4.

Table 4  
Training and test results (local tests)

<table><tr><td rowspan="2">Neural network alias</td><td colspan="3">Training phase</td><td colspan="3">Test phase (classification accuracy)</td></tr><tr><td>Data set</td><td># of epochs</td><td>MSE</td><td>10% noise</td><td>20% noise</td><td>30% noise</td></tr><tr><td rowspan="4">PMNET</td><td>1st</td><td>100</td><td>.0048</td><td>.953</td><td>.854</td><td>.768</td></tr><tr><td>2nd</td><td>12</td><td>.0017</td><td>.960</td><td>.868</td><td>.814</td></tr><tr><td>3rd</td><td>71</td><td>.0042</td><td>.965</td><td>.948</td><td>.891</td></tr><tr><td>4th</td><td>31</td><td>.0047</td><td>.977</td><td>.947</td><td>.941</td></tr><tr><td>PURENET</td><td>1st</td><td>5</td><td>.0038</td><td>.995</td><td>.995</td><td>.990</td></tr><tr><td rowspan="4">MIXEDNET</td><td>1st</td><td>40000*</td><td>.0161</td><td>.978</td><td>.902</td><td>.896</td></tr><tr><td>2nd</td><td>20</td><td>.0049</td><td>.980</td><td>.920</td><td>.908</td></tr><tr><td>3rd</td><td>10</td><td>.0038</td><td>.988</td><td>.976</td><td>.930</td></tr><tr><td>4th</td><td>5</td><td>.0037</td><td>.986</td><td>.976</td><td>.964</td></tr><tr><td>ARNET</td><td>1st</td><td>100*</td><td>.0177</td><td>.990</td><td>.990</td><td>.960</td></tr><tr><td>MANET</td><td>1st</td><td>100*</td><td>.0151</td><td>.990</td><td>.970</td><td>.950</td></tr><tr><td>MIX1NET</td><td>1st</td><td>100*</td><td>.0151</td><td>.990</td><td>.970</td><td>.990</td></tr><tr><td>MIX2NET</td><td>1st</td><td>100*</td><td>.0152</td><td>.980</td><td>.980</td><td>.930</td></tr><tr><td>MIX3NET</td><td>1st</td><td>100*</td><td>.0156</td><td>.990</td><td>.980</td><td>.960</td></tr><tr><td>MIX4NET</td><td>1st</td><td>100*</td><td>.0136</td><td>.970</td><td>.950</td><td>.940</td></tr><tr><td>MIX5NET</td><td>1st</td><td>100*</td><td>.0123</td><td>.990</td><td>.990</td><td>.970</td></tr></table>

Legend: \* MSE converges before it reaches the predetermined error bound.

Table 6
Application to series C [7]  
Table 5  
Test results (global tests)

<table><tr><td rowspan="2">Noise level</td><td colspan="5">Test set</td><td rowspan="2">Average performance</td><td rowspan="2">MLP2H with NFN [31]</td></tr><tr><td>1st</td><td>2nd</td><td>3rd</td><td>4th</td><td>5th</td></tr><tr><td>10%</td><td>88.6</td><td>97.1</td><td>97.1</td><td>97.1</td><td>97.1</td><td>95.4</td><td>96.7</td></tr><tr><td>20%</td><td>88.6</td><td>88.6</td><td>88.6</td><td>100.0</td><td>88.6</td><td>90.9</td><td>89.7</td></tr><tr><td>30%</td><td>85.7</td><td>85.7</td><td>88.6</td><td>88.6</td><td>85.7</td><td>86.9</td><td>80.8</td></tr><tr><td>Average</td><td>87.6</td><td>90.5</td><td>91.4</td><td>95.2</td><td>90.5</td><td>91.1</td><td>89.1</td></tr></table>

## 5.4. Results II (global tests)

Average classification accuracy of the global tests is summarized in Table 5. As noted in 5.2., “global” means our neural network-driven DTC itself. As seen in Table 5, the average performance deteriorates with the increase of noise level from 10% to 30%, which is consistent with the experimental findings appeared in [31]. Our neural network-driven DTC approach is similar to [31] in that both are using neural network approach. However, our approach is more systematic in that the TSI problem can be decomposed by our DTC approach into a set of small local decision problems which neural networks are able to deal more effectively than other neural network-based approaches. Comparative results are shown in the last right column in Table 5, showing that our approach is more robust in case of high level of noise.

<table><tr><td colspan="7">Application to series C [7]</td></tr><tr><td colspan="7">(a) Feature values</td></tr><tr><td>MA</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>AR</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>0</td><td>.98</td><td>.94</td><td>.90</td><td>.85</td><td>.80</td><td>.75</td></tr><tr><td>1</td><td>.81</td><td>.66</td><td>.55</td><td>.48</td><td>.43</td><td>.38</td></tr><tr><td>2</td><td>-.03</td><td>-.03</td><td>-.11</td><td>-.06</td><td>.02</td><td>-.01</td></tr><tr><td>3</td><td>-.50</td><td>.01</td><td>-.07</td><td>-.11</td><td>-.01</td><td>.00</td></tr><tr><td>4</td><td>-.24</td><td>-.25</td><td>-.05</td><td>-.11</td><td>-.01</td><td>.03</td></tr><tr><td>5</td><td>-.48</td><td>.28</td><td>-.29</td><td>-.07</td><td>.04</td><td>-.04</td></tr><tr><td colspan="7">(b) ESACF pattern</td></tr><tr><td>MA</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>AR</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>3</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td></tr><tr><td>4</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td></tr><tr><td>5</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td></tr><tr><td colspan="7">(c) Optimal path</td></tr><tr><td colspan="7">T(root): (0.766789, 0.240525) → search T(pure) path and prune T(mixed) pathT(pure): (0.964571, 0.034410) → search T(AR) path and prune T(MA) pathT(AR): (0.073394, 0.886671, 0.068760, 0.057454, 0.082070) → AR(2) model is appropriate</td></tr></table>

## 5.5. Applications to real data

Example 1.

An ARMA(2,0) model has been suggested for the series C in [7]. Table 6 shows the ESACF pattern, optimal path, potential terminal node, and the determined model. ARMA(2,0) model is verified.

## Example 2.

An ARMA(1,1) model was suggested for the series A in [7]. The classification results in Table 7 also confirm ARMA(1,1) model.

## 5.6. Discussion

The proposed NPS algorithm may misclassify the input pattern if it follows a wrong path at an earlier stage. This is because the current NPS algorithm does not have a backtracking mechanism which enables the input pattern to escape from the wrong paths. We are now developing an efficient backtracking mechanism in which neural network and DTC is integrated within a fuzzy framework. However, it is noteworthy that the degree of wrong classification at any node depends on the recognition power of neural network function attached to it.

Competitive learning techniques such as ART (Adaptive Resonance Theory) [8,9] or Kohonen's SOFM (Self-Organizing Feature Maps) [29] may be also applied to partition the input patterns into appropriate ARMA class. However, experiments show that those classification results from applying competitive learning techniques are usually very poor due to a high level of noises hidden in the input time series pattern. In this sense, competitive learning techniques can be used only as a preprocessing tool for solving TSI problem. Sörheim [44] proposed integration of backpropagation neural network and competitive learning technique (i.e., ART) to obtain more robust ARMA forecast.

It is unnecessary to perform the comparative works with the statistical TSI methods in order to prove the external validity of our proposed approach. The reasons are: (1) our approach is based on artificial intelligence methods, (2) other TSI methods use statistical inference procedures, and (3) the previous works using intelligent approaches to TSI problem [25,32–34] have already proved that artificial intelligence-based approaches to TSI problem can yield more robust results than the existing statistical TSI methods.

Table 7
Application to series A [7]

<table><tr><td colspan="7">Application to series A [7]</td></tr><tr><td colspan="7">(a) Feature values</td></tr><tr><td>MAAR</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>0</td><td>.92</td><td>.77</td><td>.61</td><td>.52</td><td>.54</td><td>.63</td></tr><tr><td>1</td><td>.74</td><td>.22</td><td>-.44</td><td>-.88</td><td>-.39</td><td>.12</td></tr><tr><td>2</td><td>.75</td><td>.20</td><td>-.35</td><td>-.58</td><td>-.37</td><td>.13</td></tr><tr><td>3</td><td>.91</td><td>.88</td><td>.84</td><td>.82</td><td>.80</td><td>.80</td></tr><tr><td>4</td><td>-.50</td><td>.02</td><td>-.06</td><td>.12</td><td>-.04</td><td>-.06</td></tr><tr><td>5</td><td>-.48</td><td>-.27</td><td>.00</td><td>.13</td><td>-.04</td><td>-.02</td></tr><tr><td colspan="7">(b) ESACF pattern</td></tr><tr><td>MAAR</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>2</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>3</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>4</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>5</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td></tr><tr><td colspan="7">(c) Optimal path</td></tr><tr><td colspan="7">T(root): (0.044413, 0.956034) → search T(mixed) path and prune T(pure) path</td></tr><tr><td colspan="7">T(mixed): (0.703633, 0.462708, 0.000415, 0.111319, 0.00000) → search ARMA(1,*) terminal nodes and prune ARMA(p,*) terminal nodes where T(ARMA1*): (0.832901, 0.192837, 0.049526, 0.065783, 0.061780) → ARMA(1,1) model is appropriate</td></tr></table>

## 6. Concluding remarks

In this paper, we proposed a neural network-driven DTC approach for solving the TSI problem. Its solution process heavily relies upon two pattern recognition-based decision support mechanisms: (1) ESACF approach for extracting patterns, and (2) the notion of pattern matching for determining an appropriate model. To find the optimal path in the DTC, a NPS algorithm was proposed which uses the neural decision values at each node. The proposed approach differs sharply from traditional TSI methods in that: (1) the notion of pattern matching is applied to facilitate the procedure of classifying the time series patterns, (2) a DTC is used to divide the complex TSI process into a number of simple decision making problems at each node, and (3) neural network is utilized to intelligently guide the tree search. The robustness of our approach is verified by theoretical proofs as well as the experimental result that the test time series data which have been rigorously studied in the literature are correctly identified by our approach. In this case, one of expected advantages is that the size of patterns derived from a particular time series is usually small compared to that of original measurements of the time series. This has an important implication that the computational burden in applying pattern recognition techniques to TSI problems is relatively small compared with the traditional TSI approaches.

## References

[1] H. Akaike, A New Look at the Statistical Model Identification, IEEE Transactions on Automatic Control 19 (1974) 716–723.

[2] F.M. Anglin, Discrimination of Earthquakes and Explosions Using Short Seismic Array Data, Nature 223 (1971) 51–52.

[3] A. Basilevsky and D.P.J. Hum, Karhunen–Loeve Analysis of Historical Time Series With an Application to Plantation Births in Jamaica, Journal of the American Statistical Association 74, No. 366 (June 1979) 284–290.

[4] J.M. Beguin, C. Gourieroux and A. Monfort, Identification of a Mixed Autoregressive Moving Average Process: The Corner Method, in: O.D. Anderson, Ed., Time Series (Amsterdam, North-Holland, 1980) 423–436.

[5] A. Booker and W. Mitronovas, An Application of Statistical Discrimination to Classify Seismic Events, Bulletin Seismological Society America 54 (1964) 961–977.

[6] R.E. Boucher and J.P. Noonan, Adaptive Detection and Removal of Non-Gaussian Spikes for Gaussian Data, IEEE Transactions on Pattern Analysis and Machine Intelligence 4, No. 2 (1982) 132–136.

[7] G.E.P. Box and G.M. Jenkins, Time Series Analysis-Forecasting and Control (Holden-Day, San Francisco, 1970).

[8] G.A. Carpenter and S. Grossberg, A Massively Parallel Architecture for a Self-Organizing Neural Pattern Recognition Machine, Computer Vision, Graphics, and Image Processing 37 (1987) 54–115.

[9] G.A. Carpenter and S. Grossberg, ART2: Self-Organization of Stable Category Recognition Codes for Analog Input Patterns, Applied Optics 1 (1987) 4919–4930.

[10] K. Chakraborty, K. Mehrotra, C.K. Mohan, and S. Ranka, Forecasting the Behavior of Multivariate Time Series Using Neural Networks, Neural Networks 5 (1992) 961–970.

[11] R.L.P. Chang and T. Pavlidis, Fuzzy Decision Tree Algorithms, IEEE Transactions on Systems Man and Cybernetics 7 (1977) 28–35.

[12] C.H. Chen, Adaptive and Learning Algorithms for Seismic Detection of Personnel, IEEE Transactions on Pattern Analysis and Machine Intelligence 4, No. 2 (1982) 129–132.

[13] C.J. Chen and Q.Y. Shi, Shape Features for Cancer Cell Recognition, in: Proceeding of 5th International Conference on Pattern Recognition (1980) 579–581.

[14] C.H. Chu and D. Widjaja, Neural Network System for Forecasting Method Selection, Decision Support System 12 (1994) 13–24.

[15] F. Collopy and J.S. Armstrong, Rule-Based Forecasting: Development and Validation of an Expert Systems Approach to Combining Time Series Extrapolations, Management Science 38 (1992) 1394–1414.

[16] G.R. Dattatreya and V.V.S. Sarma, Decision Tree Design for Pattern Recognition Including Feature Measurement Cost, in: Proceeding of 5th International Conference on Pattern Recognition (1980) 1212–1214.

[17] W.B. Davenport and W.L. Root, An Introduction to the Theory of Random Signals and Noise (McGraw-Hill, New York, 1958).

[18] S.R. Dubois and F.H. Glanz, An Autoregressive Model Approach to Two-Dimensional Shape Classification, IEEE Transactions on Pattern Analysis and Machine Intelligence 8, No. 1 (1986) 55–66.

[19] H.R. Fogler, A Pattern Recognition Model for Forecasting, Management Science 20, No. 8 (April 1974) 1178–1189.

[20] W. Gersh, J. Yonemoto, and P. Naitoh, Automatic Classification of Multivariate EEGs Using an Amount of Information Measure and the Eigen Values of Parametric Time Series Model Features, Computers and Biomedical Research 10 (1977) 297–318.

[21] A.S. Gevins, C.L. Veager, S.L. Diamond, J. Spire, G. Zeitlin, and A. Gevins, Automated Analysis of the Electrical Activity of the Human Brain (EEG): A Progress Report, Proceeding of IEEE 63 (1975) 1382–1399.

[22] H.L. Gray, A.G. Kelly and D.D. McIntire, A New Approach to ARMA Modelling, Communications in Statistics B7 (1978) 1–77.

[23] Y.K. Gu, Q.R. Wang and C.Y. Suen, Application of Multilayer Decision Tree in Computer Recognition of Chinese Characters, IEEE Transactions on Pattern Analysis and Machine Intelligence 5 (1983) 83–89.

[24] D.C. Hamilton and D.G. Watts, Interpreting Partial Autocorrelation Functions of Seasonal Time Series Models, Biometrika 65 (1978) 135–140.

[25] W.C. Jhee, K.C. Lee and J.K. Lee, A Neural Network Approach for the Identification of the Box-Jenkins Model, Network 3 (1992) 323–329.

[26] W.C. Jhee and J.K. Lee, Performance of Neural Networks in Managerial Forecasting, Intelligent Systems in Accounting, Finance and Management 2 (1993) 55–71.

[27] L.N. Kanal, On Hierarchical Classifier and Interactive Design, in: P.R. Krishnaiah, Ed., Applications of Statistics (North-Holland, Amsterdam, 1977) 301–321.

[28] L.N. Kanal, Problem-Solving Models and Search Strategies for Pattern Recognition, IEEE Transactions on Pattern Analysis and Machine Intelligence 1 (1979) 193–201.

[29] T. Kohonen, Self-Organization and Association Memory. 2nd Ed. (Springer-Verlag, Berlin, 1988).

[30] A.V. Kulkarni and L.N. Kanal, Admissible Search Strategy for Parametric and Nonparametric Hierarchical Classifiers, in: Proceeding of 4th International Conference on Pattern Recognition (1978) 238–248.

[31] J.K. Lee and W.C. Jhee, A Two-Stage Neural Network Approach for ARMA Model Identification with ESACF, Decision Support Systems 11 (1994) 461–479.

[32] K.C. Lee and S.J. Park, Decision Support in Time Series Modeling by Pattern Recognition, Decision Support Systems 4 (1988) 199–207.

[33] K.C. Lee and S.J. Park, A Knowledge-Based Fuzzy Decision Tree Classifier for Time Series Modeling, Fuzzy Sets and Systems 33 (1989) 1–18.

[34] K.C. Lee and S.J. Park, PRTSM: Pattern Recognition-Based Time Series Modeler, Computer Science in Economies and Management 2 (1989) 239–254.

[35] H.H. Liu and K.S. Fu, A Syntactic Approach to Seismic Pattern Recognition, IEEE Transactions on Pattern Analysis and Machine Intelligence 4, No. 2 (March 1982) 136–140.

[36] S.M. Pandit and S.M. Wu, Time Series and System Analysis with Applications (John Wiley and Sons, 1983).

[37] Y.H. Pao, Pattern Recognition and Neural Networks (Addison-Wesley, 1988).

[38] E. Parzen, ARMA Models for Time Series Analysis and Forecasting, Journal of Forecasting 1 (1982) 67–82.

[39] D.E. Rumelhart, G.E. Hinton and R.J. Williams, Learning Internal Representations by Error Backpropagation, in: D.E. Rumelhart, D.E. and J.L. McClelland, Eds., Parallel Distributed Processing: Explorations in the Microstructure of Cognition, Vol. I: Foundations (MIT Press, MA, 1986).

[40] C.S. Sarna and H. Stark, Pattern Recognition of Waveforms Using Modern Spectral Estimation Techniques and Its Application to Earthquake/Explosion Data, in: Proceeding of 5th International Conference on Pattern Recognition (December 1980) 1–4.

[41] I. Selin, Detection Theory, Princeton University Press (Princeton, 1965).

[42] Q.Y. Shi, A Method for the Design of Binary Tree Classifiers, in: Proceeding of IEEE Conference on Image Processing and Pattern Recognition (1981) 21–26.

[43] R.H. Shumway, Discriminant Analysis for Time Series, P.R. Krishnaiah and L.N. Kanal, Eds., Handbook of Statistics, Vol.2 (North-Holland Publishing, 1982) 1–46.

[44] E. Sorheim, A Combined Network Architecture Using ART2 and Backpropagation for Adaptive Estimation of Dynamical Processes, Proceedings of the 24th Annual Hawaii International Conference on Systems Science (HICSS), Vol. 2 (1991) 468–475.

[45] G.C. Stockman, Waveform Parsing System, P.R. Krishnaiah and L.N. Kanal, Eds., Handbook of Statistics, Vol. 2 (North-Holland Publishing, 1982) 527–548.

[46] G.C. Stockman, L.N. Kanal and M.C. Kyle, Structural Pattern Recognition of Carotid Pulse Waves Using a General Waveform Parsing Systems, Communications of the ACM 19 (December 1976).

[47] P.H. Swain and H. Hauska, The Decision Tree Classifier: Design and Potential, IEEE Transactions on Geoscience and Electronics 15 (1977) 142–147.

[48] R.S. Tsay and G.C. Tiao, Consistent Estimates of AR Parameters and ESACF for Stationary and Nonstationary ARMA Models, Journal of American Statistical Association 79 (1984) 84–96.

[49] W.T. Tucker, On the Pade Table and Its Relationship to the R and S Arrays and ARMA Modelling, Communications in Statistics A11 (1982) 1335–1379.

[50] Q.R. Wang and C.Y. Suen, Analysis and Design of a Decision Tree Based on Entropy Reduction and Its Application to Large Character Set Recognition, IEEE Transactions on Pattern Analysis and Machine Intelligence 6 (1984) 406–417.

[51] Q.R. Wang and C.Y. Suen, Large Tree Classifier with Heuristic Search and Global Training, IEEE Transactions on Pattern Analysis and Machine Intelligence 9 (1987) 91–102.

[52] W.R. Valenzuela and A. Klinger, Pattern Recognition Applied to Monitory Waveforms, IEEE Transactions on Biomedical Engineering 22 (1975) 18–24.

[53] J.J. Wolf, Speech Recognition and Understanding, in: K.S. Fu, Ed., Digital Pattern Recognition (Springer-Verlag, Berlin, 1976) 167–203.

[54] W.A. Woodward and H.L. Gray, On the Relationship between S-Array and the Box--Jenkins Method of ARMA Model Identification, Journal of American Statistical Association 76 (1981) 579–587.

[55] K.C. You and K.S. Fu, An Approach to the Design of a Linear Binary Tree Classifier, in: Proceeding of 3rd Symposium on Machine Processing of Remotely Sensed Data (Purdue University, June–July, 1976) 1–10.

![](/api/attachments/RQ2YE4WH/fulltext/images/fbfa1dc2a01b9d52a0152e2222f497b2d62f20d9bb3252acd9f27a7fdc998221.jpg)

Kun Chang Lee is a professor in Management Information Systems at Sung Kyun Kwan University. He received a B.A. degree in 1982 from Sung Kyun Kwan University (Korea), and a M.S. in 1984 and a Ph.D. in MIS in 1988 from the Department of Management Science at Korea Advanced Institute of Science and Technology (KAIST). Professor Lee's publications have appeared or will be shown in Decision Support Systems, Fuzzy Sets and Systems, Computer Sci

ence in Economics and Management, Network, Expert Systems, Decision Sciences, Intelligent Systems in Accounting Finance and Management. He has presented papers at several international conferences including Hawaii International Conference on Systems and Science (HICSS), Int'l Joint Conference on Neural Networks (IJCNN), IEEE Conference on Systems, Man, and Cybernetics, Int'l Society of DSS Conference. His research interests include decision support systems, expert systems, and synergism of expert systems and neural networks, and fuzzy logic-driven decision makings.

![](/api/attachments/RQ2YE4WH/fulltext/images/5cb3e09d74c6159c844a884dd7c28c9b466d20a8be5194c0e35e40c2cee83213.jpg)

Sang Bong Oh is an assistant professor in the Department of Information and Communication Engineering at Taejon University. He received B.A. from Seoul National University, M.S. and Ph.D. in Expert Systems from Korea Advanced Institute of Science and Technology. He has written a book on expert systems (in Korean) and several papers in International Social Work, Fuzzy Sets and Systems, Expert Systems with Applications: An International Journal, Information

Processing Letters. He is interested in AI/ES applications to managerial problems, AI algorithms, and integration of expert systems, neural networks, and fuzzy systems.

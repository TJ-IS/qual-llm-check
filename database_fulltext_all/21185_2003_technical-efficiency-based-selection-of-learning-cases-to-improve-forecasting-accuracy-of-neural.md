---
otero_id: 21185
otero_key: "YNSUY9NE"
title: "Technical efficiency-based selection of learning cases to improve forecasting accuracy of neural networks under monotonicity assumption"
authors: "Parag C. Pendharkar; James A. Rodger"
year: "2003"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00138-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Technical efficiency-based selection of learning cases to improve forecasting accuracy of neural networks under monotonicity assumption

Parag C. Pendharkar <sup>a,</sup>\*, James A. Rodger <sup>b</sup>

<sup>a</sup>Information Systems, School of Business Administration, Capital College, Pennsylvania State University, 777 W. Harrisburg Pike, Middletown, PA 17057 4898, USA

<sup>b</sup>MIS and Decision Sciences, Eberly College of Business and Information Technology, Indiana University of Pennsylvania, Indiana, PA 15705, USA

Accepted 3 July 2002

## Abstract

In this paper, we show that when an artificial neural network (ANN) model is used for learning monotonic forecasting functions, it may be useful to screen training data so the screened examples approximately satisfy the monotonicity property. We show how a technical efficiency-based ranking, using the data envelopment analysis (DEA) model, and a predetermined threshold efficiency, might be useful to screen training data so that a subset of examples that approximately satisfy the monotonicity property can be identified. Using a health care forecasting problem, the monotonicity assumption, and a predetermined threshold efficiency level, we use DEA to split training data into two mutually exclusive, ‘‘efficient’’ and ‘‘inefficient’’, training data subsets. We compare the performance of the ANN by using the ‘‘efficient’’ and ‘‘inefficient’’ training data subsets. Our results indicate that the predictive performance of an ANN that is trained on the ‘‘efficient’’ training data subset is higher than the predictive performance of an ANN that is trained on the ‘‘inefficient’’ training data subset.

<sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Data envelopment analysis; Connectionist models/artificial neural networks; Human resource management

## 1. Introduction

In certain forecasting problems, it is very natural to assume that the forecasting function will satisfy monotonicity property. For example, in financial forecasting models, individual demand is shown to increase with one’s income [37,19]. In the transportation and leisure industries, price of perishable goods such as airline seats and hotel rooms increases monotonically with the consumer demand [25]. A few researchers in information systems have shown that the software development effort monotonically increases with project size and complexity [18]. Several models in economics, operations research, and transportation science are required to satisfy the monotonicity property [20].

For a multivariate input vector $\pmb { x } _ { j } { = } ( x _ { 1 j } , . . . . , x _ { n j } )$ $\forall j { \in } [ 1 , . . . . , k ]$ , and an output $y _ { j } , \mathrm { i f } f ( )$ is a forecasting function that maps the input vector $x _ { j }$ to the output $y _ { j , \ast }$ then for any two input vectors $x _ { 1 }$ and $\boldsymbol { x } _ { 2 }$ and their respective outputs $y _ { 1 }$ and $y _ { 2 } ,$ , the monotonicity property requires that the following conditions must be satisfied.

1. $y _ { 1 } { > } y _ { 2 } { \Leftrightarrow } ( x _ { i 1 } - x _ { i 2 } ) { > } 0 , { \Leftrightarrow } \exists$ at least one $i { \in } [ 1 , . . . . , n ]$ such that $x _ { i 1 } > x _ { i 2 }$ and there is no $i { \in } [ 1 , . . . . , n ]$ such that $x _ { i 1 } < x _ { i 2 }$ , and

$$
2. y _ {1} = y _ {2} \Leftrightarrow (x _ {i 1} - x _ {i 2}) = 0, \forall i \in [ 1, \dots , n ].
$$

The monotonicity property of the forecasting function makes it easy to aggregate forecasts. For example, Quah [37] suggests that if $f _ { 1 } , f _ { 2 } , . . . , f _ { n }$ represent n monotonic individual preference functions, then, for all $i { \in } \{ 1 , . . . . , n \}$ , the market demand function $\left( f _ { \mathrm { m } } \right)$ can be represented as:

$$
f _ {\mathrm{m}} = \sum_ {i = 1} ^ {n} a _ {i} f _ {i}
$$

where $a _ { i } \geq 0$ is the weight associated with individual preference function $f _ { i \cdot }$ Wang [49] notes the importance of monotonicity property in market development and writes $^ { 6 6 } \cdot$ . .growth curves are all monotonic. Monotonicity is a generic characteristic of the market development growth curve, and can be used to regulate the generalization of the trend of a growth curve.’’

For the linear forecasting function, it is easy to check if the function satisfies the monotonicity property. Perhaps some measures such as positive values of regression coefficients can be used to ensure that the learned forecasting function satisfies the monotonicity property. When it is desired to use a nonlinear forecasting function, monotonicity can be preserved by (1) redesigning the learning algorithm so the resulting forecasting function learnt by the nonlinear algorithm preserves monotonicity, or (2) using the training data set that does not violate the monotonicity property. Several nonlinear machine learning forecasting algorithms are available. Examples of nonlinear machine learning algorithms include artificial neural network (ANN), classification and regression tree (CART), and genetic programming (GP). All of these algorithms do not assume any particular functional form of the forecasting function, and learn the nonlinear forecasting function based solely on the properties of the training data set [48].

ANN is a popular nonlinear forecasting method [24]. ANNs have been used for forecasting short-term electric loads [24], daily sales [49], software efforts [18], and forecasting the price of initial public offerings [17]. Since the functional form of the ANN depends on the training data, for learning the monotonic forecasting function using ANN, the training data may have to satisfy the monotonicity property. When training data violate the monotonicity property, some data screening may be required to create a training data subsample that does not violate monotonicity. In a small-size data set, such data screening may not be feasible due to the very small size of the resulting subsample. However, in mid- to large-size data sets, it may be possible to create a subsample that preserves monotonicity. In mid-size data sets, if a subsample that preserves monotonicity is too small, then perhaps a large subsample, not containing all the original training data, may be created with the subsample data that approximately preserves monotonicity. The term approximate monotonicity means that most of the cases in the training subsample satisfy monotonicity property, and a few cases may somewhat violate monotonicity.

The design of the data screening algorithm that may be used to create a subsample is an important issue. It is important that the screening algorithm be nonlinear, preserve monotonicity, and not assume any particular nonlinear functional form. For a multivariate input and one output, the data envelopment analysis (DEA) model seems to satisfy all the requirements. DEA is a nonparametric methodology for production function estimation. The DEA model was first developed by Charnes et al. [9] and later extended by Banker et al. [3]. The DEA model is a nonlinear (piecewise linear), nonparametric model used to measure the efficiency of production units. The DEA model assumes monotonicity of inputs and output, but does not impose any specific form of the production function. Banker and Maindiratta [2] note that DEA estimates are more robust than those obtained from parametric models that postulate a certain structure, such as linear or quadratic form.

In this research, we use DEA as a data screening approach to create a subsample training data set that is ‘‘approximately’’ monotonic. We then use ANN as tool to learn a nonlinear forecasting model. The contribution of our research is twofold: (1) we show how DEA can be used as a methodology to screen training cases, where forecasting models are subject to managerial monotonicity assumption; and (2) we show how ANNs can be applied to forecast the number of employees in the health care industry. Empirical studies are conducted to compare the predictive performance of ANNs to the following sets of data: (1) DEA-based selected training cases, (2) DEA-based rejected training cases, and (3) a combination of DEA-based selected and rejected training cases. We use publicly available data from health care facilities in Pennsylvania to learn about and predict the number of employees based on a set of predictor variables.

The rest of the paper is organized as follows. In Section 2, we provide an overview of DEA and backpropagation ANN models. In Section 3, we review the literature on input data preprocessing for ANN. In Section 4, we provide arguments for using DEA for prescreening input data. In Section 5, we describe the human resource management problem in health care. In Section 6, we describe our data and experiments. In Section 7, we conclude our paper with limitations and directions for future work.

## 2. Overview of DEA and back-propagation ANN

DEA was a technique introduced by Charnes et al. [9] for comparing efficiencies of decision-making units (DMUs). The basic ratio DEA model seeks to determine a subset of k DMUs that determine the envelopment surface when all k DMUs consist of m inputs and s outputs. The envelopment surface was determined by solving k linear programming models (one for each DMU), where all k DMUs appear in the constraints of the linear programming model. Let for DMU $n { \in } [ 0 , . . . , k ] , x _ { m n } { \geq } 0$ denote the mth input value, and $y _ { s n } \ge 0$ denote the sth output value. The envelopment surface is determined by solving the following set of k linear programs:

$$
\text { Max } \xi_ {0} = \frac {\sum_ {s} O _ {s} y _ {s k _ {0}}}{\sum_ {m} I _ {m} x _ {m k _ {0}}} \quad k _ {0} = 1, k\tag{2.1}
$$

subject to:

$$
\frac {\sum_ {s} O _ {s} y _ {s k}}{\sum_ {m} I _ {m} x _ {m k}} \leq 1, \quad \forall k\tag{2.2}
$$

$$
O _ {s}, I _ {m} \geq 0\tag{2.3}
$$

$O _ { s }$ and $I _ { m }$ are output and input multipliers that are determined by the model, respectively. All of the DMUs that have $\xi _ { 0 } = 1$ (Eqs. 2.1–2.3) are deemed efficient and lie on the efficient frontier (envelopment).

ANNs have been applied to numerous nonparametric and nonlinear classification and forecasting problems [17,40]. In an ANN model, a neuron is an elemental processing unit that forms part of a larger network. There are two basic types of ANNs: a single layer (of connections) network and a double layer (of connections) network. A single-layer network, using the perceptron convergence procedure [39], represents a linear forecasting model. A modification of the perceptron convergence procedure can be used to minimize the mean-square error between the actual and desired outputs in a two-layer network [11], which yields a nonlinear, multivariateforecasting model. The back-propagation learning algorithm [38], most commonly used to train multilayer networks, implements a gradient search to minimize the squared error between realized and desired outputs.

Fig. 1 shows a three-layer network that can be used for multivariate forecasting. The number of input layer nodes corresponds to the number of independent variables describing the data. The number of nodes in the hidden layer determines the complexity of the forecasting model and needs to be empirically determined to best suit the data being considered. While larger networks tend to overfit the data, too few hidden layer nodes can hinder learning of an adequate separating region. Although having more than one hidden layer provides no advantage in terms of nature of forecasting accuracy, it can in certain cases provide for faster learning [38].

![](/api/attachments/YNSUY9NE/fulltext/images/21ac9753e9d0e87821011d78acb6c463274a6cc81a472ff0bcb1cff26d2446e0.jpg)  
Fig. 1. A three-layer network used in forecasting.

For any neuron $n _ { k } ,$ its output is determined by one of the following formulas:

$$
h _ {k} = \frac {1}{1 + e ^ {- \sum_ {i = 0} ^ {A} w _ {1 i k} x _ {i}}}
$$

$\forall k = 1 , \hdots B$ if the neuron is in the hidden layer

$$
o _ {k} = \frac {1}{1 + e ^ {- \sum_ {i = 0} ^ {B} w _ {2 i k} h _ {i}}}
$$

$\forall k = 1 , \ldots C$ if the neuron is in the output layer

where $x _ { i }$ is the ith input, $w _ { 1 i k }$ is the strength of connection from the ith input node to the kth hidden node, A is the number of input nodes, B is the number of hidden nodes, $w _ { 2 i k }$ is the strength of connection from the ith hidden node to the kth output node, and C is the number of output nodes. The weights $w _ { 1 0 k }$ and $w _ { 2 0 k }$ are thresholding weights, and $x _ { 0 }$ and $h _ { 0 }$ are both equal to 1. The errors for output and hidden layer units are calculated as follows:

$$
\partial 2 _ {k} = o _ {k} (1 - o _ {k}) (y _ {k} - o _ {k}), \quad \forall k = 1, \dots , C
$$

$$
\partial 1 _ {k} = h _ {k} (1 - h _ {k}) \sum_ {i = 1} ^ {C} \partial 2 _ {i} w _ {2 k i}, \quad \forall k = 1, \dots , B
$$

where $\delta \boldsymbol { 2 } _ { k }$ is the error of units in output layer, $y _ { k }$ is the target output, and $\ S 1 _ { k }$ is the error of units in the hidden layer. The weights between the hidden layer and the output layer, and between the input layer and the hidden layer are adjusted as follows:

$$
\Delta w 2 _ {i k} = \eta \partial 2 _ {k} h _ {i}, \quad \forall i = 0, \ldots B, k = 1, \ldots , C
$$

$$
\Delta w 1 _ {i k} = \eta \partial 1 _ {k} x _ {i}, \quad \forall i = 0, \dots A, k = 1, \dots , B
$$

where g is the learning rate. The network is initialized with small random values for the weights, and the back-propagation learning procedure is used to update the weights as the data are iteratively presented to the input-layer neurons. The weights are updated until some predetermined criterion is satisfied. The number of hidden layer neurons is chosen as twice the number of data inputs, a commonly used heuristic in the literature [32].

Schalkoff [39] suggests that heuristics of ‘‘the more the better’’ could be used as a guide to select the number of hidden nodes in an ANN. Further, a network with a higher number of hidden nodes can always be considered as a special case of the network, with a fewer number of hidden nodes with additional nodes (in the case of an ANN with a higher number of hidden nodes) having connection weights taking values equal to zero. The disadvantages of having too many hidden nodes (two times inputs and above) are excessive training time and memorization of training patterns [39]. Since hidden nodes are one of the parameters that may play a role in ANN performance, we try two configurations, one with the number of hidden nodes equal to the number of inputs + 1, and the other with the number of hidden nodes equal to twice the number of inputs + 1. After some initial experimentation (experiment #1), we identify a better configuration and use it for our DEA-based data preprocessing experimentation (experiment #2). We do admit that better designs, in terms of selecting the number of hidden nodes, are possible but such issues are considered beyond the scope of the current research.

Athanassopoulos and Curram [1] lists the following similarities between ANNs and DEA models:

(1) DEA and ANN are nonparametric models.

(2) Neither DEA nor ANNs make assumptions about the functional form that links its inputs to outputs.

(3) DEA seeks a set of weights to maximize the technical efficiency, whereas ANNs seek a set of weights to derive the best possible fit through observations of the training data set.

In the case of using DEA for preprocessing data for ANNs, DEA eliminates some of the inconsistencies in the data that may hurt the monotonicity assumption. For example, if the training data set consists of two examples with the same inputs but different outputs, the example with a lower output receives a lower technical efficiency. The lower technical efficiency increases the likelihood of eliminating the case with the lower efficiency. For slight difference in outputs, the difference in efficiency between the two examples may be low, and both examples may be included in the training data. However, for large differences in outputs, the case with a lower efficiency may clearly be considered as an outlier (as this may hurt monotonicity assumption) and has higher likelihood of elimination from the ‘‘efficient’’ training data. The possibility of eliminating a low efficiency case from training data set is important when two examples show inconsistency; keeping both examples in the training data set would impair the ANN learning. Because ANN learning is through ‘‘nonparametric, regression-type’’ learning of a nonlinear curve, outliers and inconsistent data impair its learning. DEA models, on the other hand, are not as severe on the training data set, where two examples may show the same input and slightly different output. In such a case, the DEA model would give similar efficiency rating to both cases.

Unpredictability in ANN occurs due to violation of monotonicity property [47]. According to Wang [47] $^ { 6 6 } \cdot \cdot \cdot$ Research has shown that the monotonicity neural network classification model can alleviate the overfitting problem. . .’’. Troutt et al. [44] illustrate that ratio DEA models are consistent with the monotonicity property. For example, in an event where two DMUs have the same inputs and different outputs, the DMU with higher output will receive a higher efficiency score. Selecting the DMU with a higher efficiency score for training ANN will reduce unpredictability as the selection of DMU is consistent with monotonicity property. At first, it may appear that selecting a DMU (hospital) from a different peer group can significantly alter the efficiency results for all the members in the group. Although this is true, the problem is not significant, as change in efficiency scores does not alter the ranking/selection of the DMUs in the group significantly. For example, if DMU<sub>1</sub> has a higher efficiency score than ${ \boldsymbol { \mathrm { D M U } } } _ { 2 }$ before $\mathrm { D M U } _ { 3 }$ was added, then even after the addition of ${ \mathrm { D M U } } _ { 3 } ,$ the efficiency of $\mathrm { D M U } _ { 1 }$ will be higher than $\mathrm { D M U } _ { 2 } .$ . In other words, DEA models do not lead to rank reversal (i.e., an inefficient DMU will appear efficient due to addition of new DMU) due to the addition of new DMUs. The individual efficiency scores may change reflecting the impact of each DMU on the ANN training.

## 3. Literature review of input data preprocessing for ANN

ANNs are data-driven techniques; thus, high-quality training data to the ANN implementation cannot be overstressed. The quality and structure of the input data largely determine the success or failure of an ANN implementation. High-quality data does not necessarily mean data that are free of noise (e.g., errors, inaccuracies, outlying values). In fact, it has been shown that ANNs are highly noise-tolerant in comparison to other forecasting methods. A study comparing the forecasting performance of ANNs to linear regression under circumstances of varying data accuracy concluded that ANN-based forecasts were more robust as the data accuracy degraded [4].

Several studies point out that for ANNs, providing high-quality training input data is not as simple as ‘‘cleaning’’ inaccuracies from data or eliminating extreme outliers. On the contrary, Caudill [7,8] and Pendharkar [34] suggest that a valuable technique for improving the quality of training data is to add noise to the network inputs. The addition of noise is shown to strengthen the generalizability of ANNs, and the absence of noise in the training data forces the network to ‘‘memorize’’ specific patterns rather than abstract the essential features from the examples [13].

Three essential requirements for high-quality training data consist of the following: (1) the data should adequately represent the fundamental features the network must detect in order to obtain correct outputs; (2) the training set should provide sufficient variation to allow generalization and discourage ‘‘memorization’’; and (3) the training data should not contain contradictory examples (i.e., examples with identical inputs but different outputs). In regard to the first and second requirements, Caudill [7] cautions that pattern variations (noise), while helpful in the training process, must be controlled to avoid ‘‘swamping’’ the essential features in the input data. The need to find a balance between these two requirements has been described as the ‘‘noise-saturation dilemma.’’ The dilemma can be expressed in terms of communications theory as follows: some fixed dynamic range will always exist within which the components of a system can operate. That is, any signal below a certain baseline level will become lost in system noise, and any signal above a certain level will cause the components to become saturated at their maximum value. To successfully resolve the noise-saturation dilemma, an ANN must be able to process the dominating patterns without allowing the weaker patterns to become lost in system noise. At the same time, an ANN must be able to process weak patterns without allowing the dominating patterns to saturate the processing units [30].

Several researchers proposed approaches for training task in ANNs. The various approaches can be grouped into the following categories: (1) statistical and other data analysis techniques; (2) data transformation and preprocessing; (3) analysis of feedback obtained by interpreting the connection weights; and (4) hybrid techniques.

Stein [42,43] proposed statistical and numerical approaches that can be useful in selecting and preprocessing training data for ANNs. One approach was to apply significant measures (correlation coefficients and plots) to assess the strength of the relationship between data elements; linear regression was used to examine the degree of contribution a candidate data element makes to the model as a whole. In cases where two data elements were highly correlated, one of the elements was eliminated. Another approach was to calculate correlation coefficients between the error terms of a model prediction and each individual unused candidate variable. A high correlation between an unused variable and the error terms suggested that including that variable in the model might add explanatory power (resulting in improved ANN performance). Data aggregation approaches, such as the use of histograms, were proposed to facilitate inspection of the data. These approaches sometimes revealed unusual characteristics or complex relationships and outliers in the data. Stein pointed out that outliers and odd patterns in the data do not necessarily indicate that data should be eliminated or modified. Such patterns can be indicators of important relationships in the data, and further analysis of these areas can lead to improved input selections as the ANN model is refined.

Several other studies focused on training data transformation and preprocessing. The studies included both formal (applying a nonlinear transform to non-normal data) and heuristic approaches (‘‘If you are unsure about including a certain type of data, include it!’’). A transform was sometimes applied to data when the data did not approximate the normal curve. In general, the ANN performed better when the input data was normally distributed [43]. Other formal techniques for preprocessing included the calculation of intermediate functions and trends. An example of an intermediate function was the use of ratios. It was usually more meaningful and efficient to present a ratio, such as miles per gallon, to the network than to input the individual components, such as miles traveled and gallons consumed. Similarly, an algorithm was used to convert raw data into a form that captures a trend over time [43].

Lawrence [23] proposed the following heuristics for the use of binary and continuous data for training ANNs:

1. For naturally occurring groups, the binary categories are often the best method for determining the correlation.

2. Continuous-valued inputs should never be used to represent unique concepts.

3. For continuous value attributes, breaking them up into groups can be a mistake.

Among other heuristics was the ‘‘leave-k-out’’ technique, which involved the decision of how to handle input samples when relatively few examples are available. The procedure was to train several networks (each with a different subset), including most of the examples, and then test each network with a different subset [23].

In enumerating the three general requirements for high-quality training data above, it was stated that the training data should not contain contradictory examples (i.e., examples with identical inputs but different outputs). This problem was addressed by Versaggi [45]. As a preprocessing issue, an algorithm was developed to deal with conflicting data. Conflicting data exists when two or more input patterns are either identical or very similar, but the two inputs have completely different outputs. Because the patterns being presented are contradictory, the ANN is unable to learn both patterns. In an example described by Versaggi [45], 65% of the original data file consisted of conflicting data [45]. The cause was not attributed to faulty data, but to an incomplete modeling process. When a sufficient number of fields are not included in the model to distinguish between the two output categories, a conflicting-data situation exists and the network trains and tests poorly; however, eliminating portions of the data does not solve the problem. The solution involves reexamining the data model and including the necessary fields, a tedious task when performed manually. To assist with this examination process, an algorithm was developed. With the use of the algorithm to reconstruct the training data, Versaggi [45] obtained a 25% increase in network performance.

Wright [50] proposed a Bayesian approach to eliminating input noise, provided that some model of the noise process exists. According to Wright [50], the input–output function of an ANN, which is modeled as a least square regression, can be probabilistically represented as:

$$
E (y \mid x) = \int y p (y \mid x) d y = f (x)\tag{3.1}
$$

where $E ( y | x )$ is the expectation of $y$ conditioned of input vector $x ,$ and $p ( y | x )$ is the predictive probability density function of the ANN. When an ANN is trained on noisy input data such that $z _ { i } = x _ { i } + \delta$ is the new input vector with a small random noise d added to the original uncorrupted inputs $( x _ { i } )$ , the new expectation for y given input noise can be probabilistically represented as:

$$
E (y \mid z) = \frac {1}{p (z)} \int y p (y \mid z) p (z \mid x) p (x) d y d x\tag{3.2}
$$

where $p ( z | x )$ is the distribution of the noise process. Wright [50] argues that given the prior knowledge of the input noise process, it is possible to obtain an estimate of the posterior distribution on the output. Assuming that the noise is additive Gaussian and $p ( x )$ is slowly varying such that it can be approximated to be uniform, Wright [50] shows that it is possible to reconstruct the regression over the true noiseless input.

A set of studies focused on improving the data model for ANN training by analyzing the feedback obtained by ‘‘interpreting’’ the connection weights of the network’s processing elements. The nature of the ANN paradigm is such that the ‘‘meaning’’ of connection weights is opaque; therefore, it is difficult to assess the relative importance of the input factors used by an ANN to arrive at its conclusions. If such feedback was available, it might be possible to gain better insight into the types of inputs that could enhance the network effectiveness. Several techniques have been developed that attempt to provide an interpretation of the connection weights.

Garson [16] describes a method whereby ‘‘the connection weights from the input layer to hidden nodes to the output layer can be used to partition the relative share of the output prediction associated with each input variable.’’ In other words, the partition is used to make judgements about the relative importance of the various inputs. The method consists of applying an equation that effectively partitions the middle-to-output layer weights of each middle (hidden-layer) node into components associated with each input node. Garson [16] suggests that this method can make ANNs as effective for modeling applications as for pattern matching.

Caudill [7,8] presents a more manually intensive method for interpreting the weights that entails iteratively presenting specific isolated ‘‘features’’ to the trained network and assessing the network’s ‘‘reaction.’’ For example, after training the network to recognize seven letters of the alphabet, various features of the letters (such as the angular top of the letter $\mathrm { A } )$ were presented to the network, and the responses of each node were examined. Through this method, the discriminating features were identified. In both the above-mentioned methods, it was unclear to what degree the technique’s applicability would extend to networks with different architectures and levels of complexity.

One of the most interesting methods of a weightinterpreting technique was the Knowledgetron (KT)

developed by Fu [14,15]. The KT method uses a sophisticated algorithm to walk through the nodes of the network, interpret the connections, and generate a set of ‘if–then’’ rules to match the behavior of the network. These rules can then become the basis for a rule-based expert system. It is particularly noteworthy that the KT technique was able to process the classic ‘‘Iris’’ data set successfully. A set of only five relatively simple rules were generated from ANN trained on the Iris data. In fact, it was found that the generated rules actually outperformed the ANN from which they were generated. Because the Iris data set is not particularly complex, it would be premature to assume that the KT technique would scale to more complex, real-world data sets; however, its performance provides evidence that further research in this area would be worthwhile. From the perspective of the data issue, the production of rules provides a convenient mechanism for evaluating the importance and role of each input data element. This could form the basis for a ‘‘feedback-and-refine’’ iterative process to guide the selection and preprocessing of training data, which might result in improved ANN performance.

From the foregoing discussion, it can be observed that the range of techniques and possibilities for enhancing ANN effectiveness, even limiting the field to consider only the data component, is broad and complex. Many of these techniques require a level of expertise that may prohibit their use in practical situations; however, a growing body of research and applications in the area of hybrid intelligent systems could address this concern.

Medsker [26] has given a summary of many of the hybrid intelligent systems that have been developed in recent years. He states that expert systems and ANNs have characteristics that can complement each other and form the basis for powerful hybrid systems. In Medsker and Turban [27], several examples of expert systems used as front-ends for ANN are reviewed. These hybrid systems essentially automate the tedious work of preprocessing, including organizing data available from cases in a manner required by a specific ANN model. An expert system can also be used to select the best ANN paradigm for the data, or to determine the optimal sample size of training and test sets.

Steib and Weidman [41] elaborated a framework for the development of expert system and hybrid technologies to assist in the improvement of ANN training. Among the experimental questions they posed were those targeting the need for guidelines in the selection of the training data. Using the example of character recognition, they make the point that an expert system is a natural fit for training. They state, ‘‘. . .the expert system trains the neural net with a few [examples], checks for accuracy, and continues training with additional sets if necessary; else it signals completion. Total computer time goes up, but human intervention is diminished. . .A record of the expert system’s training success and failures could begin providing insight into how complete and complex the training set must be relative to the space in which the network will be expected to operate.’’

Genetic algorithms (GAs) are another area of artificial intelligence (AI) application that can add value to the training and data selection tasks. Medsker [26] discusses the developments in hybrid systems of this type and states that most of the work performed in this area focuses on the advantages of employing GAs to search large spaces and find an initial set of parameters for training ANN. Murray [29] describes a number of GA techniques that can be used to select optimal values for data and parameters used in the ANN training process.

Bayesian approaches have been recently used to select the best ANN architecture in a set of several candidate architectures. In particular, Vila [46] used the Bayesian nonlinear regression model comparison procedure to select an ANN architecture under which the training data set achieves the highest level of internal consistency.

Most of the techniques proposed in the literature attempted to increase the generalizability of ANN by removing inconsistent data or by adding random noise in the data. A few researchers illustrated different procedures that may be used to identify the inputs that may significantly (in statistical sense) be related to the output variable. While significant, none of the approaches focused on preserving the monotonicity property of the forecasting function learnt by an ANN. In our research, we propose DEA-based prescreening of ANN data to preserve monotonicity property. Our prescreening approach, while preserving monotonicity, does not hurt nonlinearity of the training data. We view DEA as a complement to other approaches to training data selection. When it is desired to increase generalizability of ANN, DEA may not be an appropriate technique to use. However, when it is desired to preserve monotonicity property, DEA may be a suitable approach for prescreening training data.

## 4. Using DEA for prescreening input data

In this section, we describe a DEA-based approach for selecting the input data. First, we present a simple graphical univariate input case example to show how DEA can be used for screening input data. We then provide a generalized mathematical formulation for a multivariate input vector case.

## 4.1. Univariate input case

Several managerial decision-making problems require the assumption or knowledge of monotonicity [21]. Mathematically, monotonicity, for univariate input, is defined as follows:

$$
[ x _ {1} > x _ {2} ] \leftrightarrow [ f (x _ {1}) > f (x _ {2}) ]
$$

DEA models provide an efficient frontier, which is consistent with monotonicity assumption. In fact, all the efficient DMUs (also called reference set) lie on the efficient frontier, which satisfies monotonicity property. Fig. 2 illustrates several frontiers for a single input and a single output combination. Frontier #1 is the efficient frontier. It can be shown that if DMUs lying on frontier #1 are taken out from the analysis, then frontier #2 becomes the next efficient frontier, and so on. Assuming that all nine DMUs are used, it can be argued that DMUs lying on efficient frontier #1 have an efficiency score equal to 1, and DMUs lying on frontier #2 have an efficiency score of less than 1, but the score is higher than the DMUs lying on frontier #3.

ANNs use a least square error minimizing approach to learn nonlinear forecasting models. If only DMUs lying on frontier #1 are used for training, then it can be argued that the resulting model is guaranteed to have a monotonicity property. In fact, the forecasting model will closely follow frontier #1. If all nine DMUs are used, then there is a likelihood that the monotonicity assumption may be violated and the resulting model may produce forecasts that are not consistent with the assumption of monotonicity. Fig. 3 illustrates two forecasting models. The first model (least square forecast #1) is an approximate model that may be learnt by an ANN if DMUs lying on frontier #1 and frontier #2 are used for training. The second model (least square forecast #2) is an approximate model that may be learnt by an ANN if all nine DMUs are used for training.

Let DMUs<sub>1</sub>, $\mathrm { D M U s } _ { 2 } ,$ , and $\mathrm { D M U s } _ { 3 }$ represent the DMUs lying on frontiers #1, #2, and #3, respectively, and P(MonotonicityjDMUs<sub>i</sub>) represent conditional probability that monotonicity assumption is satisfied, if DMUs lying on frontier $i { \in } \{ 1 , 2 , 3 \}$ are used for training ANN. Based on the aforementioned discussion, we can argue the following: P(MonotonicityjD-$\mathrm { D M U s _ { 1 } } ) { > } P ( \mathrm { M o n o t o n i c i t y } | \mathrm { D M U s _ { 1 } } , \ \mathrm { D M U s _ { 2 } } ) { > } P ( \mathrm { M o - } \ \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - } \mathrm { D - }$ onotonicity $| \mathrm { D M U s } _ { 1 }$ , DMUs<sub>2</sub>, DMUs<sub>3</sub>). In other words, probability of a monotonic forecasting function learnt by an ANN decreases when cases that have lower DEA-based efficiency are used in the training data.

![](/api/attachments/YNSUY9NE/fulltext/images/1fd3bd87f510f929e53c29cd6f67921a740f3dc64f5f546647293ac6c30b21d5.jpg)  
Fig. 2. A set of piecewise linear frontiers.

![](/api/attachments/YNSUY9NE/fulltext/images/51e329b6427df07fd190868a26db78a726400bd54c57aa88fe73f1d8bdad0fbe.jpg)  
Fig. 3. Two approximate forecasting surfaces.

## 4.2. Generalized multivariate input vector case

The aforementioned arguments can be easily generalized to a multivariate input vector case. For example, if an example contains n inputs and one output, then two-dimensional figures, such as Figs. 2 and 3, can be drawn by replacing the Input variable on the x-axis by a composite input defined as follows,

$$
\text { Input } = \sum_ {i = 1} ^ {n} w _ {i} x _ {i}
$$

where $x _ { i }$ is the ith input and $w _ { i }$ is the nonnegative weight associate with the ith input. The exact values of the weights, given the data, can be calculated by the DEA model.

In summary, we can conclude that when ANN forecasting models are subject to managerial monotonicity assumption, and training data set is large, using DEA for selecting training data would reduce the ANN training time (as a result of fewer data) and reduce the probability of violation of monotonicity assumption. The heuristic to remove the cases from the large data set is to remove the cases that have lower relative efficiency. This is similar to removing cases lying on frontier #3 in our univariate case example, and deleting lower efficiency outliers in multivariate input cases.

## 5. Human resource management problem in health care

Human resource management represents significant expense to an organization [28]. Among the responsibilities of a human resource department is the task of solving the problems of workforce utilization, organizational development, performance measurement, and adaptation to evolving business demands [28]. The inappropriate management of human resources for a health care facility involves the risk of delays and the inability to deliver quality care [35]. The delays and poor quality assurance translate into a weakened position of the company, both in terms of cost and quality care.

Among the factors that determine the human resource requirements in health care industry are the number of patients, available physical resources and capacity, the type of hospital, and the types of services offered by the hospital [35]. Because recruitment schedule and budget decisions are based on managerial estimates, we focus on the impact of the different factors on the human resource estimation. In reality, the human resource estimation depends on several complex variables (including the ones identified above), the relationships of which are often unclear. Given the lack of information on the interrelationships of the various variables, it becomes difficult to establish any specific parametric form of human resource requirement dynamics. Based on the review of ANN literature, we believe that an ANN model can be used to discover the nonparametric and nonlinear relationships among the various predictor variables.

Top 5 DRGs in PA Hospitals  
![](/api/attachments/YNSUY9NE/fulltext/images/ea0faa6d19806576244e74fe6417753476522f30b3095fbff40c48517c205886.jpg)  
Fig. 4. Percentage of hospitals offering top five DRG-related services (Appendix A).

## 6. Data and experiments

Data on various hospitals was obtained from the Hospital Association of Pennsylvania, Pennsylvania Health Department, and the Pennsylvania Medical Society. The data set consisted of information on 275 hospitals throughout Pennsylvania.

Information about the following was collected from each hospital:

1. Hospital name

2. Ownership

3. Total beds

4. Employees (full-time equivalents)

5. Emergency services visits

6. Top diagnostic-related group

7. Admissions

8. Outpatient visits

9. Average daily census

10. Other information (e.g., surgical combination, nursing home admissions and long-term care, special services).

Not all 275 hospitals contained complete information. From our analysis, we found that approximately 188 hospitals contained the complete data. A preliminary analysis was undertaken on the collected data. First, we plotted the percentage of hospitals that provide the top five diagnostic related group (DRG)- related services (Fig. 4). Note that many hospitals provide more than one DRG-related service; thus, the percentages do not add up to 100%. We further plotted the ratio of admissions per employee (Fig. 5) and the beds available per employee (Fig. 6).

The mean and standard deviation for the number of admissions per employee were 7.12 and 2.74, respectively. The mean and standard deviation for number of beds per employee were 0.29 and 0.14, respectively. The higher standard deviation of number of admissions per employee compared to the number of beds per employee shows that some hospitals have lower admissions per employee compared to other hospitals. The differences in hospitals in terms of number of beds per employee are relatively low.

Among the set of factors that lead to the demand of human resources are the admissions, physical capacity (beds in our case), special ambulatory services, type of hospital, and the top DRG-related service [35]. In other words, the employee requirement may be represented in the following functional form:

Admissions per employee  
![](/api/attachments/YNSUY9NE/fulltext/images/384680f4d12708f1b481d8c0728020c29c5bb20b1df8360a3523071e091d46c6.jpg)  
Fig. 5. The number of admissions per employee.

Beds per employee  
![](/api/attachments/YNSUY9NE/fulltext/images/557ae663ca04e36334b752837eb3e28991856f7481ac1901be9b393c4f27e822.jpg)  
Fig. 6. The number of beds per employee.

Number of Employees ¼

f ðadmissions; number of beds; number of emergency service visits; hospital ownership; top DRGÞ

where f(	) is a mapping that maps the independent variables to the dependent variable. Table 1 explains the variables used in the research model. The total number of employees is a monotonic function of admissions, number of beds, and number of emergency service visits. The hospital ownership and top DRG are binary variables that were operationalized as 0 and 1. The value of 1 was used for not-for-profit hospitals, the value of 0 was used for profit hospitals. In case of top DRG, when top DRG was 127 (about 80% of times), a value of 1 was used for input; when the top DRG was not 127, a value of 0 was used for input. Since there are only three independent variables that take continuous values, and the dependent variable is considered to have a monotonic relationship with these three independent variables, four variables are used to compute technical efficiency using DEA. These four variables provide a one output (number of employees) and three inputs (admissions, number of beds, and number of emergency visits) combination for computing efficiency using DEA.

Research model variables

<table><tr><td>Variable</td><td>Description</td></tr><tr><td>Number of employees</td><td>the number of full-time equivalent employees</td></tr><tr><td>Admissions</td><td>the number of patient visits and patients admitted</td></tr><tr><td>Number of beds</td><td>physical count of number of patient beds</td></tr><tr><td>Number of emergency visits</td><td>the number of ambulatory visits</td></tr><tr><td>Hospital ownership</td><td>not-for-profit or private hospital</td></tr><tr><td>Top DRG</td><td>top DRG (either heart failure and shock or other DRG)</td></tr></table>

In our ANN analysis, 175 hospitals were selected from 188 hospitals. Thirteen hospitals were discarded since the top DRG in these hospitals was different than the top DRGs listed in Fig. 4. All of the 175 selected hospitals contained one of the top five DRGs identified in Fig. 4 as the major DRG. We conducted two different experiments. Our first experiment consisted of randomly dividing the data into two sets. The first set, consisting of 100 hospitals, was used to train the neural network, while the second, comprising 75 hospitals, was used to test the performance of the trained neural network. In our second experiment, we took the first set of 100 hospitals and computed the relative efficiency of each hospital using DEA. The set of 100 hospitals was then divided into two sets of 50 hospitals. The first set of 50 hospitals was called the ‘‘efficient’’ set, and the other set of hospitals was called the ‘‘inefficient’’ set. The ‘‘efficient’’ set contained the 50 highest ranking hospitals based on their DEA efficiency score. Troutt et al. [44] suggest that training data for nonparametric models should be at least 10 times the number of input variables. Since we have five inputs, a minimum of 50 training examples was necessary to have reasonable learning of connection weights. Since we had only six efficient cases (efficiency of 100%), and a minimum of 50 hospitals for training were desirable, using a cut-off efficiency threshold value of 53%, we selected the top 50 hospitals (sorted in descending order of their relative efficiency) in our ‘‘efficient’’ set. The word efficient in the context of DEA means DMUs with efficiency of 100%. Since the ‘‘efficient’’ set in our cases does not contain all DMUs with 100% efficiency, we use quotes $( ^ { 6 6 } \ ' )$ to identify that the word ‘‘efficient’’ has a little different meaning than when used in the context of DEA. The same line of reasoning applies for the word inefficient (efficiency < 100%) when used in the context of DEA, and the word ‘‘inefficient’’ when used to represent the 50 hospitals that had the lowest efficiency rating. The performance of ‘‘efficient’’ and ‘‘inefficient’’ hospitals was then tested on the set of 75 hospitals in the test set. Among the design issues were the following.

(1) Normalization of dependent variable: Because we were using logistic activation function $f ( x ) = 1 /$ $( 1 + \mathsf { e } ^ { - x } )$ , it can be shown that Lim $f ( x ) = 1$ and Lim $f ( x ) = 0 ;$ <sup>x!þl</sup>  we normalized our dependent variable <sup>x!l</sup> of number of employees ( y) so that y<sup>a</sup>(0,1), where 0 stands for zero employees and 0.9 was the largest number of employees in the sample.

(2) Training sample size: Our initial decision on a training set sample size of 100 and a test set of 75 was determined on the heuristic of training set size <sub>z</sub> 10 times the number of independent variables. Because we had five independent variables, we selected the training set sample size of over 50.

Performance of four different structural design during the training phase  
Table 3

<table><tr><td>Number of hidden nodes</td><td>Input noise</td><td>Weight noise</td><td>RMS error</td><td>Prediction accuracy (%)</td></tr><tr><td>11</td><td>0</td><td>0</td><td>0.037</td><td>97</td></tr><tr><td>11</td><td>0.08</td><td>0.01</td><td>0.05</td><td>96</td></tr><tr><td>6</td><td>0</td><td>0</td><td>0.044</td><td>97</td></tr><tr><td>6</td><td>0.08</td><td>0.01</td><td>0.041</td><td>98</td></tr></table>

Performance of four different networks during the test phase

<table><tr><td>Number of hidden nodes</td><td>Input noise in trained net.</td><td>Weight noise in trained net.</td><td>RMS error</td><td>Prediction accuracy (%)</td></tr><tr><td>11</td><td>no</td><td>no</td><td>0.079</td><td>80</td></tr><tr><td>11</td><td>yes</td><td>yes</td><td>0.20</td><td>37.3</td></tr><tr><td>6</td><td>no</td><td>no</td><td>0.11</td><td>60</td></tr><tr><td>6</td><td>yes</td><td>yes</td><td>0.098</td><td>64</td></tr></table>

(3) Learning, generalizability, and overlearning issues: The network convergence criteria (stopping criteria) and learning rate determines how well and how quickly a network learns. A lower learning rate increases the time it takes for the network to converge, but it does find a better solution. The learning rate was set to 0.08. The convergence criteria was set as follows:

IF (AActual<sup>\_</sup>OutputPredicted<sup>\_</sup>Output $| \leq 0 . 1$ for all examples)

OR Training iterations <sub>z</sub> Maximum iterations THEN Convergence = Yes

ELSE

$$
\text { Convergence } = \text { No. }
$$

We selected the above-mentioned convergence criteria to account for the high variability of the dependent variable. A more strict convergence criterion was possible; however, an issue arose regarding overfitting the network on training data. Evidence in the literature shows that overfitting minimizes the sum of the square error in the training set at the expense of the performance on the test set [6]. We believed that the above-mentioned convergence criteria can make the network learning more generalizable. It is important to note that convergence (stopping) criteria should not be confused with the procedure used to learn the weights. A standard back-propagation algorithm was used to learn the weights. The backpropagation algorithm uses minimization of sum of square as the optimization criteria. The maximum number of iterations was set to 5000.

(4) Network structural issues: The network structure that we chose for our study was similar to the one shown in Fig. 1. Our networks had five input nodes and one output node. We had a three-layer (of nodes) network for modeling a nonlinear relationship between the independent variables and the dependent variable. The number of hidden nodes was twice the number of input nodes + 1, which is a more common heuristic for smaller sample sizes [6,33]. In the case of larger sample sizes, a higher number of hidden nodes are recommended [32]. For our research, we tried two different sets of hidden nodes, 11 and 6, respectively.

The Training Set Results  
![](/api/attachments/YNSUY9NE/fulltext/images/05ffa0205091029b14ea28ffd56f7d0456c06ce91428a046fb898fc386c4263f.jpg)  
Fig. 7. The performance comparison between the actual human resource requirements vs. the learned human resource requirement at convergence.

(5) Input and weight noise: One way to develop a robust neural network model is to add some noise in its input and weight nodes while the network is training. Adding a random input noise makes the ANN less sensitive to changes in input values. The weight noise shakes the network and sometimes causes it to jump out from a gradient direction that leads to a local minimum. In one of our experiments, we added input and weight noise during the network training phase.

The objective of our two experiments can be summarized as follows. In our first experiment, the objective was to identify the best ANN configuration and use this configuration in our second experiment. The objective of the second experiment was to use the proposed DEA-based training data selection to test if there are any performance differences when ‘‘efficient’’ vs. ‘‘inefficient’’ training data are used.

## 6.1. Results of experiment #1

Based on the design considerations, we conducted four different tests by varying the structural design and noise parameters in a two-layer network (of connections). Tables 2 and 3 illustrate the results of the different structural design for our four network training tests on 100 cases, and testing the trained network on 75 unseen cases, respectively. The first two tests represent the hidden number of nodes of 11 and 6 in a two-layer network. The numbers 11 and 6 were chosen to represent (2n + 1) and (n + 1) heuristic, where n is the number of input nodes. Tables 2 and 3 report two performance metrics, prediction accuracy and root mean square (RMS) error. Since our problem at hand is that of forecasting, prediction accuracy has a different meaning in our case. The prediction accuracy in our case implies the percentage of examples that satisfied the condition: AActual<sup>\_</sup>Output  Predicted<sup>\_</sup>OutputA V 0.1. The prediction accuracy of less than 100% in training indicates that the network training was stopped at 5000 iterations. When evaluating the goodness of fit of the ANN models, RMS provides better information than prediction accuracy. Although prediction accuracy numbers may make the reader believe that ANNs were overtrained, we do not believe this is true. The reason for our belief is as follows: let us consider the zero input and weight noise training and test results of 11 hidden nodes and 6 hidden nodes simultaneously. Focusing on RMS error only, we can see that RMS decreased for both training and test (for no input and weight

![](/api/attachments/YNSUY9NE/fulltext/images/fa838017c6338b3e25d2df9deee0df24dc3143a0addaf599d5a74fd30d31eb24.jpg)  
Fig. 8. The performance comparison between the actual human resource requirements and ANN-predicted human resource requirements.

Table 4  
The set of ‘‘efficient’’ hospitals (efficiency>53%)  
Table 5  
The set of ‘‘inefficient’’ hospitals (efficiency V 53%)

<table><tr><td>Hospital number</td><td>Relative efficiency (%)</td><td>Hospital number</td><td>Relative efficiency (%)</td></tr><tr><td>1</td><td>100</td><td>1</td><td>52.64</td></tr><tr><td>2</td><td>100</td><td>2</td><td>52.63</td></tr><tr><td>3</td><td>100</td><td>3</td><td>51.33</td></tr><tr><td>4</td><td>100</td><td>4</td><td>51.32</td></tr><tr><td>5</td><td>100</td><td>5</td><td>50.57</td></tr><tr><td>6</td><td>100</td><td>6</td><td>49.83</td></tr><tr><td>7</td><td>97.27</td><td>7</td><td>49.35</td></tr><tr><td>8</td><td>91.24</td><td>8</td><td>49.10</td></tr><tr><td>9</td><td>82.44</td><td>9</td><td>48.18</td></tr><tr><td>10</td><td>81.25</td><td>10</td><td>48.18</td></tr><tr><td>11</td><td>80.49</td><td>11</td><td>47.79</td></tr><tr><td>12</td><td>79.84</td><td>12</td><td>47.79</td></tr><tr><td>13</td><td>79.39</td><td>13</td><td>47.37</td></tr><tr><td>14</td><td>75.90</td><td>14</td><td>47.37</td></tr><tr><td>15</td><td>73.32</td><td>15</td><td>46.67</td></tr><tr><td>16</td><td>71.95</td><td>16</td><td>46.15</td></tr><tr><td>17</td><td>71.57</td><td>17</td><td>45.27</td></tr><tr><td>18</td><td>71.43</td><td>18</td><td>45.02</td></tr><tr><td>19</td><td>70.86</td><td>19</td><td>42.83</td></tr><tr><td>20</td><td>70.39</td><td>20</td><td>42.42</td></tr><tr><td>21</td><td>70.21</td><td>21</td><td>42.42</td></tr><tr><td>22</td><td>68.99</td><td>22</td><td>42.15</td></tr><tr><td>23</td><td>68.99</td><td>23</td><td>42.13</td></tr><tr><td>24</td><td>68.75</td><td>24</td><td>42.11</td></tr><tr><td>25</td><td>67.88</td><td>25</td><td>42.06</td></tr><tr><td>26</td><td>67.88</td><td>26</td><td>41.48</td></tr><tr><td>27</td><td>64.90</td><td>27</td><td>41.27</td></tr><tr><td>28</td><td>64.41</td><td>28</td><td>41.04</td></tr><tr><td>29</td><td>64.11</td><td>29</td><td>39.92</td></tr><tr><td>30</td><td>63.83</td><td>30</td><td>38.94</td></tr><tr><td>31</td><td>63.26</td><td>31</td><td>37.45</td></tr><tr><td>32</td><td>63.16</td><td>32</td><td>37.31</td></tr><tr><td>33</td><td>63.16</td><td>33</td><td>36.84</td></tr><tr><td>34</td><td>62.51</td><td>34</td><td>36.29</td></tr><tr><td>35</td><td>62.50</td><td>35</td><td>36.19</td></tr><tr><td>36</td><td>61.42</td><td>36</td><td>35.39</td></tr><tr><td>37</td><td>61.32</td><td>37</td><td>35.29</td></tr><tr><td>38</td><td>61.22</td><td>38</td><td>33.72</td></tr><tr><td>39</td><td>58.41</td><td>39</td><td>32.34</td></tr><tr><td>40</td><td>57.89</td><td>40</td><td>31.58</td></tr><tr><td>41</td><td>57.49</td><td>41</td><td>31.58</td></tr><tr><td>42</td><td>57.03</td><td>42</td><td>31.58</td></tr><tr><td>43</td><td>56.25</td><td>43</td><td>30.80</td></tr><tr><td>44</td><td>56.23</td><td>44</td><td>30.66</td></tr><tr><td>45</td><td>56.02</td><td>45</td><td>28.90</td></tr><tr><td>46</td><td>55.71</td><td>46</td><td>25.07</td></tr><tr><td>47</td><td>55.00</td><td>47</td><td>19.82</td></tr><tr><td>48</td><td>53.99</td><td>48</td><td>16.67</td></tr><tr><td>49</td><td>53.37</td><td>49</td><td>15.38</td></tr><tr><td>50</td><td>53.23</td><td>50</td><td>10.53</td></tr></table>

Table 6  
The Actual & Efficient and Inefficient Forecasts  
![](/api/attachments/YNSUY9NE/fulltext/images/a544b5b24ffd88a5434722136174d35007e4a60e1ae285126345c5f498e2b069.jpg)  
Fig. 9. The performance comparison between the actual human resource requirements and ‘‘efficient’’ and ‘‘inefficient’’ ANN-predicted human resource requirements.

<sup>a</sup> Significant at a = 0.01.

T-test for difference of means for predicting unseen cases through learning from ‘‘inefficient’’ and ‘‘efficient’’ cases

<table><tr><td>Mean difference</td><td>Correlation</td><td>t-value</td><td>df</td><td>2-tail significance</td></tr><tr><td>0.064</td><td>0.9976</td><td>-36.47</td><td>74</td><td> $0.000^a$ </td></tr></table>

noise case) when the number of hidden nodes was changed from 6 to 11. The lowering of RMS with the increase in number of hidden nodes gives an indication that even a larger network (hidden nodes greater than 11) would have lowered the training RMS further. Further, in a case of overtraining, an expectation is that RMS for training data would decrease, and RMS for test data will either not change or would increase. Clearly the results did not indicate this situation. Overtraining in ANN occurs when a very large size ANN is used [39]. A large size ANN would have a tendency to memorize input cases and lower training RMS significantly without lowering test RMS. Our results indicate that the number of hidden nodes (for no-noise case) not only decreased the training RMS, but also decreased the test RMS. Thus, we do not have any reason to believe that any significant overtraining problem was evident. The reader can view Figs. 7 and 8 to verify the lack of significant overfitting in both training and test data. When random input and weight noise are considered, an expectation is that smaller network will have lower RMS as it has lower degrees of freedom. For example, in a case of 11 hidden nodes, 5 input + 1 threshold nodes, and 1 output node, random weight noise is added to 77 weights. Whereas, in a case of six hidden nodes, random weight noise is added to 42 weights. Thus, large size ANNs are more vulnerable to random weight noise, and our results appear to confirm this hypothesis.

The performance statistics of the ‘‘efficient’’ and ‘‘inefficient’’ ANN tests

<table><tr><td>Hidden nodes</td><td>Type</td><td>Phase</td><td>RMS error</td><td>Accuracy (%)</td></tr><tr><td>11</td><td>inefficient</td><td>training</td><td>0.028</td><td>100</td></tr><tr><td>11</td><td>efficient</td><td>training</td><td>0.032</td><td>98</td></tr><tr><td>11</td><td>inefficient</td><td>test</td><td>0.11</td><td>54.7</td></tr><tr><td>11</td><td>efficient</td><td>test</td><td>0.08</td><td>85.3</td></tr></table>

![](/api/attachments/YNSUY9NE/fulltext/images/59afb02d3bab7c90294ddaf7501469f63de00021d5e1c3c67d9f0ea593c06da3.jpg)  
Fig. 10. A plot of the difference between a combined-‘‘efficient’’ ANN forecast and a combined-‘‘inefficient’’ ANN forecast.

We plot the training and test results of our best performing first experiment with 11 hidden layers and no random input and weight noise in Figs. 7 and 8, respectively. We use our best performing ANN in experiment #2.

## 6.2. Results of experiment #2

As described earlier in the paper, we divided the initial training set data into two sets of ‘‘efficient’’ and ‘‘inefficient’’ training data sets. The relative efficiency of the two sets is shown in Tables 4 and 5. A twolayer, 11-hidden-node network was first trained on ‘‘efficient’’ training set examples, and tested on the 75 test examples. A similar test was then conducted by training the ANN on ‘‘inefficient’’ training set examples, and then tested on the 75 test cases. Fig. 9 illustrates the forecasts generated for 75 test examples by training the two ANNs with ‘‘efficient’’ and ‘‘inefficient’’ cases.

Table 7 illustrates that ANN forecasting based on learning from ‘‘efficient’’ cases is higher than ANN forecasting based on learning from ‘‘inefficient’’ cases. A t-test on the difference of means between the ANN forecast values from learning from efficient and inefficient cases (Table 6) shows that the difference is significant, at 0.01 level of significance. The learning and predictive performance of the ‘‘efficient’’ and ‘‘inefficient’’ ANN tests is shown in Table 7.

The results in Table 7 indicate that training ANNs on efficient cases increases the predictive accuracy by 5.3% when compared to training an ANN containing both ‘‘efficient’’ and ‘‘inefficient’’ cases (as shown in experiment #1).

To determine if ‘‘inefficient’’ cases impair the predictive validity of the ANN, we plotted the differences in the forecast generated by the combined set (containing total of 100 examples) and the forecast generated by 50 ‘‘efficient’’ and 50 ‘‘inefficient’’ cases. Fig. 10 illustrates the results.

Based on the results plotted in Fig. 10, it can be seen that the difference between the combined forecast and the forecast generated by learning from ‘‘efficient’’ cases is lower (RMS error = 0.0245) than the difference between the combined forecast and the ‘‘inefficient’’ forecast (RMS error = 0.0667). This shows that for larger data sets, ANNs have a tendency to learn patterns from ‘‘efficient’’ cases. ‘‘Inefficient’’ cases in the training set lead to poor forecasting accuracy, hurt monotonicity assumption, and foster inconsistent learning.

## 7. Conclusions, limitations, and future work

We have described a DEA-based training data screening approach to learn monotonic nonlinear forecasting function. Using data from various hospitals throughout Pennsylvania and ANN for learning forecasting function, we have successfully tested our approach.

The DEA-based approach for data screening assumes nonnegative independent and dependent variables, and may not work when any one of the independent variables or the dependent variable is negative. The nonnegativity of inputs and output is imposed in all DEA models and can be a limitation. In our study, we assumed that the size of the training data is large enough to allow a decision-maker to use the DEA model and prescreen training data. If the original training data sample size is not large (10 times the number of inputs), then DEA-based screening may not be a viable option. In the case of a large data set, a user may need to use a cut-off efficiency threshold. All the cases that have an efficiency below the cut-off threshold can be omitted from the training data subset. The predictive performance of ANN may be sensitive to the choice of threshold.

Among the ANN model design and data preprocessing issues were technical efficiency of training data set, size, and random input and weight noise during the learning phase of our experiments. Our experiments showed that selecting a training data set based on technically efficient cases is beneficial for the ANN performance on unseen cases. Our experiments on adding input and weight noise during ANN training phase showed that noise helped networks with lesser nodes in the middle layer (6) predict well; however, for networks with a higher number of nodes in the middle layer (11), the addition of noise was detrimental for both its learning and predictive performance. Our conjecture is that a higher number of nodes in the middle layer help the neural network store more sensitive patterns in a larger set of training examples. The addition of noise in a network with a higher number of layers distorts the learning of the sensitive patterns and hinders the predictive performance. In smaller networks (i.e., having a few number of nodes in the hidden layer), a general pattern is learned, and the addition of noise reduces the overfitting of the network on the training set. Noise in smaller networks is more beneficial compared to noise in larger networks. Our conjectures on the impact of noise on the predictive ability of connectionist models are open for future tests.

In our experiments, we used a traditional backpropagation ANN algorithm without considering other algorithms. Several approaches have been tried in the literature that improve the performance of connectionist models over the traditional back-propagation. Recently, Piramuthu et al. [36] showed that feature construction can be used to improve learning and prediction of connectionist models. Several researchers [5,10,12,31] showed that second-order gradient search and other gradient-free methods improve the performance of the back-propagation model that uses the steepest-decent search method. We believe that the performance of current ANNs can be improved further by considering other learning algorithms.

The successful implementation of our ANN model shows the promise of ANNs in forecasting the number of employees in the health care industry; however, it must be noted that the proposed model represents a subset of variables that impact employee requirements. Improved forecasts can be obtained by acquiring information in areas such as staff turnover rates and organizational reward structuring for employees involved in the facilities. Future research needs to be conducted in identifying other factors that impact the number of employees.

We used random sampling for dividing our sample into training and testing sets. A stratified sampling approach may be better suited, as this approach will ensure the output values (number of employees) in both training and testing sets are similar. Further, the current approach may be benchmarked against other data screening approaches described in the literature review. Sampling and benchmarking our approach with other approaches were considered out of the scope of the current research. Future research may focus on addressing these issues.

In the course of our experiments, we examined evolutionary data mining techniques such as genetic algorithms and genetic programming. In our study, the use of genetic algorithms required that we prespecify the nonlinear relationships between our independent variables and the dependent variable. We concluded that this assumption was restrictive and, thus, removed the technique from further consideration. Genetic programming [22], however, did not require any prespecification of relationships between independent and dependent variables. The design of genetic programming model in studying employee requirement patterns required that we examine too many parameters (e.g., population size, mutation rate, initial tree size, crossover rate, function set, terminal set, etc.). With the lack of adequate knowledge regarding the exact impact these parameters had on our smaller sample, we did not consider this technique further. We do believe that both of these techniques may hold potential for learning about human resource requirement patterns. Future research may be focused on the performance comparisons of genetic programming and neural networks in learning and forecasting employees in the health care industry.

## Acknowledgements

The authors acknowledge financial support for this study from the Central Research Development Fund, Small Grants Program, University of Pittsburgh. We thank graduate student David Welliver for identifying relevant neural network literature and the anonymous reviewers for very valuable comments.

## Appendix A

<table><tr><td>DRG number</td><td>Explanation</td></tr><tr><td>127</td><td>heart failure and shock</td></tr><tr><td>89</td><td>simple pneumonia and pleurisy age&gt;17</td></tr><tr><td>88</td><td>chronic obstructive pulmonary disease</td></tr><tr><td>430</td><td>psychoses</td></tr><tr><td>462</td><td>rehabilitation</td></tr></table>

## References

[1] A.D. Athanassopoulos, S.P. Curram, A comparison of data envelopment analysis and artificial neural networks as tools for assessing the efficiency of decision making units, Journal of the Operational Research Society 47 (8) (1996) 1000 – 1016.

[2] R.D. Banker, A. Maindiratta, Nonparametric analysis and allocative efficiencies in production, Econometrica 56 (6) (1988) 1315– 1332.

[3] R.D. Banker, A. Charnes, W.W. Cooper, Some models for estimating technical and scale inefficiencies in DEA, Management Science 30 (9) (1984) 1078– 1092.

[4] A. Bansal, R.J. Kauffman, R.R. Weitz, Comparing the modeling performance of regression and neural networks as data quality varies: a business value approach, Journal of Management Information Systems 10 (1) (1993) 11 – 32.

[5] S. Becker, Y.L. Cun, Improving the convergence of back-propagation learning with second-order methods, Proceedings 1988 Connectionist Models Summer School, Morgan-Kaufman, San Mateo, CA, 1988, pp. 12– 17.

[6] S. Bhattacharyya, P.C. Pendharkar, Inductive, evolutionary and neural techniques for discrimination: a comparative study, Decision Sciences 29 (4) (1998) 900 – 971.

[7] M. Caudill, Using neural nets: representing knowledge, AI Expert, (1989) 34– 41.

[8] M. Caudill, Neural network training tips and techniques, AI Expert (1991) 56– 61.

[9] A. Charnes, W.W. Cooper, E. Rhodes, Measuring the efficiency of decision making units, European Journal of Operational Research 2 (1978).

[10] B. Curry, P. Morgan, Neural networks: a need for caution, Omega: An International Journal of Management Science 25 (1) (1997) 123 – 133.

[11] R.O. Duda, P.E. Hart, Pattern Classification and Scene Analysis, Wiley, New York, 1973.

[12] S.E. Falhman, Faster-learning variations of back-propagation: an empirical study, Proceedings 1988 Connectionist Models Summer School, Morgan-Kaufman, San Mateo, CA, 1988, pp. 38 – 51.

[13] J.A. Freeman, D.M. Skapura, Neural Networks: Algorithms, Applications and Programming Techniques, Addison-Wesley, MA, 1991.

[14] L. Fu, Knowledge based connectionism for revising domain theories, IEEE Transactions on Systems, Man and Cybernetics 23 (1) (1993) 173–182.

[15] L. Fu, Rule generation from neural networks, IEEE Transactions on Systems, Man and Cybernetics 24 (8) (1994) 1114–1124.

[16] G.D. Garson, Interpreting neural network connection weights, AI Expert (1991) 47– 51.

[17] B.A. Jain, B.N. Nag, Artificial neural network models for pricing initial public offerings, Decision Sciences 26 (3) (1995) 283–302.

[18] E.S. Jun, J.K. Lee, Quasi-optimal case-selective neural network model for software effort estimation, Expert Systems with Applications 21 (1) (2001) 1 – 14.

[19] Y. Kannai, A characterization of monotone individual demand functions, Journal of Mathematical Economics 18 (1989) 87 – 94.

[20] C. Kanzow, H. Jiang, A continuation method for (strongly) monotone variational inequalities, Mathematical Programming 81 (1) (1998) 103– 125.

[21] R.H. Keeney, H. Raiffa, Decisions with Multiple Objectives: Preferences and Value Tradeoffs, Wiley, New York, 1976.

[22] J.R. Koza, Genetic Programming: On the Programming of Computers by Means of Natural Selection, MIT Press, Cambridge, MA, 1992.

[23] J. Lawrence, Data preparation for a neural network, AI Expert (1991) 34 – 41.

[24] C.T. Leung, T.W.S. Chow, Least third-order cumulant method with adaptive regularization parameter selection for neural networks, Artificial Intelligence 127 (2001) 169 – 197.

[25] M.Z.F. Li, Pricing non-storable perishable goods by using a purchase restriction with an application to airline fare pricing, European Journal of Operational Research 134 (3) (2001) 631– 647.

[26] L.R. Medsker, Hybrid intelligent systems, International Journal of Computational Intelligence and Organizations 1 (1) (1996) 10– 20.

[27] L.R. Medsker, E. Turban, Integrating expert systems and neu-

ral computing for decision support, Expert Systems with Applications 7 (4) (1994) 553– 562.

[28] W.A. Minneman, Strategic justification for an HRIS that adds value, HR Magazine 35 (1996).

[29] D. Murray, Tuning neural networks with genetic algorithms, AI Expert (1994) 27 – 31.

[30] A. Nigrin, Neural Networks for Pattern Recognition, MIT Press, Cambridge, MA, 1993.

[31] D.B. Parker, Optimal algorithms for adaptive networks: second order back-propagation, second order direct propagation, and second order Hebbian learning, Proceedings IEEE Internation al Conference on Neural Networks, IEEE Press, San Diego, CA, 1987, pp. 593– 600.

[32] E. Patuwo, M.Y. Hu, M.S. Hung, Two-group classification using neural networks, Decision Sciences 24 (4) (1993) 825– 845.

[33] P.C. Pendharkar, An empirical study of design and testing of hybrid evolutionary – neural approach for classification, Omega: An International Journal of Management Science 29 (4) (2001) 361 – 374.

[34] P.C. Pendharkar, A computational study on the performance of neural network design under changing structural and kurtotic environments, European Journal of Operational Research 138 (1) (2002) 155 – 177.

[35] P.C. Pendharkar, J.A. Rodger, Distributed problem solving is framework for effective service pricing, resource allocation and quality performance in health care industry, 3rd Proceedings of INFORMS Conference on Information Systems and Technology, Montreal Canada. April 22– 29, 1998, pp. 437– 441.

[36] S. Piramuthu, H. Ragavan, M. Shaw, Using feature construction to improve the performance of neural networks, Management Science 44 (3) (1998) 416–430.

[37] J.K.H. Quah, The monotonicity of individual and market demand, Econometrica 68 (4) (2000) 911– 930.

[38] D.E. Rumelhart, G.E. Hinton, R.J. Williams, Learning internal representations by error propagation, in: D.E. Rumelhart, J.L. McClelland (Eds.), Parallel Distributed Processing: Exploration in the Microstructure of Cognition, vol. 1: Foundations, MIT Press, Cambridge, MA, 1986, pp. 23 – 32.

[39] R.J. Schalkoff, Artificial Neural Networks, McGraw Hill, New York, 1997.

[40] J.W. Shavlik, R.J. Mooney, G.G. Towell, Symbolic and neural learning algorithms: an experimental comparison, Machine Learning 6 (1991) 111 – 143.

[41] M.L. Steib, S.T. Weidman, Expert systems for guiding back-

propagaton training of layered perceptrons, Expert Systems with Applications 2 (1991) 73–81.

[42] R. Stein, Selecting data for neural networks, AI Expert (1993) 42– 47.

[43] R. Stein, Preprocessing data for neural networks, AI Expert (1993) 32–37.

[44] M.D. Troutt, A. Rai, A. Zhang, The potential use of DEA for credit applicant acceptance systems, Computers and Operations Research 4 (1995) 405 – 408.

[45] M.R. Versaggi, Understanding conflicting data, AI Expert (1995) 21 – 25.

[46] J.P. Vila, Bayesian nonlinear model selection and neural networks: a conjugate prior approach, IEEE Transactions on Neural Networks 11 (2) (2000) 265 – 278.

[47] S. Wang, The unpredictability of standard back propagation neural networks in classification applications, Management Science 41 (3) (1995) 555– 559.

[48] S. Wang, An insight into the standard back-propagation neural network model for regression analysis, Omega: An International Journal of Management Science 26 (1) (1998) 133 – 140.

[49] S. Wang, An adaptive approach to market development forecasting, Neural Computing and Applications 8 (1999) 3 – 8.

[50] W.A. Wright, Bayesian approach to neural-network modeling with input uncertainty, IEEE Transactions on Neural Networks 10 (6) (1999) 1261– 1270.

Dr. Pendharkar is an assistant professor of Information Systems at Pennsylvania State University at Harrisburg. Dr. Pendharkar’s work has appeared, or was accepted, for publication in Annals of Operations Research, Communications of ACM, Decision Sciences, Computers and Operations Research, Interfaces, European Journal of Operational Research, Expert Systems with Applications, Intelligent Systems in Accounting, Finance and Management, Omega, as well as several other journals. Dr. Pendharkar has consulted with several airline, container shipping, mining, health care, and governmental agencies on yield management, information systems, and scheduling issues.

Dr. Rodger is an associate professor at Indiana University of Pennsylvania. Dr. Rodger’s work has appeared in Annals of Operations Research, Communications of the ACM, Expert Systems with Applications, and several other journals and proceedings of international, national, and regional conferences. Dr. Rodger has consulted with the US Department of Defense and several health care companies.

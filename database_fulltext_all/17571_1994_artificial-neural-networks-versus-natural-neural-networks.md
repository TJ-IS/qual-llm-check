---
otero_id: 17571
otero_key: "P4KWTYFD"
title: "Artificial neural networks versus natural neural networks"
authors: "Jun Wang"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90016-7"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Artificial neural networks versus natural neural networks

A connectionist paradigm for preference assessment

Jun Wang

University of North Dakota, Grand Forks, ND 58202-7118, USA

Preference is an essential ingredient in all decision processes. This paper presents a new connectionist paradigm for preference assessment in a general multicriteria decision setting. A general structure of an artificial neural network for representing two specified prototypes of preference structures is discussed. An interactive preference assessment procedure and an autonomous learning algorithm based on a novel scheme of supervised learning are proposed. Operating characteristics of the proposed paradigm are also illustrated through detailed results of numerical simulations.

Keywords: Neural networks; Supervised learning; Preference assessment

![](/api/attachments/P4KWTYFD/fulltext/images/0ad33232cb10780907822e4810d078efa693954a1ab06a18da9631c667c35a5f.jpg)

Jun Wang is an Associate Professor of Industrial Technology at the University of North Dakota. He received a B.S. degree in electrical engineering and an M.S. degree in systems engineering from Dalian University of Technology (formerly Dalian Institute of Technology), Dalian, China. He received his Ph.D. degree in systems engineering from Case Western Reserve University, Cleveland, Ohio. Before joining the faculty of the University of North Dakota, he was on the faculty of Electrical Engineering at Dalian University of Technology, a research and teaching assistant in the Department of Systems Engineering and Center for Automation and Intelligent Systems Research at Case Western Reserve University. His current research interests are in theory and methodology of artificial neural networks, and their applications to decision systems, control systems, and manufacturing systems. Dr. Wang is a member of IEEE, INNS, IIE, DSI, ITEA, and ORSA.

Correspondence to: Jun Wang, Department of Industrial Technology, University of North Dakota, Grand Forks, ND 58202-7118, USA.

## 1. Introduction

Preference plays a key role in multiple criteria decision making (MCDM). In analyzing a multi-criteria decision problem and developing a multi-attribute decision model, it is often necessary to assess the decision maker's (DM's) underlying preference explicitly represented by a preference model such as a multiattribute utility function. From a descriptive point of view, a preference model can be used to describe a DM's preferential behavior and predict the choice of the DM. From a prescriptive point of view, a preference model can be used to apply a decision rule and aid a DM in determining the most preferred choice from a given set of alternatives.

During the past three decades, great efforts were made by decision theorists and practitioners in developing theory and methodology for preference assessment. In the literature, the major approaches are multiattribute utility theory (MAUT) and analytic hierarchy process (AHP). The common feature of preference assessment techniques based on MAUT is decomposition of multiattribute utility function into a simple functional form such as additive or multiplicative representations by assuming or verifying some independence conditions, assessing marginal utility functions, estimating scaling constants, and aggregating into a multiattribute utility function. For example, if a DM's preference is mutually value independent among attributes, then the DM's preference structure can be represented by an additive utility function. If a DM's preference is utility independent for each attribute, then the DM's preference structure can be represented by a quasi-additive (multilinear) utility function. If a DM's preference is mutually utility independent, then the DM's preference structure can be represented by an additive-multiplicative utility func tion. For details of decomposable utility functions and their independence conditions, see, e.g. [2,5,6,7,8,13,14]. In contrast to the MAUT that is a normative theory, the AHP originally developed in [16] is a descriptive methodology. The AHP begins with inquiring a DM's judgment concerning the relative importance of each criterion and a preference for each alternative on each criterion. The outcome of the AHP is a prioritized overall performance for each decision alternative.

There are many reasons to develop new paradigms of preference models and assessment procedures. Admittedly, preference assessment based the existing assessment techniques is challenging in practice. The dominant decomposition approach to preference assessment in the MAUT theoretically requires that the DM's preference structure satisfy one of a few established independence conditions. This requirement places restriction on the DM's preference structures since the DM's preference may not be decomposable or ascertainment of attribute independency may be extremely difficult in a complex decision situation. Another limitation of the existing approaches in the MAUT is a priori specification of decomposable functional forms of multiattribute utility functions, in which attribute independence needs to be verified. As an intelligent being, a human decision maker's preference behavior is generally more complicated than utility theory posited [10]. For example, it has been observed and documented in descriptive empirical studies that preferences of DMs' are inconsistent with MAUT. Some studies have also reported difficulties in using the traditional models in decision support system [12]. As a relatively new and promising approach, the AHP has not received universal acceptance [e.g., 4]. The discrepancy and interaction among descriptive, normative and prescriptive theories also suggest that new paradigms would be necessary to serve descriptive, normative, and prescriptive analysis [1].

Recent advances in artificial neural networks (ANNs) have laid a solid basis for developing new methodology for preference assessment. Advocated by connectionist researchers from a variety of disciplines, artificial neural networks are gaining more and more popularity in recent years. Artificial neural network models have manifested significant application potential in numerous areas including pattern recognition, associative memory, combinatorial optimization, robotics and process control. As adaptive representations for complex problem solving, feedforward neural networks have been investigated extensively. Such artificial neural networks, exemplified by the popular multilayer perceptrons with an error backward propagation learning algorithm $[16]$ , are capable of learning from examples by parameter adaptation. When trained based on a set of paired input-output training samples, a feedforward neural network adjusts its internal parameters to accommodate the training samples and to represent the underlying mapping. After a number of epochs, provided that the training instances are well representative, the network could then “discover” the input-output mapping mechanism even though the mapping is implicit to the human user (trainer) initially. It has been proven that multilayer feedforward neural networks are capable of approximating any function $[9,11]$ . It has also been found that the mapping mechanisms thus learned are often very robust, and represent generalizations of examples available in the learning process [e.g., 25]. Feedforward neural networks have been proposed for many areas of application such as dynamic systems identification $[15]$ , dynamic system prediction $[25]$ , and algebraic system modeling $[20,21]$ .

Some studies indicate that the preferential behavior of a decision maker is governed by his/her intrinsic natural neural network [e.g., 18,26]. This argument provides the plausibility for the studies of developing connectionist representations that resemble the input-output behaviors of the DMs' underlying preference in his/her natural neural networks. Wang and Malakooti [22] have demonstrated that a feedforward neural network can be applied to multiple criteria decision making under certainty. The underlying idea of the connectionist approach is to emulate decision makers' natural neural networks using artificial neural networks. In other words, the motivation is to model preference structures via supervised learning. Compared with the traditional approaches in terms of preference representation and assessment procedure, connectionist paradigms have several salient features.

(1) Connectionist representation vs. decomposable representations: The commonly used preference models are based on some decomposition rules whereas the connectionist preference models are ANN-based. This feature relaxes the independence assumptions on the functional form of the preference models and broadens the applicability.

(2) Robust representation vs. parameter-sensitive representations. The traditional preference models are usually sensitive to parameter perturbation whereas the connectionist preference models are fault-tolerant as many analyses and experiments show. This feature provides the preference models with a certain degree of immunity to erroneous and noisy input training data.

(3) Adaptive procedure vs. constructive procedures: The majority of the traditional assessment procedures are constructive in which structures and parameters of models are derived once. The connectionist learning procedure is adaptive where the assessment process is evolutionary. This feature facilitates refining the representation by incorporating updated information in a timely fashion. Once driftage of the DM's preference is detected, "calibration" of the preference models based on new preferential information and obtained ANN configuration should take much less effort than restarting any whole assessment procedure.

(4) Self-organizing procedures vs. ad hoc procedures: most of the existing assessment procedures require that a functional form be specified a priori whereas the connectionist learning procedure constructs the preference models from available data autonomously according to a set of rules. This feature reduces the cognitive burden on the DM's part by using simpler form of preferential information, and reduces the analytical work on the analyst's part by processing data on computers.

The purpose of this paper is twofold. The first one is to present a connectionist framework for preference assessment in a general multicriteria decision setting. The second one is to present a specific interactive procedure for assessing two specified preference models based on a new supervised learning strategy. Rather than focusing on the philosophical implications of connectionist approach to preference assessment or empirical studies to compare connectionist approach with classical approaches, we propose an autonomous learning algorithm that is able to automate neural network training and testing procedures.

This paper consists of six sections. Section 2 introduces constructive specifications of two preference models. Section 3 addresses configuration of artificial neural networks for preference representation. Section 4 proposes an interactive preference assessment procedure and an autonomous learning algorithm based on a new supervised learning strategy. Section 5 discusses results of numerical simulations. Finally, Section 6 concludes this paper.

## 2. Model formulation

## 2.1. Problem statement

We consider a general MCDM problem as follows.

$$
D R \colon c = F (d, s),\tag{1}
$$

where DR stands for decision rule, $c \in C \subseteq R^{p}$ is a p-dimensional vector of criteria (attribute) of the decision maker's (DM's) concerns to be maximized, C is a set of possible consequences; $d \in D \subseteq R^{q}$ is a q-dimensional decision alternative, D is a set of available decision alternatives; $s \in S \subseteq R^{r}$ is an r-dimensional state variable, S is a set of risky states of environment. In normative analysis, the MCDM problem can be interpreted as deriving a decision rule (DR) according to the DM's preference, and applying the DR to determine the most desirable decision alternative $d^{*}$ in D [3].

The fundamental assumptions of this connectionist approach are that (i) the DM's preference structure can be represented by a real-valued function of attributes; and (ii) the DM is able to articulate his/her preference among sure or risky prospects with an adequate discriminatory power.

## 2.2. Constructive specifications

A preference model is an abstract representation that pertains to a DM's individual value judgments for outcomes and reflects the DM's implicit tradeoffs among the attributes. Preference models can be formulated in different ways depending on the type of available preferential data and level of abstraction.

The most popular preference model is the multiattribute utility function. A multiattribute utility fraction (MAUF) is a map from the attribute space to a utility space; that is, $PM_{1}: C \to Z \subset R$ such that $\forall c', c'' \in C$ , $z' = PM_{1}(c')$ , $z'' = PM_{1}(c'')$ ,

$$
z ^ {\prime} \left\{ \begin{array}{l l} > z ^ {\prime \prime} & \text { iff } c ^ {\prime} \succ c ^ {\prime \prime}, \\ = z ^ {\prime \prime} & \text { iff } c ^ {\prime} \sim c ^ {\prime \prime}, \\ <   z ^ {\prime \prime} & \text { iff } c ^ {\prime} \prec c ^ {\prime \prime}, \end{array} \right.\tag{2}
$$

where $\succ, \prec$ , and $\sim$ denote is preferred to, is less preferred to, and is indifferent to respectively. A DR for $PM_{1}(c)$ is the case of decision under certainty is max $PM_{1}(c)$ subject to $d \in D$ ; i.e., select $d^{*} \in D$ such that $\forall d \in D$ , $PM_{1}(F(d^{*})) \geq PM_{1}(F(d))$ . DRs for $PM_{1}(c)$ in the cases of decision under risk could be max $\int_{s \in S} PM_{1}(F(d, s)) p(s) ds$ subject to $d \in D$ if S is continuous, and max $\sum_{s \in S} PM_{1}(F(d, s)) P(s)$ subject to $d \in D$ if S is discrete; i.e., select $d^{*} \in D$ , $\forall d \in D$ , $\int_{s \in S} PM_{1}(F(d^{*}, s)) p(s) ds \geq \int_{s \in S} PM_{1}(F(d, s)) p(s) ds$ , or $\sum_{s \in S} PM_{1}(F(d^{*}, s)) P(s) \geq \sum_{s \in S} PM_{1}(F(d, s)) P(s)$ , whichever is appropriate.

Since $\succ, \prec$ , and $\sim$ constitute a partition on $C \times C$ , it is natural to specify another type of preference model over the Cartesian product of attribute spaces; i.e., $PM_{2}$ : $C \times C \to Z \subset \mathbb{R}$ . More specifically, the input is $(c_{1}', \ldots, c_{p}', c_{1}'', \ldots, c_{p}'')$ , a 2p-dimensional vector; the outputs $PM_{2}$ can be specified as follows. $\forall c \in C$ , $z = PM_{2}(c', c'')$ ,

$$
z \left\{ \begin{array}{l l} > 0. 5, & \text { iff } c ^ {\prime} \succ c ^ {\prime}; \\ = 0. 5, & \text { iff } c ^ {\prime} \sim c ^ {\prime \prime}; \\ <   0. 5, & \text { iff } c ^ {\prime} \prec c ^ {\prime \prime}. \end{array} \right.\tag{3}
$$

$PM_{2}$ is virtually a transformation of the multiattribute utility function $PM_{1}$ ; i.e., $PM_{2}(c', c'') = S(PM_{1}(c') - PM_{1}(c''))$ where $0.5 < S(x) \leq 1$ if $x > 0$ , $S(x) = 0.5$ if $x = 0$ , and $0 \leq S(x) < 0.5$ if $x < 0$ . The sigmoid function $S(x) = (1 + e^{-x})^{-1}$ , a differentiable approximation of the step function, is well suited for this purpose. By definition, the $PM_{2}$ has the following properties. $\forall c', c'' \in C$ ,

$$
P M _ {2} (c ^ {\prime}, c ^ {\prime \prime}) = 1 - P M _ {2} (c ^ {\prime \prime}, c ^ {\prime}),\tag{4}
$$

$$
P M _ {c} (c ^ {\prime}, c ^ {\prime}) = P M _ {2} (c ^ {\prime \prime}, c ^ {\prime \prime}) = 0. 5.\tag{5}
$$

A DR for $PM_{2}$ in the case of decision under certainty could be selecting $d^{*} \in D$ such that $\forall d \in D$ , $PM_{2}(F(d^{*}), F(d)) \geq 0.5$ . DRs for $PM_{2}$ in the cases of decision under risk could be selecting $d^{*} \in D$ , $\forall d \in D$ , $\int_{s \in S} PM_{2}(F(d^{*}, s))$ .

$F(d, s))p(s)ds \geq 0.5$ if $S$ is continuous, $\Sigma_{s \in S} PM_2(F(d^*, s), F(d, s))P(s) \geq 0.5$ if $S$ is discrete.

Selection of a preference model depends on the nature of decision problem and the type of preference information that the DM provides. For example, if a DM is willing to provide holistic ratings over a set of alternatives, then model $PM_{1}$ is more suitable. If, instead, a DM could articulate only his/her preference via pairwise comparison or in form of strength of preference, then model $PM_{2}$ is more appropriate.

## 3. Model configuration

## 3.1. A feedforward neural network architecture

The primary interest of this study is to investigate the ANN-based preference models that represent the essence of DM's underlying preference. In other words, the aim is to synthesize ANNs according to the constructive specifications of the preference models defined in the preceding section. Toward this end, let's consider an artificial neural network as a mechanism of many-to-one mapping from the attribute set or the Cartesian product of attribute spaces to a utility space, viz., ANN: $X \times W \rightarrow Y \subseteq R$ where X,Y, and W are the set of input, outputs, and adaptable parameters of an artificial neural network respectively; X = C or $X = C \times C$ for $PM_{1}$ and $PM_{2}$ respectively. Since artificial neural networks possess universal approximating capabilities for any real-valued function and robust generalizing capabilities from limited number of samples, they are capable of representing very general forms of preference structures.

Wang and Malakooti [21] propose a feedforward ANN architecture with a general topological structure. Since there is only one output variable, this type of topological structure allows unidirectional connections from every input to every neuron and between every neuron as shown in Figure 1. That is, unidirectional connections exist from every input to every neuron including the output neuron and from every neuron to every precedent neuron in a feedforward fashion. This type of topological structure allows maximal number of unidirectional connections, hence is possesses the highest degree of plasticity in representing input-output relations. The proposed general architecture contains the popular multilayer architecture as a special case in topology, where some of connection weights in multilayer perceptron are always zero. Since the multilayer networks are capable of approximating any real-valued function and the multilayer architecture is the special case of the proposed general architecture, an ANN with the proposed topological structure is also capable of representing approximately any real-valued function. In contrast to the multilayer architecture for which the numbers of layers and neurons in each hidden layer have to be specified, only the number of total neurons needs to be specified. An in-depth theoretical analysis of the neural network architecture can be found in [21] where a necessary and sufficient condition for such a neural network to be able to reduce training error to zero with arbitrary initial parameter configuration is derived.

They state representation of the ANN can be described as follows.

$$
v _ {i} (t) = f _ {i} \bigl (u _ {i} (t) \bigr), \quad i = 1, 2, \dots , N,\tag{6}
$$

$$
\begin{array}{l} u _ {i} (t + \Delta t) = \sum_ {j = i + 1} ^ {N} w _ {i j} ^ {(1)} (t) v _ {j} (t) + \sum_ {j = 1} ^ {n} w _ {i j} ^ {(2)} (t) x _ {j} \\ \quad + w _ {i} ^ {(3)} (t), \quad i = 1, 2, \dots , N, \end{array}\tag{7}
$$

where $y(t)=v_{1}(t)$ is the output variable, $v_{i}(t)$ is the instantaneous activation state corresponding to the i-th neuron of the ANN, $u_{i}(t)$ is an instrumental variable standing for instantaneous net input to neuron i, $f_{i}(\cdot)$ is an activation function for the i-th neuron and is usually the sigmoid function $f_{i}(u_{i})=(1+e^{-\lambda_{i}u_{i}})^{-1}$ for $i=1,2,\ldots,N$ ; N is the total number of neurons; n is the number of input components; $w_{ij}^{(1)}, w_{ij}^{(2)}$ , and $w_{i}^{(3)}$ denote the weight from neuron j to neuron i, from input j to neuron i, and threshold parameter of neuron i, respectively.

![](/api/attachments/P4KWTYFD/fulltext/images/afc691b9756deafcc7b8a6cebd9bd9e5874950bea5102543eff770ff171929a9.jpg)  
Fig. 1. Basic topological structure of the feedforward ANN architecture.

![](/api/attachments/P4KWTYFD/fulltext/images/bcc03f4d5ee66a2e85c66e8aab47114684e3d5e25bd85e76ff00d6443599bd06.jpg)  
Fig. 2. An example of the feedforward ANN architecture.

The adaptable parameters of the artificial neural network consist of the synaptic weights on connections and biasing thresholds of neurons. The weights of connections reflect the degree of interaction between neurons and influence of inputs to neurons. Thresholds reflect the biasing effects of neurons. The parameter representation of the ANN discussed above can be described in a matrix form; i.e., $W = [W_{1}|W_{2}|W_{3}]$ where $W_{1} = [w^{(1)}]$ , a matrix of N by N, $W_{2} = [w^{(2)}]$ , a matrix of N by n, and $W_{3} = [w^{(3)}]$ , an N-dimensional column vector respectively. Since the proposed artificial neural network is a fully connected feedforward model, $W_{1}$ is an upper triangular matrix. For example, let

$$
W = \left| \begin{array}{c c c c c c c} 0 & 2. 1 & - 1. 4 & 5. 2 & 0. 4 & - 1. 4 & 0. 3 \\ 0 & 0 & - 0. 3 & 2. 4 & - 0. 2 & 0. 4 & - 1. 5 \\ 0 & 0 & 0 & 1. 2 & 0. 3 & - 0. 7 & 2. 4 \\ 0 & 0 & 0 & 0 & 0. 8 & 1. 5 & 1. 3 \end{array} \right|
$$

The corresponding feedforward neural network is shown in Figure 2.

In general, for such an ANN with N neurons, the number of adaptable parameters is $N(N-1)/2 + N(n+1) = N(N+2n+1)/2$ . The detailed procedure to derive the parameter matrix is defined by a learning algorithm and will be elaborated in next section.

## 3.2. A dynamical configuration rule and an evolutionary adaptation rule

In order to train an artificial neural network, two design parameters must be determined: the size of the neural network architecture and the size of the training set. The size of an architecture is represented by the number of neuron and the size of a training set is represented by the number of training samples. Therefore, the rephrased question is what are the necessary and sufficient numbers of neurons and training samples for an adequate ANN representation. There is no established procedure to determine the necessary and sufficient numbers of training samples and neurons in the literature. The common practice is trial and error in nature. Given a problem, the number of samples needed for construction an accurate input-output mapping mechanism depends on the complexity of the problem under study and the number of neurons is related to the number of training samples. On one hand, an ANN that was trained based on a smaller number of training samples than that actually required could generalize poorly when new samples are used, whereas an ANN that has a smaller number of neurons could result in intolerable training error and yield an inadequate representation of the training data. On the other hand, an ANN that has more neurons or that was trained based on redundant samples could result in unnecessary and formidable computation, since training processes of neural networks are admittedly time-consuming.

Many research findings indicate that the natural neural networks are dynamically configurable and seek equilibrium and harmony in the dynamical configuration process. This evidence inspired us in developing a biologically plausible ANN architecture that grows as a supervised learning process proceeds. The underlying idea of the dynamical configuration is to expand the neural network architecture in size whenever the training process is hindered by a local minimum of the error function in the parameter space. This principle for the architectural expansion is referred to as the dynamical configuration rule.

A dynamical configuration rule $[23]$ is stated as follows: Starting from the basic topological structure of small size, the feedforward neural network adjusts its parameters according to an adaptation rule based on a given training set. As indicated earlier, the proposed neural network architecture requires only a specification of the total number of hidden neurons. If a learning process gets stuck in a local minimum of error function in the parameter space, then the architecture is expanded in size by adding one more hidden neuron with randomized initial parameters (connection weights and biasing threshold) following the pattern of connectivity specified by the basic topological structure. In other words, if the training error is larger than a specified tolerance and the decreasing rate of the training error is lower than another specified tolerance, then the number of neurons increases by one with random initial threshold and weights connected unidirectionally from all inputs to the newly introduced neuron and from the new neuron to all other neurons.

The number of training samples required is also another important design parameter. Given the training accuracy, it is usually difficult, if not impossible, to determine a priori the minimum number of training samples that are sufficient to generalize the implicit mapping. In practice, large training sets are usually specified in a conservative way. In general, the more the information included in supervised learning, the more accurate the resultant representation. The problem is the increased computational complexity, since the supervised learning is computationally intensive. For given accuracy requirement, a larger number of training samples than actually needed will unnecessarily increase computational complexity. Furthermore, on the DM's part, more training samples mean more devoted time and effort, and heavier cognitive burden. Since the input-output mapping represented by a neural network is generalized based on a limited number of training samples, a smaller number of training samples than actually required will yield an inaccurate approximation. Therefore, there is a tradeoff between the computational complexity and representational accuracy.

Since a human being's knowledge accumulates piece by piece, an evolutionary adaptation rule in which the training set expands dynamically can be advantageous. Specifically the evolutionary adaptation rule can be stated as follows. A learning process begins with a minimum training set in which there are minimum number of paired input-output training samples. The training set expands by including one new paired input-output training sample when the training error reaches a predetermined tolerance level but the testing error is above another tolerance level. Since the training set initially contains a single training sample, a neural network can reach a global minimum quickly, but generalizes poorly. As the training set augments, the training process terminates once the tolerance levels for both training and testing errors are reached. Because the training set grows only when necessary, its size can be kept small if not minimal.

## 4. Assessment procedure

## 4.1. An interactive assessment procedure

In lights of above discussion, an interactive assessment procedure based on a new supervised learning scheme is delineated as follows. The interactive preference assessment procedure begins with determining a set of representative alternatives as the basis of the inductive inference. A particular type of preference information (e.g., holistic ratings or paired comparisons) on the selected alternatives is the elicited by presenting the outcomes of these alternatives in a format (e.g., certainty equivalent or probability equivalent methods) to the DM for evaluations. For prescriptive and normative analyses, the results of the DM's evaluation then have to be checked according to rationality axioms such as Pareto optimality to eliminate inconsistency and incoherence. Based on some properties of specific preference models, additional data may be reproduced from the preference information. The selected alternatives along with their associated preference relations constitute a preferential information database. The data in the database are divided into two sets, $S_{trn}$ and $S_{tst}$ , for their subsequent usage.

Selection of the training and testing instances is important for the inductive inference. The general requirements for the training and testing instances are that they should be (i) consistent, (ii) presentable, and (iii) informative. The consistency means that the training instances should be consistent with the behavior of the DM's underlying preference, i.e., $S_{trn}$ and $S_{tst}$ should contain the pairs with the highest probability of association. The presentability means that these training instances should satisfy the constraints on C enforced by the decision situation. The informativeness implies that the input components of training instances should distribute uniformly or as uniformly as possible on the domain of interests, and the output components should cover completely or as completely as possible over the spectrum of the output value. The informativeness also implies nonredundancy; i.e., without loss of information the training set should be minimal.

The instances in the training set are then used to train an artificial neural network. Based on a prespecified performance evaluation rule, the artificial neural network adjusts its parameters according to the evolutionary adaptation rule and configures its architecture according to the dynamical configuration rule to learn the DM's preference behavior represented by the training instances. Figure 3 illustrates the dynamic process of the supervised learning in neural networks.

![](/api/attachments/P4KWTYFD/fulltext/images/a9cdd820d4e913b5b093a268d59214f171c9c4644dc3aafc481267b63db30db6.jpg)  
Fig. 3. A block diagram of supervised learning.

Once a prespecified tolerance level for training error is reached, a test is performed based on the data in the testing set. If the testing result is not satisfactory (i.e., the testing error is larger than a predetermined tolerance), then interact with the DM to obtain another paired input-output training sample, check it in terms of consistency and coherence, add it to the training set, and continue to train the neural network based on the updated training set and obtained parameters until both the training and testing errors are reduced to or below their tolerance levels.

Following the interactive preference assessment procedure, an artificial network interacts with and learns from its natural counterpart to elicit and represent a DM's preference. Once the preference model is assessed and validated, it can be used to predict the DM's choice or assist the DM in evaluating or ranking given sure or risky prospects.

In the common practice of supervised learning, training and testing are performed separately. The separation of training and testing may entail re-training if the result of testing is unsatisfactory and the re-training is more time-consuming. The proposed new supervised learning scheme allows on-line testing by incorporating testing phase into training phase and allows the numbers of training samples and neurons grow alternately to automate the neural network synthesis procedure.

![](/api/attachments/P4KWTYFD/fulltext/images/87eed8efc77a74cab6a68c680c782b70871be3883348fc8aa71d2fb7fa74ebd7.jpg)  
Fig. 4. A flowchart of the autonomous learning algorithm.

In contrast to existing interactive methods that search for solutions in decision spaces D or attribute space C, the proposed interactive procedure searches solutions in the parameter space W. The existing interactive methods give rise to local decisions to specific MCDM problems, whereas the proposed approach produces global preference models of specific DMs.

## 4.2. An autonomous learning algorithm

Based on the new supervised learning scheme, an autonomous learning algorithm that integrates the dynamical configuration rule and the evolutionary adaptation rule is outlined by a flowchart in Figure 4. A complete feedforward ANN (i.e., the value of adaptable parameters, the number of neurons, and the number of training samples needed) can be determined by the learning algorithm autonomously.

Let $N_{min}$ be the potential minimum number of neuron(s) for a given problem. Let $P(t)$ , $P_{1}(t)$ , and $P_{2}(t)$ be the total number of paired input-output samples in the preferential information database, the number of training samples, the number of testing samples at time t respectively. $P_{1}(t) + P_{2}(t) = P(t)$ and $P(t)$ , $P_{1}(t)$ and $P_{2}(t)$ are integers and monotone nondecreasing with respect to time t, which allow accomodation of new samples. Let $P_{\min(N)}$ be the minimum number of training samples for a given ANN with N neurons. Let error functions for training and testing be defined as weighted sums of mean square errors; i.e., for training $E_{1}[W(t)] = \sum_{p=1}^{P_{1}(t)} \mu_{p}[z^{p} - y(x^{p}, W(t), N(t))]^{2}/P_{1}(t)$ where $(x^{p}, z^{p}) \in S_{trn}$ and $\mu_{p} > 0$ denote the p-th paired input-output sample and the weight of importance for the p-th sample in the training set and for testing $E_{z}[W(t) = \sum_{p=1}^{P_{2}(t)} \mu_{p}[z^{p} - y(x^{p}, W(t), N(t))]^{2}/P_{2}(t)$ where $(x^{p}, z^{p}) \in S_{tst}$ denotes the p-th sample in the testing set. The weight of importance $\mu_{p} (p = 1, 2, \ldots, P(t))$ reflects the confidence level of the DM and/or analyst on the p-th sample. Let $\|\cdot\|$ be a predetermined norm. Let $\epsilon_{1}, \epsilon_{2}$ , and $\epsilon_{3}$ be tolerance levels of training error, testing error, line search error respectively, $\rho$ be a threshold of gradient for dynamical architecture expansion, and $\gamma$ be a step length for the line search along the opposite direction of the gradient.

In the following learning algorithm, Step 0 initializes all variables and constants. Step 1 evaluates the training error function and its gradient. Step 2 controls the learning process through branching. Step 3 determines an interval that brackets a local minimum along the opposite direction of gradient. Step 4 performs golden section search to determine an optimal learning rate parameter along he opposite direction of gradient. Step 5 updates the adaptable parameters (weights and thresholds). Step 6 tests the ANN through on-line evaluation of testing error function. Step 7 checks termination criterion. Step 8 expands the ANN architecture dynamically.

Step 0: Set $N(0) = N_{\min}$ , $P_1(0) = P_{\min [N(0)]}$ , $P_2(0) \geq 1$ , $W(0)$ randomly, $\tau = (\sqrt{5} - 1) / 2 \approx 0.618$ (the golden number), $\gamma > 0$ , $\epsilon_1 \geq 0$ , $\epsilon_2 \geq 0$ , $\epsilon_3 \geq 0$ , $\rho \geq 0$ , and $t = 0$ .

Step 1: For $(x,z)\in S_{trn}$ , evaluate $E_I[W(t)]$ and $G(t)\triangleq \nabla_W E_I[W(t)].$

Step 2: If $E_1[W(t)] \leq \epsilon_1$ , then go to step 6; else, if $\| G(t) \| > \rho$ , go to Step 3, if $\| G(t) \| \leq \rho$ , go to Step 8.

Step 3: If $E_{l}[W(t)] < E_{l}[W(t) - \gamma G(t)], l = \gamma$ and go to Step 4;

if $E_{1}[W(t) - \gamma G(t)] < E_{1}[W(t) - 2\gamma G(t)]$ , then $l = 2\gamma$ and go to Step 4; else $W(t) = W(t) - 2\gamma G(t)$ and repeat Step 3.

Step 4: $W'(t) = W(t) - (1 - \tau)lG(t), \quad W''(t) = W(t) - \tau lG(t),$ if $E_1[W'(t)] < E_1[W''(t)], \text{ then } W''(t) = W'(t), \; W'(t) = W(t) - \tau (1 - \tau)lG(t);$ else $W(t) = W'(t), \; W'(t) = W''(t), \; W''(t) = W(t) - \tau (1 - \tau)lG(t).$

Step 5: If $|E_1[W'(t)] - E_1[W''(t)]| \leq \epsilon_3$ , then $W(t) = [W'(t) + W''(t)] / 2.$ else l = τl and go to Step 4.

Step 6: Evaluate $E_2[w(t)]$ for $(x, z) \in S_{tst}$ .

Step 7: If $E_2[W(t)] \leq \epsilon_2$ for $(x, z) \in S_{tst}$ then $W^* = W(t)$ and stop; else, include one more sample into training set $S_{trn}$ , $P_1(t) = P_1(t) + 1$ , $t = t + 1$ , and go to Step 1.

Step 8: $N(t) = N(t) + 1$ , set associated weights and threshold parameters randomly, $t = t + 1$ , and go to Step 1.

![](/api/attachments/P4KWTYFD/fulltext/images/a0d15cf91167e84a3d8eb4b34a86d2220200ee1054d3bd1c6833d6b1e24e5c48.jpg)

![](/api/attachments/P4KWTYFD/fulltext/images/e14bfd49ae6b5b30b2e5d070066051ac5cfe6c541ce927daae4cc06a6827219f.jpg)  
(a) Additive Preference Structure.  
Fig. 5. Temporal behavior of the feedforward ANNs for $PM_{1}$ .

The selection of error tolerance levels is of an ad hoc nature depending on the requirements and characteristics of the problem under study (e.g., accuracy and timing factors) as well as the analyst's experience and preference. Ideally, $\epsilon_{1}$ , $\epsilon_{2}$ , $\epsilon_{3}$ , and $\rho$ should be zero so that the resultant neural network models could be optima. Practically, however, the optimal neural network models require formidable computation. In general, the lower the tolerance levels the more preference information is needed and the longer an assessment process. Since testing (generalization) results are rarely better than training (approximation) results, it is usually set that $\epsilon_{3} \leq \epsilon_{1} \leq \epsilon_{2}$ .

In the ANN literature, pruning or trimming has been proposed for reduce oversized neural network architecture [e.g., 19]. Training an over-

![](/api/attachments/P4KWTYFD/fulltext/images/54a4de82877ff161804c80ebc92ab09b516cd62192e90aabc3cbf25d3d396c98.jpg)

![](/api/attachments/P4KWTYFD/fulltext/images/6710136c3dfa69cdb9864ca8ab966950bcc5fd6103f49ab444772681c20748fd.jpg)  
(b) Multilinear Preference Structure.

![](/api/attachments/P4KWTYFD/fulltext/images/740d517c212bba3cc795a2be8ed5bceb8fc6eda0ad77b2171e2568b20ab75712.jpg)

![](/api/attachments/P4KWTYFD/fulltext/images/a9c3f751f7c1bf93e85448f72b25e652c1dbec8068ec300475a807c2881af902.jpg)  
Fig. 5 (continued).  
(c) Quadratic Preference Structure.

sized neural network architecture, however, could be avoided in the very beginning since it unnecessarily increases computational burden. Moreover, a pruning process may not always preserve the generalization capability of original networks [19]. The proposed autonomous learning algorithm is a new approach to the very problem. Instead of training potentially oversized neural networks and then trimming them, we purposely avoid oversizing by using a growing architecture. The proposed autonomous learning algorithm starts with a small number of neuron(s) and allows the number to grow when the norm of the gradient of error function is less $\rho$ and both training and testing exceed their tolerance levels $\epsilon_{1}$ and $\epsilon_{2}$ . The proposed autonomous learning algorithm provides a mechanism to balance the computational complexity and representational accuracy. By properly selecting the tolerance level $\rho$ , the size of resultant network can be minimized and overfitting can be avoided. This point is further evidenced by the simulation results in the next section. In general, the smaller the tolerance levels, the larger the sizes of network architecture and training set are required.

![](/api/attachments/P4KWTYFD/fulltext/images/dc194d273161170f8d28368071ee24ec397a1d7071e867b42f63f1911ae8914f.jpg)

![](/api/attachments/P4KWTYFD/fulltext/images/e011e522b37921a804dfb8619dd1247c4b42d040cd363e7f78c35da1143cc7f5.jpg)  
(d) Polynex Preference Structure.

## 5. Computer simulation

A simulator in C code implementing the proposed learning algorithm has been developed where norm $L_{1}$ has been used to measure $\|G(t)\|$ (i.e., $\|G(t)\|=\sum_{i}\sum_{j}|g_{ij}(t)|$ ) and $\forall p,\quad\mu_{p}=1$ . Simulations have been performed using the developed simulator to assess the specified $PM_{1}$ and $PM_{2}$ . For experimental purpose, tri-attribute alternatives have been generated randomly based on the uniform probability distribution over the interval [0, 1]; four different types of multiattribute utility functions, an additive function, a multilinear function, a quadratic functions, and a polynomial-exponential (polynex) function have been assumed to act implicitly as the DM's underlying preference in providing responses of preferential information; i.e.,

![](/api/attachments/P4KWTYFD/fulltext/images/ce035d4197bca9428e54ecdafacba0b3df1c7b8e9ad8c2ab5cdae7ede6d98f52.jpg)

![](/api/attachments/P4KWTYFD/fulltext/images/6e4a0ea0c7eed490b65b636387e437369e416ba3b31ab1d95e5d87ab3c5be216.jpg)

![](/api/attachments/P4KWTYFD/fulltext/images/fde400b198ea849f06a73072ce4137d978facf480b139aa761291c8746080403.jpg)  
(a) Additive Preference Structure.

![](/api/attachments/P4KWTYFD/fulltext/images/c438b9ed55f31ff6330a2a3035ea53fcc3947fa60dbf06359df5d146f5bb7e11.jpg)  
(b) Multilinear Preference Structure.

![](/api/attachments/P4KWTYFD/fulltext/images/df99615bf149a8b3a78c378a295657fb2d27f8edaa04e42e8fa38086983671b6.jpg)

![](/api/attachments/P4KWTYFD/fulltext/images/818b883b4691628b31cb4ae90208ddac8e74a971b2c969f20f3473d8436a5f44.jpg)  
(c) Quadratic Preference Structure.

![](/api/attachments/P4KWTYFD/fulltext/images/4697b044286f6f620fde530c12426c1479b7666bb996fc380be22d0a26b8137a.jpg)

Fig. 6. Temporal behavior of the feedforward ANNS for $PM_{2}$ .  
![](/api/attachments/P4KWTYFD/fulltext/images/f6d95d3d0162b09d03a9f67868ec3aa881c680890db699dddac45e7bcac47445.jpg)  
(d) Polynex Preference Structure.

Table 1  
Summary of numerical simulation results for preference model $PM_{1}$ .

<table><tr><td> $PM_{1}$ </td><td> $E_{1}(W^{*})$ </td><td> $E_{2}(W^{*})$ </td><td>N</td><td> $P_{1}$ </td><td>T</td></tr><tr><td>Additive</td><td> $4.76 \times 10^{-4}$ </td><td> $1.75 \times 10^{-4}$ </td><td>2</td><td>18</td><td>35</td></tr><tr><td>Multilinear</td><td> $4.77 \times 10^{-4}$ </td><td> $1.89 \times 10^{-4}$ </td><td>2</td><td>18</td><td>39</td></tr><tr><td>Quadratic</td><td> $1.14 \times 10^{-4}$ </td><td> $1.98 \times 10^{-4}$ </td><td>4</td><td>85</td><td>10464</td></tr><tr><td>Polynex</td><td> $3.01 \times 10^{-4}$ </td><td> $1.96 \times 10^{-4}$ </td><td>2</td><td>18</td><td>32</td></tr></table>

$$
U _ {1} \left(c _ {1}, c _ {2}, c _ {3}\right) = 0. 5 c _ {1} + 0. 3 c _ {2} + 0. 2 c _ {3} + \epsilon ,
$$

Table 2  
Summary of numerical simulation results for preference model $PM_{2}$ .

<table><tr><td> $PM_2$ </td><td> $E_1(W^*)$ </td><td> $E_2(W^*)$ </td><td>N</td><td> $P_1$ </td><td>T</td></tr><tr><td>Additive</td><td> $1.07\times 10^{-4}$ </td><td> $1.50\times 10^{-4}$ </td><td>2</td><td>30</td><td>8</td></tr><tr><td>Multilinear</td><td> $1.09\times 10^{-4}$ </td><td> $1.95\times 10^{-4}$ </td><td>2</td><td>30</td><td>8</td></tr><tr><td>Quadratic</td><td> $2.05\times 10^{-4}$ </td><td> $1.97\times 10^{-4}$ </td><td>5</td><td>54</td><td>6954</td></tr><tr><td>Polynex</td><td> $0.66\times 10^{-4}$ </td><td> $1.99\times 10^{-4}$ </td><td>5</td><td>80</td><td>7925</td></tr></table>

$$
\begin{array}{r l} U _ {2} (c _ {1}, c _ {2}, c _ {3}) & = 0. 4 c _ {1} + 0. 3 c _ {2} + 0. 2 c _ {3} + 0. 0 4 c _ {1} c _ {2} \\ & \quad + 0. 0 3 c _ {1} c _ {3} + 0. 0 2 c _ {2} c _ {3} \\ & \quad + 0. 0 1 c _ {1} c _ {2} c _ {3} + \epsilon , \end{array}
$$

$$
\begin{array}{c} U _ {3} (c _ {1}, c _ {2}, c _ {3}) = c _ {1} + 0. 6 c _ {2} + 0. 4 c _ {3} - 0. 5 c _ {1} ^ {2} \\ - 0. 3 c _ {2} ^ {2} - 0. 2 c _ {3} ^ {2} + \epsilon , \end{array}
$$

$$
\begin{array}{c} U _ {4} (c _ {1}, c _ {2}, c _ {3}) = 0. 5 c _ {2} e ^ {3 c _ {1} - 3} + 0. 3 c _ {3} ^ {2} e ^ {2 c _ {2} - 2} \\ + 0. 2 c _ {1} ^ {3} e ^ {c _ {3} - 1} + \epsilon , \end{array}
$$

Table 3  
Testing errors of individual sample for the ANN-based $PM_{1}s$ .

<table><tr><td>No.</td><td> $c_1, c_2, c_3$ </td><td>ADD</td><td>MLN</td><td>QUD</td><td>PLX</td></tr><tr><td>1</td><td>0.7210, 0.9977, 0.4211</td><td>0.0201</td><td>0.0196</td><td>-0.0080</td><td>-0.0118</td></tr><tr><td>2</td><td>0.5622, 0.3767, 0.9836</td><td>0.0083</td><td>0.0071</td><td>-0.0470</td><td>0.0305</td></tr><tr><td>3</td><td>0.0146, 0.9421, 0.4523</td><td>0.0128</td><td>0.0017</td><td>0.0026</td><td>-0.0198</td></tr><tr><td>4</td><td>0.2373, 0.5464, 0.4946</td><td>0.0021</td><td>0.0001</td><td>0.0027</td><td>-0.0095</td></tr><tr><td>5</td><td>0.6263, 0.7078, 0.5833</td><td>0.0064</td><td>0.0076</td><td>-0.0167</td><td>-0.0012</td></tr><tr><td>6</td><td>0.7898, 0.4325, 0.0037</td><td>-0.0211</td><td>-0.0222</td><td>-0.0048</td><td>0.0050</td></tr><tr><td>7</td><td>0.8356, 0.7160, 0.9867</td><td>0.0473</td><td>0.0520</td><td>0.0042</td><td>-0.0060</td></tr><tr><td>8</td><td>0.4572, 0.3529, 0.9392</td><td>0.0078</td><td>0.0055</td><td>-0.0278</td><td>-0.0295</td></tr><tr><td>9</td><td>0.6445, 0.5647, 0.6985</td><td>0.0053</td><td>0.0066</td><td>-0.0205</td><td>0.0001</td></tr><tr><td>10</td><td>0.2235, 0.3098, 0.8983</td><td>0.0076</td><td>0.0027</td><td>0.0123</td><td>0.0376</td></tr></table>

Table 4  
Testing errors of individual sample for the ANN-based $PM_{2}s$ .

<table><tr><td>No.</td><td> $c_1', c_2', c_3'; c_1'', c_2'', c_3''$ </td><td>ADD</td><td>MLN</td><td>QUD</td><td>PLX</td></tr><tr><td>1</td><td>0.9313, 0.4897, 0.4046; 0.0917, 0.6465, 0.3491</td><td>0.0061</td><td>-0.0007</td><td>0.0013</td><td>-0.0007</td></tr><tr><td>2</td><td>0.5497, 0.4705, 0.1448; 0.6305, 0.8610, 0.6507</td><td>-0.0198</td><td>-0.0107</td><td>0.0097</td><td>-0.0068</td></tr><tr><td>3</td><td>0.9065, 0.9641, 0.3835; 0.4489, 0.2356, 0.0303</td><td>0.0223</td><td>-0.0276</td><td>-0.0122</td><td>-0.0142</td></tr><tr><td>4</td><td>0.2178, 0.6928, 0.6643; 0.5562, 0.9469, 0.9885</td><td>-0.0178</td><td>0.0223</td><td>0.0172</td><td>-0.0358</td></tr><tr><td>5</td><td>0.1842, 0.0227, 0.5974; 0.7573, 0.5456, 0.0583</td><td>0.0168</td><td>-0.0209</td><td>0.0289</td><td>-0.0166</td></tr><tr><td>6</td><td>0.3300, 0.8856, 0.9563; 0.0537, 0.8272, 0.3277</td><td>0.0072</td><td>0.0199</td><td>-0.0028</td><td>0.0218</td></tr><tr><td>7</td><td>0.3998, 0.5913, 0.8467; 0.5091, 0.2916, 0.7817</td><td>0.0139</td><td>0.0156</td><td>-0.0357</td><td>0.0066</td></tr><tr><td>8</td><td>0.9101, 0.8718, 0.6919; 0.1035, 0.5941, 0.4056</td><td>0.0206</td><td>0.0120</td><td>0.0080</td><td>-0.0322</td></tr><tr><td>9</td><td>0.7936, 0.8384, 0.3955; 0.5100, 0.9050, 0.6948</td><td>-0.0256</td><td>0.0229</td><td>-0.0071</td><td>-0.0060</td></tr><tr><td>10</td><td>0.6356, 0.0298, 0.6446; 0.7163, 0.3755, 0.8082</td><td>0.0124</td><td>-0.0281</td><td>-0.0340</td><td>0.0240</td></tr></table>

where $\epsilon$ is white Gaussian noise with variance being 0.0001. Ten input–output samples that are independent of training samples have been used as testing samples. A potential minimum number of neurons, a modest step length and error tolerance levels have been chosen; i.e., $N_{min} = 2$ , $\gamma = 0.01$ , $\epsilon_{1} = \epsilon_{3} = \rho = 0.0001$ , $\epsilon_{2} = 0.0002$ for both $PM_{2}$ . The minimum number of training samples is twice as many as the number of the adaptable parameters; i.e., $P_{\min(N)} = N(N + 2n + 1)$ .

Figures 5 and 6 show the temporal behavior of the training and testing errors, the numbers of neurons and training samples, with respect to epoch. The spikes of the training error are induced by the expansion of the neural network architecture and the inclusion of new training samples.

Tables 1 and 2 summarize the results of numerical simulations for assessed preference models $PM_{1}$ and $PM_{2}$ respectively based on the hypothetical additive, multilinear, quadratic, and polynex utility functions. The entries in the second and third columns of the tables are the mean square training and testing errors respectively. The entries in the fourth, fifth, and sixth columns are the final number of neurons, the number of training samples included in $S_{trn}$ , and the number of epochs respectively. More detailed simulation results are recorded in Appendices.

The results of the simulation show that the configured neural networks possess the capability of learning from examples. The configured artificial neural networks can determine the most preferred alternatives based on the implicit multiattribute utility functions correctly and the samples in both training and testing sets. The actual outputs of the synthesized artificial neural networks are also reasonably close to the target outputs for the samples in both training and testing sets. The simulation results also show that the number of neurons and training samples increase only when necessary. For example, for the implicit additive and multilinear multiattribute utility functions, the initially specified neurons and training samples were sufficient to reduce the training error and testing error to the specified tolerance levels. The neural network architecture and training set grew in the cases in which quadratic and polynex multiattribute value functions were used to provide the DM's responses. Because the proposed learning algorithm is inherently autonomous, the total configuration time for the neural networks is much less than that using conventional learning algorithms.

## 6. Conclusion

We have delineated a connectionist approach to preference assessment. Specifically, we have introduced two general preference models, described an interactive preference assessment procedure based on a new supervised learning scheme, and discussed the performance of proposed paradigm in numerical simulation. The proposed connectionist approach provides a specific paradigm for preference model and assessment procedure in a general setting of multiple criteria decision making. We believe that the proposed approach could be very useful in representing DM's preference, especially the complex ones in real world applications. In principle, the proposed interactive assessment procedure and autonomous learning algorithm are able to approximate any preference structure. Since the proposed learning algorithm starts with a small ANN architecture and a small training set and construct the ANN-based preference models autonomously, the neural network synthesis time is substantially reduced and the assessment procedure is easily accessible to unexperienced users. Because the learning process terminates according to the result of an independent testing, the creditability of trained ANN-based preference models is increased. Although the proposed autonomous learning algorithm has been developed for preference assessment in this paper, it is applicable to other areas as well.

There is a significant potential for future work. Further investigations in this direction have been aimed at specification of new preference models, development of more effective and efficient assessment procedures and ANN paradigms, and implementation of decision support systems based on the proposed connectionist approach. Because of its desirable features, the proposed approach is particularly suitable to be a core for a connectionist decision support system $[24]$ . An integration of the connectionist approach into a decision support system could produce a powerful paradigm for multiple criteria decision analysis.

Acknowledgment: The author would like to thank the anonymous referees and the guest editor for their comments and suggestions for improving an earlier version of this paper.

## References

[1] D.E. Bell, H. Raiffa, and A. Tversky, Descriptive, Normative, and Prescriptive Interactions in Decision Making, in: D.E. Bell, H. Raiffa, and A. Tversky, Eds., Decision Making: Descriptive, Normative, and Prescriptive Interactions, (Cambridge University Press, Cambridge, England, 1988, 9–30).

[2] D.E. Bell, Consistent Assessment Procedures Using Conditional Utility Functions, Operations Research 27, Nr. 5 (1979) 1054–1066.

[3] V. Chankong and Y.Y. Haimes, Multiobjective Decision Making: Theory and Methodology, (North-Holland Publishing Comp., New York, NY, 1983; ISBN: 0-444-00710-5).

[4] J.S. Dyer, Remarks on the Analytic Hierarchy Process, Management Science 36, Nr. 3, (1990) 249–258.

[5] J.S. Dyer and R.K. Sarin, Measurable Multiattribute Value Functions, Operations Research 27, (1979) 810-822.

[6] P.H. Farquhar, A Fractional Hypercube Decomposition Theorem for Multiattribute Utility Functions, Operations Research 23, (1975) 941–967.

[7] P.G. Fishburn, von Neumann Morgenstern Utility Functions on Two Attributes, Operations Research 22, (1974) 35–45.

[8] P.G. Fishburn, Bernouillian Utilities for Multiple-Factor Situations, in: J.L. Cochrane and M. Zeleny, Eds. Multiple Criteria Decision Making, (Univ. of South Carolina Press, Columbia, SC, 1973, 47–61).

[9] K. Funahashi, On the Approximate Realization of Continuous Mappings by Neural Networks, Neural Networks 2, Nr. 3, (1989) 183–192.

[10] J. Hershey, H. Kunreuther, and P. Schoemaker, Sources of Bias in Assessment Procedures for Utility Functions, in: D.E. Bell, H. Raiffa, and A. Tversky, Eds., Decision Making: Descriptive, Normative, and Prescriptive Interactions, (Cambridge University Press, Cambridge, England, 1988, 422–442).

[11] K. Hornik, M. Stinchcombe, and H. White, Multilayer Feedforward Networks are Universal Approximators, Neural Networks 2, Nr. 5 (1989) 359–366.

[12] R.G. Javalgi and H.K. Jain, Integrating Multiple Criteria Decision Making Models into the Decision Support System Framework for Marketing Decisions, Naval Research Logistics Quarterly 35 (1988) 575–591.

[13] R.L. Keeney and H. Raiffa, Decisions with Multiple Objectives: Preference and Value Tradeoffs, (John Wiley & Sons, New York, NY, 1976).

[14] C.W. Kirkwood, Parametrically Dependent Preferences for Multiattributed Consequences, Operations Research 24 (1976) 92–103.

[15] K. Narendra and K. Parthasarathy, Identification and Control of Dynamical Systems using Neural Networks, IEEE Transactions on Neural Networks 1, Nr. 1 (1990) 4–27.

[16] D.E. Rumelhart, G.E. Hinton, and R.J. Williams, Learning Internal Representations by Error Propagation, in: D.E. Rumelhart, J.L. McClelland, and the PDP Research Group, Eds., Parallel Distributed Processing - Explorations in the Microstructures of Cognition, Vol. 1: Foundations, MIT Press, Cambridge, MA, 1986 318–362).

[17] T.L. Saaty, The Analytic Hierarchy Process, (McGraw-Hill, New York, NY, 1980).

[18] Y. Shi and P.'L. Yu, Habitual Domain Analysis for Effective Decision Making, Asia-Pacific Journal of Operational Research 4 (1987) 131–150.

[19] J. Sietsma and R. Dow, Creative Artificial Neural Networks That Generalize, Neural Networks 4 (1991) 67–79.

[20] M. Tenorio and W. Lee, Self-Organizing Network for Optimum Supervised Learning, IEEE Transactions on Neural Networks 1 (1990) 100–110.

[21] J. Wang and B. Malakooti, Analysis and Synthesis of Artificial Neural Networks for Modeling Complex Systems, in Progress in Neural Networks, 2, in: O.M. Omidvar, Ed., (Ablex Publishing Corporation, Norwood, NJ, 1993, in press); also Technical Report 90–156, Center for Automation and Intelligent Systems Research, Case Western Reserve University, Cleveland, Ohio (1990).

[22] J. Wang and B. Malakooti, A Feedforward Neural Network for Multiple Criteria Decision Making, Computers & Operations Research 19, Nr. 2, (1992) 151–167.

[23] J. Wang, Dynamical Configuration of Neural Network Architectures, Proceedings of IEEE International Conference on Systems, Man, Cybernetis, (IEEE Press, New York, NY, 1990, 376–378).

[24] J. Wang and M. Bender, Connectionist Decision Support systems for Multiple Criteria Decision Making, in Proceedings of IEEE International Conference on Systems, Man, and Cybernetics (IEEE Press, New York, NY, 1991, 1955–1960).

[25] A.S. Weigend, B.A. Huberman, and D.E. Rumelhart, Predicting the Future: A Connectionist Approach, International Journal of Neural Systems 1 (1991) 193.

[26] M. Zeleny, Stable Patterns from Decision-Producing Networks: New Interfaces of DSS and MCDM, MCDM WorldScan 3 (1989) 6–7.

## Appendices

## A.1. Training errors and testing errors of individual samples

Tables 3 and 4 record the testing error $z^{p}-y^{p}$ of individual samples $(x^{p},z^{p})\in S_{tst}$ for p=1, $2,\ldots,P_{2}$ of the trained feedforward neural networks for $PM_{1}$ and $PM_{2}$ , where the target samples used are the true (noncontaminated) values of desired outputs, ADD stands for additive utility function, MLN for multilinear utility function, QUD for quadratic utility function, and PLX for polynex utility function.

## A.2. Parameter matrices for the trained feedforward neural networks

For $PM_{1}$ based on the implicit additive utility function $U_{1}$ ,

$$
W ^ {\prime} = \left| \begin{array}{c c c c c c} 0 & - 0. 9 8 0 7 & 1. 9 9 0 5 & 1. 0 6 1 1 & 0. 7 2 2 1 & - 1. 3 7 0 1 \\ 0 & 0 & - 0. 3 4 8 4 & - 0. 2 1 9 8 & 0. 1 0 9 5 & 0. 3 1 5 5 \end{array} \right|;
$$

for $PM_{1}$ based on the implicit multilinear utility function $U_{2}$ ,

$$
W ^ {*} = \left| \begin{array}{c c c c c} 0 & - 1. 0 1 4 4 & 1. 7 1 7 5 & 1. 1 9 1 9 & 0. 8 3 8 1 \\ 0 & 0 & - 0. 3 3 1 0 & - 0. 2 4 3 7 & 0. 0 8 7 0 \end{array} \right|;   - 1. 4 4 5 2
$$

for $PM_{1}$ based on the implicit quadratic utility function $U_{3}$ ,

$$
W ^ {*} = \left| \begin{array}{c c c c c c c c} 0 & - 2. 8 4 4 3 & - 0. 0 3 0 5 & 4. 7 6 6 5 & - 0. 8 0 0 4 & 2. 1 5 6 1 & 0. 8 9 7 9 & - 2. 5 4 9 9 \\ 0 & 0 & 0. 2 7 8 5 & 0. 9 1 4 2 & 1. 7 7 3 8 & - 1. 5 1 3 6 & - 2. 3 2 7 7 & 0. 7 1 9 2 \\ 0 & 0 & 0 & - 0. 5 3 9 7 & - 0. 2 0 6 9 & 3. 2 1 5 7 & - 1. 5 2 8 3 & - 2. 3 6 4 4 \\ 0 & 0 & 0 & 0 & 3. 9 3 3 6 & - 0. 6 8 4 0 & - 1. 8 8 9 4 & 0. 6 5 0 4 \end{array} \right|;
$$

for $PM_{1}$ based on the implicit polynex utility function $U_{4}$ ,

$$
W ^ {*} = \left| \begin{array}{c c c c c c} 0 & - 1. 9 1 5 7 & 1. 1 1 5 0 & 1. 6 5 2 8 & 1. 7 0 9 0 & - 2. 8 2 8 9 \\ 0 & 0 & - 0. 3 8 4 8 & - 0. 5 5 9 7 & - 0. 3 0 9 5 & 0. 7 5 9 4 \end{array} \right|.
$$

For $PM_{2}$ based on the implicit additive utility function $U_{1}$ ,

$$
W ^ {*} = \left| \begin{array}{c c c c c c c c} 0 & - 0. 1 0 8 3 & 1. 0 6 5 9 & 0. 6 9 4 0 & 0. 3 1 7 8 & - 0. 9 7 1 5 & - 0. 4 6 9 2 & - 0. 3 3 4 8 & - 0. 1 0 6 4 \\ 0 & 0 & 0. 1 3 8 8 & 0. 1 8 1 6 & 0. 1 4 1 2 & - 0. 0 0 0 5 & 0. 0 6 9 7 & 0. 0 9 1 0 & 0. 0 4 1 3 \end{array} \right|;
$$

for $PM_{2}$ based on the implicit multilinear utility function $U_{2}$ ,

$$
W ^ {*} = \left| \begin{array}{c c c c c c c c c} 0 & - 0. 1 0 7 5 & 0. 9 7 1 7 & 0. 7 3 1 2 & 0. 3 5 7 4 & - 0. 8 4 8 3 & - 0. 5 4 2 2 & - 0. 3 5 6 0 & - 0. 1 0 0 8 \\ 0 & 0 & 0. 1 4 2 2 & 0. 1 8 0 6 & 0. 1 3 9 9 & - 0. 0 0 4 9 & 0. 0 7 2 0 & 0. 0 9 1 6 & 0. 0 4 0 9 \end{array} \right|;
$$

for $PM_{2}$ based on the implicit quadratic utility function $U_{3}$ ,

$$
W ^ {*} = \left| \right.\begin{array}{c c c c c c c c c c c}0&1. 2 0 1 7 - 1. 1 0 0&1. 7 9 7 7&- 2. 4 2 5 7&0. 2 9 4 8&0. 9 0 7 9&0. 1 4 8 4&- 0. 3 6 6 6 6&- 1. 6 0 5 6&- 1. 2 0 4 9&- 0. 1 3 9 6\\0&0&- 1. 5 2 8 0&- 0. 4 4 9 8&- 0. 5 6 8 3&- 0. 7 5 7 7&- 0. 9 4 9 0&2. 5 1 2 8&2. 3 2 1 3&2. 9 2 8 7&- 1. 0 9 3 0\\0&0&0&- 0. 3 9 2 7&- 0. 1 4 9 6&- 0. 2 1 3 7&- 0. 4 4 2 3 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\\\hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline\\\hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline\end{array};
$$

for $PM_{2}$ based on the implicit polynex utility function $U_{4}$ ,

$$
W ^ {*} = \left| \begin{array}{c c c c c c c c c c c} 0 & - 5. 5 9 5 6 & 0. 0 2 8 5 & 3. 3 4 9 0 & 1. 2 5 5 2 & 1. 3 7 9 2 & 2. 2 0 7 6 & 1. 8 4 5 5 & 0. 4 2 9 7 & - 1. 4 9 1 6 & - 0. 5 4 7 5 & 0. 5 3 6 5 \\ 0 & 0 & - 0. 4 2 2 3 & 1. 8 4 8 6 & - 1. 0 5 4 8 & 0. 8 1 1 1 & 1. 3 6 6 9 & 1. 0 8 2 1 & 0. 7 5 6 9 & - 0. 2 8 8 9 & 0. 4 4 8 6 & - 0. 3 8 2 3 \\ 0 & 0 & 0 & - 0. 3 4 8 5 & - 0. 1 1 6 4 & 0. 3 0 3 1 & 0. 3 2 3 4 & 0. 1 2 8 9 & - 0. 6 4 7 3 & 0. 0 7 5 2 & 0. 1 4 4 4 & - 0. 4 9 5 4 \\ 0 & 0 & 0 & 0 & - 1. 8 4 6 6 & 1. 4 1 1 5 & \text {2.7110} & - \text {0.5659} & - \text {2.5952} & \text {0.6584} & \text {0.0334} & - \text {2.3598} \\ \text {0} & \text {0} & \text {0} & \text {0} & \text {0} & - \text {0.4923} & - \text {0.2826} & - \text {0.1061} & \text {1.0179} & \text {1.3116} & \text {1.9634} & \text {0.1683} \end{array} \right|
$$

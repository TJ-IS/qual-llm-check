---
otero_id: 9342
otero_key: "BDXF4GS2"
title: "Predicting performances in business processes using deep neural networks"
authors: "Gyunam Park; Minseok Song"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.113191"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Journal Pre-proof

Predicting Performances in Business processes using Deep Neural Networks

Decision Support Systems

Gyunam Park, Minseok Song

![](/api/attachments/BDXF4GS2/fulltext/images/95159ec84a4b1483360348478cfe885f9733daaa983281e24546b31e498521f3.jpg)

PII: S0167-9236(19)30220-9

DOI: https://doi.org/10.1016/j.dss.2019.113191

Reference: DECSUP 13191

To appear in: Decision Support Systems

Received date: 2 July 2019

Revised date: 18 October 2019

Accepted date: 4 November 2019

Please cite this article as: G. Park and M. Song, Predicting Performances in Business processes using Deep Neural Networks, Decision Support Systems (2019), https://doi.org/ 10.1016/j.dss.2019.113191

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2019 Published by Elsevier.

# Predicting Performances in Business processes using Deep Neural Networks

Gyunam Park, Minseok Song<sup>∗</sup>

Department of Industrial & Management Engineering, POSTECH (Pohang University of Science and Technology), Pohang, Republic of Korea

## Abstract

Online operational support is gaining increasing interest due to the availability of real-time data and suficient computing power, such as predictive business process monitoring. Predictive business process monitoring aims at providing timely information that enables proactive and corrective actions to improve process enactments and mitigate risks. There are a handful of research works focusing on the predictions at the instance level. However, it is more practical to predict the performance of processes at the process model level and detect potential weaknesses in the process to facilitate the proactive actions that will improve the process execution. Thus, in this paper, we propose a novel method to predict the future performances of a business process at the process model level. More in detail, we construct an annotated transition system and generate a process representation matrix from it. Based on the process representation matrix, we build performance prediction models using deep neural networks that consider both spatial and temporal dependencies present in the underlying business process. To validate the proposed method, we performed case studies on three real-life logs.

Keywords: Process mining, Process management, Online operational support, Process performance prediction, Deep neural networks

## 1. Introduction

In today’s competitive and challenging business world, it is of utmost importance to consistently improve business processes [1]. Process mining, a promising discipline that aims at extracting process-oriented knowledge from event data stored in information systems, has provided practical techniques to that end. Traditionally, process mining focus on analyzing historical data in order to fully understand the process of an organization and identify possible improvements [2]. In recent years, research in process mining has shifted the spotlight from this ofline analysis to online operational support due to the availability of realtime data and suficient computing power. Diferent from the ofline analysis, online operational support aims at monitoring and influencing running cases. As one of the approaches in online operational support, predictive business process monitoring provides timely information that enables proactive and corrective actions to improve process enactments and mitigate risks [3]. Task/resource recommendations [4] and risk notifications [5] are examples of those actions.

Existing studies in predictive business process monitoring focus on making predictions at the process instance level (e.g., predicting the remaining time for an instance to complete the process) [6] and identifying problematic instances (e.g., delayed instances) based on them. However, it is dificult for an operation manager to manage singular process instances in the complex business process [7]. Instead, it is more practical to predict the performance of processes at the process model level (e.g., predicting the processing time and waiting time of activities in the process) and detect potential weakness (e.g., delayed activities) in the process to facilitate the proactive actions that will improve the process execution. For example, in the context of trafic congestion, we focus on not each vehicle (i.e., each instance) but roads or junctions (i.e., activities in a process model).

Suppose the temporal performance of a business process evolves over a given period due to the changes in the process context (e.g., number of cases in progress, number of resources allocated to process, etc.) [2], as shown in Fig. 1.

![](/api/attachments/BDXF4GS2/fulltext/images/22f9d76cf35627a281ff65646728ffe533828442b493647455982fa57e1569bf.jpg)  
Figure 1: An example of performance evolution in a business process

During time window<sub>1</sub>(01:00 ∼ 02:00), exceptionally large number of cases enter the process causing delay in activity A. At time window (02:00 ∼ 03:00), the limited number of resources causes the next delay in activity B and activity C. Finally, the accumulated demands for activity D after finishing either activity B or activity C result in the new delay on activity D. If it recurs regularly and is expected to be valid in the future, we call it a pattern [8]. Given this pattern, at time window<sub>2</sub>, one can predict the problematic point in the business process (i.e., activity D) and take proactive actions such as assigning more resources to serve it and finding an alternative activity to bypass it.

Thus, in this paper, we aim at developing a method to predict the future performances of a business process at the process model level to enable proactive actions to improve the business process. To this end, we concentrate on the similarity between the trafic and the business process model [2]. We can think of cars in the trafic as cases in the business process model, roads as activities, and movements as events. The congestion in the trafic can be understood as bottlenecks in the business process. In the field of trafic research, the congestion prediction, that aims at predicting the future speed of roads based on historical observations, is known as an essential but challenging problem [9]. In recent years, the large volume of trafic data enables the researchers to develop novel prediction algorithms based on it. Among those data-driven methods, deep learning-based approaches, that deploy techniques for image/video processing, have achieved significant success [10, 11, 12].

Motivated by the recent breakthroughs in congestion prediction problems, we propose a novel method to predict the future performances of a business process based on deep neural networks (DNN). More in detail, we first discover a process model from an event log and annotate it with relevant information by replaying the log. Next, we generate a process representation matrix that contains information on the performances in the business process. Finally, we generate a training set from the process representation matrix and construct performance prediction models based on DNN that consider temporal evolution and spatial dependency of the process model.

The paper is organized as follows. Section 2 discusses the related work. Section 3 explains the backgrounds required to understand the proposed method. The performance prediction method is explained in Section 4 and evaluated on two real-life logs in Section 5. Section 6 discusses the usefulness and limitation of the proposed method. Finally, Section 7 concludes this paper.

## 2. Related work

## 2.1. Predictive business process monitoring

Predicting performances in business processes is concerned with the research of predictive business process monitoring, which is one of the sub-fields of process mining. It encompasses the set of methods to build predictive models aiming at providing timely information which can be used to improve the business process and mitigate possible process-related risks.

Several approaches have been proposed to predict three types of values: 1) remaining time, 2) risk probability, and 3) next event [3]. First, the remaining time prediction is concerned with the completion time of business process instances. Van der Aalst et al. [6] suggests a configurable method to construct a process model where the annotated values are used to predict the remaining time of instances. Extending on [6], Polato et al. [13] proposes a method to predict the remaining time using a set of machine learning approaches, such as Naive Bayes and Support Vector Regression (SVR). Second, the risk prediction generates various process-related risks in a business process. Pika et al. [14] propose a set of process risk indicators such as abnormal execution time and repetition of multiple events and predict them with statistical techniques. Kang et al. [15] develop the monitoring system to predict the abnormal termination of a running instance using the K-Nearest Neighbor technique. Finally, the next event prediction deals with what the next event (e.g., activity, resource, and timestamp) will become. Breuker et al. [16] develop a method to determine the next activity in a running instance using Probabilistic Finite Automaton (PFA) built upon a Petri net. Motivated by natural language processing, a couple of approaches [17, 18] apply the recurrent neural network (RNN) to predict the next event in a business process. These approaches are extended by Mehidiyev et al. [19], where the authors utilized a deep learning architecture composed of unsupervised stacked autoencoders and supervised fine-tuning with n-gram features which are leveraged by feature hashing.

Existing studies in predictive business process monitoring focus on predicting the future status of running instances. This instance-level prediction enables operational support for enhancement in productivity. For example, operation manager can take actions for instances which are expected to be delayed or prone to risks. However, this microscopic approach is not suficient for the comprehensive management of a business process. In this regards, we need to provide the model-level predictions such as the future bottlenecks in the business process to enable proactive actions to mitigate them.

## 2.2. Congestion prediction

Congestion prediction problem, one of the most attractive problems in transportation management, means to predict the future speed of roads based on historical observations. Over the last few years, the availability of trafic data has been increased, and many approaches try to solve the problem in a data-driven manner [20].

Recently, deep learning algorithms with its competency in extracting features are widely applied to the congestion prediction problem. The deep-learningbased methods pay special attention to learn spatial and temporal correlations existing in a trafic network. Ma et al. [10] applies a Long-Short Term Memory neural network (LSTM NN) to capture the dynamic nature of the trafic network. A couple of approaches based on Convolutional Neural Networks (CNN) are also presented in recent years [21, 11], showing good performances. To consider network structure, Yu et al. [12] proposes a method which incorporates CNN and LSTM.

Motivated by the recent breakthroughs in the congestion prediction problem, We develop a novel method to predict the future performances of a business process given historical observations. To this end, We extend the deep-learningbased models suggested in this literature.

## 3. Backgrounds

This section describes the background necessary to understand our approach. We first explain preliminary concepts related to process mining that we will use throughout the paper. Second, we elaborate transition system we use to discover a process model from the event log. Finally, we provide basic concepts of three

## 3.1. Preliminaries

Process mining techniques can extract useful information from event logs. An event log is detailed information about the activities that have been executed in a single process [2]. In this sub-section, we give formal definition of event, trace and event log. First, an event is a record of the execution of an activity. It contains information such as activity, resource, timestamp.

Definition 1 (Event). Let E be the event universe. Events are characterized by various attributes (e.g., activity, originator, timestamp). Let AN be a set of attribute names. For any event $e \in { \mathcal { E } }$ and any attribute name an $\in \mathcal { A } \mathcal { N } , \pi _ { a n } ( e )$ is the value of an for event e. If e does not contain the attribute an, $\pi _ { a n } ( e ) = \bot$

Each event is associated with the process instance (e.g., customer, patient, or student) which has its trace. Trace is a sequence of events. For example, a patient might undergo a sequence of events, $\mathrm { e . g . }$ , Blood test, MRI, and Treatment. An event log is a collection of process instances. The formal definition is as follows:

Definition 2 (Trace, Event log). Let $\mathcal { E } ^ { * }$ be the set of all finite sequences over E. A trace, $\sigma \in { \mathcal { E } } ^ { * }$ , is a finite sequence of events. Each event in a trace appears only once and time is non-decreasing. For $\sigma = \langle e _ { 1 } , e _ { 2 } , . . . , e _ { n } \rangle , h d ^ { k } ( \sigma )$ consists of first k elements, i.e., $h d ^ { k } ( \sigma ) = \langle e _ { 1 } , e _ { 2 } . . . , e _ { k } \rangle$ i. On the other hand, $t l ^ { k } ( \sigma )$ consists of the last k elements, i.e., $t l ^ { k } ( \sigma ) = \langle e _ { n - k + 1 } , . . . , e _ { n } \rangle$ . Let C be the set of traces. An event log L is a collection of traces, i.e., $\mathcal { L } = \{ \sigma _ { c } | c \in \mathcal { C } \}$

## 3.2. Transition system

A transition system is one of the most eficient approaches to model the behaviors in an event log [2]. A transition system is composed of states, event labels, and transitions that describe how the system moves from one state to another. States represent the status of the system, and transitions enable the system to move from a particular state to another state. Event labels indicate particular events which trigger the transitions. Transition systems have one or more initial and final states. From the transition system, one can reason about the behavior of a process. Starting from the initial states and finishing at the final states, any path in the graph corresponds to a possible execution sequence in the business process.

State representation function and event representation function are two core functions to construct the transition system. The formal definition of them is as follows:

Definition 3 (State & Event Representation Function). A state representation function $l ^ { s } \in \mathcal { C }  \mathbb { R } ^ { s }$ produces a representation of a (partial) trace $\sigma _ { \mathrm { { : } } }$ where C is the set of traces and $\mathbb { R } ^ { s }$ is the set of state representations (e.g., sequences, sets, multiset). An event representation function $l ^ { e } \in E \to \mathbb { R } ^ { e }$ produces a representation of an event $e ,$ where $\mathbb { R } ^ { e }$ is the set of event representations $( e . g .$ $\pi _ { A } ( e ) , \pi _ { \tau } ( e ) . )$ 1

A transition system can be produced based on l<sup>s</sup> and l<sup>e</sup>. With the state representation function l<sup>s</sup>, the prefixes in the log are transformed to the states, creating a state space S (i.e., possible states of the process). Afterwards, the transition T is computed by replaying the process instances and connecting states $s \in S .$ , while using the event representation function l<sup>e</sup> to generate event label E of the transition. Formally, it is defined as follows:

Definition 4 (Transition System). A transition system T S is defined as a triplet (S, E, T ) such that $S ~ = ~ \{ l ^ { s } ( h d ^ { k } ( \sigma ) ) | \sigma ~ \in ~ L \wedge 0 ~ \leq ~ k ~ \leq ~ | \sigma | \} , ~ E ~ =$ $\{ l ^ { e } ( \sigma ( k ) ) | \sigma \in L \land 1 \leq k \leq | \sigma | \}$ , and $T = \{ l ^ { s } ( h d ^ { k } ( \sigma ) ) , l ^ { e } ( \sigma ( k { + } 1 ) ) , l ^ { s } ( h d ^ { k { + } 1 } ( \sigma ) ) | \sigma \in$ $L \wedge 0 \leq k \leq | \sigma | \} . ~ S ^ { s t a r t } = \{ l ^ { s } ( \langle \rangle ) \}$ is the set of initial states and $S ^ { e n d } =$ $\{ l ^ { s } ( \sigma ) | \sigma \in L \}$ is the set of final states.

We can produce various forms of transition systems based on diferent abstractions: representation, horizon, and filter [6]. First, representation determines whether to remove the order and frequency from the trace or not. Second, horizon means how many events are considered from the prefix to derive the states. Third, filter decides which events to consider when calculating the state. For a more detailed explanation, see van der Aalst et al. [6].

## 3.3. Deep neural networks

Deep neural networks (DNN) have been successfully applied to various domains [22]. In the following, we will explain the architectures of DNN we use in this paper.

## 3.3.1. Convolutional neural network

Convolutional Neural Network (CNN) has an exceptional ability to understand the spatial structure of an input (e.g., image). Having this competency, CNN has achieved remarkable improvements in visual tasks such as image and video recognition [23].

CNN is composed of model input, feature extraction layers, fully connected

layer, and model output. First, let model input be:

$$
x = [ x _ {1}, x _ {2},, x _ {n} ], \text {   where   } x _ {i} \in \mathbb {R} ^ {n}, \forall i \in [ 1, n ].\tag{1}
$$

The combination of convolutional and pooling layers extract the features from the input. More in detail, the convolutional layer captures the local features present in the model input by a set of learnable filters called convolutional kernels $w \in \mathbb { R } ^ { m \times m }$ . The kernel convolves every possible window of the model input, resulting in the feature map:

$$
c \in \mathbb {R} ^ {(n + m - 1) \times (n + m - 1)} \text {   such   that   } c _ {i, j} = f (\sum_ {k} \sum_ {l} w _ {k, l} x _ {i + k - 1, j + l - 1} + b)\tag{2}
$$

,where $b \in R$ is the bias and $f$ is a non-linear activation function. The pooling layer addresses the most important features by pooling (e.g., max pooling) over every feature map. The resulting feature map p is computed by:

$$
p = [ p o o l (c) ]\tag{3}
$$

Finally, the pooled feature maps from diferent kernels is concatenated and flattened:

$$
p ^ {f l a t t e n} = f l a t t e n ([ p ])\tag{4}
$$

It is then passed to the fully connected layer and transformed into model output:

$$
\hat {y} = w _ {f} \cdot p ^ {f l a t t e n} + b _ {f}\tag{5}
$$

where $w _ { f }$ is the weight of the layer and $b _ { f }$ is the bias.

## 3.3.2. Long-short-term memory neural network

Recurrent Neural Network (RNN) has a competency to learn temporal dynamics. Fig. 2 shows the architecture of RNN where the hidden states are generated in recurrent manner to maintain information over time. Let g be an activation function (e.g., sigmoid or hyperbolic tangent), $x _ { t }$ be the input, $h _ { t }$ be the hidden state, and $o _ { t }$ be the output at time t. Following is the recurrent equation to produce outputs from input sequences.

![](/api/attachments/BDXF4GS2/fulltext/images/4a313d8bc247319d18ab20e417cfeaa1e0333cec6540dfa824adda03b9711e8d.jpg)  
Figure 2: An architecture of Recurrent Neural Networks

$$
h _ {t} = g (U x _ {t} + W h _ {t - 1} + b _ {h}), o _ {t} = g (V h _ {t} + b _ {o})\tag{6}
$$

Long-Short-Term Memory Neural Network (LSTM NN) is a special kind of RNN which solves the gradient vanishing problem the conventional RNN models have. LSTM NN is composed of LSTM units which determine when to forget previous hidden states and when to update hidden states from new information. A typical architecture of the LSTM unit consists of a cell state and three gates, i.e., forget gate, input gate, and output gate. The cell state $( \mathrm { i . e . , } C _ { t } )$ allows the data to pass through the neuron without losing much information, while the gates regulate the flow of information inside the LSTM unit. Each gate is composed of a sigmoid function, $\sigma ,$ and a pointwise multiplication operation, ⊗. The forget gate $( \mathrm { i . e . , ~ } f _ { t } )$ decides whether to discard information from the cell state. The input gate(i.e., i<sub>t</sub>) allows adding new information to the cell state. The output gate $\left( \mathrm { i . e . , } o _ { t } \right)$ determines what the model will generate as an output. Let X, H, $Y$ be the input time series, the hidden state of memory cells, and the output time series, respectively. The hidden state of memory cells is calculated in the following formulas:

$$
\begin{array}{r l} & f _ {t} = \sigma (W _ {f} [ h _ {t - 1}, x _ {t} ] + b _ {f}), \\ & \tilde {C} _ {t} = t a n h (W _ {c} [ h _ {t - 1}, x _ {t} ] + b _ {c}), \\ & o _ {t} = \sigma (W _ {o} [ h _ {t - 1}, x _ {t} ] + b _ {o}), \end{array}
$$

$$
\begin{array}{l} {i _ {t} = \sigma (W _ {i} [ h _ {t - 1}, x _ {t} ] + b _ {i})} \\ {C _ {t} = \sigma (f _ {t} C _ {t - 1} + i _ {t} \tilde {C} _ {t})} \\ {h _ {t} = o _ {t} t a n h (C _ {t})} \end{array}\tag{7}
$$

where W , b indicates the weights and biases which are learned during the

training phase.

## 3.3.3. Long-term recurrent convolution network

Diferent from image recognition tasks, video processing requires a model to deal with variable-length input sequences, and generate variable length outputs as well. In this regard, Donahue et al. [24] proposed a novel neural network architecture called Long-term Recurrent Convolutional Networks (LRCNs). LRCN combines a deep hierarchical visual feature extractor (e.g., CNN) with a recurrent model (e.g., RNN) to recognize and learn temporal dynamics for tasks involving sequential data (e.g., video recognition).

An LRCN is composed of model input, feature extractor, sequence learning layer, and model output. Let $x _ { t }$ be a model input (i.e., an image or a frame from a video). The feature extractor $f _ { V } ( \cdot )$ with parameters V produce a fixed-length feature vector as follows:

$$
f v _ {t} = f _ {V} (x _ {t})\tag{8}
$$

A CNN is deployed for this purpose. The feature vector $f v _ { t }$ is then passed into a recurrent sequence learning layer. The recurrent model is LSTM NN with parameters U, W and $V$ $h _ { t }$ $o _ { t }$ $f v _ { t }$ and a previous time step hidden state $h _ { t - 1 }$ are used to produce output $o _ { t }$ as follows:

$$
h _ {t} = g (U x _ {t} + W h _ {t - 1} + b _ {h}), o _ {t} = g (V h _ {t} + b _ {o})\tag{9}
$$

Finally, a distribution $P ( y _ { t } )$ at time t is produced through a linear prediction layer:

$$
\hat {y} _ {t} = W _ {o} o _ {t} + b _ {o}\tag{10}
$$

where $W _ { o }$ and $b _ { o }$ are learned parameters.

## 4. Method

This section proposes a method to predict the future performances of a business process based on deep neural networks. A general overview is presented first, and then we explain each step in more detail.

## 4.1. Overview

Our method consists of three steps: 1) annotated process model construction, 2) process representation matrix generation, and 3) prediction model construction. Fig. 3 describes the overview of this method. As the first step, we produce a process model from an event log and annotate the derived model with measurements by replaying the log. In the process mining discipline, many process discovery algorithms have been proposed to produce better process models with diferent modeling notations. In this paper, we adopt a state transition system because of its ability to derive diverse forms of features (i.e., not only controlflow but also organizational/data perspective) for deep learning techniques by applying various abstraction techniques (see Section 3.2). For example, a state in a transition system can be an activity, a resource, or the combination of an activity and a resource, etc. It enables us to use diferent forms of process models according to the objectives.

In the second step, we generate a process representation matrix that contains information on the temporal performances in the business process, from the annotated process model. In this paper, we suggest two forms of the process representation matrix that eficiently represent the spatial dependence and temporal evolution of the business process.

Finally, we generate a training set from the process representation matrix and train the deep-learning-based prediction models to forecast the future performances of the business process based on the historical records of the performances. In this work, we utilize three deep learning architectures (i.e., CNN, LSTM, and LRCN ) to eficiently learn the spatial and temporal dependencies, which are embodied in the process representation matrix.

## 4.2. Annotated process model construction

The initial step of the proposed method is to produce a transition system that describes the behaviors seen in an event log. In the rest of the paper, we assume a transition system with a state representation function $l ^ { s } ( \sigma ) = \langle \pi _ { A } ( \sigma ( | \sigma | ) \rangle$ , which represents the partial trace by the sequence of events with horizon of 1, and an event representation function $l ^ { e } ( e ) = \pi _ { A } ( e )$ , which labels the transition with activities, in order to eficiently deliver the idea behind this research.

![](/api/attachments/BDXF4GS2/fulltext/images/10c5984ca48c64ae3a4f53e3d99092d62d53e21ab31de9e37be6fa7b2e7a7bf7.jpg)  
Figure 3: Overview of the proposed method

Next, we annotate the states and transitions of the transition system with measurements by replaying the event log to it. The following definition formalize how to calculate the measurements from the two partial traces $\sigma _ { 1 }$ and $\sigma _ { 2 }$ such that $\sigma _ { 1 }$ and $\sigma _ { 2 } ~ \mathrm { i s }$ prefix and the postfix of a trace $\sigma .$ . Each measurement is annotated to the corresponding state or transition in a transition system. Although numerous measurements are possible, we use waiting time, processing time, and sojourn time in this paper.

Definition 5 (Measurements). Let $\sigma _ { 1 }$ and $\sigma _ { 2 }$ be the prefix trace and postfix trace of given trace σ. A measurement function l<sup>m</sup> is a function that generates tuples of measurement and its relevant timestamp $( e . g . , \ ( 4 , 0 0 { : } 1 0 ) )$ . Formally, $l ^ { m } \in C \times C \to \mathbb { R } ^ { + } \times T$ . Let min ${ } _ { S T / C T } ( \sigma ) = m i n \{ \pi _ { S T / C T } ( e ) | e \in \sigma \}$ and $m a x _ { S T / C T } ( \sigma ) = m a x \{ \pi _ { S T / C T } ( e ) | e \in \sigma \}$ , where ST and CT stands for the start time and the complete time. $l _ { w a i t i n g } ^ { m } = ( m i n _ { S T } ( \sigma _ { 2 } ) - m a x _ { C T } ( \sigma _ { 1 } ) , m a x _ { C T } ( \sigma _ { 1 } ) ) \ v a r$ f $\sigma _ { 1 } \neq \langle \rangle$ and $\sigma _ { 2 } \neq \langle \rangle ; 0$ otherwise. $l _ { p r o c e s s i n g } ^ { m } = \left( m i n _ { C T } ( \sigma _ { 2 } ) - m i n _ { S T } ( \sigma _ { 2 } ) , m i n _ { S T } ( \sigma _ { 2 } ) \right)$ if $\sigma _ { 2 } \neq \langle \rangle _ { \mathrm { { : } } }$ ; 0 otherwise. $l _ { s o j o u r n } ^ { m } = \left( m i n _ { C T } ( \sigma _ { 2 } ) - m a x _ { C T } ( \sigma _ { 1 } ) , m a x _ { C T } ( \sigma _ { 1 } ) \right) \ i f$ $\sigma _ { 1 } \neq \langle \rangle$ and $\sigma _ { 2 } \neq \langle \rangle ; 0$ otherwise.

The measurements are annotated to the corresponding states and transitions in the transition system to generate the annotated transition system. Let the prefix of σ be $h d ^ { k } ( \sigma )$ and the postfix be $t l ^ { | \sigma | - k } ( \sigma )$ A measurement $l ^ { m } ( h d ^ { k } ( \sigma ) , t l ^ { | \sigma | - k } ( \sigma ) )$ is annotated to the state $l ^ { s } ( h d ^ { k + 1 } ( \sigma ) )$ $( l ^ { s } ( h d ^ { k } ( \sigma ) ) , l ^ { e } ( \sigma ( k + 1 ) ) , l ^ { s } ( h d ^ { k + 1 } ( \sigma ) ) )$ . The formal definition of the annotated transition system is as follows:

Definition 6 (Annotated transition system). Let L be an event log and $T S = ( S , E , T )$ a transition system based on a state representation function l<sup>s</sup> and event representation function l<sup>e</sup>. Given a particular measurement function $l ^ { m }$ , we define a state annotation function $A _ { s } \in S \to B ( M )$ such that $A _ { s } ( s ) =$ $\begin{array} { r } { \sum _ { \sigma \in L } \sum _ { 1 \leq k \leq | \sigma | - 1 , s = l ^ { s } ( h d ^ { k + 1 } ( \sigma ) ) \in S } [ l ^ { m } ( h d ^ { k } ( \sigma ) , t l ^ { | \sigma | - k } ( \sigma ) ) ] } \end{array}$ . In other words, $A _ { s } ( s )$ is a multi-set composed of measurements corresponding to the state s. In addition, we define a transition annotation $A _ { t } \in T \to B ( M )$ such that $A _ { t } ( t ) =$ $\begin{array} { r } { \sum _ { \sigma \in L } \sum _ { 1 \leq k \leq | \sigma | - 1 , t = ( l ^ { s } ( h d ^ { k } ( \sigma ) ) , l ^ { \epsilon } ( \sigma ( k + 1 ) ) , l ^ { s } ( h d ^ { k + 1 } ( \sigma ) ) ) \in T } [ l ^ { m } ( h d ^ { k } ( \sigma ) , t l ^ { | \sigma | - k } ( \sigma ) ) ] } \end{array}$ . In other words, $A _ { t } ( t )$ is a multi-set composed of measurements corresponding to the transition t. An annotated transition system is the tuple $( S , E , T , A _ { s } , A _ { t } )$

## 4.3. Process representation generation

In this step, we build a process representation matrix from an annotated transition system. To this end, we first define temporal aggregation functions that will be used to calculate a temporary performance measure from measurements in an annotated transition system. Using the temporal aggregation function, we derive two diferent types of process representation matrix that will be used to produce a training set (i.e., predictor and response variables) for prediction models in the next step.

In order to evaluate the evolution of the performances in the underlying business process, we need the time window upon which we calculate the temporal performance. If we want to measure the hourly evolution of performances in the business process, we need the time windows of an hour, e.g., [Oct. 5 00:00, Oct. 5 01:00], [Oct. 5 01:00, Oct. 5 02:00], and so on. The definition of the time window is as follows:

Definition 7 (Time window). Given a time point t, a time period p, the $\mathit { l } _  t , $ $t + p ]$ will form a single block. Given a time stride s, the next block slides with $T W _ { p , s }$ is a set of all blocks formed by p and s within T .

After producing a set of time windows, we need to calculate the temporal performance measures of the states and transitions associated with each time window. To this end, we use temporal aggregation function (e.g., average).

Definition 8 (Temporal aggregation function and performance measure). Let tw ∈ T W be a time window and M be a multi-set of measurements. A temporal aggregation function, $a g g _ { t w } ( M )$ is a function that generates a numerical value by aggregating measurements M at tw. Formally, $a g g _ { t w } \in M \to \mathbb { R }$ such that M is multi-set of measurements. $p _ { a g g } ^ { M , t w }$ is the temporal performance measure resulting from the temporal aggregation function $a g g _ { t w }$

This paper proposes two forms of process representation matrix to embed the evolution of performance in business processes eficiently. First, the two-dimensional process presentation matrix expresses the evolutionary performances of a business process in the two-dimensional matrix. Using the process model entities (i.e., state and transition) and the time windows as the first and second dimensions, we eficiently represent the spatial dependence and the temporal evolution.

Definition 9 (two-dimensional process representation matrix). Let tw ∈ T W be a time window and $o \in \{ s t a t e , t r a n s i t i o n \}$ be the state and transition in the annotated transition system. Then, a matrix $R ^ { 2 d i m , o } \ \in \ \mathbb { R } ^ { | O | \times | T W | }$ is called 2-dimensional representation matrix with $\boldsymbol { r } _ { i , j }$ indicating the performance measure of $o _ { i }$ at $t w _ { j }$ , i.e., $a g g _ { t w _ { j } } \big ( A _ { o } \big ( o _ { i } \big ) \big )$ ), where $A _ { o } \in \{ A _ { s } , A _ { t } \}$ is the state $o r$ transition annotation function.

Second, a three-dimensional process representation matrix eficiently embodies the spatial dependency in the first two dimensions and the temporal evolution in the third dimension. The first two dimensions represent the network topology (i.e., directly-follows relations) and indicate the outgoing state (i.e., from-state) and the incoming state (i.e., to-state). The third dimension is the time window.

Definition 10 (three-dimensional process representation matrix). Let tw $\in T W$ be a time window and $s \in S$ be the state in the annotated transition system. Let $t r ( s _ { 1 } , s _ { 2 } )$ be a function to produce the transition connecting $s _ { 1 }$ and $s _ { 2 }$ in the annotated transition system. $T h e n , \textit { a }$ matrix $R ^ { 3 d i m } \in \mathbb { R } ^ { | S | \times | S | \times | T W | }$ is called three-dimensional process representation matrix with $r _ { i , j , k }$ representing the performance measure of transition $t = t r ( s _ { i } , s _ { j } ) \in T$ at tw, i.e., $a g g _ { t w } ( A _ { t } ( t ) )$ such that $A _ { t }$ is the transition annotation in the annotated transition system.

## 4.4. Prediction model construction

In this step, we aim at learning a performance prediction function which returns future performance measures of the states and transitions in the business process, given the historical performance measures of them. In order to consider both spatial and temporal dependencies underlying the business process, we deploy three deep neural networks that show the competency in learning spatiotemporal correlations in the trafic network, i.e., CNN [11], LSTM [10], and LRCN [12]. In the following, we will explain each of three prediction models, i.e., CNN-based model, LSTM-based model, and LRCN-based model. Fig. 4 shows the architecture of each prediction model. Although the proposed models have diferent input and model architecture, the procedure to construct them is composed of the same two phases, i.e., 1) training set generation and 2) model learning.

![](/api/attachments/BDXF4GS2/fulltext/images/7a1063d3060dbe8c82bb9fe2650a60d5cb0d57bfd026020d5dd1097e1ca0a991.jpg)  
Figure 4: Architectures of prediction models

## 4.4.1. CNN-based prediction model

A CNN has the competency to extract essential features from the input imwhere channels commonly represent the RGB values. In order to exploit its competency, we generate image-like input, $x \in \mathbb { R } ^ { }$ sentation matrix $R ^ { 2 d i m , o }$ by setting the number of channels as one. Let $P$ be the length of input time windows. The model input can be written as:

$$
x ^ {\prime j} = [ r _ {j}, r _ {j + 1},, r _ {j + P - 1} ], j \in [ 1, | T W | - P ],\tag{11}
$$

where $r _ { j }$ is a column vector representing performance measures at $t w _ { j }$ , i.e., $R _ { \cdot , j } ^ { 2 d i m , o }$ . By adding a channel of 1, we transform $\boldsymbol { x } ^ { \prime } { } ^ { j } \in \mathbb { R } ^ { | O | \times | T W | }$ to an imagelike $x ^ { j } \in \mathbb { R } ^ { | O | \times | T W | \times 1 } .$ The model output can be written as:

$$
y ^ {j} = [ r _ {j + P} ], j \in [ 1, | T W | - P ]\tag{12}
$$

where $r _ { j + P }$ is a column vector representing performance measures at $t w _ { j + P }$ $R _ { \cdot , j + P } ^ { 2 d i m , o }$

Afterward, we train a CNN-based prediction model that extracts spatiotemporal features embedded in the model input, where the first and second dimensions represent the temporal and spatial information, respectively. Fig. 4-(a) shows the architecture of the proposed CNN model. The model input $x ^ { j }$ is passed to a feature transformation $f _ { V } ( . )$ that consists of the combination of convolution and pooling layers. Through the transformation, the model learns the spatiotemporal features of the business process. The extracted features $f _ { V } ( x ^ { j } )$ from diferent filters are concatenated to a dense vector by flattening, and then they are passed into a fully connected layer to be transformed to the model output $\hat { y } ^ { j }$ .

We train all sets of network weights using RMSProp algorithm [25] such that the mean absolute error (MAE) between the predicted value $\hat { y }$ and the actual value y is minimized. We use convolutional filters of size $( 3 , 3 )$ and max poolings of size (3, 3). Convoultional layers consecutively transform the number of channels into 32 and 16 with the corresponding number of convolutional filters. As regularization strategies, we use Dropout [26] and Batch Normalization [27].

## 4.4.2. LSTM-based prediction model

Long-Short Term Memory Neural Networks (LSTM) has the competency to learn long temporal dependency for the input sequence. The strength to learn the temporal dependency is suitable for predicting the future performances of the business process based on historical performances. Furthermore, by producing a sequence of vectors as model input where each vector represents the snapshot of performances on all locations in the business process model, we can construct the prediction model to reflect both the spatial and temporal information efectively. To this end, we first generate a training set from the two-dimensional process representation matrix $R ^ { 2 d i m , o }$ using equation (11) and (12) in Section 4.4.1.

Afterward, we train an LSTM-based prediction model from the training set. Fig. 4-(b) shows the unrolled structure of the proposed LSTM-based prediction model. Note that the number of steps LSTM unrolled is P that is the length of input time windows. The model is composed of two hidden LSTM layers, where each layer contains multiple memory cells. Each layer contains LSTM cells as much as the number of column vectors in $x ^ { j }$ . The model is trained in a recurrent manner. In other words, LSTM cell $f _ { W _ { 1 } } ^ { 1 } ( . )$ with parameters $W$ takes as input not only the element $x ^ { j , t }$ in the model input $x ^ { j }$ , but also the hidden state $h _ { 1 } ^ { j , t - 1 }$ generated from the previous LSTM cell. The output $o _ { 1 } ^ { j , t }$ of the

LSTM cell in the first layer is passed to the next LSTM $f _ { W _ { 2 } } ^ { 2 } ( . )$ layer as an input. The output $o _ { 2 } ^ { j , t }$ of the last LSTM cell in the second layer becomes an input to a fully connected layer $f _ { L } ( . )$ , which then produces the prediction results $\hat { y } ^ { j }$ .

We train all sets of network weights using RMSProp algorithm [25] such that MAE between the predicted value ˆy and the actual value y is minimized. The number of hidden states in the first layer is twice as large as the input dimension, and the number of hidden states in the second layer is four times larger than the input dimension. As regularization strategies, we use Dropout [26] and Batch Normalization [27].

## 4.4.3. LRCN-based prediction model

It is paramount to reflect the process model topology to build an accurate prediction model. To this end, we produce a model input based on the threedimensional process representation matrix $R ^ { 3 d i m }$ , which involves the directlyfollows relations. The model input can be written as:

$$
x ^ {j} = [ i m g _ {j}, i m g _ {j + 1},, i m g _ {j + P - 1} ], j \in [ 1, | T W | - P ]\tag{13}
$$

, where $i m g _ { j }$ is an image generated from $R _ { \cdot , \cdot , j } ^ { 3 d i m }$ (i.e., the performance at j<sub>th</sub> time window) by setting the channel as one just as we did in Section 4.4.1.

The model output can be written as:

$$
y ^ {j} = [ i m g _ {j + P} ], j \in [ 1, | T W | - P ]\tag{14}
$$

, where $i m g _ { j + P }$ is an image generated from $R _ { \cdot , \cdot , j + P } ^ { 3 d i m } \ ( \mathrm { i . e . }$ ., the performance $j + P _ { t h }$ time window) by setting the channel as one.

We can understand the prediction task as the video recognition problem where the previous sequence of frames (i.e., images) is used to predict the future frame. An LRCN, a class of neural network architectures for video recognition, combines a visual feature extractor (i.e., CNN) and a recurrent model $( \mathrm { i . e . , }$ LSTM) which recognize the temporal dynamics of the sequential images. Fig. 4-(c) shows the architecture of our LRCN-based prediction model. We start by passing each element $x ^ { j , t }$ in $x ^ { j }$ through a CNN, $f _ { V }$ , with parameters V to produce a feature vector $f v ^ { j , t }$ . The resulting feature vector $f v ^ { j , t } = f _ { V } ( x ^ { j , t } )$ is then passed into a LSTM layer. The LSTM layer $f _ { W }$ works in recurrent manner by taking both feature vector $f v ^ { j , t }$ and previous hidden state $h _ { 1 } ^ { j , t - 1 }$ as an input. For example, $h _ { 1 } = f _ { W _ { 1 } } ( f v ^ { j , 1 } , h _ { 1 } ^ { j , 0 } ) = f _ { W _ { 1 } } ( f v ^ { j , 1 } , 0 ) , \ h _ { 2 } = f _ { W _ { 1 } } ( f v ^ { j , 2 } , h _ { 1 } ^ { j , 1 } ) =$ $f _ { W _ { 1 } } ( f v ^ { j , 2 } , f _ { W _ { 1 } } ( f v ^ { j , 1 } , 0 ) )$ , etc. We stack another LSTM layer as we do for the LSTM-based model. The output of the second LSTM layer $o _ { 2 } ^ { j , P }$ is passed through $\hat { y } ^ { j }$

Since this model is the combination of CNN-based model and LSTM-based model, we follow the same procedure as the previous two approaches to train the model.

## 5. Evaluation

In order to evaluate the applicability of the proposed method to predict the future performances of a business process, we conduct three case studies with real-life logs: healthcare service, BPI Challenge 2012 (BPIC’12) <sup>1</sup>, and helpdesk <sup>2</sup>. When applying the proposed method, we initialized all network weights using a uniform random distribution over [0.1, 0.1]. The models were trained with a batch size of 16 with 100 epochs and a learning rate of 0.001. The learning rate decreased by a factor of 0.1 when a metric has stopped improving. The training was stopped if the loss stops decreasing for five epochs. In the case studies, we compare the proposed method with the two baseline approaches, i.e., statistical approach and search-based approach.

Statistical approach. Existing studies [13] enrich each state with a prediction model to conduct a prediction task. Based on these works, we design an approach that builds an individual prediction model for each state and transition in the transition system. Through the prediction model, we can predict the future performance of individual state and transition based on its historical performances. The statistical algorithms we utilize for this purpose are linear regression (LR), random forest (RF), and support vector machine (SVR).

Search-based approach. The performance of a business process is likely to be repeated with some periodicity. In this regard, one intuitive method to predict future performance in the business process is first to find the most similar past status with the current status and then suggest its next performance record as a prediction. To this end, we take a snapshot for each time window in the form of a one-dimensional vector whose elements indicate the performances of states from the transition system. Next, we calculate the distance between the historical snapshots and the current one. Afterward, we find the prior snapshot having the shortest distance and provide its next snapshot as a prediction. The distance metrics we utilize in this approach are Euclidean Distance (Euc.), Chebyshev Distance (Che.), and Cosine Distance (Cos.).

Note that the proposed method and two baseline approaches are implemented in Python3.6.8, and the source code and supplementary materials required to reproduce the experiments can be found at the Github repository <sup>3</sup>.

In each case study, the experiments were performed with 5-fold cross-validation. To measure and compare the prediction accuracy, we used two metrics: Mean Absolute Error (MAE) and Mean Absolute Percentage Error (MAPE). Let $y _ { i , t }$ and $\hat { y } _ { i , t }$ denote the actual and predicted performance at time t at object $( \mathrm { i . e . , }$ state or transition) i.

## 5.1. Case study I: healthcare service process

The real-life log used in this case study is from an emergency department in a tertiary hospital in South Korea. It contains event records of the treatment process in the emergency department, collected from January 2018 to December 2018. The log is comprised of 459,700 events by 29,871 patients who visit the emergency department. Each patient goes through 15 activities on average until they leave. The average time for each patient to stay in the department is approximately 8.5 hours. The unique number of activities conducted in the process is 19. In total, 754 resources serve the activities in a shift system.

In this case study, we aim at evaluating the applicability of our proposed method in diferent settings. To this end, we define four purposeful tasks by discussing with domain experts, each of which represents if the task is short-term or long-term and with enough information or limited information. We consider the next hour prediction as a short-term prediction and the next three-hour prediction as a long-term prediction. Also, the available performance records for 12 times and 24 times of the prediction length are regarded as limited and enough information, respectively. Let tasks be specified with the (time interval of output, time interval of input). The four tasks are as follows:

• Task 1 with (1,24) : 1 hour prediction using past 24 hours, i.e., short-term prediction with enough information

• Task 2 with (1,12): 1 hour prediction using past 12 hours, i.e., short-term prediction with limited information

• Task 3 with (3,72): 3 hour prediction using past 72 hours, i.e., long-term prediction with enough information

• Task 4 with (3,36): 3 hour prediction using past 36 hours, i.e., long-term prediction with limited information

For each task, we predict the average sojourn time for states and transitions in the business process model. The experiments were performed using an entire log with 5-fold cross-validation.

Table 1 shows mean absolute error (MAE) and mean absolute percentage error (MAPE) of predicting average sojourn time for states and transitions. Our deep-learning approach generally works better than both the statistical approach and the search-based approach both in the short-term (i.e., Task 1 and Task 2) and the long-term (i.e., Task 3 and Task 4) prediction. The bold font indicates the best result in a specific task. Our proposed CNN-based model and LRCN-based model show the most accurate predictions in all tasks. In particular, LRCN-based model demonstrates the stable results for all tasks. It attributes to its ability to learn network topology present in the three-dimensional process representation matrix. However, our deep learning approach does not outperform in all tasks. In the short-term prediction (i.e., Task 1 and Task2), the LSTM-based model fails to properly learn the spatiotemporal dependencies underlying the business process when enough information is not given, showing inferior results than baseline approaches. Also, in long-term transition prediction tasks (i.e., transition prediction in Task 3 and Task 4), the CNN-based model and LSTM-based model show inferior results compared to the statistical

Table 1: MAE (hours) and MAPE of predicting average sojourn time for states and transitions in healthcare service process using 5-fold cross validation (ST: statistical approach, SB: searchbased approach, DL: deep-learning approach)

<table><tr><td rowspan="3" colspan="2"></td><td colspan="4">Task 1</td><td colspan="4">Task 2</td></tr><tr><td colspan="2">State</td><td colspan="2">Transition</td><td colspan="2">State</td><td colspan="2">Transition</td></tr><tr><td>MAE</td><td>MAPE</td><td>MAE</td><td>MAPE</td><td>MAE</td><td>MAPE</td><td>MAE</td><td>MAPE</td></tr><tr><td rowspan="3">ST</td><td>LR</td><td>0.42 ± 0.01</td><td>0.15 ± 0.01</td><td>0.15 ± 0.01</td><td>0.06 ± 0.01</td><td>0.41 ± 0.01</td><td>0.14 ± 0.01</td><td>0.15 ± 0.01</td><td>0.06 ± 0.01</td></tr><tr><td>RF</td><td>0.42 ± 0.01</td><td>0.14 ± 0.01</td><td>0.15 ± 0.01</td><td>0.06 ± 0.01</td><td>0.41 ± 0.02</td><td>0.13 ± 0.01</td><td>0.15 ± 0.01</td><td>0.06 ± 0.01</td></tr><tr><td>SVR</td><td>0.36 ± 0.02</td><td>0.14 ± 0.01</td><td>0.24 ± 0.01</td><td>0.05 ± 0.01</td><td>0.35 ± 0.01</td><td>0.13 ± 0.01</td><td>0.24 ± 0.01</td><td>0.06 ± 0.01</td></tr><tr><td rowspan="3">SB</td><td>Euc.</td><td>0.42 ± 0.02</td><td>0.14 ± 0.01</td><td>0.13 ± 0.01</td><td>0.07 ± 0.01</td><td>0.42 ± 0.02</td><td>0.14 ± 0.01</td><td>0.13 ± 0.01</td><td>0.06 ± 0.01</td></tr><tr><td>Che.</td><td>0.41 ± 0.01</td><td>0.15 ± 0.01</td><td>0.14 ± 0.01</td><td>0.08 ± 0.01</td><td>0.41 ± 0.01</td><td>0.15 ± 0.01</td><td>0.14 ± 0.01</td><td>0.07 ± 0.01</td></tr><tr><td>Cos.</td><td>0.40 ± 0.05</td><td>0.14 ± 0.05</td><td>0.11 ± 0.01</td><td>0.07 ± 0.05</td><td>0.40 ± 0.05</td><td>0.14 ± 0.05</td><td>0.11 ± 0.01</td><td>0.07 ± 0.05</td></tr><tr><td rowspan="3">DL</td><td>CNN</td><td>0.30 ± 0.02</td><td>0.13 ± 0.01</td><td>0.10 ± 0.01</td><td>0.05 ± 0.03</td><td>0.25 ± 0.01</td><td>0.11 ± 0.02</td><td>0.09 ± 0.01</td><td>0.05 ± 0.01</td></tr><tr><td>LSTM</td><td>0.33 ± 0.11</td><td>0.16 ± 0.02</td><td>0.11 ± 0.02</td><td>0.05 ± 0.01</td><td>0.40 ± 0.05</td><td>0.21 ± 0.05</td><td>0.13 ± 0.05</td><td>0.08 ± 0.02</td></tr><tr><td>LRCN</td><td>0.26 ± 0.02</td><td>0.13 ± 0.01</td><td>0.08 ± 0.01</td><td>0.04 ± 0.01</td><td>0.26 ± 0.01</td><td>0.12 ± 0.01</td><td>0.08 ± 0.01</td><td>0.05 ± 0.01</td></tr></table>

<table><tr><td rowspan="3" colspan="2"></td><td colspan="4">Task 3</td><td colspan="4">Task 4</td></tr><tr><td colspan="2">State</td><td colspan="2">Transition</td><td colspan="2">State</td><td colspan="2">Transition</td></tr><tr><td>MAE</td><td>MAPE</td><td>MAE</td><td>MAPE</td><td>MAE</td><td>MAPE</td><td>MAE</td><td>MAPE</td></tr><tr><td rowspan="3">ST</td><td>LR</td><td> $0.51 \pm 0.01$ </td><td> $0.16 \pm 0.01$ </td><td> $0.34 \pm 0.01$ </td><td> $0.12 \pm 0.01$ </td><td> $0.52 \pm 0.02$ </td><td> $0.16 \pm 0.01$ </td><td> $0.34 \pm 0.01$ </td><td> $0.18 \pm 0.12$ </td></tr><tr><td>RF</td><td> $0.50 \pm 0.01$ </td><td> $0.15 \pm 0.01$ </td><td> $0.32 \pm 0.01$ </td><td> $0.11 \pm 0.01$ </td><td> $0.52 \pm 0.02$ </td><td> $0.15 \pm 0.01$ </td><td> $0.32 \pm 0.01$ </td><td> $0.11 \pm 0.01$ </td></tr><tr><td>SVR</td><td> $0.46 \pm 0.02$ </td><td> $0.15 \pm 0.01$ </td><td> $0.37 \pm 0.01$ </td><td> $0.10 \pm 0.01$ </td><td> $0.47 \pm 0.02$ </td><td> $0.15 \pm 0.01$ </td><td> $0.37 \pm 0.01$ </td><td> $0.10 \pm 0.01$ </td></tr><tr><td rowspan="3">SB</td><td>Euc.</td><td> $0.42 \pm 0.02$ </td><td> $0.17 \pm 0.01$ </td><td> $0.45 \pm 0.02$ </td><td> $0.11 \pm 0.01$ </td><td> $0.42 \pm 0.02$ </td><td> $0.16 \pm 0.01$ </td><td> $0.45 \pm 0.02$ </td><td> $0.11 \pm 0.01$ </td></tr><tr><td>Che.</td><td> $0.41 \pm 0.01$ </td><td> $0.17 \pm 0.01$ </td><td> $0.46 \pm 0.01$ </td><td> $0.11 \pm 0.01$ </td><td> $0.41 \pm 0.01$ </td><td> $0.17 \pm 0.01$ </td><td> $0.46 \pm 0.01$ </td><td> $0.12 \pm 0.01$ </td></tr><tr><td>Cos.</td><td> $0.40 \pm 0.05$ </td><td> $0.18 \pm 0.05$ </td><td> $0.38 \pm 0.01$ </td><td> $0.13 \pm 0.04$ </td><td> $0.40 \pm 0.05$ </td><td> $0.17 \pm 0.05$ </td><td> $0.38 \pm 0.01$ </td><td> $0.17 \pm 0.04$ </td></tr><tr><td rowspan="3">DL</td><td>CNN</td><td> $0.32 \pm 0.05$ </td><td> $0.15 \pm 0.01$ </td><td> $0.32 \pm 0.02$ </td><td> $0.10 \pm 0.01$ </td><td> $0.28 \pm 0.02$ </td><td> $0.12 \pm 0.02$ </td><td> $0.32 \pm 0.01$ </td><td> $0.10 \pm 0.01$ </td></tr><tr><td>LSTM</td><td> $0.31 \pm 0.06$ </td><td> $0.16 \pm 0.02$ </td><td> $0.34 \pm 0.03$ </td><td> $0.11 \pm 0.01$ </td><td> $0.29 \pm 0.02$ </td><td> $0.13 \pm 0.01$ </td><td> $0.33 \pm 0.03$ </td><td> $0.11 \pm 0.01$ </td></tr><tr><td>LRCN</td><td> $0.29 \pm 0.01$ </td><td> $0.13 \pm 0.01$ </td><td> $0.16 \pm 0.01$ </td><td> $0.08 \pm 0.01$ </td><td> $0.29 \pm 0.02$ </td><td> $0.13 \pm 0.01$ </td><td> $0.17 \pm 0.01$ </td><td> $0.09 \pm 0.01$ </td></tr></table>

approach.

## 5.2. Case study II: BPIC’12

In this case study, we use a real-life log of the application procedure for a personal loan or overdraft at a global financing organization over the six months from October 2011 to March 2012. Approximately 262,200 events regarding 13,087 cases are recorded for the period. This log contains three types of process: one that refers to the states of the application, one that refers to the states of an ofer, and one that tracks the states of work items that occur during the approval process. Since we are only interested in the events performed manually, we only investigate the third type.

Using this log, we aim at predicting the average processing time for states and transitions in the next 6 hours, given the historical performance of the last 144 hours. The experiment was performed using 5-fold cross-validation. Table 2 shows the mean absolute error (MAE) and mean absolute percentage error (MAPE) of predicting average processing time for states and transitions. Our proposed deep-learning-based models perform well both in state and transition predictions. In particular, the CNN-based and the LRCN-based prediction models outperform the two baseline approaches both in the state and transition predictions. It verifies that the competency of CNN in extracting critical features is crucial to produce accurate predictions. However, the LSTM-based model shows inferior prediction accuracy in terms of MAPE, compared to LR and RF, failing to learn the temporal dynamics.

## 5.3. Case study III: Helpdesk

The third case study log concerns a ticketing management system designed for the help desk of an Italian software company. The process starts with the insertion of a new ticket into the ticketing management system. The ticket is managed by resources, and the process ends when the problem is resolved. In this case study, we use 8,988 events by 2,542 cases from January 2011 to June 2012.

Table 2: MAE (hours) and MAPE of predicting average processing time for states and transitions in BPIC’12 using 5-fold cross validation

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">State</td><td colspan="2">Transition</td></tr><tr><td>MAE</td><td>MAPE</td><td>MAE</td><td>MAPE</td></tr><tr><td rowspan="3">Statistical Approach</td><td>LR</td><td>1.03 ± 0.18</td><td>1.20 ± 0.38</td><td>0.45 ± 0.06</td><td>0.75 ± 0.02</td></tr><tr><td>RF</td><td>0.86 ± 0.22</td><td>0.70 ± 0.01</td><td>0.39 ± 0.06</td><td>0.65 ± 0.01</td></tr><tr><td>SVR</td><td>0.53 ± 0.09</td><td>0.59 ± 0.01</td><td>0.30 ± 0.03</td><td>0.63 ± 0.01</td></tr><tr><td rowspan="3">Search-based approach</td><td>Euc.</td><td>0.69 ± 0.12</td><td>0.77 ± 0.05</td><td>0.30 ± 0.07</td><td>0.79 ± 0.04</td></tr><tr><td>Che.</td><td>0.67 ± 0.12</td><td>0.78 ± 0.05</td><td>0.29 ± 0.06</td><td>0.79 ± 0.05</td></tr><tr><td>Cos.</td><td>0.45 ± 0.10</td><td>0.93 ± 0.15</td><td>0.20 ± 0.05</td><td>0.93 ± 0.14</td></tr><tr><td rowspan="3">Deep Learning approach</td><td>CNN</td><td>0.44 ± 0.10</td><td>0.55 ± 0.02</td><td>0.19 ± 0.03</td><td>0.65 ± 0.10</td></tr><tr><td>LSTM</td><td>0.45 ± 0.10</td><td>0.87 ± 0.45</td><td>0.21 ± 0.03</td><td>0.90 ± 0.18</td></tr><tr><td>LRCN</td><td>0.44 ± 0.09</td><td>0.51 ± 0.04</td><td>0.19 ± 0.03</td><td>0.61 ± 0.03</td></tr></table>

We predict the average sojourn time for states and transitions in the next five days using the historical performances of the last 30 days. As in the previous case study, the experiments were performed using 5-fold cross-validation. Table 3 shows the mean absolute error (MAE) and mean absolute percentage error (MAPE) of predicting average sojourn time for states and transitions. Our proposed deep-learning-based models perform well both in the state prediction and transition prediction in terms of MAE and MAPE. For state prediction, the LSTM-based model and the CNN-based model achieve outstanding performances in terms of MAE and MAPE, respectively. On the other hand, the search-based approach using the Euclidean metric outperforms other approaches in transition predictions.

## 5.4. Further experiments

In the case studies, we use a transition system with a state representation function $l ^ { s } ( \sigma ) = \langle \pi _ { A } ( \sigma ( | \sigma | ) \rangle$ that represents the partial trace by the sequence of events with the prefix length (i.e., horizon) of 1 and an event representation function $l ^ { e } ( e ) = \pi _ { A } ( e )$ . We performed the experiments to investigate the efect of the diferent horizons to the prediction accuracy and computation time. As the size of the horizon increases, the transition system has more states and transitions. It enables prediction models to reflect more features when training.

Table 3: MAE (days) and MAPE of predicting average sojourn time for states and transitions in Helpdesk using 5-fold cross validation

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">State</td><td colspan="2">Transition</td></tr><tr><td>MAE</td><td>MAPE</td><td>MAE</td><td>MAPE</td></tr><tr><td rowspan="3">Statistical Approach</td><td>LR</td><td>2.62 ± 0.16</td><td>0.64 ± 0.02</td><td>1.63 ± 0.05</td><td>0.85 ± 0.01</td></tr><tr><td>RF</td><td>2.64 ± 0.17</td><td>0.63 ± 0.03</td><td>1.62 ± 0.06</td><td>0.84 ± 0.01</td></tr><tr><td>SVR</td><td>2.24 ± 0.17</td><td>0.68 ± 0.02</td><td>1.31 ± 0.05</td><td>0.88 ± 0.01</td></tr><tr><td rowspan="3">Search-based approach</td><td>Euc.</td><td>2.58 ± 0.32</td><td>0.63 ± 0.02</td><td>1.00 ± 0.06</td><td>0.59 ± 0.02</td></tr><tr><td>Che.</td><td>2.68 ± 0.27</td><td>0.63 ± 0.03</td><td>0.99 ± 0.06</td><td>0.60 ± 0.02</td></tr><tr><td>Cos.</td><td>2.49 ± 0.15</td><td>0.63 ± 0.01</td><td>1.03 ± 0.06</td><td>0.58 ± 0.03</td></tr><tr><td rowspan="3">Deep Learning approach</td><td>CNN</td><td>2.00 ± 0.21</td><td>0.83 ± 0.16</td><td>0.79 ± 0.05</td><td>0.63 ± 0.03</td></tr><tr><td>LSTM</td><td>1.85 ± 0.18</td><td>0.75 ± 0.11</td><td>0.72 ± 0.05</td><td>0.58 ± 0.01</td></tr><tr><td>LRCN</td><td>1.71 ± 0.11</td><td>0.61 ± 0.02</td><td>0.75 ± 0.05</td><td>0.58 ± 0.05</td></tr></table>

The detailed experiment results are found in the Github repository <sup>4</sup>. The experiment results show that the Case Study II using the BPIC’12 event log is afected by the increase of horizon, while there is almost no efect in the first and third case studies. Fig. 5-(a) shows the efects of the diferent horizons in the Case Study II. Note that the most accurate models of each approach (i.e., SVR, Cos., and LRCN ) are selected. The LRCN model shows the most improved prediction accuracy as the horizon expands. On the other hand, the extended feature exposes the prediction models to be vulnerable to overfitting. Besides, as depicted in Fig. 5-(b), it needs more computation time for training and prediction when the horizon increases.

## 6. Discussion

The three case studies on three real-life logs suggest that our proposed methods based on deep neural networks outperform the two baseline approaches by successfully learning the temporal evolution and the spatial dependency underlying the business process. The first case study also shows that our proposed method applies to any prediction tasks regardless of the prediction length (i.e., short-term or long-term) and the availability of data (i.e., enough or limited information). Among the deep learning approach, the LRCN-based model shows stable performances on all prediction tasks by learning network topology (i.e., directly-follows relations) that is provided by the three-dimensional process representation matrix.

![](/api/attachments/BDXF4GS2/fulltext/images/310dc311e593c447893ee029f549a8a624cc3a30f24b0c3637fab9fc98306b13.jpg)  
(a) Effect of horizon to MAE

![](/api/attachments/BDXF4GS2/fulltext/images/7f7059056805c42d280a7fd1a151c857ba348f69f8a21bf200da89e4cb881a5a.jpg)  
(b) Effect of horizon to computation time  
Figure 5: Efects of varying horizon to the prediction accuracy and computation time: experiments on the same setting as in Case Study II

Existing works on predictive business process monitoring aims at providing timely information that enables proactive and corrective actions to improve the at the process model level, but at the instance level, failing to provide useful knowledge of future problematic points in the business process. In this regard, the proposed method bridges the gap between the process performance mining and the predictive business process monitoring to provide practical information which will facilitate proactive actions to improve the business process.

The proposed approach has some limitations. Firstly, this work does not assess what extent managers can rely on prediction results to make operational management decisions. There are two possible directions to deal with this limitation. The first one is to calculate the required level of prediction accuracy by conducting sensitivity analysis concerning the efect of prediction accuracy in managerial decisions. For example, Park and Song provide the required level of prediction accuracy to execute the prediction-based resource allocation in business processes [28]. In the experiment on a real-life business process, the sensitivity analysis demonstrates that the suggested resource allocation technique is applicable if the prediction accuracy is above 60 percent. The other way to deal with this limitation is to develop prediction models to quantify the prediction uncertainty, such as Bayesian Neural Networks (BNNs), which is a promising direction for future works.

Second, the proposed approach assumes that past behaviors in a business process can be used to predict future behaviors. However, this assumption is invalid if there are some changes in the business environment. The changes afect business processes and lead to concept drift in prediction models. Concept drift means that the relation between the feature and the target variable changes due to the external factors that causes a decrease of the prediction accuracy over time. In this case, the predictive models should be adapted in an online manner, i.e., the models should be updated if the prediction accuracy is below a certain threshold.

Thirdly, we only utilize historical performances as the only input for training the prediction models. In other words, we predict the average waiting time for transitions based on the historical records of average waiting time in the business process. However, these one-to-one matches between the model input and the model output ignore other possible inuencing factors such as other related performance measures, the context of cases, and the availability of resources.

Fourth, our intention to make the method as general as possible leads to several parameters for the practitioners to determine before implementing the proposed method. First of all, constructing a transition system from an event log requires to specify the abstractions to represent the business process better. Second, one needs to define the time window $T W _ { p , s }$ by setting the period p and the stride s. Since both of them are numerical values, the possible options for the time window are infinite. Besides, the length of the model input P should

be presented before training the model.

Finally, since it is computationally expensive to learn deep neural networks, it took more time to implement our deep learning approach than two baseline approaches. The use of nonlinear activation functions in the neural network makes the optimization problem non-convex. Since the non-convex optimization problem contains many local optima, flat spots, and clifs, it is challenging to find an optimal solution to this problem. To deal with this problem, the optimizer in deep neural network repeats the steps of evaluating the model and updating the model parameters to step down the error surface. This search process, which is called gradient optimization, is known to be slow.

## 7. Conclusion

This paper has proposed a novel method for predicting the future performances of a business process on the process model level. The proposed method incorporates the process discovery technique in process mining and the congestion prediction technique in trafic network research. It is composed of three steps where the first step discovers the business process model we aim at analyzing, the second step represents the performance in the business process model as a matrix upon which we can construct prediction models, and the third step builds prediction models to predict the future performances of the business process.

The proposed method has been validated using three real-life event logs from diferent domains. All three experiments show that our proposed approach successfully predicts the performances at the process model level. It suggests that our proposed method is applicable to various domains with its competency to learn spatiotemporal dependency and reflect the network topology.

Our work has important implications for both research and practice. From an academic research standpoint, the proposed method provides a novel method to predict the performance of business processes at the process model level. As such, it shifts the focus of predictive process monitoring from the instance level to the process model level. Existing works in predictive process monitoring provide predictions at the instance level. This information requires proactive actions for the singular instances, which is infeasible to managers of complex business processes. Instead, the information acquired by predictions at the process model level is more actionable in that it enables managers to identify weaknesses in the process and apply remedial actions to improve them.

Moreover, this research links the realms of trafic research and the business process management based on the analogy of trafic and business processes. This research borrows concepts from congestion prediction in trafic research to predict performance in business processes. This efort can be extended to deploy other prediction tasks such as trafic flow prediction to achieve relevant prediction results in the field of business process management. Further, other techniques developed in trafic research, such as a method for analyzing trafic violations, can be applied to solve related problems in the business process management.

This paper demonstrates the importance of reflecting spatiotemporal information when building a prediction model at the process model level. The experimental results show that the suggested models, which are designed to incorporate spatial dependence and temporal evolution, outperform two baseline approaches, which do not reflect them. Also, learning proper network topology (e.g., directly-follows relations) is another critical aspect of building reliable prediction models.

When it comes to implications for practice, the proposed method gives practitioners a ready to use tool to predict weaknesses in business processes. This information enables them to make more informed decisions for taking corrective and proactive actions to improve business processes and mitigate risks (e.g., by resource allocation and risk notification). The fast evolution of technology combined with the ever-changing needs of customers forces organizations to swiftly and frequently adapt their business processes.The ability to forecast possible problems in business processes and reacting in a proactive manner is one of the most crucial success factors for organizations. Also, while conducting our case study in the hospital, we noted an increasing requirement of executives to flexibly and proactively deal with operational issues.

As future work, we plan to extend the proposed method by incorporating other process-related performance measures and contextual information into the prediction models. We also plan to apply our proposed method to predict the performance measures from diferent dimensions other than time, such as quality. Second, our proposed method eficiently predicts the future performances of a business process at the process model level and identifies the weakness in the process. However, the predictions must be transformed into concrete remedial actions. In order to deal with this, future works should present a method for improving the performance in business processes by recommending proactive actions with optimization and simulation techniques. Another important direction of future work is to deploy prediction models that quantify the prediction accuracy to support business managers to make decisions on the remedial actions to improve performances and mitigate risks.

## Acknowledgment

This paper was supported by Korea Institute for Advancement of Technology(KIAT) grant funded by the Korea Government(MOTIE) (N0008691, The Competency Development Program for Industry Specialist)

## References

[1] M. Dumas, M. L. Rosa, J. Mendling, H. A. Reijers, Fundamentals of Business Process Management, 2nd Edition, Springer, 2018.

[2] W. M. P. van der Aalst, Process Mining: Data Science in Action, 2nd Edition, Springer, 2016.

[3] A. E. Mrquez-Chamorro, M. Resinas, A. Ruiz-Corts, Predictive monitoring of business processes: A survey, IEEE Transactions on Services Computing 11 (6) (2018) 962–977.

[4] G. Park, M. Song, Prediction-based resource allocation using lstm and minimum cost and maximum flow algorithm, in: 2019 International Conference on Process Mining (ICPM), 2019, pp. 121–128.

[5] S. A. Fahrenkrog-Petersen, N. Tax, I. Teinemaa, M. Dumas, M. de Leoni, F. M. Maggi, M. Weidlich, Fire now, fire later: Alarm-based systems for prescriptive process monitoring, CoRR abs/1905.09568 (2019). arXiv:1905.09568.

[6] W. M. P. van der Aalst, M. Schonenberg, M. Song, Time prediction based on process mining, Information Systems 36 (2) (2011) 450–475.

[7] E. D. Arnheiter, J. Maleyef, The integration of lean management and six sigma, The TQM Magazine 17 (1) (2005) 5–18.

[8] F. Gullo, From patterns in data to knowledge discovery: What data mining can do, Physics Procedia 62 (2015) 18 – 22, 3rd International Conference Frontiers in Diagnostic Technologies, ICFDT3 2013, 25-27 November 2013, Laboratori Nazionali di Frascati, Italy.

[9] C.-H. Wu, J.-M. Ho, D. T. Lee, Travel-time prediction with support vector regression, Trans. Intell. Transport. Sys. 5 (4) (2004) 276–281.

[10] X. Ma, Z. Tao, Y. Wang, H. Yu, Y. Wang, Long short-term memory neural network for trafic speed prediction using remote microwave sensor data, Transportation Research Part C: Emerging Technologies 54 (2015) 187–197.

[11] X. Ma, Z. Dai, Z. He, J. Ma, Y. Wang, Y. Wang, Learning trafic as images: A deep convolutional neural network for large-scale transportation network speed prediction, Sensors 17 (4) (2017) 818.

[12] H. Yu, Z. Wu, S. Wang, Y. Wang, X. Ma, Spatiotemporal recurrent convolutional networks for trafic prediction in transportation networks, Sensors 27 (2017) 1501.

[13] M. Polato, A. Sperduti, A. Burattin, M. D. Leoni, Time and activity sequence prediction of business process instances, Computing 100 (9) (2018) 1005–1031.

[14] A. Pika, W. M. P. van der Aalst, C. J. Fidge, A. H. M. ter Hofstede, M. T. Wynn, Profiling event logs to configure risk indicators for process delays, in: C. Salinesi, M. C. Norrie, O. Pastor (Eds.), Conference on Advanced In-<sup>´</sup> formation Systems Engineering, Springer-Verlag, Berlin, Heidelberg, 2013, pp. 465–481.

method for prediction of abnormal termination using knni-based lof prediction, Expert Systems with Applications: An International Journal 39 (2012) 6061–6068.

[16] D. Breuker, M. Matzner, P. Delfmann, J. Becker, Comprehensible predictive models for business processes, MIS Q. 40 (4) (2016) 1009–1034.

[17] J. Evermann, J.-R. Rehse, P. Fettke, Predicting process behaviour using deep learning, Decision Support Systems 100 (2017) 129–140.

[18] N. Tax, I. Verenich, M. L. Rosa, M. Dumas, Predictive business process monitoring with lstm neural networks., in: E. Dubois, K. Pohl (Eds.), CAiSE, Vol. 10253 of Lecture Notes in Computer Science, Springer, 2017, pp. 477–492.

[19] N. Mehdiyev, J. Evermann, P. Fettke, A novel business process prediction model using a deep learning method, Business & Information Systems Engineering (07 2018).

[20] J. Zhang, F. Wang, K. Wang, W. Lin, X. Xu, C. Chen, Data-driven intelligent transportation systems: A survey, IEEE Transactions on Intelligent Transportation Systems 12 (4) (2011) 1624–1639.

[21] J. Wang, Q. Gu, J. Wu, G. Liu, Z. Xiong, Trafic speed prediction and congestion source exploration: A deep learning method, in: IEEE 16th International Conference on Data Mining, 2016, pp. 499–508.

[22] Y. LeCun, Y. Bengio, G. Hinton, Deep learning, Nature 521 (2015) 436–44.

[23] R. Collobert, J. Weston, A unified architecture for natural language processing: Deep neural networks with multitask learning, in: Proceedings of the 25th International Conference on Machine Learning, ICML ’08, ACM, New York, NY, USA, 2008, pp. 160–167.

[24] J. Donahue, L. A. Hendricks, M. Rohrbach, S. Venugopalan, S. Guadarrama, K. Saenko, T. Darrell, Long-term recurrent convolutional networks for visual recognition and description, IEEE Transactions on Pattern Analysis and Machine Intelligence 39 (4) (2017) 677–691.

[25] T. Tieleman, G. Hinton, Lecture 6.5—RmsProp: Divide the gradient by a running average of its recent magnitude, COURSERA: Neural Networks for Machine Learning (2012).

[26] N. Srivastava, G. Hinton, A. Krizhevsky, I. Sutskever, R. Salakhutdinov, Dropout: A simple way to prevent neural networks from overfitting, J. Mach. Learn. Res. 15 (1) (2014) 1929–1958.

[27] S. Iofe, C. Szegedy, Batch normalization: Accelerating deep network training by reducing internal covariate shift, in: Proceedings of the 32nd International Conference on International Conference on Machine Learning, ICML’15, JMLR.org, 2015, pp. 448–456.

[28] G. Park, M. Song, Prediction-based resource allocation using bayesian neural networks and minimum cost and maximum flow algorithm (2019). arXiv:1910.05126.

# Journal Pre-proof

## Author Biography

![](/api/attachments/BDXF4GS2/fulltext/images/0f023f8a867a0aafef7265c69027c4c06d86dbcd2605684843630fb63c194d74.jpg)

Gyunam Park received the M.S. degree in the Department of Industrial & Management Engineering at POSTECH (Pohang University of Science and Technology), Pohang, South Korea, in 2019. He is currently a Ph.D student in Department of Computer Science, RWTH Aachen University, Aachen, Germany. His research interest includes process mining, data science, online operational support, machine learning, and deep learning. He has participated in several research project funded by Nationa Research Foundation of Korea, Samsung Electronics, etc.

![](/api/attachments/BDXF4GS2/fulltext/images/13a97cacd16f9c6b1026ad3342478974a14240e52b94b98007162f28f2b702b9.jpg)

Minseok Song received his Ph.D. degree in the Department of Industrial & Management Engineering at POSTECH (Pohang University of Science and Technology) in 2006. He is now an associate professor at the Department of Industrial & Management Engineering at POSTECH. Prior to this, he stayed at the Information Systems department of the Technology Management of Eindhoven University of Technology as a post-doctoral researcher from 2006 until 2009. Also, he was an assistant/associate professor at UNIST (Ulsan National Institute of Science and Technology). His research interest includes business process management, process mining, business analytics, simulation, and social network analysis. He has published more than 60 scientific papers in several top-level venues such as Decision

Support Systems, Information Systems, Journal of Information Technology, International Journal of Medical Informatics, etc.

## Highlights

This paper proposes a novel method to predict the future performances of a business process from the historical records of the performances.

The method constructs an annotated transition system and generates a process representation matrix from it.

Based on the process representation matrix, performance prediction models are created using deep neural networks that consider both spatial and temporal dependencies present in the underlying business process.

Two case studies related to a healthcare service process and a manufacturing process are conducted to validate the proposed method.

![](/api/attachments/BDXF4GS2/fulltext/images/876e9de90835a78201e622052141e5f4ef73a4760d2ba3a87858bc9e2d6c71d2.jpg)  
Figure 1

![](/api/attachments/BDXF4GS2/fulltext/images/86bc9d0a11710413ff7ba2cde3e990fbfe8ea33e236e5b3a8084c555ba52b48d.jpg)  
Figure 2

![](/api/attachments/BDXF4GS2/fulltext/images/eccaba6dc9c914c82a2c76ecdd0837b8bb2fb429b8ffc9d723f6be12a860b1cf.jpg)

![](/api/attachments/BDXF4GS2/fulltext/images/bfa2e088ca1ea0af290567635be1fc5cb2733b3b2b39708d96266d66847bac45.jpg)  
(a) CNN-based model

![](/api/attachments/BDXF4GS2/fulltext/images/a914a42f99d5040535f759e3d936305b8d9ee799e75d3094fec605a3eff2c1bc.jpg)  
(b) LSTM-based model

![](/api/attachments/BDXF4GS2/fulltext/images/7a913a49b808dd597a6100ec6e7a9809648d76eabcfaf73c6999a8d8d3ca4af0.jpg)  
(c) LRCN-based model  
Figure 4

![](/api/attachments/BDXF4GS2/fulltext/images/16d84d5a52eae249fc818355e1a6282a4526ac66bbc211c9501fbc8aeab9e5f5.jpg)  
(a) Effect of horizon to MAE

![](/api/attachments/BDXF4GS2/fulltext/images/4b05afc523a9d8b885eb0f0ef56cd5f49804ff229fd4ce06f60feb1c23d77eb4.jpg)  
(b) Effect of horizon to computation time  
Figure 5

---
otero_id: 19708
otero_key: "D6JFYNSY"
title: "A technique for determining relevance scores of process activities using graph-based neural networks"
authors: "Matthias Stierle; Sven Weinzierl; Maximilian Harl; Martin Matzner"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113511"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A technique for determining relevance scores of process activities using graph-based neural networks

![](/api/attachments/D6JFYNSY/fulltext/images/2914320b2ed5f27c8b4eea09e6d07f2518c3eb3f54b3fbc4194598311d005167.jpg)

Matthias Stierle <sup>\*</sup>, Sven Weinzierl, Maximilian Harl, Martin Matzner

Institute of Information Systems, Friedrich-Alexander-Universitat ¨ Nürnberg, Erlangen, Germany

## A R T I C L E I N F O

Keywords: Process mining Process analytics Business process management Deep learning Graph neural networks

## A B S T R A C T

Process models generated through process mining depict the as-is state of a process. Through annotations with metrics such as the frequency or duration of activities, these models provide generic information to the process analyst. To improve business processes with respect to performance measures, process analysts require further guidance from the process model. In this study, we design Graph Relevance Miner (GRM), a technique based on graph neural networks, to determine the relevance scores for process activities with respect to performance measures. Annotating process models with such relevance scores facilitates a problem-focused analysis of the business process, placing these problems at the centre of the analysis. We quantitatively evaluate the predictive quality of our technique using four datasets from different domains, to demonstrate the faithfulness of the relevance scores. Furthermore, we present the results of a case study, which highlight the utility of the technique for organisations. Our work has important implications both for research and business applications, because process model-based analyses feature shortcomings that need to be urgently addressed to realise successful process mining at an enterprise level.

## 1. Introduction

The purpose of business process management (BPM) is to improve business processes [1]. A central role in process improvement is played by the process analyst [2], who is responsible for ‘monitoring, measuring, and providing feedback on the performance of a business process $[ 3 , \mathrm { p } . 4 5 ]$ . The ongoing implementation of information systems in organisations, along with the subsequently enhanced availability of event log data, have enabled process analysts to discover as-is models of processes with process mining (PM) with relative ease [4]. However, the crucial challenge lies in identifying potential areas for process im provements (i.e., process analysis) with respect to a strategic goal [5]; this requires analytical capabilities such as Pareto or root cause analysis [2].

A business process can be defined as a ‘completely closed, timely, and logical sequence of activities’ $\left[ 6 , \mathsf { p } . 3 \right]$ that realises an outcome valuable to a customer [7]. The effectiveness (i.e., customer value) and efficiency (e.g., timely, logical sequence, resource utilisation) of a business process are monitored using key performance indicators (KPIs) as aggregated measures of process outcomes; in the context of BPM, these are often referred to as process performance indicators (PPIs) [8]. Thus, to improve a business process, it is essential for a process analyst to un derstand the relevance of individual process activities in terms of their impact on the dimensions expressed by these performance measures.

For example, we consider a travel reimbursement process at a uni versity; it aims for a high degree of compliance with travel policies. Observing that the KPI ratio of budget violations increases, the process analyst must understand which activities in the process should be redesigned to improve the process; hence, they must evaluate the KPI. In Fig. 1, two discovered process models are presented. On the left, the most frequent path is shown, annotated with the number of occurrences for each activity. The process analyst can deduce information about the reimbursement process’ execution from a generic perspective but not with respect to the budget violations. The right-hand process model indicates the most relevant path in terms of budget violations, and each process activity is annotated with a relevance score expressing its importance thereto. The process analyst can directly identify which activities should be considered for redesign and can also suggest which of these activities should be considered first (e.g., Permit A).

Process model-based analysis—that is, process analysis based on the discovered process model—is able to make users aware of the business processes behind the data and can subsequently guide process analysts as they improve these processes [9]. To facilitate analysis beyond the simple discovery of a process, the process model must provide infor mation suitable for the improvement initiative. Therefore, we design a technique to determine the relevance scores of process activities with respect to a performance measure extracted from the event log data.

![](/api/attachments/D6JFYNSY/fulltext/images/b2810abf55edccf81dbd3503e70a87067e3df279e1d4a3a59e356dd3b242736c.jpg)  
Fig. 1. Process visualisation: frequency vs. relevance.

Determining relevance scores for process activities is an interesting challenge, owing to the plurality of relationships between activities. For instance, an activity may or may not occur; if it does, then it may occur towards the start or end of a process, once or multiple times, and before, after, or between other activities, etc. Understanding these complex relationships and their influences on process performance is a difficult task.

To address this challenge, the field of machine learning (ML) pro vides a set of algorithms that automatically discover structures in data and capture those as mathematical models representing functions [10]. In the context of ML, deep neural networks (DNNs) have ‘turned out to be very good at discovering the intricate structures in high-dimensional data and is therefore applicable to many domains’ [11,p.436]. Among others, Evermann et al. [12], Mehdiyev et al. [13], and Kratsch et al. [14] showed that with deep learning (DL), in particular DNNs, predic tive models can be learned from event log data more accurately than with traditional ML techniques. However, DNNs often struggle to intu itively represent the learned structures; this is commonly referred to as the black-box problem [15].

Graph-based neural networks (GNNs) are a relatively new group of DNNs; they have proved useful in domains where the input data have a graph structure, such as in chemistry and molecular biology [16]. Compared to traditional DNNs such as multi-layer perceptrons, GNNs can compute graph data directly [17]. In particular, the structure of the input graph can be matched directly to the topology of the GNN; this allows for direct inferences to be made between the relevance of network nodes and graph nodes. Gated graph neural networks (GGNNs) are a variant of GNNs; they were designed to tackle temporal de pendencies in the data [18]; such dependencies are a significant aspect of event log data.

The main idea of this paper is to design a GGNN-based techni que—referred to as Graph Relevance Miner (GRM)—to determine the relevance scores (with respect to a given performance measure) of process activities from event log data. First, we transform process in stances using a prediction label (i.e., the performance measure), con verting them into instance graphs (IGs). Second, we input these graphs into the GGNN model for training and testing. Finally, we input multiple instances into the GGNN model, to determine the relevance scores.

This paper builds on previous work where we demonstrated the use of GNNs with process data [19] within the context of explainable artificial intelligence. We presented a technique that provides explanations for predictions made for the outcome of single process instances to process workers. In this paper, we follow up on the idea to extract relevance scores from GNN. However, we shift the focus from the prediction of single instances for process workers onto providing insights on the process level for process analysts. We formally describe the technique and evaluate both its efficacy and its effectiveness with empirical data [20].

The remainder of this paper is organised as follows. In Section 2, we introduce the preliminary information regarding event logs and GNNs. Next, we present the design of our technique in Section 3. In Section 4, we present the results from our evaluation of the technique, obtained for four different real-life datasets; then, we describe our case study. In Section 5, we summarise our contributions, review the related works, and consider the limitations of our study. Lastly, in Section 6, we conclude the paper with a brief summary of the technique’s potential impacts on research and business applications, and we highlight possible future research directions.

## 2. Background

## 2.1. Event logs

PM is a technology that facilitates the discovery, analysis, and enhancement of process models, using the data extracted from event logs [4]. An event log is structured into traces, which are in turn structured into events. Thus, based on Polato et al. [21], we define the terms event universe, event, trace, and event log as follows:

Definition 1 (Event universe). $\mathcal { E } = \mathcal { A } \times C \times \mathcal { T }$ is the event universe in which is the set of process activities, the set of process instances (cases), C the set of case IDs with the bijective projection id : $C \to { \mathcal { C } } ,$ , and T the set of timestamps. To consider time, a process instance $c \in \mathcal { C }$ contains all past and future events, whereas events in the trace $\sigma _ { c }$ of c contain all events up to the current time instant.

Definition 2. (Event). An event $e \in \mathcal { E }$ is a tuple $e = ( a , c , t ) ;$ , where a ∈ A is the process activity, $c \in C$ is the case ID, and $t \in \mathcal { T }$ is its starting timestamp. Given an event e, we define the projection functions $F _ { p } = \{ f _ { a } ,$ $f _ { c } , f _ { t } \} \colon f _ { a } : e \to a , f _ { c } : e \to c , \mathrm { a n d } f _ { t } : e \to t .$

Definition 3. (Trace). A trace is a non-empty sequence $\sigma _ { c } = \langle e _ { 1 } , . . . ,$ $e _ { | \sigma c | } \rangle \in \mathcal { E } ^ { * }$ of events, such that $f _ { c } ( e _ { i } ) = f _ { c } ( e _ { j } ) \wedge f _ { t } ( e _ { i } ) \leq f _ { t } ( e _ { j } )$ for $1 \leq i < j \leq |$ σ ∣. A trace can also be considered as a sequence of vectors, in which a vector contains all or part of the information relating to an event (e.g., an event’s activity). Formally, $\boldsymbol { \sigma } = \langle \mathbf { x } ^ { ( 1 ) } , \mathbf { x } ^ { ( 2 ) } , . . . , \mathbf { x } ^ { ( t ) } \rangle$ , where $\mathbf { x } ^ { ( i ) } \in \mathbb { R } ^ { n \times 1 ^ { - } }$ is a vector, and the superscript denotes the time-ordering of the events.

Definition 4. (Event log). An event log ${ \mathcal { L } } _ { \tau } f o r$ time instant τ is the set of traces such that $\forall \sigma _ { c } \in \mathcal { L } _ { \tau } , \exists c \in \mathcal { C }$ with ∀ $: \in \sigma _ { c } \mathrm { ~ . ~ } i d ( f _ { c } ( e ) ) = c \mathrm { ~ \wedge ~ } \forall e \in \sigma _ { c }$ $f _ { t } ( e ) \leq \tau \ ( \mathrm { i . e . }$ ., all events of the observed cases that have already happened).

Finally, our technique assumes a labelled event log for training. Thus, we define the term label

Definition 5. (Label). Given a trace $\sigma = \langle e _ { 1 } , . . . , e _ { k } , . . . , e _ { | \sigma | } \rangle$ , we can define its label as $f _ { l } ( \sigma ) = l .$ In this paper, a label represents a certain outcome of a process; for example, ‘loan is accepted’ or ‘loan is not accepted’ in the case of a loan application process.

## 2.2. Graph neural networks

GNNs [16] are a type of neural network in which the network ar chitecture is defined according to a graph structure. Because graphs constitute an integral part of these neural networks, we define the term graph first.

Definition 6. (Graph). A tuple $G = ( V , E )$ is a graph, where V is a set of nodes and E a set of edges. A node v ∈ V has a unique value assigned to it, whilst an edge is a pair $e ^ { \circ } = ( \nu , \nu ^ { \prime } ) \in V \times V .$ The node vector (node representation or node embedding) for node v is denoted by $\mathbf { h } _ { \nu } \in \mathbb { R } ^ { D } .$ .D denotes the vector dimensionality of node v. Graphs can also contain node labels $\mathbf { l } _ { \nu } \in \{ 1 _ { 1 } , . . . , 1 _ { | V | } \}$ for each node v, as well as edge labels ${ \mathbf { l } } _ { e } \in \{ { \mathbf { l } } _ { 1 } ,$

$\ldots , \mathbf { l } _ { | E | } \}$ for each edge.

Furthermore, we define four functions to help us manage these graphs.

Definition 7. (Graph functions). $f _ { i n } ( \nu ) = \{ \nu ^ { \prime } | ( \nu ^ { \prime } , \nu ) \in E \}$ returns the set of predecessor nodes $\nu _ { , } ^ { \prime }$ with $\nu ^ { \prime } \to \nu . f _ { o u t } ( \nu ) = \{ \nu ^ { \prime } | ( \nu , \nu ^ { \prime } ) \in E \}$ returns the set of successor nodes $\nu ^ { \prime } ,$ with edges $\nu \to \nu ^ { \prime } . f _ { n b r } ( \nu ) = f _ { i n } ( \nu ) \cup f _ { o u t } ( \nu )$ returns the set of all nodes neighbouring v. $f _ { c o } ( \nu ) = \{ ( \nu ^ { \prime } , \nu ^ { \prime \prime } ) \in E | \nu = \nu ^ { \prime } \vee \nu = \nu ^ { \prime \prime } \}$ is the set of all edges going into or out of v.

GNNs map graphs to outputs via two steps. First, a propagation model computes the node representations $\mathbf { h } _ { \nu }$ for each node v. Through this, the model propagates node representations over time. The initial node representations ${ \bf \ddot { h } } _ { \nu } ^ { ( 0 ) }$ are set to arbitrary values. Then, until convergence is reached, each node representation ${ \bf h } _ { \nu } ^ { ( t + 1 ) }$ is updated ac cording to a local transition function $f _ { l t } \mathbf { : }$

$$
\mathbf {h} _ {v} ^ {(t + 1)} = f _ {l t} \left(l _ {v}, l _ {f _ {c o (v)}}, \mathbf {h} _ {f _ {n b r (v)}} ^ {(t)}, l _ {f _ {n b r (v)}}\right)\tag{1}
$$

The recurrent function $f _ { l t }$ is shared among all nodes. Its input pa rameters are as follows: l (features of node v), $\mathbf { l } _ { f c o ( \nu ) }$ (features of node v’s edges), h (states of the neighbouring nodes; i.e., nodes that are directly connected) and $1 _ { f n b r ( \nu ) }$ (features of the neighbouring nodes). For this, Scarselli et al. [16] have suggested decomposing $f _ { l t } ( \cdot )$ into a sum of terms describing ingoing and outgoing edges:

$$
\begin{array}{l l} \mathbf {h} _ {v} ^ {(t + 1)} = & \sum_ {v ^ {\prime} \in f _ {i n} (v)} f _ {l t} \left(\mathbf {l} _ {v}, \mathbf {l} _ {(v ^ {\prime}, v)}, \mathbf {l} _ {v ^ {\prime}}, \mathbf {h} _ {v ^ {\prime}} ^ {(t)}\right) + \\ & \sum_ {v ^ {\prime} \in f _ {o u t} (v)} f _ {l t} \left(\mathbf {l} _ {v}, \mathbf {l} _ {(v, v ^ {\prime})}, \mathbf {l} _ {v ^ {\prime}}, \mathbf {h} _ {v ^ {\prime}} ^ {(t)}\right) \end{array}\tag{2}
$$

where $f _ { l t }$ is either a feed-forward neural network or a linear function of $\mathbf { h } _ { \nu ^ { \prime } } .$ The terms’ parameters differ according to the label configuration (i. $\boldsymbol { \mathrm { e } } . , \boldsymbol { 1 } _ { ( \nu ^ { \prime } , \nu ) }$ or $\mathbf { l } ( \nu , \nu ^ { \prime } )$ , where each vector represent edge type and direction). For example, in the linear case, $f _ { l t }$ can be defined as follows:

$$
f _ {l t} \left(\mathbf {l} _ {v}, \mathbf {l} _ {\left(v ^ {\prime}, v\right)}, \mathbf {l} _ {v ^ {\prime}}, \mathbf {h} _ {v ^ {\prime}} ^ {(t)}\right) = \mathbf {A} ^ {\left(\mathbf {l} _ {v}, \mathbf {l} _ {\left(v ^ {\prime}, v\right)}, \mathbf {l} _ {v} ^ {\prime}\right)} \mathbf {h} _ {v ^ {\prime}} ^ {(t)} + \mathbf {b} ^ {\left(\mathbf {l} _ {v}, \mathbf {l} _ {\left(v ^ {\prime}, v\right)}, \mathbf {l} _ {v} ^ {\prime}\right)},\tag{3}
$$

where $\mathbf { A } ^ { ( 1 _ { V } , 1 _ { ( V ^ { \prime } , \nu ) } , 1 _ { V } ^ { \prime } ) }$ is the sparsity matrix (or adjacency matrix) containing the weight of the edge running from node $\nu ^ { \prime }$ to $\nu ,$ and $\mathbf { b } ^ { ( 1 _ { \nu } , \mathbf { l } _ { ( \nu ^ { \prime } , \nu ) } , \mathbf { l } _ { \nu ^ { \prime } } ) }$ is the bias of this edge. Both the weight and bias are learnable parameters.

After computing node representations using the propagation model, the output model maps these representations and their corresponding labels to an output. Depending on the problem to be addressed, the output can be graph-based, node-based, or edge-based. In this work, we focus on graph-based outputs, because the outcome of a process is not determined by a single node or edge. The graph-based output ̂o is calculated by a local output function $f _ { l o } { : }$

$$
\widehat {\mathbf {o}} = f _ {l o} \left(\mathbf {h} ^ {(T)}, \mathbf {h} ^ {0}\right)\tag{4}
$$

Similar to the function $f _ { l t } , f _ { l o }$ is either a feed-forward neural network or a linear function of $\mathbf { h } _ { \nu } .$ To summarise, the computations described in $f _ { l t }$ and $f _ { l o }$ can be interpreted as feed-forward neural networks or linear functions, and their (internal) parameters are updated through a gradient-descent strategy.

Lastly, we adopt a framework for standardising GNNs—referred to as message passing neural network (MPNN) [22]—to provide a more intuitive understanding of GNN’s operation. Corresponding to the MPNN framework, a GNN’s propagation and output step—as defined in Scarselli et al. [16]—can be described in terms of message-passing and readout phases. In contrast to the propagation phase, the messagepassing phase updates the node representations ${ \bf h } _ { \nu }$ of node v over T time steps, by using messages ${ \bf m } _ { \nu }$ . Node v’s messages m are calculated from its neighbourhood f via the message function $M _ { t } ,$ as

$$
\mathbf {m} _ {v} ^ {(t + 1)} = \sum_ {w \in f _ {n b r (v)}} M _ {t} \left(\mathbf {h} _ {v} ^ {(t)}, \mathbf {h} _ {w} ^ {(t)}, \mathbf {e} _ {(v, w)}\right),\tag{5}
$$

where $\mathbf { h } _ { \nu } ^ { ( t ) }$ and $\mathbf { h } _ { w } ^ { ( t ) }$ are the node representations of nodes v and w, respectively; $\mathbf { e } _ { ( \nu , w ) }$ represents the features of the edge running from node v to node w. Then, a node update function $U _ { t }$ calculates node v’s new node representation ${ \bf h } _ { \nu } ^ { ( t + 1 ) }$ , as formalised in Eq. (6):

$$
\mathbf {h} _ {v} ^ {(t + 1)} = U _ {t} \left(\mathbf {h} _ {v} ^ {(t)} \mathbf {m} _ {v} ^ {(t + 1)}\right)\tag{6}
$$

Second, the readout phase uses function R to omit the input parameter $ { \mathbf { h } } ^ { 0 }$ of the GNN output function $f _ { l o } ,$ as formalised in Eq. (7):

$$
\widehat {\mathbf {y}} = R \left(\left\{\mathbf {h} _ {v} ^ {(T)} \mid v \in G \right\}\right)\tag{7}
$$

## 2.3. Gated recurrent units of the gated graph neural network

In this paper, we adopt the GGNN architecture described in Li et al. [18]. This architecture extends the ‘vanilla’ GNN of Scarselli et al. [16], using gated recurrent units (GRUs). A GRU [23] can be considered as a logical unit employing two gates to control the information flow over time. These two gates are referred to as reset and forget gates. The reset gate determines the quantity of past information (from previous time steps) to be forgotten; conversely, the update gate determines the quantity of past information to be propagated to the future. Given a sequence of inputs, a GRU computes the sequence of activations via the following recurrent equations:

$$
\mathbf {z} ^ {(t)} = \operatorname{sig} \left(\mathbf {W} _ {z} ^ {T} \mathbf {x} ^ {(t)} + \mathbf {U} _ {z} h ^ {(t - 1)} + \mathbf {b} _ {z}\right),\tag{8}
$$

$$
\mathbf {r} ^ {(t)} = \operatorname{sig} \left(\mathbf {W} _ {r} ^ {T} \mathbf {x} ^ {(t)} + \mathbf {U} _ {r} h ^ {(t - 1)} + \mathbf {b} _ {r}\right),\tag{9}
$$

$$
\widetilde {\mathbf {h}} ^ {(t)} = \tanh \left(\mathbf {W} _ {h} ^ {T} \mathbf {x} ^ {(t)} + \mathbf {U} _ {h} ^ {T} \left(\mathbf {r} ^ {(t)} \odot \mathbf {h} ^ {(t - 1)}\right) + \mathbf {b} _ {h}\right),\tag{10}
$$

$$
\mathbf {h} ^ {(t)} = \mathbf {z} ^ {(t)} \odot \mathbf {h} ^ {(t - 1)} + (1 - \mathbf {z} ^ {(t)}) \odot \widetilde {\mathbf {h}} ^ {(t)},\tag{11}
$$

where sig denotes the sigmoid activation function, r is the reset gate vector, z is the update gate vector, ⊙ indicates a point-wise multipli cation, h is a hidden state vector, b is a bias vector, and W and U are weight matrices. To summarise, the set $\boldsymbol { \theta } = \{ \mathbf { W } , \mathbf { U } , \mathbf { b } \}$ } includes the GRU’s learnable parameters (i.e., its weights and biases). Finally, we define the projection function $f _ { G R U } : ( { \bf h } ^ { ( t ) } , { \bf x } ^ { ( \breve { t } ) } ) \to { \bf h } ^ { ( t + 1 ) }$ <sup>)</sup>, which applies Eqs. (8) to (11).

## 3. GRM – Determining relevance scores of process activities with GGNNs

GRM determines the relevance scores for activities using the event log data. GRM is based on GGNNs. GRM consists of three steps: (1) event log transformation, (2) GGNN model creation and training, and (3) pre diction and relevance determining. The steps are depicted in Fig. 2.

First, GRM loads an event log, transforms it into IGs, and numerically encodes the IGs’ categorical values. To determine process activity rele vance scores, a GGNN model requires a graph-oriented representation of the event log data, in the form of IGs. Second, GRM receives as its input the IGs from the previous step, creating and training the GGNN model therefrom. In the last step. GRM feeds the IGs into the GGNN model. to calculate the outcome prediction. Thus, it determines the relevance scores for activities, using IGs from the GGNN model.

In the following, we refer to the representative event log $\mathcal { L } _ { \tau } ^ { e x } - \mathsf { a s }$ depicted in Table 1—to describe our technique’s steps. $\mathcal { L } _ { \tau } ^ { e x }$ comprises the trace $\sigma _ { 1 } ,$ which represents Case 1 of a reimbursement process for business travel.<sup>1</sup> Along with the three control-flow attributes Case, Ac tivity, and Timestamp, the event log includes the data attribute Travel expense overspent. The data attribute takes either the value ‘true’ or ‘false’; this indicates whether or not the travel expense was excessive. We consider this data attribute as the target attribute for learning, and we use it to apply our technique’s GGNN model M .

![](/api/attachments/D6JFYNSY/fulltext/images/61f9955a727d971c511c44891442eaeeac659c4c8c5b5ece9ca9e5d3c6d59136.jpg)  
Fig. 2. Our three-step GGNN-based technique for determining activity relevance scores.

Examplary event log $\mathcal { L } _ { \tau } ^ { e x }$ comprising the trace $\sigma _ { 1 \cdot }$

<table><tr><td>Case</td><td>Activiy</td><td>Timestamp</td><td>Travel expense overspent</td></tr><tr><td>1</td><td>Start Trip</td><td>01.02.16 10:06:00</td><td>True</td></tr><tr><td>1</td><td>Permit S</td><td>01.02.16 11:43:00</td><td></td></tr><tr><td>1</td><td>Permit A</td><td>01.02.16 13:00:10</td><td></td></tr><tr><td>1</td><td>Permit A</td><td>01.02.16 15:10:00</td><td></td></tr><tr><td>1</td><td>Permit F_A</td><td>02.02.16 12:00:04</td><td></td></tr><tr><td>1</td><td>End trip</td><td>03.02.16 17:30:39</td><td></td></tr><tr><td>1</td><td>Send Reminder</td><td>04.02.16 12:00:00</td><td></td></tr><tr><td>1</td><td>Send Reminder</td><td>05.02.16 12:00:00</td><td></td></tr></table>

## 3.1. Event log transformation

First, our technique transforms the event log data into a graph oriented representation that can be employed by the GGNN model ${ \mathcal { M } } .$ The transformation procedure consists of three steps: (1) event log importing, (2) IG creation, and (3) numerical encoding.

To begin, GRM loads an event log $\mathcal { L } _ { \tau } .$ . This event log $\mathcal { L } _ { \tau }$ is trans formed into a data set ${ \mathcal { D } } ,$ where each instance represents a sequence of activities. As previously described, the activity and timestamp constitute elements of an event tuple. The events of the sequence are sorted by their timestamp values. To obtain the sequence of activities of trace $\sigma _ { c }$ from $\mathcal { L } _ { \tau } ,$ we use the projection function $f _ { a } ( e )$ ∀e $\in \sigma _ { c } .$ Moreover, the target attribute’s value for each case is stored in a global label vector. After transformation, the trace $\sigma _ { 1 }$ of the event log $\mathcal { D }$ is represented, as shown in (12).

$$
\begin{array}{l l} \sigma_ {1} = \langle & \langle \text { StartTrip } \rangle , \langle \text { PermitS } \rangle , \langle \text { PermitA } \rangle , \\ & \langle \text { PermitA } \rangle , \langle \text { PermitF\_A } \rangle , \langle \text { Endtrip } \rangle , \\ & \langle \text { SendReminder } \rangle , \langle \text { SendReminder } \rangle \rangle \end{array}\tag{12}
$$

Second, GRM transforms the dataset $\mathcal { D }$ into a set of IGs ${ \mathcal { I } } .$ To this end, van Dongen and van der Aalst [24] and Diamantini et al. [25] have proposed methods to map sequences of events $( \mathrm { i . e . }$ , traces) onto directed graphs of events, to enhance the transparency of the event log’s traces in an isolated or aggregated manner. In these methods, the node of a graph instance represents an event. However, we are here interested in the relevance scores of activities $( \mathrm { i . e . , }$ event types) on the prediction outcome. Thus, we introduce a definition of the IG, in which a node denotes an activity.

Definition 8. (Process instance graph). Given the trace $\sigma _ { C }$ representing a sequence of activities for dataset ${ \mathcal { D } } ,$ , an IG is a tuple of two elements $\Psi _ { \sigma c } =$ $( V _ { \sigma c } ^ { \Psi } , E _ { \sigma c } ^ { \Psi } ) ,$ , where $V _ { \sigma c } ^ { \Psi }$ denotes the set of nodes extracted from the trace $\sigma _ { c } ,$ , and $E _ { \sigma c } ^ { \Psi }$ denotes the set of edges extracted from the trace $\sigma _ { c * }$ . For an activity $a \in \sigma _ { c } ,$ we define the projection function $f _ { \nu } : a  \nu ; \forall a \in \sigma _ { c } ,$ we apply $f _ { \nu } ( . )$ to obtain

$V _ { \sigma c } ^ { \Psi } .$ . Hence, each activity $a \in \sigma _ { c }$ is mapped to a node $\nu \in V _ { \sigma c } ^ { \Psi }$ . Furthermore, we add the ‘pseudo-activity’ 〈Start/End〉 in form of a node to the set of nodes $V _ { \sigma c } ^ { \Psi } .$ An edge e connecting two nodes is represented by a tuple of two temporally ordered nodes $( f _ { \nu } ( a _ { i } ) , f _ { \nu } ( a _ { j } ) ) \in \sigma _ { c } ,$ with $0 < i \leq j \leq \mid \sigma _ { c } \vert .$ Moreover, we add two edges to the set of edges $E _ { \sigma c } ^ { \Psi }$ . First, the edge $( f _ { \nu } ( \langle S t a r t / E n d \rangle ) , f _ { \nu } ( a _ { 1 } ) )$ from node f (〈Start/End〉) to node f (a ) represents the first activity of $\sigma _ { c } .$ . Second, the edge $( f _ { \nu } ( a _ { \vert \sigma c \vert } ) , f _ { \nu } ( \langle S t a r t / E n d \rangle ) )$ from node $f _ { \nu } ( a _ { | \sigma c | } )$ to node f (〈Start/End〉) represents the last activity of $\sigma _ { c } .$

We introduce the activity ‘Start/End’ as a node in $V _ { \sigma c } ^ { \Psi }$ of $\Psi _ { \sigma c } ,$ to indicate the start and end of the original trace $\sigma _ { c } .$ . The GGNN model expects the IGs for such a ‘Start/End’ activity to preserve the correct ordering of the instances’ activities in the model-learning and prediction phases. For example, the trace $\sigma _ { 1 }$ from Eq. (12) is transformed into the IG $\Psi _ { \sigma 1 } ,$ as depicted in Fig. 3.

Furthermore, the GGNN model M requires IGs, where each input edge has a discrete edge type assigned to it [18]. Thus, $\forall ( f _ { \nu } ( a _ { i } ) , f _ { \nu } ( a _ { j } ) ) \in$ $E _ { \sigma _ { c } } ^ { \mathrm { ~ \searrow ~ } }$ of an IG $\Psi _ { \sigma _ { c } }$ (where $0 < i \leq j \leq \ | \ \sigma _ { c } | )$ , we define the edge type annotation function $f _ { e t } ( ( x _ { 1 } , x _ { 2 } ) , \Psi _ { \sigma _ { c } } ) _ { : }$ , as formalised in $\operatorname { E q . }$ (13).

$$
f _ {e t} \Big ((x _ {1}, x _ {2}), E _ {\sigma_ {c}} ^ {\Psi} \Big) = \left\{ \begin{array}{l l} \langle \text {Recursive} \rangle & \text { if } x _ {1} = x _ {2}, \\ \langle \text { Start} \rangle & \text { if } x _ {1} = f _ {v} (\langle \text { Start / End } \rangle), \\ \langle \text { End } \rangle & \text { if } f _ {v} (\langle \text { Start / End } \rangle) = x _ {2}, \\ \langle \text { Backward } \rangle & \text { if } \exists (x _ {2}, x _ {1}) \in E _ {\sigma_ {c}} ^ {\Psi}, \\ \langle \text { Forward } \rangle & \text { else }. \end{array} \right.\tag{13}
$$

The edge type is also stored in the respective edges of $E _ { \sigma _ { c } } ^ { \Psi } .$ . For example, following the insertion of the edge type 〈Start〉 between the source and target node, the edge can be represented as (〈Start/End〉, 〈 Start〉, 〈StartTrip〉) in ${ E _ { \sigma _ { 1 } } } ^ { \Psi } .$ . Fig. 4 depicts the IG of our running example $\Psi _ { \sigma _ { 1 } } ,$ including its edge types.

In the last step of event log transformation, we numerically encode the categorical node label $( \mathrm { i . e . , }$ , activity) and edge label values of the IGs. The GGNN used in this paper requires a numerical encoding of the input data for calculating forward- and backward-propagation [18]. To ensure this, we one-hot encode the categorical label values of the IGs’ nodes and edges (i.e., source node, edge type, and target node).

![](/api/attachments/D6JFYNSY/fulltext/images/cb273dfb527e0050aae92f3c458efb3dce2ea606c9cdf7f3e7d67b49750d0b30.jpg)  
Fig. 3. IG $\Psi _ { \sigma _ { 1 } }$ extracted from trace $\sigma _ { 1 } .$

![](/api/attachments/D6JFYNSY/fulltext/images/392858cbd5007f29a6858d77d2543875914e13994bbafd321eb612eb0295cafe.jpg)  
Fig. 4. Graph-oriented representation of IG $\Psi _ { \sigma _ { 1 } }$ with edge types.

## 3.2. GGNN model creation and training

GRM uses a GGNN to create and train the model M for process outcome prediction, using the set of IGs ℐ. From the created model, activity relevance scores for individual IGs are determined during pre diction. We select a GGNN model because it can directly manage the graph-oriented structure of process data; expressed otherwise, it can explicitly map process activities of IGs as nodes and even the relation ships between these process activities as edge types and directions. Typically, other ML or DL algorithms are incapable of understanding the semantics of a process to the same extent. This is because they do not encode node and edge information separately from each other, and some neglect edge information entirely [17]. Therefore, GGNN models are a promising candidate for capturing process semantics.

For our GGNN architecture, we used an adapted version of the ar chitecture proposed in Li et al. [18]. Their GGNN extends the ‘vanilla GNN of Scarselli et al. [16] through using GRUs [23] and back propagation through time (BPTT) [26] for parameter learning. GRUs resolve the problem of gradient vanishing [27], which occurs when performing backpropagation in GNNs for longer sequences [18]. Generally, event logs include several sequences exceeding 50 steps (cf., the event logs we use in this paper). On the other hand, the BPTT gradient-based technique enables us to learn the internal parameters of a GGNN more efficiently [17]. Such efficient computation is necessary because event logs can contain several million events.

According to the MPNN framework of Gilmer et al. [22], the archi tecture of the GGNN model can be described in terms of message-passing and readout phases. The message-passing phase receives as its input IGs of $\mathcal { I }$ and returns abstract node representations. In our case, an IG’s nodes represent process activities. In the message-passing phase, these node representations $\mathbf { h } ^ { ( t + 1 ) }$ are calculated via two steps. First, for a node v, it calculates messages m $\mathbf { \Delta } _ { \mathbf { \nu } } ^ { ( t + 1 ) }$ by applying the message function $M _ { t } ,$ as formalised in $\operatorname { E q } .$ . (14).

$$
\mathbf {m} _ {v} ^ {(t + 1)} = \sum_ {w \in f _ {n b r} (v)} M _ {t} \left(\mathbf {h} _ {v} ^ {(t)}, \mathbf {h} _ {w} ^ {(t)}, \mathbf {e} _ {(v, w)}\right) = \sum_ {w \in f _ {n b r} (v)} \mathbf {A} _ {e (v, w)} \mathbf {h} _ {w} ^ {(t)}.\tag{14}
$$

Messages express the interactions between nodes; here, these are the interaction between process activities of IGs. Given these messages $\mathbf { m } _ { \nu } ^ { ( t + 1 ) }$ and the node representations ${ \bf h } _ { \nu } ^ { ( t ) }$ of node v at time $\mathbf { \rho } ( t ) ,$ the new node representation ${ \bf h } _ { \nu } ^ { ( t + 1 ) }$ of node v at time $( t + 1 )$ can be calculated by using the node update function $f _ { G R U } ,$ as shown in Eq. (15).

$$
\mathbf {h} _ {v} ^ {(t + 1)} = f _ {G R U} \left(\mathbf {h} _ {v} ^ {(t)}, \mathbf {m} _ {v} ^ {(t + 1)}\right)\tag{15}
$$

For every node of an IG $\Psi _ { \sigma _ { c } } \in \mathcal { I } ,$ , node representations are updated roughly simultaneously for each time step (t). Depending on the number of hidden layers and propagation steps per each hidden layer, the update of the node representations is repeated. After completing the last propagation step in the final layer, the message-passing phase outputs the final node representations to the readout phase.

Then, the readout phase takes as its input the abstract node repre sentations ${ \bf h } _ { \nu } ^ { ( T ) }$ and maps these to a predicted process outcome $\widehat { \mathbf { o } }$ via the readout function $R ,$ as formalised in Eq. (16):

$$
\widehat {\mathbf {o}} = R \left(\left\{\mathbf {h} _ {v} ^ {(T)} \mid v \in G \right\}\right)\tag{16}
$$

The predicted process outcome $\widehat { \mathbf { o } }$ is a real value lying within the range [0, 1]. To learn the GGNN’s internal parameters, the loss function mean squared error is applied to each data point (i.e., prediction and label) of a batch of IGS $\in \mathcal { I }$ and measures the penalty. Additionally, a cost function calculates the sum of loss functions over the batch of IGs $\in { \mathcal { I } } .$ . After parameter learning, the values of the GGNN model M are adjusted.

## 3.3. Prediction and relevance determining

GRM extracts the relevance scores for the process activities of an IG $\Psi _ { \sigma c } \in \mathcal { I }$ from the created GGNN model M during outcome prediction. Given an IG $\Psi _ { \sigma c s }$ the GGNN model M returns a real-valued process outcome prediction ̂o. If the value of the prediction is $\ge 0 . 5 ,$ we map the value to 1; otherwise, we map it to 0. During prediction, relevance scores are calculated by the readout phase of the model M , based on the final node representations provided by the message-passing phase. The rele vance scores are the weights of the nodes representing process activities of an IG $\Psi _ { \sigma c } .$ . Such weights express a process activity’s importance with regard to a predicted process outcome. To understand how the relevance scores are calculated in the model ${ \mathcal { M } } ,$ the readout function R (cf., Eq. (16)) can be further described as follows [18]:

$$
\widehat {\mathbf {0}} = R \left(\operatorname{sig} \left(\tanh \left(\sum_ {v \in G} \operatorname{sig} \left(i \left(\mathbf {h} _ {v} ^ {(T)}, \mathbf {h} _ {v} ^ {0}\right)\right) \odot \tanh \left(j \left(\mathbf {h} _ {v} ^ {(T)}, \mathbf {h} _ {v} ^ {0}\right)\right)\right)\right)\right),\tag{17}
$$

where the term $\mathrm { s i g } ( i ( \mathbf { h } _ { \nu } ^ { ( T ) } , \mathbf { h } _ { \nu } ^ { 0 } ) )$ ) calculates the node relevance $r _ { \nu }$ for node $\nu ,$ and the term tanh $( j ( \mathbf { h } _ { \nu } ^ { ( T ) } , \mathbf { h } _ { \nu } ^ { 0 } ) )$ returns the node representation of node v. i and j are neural networks. Both neural networks take as their inputs the concatenation of the final node representation ${ \bf h } _ { \nu } ^ { ( T ) }$ and the initial node representation h<sup>0</sup>. A graph-based representation vector $\mathbf { h } _ { G }$ is calculated by point-wise multiplying the output of both terms for each node, calculating the sum over all nodes, and inputting this through a tanh activation function. Then, a sigmoid function (sig) is applied to the vector $\mathbf { h } _ { G } ,$ to obtain a process outcome prediction ̂o.

More specifically, the term $\mathrm { s i g } ( i ( \mathbf { h } _ { \nu } ^ { ( T ) } , \mathbf { h } _ { \nu } ^ { 0 } ) )$ ) operates as a soft-attention mechanism; it determines which activities of the IG $\Psi _ { \sigma c }$ are of greater and lesser relevance to the current graph-based process outcome. The term returns for each node v a real-valued relevance score $r _ { \nu \mathrm { * } }$ . To capture the relevance scores for all activities of the IG $\Psi _ { \sigma c , \mathbf { \ell } }$ we store these in a relevance score vector $\mathbf { r } \Psi \sigma c \in \mathbb { R } ^ { | V | \times 1 }$ . Then, we min-max normalise the activities’ relevance scores of $\mathbf { r } _ { \Psi \sigma c \cdot }$ For this. the minimum is set to $^ { 0 , }$ and the maximum is set to 1. Note: The relevance scores of the activities excluded from the IG $\Psi _ { \sigma c }$ are set to zero.

For instance, GRM determines for the IG $\Psi _ { \sigma _ { 1 } }$ the relevance score vector $\mathbf { r } _ { \Psi _ { \sigma 1 } } = \langle 0 . 4 , 0 . 1 , 0 . 0 5 , 0 . 2 5 , 0 . 1 , 0 . 2 5 \rangle$ , by calculating the process outcome prediction $\widehat { \mathbf { o } } _ { \Psi _ { \sigma _ { 1 } } } = 1 \ ( ^ { \circ } \mathrm { t r u e } ^ { \prime } )$ from the GGNN model M . In this example, the activity ‘Start Trip’ obtains the highest relevance score of 0.3, indicating the importance of this activity for the process outcome (i.

$\mathrm { e } _ { \cdot , }$ the overspending of travel expenses).

## 4. Evaluation

## 4.1. Procedure

The goal of the evaluation is to assess (1) the efficacy of our tech nique and (2) its effectiveness [20]. We consider GRM to be efficacious if it delivers relevance scores for process activities with a high faithfulness [28]. Therefore, we evaluate the predictive quality (which determines the quality of the relevance scores) of the model and compare it against those of other state-of-the-art techniques. Furthermore, we verify the relevance scores by repeating the experiments after removing each in stance’s most/least relevant activity from one of the datasets, to observe changes in predictive quality. Thus, to evaluate the efficacy of GRM, we test the following hypotheses: (1) GRM exhibits a similar or superior predictive quality to other state-of-the-art algorithms for outcome pre diction and (2) removing activities identified by GRM as being most relevant has a stronger negative impact on predictive quality than removing activities that it identifies as least relevant.

We consider GRM effective if it fulfils the stated goal of supporting process analysts in improving business processes. More specifically, we aim to close the gap between process discovery and process analysis, using GRM. We conduct a case study to evaluate the usefulness of the relevance scores determined through GRM for process analysts, in terms of identifying the root causes of process performance issues in the pro cess flow.

## 4.2. Setup

To improve model generalisability, we randomly shuffle the process instances of each event log. For this, we perform a process-instancebased sampling to consider the process-instance-affiliations of event log entries. For each event log, we perform ten-fold cross-validation. Thus, in every iteration, the event log’s process instances are split into a 90%-training and 10%-testing set. Additionally, we use 10% of the training set for validation; this prevents overfitting by implementing early stopping after ten epochs (i.e., learning iterations).

As a benchmark, we use three state-of-the-art ML algorithms for predicting process outcomes: bi-directional long short-term memory DNN (BiLSTM) [29], Random Forest (RF) [30], and XGBoost (XG) [31]. Hinkka et al. [32] demonstrate that GRUs achieve a comparable pre dictive quality like ‘vanilla’ LSTMs while being more efficient. However, efficiency is not within the scope of our evaluation. We decided to use a BiLSTM as DNN-based benchmark, because it can exploit the sequences control-flow information from both directions and because BiLSTMs tend to outperform ‘vanilla’ LSTMs in terms of predictive quality [29].

We measure predictive quality (i.e., efficacy) using the following metrics: Area under the receiver operating characteristic (ROC) curve (AUC ), Specificity, and Sensitivity [33]. $A U C _ { R O C }$ measures a classifier’s ability to avoid false classifications [33]. A major advantage of the AUC over other popular measures—such as the Accuracy (overall correctness of a classifier) or F1-score (harmonic mean of Precision and Recall)—is that it remains unbiased for a highly imbalanced class label distribution [14]. In outcome prediction scenarios, the distribution of class labels is typically imbalanced [31]. Additionally, we use Specificity (true negative rate (TNR) = 1 – false positive rate (FPR)) and Sensitivity (true positive rate (TPR)) to measure the classifiers’ predictive quality. The FPR and TPR are mapped onto the ROC curve’s horizontal and vertical axes, respectively. Therefore, the Specificity and Sensitivity allow us to better interpret the $A U C _ { R O C } .$ For significance testing, we perform a Friedman test followed by a Nemenyi test (post hoc) as suggested by Demˇsar [34] for each data set and metric. Finally, to intuit the classifier predictions' robustness, we evaluate the standard deviation over the ten folds for each measurement.

For the second part of the evaluation $( \mathrm { i . e . , }$ evaluating the effectiveness of GRM), we use the best models (in terms of the AUC ) from the first part of the evaluation, to determine relevance scores for single instances. We use the directly-follows graph (DFG) miner in pm4py<sup>2</sup> to identify the process from the event log, and we colour the activities according to their relevance. DFGs are a user-friendly visual isation that ‘shows which activities can follow another directly’ [35]. To visualise multiple instances, we split them by outcome label (because the relevance scores are only useful for the predicted outcome of the instance) into two datasets and aggregate the relevance scores for each by finding the mean value.

Table 2  
Event log characteristics.

<table><tr><td>Event log</td><td>No. of instances</td><td>No. of events</td><td>No. of activities</td><td>Target variable</td><td>Class distr. (pos./ neg.)</td></tr><tr><td>bpi2017w</td><td>31,500</td><td>128,227</td><td>8</td><td>Loan accepted</td><td>73.04–26.96</td></tr><tr><td>bpi2018al</td><td>43,809</td><td>2,514,266</td><td>41</td><td>Rejected</td><td>0.62–99.38</td></tr><tr><td>bpi2020pl</td><td>7,065</td><td>69,193</td><td>48</td><td>Overspent</td><td>26.80–73.19</td></tr><tr><td>sp2020</td><td>23,906</td><td>178,078</td><td>13</td><td>Repair in time</td><td>34.65–65.35</td></tr></table>

## 4.3. Data

We evaluate GRM using four real-life event logs, whose character istics are summarised in Table 2. Three of them originate from the Business Process Intelligence challenges; the other was provided by a mid-sized German home appliances vendor.

bpi2017w [36] contains event data describing the loan application process of a Dutch financial institute. We only consider workflow events, which are executed by humans. For the outcome prediction target, we select the attribute accepted. Therefore, GRM determines the relevancy of process activities with respect to the acceptance or rejection of a loan.

bpi2018al [37] describes the European Union’s application process for German farmers (Application log). For the outcome prediction target, we select the attribute rejected, which is highly imbalanced. Therefore, GRM determines the relevancy of process activities with respect to the rejection or acceptance of direct payment applications.

bpi2020pl [38] describes the reimbursement process at the Eind hoven University of Technology (Permit log). For the outcome prediction target, we select the attribute travel expense overspent. Therefore, GRM determines the relevancy of process activities with respect to the adherence or non-adherence to travel budgets.

sp2020 [39] represents a customer service process for faulty home appliance devices in need of repair. We collected the dataset and pub lished it along with a documentation as part of this research. The process begins with the creation of the repair order; then, it proceeds through the reception and analysis of the device, extending up to the actual repair and the final return of the device to the customer. We choose the attribute customer repair on time as the outcome prediction target. Therefore, GRM determines the relevancy of process activities with respect to the meeting or falling short of service agreements (in terms of repair time) with customers.

To run the experiments, we implemented GRM using Python. For reproducibility, the source code, event logs, and results can be found on GitHub.<sup>3</sup>

## 4.4. Results for predictive quality

Table 3 presents the results (averaged over ten folds) for GRM and the baseline techniques. In terms of $A U C _ { R O C } ,$ GRM outperforms all three baseline techniques for each dataset (signficantly for bpi2018al). Taking a closer look (by considering Specificity and Sensitivity), it is seen that GRM is consistently significantly superior for the less frequent class (in the bpi2017w event log, the negative class is underrepresented, whereas in the other three logs it is overrepresented). We can see that the more distorted the class of interest is, the better GRM’s results are for the weaker class compared to the baseline techniques. This observation accords well with the research in Kratsch et al. [14], which found that DL techniques outperformed traditional ML techniques for imbalanced target variables in process outcome prediction. However, our results show that of the DL architectures, GGNNs clearly outperform LSTMs.

Table 3 Predictive Quality of GRM.

<table><tr><td>Event log</td><td>Technique</td><td> $AUC_{ROC}$ </td><td>Sensitivity</td><td>Specificity</td></tr><tr><td rowspan="4">bpi2017w</td><td>GRM</td><td>0.600 (0.007)</td><td>0.806 (0.057)</td><td>0.395**(0.060)</td></tr><tr><td>BiLSTM</td><td>0.593 (0.005)</td><td>0.948 (0.004)</td><td>0.237 (0.011)</td></tr><tr><td>RF</td><td>0.589 (0.008)</td><td>0.941 (0.006)</td><td>0.238 (0.014)</td></tr><tr><td>XG</td><td>0.590 (0.005)</td><td>0.942 (0.004)</td><td>0.237 (0.010)</td></tr><tr><td rowspan="4">bpi2018al</td><td>GRM</td><td>0.942 (0.015)</td><td>0.945**(0.032)</td><td>0.939 (0.010)</td></tr><tr><td>BiLSTM</td><td>0.784 (0.19)</td><td>0.569 (0.401)</td><td>0.999 (0.000)</td></tr><tr><td>RF</td><td>0.530 (0.014)</td><td>0.060 (0.030)</td><td>1.000 (0.000)</td></tr><tr><td>XG</td><td>0.546 (0.028)</td><td>0.094 (0.059)</td><td>0.999 (0.000)</td></tr><tr><td rowspan="4">bpi2020pl</td><td>GRM</td><td>0.625**(0.021)</td><td>0.793**(0.060)</td><td>0.457* (0.052)</td></tr><tr><td>BiLSTM</td><td>0.528 (0.017)</td><td>0.078 (0.045)</td><td>0.978 (0.011)</td></tr><tr><td>RF</td><td>0.535 (0.011)</td><td>0.128 (0.028)</td><td>0.942 (0.013)</td></tr><tr><td>XG</td><td>0.541 (0.012)</td><td>0.138 (0.030)</td><td>0.943 (0.013)</td></tr><tr><td rowspan="4">sp2020</td><td>GRM</td><td>0.778 (0.007)</td><td>0.813**(0.019)</td><td>0.744** (0.014)</td></tr><tr><td>BiLSTM</td><td>0.763 (0.012)</td><td>0.645 (0.038)</td><td>0.881 (0.016)</td></tr><tr><td>RF</td><td>0.757 (0.006)</td><td>0.631 (0.016)</td><td>0.882 (0.009)</td></tr><tr><td>XG</td><td>0.759 (0.005)</td><td>0.633 (0.009)</td><td>0.884 (0.009)</td></tr></table>

As all Friedman tests indicated a difference between the techniques, we only report the results of the Nemenyi post hoc test. $^ { \ast } / ^ { \ast \ast }$ indicates that a technique was significantly different (i.e. better or worse) from all alternatives. See GitHub repository for detailed results. $^ { * } p < 0 . 1 , ^ { * * } p < 0 . 0 5 .$

Meanwhile, GRM performs significantly worse on three of four datasets for the more frequent class. While GRM still performs reason ably well for some of the datasets (e.g., bpi2018al and sp2020), the results also suggest that GRM performs poorly for a more frequent class (e.g., bpi2020pl). This part of the evaluation did not aim to prove that GRM is superior to other state-of-the-art techniques but rather to assure a reasonable predictive quality relative to the baselines. The $A U C _ { R O C }$ values for GRM are better than those of the baseline techniques for all datasets; thus, we are confident that GRM can compete against state-ofthe-art predictive business process (PBPM) techniques. However, when using GRM to determine the relevance scores for the more frequent class, the predictive quality (sensitivity or specificity)—operating as a proxy for the faithfulness of the relevance scores—must first be assured by the process analyst.

To further substantiate the validity of the relevance scores, we created two new datasets from the sp2020 dataset, by removing the least and most frequent activity from each instance, respectively. The AUC results in Table 4 confirm the hypothesis that removing an activity results in a lower predictive quality (i.e., less information for the model). More importantly, it confirms our hypothesis that the effect of removing the most relevant activity is significant (for $A U C _ { R O C }$ and Specificity). Removing the least relevant activity from an instance has little impact on the $A U C _ { R O C } ,$ and the Sensitivity even improves slightly. There is a noticeable difference for Specificity; however, this did not prove to be significant.

Table 4  
Predictive quality of GRM after removing least/most relevant activities.

<table><tr><td>Event log</td><td> $AUC_{ROC}$ </td><td>Sensitivity</td><td>Specificity</td></tr><tr><td>sp2020</td><td>0.778 (0.007)</td><td>0.813 (0.019)</td><td>0.744 (0.014)</td></tr><tr><td>sp2020 (w/o least relevant)</td><td>0.774 (0.006)</td><td>0.818 (0.019)</td><td>0.729 (0.017)</td></tr><tr><td>sp2020 (w/o most relevant)</td><td>0.764*(0.008)</td><td>0.804 (0.018)</td><td>0.724* (0.006)</td></tr></table>

The Friedman test indicated no difference between the Sensitivity values but for $A U C _ { R O C }$ and Specificity. The Nemenyi test showed that w/o most is significantly worse than the origingl event log and w/o least. See GitHub repository for detailed results. $^ { \ast } p < 0 . 0 5$

## 4.5. Case study

To evaluate the utility of GRM, we conducted a case study. For this, we sought an organisation that was actively engaging in process improvement and had event log data available for the respective pro cesses. The company that provided us with the sp2020 event log is a premium supplier for home appliances, who strives for service excel lence. Their portfolio comprises roughly 25 products (not considering remakes of device types). Their sales are exclusively performed by retail partners (i.e., no direct sales); however, customer service is primarily delivered by the company itself, giving it strategic value. One of their important target measures is the percentage of service orders fulfilled within five business days.

Several workshops were held, in which we learned about the com pany, its products, and the customer service process; these workshops included a visit of the repair shop. In return, we introduced them to PM and began a data-driven analysis of their customer service process. In a joint effort between the head of customer service (as process owner), process analysts, and customer service agents (as process participants), we implemented GRM to identify and analyse the process in terms of delayed repairs.

From the class distribution in Table 2, it is evident that only 32.6% of all repairs could be completed within the desired time-frame of five business days. Hence, the company was eager to improve their repai time and subsequent customer satisfaction. However, their process an alysts struggled to identify the root causes for delays within the process execution. Fig. 5 illustrates a DFG mined from the sp2020 event log. The frequency was represented by the activities’ colours and edge thick nesses (darker blue/thicker = more frequent). This process visualisation represents the current process-discovery capabilities of PM software, as we identified from a recent market study.<sup>4</sup>

While it offered the process analysts some insights pertaining to the repair time (e.g., a high degree of variation was found for non-timely service orders), the analysts struggled to identify root causes for the delays from the process flow. Log filtering was applied as a possible method for isolating the issues, although this was predominantly a tedious procedure of trial and error.

In contrast, Fig. 6 shows a DFG mined from the sp2020 event log, augmented with the relevance scores determined through GRM. Each process activity is coloured according to its relevance score, which was determined by averaging the scores of all instances with the same outcome prediction (i.e., either positive or negative) contained in the log (darker colours correspond to higher relevance).

Presented with Fig. 6 in a workshop, the process analysts were immediately drawn towards the process activity Approved. According to the process stakeholders, the activity indicates that the customers were required to provide approval for costs that were incurred for the repair but not covered by the warranty. Further analysis showed that the process was indeed delayed when the activity Approved occurred, not only whilst waiting for the approval but also because it occasionally took several days to even request approval from the customer. The company implemented an immediate redesign of the process, by starting low-cost repairs without approval; this was because the risk of losing an unsat isfied customer through long repair times exceeded the risk of bearing the costs. Looking at the next most relevant process activities,

No of Service Orders: 4307, Filter: Repair not on time (Label = 0)

![](/api/attachments/D6JFYNSY/fulltext/images/7bd161797b3c658f63ea5184656005fa56c31543d7ee3efbc7961040ae1f8680.jpg)  
Fig. 5. Process model discovered using pm4py’s DFG miner with frequency information.

StatusRequest simply indicated that the customer became impatient with the long waiting times, whilst StockEntry suggested that missing spare parts delayed the process. Here, an immediate action was to increase the stock for all service points.

To summarise, both figures provided insights regarding the delays in repair time. However, the process analysts found it easier to analyse the process model that was augmented with relevance scores based on the business goal. The activities marked as more relevant drew their attention and triggered immediate discussions, resulting in process redesign ideas.

## 5. Discussion

Process analysis—in particular, root cause analysis—is a challenging task and a significant endeavour for organisations, owing to the continuous need to improve business processes for lasting competitive ness [5]. Manual analysis of a process can be costly and time-consuming. PM has emerged as a data-driven technology to support process analysts. By definition, process discovery in BPM facilitates the identification of the as-is process (model) of an organisation [7,p.155], which is therefore the objective of discovery techniques in PM. The discovered process model encourages data analysis from a process perspective, rather than—for example—tables or column charts, which omit the process dimension behind the data. As such, process models are an excellent starting point for process analysis. However, decision support systems in BPM must guide process analysts even further in their search for per formance issues such as bottlenecks or rework.

Existing studies on process model-based analysis have tried to incorporate this aspect. Seeliger et al. [40] presented ProcessExplorer to suggest similar subsets of the process to the analyst. However, whilst recommendations were shown next to the process model, the process model itself was not enriched. Mannhardt [41] presented a multiperspective process explorer allowing for the projection of performance statistics onto the process model. However, the performance statistic solely relied upon frequency and were not learned. An example of pro cess model-based analysis was presented by van Eck et al. [9], who designed an extension of their composite state machine miner, a process discovery technique. They coloured the process nodes according to their degree of artefact interaction; that is, the (‘correlations between sets of artefact states or transitions’ [9]). However, their technique did not directly permit root cause analysis with respect to performance in dicators. Furthermore, the authors stated a limitation of their study: they did not evaluate their work with domain experts. We provide thi evaluation via our case study.

To bridge the gap between process discovery and process analysis, we developed GRM as a process model-based analysis technique, to identify the relevance of process activities with respect to a business goal (i.e., a process outcome). The quantitative evaluation of GRM ensures trust in the validity of the relevance scores. GRM provides a reasonable predictive quality, because it can compete against state-of-the-art techniques for process outcome prediction. We were able to demon strate the impact of process activities that were identified as more relevant on the predictive quality of the model. As such, we find that using a GNN is not only beneficial because of its ability to reveal rele vance scores but also because it provides good predictive quality; in particular, for imbalanced classification problems. Furthermore, we evaluated GRM via a case study; the results suggest that the relevance scores can help process analysts identify root causes in the process flow

No of Service Orders: 4307, Filter: Repair not on time (Label = 0)

![](/api/attachments/D6JFYNSY/fulltext/images/31d3741fb4e90183064309a3c9fcffcf80952d394536f6a74633d0c45aeba81b.jpg)  
Fig. 6. Process model discovered using pm4py’s DFG miner augmented by GRM’s relevance scores.

and address performance issues.

Besides these contributions, this work also features several limita tions. First, we argued that business process outcomes are imbalanced and that the problematic outcome is typically less frequent. While the case study showed that a violation of this assumption does not neces sarily impact the utility of the relevance scores, it remains an aspect that should be carefully evaluated when applying GRM. Second, we did not further evaluate the impact of incorrect predictions on the relevance scores. Currently, we consider the relevance scores of an instance in the context of the predicted label, and this label may be incorrect. Third, GGNNs are computationally expensive to train. We did not accurately evaluate efficiency; however, from the run-times it was evident that the experiments for the baseline approaches (especially RF) ran significantly faster than those conducted with GRM. As run-time correlates with the model’s size, especially event logs with a large number of different ac tivities will be challenging to handle. Event logs retrieved from current information systems, such as those used in the evaluation, commonly have a manageable amount of activities. The possible increase in event data in the future—e.g., through sensors and improved logging capa bilities—might require a re-evaluation of GRM. Whilst this does not impair the theoretical contributions of our work, it may hinder its adoption in practice.

We see several directions for future research. We presented GRM as a technique to close the gap between process discovery and process analysis. However, we believe that GNNs can be of use in other phases of the BPM life-cycle. Sparse event logs with many different activities pose a challenge for process discovery algorithms in PM as models tend to be complex. The relevance scores could be used as an alternative to com mon threshold parameters for simplifying discovered process model such as fitness [42] or probability [43]. Especially for processes with many different activities, users could filter on those that have been found most relevant by GRM in regards to the defined business goal. Furthermore, the relevance scores could be used as inputs for some of the redesign heuristics proposed by Reijers and Mansar [44]. For example, the heuristic task elimination suggests unnecessary tasks that can be removed from a business process. GRM could indicate irrelevant process activities with respect to a defined process goal. In another work, we have shown how GNNs can provide explainability for pre dictions in the (predictive) monitoring phase [19] of the BPM life-cycle.

We proposed GRM as a technique capable of capturing the semantics of a business process. However, we think that this capability of GNN could be exploited even further. Future work should consider using a formal process model such as a Petri net (instead of a graph) as input. This would allow analysts to determine not only relevance scores for activities but also—for example—transitions that represent decision points in the process. Following this line of thought, GNN could also be used in combination with decision models [45].

Finally, we plan to extend GRM by considering the relevance of contextual attributes of events and process instances alongside the process flow. Contextual information can have a valuable contribution to predictive models [46,49,50]. Potential challenges include incorpo rating context into the GGNN architecture and visualising the contextual attributes in the process model.

## 6. Conclusion

In this paper, we presented GRM, a GNN-based technique for determining activity relevance scores. Our work has important implications for both research and business applications. In term of the academic community, our work is an example of applying ML to PM, to produce results on a process-model level rather than on an instance one [47]. While the latter approach might be suitable for supporting oper ations, process analysts and managers require actionable insights to achieve long-term improvements for business processes [47].

We present a novel method with a problem-focused approach. Our technique requires a business goal to be specified in the form of a per formance measure. The model learns towards this goal rather than using heuristics (e.g., frequency, similarity, or distance measures); such techniques can provide more guidance for a process analyst considering a business problem [9].

We envisage major implications for business practice. PM is rapidly gaining momentum in practice. Davenport recently suggested that it might even trigger ‘a new era of process management’ [48]. Most commercial PM vendors seek to bridge the gap between process dis covery and analysis, by adding business intelligence capabilities to their solutions.<sup>5</sup> Several solutions also offer root cause analysis, combined with the deviations identified through conformance checking. Our work highlights the potential of process model-based analysis. Placing the discovered process model at the centre of the analysis facilitates a pro cess-aware analysis of the data.

## Acknowledgement

This work was supported by the German Federal Ministry of Edu cation and Research (BMBF) within the framework programme "Soft ware Campus" (www.softwarecampus.de) [No. 01IS17045].

## References

[1] W.M.P. van der Aalst, M. La Rosa, F.M. Santoro, Business process management: Don't forget to improve the process!. BISE 58 (2016) 1–6.

[2] M. Rosemann. The service portfolio of a BPM CoE, in: J. Vom Brocke. M. Rosemann (Eds.). Handbook on BPM. Springer, 2010. pp. 267–284.

[3] T. Sonteya, L. Seymour, Towards an understanding of the business process analyst,

[4] W.M.P. van der Aalst, Process discovery from event data: relating models and logs through abstractions, in: Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery 8, 2018 (e1244).

[5] D. Beverungen, J. Buijs, J. Becker, C. Di Ciccio, W.M.P. van der Aalst, C. Bartelheimer, V. Wolf, Seven Paradoxes of BPM in a Hyper-Connected World 18, BISE, 2020.

[6] J. Becker, M. Kugeler, M. Rosemann, Process Management: A Guide for the Design of Bps, Springer, 2003, https://doi.org/10.1007/978-3-540-24798-2.

[7] M. Dumas, M. La Rosa, J. Mendling, H.A. Reijers, Fundamentals of BPM, Springer, Berlin. Heidelberg, 2013. https://doi org/10.1007/978-3-642-33143-5

[8] A. del Río-Ortega, M. Resinas, C. Cabanillas, A. Ruiz-Cort´es, On the definition and design-time analysis of PPIs, Inf. Syst. 38 (2013).

[9] M.L. van Eck, N. Sidorova, W.M.P. van der Aalst, Guided interaction exploration and performance analysis in artifact-centric process models, BISE 61 (2019) 649–663.

[10] C.M. Bishop, Pattern Recognition and Machine Learning, Springer, 2006.

[11] Y. LeCun, Y. Bengio, G.E. Hinton, Deep Learning, Nature 521, 2015.

[12] J. Evermann, J.-R. Rehse, P. Fettke, Predicting process behaviour using deep learning, Decis. Support. Syst. 100 (2017) 129–140.

[13] N. Mehdiyev, J. Evermann, P. Fettke, A novel business process prediction model using a deep learning method. BISE 62 (2020) 143–157.

[14] W. Kratsch, J. Manderscheid, M. Roglinger, ¨ J. Seyfried, Machine learning in business process monitoring, BISE 31 (2020) 686.

[15] D. Castelvecchi, Can we open the black box of AI? Nat. News 538 (7623) (2016) 20.

[16] F. Scarselli, M. Gori, A.C. Tsoi, M. Hagenbuchner, G. Monfardini, The GNN model, JEEE Trans. Neural Netw. 20 (2008) 61–80.

[17] J. Zhou, G. Cui, Z. Zhang, C. Yang, Z. Liu, L. Wang, C. Li, M. Sun, GNNs: A Review of Methods and Applications, arXiv:1812.08434. 2018.

[18] Y. Li, D. Tarlow, M. Brockschmidt, R.S. Zemel, Gated graph sequence neural networks, in: Y. Bengio, Yann LeCun (Eds.), Proceedings of the 4th International Conference on Learning Representations (ICLR), 2016.

[19] M. Harl, S. Weinzierl, M. Stierle, M. Matzner, Explainable predictive business

[20] S.T. March. G.F. Smith. Design and natural science research on informatior technology, Decis. Support. Syst. 15 (1995) 251–266

[21] M. Polato, A. Sperduti, A. Burattin, M. de Leoni, Data-aware remaining time prediction of bps instances, in: Int. Joint Conference on NNs, 2014.

[22] J. Gilmer, S.S. Schoenholz, P.F. Riley, O. Vinyals, G.E. Dahl, Neural message passing for quantum chemistry, in: 34th International Conference on Machine Learning (ICML) 70. PMLR. 201Z, pp. 1263–1272

[23] K. Cho, B. van Merri¨enboer, C. Gulcehre, D. Bahdanau, F. Bougares, H. Schwenk Y. Bengio, B. van Merrienboer, Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation. arXiv:1406.1078. 2014.

[24] B.F. van Dongen, W.M.P. van der Aalst, Multi-phase process mining: Building instance graphs, in: 23rd International Conference on Conceptual Modeling (ER2004) 3288, 2004, pp. 362–376.

[25] C. Diamantini, L. Genga, D. Potena, W.M.P. van der Aalst, Building instance graphs for highly variable processes, Expert Syst. Appl. 59 (2016) 101–118.

[26] D.E. Rumelhart, G.E. Hinton, R.J. Williams, Learning representations by back propagating errors, Nature 323 (1986) 533–536.

[27] P. Frasconi, Y. Bengio, P. Simard, P. Frasconi, Learning long-term dependencies with gradient descent is difficult, IEEE Trans. Neural Netw. 5 (1994) 157–166.

[28] M. Du, N. Liu, X. Hu, Techniques for interpretable machine learning, Commun. ACM 63 (2019) 68–77

[29] J. Wang, D. Yu, C. Liu, X. Sun, Outcome-oriented predictive process monitoring with attention-based bidirectional LSTM neural networks, in: 17th International Conference on Web Services, IEEE, 2019, pp. 360–367.

[30] A. Senderovich, C. Di Francescomarino, C. Ghidini, K. Jorbina, F.M. Maggi, Intra and inter-case features in predictive process monitoring, in: Internationa Conference on BPM, Springer, 2017, pp. 306–323.

[31] I. Teinemaa, M. Dumas, M. La Rosa, F.M. Maggi, Outcome-oriented predictive process monitoring: review and benchmark, in: ACM Transactions on Knowledge Discovery from Data (TKDD) 13, 2019, pp. 1–57.

[32] M. Hinkka, T. Lehto, K. Heljanko, A. Jung, Classifying process instances using recurrent neural networks, in: International Conference on Business Process Management, Springer, 2018, pp. 313–324.

[33] M. Sokolova, G. Lapalme. A Systematic Analysis of Performance Measures for Classification Tasks, Information Processing & Mgmt, 2009, pp. 427–437.

[34] J. Demˇsar, Statistical comparisons of classifiers over multiple data sets, J. Mach. Learn. Res. (2006) 1–30.

[35] S.J. Leemans, E. Poppe, M.T. Wynn, Directly follows-based process mining, in: International Conference on Process Mining, 2019. IEEE.

[36] B.F. van Dongen, BPI Challenge 2017, 2017, https://doi.org/10.4121/UUID: 5F3067DF-F10B-45DA-B98B-86AE4C7A310B.

[37] B.F. van Dongen, F. Borchert, BPI Challenge 2018, 2018, https://doi.org/10.4121 UUID:3301445F-95E8-4FF0-98A4-901F1F204972.

[38] B.F. van Dongen, BPI Challenge 2020, 2020, https://doi.org/10.4121/UUID: 52FB97D4-4588-43C9-9D04-3604D4613B51

[39] M. Stierle, M. Matzner, Customer Service - Device Repair Process (sp2020), 2020, https://doi.org/10.5281/zenodo.3928487.

[40] A. Seeliger, A. S´anchez Guinea, T. Nolle, M. Mühlhauser, ¨ ProcessExplorer: intelligent process mining guidance, in: International Conference on BPM, Springer, 2019, pp. 216–231.

[41] F. Mannhardt. Multi-Perspective Process Mining, Ph.D. Thesis, Technical University of Eindhoven. Eindhoven, Netherlands. 2018.

[42] J.C. Buijs, B.F. van Dongen, W.M. van der Aalst, Quality dimensions in process discovery, Int. J. Coop. 23 (2014). IS

[43] D. Breuker, M. Matzner, P. Delfmann, J. Becker, Comprehensible predictive models for business processes, MIS O. 40 (2016) 1009–1034.

[44] H.A. Reijers, S.L. Mansar, Best practices in business process redesign, Omega 3 (2005) 283–306.

[45] F. Hasi´c, J. de Smedt, J. Vanthienen, Augmenting Processes with Decision Intelligence, Decision Support Systems 107, 2018.

[46] A.E. Marquez-Chamorro, ´ M. Resinas, A. Ruiz-Cort´es, Predictive Monitoring of Bps: A Survey, JEEE Transactions on Services Computing 11. 2017

[47] G. Park, M. Song, Predicting performances in business processes using deep neural networks, Decis. Support. Syst. 129 (2019) 113191.

[48] T. Davenport, Process Mining: from Analytics to Action, Forbes, 2020 https://bit. ly/3kkMo0E.

[49] J. Brunk, M. Stierle, L. Papke, K. Revoredo, M. Matzner, J. Becker, Cause vs. effect in context-sensitive prediction of business process instances, Information Systems 95 (2021). 101635

[50] J. Brunk, J. Stottmeister, S. Weinzierl, M. Matzner, J. Becker, Exploring the effect of context information on deep learning business process predictions, J. Decis. Syst. (2020).

Matthias Stierle is a researcher at the Chair of Digital Industrial Service Systems at Friedrich-Alexander-Universitat ¨ Erlangen-Nürnberg, Germany. His research interests include business process management with a focus on analytical topics including process mining. He has participated in several research proiects funded by the European Union and by the German Federal Ministry of Education and Research (BMBF).

Sven Weinzierl received his M.Sc. degree in 2018 at the faculty of Information Systems and Applied Computer Science at the Otto-Friedrich-Universitat ¨ Bamberg, Germany. He is currently a researcher and PhD candidate at the Chair of Digital Industrial Service Systems, Friedrich-Alexander-Universitat ¨ Erlangen-Nürnberg, Germany. His research focuses on the application of machine learning, particularly deep learning, in the field of business process management.

Maximilian Harl is a research assistant at the Chair of Digital Industrial Service Systems at Friedrich-Alexander-Universit¨at Erlangen-Nürnberg, Germany. His research interests include deep learning - in particular, graph neural networks. He has participated in research projects funded by the German Federal Ministry of Education and Research (BMBF).

Martin Matzner holds the chair of Digital Industrial Service Systems at Friedrich-Alex ander-Universit¨at Erlangen-Nürnberg, Germany. In 2012, he received his Ph.D. in information systems from the University of Münster for his work on the management of networked service business processes. His research areas include business process man agement, business process analytics, as well as service engineering and service manage ment. In these areas, he concluded and currently manages several research projects funded by the European Union, by the German Federal Government and by industry. He has published more than 90 research papers and articles, among others in MIS Quarterly, Business & Information Systems Engineering and IEEE Transactions on Engineering Management. He is editor of the Journal of Service Management Research.

---
otero_id: 19696
otero_key: "AX53AUW7"
title: "Process data properties matter: Introducing gated convolutional neural networks (GCNN) and key-value-predict attention networks (KVP) for next event prediction with deep learning"
authors: "Kai Heinrich; Patrick Zschech; Christian Janiesch; Markus Bonin"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113494"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
![](/api/attachments/AX53AUW7/fulltext/images/6a0665da7245c6e62135d0c2c2ea6a39b001255048eddd6cdd6620ff1585a0cf.jpg)

# Process data properties matter: Introducing gated convolutional neural networks (GCNN) and key-value-predict attention networks (KVP) for next event prediction with deep learning

Kai Heinrich <sup>a,b</sup>, Patrick Zschech <sup>c</sup>, Christian Janiesch <sup>d,\*</sup>, Markus Bonin <sup>e</sup>

<sup>a</sup> Otto-von-Guericke-Universitat ¨ Magdeburg, Universitatsplatz ¨ 2, 39106 Magdeburg, Germany

<sup>b</sup> Technische Universitat ¨ Dresden, Helmholtzstraße 10, 01069 Dresden, Germany

<sup>c</sup> Friedrich-Alexander-Universitat ¨ Erlangen-Nürnberg, Lange Gasse 20, 90403 Nürnberg, Germany

<sup>d</sup> Julius-Maximilians-Universitat ¨ Würzburg, Sanderring 2, 97084 Würzburg, Germany

<sup>e</sup> Capgemini Deutschland GmbH, L¨offelstraße 46, 70597 Stuttgart

## A R T I C L E I N F O

Keywords: Process mining Predictive process monitoring Machine learning Deep learning Gated convolutional neural network Key-value-predict attention network

## A B S T R A C T

Predicting next events in predictive process monitoring enables companies to manage and control processes at an early stage and reduce their action distance. In recent years, approaches have steadily moved from classical statistical methods towards the application of deep neural network architectures, which outperform the former and enable analysis without explicit knowledge of the underlying process model. While the focus of prior research was on the long short-term memory network architecture, more deep learning architectures offer promising extensions that have proven useful for other applications of sequential data. In our work, we introduce a gated convolutional neural network and a key-value-predict attention network to the task of next event pre diction. In a comprehensive evaluation study on 11 real-life benchmark datasets, we show that these two novel architectures surpass prior work in 34 out of 44 metric-dataset combinations. For our evaluation, we consider the effects of process data properties, such as sparsity, variation, and repetitiveness, and discuss their impact on the prediction quality of the different deep learning architectures. Similarly, we evaluate their classification prop erties in terms of generalization and handling class imbalance. Our results provide guidance for researchers and practitioners alike on how to select, validate, and comprehensively benchmark (novel) predictive process monitoring models. In particular, we highlight the importance of sufficiently diverse process data properties in event logs and the comprehensive reporting of multiple performance indicators to achieve meaningful results.

## 1. Introduction

Predictive process monitoring (PPM) aims to provide timely infor mation about running process instances to identify risks and issues before or while they develop [1]. In this way, companies can derive recommendations for action to manage and control processes at an early stage [2] and reduce their action distance [3]. Depending on the monitoring focus and the richness of event data, PPM approaches sup port a variety of prediction tasks, such as forecasting remaining cycles times [4] or predicting next events in running process instances [5].

Prediction tasks are realized by methods from the fields of statistics and machine learning (ML) [6]. In ML, the focus is increasingly on artificial neural networks (ANN) that are organized in deep network architectures consisting of multiple processing layers. This allows ANNs to automatically process raw input data without manual feature engi neering and learn patterns that are relevant for prediction tasks, which is commonly known as deep learning (DL). With this functionality, advanced DL networks are exceedingly outperforming classic ML tech niques as well as statistical approaches, especially in tasks related to large and high-dimensional data, for example, in natural language processing (NLP) and computer vision [7]. In PPM, we face a similar development for predicting process behavior. While the first approaches focused on classical methods like hidden Markov models and support vector machines, recent work is steadily moving towards the application of DL models [e.g., [1,5]]. We observe considerable performance im provements for several prediction tasks such as outcome classification

[8] and next event prediction [9].

DL models come in different architectural variants that are mostly characterized by the type of processing units, layers, and connections they use [e.g., [10,11]]. Depending on the properties of the input data, the network architecture determines how relevant structures are auto matically recognized by the model. The predominant type in the field of PPM is that of recurrent neural networks (RNN). This type of network is explicitly designed for sequential data properties present in process structures and the underlying event logs. Recurrent architectures offer internal feedback loops and therefore enable sequential pattern learning to model time dependencies by forming a memory. Motivated by the achievements in NLP, Evermann, et al. [5] were among the first to introduce a long short-term memory (LSTM) network as a particular type of RNN to the field of PPM. Much of the subsequent work at the intersection of PPM and DL was based on LSTMs, and researchers referred to it as a reference architecture for proposing further modifi cations or for adapting it to a variety of different PPM tasks [e.g., [12,13–18]]. Apart from this, only a few architectural DL alternatives have been proposed and tested in comprehensive evaluation studies with competitive results. Some of these exceptions are stacked autoen coders [9], memory-augmented networks [19], and convolutional neu ral networks (CNN) [20,21]. These examples emphasize that while LSTM is the predominant DL architecture today, it is by no means without competition. Prediction performance rather depends on the triangle of architecture, dataset, and hyperparameters [22].

Against this backdrop, we argue that there cannot be a silver bullet architecture for all circumstances. Instead, it rather requires a closer look at the properties of the process data in the corresponding event logs to choose the DL architecture that is best suited to adequately learn and capture the structural patterns within the data to make predictions with high quality.

In this work, we introduce two novel DL architectures, which have demonstrated promising results in sequential modeling tasks such as NLP, to the field of PPM and evaluate them with multiple datasets in varying circumstances. The first approach is a gated convolutional neural network (GCNN) as a non-recurrent network alternative. Due to its convolutional layers, the network can learn hierarchical structures in sequences, which are also present in business processes that are subject to non-linear execution patterns. The second approach is a key-valuepredict attention network (KVP). Based on an advanced attention mechanism, the network can capture long-range connections in large sequences, which can also be observed in real-life processes with many involved activities.

In this respect, our contribution is threefold:

1. We introduce GCNN and KVP as two novel DL architectures into the field of PPM, and more specifically, the task of predicting next events in running instances based on past activities.

2. We conduct a comprehensive evaluation study based on 11 real-life benchmark datasets using multiple established evaluation metrics for assessing the multi-class prediction task.

3. We demonstrate that our approaches show competitive prediction results and exceed existing DL approaches for next event prediction on most datasets with regard to different evaluation metrics. We discuss the circumstances in which the individual DL architectures unfold their benefits

Our article is structured accordingly: First, we discuss related work on predictive process monitoring and next event prediction in Section 2. Subsequently, we go into more details about previously applied DL ar chitectures and outline GCNN and KVP as novel architectures in Section 3. In Section 4, we describe our study design, followed by the presen tation of the results in Section 5. We summarize our findings and highlight potential for future work in Section 6.

## 2. Related work

Predictive process monitoring covers a variety of tasks, mainly expressed by the target to be predicted. Thus, related work can be found for performance predictions of remaining cycle times, delays, and next timestamps [e.g., [4,23,24]], predictions of partial or final process outcomes [e.g., [8,25,26]], the anticipation of business rule violations [e.g., [27,28]], anomaly classification [e.g., [29]], predictions regarding the next event [e.g., [5,9,13]] or a sequence of next events [e.g., [2]], and prediction-based resource allocation [e.g., [30]].

In this paper, we focus on the task of next event prediction in running process instances using previous activities, based on historical execution and context data recorded in event logs. This is an important task in PPM as it allows business analysts to proactively intervene and prevent un desired behavior in case of anticipated deviations in a timely manner [9]. The task has received special attention in recent years by re searchers across different disciplines and is a valuable basis when introducing and comparing novel approaches into the field of PPM [1].

Traditionally, approaches for next event prediction largely relied on explicit process representations, that is, process models. For example, Breuker, et al. [31] proposed a probabilistic finite automaton (RegPFA) based on Bayesian regularization to derive a process model that can be used for predicting future behavior. The authors evaluated their approach with two publicly available data collections from the BPI Challenges 2012 (BPI’12) [32] and 2013 (BPI’13) [33], providing a baseline for benchmark purposes. Other exemplary approaches in this context cover state-transition models [34], sequential pattern mining [35], and hidden Markov models [e.g., [36,37]]. However, such ap proaches generally face the limitation that they rely on restrictive as sumptions given by the explicit process representation [5].

Recent work is steadily moving away from explicit models towards DL approaches due to their capability of automated representation learning and superior prediction results [9]. The focus of this develop ment is primarily on recurrent architectures and especially LSTMs as a subtype of RNNs (cf. Section 3 for further details). One of the first LSTMs was introduced by Evermann, et al. [5], consisting of an embedding layer for transforming event log features into a vector space and two subsequent LSTM layers for predicting upcoming events. Subsequently, Tax, et al. [13] proposed a network for multi-task prediction that con sisted of three LSTM layers: an event prediction layer, a timestamp prediction layer, and a shared layer. Input features were transformed via one-hot encoding. Camargo, et al. [12] extended this approach by pro posing a multi-task network with four LSTM layers for predicting the upcoming events, their timestamps, and associated resource attributes. Event and resource inputs were encoded with separate embedding layers. Both, Tax, et al. [13] and Camargo, et al. [12] evaluated thei approaches with a BPI’12 subset and an additional event log from a ticketing system called Helpdesk [38]. Further LSTM variants were proposed by Tello-Leal, et al. [15] as well as Schonig, ¨ et al. [14]. The former introduced a network with a single LSTM layer, whereas the latter considered two LSTM layers for predicting next events in combi nation with related resource information.

Apart from LSTMs, only few architectural alternatives have been considered for next event prediction. Hinkka, et al. [39] considered an RNN with gated recurrent units (GRU). Such units consist of a cell structure that is less complex in contrast to LSTM cells [40]. Khan, et al. [19] use a memory-augmented neural network (MANN) with external memory units for enhanced learning capabilities of long sequences as compared to conventional LSTMs. Lin, et al. [41] introduced MM-Pred using a modulator, which customizes weights for events and their at tributes, to combine separately encoded events and their attributes for PPM.

In contrast to recurrent architectures, Mehdiyev, et al. [9] proposed a network that consists of two stacked autoencoders (SAE) for dimen sionality reduction and unsupervised feature learning, followed by a multi-layer perceptron with two hidden layers for activity prediction.

Input events are encoded into n-grams in combination with feature hashing to receive a reasonable vector size. The approach is compre hensively evaluated and compared to related work using samples from the Helpdesk, BPI’12, and BPI’13 datasets. Moreover, Di Mauro, et al. [21] and Pasquadibisceglie, et al. [20] introduce a CNN. While the former proposed a network with one embedding layer and three stacked CNN inception modules, the latter applied a CNN with three convolu tional blocks to process a spatial representation of event log traces using a frequency-based encoding of activities and timestamps.

## 3. Deep learning architectures

Prior work has extended existing networks continuously and evalu ated the results on benchmark datasets. However, little attention has been paid to the underlying properties of process data to discuss and select DL architecture for application given the specific properties of a dataset. In this section, we explain the structure of established DL ar chitectures and introduce novel approaches relevant to PPM.

## 3.1. Recurrent neural networks and long short-term memory networks

ANNs consist of connected processing units $( \mathrm { i . e . } ,$ , cells) that are organized into networks with multiple layers, including an input layer, one or more hidden layers, and an output layer. Processing units are coupled by weighted connections to other units from previous and subsequent layers in different forms. This gives ANNs the flexibility to come in various architectures and allows them to be modified for a variety of contexts and learning tasks [e.g., [10,11]].

RNNs are a particular type of ANN that specialize in processing sequential data structures such as time-series data and natural language. More specifically, each cell of an RNN is not only connected to a sub sequent layer but also feeds information back into itself to maintain a state over time, which serves as a memory to capture time dependencies. The extent of this memory can be specified by the number of time steps to be considered for processing sequences of inputs with variable length. However, classic RNN architectures have difficulties in the training procedure when the data involves long-term dependencies. Due to the problem of vanishing gradients in the training phase, the magnitude of weights assigned to distant events from the beginning of the sequence decrease rapidly so that the model may fail to consider those events during prediction [5].

LSTMs address this problem by introducing advanced long-term memory cells based on gating components with forget functions for unimportant parts and emphasize functions for important parts of the sequence. In this way, the network can control which information will be forgotten and which information will be maintained for long periods of time [42].

As described in the previous section, LSTMs are organized in different layers, mostly depending on the target(s) to be predicted and the type of feature encoding. Since ANNs operate on real-valued data, event log features need to be encoded accordingly. A common option is to use embeddings as an input layer by which events and related attri butes are first transformed into an n-dimensional vector space and subsequently processed by one or more LSTM layers. Alternatively, input data can be transformed into a feature vector via one-hot-encoding that is directly fed into the LSTM. However. this results in large feature vectors and correspondingly large network layers in case of event logs with many process activities [5].

## 3.2. Gated convolutional neural networks

A GCNN is a non-recurrent network alternative to capture long-term dependencies while avoiding sequential operations for better paral lelizability. Thus, recurrent connections typically applied in RNNs are replaced by gated temporal convolutions. In general, convolutional operations are responsible for hierarchical feature learning. For this purpose, multiple convolutional layers are stacked into a network to extract hierarchical structures over increasingly larger contexts with more abstract features. In this way, long-term dependencies can be modeled over a context of size N and kernel width k [43].

To overcome the problem of vanishing gradients, GCNNs contain gating mechanisms like those introduced by LSTMs. More specifically, gated linear units (GLU) are employed to keep control over the infor mation that should be propagated through the hierarchy of layers. Additionally, convolutions and GLUs can be wrapped in residual blocks adding the input of the block to the output for further mitigation of the degradation problem [44]. Since GCNNs have demonstrated state-ofthe-art results in the field of NLP [43,45], we assume that they have the potential to advance PPM as well. In this work, we adopt the approach proposed by Dauphin, et al. [43] and apply it to next event prediction.

Formally speaking, the GCNN should produce a representation $H =$ $[ h _ { 0 } , . . . , h _ { N } ]$ of the context for each event $w _ { 0 } , . . . ,$ w to predict the next event $P ( w _ { i } | h _ { i } )$ . This is done by convolving the inputs with a function f to obtain $H = f ^ { * }$ w. The input of the network is a sequence of events $w _ { 0 } , . . . ,$ w represented by embeddings $E = [ D _ { w 0 } , . . . , D _ { w N } ]$ . The hidden layers of the network $h _ { 0 } , . . . , h _ { L }$ are computed as follows

$$
h _ {l} (X) = \left(X ^ {*} W + b\right) \otimes \sigma \left(X ^ {*} V + c\right)\tag{1}
$$

where $m ,$ n are respectively the number of input and output feature maps, k is the patch size, $\ b X \in \mathbb { R } ^ { \mathbf { N } \times \mathbf { m } }$ is the input of layer $h _ { l } , W \in \mathbb { R } ^ { k \times m \times n } , k$ $\in \mathbb { R } ^ { n } , V \in \mathbb { R } ^ { k \times m \times n } , c \in \mathbb { R } ^ { n }$ are learned parameters, and σ is the sigmoid function. The output of each layer is a linear projection $X ^ { \ast } \ W + b$ modulated by the gates $\sigma ( X ^ { * } V + c ) .$ . In comparison with a regular CNN that centers a window around a time step, the causal convolution in (1) does not include future time steps in the context, ensuring real predic tion power based on past inputs instead of including future information that will not be present for new data. The gating operation in (1) uses simple sigmoid gating to filter in the important parts of the context that serve as input to the next hidden layer.

## 3.3. Key-value-predict attention networks

Another approach for extending DL architectures for sequential modeling is that of attention mechanisms. Attention layers assist in identifying global dependencies disregarding sequential distance $( \boldsymbol { \mathrm { e . g . } }$ time-based). They consist of context and attention vectors, as well as attention weights. Vaswani, et al. [46] extended attention mechanisms by introducing key-value attention. Later, Daniluk, et al. [47] improved the approach and proposed key-value-predict attention for LSTMs that separates output vectors (2) into a key, a value, and a predict part. The newly introduced attention layer can identify correlations between two elements that have different positions within an input sequence. The context vector contains a summarizing vector that comprises the pre dictions of past iterations. This separation improves the performance for predicting the next token in very large sequences. We adopt their approach for next event prediction and apply the definitions by Daniluk, et al. [47] to augment LSTMs with KVP attention.

Formally speaking, KVP operates as follows: Let $Y _ { t } = [ h _ { t - L } . . . h _ { t - 1 } ]$ be a memory of previous L output vectors of an LSTM unit, where k is the output dimension and $h _ { t }$ is the output representation at time step t. To determine the probability distribution $y _ { t }$ for the next event, the following applies:

$$
\left[ \begin{array}{c} k _ {t} \\ v _ {t} \\ p _ {t} \end{array} \right] = h _ {t} \in \mathbb {R} ^ {3 k}\tag{2}
$$

$$
\mathrm{M} _ {\mathrm{t}} = \phi \left(\mathrm{W} ^ {\mathrm{Y}} \left[ \mathrm{k} _ {\mathrm{t} - \mathrm{L}} \dots \mathrm{k} _ {\mathrm{t} - 1} \right] + \left(\mathrm{W} ^ {\mathrm{h}} \mathrm{k} _ {\mathrm{t}}\right) 1 ^ {\mathrm{T}}\right) \in \mathbb {R} ^ {\mathrm{k} \times \mathrm{L}}\tag{3}
$$

$$
\alpha_ {t} = \operatorname{softmax} \left(\mathrm{w} ^ {\mathrm{T}} \mathbf {M} _ {t}\right) \in \mathbb {R} ^ {1 \times L}\tag{4}
$$

$$
\mathbf {r} _ {\mathrm{t}} = [ \mathbf {v} _ {\mathrm{t-L}}... \mathbf {v} _ {\mathrm{t-1}} ] \mathbf {a} ^ {\mathrm{T}} \in \mathbb {R} ^ {\mathrm{k}}\tag{5}
$$

$$
\mathrm{h} _ {\mathrm{t}} ^ {*} = \phi (\mathrm{W} ^ {\mathrm{r}} \mathrm{r} _ {\mathrm{t}} + \mathrm{W} ^ {\mathrm{x}} \mathrm{p} _ {\mathrm{t}}) \in \mathbb {R} ^ {\mathrm{k}}\tag{6}
$$

$$
\mathrm{y} _ {\mathrm{t}} = \operatorname{softmax} \left(\mathrm{W} ^ {*} \mathrm{h} _ {\mathrm{t}} ^ {*} + \mathrm{b}\right) \in \mathbb {R} ^ {| \mathrm{V} |}\tag{7}
$$

with $\boldsymbol { W } ^ { Y } ,$ $\boldsymbol { W } ^ { h } ,$ , W<sup>r</sup>, $\boldsymbol { W } ^ { \boldsymbol { x } } \in \mathbb { R } ^ { k \times k }$ \*4 $W ^ { \ast } \in \mathbb { R } ^ { | V | \times k }$ being trainable projection matrices, $w \in \mathbb { R } ^ { k }$ being a trainable vector, $b \in \mathbb { R } ^ { | V | }$ being a bias vector, and $\phi$ being the hyperbolic tangent function. The output vector $h _ { t }$ is divided into three equal parts (2): key $( k _ { t } ) ,$ , value (v ) and predict (p ). $p _ { t }$ is used to encode the next-event distribution, $k _ { t }$ serves as key, and $\nu _ { t }$ serves as value for an attention mechanism. The attention distribution $\alpha _ { t }$ is computed from a comparison of the key at time step t with the previous L keys, which is then used to obtain a weighted context representation $r _ { t }$ ∈ $\mathcal { R } ^ { k }$ from values associated with these keys. The final representation $h _ { t } ^ { * }$ is computed from a non-linear combination of the attention-weighted representation $r _ { t }$ and the respective encoding of the next-event distri bution $p _ { t }$ and subsequently used to predict the next event probability using $y _ { t } .$ In comparison to concurrent context extraction in GCNN, KVP uses a window of the history L, sequentially determining important context events by the comparison in (3) that is used to calculate atten tion weights in (4). The weights then serve as input to (5) resulting in weighted context values, so that only the important context information is passed through to be used in the subsequent prediction (6) and (7).

## 4. Study design

Our study design generally follows that of existing studies on next event prediction to ensure comparability of the results [5,9]. That is, we use the same publicly available benchmark datasets, apply established evaluation metrics for multi-class prediction, and compare our results to related work. However, we deviate from previous studies as we go into further details about relevant circumstances and discuss process data properties with respect to the suitability of the novel architectures.

## 4.1. Datasets and subsets

We used five different dataset collections of real-life event logs for our evaluation: BPI’11 [48], BPI’12 [32], BPI’13 [33], Helpdesk [38], and EnyLog [49]. On the one hand. we considered these datasets because they are widely used for benchmark purposes in the field of PPM [5,9]. On the other hand, we looked for datasets that support a wider range of circumstances regarding their process data properties. Based on those datasets, we additionally consider two typical set of actions per formed on process data:

• Process data focusing. Limiting the database by only focusing on selected process instances or subprocesses of the top-level process,

• Process data augmentation. Enriching the database by augmenting it with additional activity and/or instance attributes.

We summarize the properties of the top-level datasets used in this study, along with their focusing subsets in Table 1. The metrics to describe process data properties are the number of process instances (#I), the number of unique process variants (#V), the number of events (#E), the number of activity types (#A), minimum, average, and maximum statistics of events and activity types per instance, activity-to instance ratio (sparsity), variant-to-instance ratio (variation), and average-based event-to-activity ratio (repetitiveness).

In the following, we describe the chosen datasets in more detail:

• BPI’11 contains event logs from process executions related to cancer treatments of patients in the Gynecology department of a Dutch ac ademic hospital. Each process instance is related to the treatment of one patient.

• BPI’12 comprises data from a loan application process of a large Dutch financial institute. For focusing, the process can be divided into three subprocesses related to the work (W), the application (A), and the offer (O) of the loan application process. Additionally, the W process contains three different lifecycle transitions, schedule, start, and complete (Cmpl), whereas A and O only contain events with the lifecycle transition complete. Analogous to $[ 5 , 9 , 1 3 ]$ , BPI’12 can be considered as multiple subsets with varying circumstances. Furthermore, for augmentation purposes, the dataset can be enriched by activity attributes (e.g., organizational resources executing an activity (org:resource)), and instance attributes (e.g., amount of requested loan (amnt\_req)).

• BPI’13 comprises event logs of an incident and problem manage ment system at Volvo IT in Belgium. The event logs can be divided into two separate subsets handling incidents and problems indepen dently. Analogous to $[ 5 , 8 , 9 ]$ , problem cases can be separated into open and closed problems for focusing purposes. For augmentation purposes, the subsets can be enriched by additional attributes as well.

• Helpdesk contains events from an Italian software company and details the processes of a ticketing system of an IT helpdesk. It has been used widely for evaluation purposes [9,13,19–21] and does not contain any further attributes besides case and activity number as well as a timestamp.

• EnvLog contains data from an environmental building permit application process (‘WABO’) from five different anonymous Dutch municipalities. The events of the five processes are comparable, as the same labels were used across all five municipalities. For augmentation purposes, the dataset can be enriched with attributes at different levels (e.g., human resource involved (org:resource)).

## 4.2. Process data properties

In general, process event logs such as the ones summarized in Table 1 exhibit certain properties affecting next event prediction performance in critical ways. Since these properties can be determined prior to the analysis, they enable the suggestion of appropriate DL architecture based on dataset properties. Kratsch, et al. [8] propose three process data properties that can affect DL model performance substantially. For our analysis, we specifically focus on two of these (variation and repetitive ness). Following [2], we take a more general stance on the process data property sparsity as the ratio between activity labels and traces rather than solely considering payload attributes:

Table 1  
Selected datasets and process data properties.

<table><tr><td>Dataset</td><td>Instances (#I)</td><td>Variants (#V)</td><td>Events (#E)</td><td>Activities (#A)</td><td>min/avg/max E per I</td><td>min/avg/max A per I</td><td>Sparsity</td><td>Variation</td><td>Repetitiveness</td></tr><tr><td>BPI&#x27;11</td><td>1143</td><td>981</td><td>150,291</td><td>624</td><td>1/131/1814</td><td>1/33/113</td><td>0.5459</td><td>0.8583</td><td>3.97</td></tr><tr><td>BPI&#x27;12 (all events)</td><td>13,087</td><td>4366</td><td>262,000</td><td>36</td><td>3/20/175</td><td>3/12/32</td><td>0.0028</td><td>0.3336</td><td>1.67</td></tr><tr><td>BPI&#x27;12Cmpl</td><td>13,087</td><td>4336</td><td>164,506</td><td>23</td><td>3/13/96</td><td>3/8/20</td><td>0.0018</td><td>0.3313</td><td>1.63</td></tr><tr><td>BPI&#x27;12WCmpl</td><td>9658</td><td>2263</td><td>72,413</td><td>6</td><td>1/7/74</td><td>1/2/6</td><td>0.0006</td><td>0.2343</td><td>3.50</td></tr><tr><td>BPI&#x27;12A</td><td>13,087</td><td>17</td><td>60,849</td><td>10</td><td>3/5/8</td><td>3/5/8</td><td>0.0008</td><td>0.0013</td><td>1.00</td></tr><tr><td>BPI&#x27;12O</td><td>5015</td><td>168</td><td>31,244</td><td>7</td><td>3/6/30</td><td>3/5/6</td><td>0.0014</td><td>0.0335</td><td>1.20</td></tr><tr><td>BPI&#x27;13Incidents</td><td>7554</td><td>2278</td><td>65,533</td><td>13</td><td>1/9/123</td><td>1/4/9</td><td>0.0017</td><td>0.3016</td><td>2.25</td></tr><tr><td>BPI&#x27;13Problems</td><td>2306</td><td>454</td><td>9011</td><td>7</td><td>1/4/35</td><td>1/3/6</td><td>0.0030</td><td>0.1969</td><td>1.33</td></tr><tr><td>BPI&#x27;13Closed</td><td>1487</td><td>327</td><td>6660</td><td>7</td><td>1/4/35</td><td>1/3/6</td><td>0.0047</td><td>0.2199</td><td>1.33</td></tr><tr><td>Helpdesk</td><td>3804</td><td>154</td><td>13,710</td><td>9</td><td>1/4/14</td><td>1/3/5</td><td>0.0024</td><td>0.0405</td><td>1.33</td></tr><tr><td>EnvLog</td><td>787</td><td>781</td><td>34,848</td><td>331</td><td>2/44/93</td><td>2/44/92</td><td>0.4206</td><td>0.9924</td><td>1.00</td></tr></table>

• Sparsity: A high activity-to-instance ratio can be an issue for process prediction. That is, there are only (relatively) few instances in the dataset to train a model in relation to the complexity of the process resulting in high sparsity because some or even most activities are not instantiated often and, thus, are more difficult to predict. For example, although the average number of activities in the EnvLog dataset is only 44 (compared to 20 for BPI’12), the dataset only provides 787 instances for 331 possible activities resulting in a high sparsity of 0.42, whereas BPI’12 has a comparably low sparsity of 0.0028.

• Variation: The number of observed unique activity combinations measures the variant-to-instance ratio that describes the potential variation in the process data. Low variation indicates standardized process behavior, while high variation indicates highly individual behavior resulting in many variants. While the complexity of the process data in terms of possible activity types and the average number of events can be low, the variation can still be comparably high. For example, the BPI’12WCmpl dataset contains 2263 variants, whereas BPI’12A and BPI’12O comprise 17 and $^ { 1 6 9 , }$ respectively.

• Repetitiveness: The number of loops and iterations, resulting in many repetitions of activities can be expressed by comparing the average number of events with the average number of activities. High event-to-activity ratio processes usually contain few activitie that are repeated often, while a low event-to-activity ratio indicates many specific and rare combinations rather than many loops. How ever, this is not necessarily a sign of standardization, as we can see from EnvLog where we have high variation (0.99) and low repeti tiveness (1.00) compared to BPI’11 with high repetitiveness (3.97), but also a high variation (0.85).

## 4.3. Classification properties and evaluation metrics

To handle stochastic influences when training DL models, for example, due to random parameter initialization and arbitrary order of training samples, we used 10-fold cross-validation to perform our evaluation [5]. The results serve for statistical analyses and classifier comparison [50,51] based on two classification properties.

• Generalization: To assess the classification property of generaliza tion, we provide both training accuracy (Tr) and validation accuracy (Va) results of the cross-validation. In addition, we calculated the metrics of precision, recall, and F1-score for the validation data [52,53].

• Class imbalance: The distribution of activity instances to activity types in a dataset can deviate heavily from a uniform distribution resulting in some rare activities (i.e., classes) with only a few in stances. This potentially signifies the classification property of clas imbalance. Thus, we considered multiple variants of averaging the metrics over all activity classes: i) macro averaging (ma), which does not take the sizes of the l classes into account, ii) micro averaging (mi), which accounts for the difference in class distribution, and iii) a weighted average (w) that is based on the number of class occur rences $s _ { i }$ for each class i in the dataset of size n [9].

We set β = 1.0 for the F1-score. The metrics are calculated using the outputs of the one-vs-all confusion matrix for each class: tp for true positives, tn for true negatives, fn for false negatives, and $f p$ for false positives. Our metrics are defined as follows:

$$
\text { accuracy } = \frac {1}{n} \sum_ {i = 1} ^ {l} s _ {i} \frac {\mathrm{tp} _ {i} + \mathrm{tn} _ {i}}{\mathrm{tp} _ {i} + \mathrm{fn} _ {i} + \mathrm{tn} _ {i} + \mathrm{fp} _ {i}}\tag{8}
$$

$$
\text { precision } _ {\text { weighted }} = \frac {1}{n} \sum_ {i = 1} ^ {l} s _ {i} \frac {t p _ {i}}{t p _ {i} + f p _ {i}}\tag{9}
$$

$$
\text { precision } _ {\text { macro }} = \frac {1}{1} \sum_ {i = 1} ^ {1} \frac {\mathrm{tp} _ {i}}{\mathrm{tp} _ {i} + \mathrm{fp} _ {i}}\tag{10}
$$

$$
\text { precision } _ {\text { micro }} = \frac {\sum_ {i = 1} ^ {l} \mathrm{tp} _ {\mathrm{i}}}{\sum_ {i = 1} ^ {l} (\mathrm{tp} _ {\mathrm{i}} + \mathrm{fp} _ {\mathrm{i}})}\tag{11}
$$

$$
\text { recall } _ {\text { weighted }} = \frac {1}{n} \sum_ {i = 1} ^ {l} s _ {i} \frac {t p _ {i}}{t p _ {i} + f n _ {i}}\tag{12}
$$

$$
\text { recall } _ {\text { macro }} = \frac {1}{1} \sum_ {i = 1} ^ {1} \frac {\mathrm{tp} _ {i}}{\mathrm{tp} _ {i} + \mathrm{fn} _ {i}}\tag{13}
$$

$$
\operatorname{recall} _ {\text { micro }} = \frac {\sum_ {i = 1} ^ {l} \mathrm{tp} _ {\mathrm{i}}}{\sum_ {i = 1} ^ {l} \left(\mathrm{tp} _ {\mathrm{i}} + \mathrm{fn} _ {\mathrm{i}}\right)}\tag{14}
$$

$$
F 1 - \text { score } _ {\text { weighted }} = \frac {(\beta^ {2} + 1) \text { precision } _ {\text { weighted }} * \text { recall } _ {\text { weighted }}}{\beta^ {2} \text { precision } _ {\text { weighted }} + \text { recall } _ {\text { weighted }}}\tag{15}
$$

$$
F 1 - \text { score } _ {\text { macro }} = \frac {(\beta^ {2} + 1) \text { precision } _ {\text { macro }} * \text { recall } _ {\text { macro }}}{\beta^ {2} \text { precision } _ {\text { macro }} + \text { recall } _ {\text { macro }}}\tag{16}
$$

$$
F 1 - \text { score } _ {\text { micro }} = \frac {\left(\beta^ {2} + 1\right) \text { precision } _ {\text { micro }} * \text { recall } _ {\text { micro }}}{\beta^ {2} \text { precision } _ {\text { micro }} + \text { recall } _ {\text { micro }}}\tag{17}
$$

## 4.4. Technical implementations

We set up a development environment in Python using different ML packages and frameworks to implement our study design: OpenXes and NLTK were used for data transformation, Tensorflow and Keras for implementing the DL architectures, Scikit-opt for parameter tuning, and Scikit-learn, Pandas and Seaborn for data management and evaluation [54]. Furthermore, we used the Process Mining Toolkit (ProM) [55] for calculating the descriptive statistics of the event logs in Table 1 and for creating subsets of the BPI’12 and BPI’13 datasets.

For the extraction of features from the event logs, we followed Evermann, et al. [5] and created tokens as a concatenation of activity names (e.g., “Approve Loan”, “Submit Order”), lifecycle transitions (e.g., “Start”, “Complete”), and, for some experiments, additional event attri butes such as organizational resources (e.g., “Unit A”, “Supervisor”). Thus, an exemplary event within a sequence takes the form “Approve Loan–Started–Unit A”, with all unique events that follow this form constituting the vocabulary of an event log.

To instantiate the novel DL architectures of GCNN and KVP. we adapted existing implementations<sup>1</sup> from NLP applications and modified them regarding feature preparation, parameter tuning, and validation procedures. For benchmarking purposes, we reconstructed two addi tional DL networks, which have demonstrated superior prediction performances across a variety of datasets for PPM: an LSTM as intro duced by Evermann, et al. [5] and an SAE as proposed by Mehdiyev, et al. [9].

More specifically, we implemented a GCNN using depth-wise 2D convolution with eleven hidden layers wrapped in a flexible number of residual blocks [1:10]. KVP and LSTM were implemented with up to three hidden RNN layers. All three networks use embedding layers a input for feature encoding. In contrast, the SAE is based on n-grams and feature hashing for feature encoding as proposed by the authors. Since no source code is available for replication, we reconstructed the SAE in an educated guess using a flexible number of hidden layers [3:7].

Regarding further hyperparameters, we kept several of them un changed, as suggested by related work. For several other parameters such as the size of embeddings or the prefix length of preceding event sequences (i.e., sequence length and kernel width for GCNN, number of time steps for LSTM and KVP), we searched optimal settings. Table 2 details the hyperparameters that we considered for optimization. We applied a grid search method using Bayes optimization [56] based on the intervals given in Table 2 and checked if results are close to boundaries to adjust the intervals if necessary. The specifications of all networks can be reviewed in our source code [57].

All networks were trained on a high-performance computing cluster using 64 nodes, each with 2× Intel(R) Xeon(R) CPU E5-E5-2680 v3 (12 cores) @2.50GHz, no multi-threading, 64 GB RAM (2.67 GB per core), 128 GB SSD, 4× NVIDIA Tesla K80 (12 GB GDDR RAM). The training procedure generally covered 100 epochs. However, in most cases, the results converged much faster towards a stable level, especially for datasets with a lower vocabulary (e.g., BPI’12A and BPI’12O). After running all epochs, the model with the best validation accuracy was chosen.

## 5. Results

In the following, we present the results of our experiments in a stepwise manner. First, we compare our results to the related work and outline some tendencies of the networks’ strengths. Subsequently, we go into further detail by providing a statistical model comparison and discussing the effects of process data properties on our networks’ pre diction qualities. Thereafter, we consider their classification properties to address dataset challenges. In the last step, we discuss the effects of process data focusing and augmentation. A comprehensive overview of our results with all metrics across all models and datasets can be found in [57].

## 5.1. Comparison with related work

For a comparison with related work, we consider the metrics of accuracy, precision, recall, and F1-score in their weighted forms. Table 3 summarizes the results by reporting mean values and standard de viations for each metric across all folds from cross-validation. Both KVP and GCNN achieve competitive results across all datasets and even surpass prior approaches in 34 out of 44 metric-dataset combinations (KVP in 20, GCNN in 14).

Table 2  
Optimized hyperparameters of the implemented DL architectures.

<table><tr><td>GCNN [43]</td><td>KVP [47]</td><td>LSTM [5]</td><td>SAE [9]</td></tr><tr><td>Residual blocks[1:10]</td><td>Hidden RNN layers [1:3]</td><td>Hidden RNN layers [1:3]</td><td>Hidden layers[3:7]</td></tr><tr><td>Kernel width[3:5]</td><td>Hidden Units[256:612]</td><td>Hidden Units[256:612]</td><td>Hidden units[10:500]</td></tr><tr><td>Sequence length[3:15]</td><td>Time steps [5:30]</td><td>Time steps [5:30]</td><td>Learning rate[0.001:1]</td></tr><tr><td>Minibatch size[20:300]</td><td>Learning rate[0.8:1]</td><td>Learning rate[0.8:1]</td><td>Learning decay[0.8:0.99]</td></tr><tr><td rowspan="4">Embedding size[128:256]</td><td>Keep probability[1:10]</td><td>Keep probability[1:10]</td><td>Momentum[0.7:0.9]</td></tr><tr><td>Batch size [10:30]</td><td>Batch size [10:30]</td><td>Activation [ReLU, Sigmoid]</td></tr><tr><td>Embedding size[256:612]</td><td>Embedding size[256:612]</td><td>Batch size[20:100]</td></tr><tr><td>Attention window[2:6]</td><td></td><td></td></tr></table>

With respect to specific metrics, we can distinguish several ten dencies. When focusing on accuracy as the most commonly reported metric across the related work, GCNN outperforms alternative ap proaches in 6 of 11 datasets. In comparison to previous studies, we can see differences in accuracy of up to 8% (e.g., 7.2% for Helpdesk compared to [21], 8% for BPI’12 compared to [12], 4.9% for BPI’12A compared to [9]). In contrast, when focusing on the F1-score as a weighted mean of precision and recall, KVP is more dominant and ex ceeds the performance of other approaches in 7 out of 11 datasets. Here, we obtain differences of up to 16.8% as observed in the Helpdesk dataset in comparison to [9].

With respect to datasets, we can report some tendencies as well. While GCNN generally performs well across all metrics on BPI’12A and BPI’12O, KVP shows remarkable results on BPI’11 and EnvLog. This demonstrates that there is no silver bullet approach dominating the re sults across all datasets and metrics. It rather requires a closer look at the effects of process data and classification properties on model perfor mance, which we will present in the subsequent sections.

Furthermore, our reconstructed SAE performs rather poorly and the results are generally lower than those reported by Mehdiyev, et al. [9]. An exception is the dataset BPI’12WCmpl where both SAE models are among the best results. Interestingly, this is the only dataset that is characterized by a low degree of sparsity and variation in combination with a high degree of repetitiveness. This indicates that SAE can handle these circumstances exceptionally well. However, due to the poor results of our SAE, we did not include it in the further analyses.

In contrast, we used our LSTM as a baseline for subsequent analyses since the model shows promising results and outperforms other LSTM approaches on several datasets (e.g., Helpdesk compared to [13], BPI’12 compared to $[ 5 , 1 2 ]$ , BPI’13 compared to [5]).

## 5.2. Statistical model comparison and effects of process data properties

To assess our DL models’ prediction qualities in more detail, we performed a statistical model comparison. Hutson [58] suggests that additional statistical testing should be done to underline the comparison efforts for classifiers in any setting. We performed the Iman and Davenport omnibus test followed by the Friedman post hoc test with Bergmann and Hommel’s correction for comparison over all datasets using a significance level of $\alpha = 0 . 0 5 [ 5 1 , 5 9 ]$ . The omnibus test showed significant overall differences for F1-score $( p < 0 . 0 0 0 1 )$ and validation accuracy $( p = 0 . 0 1 )$ . Post hoc analysis on F1-scores, however, only revealed significant differences between GCNN and KVP $( p < 0 . 0 0 1 )$ . Post hoc results for validation accuracy only indicated significant dif ferences between GCNN and LSTM $( p = 0 . 0 2 )$ . As shown in Fig. 1, we can confirm that GCNN performed better on average when only looking at accuracy, which is often considered by practitioners and researchers alike. However, accuracy does not distinguish between positive and negative classes, while the F1-score as a weighted mean between pre cision and recall does [60]. This confirms that prediction methods should not be evaluated by a single metric. Instead, a multi-perspective view is necessary to assess a model’s prediction qualities and its suit ability for the task at hand [52].

Furthermore, we found that GCNN lacks consistency, showing large deviations from its mean, especially when looking at the F1-score, in comparison to LSTM and KVP, which show less deviation. The results concur with the notion that there is no silver bullet algorithm that per forms best in every situation.

To understand the differences in performance, we looked into the different datasets to reveal which process data properties exert certain influences on the prediction qualities of the three DL models. Fig. 2 summarizes the performances in terms of accuracy and F1-score for the six top-level datasets. Several tendencies can be observed. For example, all three models perform equally well with high prediction qualities for

Table 3  
Results obtained in comparison to benchmark approaches.

<table><tr><td>Dataset / Model</td><td>Accuracy</td><td>Precision (w)</td><td>Recall (w)</td><td>F1-score (w)</td></tr><tr><td colspan="5">BPI&#x27;11</td></tr><tr><td>LSTM (ours)</td><td>0.621 ± 0.031</td><td>0.775 ± 0.028</td><td>0.621 ± 0.031</td><td>0.665 ± 0.028</td></tr><tr><td>SAE (ours)</td><td>0.422 ± 0.005</td><td>0.430 ± 0.008</td><td>0.422 ± 0.005</td><td>0.380 ± 0.004</td></tr><tr><td>GCNN (ours)</td><td>0.565 ± 0.077</td><td>0.557 ± 0.018</td><td>0.546 ± 0.016</td><td>0.528 ± 0.017</td></tr><tr><td>KVP (ours)</td><td>0.691 ± 0.032</td><td>0.728 ± 0.016</td><td>0.692 ± 0.021</td><td>0.700 ± 0.018</td></tr><tr><td colspan="5">BPI&#x27;12</td></tr><tr><td>LSTM [5]</td><td>-</td><td>0.859 ± 0.005</td><td>-</td><td>-</td></tr><tr><td>LSTM (ours)</td><td>0.841 ± 0.022</td><td>0.924 ± 0.017</td><td>0.841 ± 0.023</td><td>0.867 ± 0.021</td></tr><tr><td>LSTM [12]</td><td>0.786</td><td>-</td><td>-</td><td>-</td></tr><tr><td>SAE (ours)</td><td>0.690 ± 0.013</td><td>0.745 ± 0.010</td><td>0.690 ± 0.013</td><td>0.684 ± 0.012</td></tr><tr><td>GCNN (ours)</td><td>0.866 ± 0.007</td><td>0.864 ± 0.008</td><td>0.866 ± 0.007</td><td>0.844 ± 0.005</td></tr><tr><td>KVP (ours)</td><td>0.855 ± 0.027</td><td>0.930 ± 0.023</td><td>0.855 ± 0.027</td><td>0.876 ± 0.030</td></tr><tr><td colspan="5">BPI&#x27;12Cmpl</td></tr><tr><td>LSTM [5]</td><td>-</td><td>0.788 ± 0.006</td><td>-</td><td>-</td></tr><tr><td>LSTM (ours)</td><td>0.757 ± 0.020</td><td>0.870 ± 0.013</td><td>0.760 ± 0.003</td><td>0.799 ± 0.006</td></tr><tr><td>SAE (ours)</td><td>0.686 ± 0.004</td><td>0.741 ± 0.005</td><td>0.686 ± 0.004</td><td>0.678 ± 0.004</td></tr><tr><td>GCNN (ours)</td><td>0.805 ± 0.015</td><td>0.807 ± 0.016</td><td>0.805 ± 0.015</td><td>0.769 ± 0.008</td></tr><tr><td>KVP (ours)</td><td>0.756 ± 0.019</td><td>0.875 ± 0.009</td><td>0.759 ± 0.005</td><td>0.800 ± 0.005</td></tr><tr><td colspan="5">BPI&#x27;12WCmpl</td></tr><tr><td>RegPFA [31]</td><td>0.719</td><td>-</td><td>0.578</td><td>-</td></tr><tr><td>LSTM [5]</td><td>-</td><td>0.658 ± 0.020</td><td>-</td><td>-</td></tr><tr><td>LSTM (ours)</td><td>0.648 ± 0.032</td><td>0.805 ± 0.051</td><td>0.665 ± 0.009</td><td>0.715 ± 0.019</td></tr><tr><td>LSTM [13]</td><td>0.760</td><td>-</td><td>-</td><td>-</td></tr><tr><td>LSTM [12]</td><td>0.778</td><td>-</td><td>-</td><td>-</td></tr><tr><td>SAE [9]</td><td>0.831</td><td>0.811</td><td>0.832</td><td>-</td></tr><tr><td>SAE (ours)</td><td>0.807 ± 0.002</td><td>0.794 ± 0.003</td><td>0.807 ± 0.002</td><td>0.795 ± 0.002</td></tr><tr><td>MANN [19]</td><td>0.777</td><td>-</td><td>-</td><td>-</td></tr><tr><td>CNN [20]</td><td>0.782</td><td>-</td><td>-</td><td>-</td></tr><tr><td>GCNN (ours)</td><td>0.765 ± 0.014</td><td>0.773 ± 0.013</td><td>0.765 ± 0.014</td><td>0.710 ± 0.017</td></tr><tr><td>KVP (ours)</td><td>0.645 ± 0.022</td><td>0.829 ± 0.041</td><td>0.662 ± 0.010</td><td>0.723 ± 0.018</td></tr><tr><td colspan="5">BPI&#x27;12A</td></tr><tr><td>RegPFA [31]</td><td>0.801</td><td>-</td><td>0.723</td><td></td></tr><tr><td>LSTM [5]</td><td>-</td><td>0.832 ± 0.010</td><td>-</td><td>-</td></tr><tr><td>LSTM (ours)</td><td>0.813 ± 0.022</td><td>0.912 ± 0.018</td><td>0.817 ± 0.013</td><td>0.848 ± 0.012</td></tr><tr><td>SAE [9]</td><td>0.824</td><td>0.852</td><td>0.824</td><td>0.817</td></tr><tr><td>SAE (ours)</td><td>0.630 ± 0.005</td><td>0.610 ± 0.008</td><td>0.630 ± 0.005</td><td>0.602 ± 0.006</td></tr><tr><td>GCNN (ours)</td><td>0.873 ± 0.015</td><td>0.924 ± 0.005</td><td>0.873 ± 0.015</td><td>0.880 ± 0.010</td></tr><tr><td>GCNN (org: resource)a</td><td>0.877 ± 0.007</td><td>0.918 ± 0.004</td><td>0.877 ± 0.007</td><td>0.882 ± 0.007</td></tr><tr><td>KVP (ours)</td><td>0.824 ± 0.011</td><td>0.915 ± 0.014</td><td>0.823 ± 0.009</td><td>0.853 ± 0.010</td></tr><tr><td colspan="5">BPI&#x27;12O</td></tr><tr><td>RegPFA [31]</td><td>0.811</td><td>-</td><td>0.647</td><td>-</td></tr><tr><td>LSTM [5]</td><td>-</td><td>0.836 ± 0.010</td><td>-</td><td>-</td></tr><tr><td>LSTM (ours)</td><td>0.816 ± 0.016</td><td>0.893 ± 0.013</td><td>0.820 ± 0.010</td><td>0.833 ± 0.011</td></tr><tr><td>SAE [9]</td><td>0.821</td><td>0.847</td><td>0.822</td><td>-</td></tr><tr><td>SAE (ours)</td><td>0.768 ± 0.004</td><td>0.815 ± 0.005</td><td>0.768 ± 0.004</td><td>0.732 ± 0.005</td></tr></table>

Table 3 (continued )

<table><tr><td>Dataset / Model</td><td>Accuracy</td><td>Precision (w)</td><td>Recall (w)</td><td>F1-score (w)</td></tr><tr><td>GCNN (ours)</td><td>0.861 ± 0.008</td><td>0.895 ± 0.006</td><td>0.861 ± 0.008</td><td>0.857 ± 0.008</td></tr><tr><td>GCNN (org: resource) $^a$ </td><td>0.885 ± 0.008</td><td>0.904 ± 0.003</td><td>0.885 ± 0.008</td><td>0.882 ± 0.008</td></tr><tr><td>KVP (ours)</td><td>0.843 ± 0.013</td><td>0.909 ± 0.008</td><td>0.833 ± 0.005</td><td>0.847 ± 0.004</td></tr><tr><td colspan="5">BPI&#x27;13Incidents</td></tr><tr><td>RegPFA [31]</td><td>0.714</td><td>-</td><td>0.377</td><td>-</td></tr><tr><td>LSTM [5]</td><td>-</td><td>0.735 ± 0.044</td><td>-</td><td>-</td></tr><tr><td>LSTM (ours)</td><td>0.697 ± 0.031</td><td>0.793 ± 0.028</td><td>0.698 ± 0.031</td><td>0.734 ± 0.031</td></tr><tr><td>SAE [9]</td><td>0.663</td><td>0.648</td><td>0.664</td><td>0.647</td></tr><tr><td>SAE (ours)</td><td>0.436 ± 0.030</td><td>0.601 ± 0.087</td><td>0.436 ± 0.030</td><td>0.463 ± 0.020</td></tr><tr><td>GCNN (ours)</td><td>0.740 ± 0.044</td><td>0.591 ± 0.011</td><td>0.676 ± 0.009</td><td>0.613 ± 0.011</td></tr><tr><td>KVP (ours)</td><td>0.666 ± 0.030</td><td>0.795 ± 0.037</td><td>0.666 ± 0.030</td><td>0.706 ± 0.027</td></tr><tr><td colspan="5">BPI&#x27;13Problems</td></tr><tr><td>RegPFA [31]</td><td>0.690</td><td>-</td><td>0.521</td><td>-</td></tr><tr><td>LSTM [5]</td><td>-</td><td>0.628 ± 0.086</td><td>-</td><td>-</td></tr><tr><td>LSTM (ours)</td><td>0.649 ± 0.023</td><td>0.811 ± 0.062</td><td>0.648 ± 0.019</td><td>0.699 ± 0.022</td></tr><tr><td>SAE [9]</td><td>0.662</td><td>0.641</td><td>0.662</td><td>-</td></tr><tr><td>SAE (ours)</td><td>0.484 ± 0.045</td><td>0.407 ± 0.031</td><td>0.484 ± 0.045</td><td>0.428 ± 0.020</td></tr><tr><td>GCNN (ours)</td><td>0.654 ± 0.013</td><td>0.668 ± 0.026</td><td>0.654 ± 0.013</td><td>0.631 ± 0.011</td></tr><tr><td>KVP (ours)</td><td>0.650 ± 0.022</td><td>0.828 ± 0.043</td><td>0.648 ± 0.016</td><td>0.702 ± 0.022</td></tr><tr><td colspan="5">BPI&#x27;13Closed</td></tr><tr><td>LSTM (ours)</td><td>0.682 ± 0.024</td><td>0.853 ± 0.064</td><td>0.682 ± 0.025</td><td>0.734 ± 0.025</td></tr><tr><td>SAE (ours)</td><td>0.496 ± 0.042</td><td>0.422 ± 0.027</td><td>0.496 ± 0.042</td><td>0.440 ± 0.018</td></tr><tr><td>GCNN (ours)</td><td>0.665 ± 0.024</td><td>0.641 ± 0.029</td><td>0.665 ± 0.024</td><td>0.642 ± 0.024</td></tr><tr><td>KVP (ours)</td><td>0.680 ± 0.024</td><td>0.870 ± 0.064</td><td>0.680 ± 0.025</td><td>0.741 ± 0.027</td></tr><tr><td colspan="5">Helpdesk</td></tr><tr><td>LSTM (ours)</td><td>0.849 ± 0.019</td><td>0.912 ± 0.008 $^b$ </td><td>0.853 ± 0.009</td><td>0.880 ± 0.009 $^b$ </td></tr><tr><td>LSTM [13]</td><td>0.712</td><td>-</td><td>-</td><td>-</td></tr><tr><td>SAE [9]</td><td>0.782</td><td>0.632</td><td>0.781</td><td>0.711</td></tr><tr><td>SAE (ours)</td><td>0.743 ± 0.009</td><td>0.658 ± 0.014</td><td>0.743 ± 0.009</td><td>0.687 ± 0.012</td></tr><tr><td>MANN [19]</td><td>0.714</td><td>-</td><td>-</td><td>-</td></tr><tr><td>CNN [20]</td><td>0.739</td><td>-</td><td>-</td><td>-</td></tr><tr><td>CNN [21]</td><td>0.785 ± 0.005</td><td>-</td><td>-</td><td>-</td></tr><tr><td>GCNN (ours)</td><td>0.857 ± 0.019</td><td>0.847 ± 0.021</td><td>0.857 ± 0.019</td><td>0.848 ± 0.020</td></tr><tr><td>KVP (ours)</td><td>0.849 ± 0.034</td><td>0.911 ± 0.007 $^b$ </td><td>0.852 ± 0.009</td><td>0.879 ± 0.008 $^b$ </td></tr><tr><td colspan="5">EnvLog</td></tr><tr><td>LSTM (ours)</td><td>0.679 ± 0.016</td><td>0.713 ± 0.016</td><td>0.672 ± 0.012</td><td>0.683 ± 0.013</td></tr><tr><td>SAE (ours)</td><td>0.524 ± 0.003</td><td>0.710 ± 0.005</td><td>0.524 ± 0.003</td><td>0.579 ± 0.004</td></tr><tr><td>GCNN (ours)</td><td>0.615 ± 0.018</td><td>0.636 ± 0.016</td><td>0.615 ± 0.018</td><td>0.595 ± 0.018</td></tr><tr><td>KVP (ours)</td><td>0.776 ± 0.051</td><td>0.806 ± 0.036</td><td>0.782 ± 0.043</td><td>0.787 ± 0.040</td></tr></table>

<sup>a</sup> Further values for process data augmentation can be found in [57].  
<sup>b</sup> We consider LSTM and KVP to perform equally well since LSTM shows higher mean values, while KVP shows lower standard deviations.

![](/api/attachments/AX53AUW7/fulltext/images/aa6f3c1f21109c5c05abe5c02e790bb302db6d62037818a2e3da26bd61071792.jpg)  
Fig. 1. Overall performance of our models.

Summary Boxplots of Validation Accuracy by Dataset  
![](/api/attachments/AX53AUW7/fulltext/images/e88eae4fc4dee3991aa2e554429484776fea103f02371f1cc69bef05945e983c.jpg)

![](/api/attachments/AX53AUW7/fulltext/images/b1859aa6d1bb32e876747a2d8d162635063e3fbd9e40c212f1fc8abc4e8cfb2f.jpg)  
Fig. 2. Model performance by top-level dataset

![](/api/attachments/AX53AUW7/fulltext/images/eb1247f54bf3a365d909190b57f6c53df67099080a4108c78cc53789bad6a1a6.jpg)  
Fig. 3. Model performance by process data properties.

BPI’12 and Helpdesk, both of which show similar characteristics in terms of a low degree of sparsity (0.0028 and 0.0024) and low repeti tiveness (1.67 and 1.33). Likewise, we can see the tendency that KVP outperforms the other two models for BPI’11 and Envlog. Both datasets are subject to a high degree of sparsity (0.55 and 0.42).

By sorting the datasets based on their process data properties such effects can be recognized more clearly. Fig. 3 shows the effects of spar sity, variation, and repetitiveness on model performance. The datasets on the x-axis are sorted in ascending order of the respective property (i.e., in the top-left plot, BPI’12WCompl shows the least amount of sparsity and BPI’11 the highest amount). We find that sparsity and variation affect prediction performance, especially on the extreme ends: GCNN performs well in situations with low sparsity and low variation, as re flected by the datasets BPI’12A and BPI’12O. In contrast, KVP, with its advanced attention mechanism, excels when faced with complex data sets exhibiting high amounts of sparsity and variation (BPI’11, EnvLog). Thus, applying the previously suggested statistical testing procedure, we found that performance differs for high variation and high sparsity (BPI’11, EnvLog) at $p < 0 . 0 0 1$

Looking at the effect of repetitiveness, we found that the model performance can only be significantly distinguished for very high repetitiveness: Considering the BPI’11 dataset with high sparsity, KVP outperforms LSTM and GCNN, with LSTM outperforming GCNN at p < 0.001 when considering accuracy and F1-Score. In the case of the low sparsity dataset BPI’12WCmpl, GCNN outperforms the other models at p < 0.001 when looking at accuracy. Likewise, when comparing the equally low repetitive EnvLog and BPI’12A datasets, we find that the difference in performance stems almost entirely from the EnvLog data set, since in addition to having low repetitiveness, in comparison to BPI’12A, it also has a high sparsity and variation. This leads to the conclusion that the results are rather influenced by sparsity and that the effects can only be observed as interactive components rather than isolated.

## 5.3. Effects of classification properties

Apart from dealing with process data properties, a general hurdle to overcome – especially in multi-class prediction problems – is the pres ence of the classification property class imbalance. Since the datasets show a very heterogeneous class structure, we checked for differences in performance metrics by taking single-class performances into account using macro-scores. Fig. 4 depicts distribution plots of the micro-macrodifference of F1-scores for the six top-level datasets. The individual plots are ordered by average micro-macro-differences. Thus, the largest dif ferences can be observed in Helpdesk and BPI’13Incidents, whereas in

BPI’12 with similar process data properties, the differences are consid erably smaller. This can be explained by the different distributions of the activity classes as shown in Fig. 5, applying the same order of plots. The first few datasets are characterized by an abrupt drop in frequencies with a few dominating activities and many rare activities, while the distribution in datasets like EnvLog and BPI’12 decreases more evenly, resulting in a lower degree of class imbalance.

Although all three models generally have problems with imbalanced data and correctly predicting rare activities, we can observe several tendencies confirming the previously observed benefits of KVP and GCNN (cf. Fig. 4). Thus, it is noticeable that GCNN performs consider ably better in predicting rare activities than its competitors in situations with low sparsity and low variation as represented by Helpdesk (0.0024, 0.04) and BPI’13Problems (0.003, 0.2). In contrast, it performs worse when faced with a high degree of sparsity, as given in BPI’11 (0.546). This is where KVP excels due its advanced attention mechanisms. Thus, even when treating every activity equally independent of its rarity, KVP shows the best performance in both datasets with large sequences and high sparsity (BPI’11, EnvLog) as opposed to LSTM and GCNN. How ever, in the case of EnvLog, the difference in performance is much smaller and less robust in contrast to LSTM since both recurrent models perform equally well on this dataset.

Another issue raised in the context of learning algorithms is the classification property generalization about the quality of the respective algorithm when applied to new data. To measure that quality, we show the distribution of differences between training and validation accuracy for the top-level datasets in Fig. 6. The plots are ordered by average training-validation-difference. While there is barely any difference, or even a negative difference, indicating well generalizable models, for the less complex datasets (BPI’12, Helpdesk, BPI’13Problems, and BPI’13Incidents), we find considerable differences for the complex datasets (BPI’11, EnvLog) that indicate a strong degree of overfitting to the training data. KVP outperforms the other algorithms in BPI’12 and EnvLog. GCNN generalizes well in both BPI’13 datasets while showing worse performance and comparatively large variance when applied to BPI’11. While LSTM tends to overfit for EnvLog, it generalizes well when applied to BPI’11, indicating that LSTM deals well with sparse and re petitive process data in terms of generalization.

## 5.4. Effects of process data focusing and augmentation

First, we consider the effect of process data focusing. As observed in the example of the BPI’12 subsets, different changes in the process data properties may occur after filtering. Thus, subsets can either show an increased or reduced level of complexity as focusing does not necessarily entail a projection and, thus, simplification, but may as well entail the accentuation of already existing process data properties and the reduc tion of training data.

![](/api/attachments/AX53AUW7/fulltext/images/6a7ddb75c1de98f1c20418f7cbd5e0e41c6a9c63e08cba8672d93950a2871da5.jpg)  
Fig. 4. Class imbalance effect by top-level dataset.

Training/Validation Differences for Accuracy  
BPI'13Problems (Skewness: 0.96)  
![](/api/attachments/AX53AUW7/fulltext/images/9f3d4626c2ee2c4077ddc7037ba849558a8e03f5ec7fc56b47406e0f27252b7b.jpg)

![](/api/attachments/AX53AUW7/fulltext/images/a000a29ab014df324fc2707f4ffb13504b4b632e737d9b5ea90b13d082821ab3.jpg)

![](/api/attachments/AX53AUW7/fulltext/images/0c0a8c98548753aeca97a3d2dd6671a7966d67ab8f21e8c03df8c877368e79e2.jpg)

![](/api/attachments/AX53AUW7/fulltext/images/00140f04bd0d08d5e0f25858d2a76119ecbda1c5038b1b40edea54b9cbbf709b.jpg)

![](/api/attachments/AX53AUW7/fulltext/images/fd46ebe9c0fc05fd6882d988369e66464d72048799ba984eecce9c0ffcba56b6.jpg)  
Fig. 5. Activity distribution for selected top-level datasets.

![](/api/attachments/AX53AUW7/fulltext/images/bc14c39f0a65ad4e1a7b5b2a4006b303d8838ed0470f3bbb6e55d11b8acfd1b3.jpg)

![](/api/attachments/AX53AUW7/fulltext/images/98768484fdd62b4d2b173ee5007953105b0ebeebcd0982ddf7e72cf89f7fdc53.jpg)  
Fig. 6. Overfitting effect by top-level dataset.

Comparison of Top-Level Performance with Subsets for BPl'12  
![](/api/attachments/AX53AUW7/fulltext/images/4e46c2d27038ba66efa7b6d3ac3bb9c7cd7cdd47be71afcdad58d7f259fa1d36.jpg)  
Fig. 7. Performance comparison for BPI’12 focusing.

When we look at event sequences with the lifecycle transition com plete as reflected by BPI’12WCmpl and BPI’12Cmpl, the resulting sub sets have a reduced average amount of events. However, they still show a high amount of variation, resulting in a higher degree of complexity (cf. Table 1). Consequently, we encounter decrease in performance for all three models when comparing the results between the subprocesses and the top-level dataset as illustrated in Fig. 7. Nevertheless, there are different tendencies. When only considering accuracy, GCNN out performs the other models at $p < 0 . 0 0 1$ . Contrary, when looking at the F1-score, we find that GCNN performs significantly worse than KVP and LSTM at $p < 0 . 0 0 1$ , while there is no significant difference between KVP and LSTM at $\begin{array} { r } { p = 0 . 0 8 . } \end{array}$ Consequently, we cannot state that any model shows superior performance across both metrics.

When focusing on the subprocesses A and O, on the other hand, we see a strong simplification of the process data properties in terms of much shorter sequences and reduced degrees of sparsity, variation, and repetitiveness. However, instead of witnessing a performance improvement across all three models, only GCNN is capable to benefit from the simplified process structures, whereas LSTM and KVP even perform slightly worse as opposed to the entire dataset of BPI’12 with all events. Consequently, we find that for the subsets A and O, GCNN out performs the other two models at $p < 0 . 0 0 1$ , when considering both accuracy and F1-score, confirming our finding that GCNN excels in sit uation with rather simple process data properties, such as low sparsity and low variation.

Additionally, we also considered a comparison between the BPI’13Problems dataset and the subprocess of closed problems. How ever, no particular tendency could be observed, except that all three models perform slightly better in the subprocess (cf. Table 3) although the properties of the subset show a marginally higher degree of sparsity (0.003 vs. 0.0047) and variation (0.1969 vs. 0.2199).

As a second effect, we examine augmentation by considering addi tional attributes as input for the prediction. As already noted by Ever mann, et al. [5], including attributes may contribute additional information and thus improve predictive power. However, at the same time, this also leads to an increased number of unique tokens resulting in a larger vocabulary (cf. Section 4.4). Thus, predictive performance might be impaired. Consequently, we observed that augmentation could yield improvements but also lead to overfitting. However, the effect differs for the different models and datasets. Fig. 8 shows the augmen tation of BPI’12A and EnvLog with additional attributes as examples fo datasets with low and high complexity.

Considering the activity attribute org:resource for BPI’12A leads to slight improvements for GCNN in terms of accuracy and F1-score, and considerably less performance fluctuations between the folds. However, it slightly decreases the performance for LSTM and KVP (cf. Fig. 8). We observed a similar effect for the datasets BPI’12O and BPI’13Problems for all three models when adding the activity attributes org:res and org: group respectively. In this way, GCNN even achieved the best overall results for BPI’12A (accuracy: 87.7%, F1-score: 88.2%) and BPI’12O (accuracy: 88.5%, F1-score: 88.2%) (cf. Table 3).

Adding the instance attribute amnt\_req to BPI’12A with org:resource causes a major drop in performance for LSTM and KVP and only a slight decrease for GCNN. While GCNN is very stable when adding additional attributes, KVP and LSTM are rather sensitive, resulting in large performance differences when both, org:resource and amnt\_req are added.

When looking at the more complex EnvLog dataset, we encounter an immediate drop in performance for both recurrent approaches, espe cially for KVP that outperforms the other models without augmentation. Contrary, GCNN stays at a similar level and even shows slightly better results than KVP based on the additional attribute.

With regard to the overfitting effect of data augmentation, we show the difference in training and validation accuracy in Fig. 9. The plots indicate that the augmentation of the BPI’12A dataset with amnt\_req leads to overfitting for KVP, while augmentation by both attributes leads to an increased overfitting effect for all three models. In the case of the complex dataset EnvLog, we observe that the generally high effect of overfitting prior to augmentation is, as expected, further intensified and that even the well-performing KVP strongly suffers from this effect when enriching the input.

In summary, we found that GCNN, in contrast to LSTM and KVP, is fairly robust to augmentation and can even improve performance when adding attributes as long as the increase in unique event-attributecombinations is manageable and overfitting is negligible. The effect of better dealing with augmented events can be attributed to the network’s capability of hierarchical feature learning. Starting from specific eventattribute-combinations the network builds increasingly abstract features through the hierarchy of layers. In this way, GCNN can capture sequential structures while using the predictive power of low-level features.

## 6. Discussion and concluding remarks

Our research focused on the performance of different DL architec tures in varying circumstances given by distinct process event logs.

![](/api/attachments/AX53AUW7/fulltext/images/e05fdfb5e09ad3447ff03eb5be3bae2a03833efbbabb584ce6211d322b276827.jpg)  
Fig. 8. Performance comparison for BPI’12A and EnvLog augmentations.

![](/api/attachments/AX53AUW7/fulltext/images/98a252dde2dbed8b1c1f6b9d93daf42b1f5cc2b64010a861038ff6e25a667c78.jpg)  
Fig. 9. Overfitting effect for BPI’12A and EnvLog subsets resulting from augmentations.

Against this backdrop, we have introduced GCNN and KVP as two novel DL architectures into the field of PPM and conducted a comprehensive evaluation study based on 11 real-life benchmark datasets. GCNN and KVP show competitive prediction results and exceed the performance of existing DL models in 34 out of 44 metric-dataset combinations.

As process data properties vary greatly between event logs, our research also shows that it is unlikely that there will ever be a silver bullet approach for next event prediction. Rather, we suppose that the choice of a specific DL architecture should incorporate its capability to deal with process data properties such as sparsity, variation, and repetitiveness.

In this respect, we found that KVP performs particularly well on complex datasets that are subject to a high degree of sparsity and high variation. The network’s superiority in this situation comes with the advanced attention mechanism that separates output vectors into a key, value, and predict part to capture long-range dependencies. Its attention mechanism passes important context through the event sequence by calculating global context weights and, thus, prevents important context from being neglected, even in long sequences. Contrary, GCNN with its capability of hierarchical feature learning excels in situations at the other end of the spectrum. This can be explained by GCNN’s focus on extracting local context at the cost of lacking global attention weighting that result in favorable results for short range dependencies but may be less favorable for long sequences. It outperforms the competitors on datasets with low sparsity and low variation, and it is fairly robust to augmentation when enriching events with additional attributes. The strengths of both networks are also apparent when looking at their capability to predict rare activities as a general challenge when facing class imbalance in event logs. The suitability of both networks for spe cific datasets and the connection of their underlying architectures to prediction quality could be investigated further with a confirmatory explainable artificial intelligence (XAI) study to reveal the detailed weighting process for each prediction.

LSTM’s performance as the most popular DL architecture in PPM often lies between the extrema and offers a robust solution, although it outperforms GCNN and KVP in only 7 of the 44 dataset-metric combi nations. That being said, the same order of magnitude of performance differences cannot be observed for these datasets with mid-level process data properties in terms of sparsity and variation. That is, in these cases, the choice of DL architecture becomes less critical. Lastly, we noticed an indication that the SAE network by Mehdiyev, et al. [9] performs exceptionally well in situations with high repetitiveness while facing a low degree of variation and sparsity. However, this observation could not be further substantiated as our reconstructed SAE generally showed poor prediction qualities and there was no other dataset in our collection covering this combination of process data properties.

At this point, we also see great potential for further investigations. Currently, our focus was on real-life datasets to review the effects of DL architecture choice across various realistic circumstances. For future work, it seems necessary to generate synthetic datasets in which properties like sparsity, variation, and repetitiveness can be adjusted in a controlled fashion to investigate said impact on classifiers. In the meantime, we suggest validating advances in PPM with DL on suffi ciently diverse event logs to avoid only incidental improvements. In this respect, our selection of datasets, including BPI’11, BPI’12, BPI’13, Helpdesk, and EnvLog, could serve as a minimal baseline as they cover a broad spectrum of different process data property combinations.

Moreover, our study shows the importance of reporting multiple metrics to convey an unbiased picture of DL architecture performance. Most of prior studies focus on single metrics to demonstrate the per formance in comparison to related work. However, this might not reveal a classifier’s full prediction qualities and its suitability for a certain task. For example, while our GCNN shows best results in terms of accuracy across of a majority of datasets, its performance is inferior to KVP when considering the balance between precision and recall as measured by the F1-score. Likewise, a single metric is not sufficient to report qualities regarding further classification properties such as class imbalance and generalization. In this sense, our study can serve as an evaluation framework to guide researchers and practitioners alike on how to comprehensively evaluate (novel) PPM approaches.

Naturally, there are some limitations to our work. As Weinzierl, et al. [61] point out, there are situations where encoding may matter more than DL architecture choice. In our work, we did not investigate different encoding options but followed the example of Evermann, et al. [5] by creating event tokens and transforming them into a vector space via embedding layers. Considering the trade-off between generalization and optimization [58], we compromised. We did not use exactly the same hyperparameter configurations as given for prior models, but our decisions were inspired by the respective studies. As a result, we kept several parameters unchanged as suggested by previous work, while we chose several crucial parameters to be specified dynamically via hyperparameter optimization. This conveys some sense of optimization as it would have been done for real-life applications. To ensure comparability, we used multiple common datasets of prior work and established an architecture baseline with an own LSTM implementation to balance the triangle of architecture, dataset, and hyperparameters [22].

Lastly, novel architectures have been and will be proposed contin uously in the coming months and years. Echoing the call by Hutson [58], our findings underline that it is important to install a common core of sufficiently distinct process event logs and report metrics comprehen sively. With respect to novel architectures, generative adversarial net works (GAN) seem to be a promising avenue to improve the performance in next event prediction [62]. However, in the future, it will not be enough to only focus on performance improvements as there is a tradeoff between model performance and model explainability [63]. Harl, et al. [64] and Mehdiyev and Fettke [65] have recognized this and started to experiment with XAI visualizations for PPM.

Declarations of interest

None.

Funding

This research and development project is funded by the Bayerische Staatsministerium für Wirtschaft, Landesentwicklung und Energie (StMWi) within the framework concept “Informations- und Kommuni kationstechnik” (grant no. DIK0143/02) and managed by the project management agency VDI+VDE Innovation + Technik GmbH.

## Acknowledgement

A prior version of this article has been published as “Heinrich, K., Zschech, P., Janiesch, C., Bonin, M., Ein Vergleich von aktuellen Deep-Learning-Architekturen für die Prognose von Prozessverhalten. Pro ceedings of the 15. Internationale Tagung Wirtschaftsinformatik (WI). Potsdam, 2020, pp. 876-892. https://doi.org/10.30844/wi\_2020\_i1 -heinrich. It has been revised and extended with permission.

## References

[11 A.E Márquez-Chamorro. M. Resinas. A. Ruiz-Cortés. Predictive monitoring of business processes: a survey. JEEE Trans, Sery. Comput. 11 (2018) 962–977

[2] C. Di Francescomarino, C. Ghidini, F.M. Maggi, G. Petrucci, A. Yeshchenko, An eye into the future: leveraging A-priori knowledge in predictive business proces monitoring. in: Proceedings of the 15th International Conference on Business Process Management (BPM), Barcelona (2017) 252–268.

[3] M. zur Mühlen, R. Shapiro, Business Process Analytics, Handbook on Business Process Management 2, Springer, Berlin, 2010, pp. 243–263.

[4] A. Rogge-Solti, M. Weske, Prediction of business process durations using non-Markovian stochastic petri nets, Inf. Syst. 54 (2015) 1–14.

[5] J. Evermann, J.-R. Rehse, P. Fettke, Predicting process behaviour using deep learning, Decis, Support, Syst, 100 (2017) 129–140.

[6] G. Shmueli, O.R. Koppius, Predictive analytics in information systems research, Manag, Inf, Syst, Q. 35 (2011) 553–572

[7] Y. LeCun, Y. Bengio. G. Hinton, Deep learning, Nature 521 (2015) 436–444.

[8] W. Kratsch, J. Manderscheid, M. Roglinger, ¨ J. Seyfried, Machine learning in business process monitoring: a comparison of deep learning and classical approaches used for outcome prediction, Bus. Inform. Syst. Eng. (2020) online fi

[9] N. Mehdiyev, J. Evermann, P. Fettke, A novel business process prediction model using a deep learning method, Bus. Inf. Syst. Eng. 62 (2020) 143–157.

[10] S. Leijnen, F. van Veen, The Neural Network Zoo, Proceedings 47, 2020, p. 9.

[11] S. Pouyanfar, S. Sadiq, Y. Yan, H. Tian, Y. Tao, M.P. Reyes, M. Shyu, S. Chen, S. S. Iyengar, A survey on deep learning: algorithms, techniques, and applications, ACM Comput, Sury, 51 (2018) 92.

[12] M. Camargo, M. Dumas, O. Gonzalez-Rojas, ´ Learning accurate LSTM models of business processes, in: Proceedings of the 17th International Conference on Business Process Management (BPM). Wien, 2019, pp. 286–302

[13] N. Tax, I. Verenich, M. La Rosa, M. Dumas, Predictive business process monitoring with LSTM neural networks. in: Proceedings of the 29th International Conference on Advanced Information Systems Engineering (CAiSE). Essen, 2017, pp. 477–492.

[14] S. Schonig, ¨ R. Jasinski, L. Ackermann, S. Jablonski, Deep learning process prediction with discrete and continuous data features, in: Proceedings of the 13th International Conference on Evaluation of Novel Approaches to Software Engineering (ENASE), Setubal, 2018, pp. 314–319.

[15] E. Tello-Leal, J. Roa, M. Rubiolo, U. Ramirez-Alcocer, Predicting activities in business processes with LSTM recurrent neural networks, in: Proceedings of the 2018 ITU Kaleidoscope: Machine Learning for a 5G Future (ITU K), Santa Fe, 2018, pp. 1–7.

[16] A. Metzger, J. Franke, T. Jansen, Data-driven deep learning for proactive terminal process management, in: Proceedings of the 17th International Conference on Business Process Management (BPM) Industry Forum. Wien, 2019, pp. 190–201.

[17] S. Weinzierl, S. Zilker, M. Stierle, G. Park, M. Matzner, From predictive to prescriptive process monitoring: Recommending the next best actions instead of calculating the next most likely events, in: Proceedings of the 15. Internationale Tagung Wirtschaftsinformatik, Potsdam, 2020, pp. 1–5.

[18] S. Weinzierl, M. Stierle, S. Zilker, M. Matzner, A. Next Click, Recommender system for web-based service analytics with context-aware LSTMs, in: Proceedings of the 53rd Hawaji International Conference on System Sciences (HICSS). Maui, HI. 2020. pp. 1542–1551.

[19] A. Khan, H. Le. K. Do. T. Tran, A. Ghose, H. Dam, R. Sindhgatta, Memoryaugmented neural networks for predictive process analytics, arXiv 1802 (2018) 00938.

[20] V. Pasquadibisceglie, A. Appice, G. Castellano, D. Malerba, Using convolutional neural networks for predictive process analytics, in: Proceedings of the 2019 International Conference on Process Mining (ICPM). Aachen, 2019. pp. 129–136.

[21] N. Di Mauro, A. Appice, T. Basile, Activity prediction of business process instances with inception CNN models, in: Proceedings of the XVIIIth Internationa Conference of the Italian Association for Artificial Intelligence (AI\*IA). Rende, 2019, pp. 348–361.

[22] R.P.W. Duin, Superlearning and neural network magic, Pattern Recogn. Lett. 15 (1994).215-217.

[23] G. Park, M. Song, Predicting performances in business processes using deep neural networks, Decis, Support, Syst, 129 (2020). 113191.

[24] N. Navarin, B. Vincenzi, M. Polato, A. Sperduti, LSTM networks for data-aware remaining time prediction of business process instances, in: Proceedings of the 2017 IEEE Symposium Series on Computational Intelligence (SSCI). Honolulu, HI 2017, pp. 1–7.

[25] I. Teinemaa, M. Dumas, M.L. Rosa, F.M. Maggi, Outcome-oriented predictive process monitoring, ACM Trans. Knowl. Discov. Data 13 (2019) 1–57.

[26] M. Hinkka, T. Lehto, K. Heljanko, A. Jung, Classifying process instances using recurrent neural networks, in: Proceedings of the 1st International Workshop on Artificial Intelligence for Business Process Management (AI4BPM). Svdney, 2018 pp. 313-324.

[27] A. Leontjeva, R. Conforti, C. Di Francescomarino, M. Dumas, F.M. Maggi, Complex symbolic sequence encodings for predictive monitoring of business processes, in: Proceedings of the 13th International Conference on Business Process Management (BPM), Innsbruck, 2015, pp. 297–313.

[28] C. Di Francescomarino, M. Dumas, M. Federici, C. Ghidini, F.M. Maggi, W. Rizzi, Predictive business process monitoring framework with hyperparameter optimization, in: Proceedings of the 28th International Conference on Advanced Information Systems Engineering (CAiSE). Ljubljana, 2016, pp. 361–376.

[29] T. Nolle, S. Luettgen, A. Seeliger, M. Mühlh¨auser, BINet: Multi-perspective Business process anomaly classification, arXiv 1902 (2019) 03155.

[30] G. Park, M. Song, Prediction-based resource allocation using LSTM and minimum cost and maximum flow algorithm, in: Proceedings of the 2019 Internationa Conference on Process Mining (ICPM), Aachen, 2019, pp. 121–128.

[31] D. Breuker, M. Matzner, P. Delfmann, J. Becker, Comprehensible predictive models for business processes, MIS Q. 40 (2016) 1009–1034.

[32] B.F. van Dongen, BPI Challenge 2012, 2012, https://doi.org/10.4121/uuid: 3926db30-f712-4394-aebc-75976070e91f (accessed 2020-05-17).

[33] W. Steeman, BPI Challenge 2013, 2013, https://doi.org/10.4121/uuid:a7ce5c55- 03a7-4583-b855-98b86e1a2b07 (accessed 2020-05-17).

[34] M. Le, B. Gabrys, D. Nauck, A hybrid model for business process event prediction, in: Proceedings of the 32nd International Conference on Innovative Techniques and Applications of Artificial Intelligence (SGAI), London, 2012, pp. 179–192.

[35] M. Ceci, P.F. Lanotte, F. Fumarola, D.P. Cavallo, D. Malerba, Completion time and next activity prediction of processes using sequential pattern mining. in Proceedings of the 17th International Conference on Discovery Science (DS). Bled 2014, pp. 49–61.

[36] G.T. Lakshmanan. D. Shamsi, Y.N. Doganata, M. Unuvar. R. Khalaf. A markoy prediction model for data-driven semi-structured business processes, Knowl. Inf. Syst. 42 (2015) 97–126.

[37] M. Unuvar, G.T. Lakshmanan, Y.N. Doganata, Leveraging path information to generate predictions for parallel business processes, Knowl. Inf. Syst. 47 (2016) 433–461.

[38] I. Verenich, Helpdesk, 2016, https://doi.org/10.17632/39bp3yy62t.1 (accessed 2020-05-17).

[39] M. Hinkka, T. Lehto, K. Heljanko, Exploiting event log data-attributes in RNN based prediction, in: Proceedings of the 23rd European Conference on Advances in Databases and Information Systems (ADBIS). Bled, 2019, pp. 405–416

[40] K. Cho, B. van Merrienboer, C. Gulcehre, D. Bahdanau, F. Bougares, H. Schwenk, Y. Bengio, Learning phrase representations using RNN encoder–decoder for statistical machine translation, in: Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP), Doha, 2014, pp. 1724–1734.

[41] L. Lin, L. Wen, J. Wang, MM-Pred: A deep predictive model for multi-attribute event sequence, in: Proceedings of the 2019 SIAM International Conference on Data Mining (SDM), Calgary, 2019, pp. 118–126

[42] S. Hochreiter, J. Schmidhuber, Long short-term memory, Neural Comput. 9 (1997)

[43] Y.N. Dauphin, A. Fan, M. Auli, D. Grangier, Language modeling with gated convolutional networks. in: Proceedings of the 34th International Conference or Machine Learning (ICML) 70, 2017, pp. 933–941. Sydney.

[44] K. He, X. Zhang, S. Ren, J. Sun, Deep residual learning for image recognition, in: Proceedings of the 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Las Vegas, NV, 2016, pp. 770–778.

[45] J. Gu, Z. Wang, J. Kuen, L. Ma, A. Shahroudy, B. Shuai, T. Liu, X. Wang, G. Wang, J. Cai, T. Chen, Recent advances in convolutional neural networks, Pattern Recogn. 77 (2018) 354–377.

[46] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L, Jones, A.N. Gomez, ł. Kaiser Advances in Neural Information Processing Systems (NeurIPS), Long Beach, CA, 2017. pp. 5998–6008

[47] M. Daniluk, T. Rocktaschel, ¨ J. Welbl, S. Riedel, Frustratingly short attention spans in neural language modeling, in: Proceedings of the 5th International Conference on Learning Representations (ICLR). Toulon, 2017, pp. 1–10

[48] B.F. van Dongen, Real-Life Event Logs - Hospital Log, 2011, https://doi,org 10.4121/uuid:d9769f3d-0ab0-4fb8-803b-0d1120ffcf54 (accessed 2020-05-17)

[49] J.C.A.M. Bujis, Environmental Permit Application Process (WABO'). CoSeLoG Proiect – Municipality 4. 2014. https://doi.org/10.4121/uuid:e8c3a53d-5301: 4afb-9bcd-38e74171ca32 (accessed 2020-05-17)

[50] R.P.W. Duin, A note on comparing classifiers, Pattern Recogn. Lett. 17 (1996) 529–536.

[51] J. Demˇsar, Statistical comparisons of classifiers over multiple data sets, J. Mach. Learn. Res. 7 (2006) 1–30.

[52] M. Sokolova, G. Lapalme, A systematic analysis of performance measures for classification tasks, Inf. Process. Manag. 45 (2009) 427–437.

[53] M. Shepperd, D. Bowes, T. Hall, Researcher bias: the use of machine learning in software defect prediction, IEEE Trans. Softw. Eng. 40 (2014) 603–616.

[54] F. Chollet, Deep Learning with Python, Manning, Shelter Island, NY, 2018.

[55] W.M.P. van der Aalst, B.F. van Dongen, C. Günther, A. Rozinat, E.M.W. Verbeek, A. J.M.M. Weiiters, ProM: The process mining toolkit. in: Proceedings of the 7th International Conference on Business Process Management (BPM) Demonstration Track, Ulm, 2009, pp. 1–4.

[56] A. Klein, S. Falkner, S. Bartels, P. Hennig, F. Hutter, Fast Bayesian optimization of machine learning Hyperparameters on large datasets, in: Proceedings of the 20th International Conference on Artificial Intelligence and Statistics, Lauderdale, FL, 2017, pp. 528–536.

[57] K. Heinrich, P. Zschech, C. Janiesch, M. Bonin, Supplementary Material for “Process Data Properties Matter: Introducing GCNN and KVP for Next Event Prediction with Deep Learning”. http://doi.org/10.23728/b2share.08b7ff704 f724b94a61b4a6cac0fe1e0, 2021 (accessed 2021-01-12).

[58] M. Hutson, Core progress in AI has stalled in some fields, Science 368 (2020) 927.

[59] S. García, F. Herrera, An extension on “statistical comparisons of classifiers over multiple data sets” for all pairwise comparisons, J. Mach. Learn. Res. 9 (2008) 2677–2694.

[60] M. Sokolova, N. Japkowicz, S. Szpakowicz, Beyond Accuracy, F-score and ROC: a family of discriminant measures for performance evaluation, in: Proceedings of the 19th Australian Joint Conference on Artificial Intelligence (AI). Hobart, 2006, pp. 1015–1021.

[61] S. Weinzierl, S. Zilker, J. Brunk, K. Revoredo, A. Nguyen, M. Matzner, J. Becker, B. Eskofier, An empirical comparison of deep-neural-network architectures for next activity prediction using context-enriched process event logs. arXiv 2005 (2020) 01194.

[62] F. Taymouri, M. La Rosa, S. Erfani, Z.D. Bozorgi, I. Verenich, Predictive business process monitoring via generative adversarial nets: The case of next event prediction, in: Proceedings of the 18th International Conference on Business Process Management (BPM), Wien, 2020, pp. 237–256.

[63] J. Wanner, K. Heinrich, C. Janiesch, P. Zschech, How much AI Do you require? Decision factors for adopting AI technology, in: Proceedings of the 41st International Conference on Information Systems (ICIS), AIS Virtual Conference, 2020, pp. 1–17.

[64] M. Harl, S. Weinzierl, M. Stierle, M. Matzner, Explainable predictive business process monitoring using gated graph neural networks, J. Decis. Syst. (2020) 1–16, forthcoming.

[65] N. Mehdiyev, P. Fettke, Explainable artificial intelligence for process mining: A general overview and application of a novel local explanation approach for predictive process monitoring, in: W. Pedrycz, S.-M. Chen (Eds.), Interpretable Artificial Intelligence: A Perspective of Granular Computing, Springer, Cham, 2021.

Kai Heinrich is an assistant professor with the Otto-von-Guericke-Universit¨at Magdeburg. Before that, he worked as a research assistant and post-doc at the Chair of Business Informatics, especially Intelligent Systems and Services, at the Technische Universitat¨ Dresden. His research is at the intersection of artificial intelligence, decision support systems, and human-computer interaction. Research core topics include the design of AIbased decision support systems and the study of interactions between humans and AIbased systems. Common fields of application include industrial application fields like manufacturing, maintenance, or agrarian management as well as health care and finance. He has authored scholarly publications in leading international journals in the field of information systems such as Business & Information Systems Engineering, International Journal of Intelligent Information Technologies as well as in various conference pro ceedings including ICIS, ECIS, AMCIS, and HICSS.

Patrick Zschech is an assistant professor with the Friedrich-Alexander-Universitat¨ Erlangen-Nürnberg. Before that, he worked as a research assistant and post-doc at th Chair of Business Informatics, especially Intelligent Systems and Services, at the Techni sche Universitat ¨ Dresden. Additionally, he worked for the IT service provider Robotron Datenbank-Software GmbH as a project member and an instructor for data science qual ification programs. In his research, Patrick focuses on the selection, evaluation, and application of data-driven methods for the development of analytical information systems. His main interests are in the areas of machine learning, computer vision, process mining, and industry 4.0. Patrick regularly publishes his research results in international journals and conferences related to the field of decision support and information systems, such as Business & Information Systems Engineering, HMD Praxis der Wirtschaftsinformatik, Controlling & Management Review as well as in various conference proceedings including ICIS, ECIS, and WI.

Christian Janiesch is assistant professor with the Julius-Maximilians-Universit¨at Würz burg. Before, Christian worked full-time at the Westf¨alische Wilhelms-Universit¨at in Münster. at the SAP Research Center Brisbane at SAP Australia Pty Ltd., and at the Karlsruhe Institute of Technology. His research is at the intersection of business process management and business analytics with frequent applications in the Industrial Internet of Things. He is on the Department Editorial Board for BISE and has authored over 150 scholarly publications. His work has appeared journals such as the Journal of the Asso ciation for Information Systems, Communications of the Association for Information Systems, Information & Management, Business & Information Systems Engineering, Future Generation Computer Systems, Information Systems as well as in various major international conferences including ICIS, ECIS, BPM, and HICSS and has been registered as U.S. patents.

Markus Bonin completed his master’s degree in Business Informatics with a focus on Business Intelligence and Data Sciences at the Technische Universitat ¨ Dresden. His recent research work focuses on the application of deep learning architectures in the field of process prediction. Currently, he works at Capgemini Deutschland GmbH and designs an advanced analytics platform for the industrialization of data science solutions. Besides, he uses machine learning to solve natural language processing problems.

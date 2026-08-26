---
otero_id: 16270
otero_key: "5AA7JVHR"
title: "Predicting process behaviour using deep learning"
authors: "Joerg Evermann; Jana-Rebecca Rehse; Peter Fettke"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.04.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Joerg Evermann<sup>a,</sup> , Jana-Rebecca Rehse<sup>b,</sup> <sup>c</sup>, Peter Fettke<sup>b,</sup> <sup>c</sup>

<sup>a</sup> Memorial University of Newfoundland, St. John’s, NL, Canada

<sup>b</sup> German Research Center for Artificial Intelligence, Saarbrücken, Germany

<sup>c</sup> Saarland University, Saarbrücken, Germany

## A R T I C L E I N F O

Article history: Received 8 July 2016 Received in revised form 22 March 2017 Accepted 5 April 2017 Available online 17 April 2017

Keywords: Process management Runtime support Process prediction Deep learning Neural networks

## A B S T R A C T

Predicting business process behaviour is an important aspect of business process management. Motivated by research in natural language processing, this paper describes an application of deep learning with recurrent neural networks to the problem of predicting the next event in a business process. This is both a novel method in process prediction, which has largely relied on explicit process models, and also a novel applica tion of deep learning methods. The approach is evaluated on two real datasets and our results surpass the state-of-the-art in prediction precision.

© 2017 Elsevier B.V. All rights reserved

## 1. Introduction

Being able to predict the future behaviour of a business process is an important business capability [1]. As an application of predictive analytics in business process management, process prediction exploits data on past process instances to make predictions about current ones [2]. Example use cases are customer service agents responding to inquiries about the remaining time until a case is resolved, production managers predicting the completion time of a production process for better planning and higher utilization, or case managers identifying likely compliance violations to mitigate business risk.

We present a novel approach to predicting the next process event using deep learning. While the term “deep learning” has only recently become a popular research topic, it is essentially an application of neural networks and thus looks back on a long history of research [3]. Recent innovations both in algorithms, allowing novel architectures of neural networks, and computing hardware, especially GPU processing, have led to a resurgence in interest for neural networks and popularized the term “deep learning” [4]. Our approach is motivated by applications of neural networks to natural language processing(NLP), more specifically the prediction of the next word in a sentence [5–7]. By interpreting process event logs as text, process traces as sentences, and process events as words, these techniques can be applied to predict future process events. The contribution of our research is threefold:

1. We improve on the state-of-the-art in process event prediction. Our results show our method has considerably better precision on next-event prediction.

2. We demonstrate that an explicit process model is not necessary for prediction. Deep learning models, where the process structure is only implicitly reflected, can perform as well as explicit process models.

3. We contribute to process management in general by showcasing the useful application of an artificial intelligence approach, illustrating that business process management can benefit from the application of smart approaches.

Our research is located at the intersection of business process management, in particular process mining, and artificial intelligence (AI) and machine learning. We bring together historic process data with an AI learning technology to leverage real-time case management, opening new perspectives into process execution, monitoring, and analysis. Extending existing solutions to novel problems (“exaptation”) is a recognized and valid way to make a contribution in design science [8], which is the research approach we apply here. We not only provide a new approach, rooted in AI, to predicting the next process event, but also give a proof-of-concept regarding its feasibility and experimentally explore its eficiency and effectiveness, thus making a valuable contribution to the field of “Smart BPM”.

This paper is a significant extension over earlier work [9], adding more advanced neural network cells, separation of training and validation samples for cross-validation to prevent overfitting, empirical assessment of the effect of different neural network parameters, prediction not only of next events but of case remainders, interpretation and visualization of neural network states, encoding of timing information, and an extended discussion of the similarities and differences between natural language processing and process event prediction.

## 2. Related work

Process prediction covers an array of different techniques, objectives, and data sources. It extends process mining from a post-hoc analysis method to operational decision support [10]. Most existing process prediction research focuses on prediction of process outcomes, primarily the remaining time to completion, rather than prediction of the next event in a process, as we do here. Only five approaches are concerned with predicting the next event [2,11-14], all of which use an explicit model representation such as a statetransition, HMM (hidden Markov models), or PFA (probabilistic finite automatons) model.

The MSA approach by Le et al. [13] considers each trace prefix as a state in a state-transition matrix. From the observed prefixes and their next events, a state transition matrix is built. When a running case has reached a state not contained in the state-transition matrix, its similarity to observed traces is computed using string edit distance. The prediction is made from the most similar observed case. Evaluating the approach on two datasets from a telecommunications company, Le et al. [13] report accuracies in predicting the next event of up to 25% and 70% for their two datasets.

The approach described by Lakshmanan et al. [12] and Unuvar et al. [14] consists of five steps. First, a process model is mined from existing logs. For each XOR split in the model, a decision tree is mined from case data. These trees are then used to compute the state transition probabilities for a HMM that is specific to the running case that is to be predicted. This HMM is then used to predict the probabilities of the following event. The approach is evaluated on simulated data. After training the decision trees for the HMM on one half of the traces (training set), each trace in the test set is cut into a prefix and postfix at a random point. For each prefix, the log-likelihood of observing the corresponding postfix is reported.

The approach described by Ceci et al. [11] uses sequence mining to identify frequent trace prefixes. For each prefix, a regression model is trained to predict remaining time to completion and a decision tree is trained to predict the next event. The algorithm identifies the appropriate prefix of the running case to choose the regression and decision tree model for predicting remaining completion time and the next event. The experimental evaluation uses two datasets, yielding prediction precision values for the next event of approximately 65% on one dataset and approximately 50% on the other, depending on the type of decision tree used and the frequency threshold for prefixes.

RegPFA [2] uses a probabilistic finite automaton (PFA) instead of a HMM, allowing the future hidden state to be a function of both the previous hidden state and the previous observed event (which itself is a probabilistic consequence of the previous hidden state). RegPFA uses an EM algorithm to estimate the model parameters of the PFA. The evaluation uses data from the 2012 and 2013 BPI Challenges [15–17].

Our approach has the same objective as these five related works, but differs in terms of method and process representation. Deep learning in the form of a recurrent neural network (RNN) is used to predict the next events, using event sequences and associated resource information. Processes are only implicitly represented within the RNN, rather than in an explicit state-transition, PFA or HM model. Because of the non-linear transformations used in neural networks, they are particularly suited to model non-linear relationships. In contrast, many of the existing methods are based on linear assumptions (e.g. regression trees). Thus, neural networks require less restrictive assumptions. Moreover, because models are built implicitly rather than explicitly, their performance does not depend on any ex-ante assumptions about the form of the model. Overall, our method constitutes an innovative new approach to process prediction.

## 3. Deep learning for process prediction

## 3.1. Introduction

A neural network is a special form of an acyclic computational graph [3]. It consists of a layer of input cells, one or more layers of “hidden” cells, and a layer of output cells. Cells in each layer are connected by weighted connections to cells in the previous and following layers, allowing for different network architectures. Each cell’s output is a function of the weighted sum of its inputs. A simple network architecture is a fully connected network of cells using sigmoid activation functions that form the hidden layer.

$$
a _ {j} ^ {l} = \sigma \left(\sum_ {i} w _ {i} ^ {l, j} a _ {i} ^ {l - 1} + b _ {j} ^ {l}\right) \quad \text { where } \quad \sigma (x) = \frac {1}{1 + \exp (x)}
$$

Here, $a _ { i } ^ { l }$ is the output (“activation”) of cell j in layer l, $w _ { i } ^ { l , i }$ is the weight of the connection from cell i on layer l 1 to cell j on layer $l , a _ { i } ^ { l - 1 }$ is the output of cell i on layer l 1 and $b _ { j } ^ { l }$ is the “bias” of cell j on layer l.

A neural network is a supervised learning technique where the output of the neural net is compared to a target by means of a loss function. The type of output layer cell and the loss function are often chosen jointly for their computational properties with respect to backpropagation. A typical combination for categorical targets is a softmax layer with a cross-entropy loss function H:

$$
y _ {i} = \text { softmax } (a) _ {i} = \frac {\exp (a _ {i})}{\sum_ {j} \exp (a _ {j})} \quad H _ {y ^ {\prime}} (y) = - \sum_ {i} y _ {i ^ {\prime}} \log (y _ {i})
$$

Here, $y ^ { \prime }$ are the target values and y are the network outputs, computed in turn from the output activations a of the next to last network layer. Gradients of the parameters $w _ { j } ^ { l , i } , b _ { i } ^ { l }$ with respect to the loss function are computed using backpropagation and parameters are adjusted using variants of gradient descent algorithms.

## 3.2. Recurrent neural networks (RNN)

Recurrent neural networks (RNN) are a neural network architecture popularized by work in natural language processing (NLP). NLP has moved away from explicit language models to statistical methods, specifically to RNN (for example, [5-7,18,19]). In a RNN, each cell’s output is not only connected to the following layer but each cell also feeds back information into itself, allowing it to maintain “state” over time. To make this tractable within an acyclic computational graph and backpropagation, the recurrent network cells are “unrolled”, that is, copies of it are produced for time $t , t - 1 , t - 2 , \ldots$ The state output of the RNN cell for time t 1 is state input to the cell for time t. In general, t need not represent time, but can index any sequence. Depending on how long one wishes to maintain state for, fewer or more cells are unrolled. Fig. 1 shows an RNN architecture with an input layer, an output layer and two hidden layers that are unrolled five steps [6]. Each layer (each box in Fig. 1) in turn consists of multiple input, output, or hidden cells that are not individually shown in Fig. 1.

![](/api/attachments/5AA7JVHR/fulltext/images/105346f66bd8b1dc592a3e5390562006cca2b113dddcd4fe46eeac2352910f00.jpg)  
Fig. 1. RNN architecture with two hidden layers of LSTM cells, unrolled five steps.

A typical NLP application trains the RNN on sequences of input words to predict the next word, e.g. to provide word suggestions for user input. As shown in Fig. 1, the target words are simply the input words shifted by one position, so that for each input word the following word is the target to be predicted. The ability to maintain state or context means that, for example, when given the input “fox” in Fig. 1 and predicting the correct target (the next word) “jumps”, the RNN can make use of the previous words “The quick brown” to improve prediction performance.

In this work, we apply a recurrent neural network to the problem of predicting the next event in a process from a sequence of observed events. In implementing process prediction using RNN, our main idea is to view an event log as a text, traces in the log as sentences, and events in a trace as analogous to words in a sentence.

## 3.3. Long short term memory(LSTM)

Recurrent networks with simple sigmoid cells have unsatisfactory performance for long time or sequence distances, leading to the development of long short term memory (LSTM) cells [20], defined by the vector equations in Fig. 2. An LSTM cell accepts $c _ { t - 1 }$ and $h _ { t - 1 }$ as state information from the prior unrolled cell on the same level, and $x _ { t }$ as input from cells on the previous layer. In turn, it passes $c _ { t }$ and $h _ { t }$ as new state information to the subsequent unrolled cell on the same level and also provides h as output to the next layer.

$$
f _ {t} = \sigma \left(W _ {f} \cdot \left[ h _ {t - 1}, x _ {t} \right] + b _ {f}\right)\tag{1}
$$

$$
i _ {t} = \sigma (W _ {i} \cdot [ h _ {t - 1}, x _ {t} ] + b _ {i})\tag{2}
$$

$$
\bar {c} _ {t} = \tanh \left(W _ {c} \cdot \left[ h _ {t - 1}, x _ {t} \right] + b _ {c}\right)\tag{3}
$$

The variables $c , x , h , f , i , o$ in Fig. 2 are vectors in $\mathbb { R } ^ { m . }$ the W and b (weights and biases) are “trainable” parameters of suitable dimensions. The functions tanh(. . .) and $\sigma ( \dots )$ are applied elementwise, $[ \ldots ]$ represents vector concatenation. Eqs. (1)–(6) describe m individual LSTM cells, each operating on a single input from <sup>R</sup>. The number of individual cells on each layer, i.e. the dimensionality m, can be freely chosen.

The intuition behind these definitions is as follows. Eq. (1) represents the “forget $\boldsymbol { \mathrm { g a t e } } ^ { \prime \prime }$ that determines, based on the inputs x and $h _ { t - 1 }$ , which part of the state to forget. Note that the prior state $c _ { t - 1 }$ is multiplied by $f _ { t }$ in $\operatorname { E q . }$ (4) to derive the new state. With $\sigma ( \dots )$ in $\mathsf { E q } .$ (1) yielding values between 0 and 1, some information in $c _ { t - 1 }$ will, to some degree, be “forgotten”. Eqs. (2) and (3) determine how the inputs $x _ { t }$ and $h _ { t - 1 }$ contribute to the updated cell state. Eq. (2) represents the “input gate” and determines which values of the state to update; some of the i will be close to zero, others close to one. Eq. (3) computes new candidate values c, which are multiplied with $i _ { t }$ in Eq. (4) when computing the new state $c _ { t } .$ Eq. (4) is the actual state update equation. The left term represents the “forgetting” of some prior state information while the right term represents the addition of new information to the cell state. Eq. (5) represents the “output gate”. It determines which values of the cell state are provided as output to the following layer and subsequent unrolled cell. It is multiplied in Eq. (6) with the tanh of the cell state to produce the final output h .

To further improve the performance of LSTM cells, Gers and Schmidhuber [21] introduce the idea of “peepholes”, which allow the forget and input gates to look (“peep”) at the prior state $c _ { t - 1 }$ , and which allows the output gate to also look (“peep”) at the current state $c _ { t } ,$ with the equations in Fig. 3 replacing those in Fig. 2. While there exist other variants to this basic LSTM cell, Greff et al. [22] conclude

$$
c _ {t} = f _ {t} \times c _ {t - 1} + i _ {t} \times \bar {c} _ {t}\tag{4}
$$

$$
o _ {t} = \sigma \left(W _ {o} \cdot [ h _ {t - 1}, x _ {t} ] + b _ {o}\right)\tag{5}
$$

$$
h _ {t} = o _ {t} \times \tanh (c _ {t})\tag{6}
$$

$$
f _ {t} = \sigma \left(W _ {f} \cdot [ c _ {t - 1}, h _ {t - 1}, x _ {t} ] + b _ {f}\right)
$$

$$
i _ {t} = \sigma \left(W _ {i} \cdot [ c _ {t - 1}, h _ {t - 1}, x _ {t} ] + b _ {i}\right)
$$

$$
o _ {t} = \sigma \left(W _ {o} \cdot [ c _ {t}, h _ {t - 1}, x _ {t} ] + b _ {o}\right)
$$

Fig. 3. Definition of peepholes for LSTM cells.

after an experimental evaluation that “the most commonly used LSTM architecture, performs reasonably well on various datasets and using any of eight possible modifications does not significantly improve the LSTM performance.”.

## 3.4. Word embeddings

As neural networks operate on real-valued data, words or any other categorical input must be appropriately encoded. One option for this is to use “one-hot” encodings, but this leads to input vectors and neural net layers whose size (the dimensionality m in Section 3.3) is the number of distinct words or categories. Word embeddings avoid this problem and allows arbitrary input vector and neural network sizes. Words are mapped into an n-dimensional “embedding” space $\mathbb { R } ^ { m }$ using an “embedding matrix”, which is essentially a look-up matrix of dimensions v m where v is the size of the vocabulary and m is the chosen dimensionality of the embedding space and hence the size of each LSTM hidden layer (cf. Section 3.3). The input layer in Fig. 1 is an embedding lookup function yields a numeric vector from $\mathbb { R } ^ { m }$ for each word in the vocabulary, which forms the input $x _ { t }$ in Eqs. (1), (2) and (5) for the first LSTM layer. The embedding matrix is also a trainable parameter that is learned during training. The output layer produces a probability distribution over the words in the vocabulary. Each output “box” in Fig. 1 represents a softmax layer with v individual cells. The word with the highest probability is selected as the predicted word and compared to the target.

## 3.5. Language and process

Referring to the XES standard [23], we define events jointly by the name of the executing activity (e.g. “Pay Invoice”, “Repair Widget”), the lifecycle transition (e.g. “Start”, “Complete”, “Schedule”) and, for some experimental settings, the organizational resource, role or group (e.g. “Jane Doe”, “Tester”, “Accounting”). An example of an event is “Repair Widget—Start—Jane Doe”. Our “vocabulary” is the set of unique events of this form contained in a log.

As natural language is constrained by grammatical and morphological rules, such as noun and verb agreement for plurals in English, process event sequences are determined or constrained by an underlying process logic, for example by business rules based on case data. Just as linguistic rules and constraints are not explicitly captured in NLP deep-learning approaches [5-7,18,19] but are learned by the neural network, the process constraints and rules also need not be explicitly represented but can be learned.

However, while there are many similarities between natural language and process traces, there are important differences. First, the size of the vocabulary in process prediction is much smaller than the size of a natural language vocabulary. Second, the length of a trace can far exceed the typical sentence length in natural language. Together, these two differences result in fewer possible prediction targets (vocabulary size or number of unique process event types) and more information to predict from (sentence or trace prefix length), suggesting that this approach may be able to achieve better results than word prediction in NLP. Third, in contrast to natural language, processes contain activities with temporally overlapping execution. But even in that case, individual lifecycle events are strictly ordered, e.g. “A—Start, B—Start, A—Complete, B—Complete”, as defined by the XES Working Group [23]: “ An event that occurs in a log . . . before another event that is related to the same trace, shall be assumed to have occurred before that other event.”. However, the possibly arbitrary temporal sequence of events of parallel activities across different traces can make the prediction task more dificult, especially when there are no underlying regularities or dependencies imposed by other process characteristics such as resources or case attributes.

![](/api/attachments/5AA7JVHR/fulltext/images/87c1caa61c12c3bb8dba87dec3382d64624f18e20ecf2a55597af1bdee9d7d0f.jpg)  
Fig. 4. Mutual information of process event logs and English language text by separation distance (solid line is I = exp(<sub>−</sub>d/5))

To empirically examine the similarity of process event logs and natural language text, we focus on two characteristics. First, the mutual information I of two words in natural language declines with their distance d according to a power law $( I \ \propto \ d ^ { - k } ) ,$ , rather than an exponential manner $( I \ \propto \ e x p \ - \ d / k )$ . Markov models cannot model this form of dependency, while RNN can [24]. We compare the mutual information in our datasets against that of two natural language text corpora, the British National Corpus<sup>1</sup> and an extract from Project Gutenberg<sup>2</sup> (Fig. 4). As our event logs exhibit exponential decline, an RNN is not strictly necessary as they can be modelled by both Markov-based models and RNNs. This invites a comparison between the RNN and Markov-based approach, which we provide by comparing our method to the PFA method by Breuker et al. [2] (Section 6).

Second, we examine whether Zipf’s law [25] holds for the event logs. Zipf’s law states that the frequency of words in a natural language corpus is inversely proportional to the frequency rank of that word. Fig. 5 shows that our event logs also adhere to Zipf’s law and are, in this characteristic, similar to natural language.

In summary, given that there are both similarities and differences, a proof-of-concept implementation to demonstrate feasibility of applying NLP methods to process prediction, and an experimental evaluation to demonstrate effectiveness and performance are clearly required.

![](/api/attachments/5AA7JVHR/fulltext/images/5d4b86d367b24ed9e2f0e462c24bd7d6009b924c8340a835141da2da30a8afe5.jpg)  
Fig. 5. Relative frequency of terms by frequency rank for process event logs and English language text (solid line is Zipf’s law).

## 4. Implementation

A number of software frameworks for deep-learning have become available recently [26]. We implement our approach using Tensorflow as it provides a suitable level of abstraction, provides RNN specific functionality, and can be used on high-performance parallel, cluster, and GPU computing platforms. Code, data and complete results are available from the corresponding author.<sup>3</sup>

Our network features an architecture as in Fig. 1 with two hidden RNN layers using LSTM cells. This architecture still affords many choices, in particular the dimensionality of the embedding space and the number of unrolled steps.

The dimensionality of the embedding space must be guided by the vocabulary size (the number of unique event types). A larger dimensionality allows better separation of words in that space, which likely leads to better predictive performance, but at the cost of computational effort. Our baseline in the experimental evaluation (Section 5) is 125, and we explore the effect of varying this parameter on predictive performance. The number of “unrolled” steps indicates the length of the sequence of words across which state information is maintained, independent of vocabulary size. A larger number of unrolled steps allows the network to take earlier process events into account when predicting the following process event. This, too, is at the expense of computational effort. Our baseline for the experimental evaluation is 20, and we explore the effect of varying this parameter on predictive performance.

In addition to these two parameters, a number of general neural network options are parameterized (Table 1). Greff et al. [22] show that these parameters are significantly less important in determining RNN performance than network size and are largely independent in their effect on RNN performance. Trainable parameters are initialized using a uniform random distribution over [ 0.1, 0.1]. Training proceeds in batches of size 20. For each batch, the backpropagation algorithm computes the mean gradients for all parameters. Training of the net proceeds in “epochs”. Each epoch trains the net on the entire event log. Subsequent epochs maintain the weights W and biases b learned from the previous epoch but reinitialize the states for each layer and then train the net again on the entire event log. The net was trained for 100 epochs. The learning rate is reduced from 1 by a factor of 0.75 each epoch after the 50th. Dropout is a technique to prevent overfitting and improve learning by randomly temporarily removing a cell from the network [27]. Dropout probability for each cell is 0.2.

Table 1  
RNN parameters.

<table><tr><td>Parameter</td><td>Value</td></tr><tr><td>Initialization scale</td><td>0.10</td></tr><tr><td>Batch size</td><td>20</td></tr><tr><td>Maximum gradient norm</td><td>5.00</td></tr><tr><td>Number of training epochs</td><td>100</td></tr><tr><td>Number of epochs with full base learning rate</td><td>50</td></tr><tr><td>Base learning rate</td><td>1.00</td></tr><tr><td>Learning rate decay</td><td>0.75</td></tr><tr><td>Dropout probability</td><td>0.20</td></tr><tr><td>LSTM forget bias</td><td>0.10</td></tr></table>

## 5. Experimental method

## 5.1. Data

To provide a compelling evaluation of our approach, it should be compared to the state-of-the-art in next event prediction. Of the related work discussed in Section 2, only Breuker et al. [2] make an implementation publicly available and use publicly available data, demonstrating “open research” [28]. We contacted all authors of the remaining papers twice, but did not receive software or data to use for comparative evaluation.

We use the same datasets as Breuker et al. [2]. The BPI Challenge 2012 dataset [15] is a real dataset from a loan application process in a Dutch financial institute with 13,087 traces. It can be separated into three subprocesses concerning the application itself (A), the offer (O) and the work item (W) belonging to the application. The BPI Challenge 2013 datasets [16,17] are real datasets from IT incident and problem management processes at Volvo Belgium with 7553 and 2300 traces, respectively.

In addition to separating the BPI 2012 dataset by sub-process as done by Breuker et al. [2], we also use the combined dataset. While Breuker et al. [2] use only activity completion events for the BPI 2012 dataset, we also test our approach on all events (including the lifecycle transitions “Start”, “Schedule” and “Complete”). However, only the “W” subset has events other than completion events. Furthermore, we include an experimental condition where we extract the activity name and lifecycle transition, and combine this with the name of the resource associated with the event (cf. Section 3.5). We simply concatenate the two character strings to form the composite word. This creates a larger vocabulary which increases the prediction dificulty, but also provides more information to the training algorithm. It also allows prediction of not only the activity of the next event but also the resource associated with the next event. Because the number of distinct resources in the BPI 2013 datasets is very large, we use the organizational group instead of organizational resource. Table 2 shows characteristics of the datasets.

The published datasets are transformed using XSL transformations to extract traces, events, and resource information in a suitable format.

## 5.2. Evaluation method

There are three random influences on prediction performance. First, the trainable parameters are initialized randomly and different initial values may lead to different outcomes (e.g. convergence to local optima). Second, the traces in a log are in a particular order but this is an arbitrary order. Because the LSTM cells maintain state, the order in which traces are used to train the network may have an effect on the outcome. Finally, the selection of the training dataset itself has an influence, and the results obtained with a particular sample may not generalize to others. Both BPI 2012 and 2013 datasets are sampled from running systems.

Table 2  
Characteristics of datasets used in experimental evaluation. Event numbers for partial BPI2012 logs do not add up to that of corresponding complete log due to end-of-case marker events added to each trace.

<table><tr><td rowspan="2">Dataset</td><td colspan="2">Number of unique event types (&quot;vocabulary size&quot;)</td><td rowspan="2">Number of events</td></tr><tr><td colspan="2">with resource information</td></tr><tr><td>BPI2013.Incidents</td><td>14</td><td>3133</td><td>65,533</td></tr><tr><td>BPI2013.Problems</td><td>8</td><td>64</td><td>9,011</td></tr><tr><td>BPI2012 (completion events)</td><td>24</td><td>877</td><td>164,506</td></tr><tr><td>BPI2012 (all events)</td><td>37</td><td>1349</td><td>262,200</td></tr><tr><td>BPI2012.W (completion events)</td><td>7</td><td>264</td><td>72,413</td></tr><tr><td>BPI2012.W (all events)</td><td>7</td><td>736</td><td>169,507</td></tr><tr><td>BPI2012.A</td><td>11</td><td>302</td><td>60,849</td></tr><tr><td>BPI2012.O</td><td>8</td><td>313</td><td>31,244</td></tr></table>

To address these stochastic influences, we perform 10-fold crossvalidation [29]. Comparing the prediction performance on an independent validation sample to the prediction performance on the training sample assesses the generalizability to similar datasets. Specifically, it examines whether the RNN overfits the training sample, i.e. exploits idiosyncrasies in the training sample, and what type of performance can realistically be expected on a dataset with similar characteristics. Note that Breuker et al. [2] do not cross-validate the results of their stochastic EM-based approach; a fair comparison is therefore to our training results.

We report the prediction precision, defined as the proportion of correct predictions of all predictions made. We report mean and standard deviation of the training precision, as well as the mean and standard deviation of the precision achieved on the validation fold, across all 10 folds.

## 6. Experimental results

We train the RNN for 100 epochs on each training dataset. Fig. 6 plots training and validation precision for each epoch for a selection of our datasets (averaged across all 10 training folds). The plot shows that 100 training epochs are suficient for optimal and stable results. The small BPI 2012 A and O datasets converge quickly to a high precision, whereas this occurs more gradually for the BPI 2013 datasets. Moreover, the BPI 2012 A, BPI 2012 O, and BPI 2013 Problem datasets with relatively small vocabularies converge faster than the BPI 2012 W and BPI 2013 Incident datasets that include resource or organizational group information and consequently have a larger vocabulary. There is a significant improvement in precision when the training rate is adjusted in epoch 50, suggesting that a dynamic training rate helps to prevent suboptimal convergence. The second panel in Fig. 6 shows that validation precision generally follows the behaviour of training precision at a lower level.

## 6.1. Predicting the next event

Table 3 shows our results and a comparison to the best result presented by Breuker et al. [2]. The table shows that our RNN approach surpasses the performance of probabilistic finate automatons on many datasets. For the BPI 2013 Incidents data, the BPI 2012 A, and the BPI 2012 O subsets, our training and validation precision values are above the best values reported by Breuker et al. [2]. For the BPI 2013 Problems dataset, our approach offers better training precision, but the validation precision is lower than that reported by Breuker et al. [2], and on the BPI 2012 W dataset, our approach performs poorly. Overall, this is in line with the expectations based on mutual information (Section 3.5) which showed that both PFA and RNN should be able to model our process data equally well.

Comparing the training and validation precision shows that lit tle overfitting occurs, with the validation precision generally within 0.05 of the training precision. The standard deviations for the validation precision are an order of magnitude above those for the training sample because of the smaller size of the validation sample (one tenth of the training sample size).

Table 3 shows many results with validation precision close to or in excess of 0.8. While we have no comparison to the state-of-theart on these datasets by Breuker et al. [2], this level of precision is encouraging for practical applications. It is also generally above the levels reported in related works (see Section 2), although this must be interpreted with caution due to different datasets with possibly very different characteristics, such as number of unique events, trace length, or the patterns due to the structure of the underlying, generating process.

![](/api/attachments/5AA7JVHR/fulltext/images/0eca4201cc8e0d26e8e2433fd017fe27b4801d09125fd5da9ea3fee567f8a3d4.jpg)

Validation Precision by Epoch  
![](/api/attachments/5AA7JVHR/fulltext/images/2911dc3476fe76d9fad942259568aafb8c82c173ddd5393bfc0f3a7de784ce51.jpg)  
Fig. 6. Training precision by training epoch for selected datasets (mean over 10 training folds).

Table 3  
Results and comparison to [2] .

<table><tr><td rowspan="2">Dataset</td><td rowspan="2">Precision in [2]</td><td colspan="2">Training precision</td><td colspan="2">Validation precision</td></tr><tr><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td></tr><tr><td>BPI2013.Incidents</td><td>0.714</td><td>0.757</td><td>0.011</td><td>0.735</td><td>0.044</td></tr><tr><td>BPI2013.Problems</td><td>0.690</td><td>0.727</td><td>0.037</td><td>0.628</td><td>0.086</td></tr><tr><td>BPI2012 (completion events)</td><td></td><td>0.796</td><td>0.001</td><td>0.788</td><td>0.006</td></tr><tr><td>BPI2012 (all events)</td><td></td><td>0.864</td><td>0.001</td><td>0.859</td><td>0.005</td></tr><tr><td>BPI2012.W (completion events)</td><td>0.719</td><td>0.676</td><td>0.002</td><td>0.658</td><td>0.020</td></tr><tr><td>BPI2012.W (all events)</td><td></td><td>0.839</td><td>0.001</td><td>0.832</td><td>0.010</td></tr><tr><td>BPI2012.A</td><td>0.801</td><td>0.837</td><td>0.001</td><td>0.832</td><td>0.010</td></tr><tr><td>BPI2012.O</td><td>0.811</td><td>0.841</td><td>0.001</td><td>0.836</td><td>0.010</td></tr></table>

Prediction is significantly better for the BPI 2012 W dataset with all events compared to the same dataset with completion events only as it exploits the regularity that after every “Start” event for an activity, the corresponding “Complete” event for that activity follows.

## 6.2. The effect of resource information

Including the organizational resource or group in the predicting data provides additional information that should lead to improved prediction precision. Including this information in both predictor and predictand allows prediction not only of the activity of the next process event but also of the resource associated with the next process event. However, this comes at the cost of a larger vocabulary and should lead to lower prediction precision. We explore both options, and the results in Table 4 are generally as expected.

Including the organizational group or resource information only in the predictor (Table 4) improves the training precision for all datasets, by up to 0.07, compared to the baseline in Table 3. However, the validation precision does not follow the same pattern, improving only for some datasets, and even then improving to a lesser extent as the training precision. This suggests that including resource information for prediction may be useful but also runs the danger of overfitting the model.

Including the organizational resource or group in both the predictor and predictand affects the prediction precision for the datasets in different ways. Training precision for the BPI 2013 Incident decreases, but increases for the BPI 2013 Problem dataset. Validation precision drops significantly for both datasets. Training and validation precision for all BPI 2012 datasets also drop significantly. An extreme example is the BPI 2012 W dataset with completion events only, where training precision drops to 0.313 and validation precision to 0.208. Here, the resources assigned to events do not follow any underlying regularity, impairing prediction performance. In contrast, for the BPI2012.W with all events, the resource of the completion event is the same as of the start event, which leads to improved performance.

## 6.3. Predicting duration of activities

An RNN can also be used to predict the duration of activities. For this, we quantize the temporal extent of a trace in minutes and, for each minute, encode the current activity in the input. For example, if activity A occurs for 3 min, the input consists of the sequence AAA. Only the BPI 2012 W dataset includes both start and completion events to allow determination of the duration of activities.<sup>4</sup> While it is possible to encode idle time between two activities in the same manner, the BPI 2012 W dataset describes long-running cases, which would have led to very long and monotonous sequences.

The validation precision for this case is 0.942, (SD = 0.027), significantly higher than the 0.832 reported in Table 3 for the case with no duration information. This increase in precision is not surprising, as the dataset consists of longer sequences of identical words, thus making prediction of the following word much easier.

## 6.4. The effect of embedding space dimensionality

To identify the effect of the dimensionality of the word embedding space on prediction performance, we repeat our experiments using embedding spaces of 500, 64, 32, 16, and 8 dimensions, keeping the other parameters unchanged. Table 5 shows the validation precision of our datasets for different numbers of dimensions. Fig. 7 plots training and validation precision for three datasets with and without organizational information.

As expected, reducing the dimensionality of the embedding has, in general, a detrimental effect on the prediction precision. However, this effect is negligible as long as the dimensionality of the embedding space is greater than the size of the vocabulary. This is the case for all datasets that do not include organizational information. For example, neither the BPI 2013 datasets with 14 and 8 event types, nor the BPI 2012 dataset with 24 event types in Fig. 7 show a marked reduction in training or validation precision when the dimensionality is reduced from 64 to 32 and to 16. However, when the dimensionality is reduced to 8, the reduction in precision is more pronounced for all datasets.

Given the larger vocabulary when including organizational information, the effect of dimensionality is more pronounced at smaller dimensions, as is visible in Fig. 7. The BPI 2013 datasets with 3133 and 64 unique combinations of event activity and organizational group, and the BPI 2012 dataset with 877 unique combinations, show a significant reduction in precision when the dimensionality is reduced from 125 to 64. Other datasets with large vocabulary show the same behaviour.

Increasing the dimensionality to 500, done only for selected datasets due to the required computational effort, shows that significant overfitting occurs, especially for datasets with a large vocabulary. As shown in Fig. 7, the training precision for the BPI 2012 and BPI 2013 datasets increases significantly whereas the validation precision is not only much lower than the training precision, but decreases with increasing dimensionality. These trends are clear indications of overfitting.

Examining Fig. 7 and the corresponding data in Table 5 shows that our chosen baseline with 125 dimensions is close to the optimum validation precision for all datasets and does not suffer from significant overfitting.

## 6.5. The effect of the number of unrolled steps

To identify the effect of the number of unrolled steps on prediction performance, we repeat our experiments using 10 and 5 unrolled steps, keeping the other parameters unchanged. Fig. 8 and Table 6 show the training and validation precision of selected

Table 4  
Precision when including resources or organizational groups.

<table><tr><td rowspan="3">Dataset</td><td colspan="4">Predictor only</td><td colspan="4">Predictor &amp; predictand</td></tr><tr><td colspan="2">Training precision</td><td colspan="2">Validation precision</td><td colspan="2">Training precision</td><td colspan="2">Validation precision</td></tr><tr><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td></tr><tr><td>BPI2013.Incidents</td><td>0.832</td><td>0.034</td><td>0.761</td><td>0.049</td><td>0.731</td><td>0.010</td><td>0.595</td><td>0.061</td></tr><tr><td>BPI2013.Problems</td><td>0.776</td><td>0.081</td><td>0.616</td><td>0.117</td><td>0.764</td><td>0.034</td><td>0.517</td><td>0.043</td></tr><tr><td>BPI2012 (completion)</td><td>0.833</td><td>0.004</td><td>0.811</td><td>0.023</td><td>0.622</td><td>0.005</td><td>0.594</td><td>0.010</td></tr><tr><td>BPI2012 (all events)</td><td>0.880</td><td>0.007</td><td>0.866</td><td>0.008</td><td>0.685</td><td>0.007</td><td>0.663</td><td>0.015</td></tr><tr><td>BPI2012.W (completion)</td><td>0.745</td><td>0.013</td><td>0.693</td><td>0.019</td><td>0.313</td><td>0.012</td><td>0.208</td><td>0.023</td></tr><tr><td>BPI2012.W (all events)</td><td>0.865</td><td>0.012</td><td>0.845</td><td>0.012</td><td>0.609</td><td>0.018</td><td>0.559</td><td>0.018</td></tr><tr><td>BPI2012.A</td><td>0.846</td><td>0.006</td><td>0.826</td><td>0.007</td><td>0.758</td><td>0.010</td><td>0.709</td><td>0.008</td></tr><tr><td>BPI2012.O</td><td>0.870</td><td>0.015</td><td>0.833</td><td>0.015</td><td>0.703</td><td>0.026</td><td>0.590</td><td>0.020</td></tr></table>

## Table 5

Validation precision for different dimensions of the embedding space. Due to computational requirements, 500 dimensions applied only to selected datasets.

<table><tr><td rowspan="2">Dataset</td><td colspan="6">Dimensionality of embedding space</td></tr><tr><td>500</td><td>125</td><td>64</td><td>32</td><td>16</td><td>8</td></tr><tr><td>BPI2013.Incidents</td><td>0.721</td><td>0.735</td><td>0.736</td><td>0.734</td><td>0.728</td><td>0.692</td></tr><tr><td>BPI2013.Problems</td><td>0.593</td><td>0.628</td><td>0.635</td><td>0.642</td><td>0.638</td><td>0.622</td></tr><tr><td>BPI2012 (completion events)</td><td>0.779</td><td>0.788</td><td>0.791</td><td>0.787</td><td>0.747</td><td>0.602</td></tr><tr><td>BPI2012 (all events)</td><td></td><td>0.859</td><td>0.859</td><td>0.854</td><td>0.772</td><td>0.578</td></tr><tr><td>BPI2012.W (completion events)</td><td>0.638</td><td>0.658</td><td>0.660</td><td>0.661</td><td>0.657</td><td>0.646</td></tr><tr><td>BPI2012.W (all events)</td><td></td><td>0.832</td><td>0.833</td><td>0.832</td><td>0.824</td><td>0.733</td></tr><tr><td>BPI2012.A</td><td>0.833</td><td>0.832</td><td>0.833</td><td>0.834</td><td>0.832</td><td>0.799</td></tr><tr><td>BPI2012.O</td><td>0.827</td><td>0.836</td><td>0.836</td><td>0.837</td><td>0.836</td><td>0.823</td></tr><tr><td>BPI2013.Incidents (with group)</td><td>0.567</td><td>0.595</td><td>0.590</td><td>0.525</td><td>0.387</td><td>0.272</td></tr><tr><td>BPI2013.Problems (with group)</td><td>0.473</td><td>0.517</td><td>0.513</td><td>0.521</td><td>0.504</td><td>0.449</td></tr><tr><td>BPI2012 (completion events, resource)</td><td>0.573</td><td>0.594</td><td>0.575</td><td>0.497</td><td>0.327</td><td>0.253</td></tr><tr><td>BPI2012 (all events, resource)</td><td></td><td>0.663</td><td>0.618</td><td>0.456</td><td>0.328</td><td>0.188</td></tr><tr><td>BPI2012.W (completion events, resource)</td><td>0.130</td><td>0.208</td><td>0.214</td><td>0.204</td><td>0.174</td><td>0.147</td></tr><tr><td>BPI2012.W (all events, resource)</td><td></td><td>0.559</td><td>0.558</td><td>0.495</td><td>0.302</td><td>0.134</td></tr><tr><td>BPI2012.A (resource)</td><td>0.714</td><td>0.709</td><td>0.717</td><td>0.717</td><td>0.688</td><td>0.615</td></tr><tr><td>BPI2012.O (resource)</td><td>0.577</td><td>0.590</td><td>0.598</td><td>0.588</td><td>0.482</td><td>0.263</td></tr></table>

datasets against the number of unrolled steps. Neither training nor validation precision is significantly affected by the number of unrolled steps. There appears to be a minor effect for the BPI 2013 Problem dataset (more pronounced when including the organizational group), where the training performance decreases with increasing number of unrolled steps, while the validation performance increases. This indicates that there are few to no longterm dependencies in the different processes that cannot be captured by even five previous steps, which is in line with the mutual information considerations in Section 3.5.

![](/api/attachments/5AA7JVHR/fulltext/images/5521f437ed93f4ee843946fc82fe372983adb9cb9df91eea0a49d40bf38cca49.jpg)

## 6.6. Interpreting the RNN

One of the main criticisms of neural networks is the fact that no explicit, human understandable model is created; the learning consists entirely in the optimization of the values of thousands or millions of floating point parameters. We present two ways in which users can gain insight into what the neural net has learned, i.e. the knowledge that is encoded in its structures.

![](/api/attachments/5AA7JVHR/fulltext/images/0194df3745f1f8d425bdacd97ff8010789fb6a240d753f1c08e748eb3648b3a5.jpg)  
Fig. 7. Training and validation precision against embedding space dimensions for selected datasets.

![](/api/attachments/5AA7JVHR/fulltext/images/869c152a32954a4524c197cd5332ea508baa86bfa46ef245163656f865c47587.jpg)

![](/api/attachments/5AA7JVHR/fulltext/images/9babc35b9e0b1640e072c35152aeaff35f21f84bca85a124f631637c1d56c509.jpg)  
Fig. 8. Validation precision for three values of unrolled steps for selected datasets.

Table 6  
Validation precision for different number of unrolled steps.

<table><tr><td rowspan="3">Dataset</td><td colspan="3">No resource info</td><td colspan="3">With resource info</td></tr><tr><td colspan="3">Unrolled steps</td><td colspan="3">Unrolled steps</td></tr><tr><td>20</td><td>10</td><td>5</td><td>20</td><td>10</td><td>5</td></tr><tr><td>BPI2013.Incidents</td><td>0.735</td><td>0.730</td><td>0.731</td><td>0.595</td><td>0.595</td><td>0.600</td></tr><tr><td>BPI2013.Problems</td><td>0.628</td><td>0.612</td><td>0.612</td><td>0.517</td><td>0.490</td><td>0.478</td></tr><tr><td>BPI2012 (completion events)</td><td>0.788</td><td>0.787</td><td>0.787</td><td>0.594</td><td>0.596</td><td>0.596</td></tr><tr><td>BPI2012 (all events)</td><td>0.859</td><td>0.860</td><td>0.860</td><td>0.663</td><td>0.667</td><td>0.667</td></tr><tr><td>BPI2012.W (completion events)</td><td>0.658</td><td>0.657</td><td>0.657</td><td>0.208</td><td>0.201</td><td>0.201</td></tr><tr><td>BPI2012.W (all events)</td><td>0.832</td><td>0.831</td><td>0.831</td><td>0.559</td><td>0.558</td><td>0.558</td></tr><tr><td>BPI2012.A</td><td>0.832</td><td>0.833</td><td>0.834</td><td>0.709</td><td>0.710</td><td>0.712</td></tr><tr><td>BPI2012.O</td><td>0.836</td><td>0.836</td><td>0.836</td><td>0.590</td><td>0.590</td><td>0.590</td></tr></table>

## 6.6.1. Process hallucinations

Neural networks, especially RNN, can be made to “hallucinate”, i.e. to generate output on their own, for example in language modeling [5,6,30] or music creation [31–33]. This is done by feeding the net output (prediction) immediately back as new input. Hallucinations can provide insight into what the RNN has learned about the training set. The ability of an RNN to re-produce, on its own, realistic and convincing process traces demonstrates that it has correctly learned the important features of the event log used as training sample and thereby validates the trained net and supports the usefulness of the RNN approach for process prediction.

Hallucinations are initialized by providing a short seed sequence of input events. One may either accept the event with the highest probability as output, or one samples from events using the output probabilities. We explore the two methods for the full BPI 2012 and BPI 2013 datasets. For each output method and for each dataset, we train a net with 32 embedding dimensions and 5 unrolled steps for 100 epochs. After training is complete, we produce 20 hallucinations of sequence length 1000 from each trained net. An excerpt of the BPI2012 hallucinations is shown in Fig. 9. The complete set of generated hallucinations is available from the authors.

In addition to visually inspecting the generated hallucinations and judging their realism, we mine a process model from the original event log using the Flexible Heuristics Miner (FHM) [34] with default parameters. We choose the FHM because it performs well on a wide variety of models [35]. We replay both the original log and the generated hallucinations against this model and compute the replay fitness, which indicates how well the model can generate the observed behaviour [36]. A replay fitness of the hallucinations similar to that of the original model is a strong indication that the generated traces are realistic. We also examine whether the frequency distribution of events in the generated hallucinations matches that in the original dataset, using the Kolmogorov-Smirnov test. A non-significant test (p-value > 0.05) indicates the frequency distributions come from the same underlying population.

Table 7 shows the results for the BPI2012 dataset. Probabilistic output sampling produces more realistic results than choosing the output with the highest probability; the latter produces many long uniform event sequences that are uncharacteristic of the input logs. Results for the other event logs are similar. In summary, the generated hallucinations show that the neural networks learn the relevant features of the input event logs.

Hallucinations can also be used to predict the remainder of a case. For this, the hallucination is initialized with a trace prefix and then continued until it produces an end-of-case indicator. The hallucination can then be compared with the actual trace continuation using a string-edit distance. We train nets with 32 embedding dimensions and 5 unroll steps for 100 epochs. Using trace prefixes of length 5, we produce hallucinations and compare them to the actual continuation using the normed Damerau–Levenshtein distance, which ranges from 0 to 1 (Table 8).

ASUBMITTED APARTLYSUBMITTED ADECLINED WAfhandelenleads [EOC] ASUBMITTED APARTLYSUBMITTED APREACCEPTED WAfhandelenleads WCompleterenaanvraag WCompleterenaanvraag WCompleterenaanvraag AACCEPTED AFINALIZED OSELECTED OCREATED OSENT WCompleterenaanvraag WNabellenoffertes WNabellenoffertes WNabellenoffertes OSENTBACK WNabellenoffertes WValiderenaanvraag WValiderenaanvraag WValiderenaanvraag WNabellenincompletedossiers OCANCELLED OSELECTED OCREATED OSENT WNabellenincompletedossiers WNabellenincompletedossiers WNabellenincompletedossiers WNabellenincompletedossiers WNabellenincompletedossiers ACANCELLED OCANCELLED WNabellenincompletedossiers [EOC] ASUBMITTED APARTLYSUBMITTED WAfhandelenleads ADECLINED WAfhandelenleads [EOC] ASUBMITTED APARTLYSUBMITTED ADECLINED [EOC] ASUBMITTED APARTLYSUBMITTED APREACCEPTED AACCEPTED OSELECTED AFINALIZED OCREATED OSENT WCompleterenaanvraag WNabellenoffertes WNabellenoffertes ADECLINED ODECLINED WNabellenoffertes [EOC]

Fig. 9. Example hallucinations for the BPI2012 dataset (probabilistic output sampling, “[EOC]” designates end-of-case).  
Hallucination characteristics for BPI2012 (completion events only) dataset.

<table><tr><td></td><td>Full log</td><td>Prob. sampling</td><td>Top-p output</td></tr><tr><td>Mean trace length</td><td>13</td><td>12</td><td>21</td></tr><tr><td>Max trace length</td><td>96</td><td>56</td><td>194</td></tr><tr><td>Replay fitness</td><td>0.586</td><td>0.582</td><td>0.350</td></tr><tr><td>KS test p-value</td><td>-</td><td>0.878</td><td>0.000</td></tr></table>

The application of hallucinations might be interesting in other areas of process mining as well, such as improving event log completeness in cases where particular mining algorithms benefit from better or larger logs.<sup>5</sup>

## 6.6.2. Hidden state dynamics

Recent work on understanding RNNs also focuses on visualization. In particular, visualizations of the embedding matrix, the state activation and the state dynamics are useful in understanding how an RNN encodes knowledge [37–40].

We export embedding matrices after completion of training to create 2D t-SNE plots [41]. They are not included here as no significant or obvious clustering of events is discernible for any of our datasets.

We use LSTMVis [40], which is motivated by earlier work by Karpathy et al. [37], to examine the activation of hidden state cells for different inputs.<sup>6</sup> The visualization assists in identifying cells that are active for some input but not others (the “hypothesis selection process”, [40]), and then confirming such hypotheses by comparing activation patterns against similar input (the “matching process”, [40]).

Mean and standard deviation of Damerau-Levenshtein distance between actual trace remainders and those predicted from a prefix of length 5. Hallucinations produced using probability sampling (k = 1) and element-wise feedback (m = 1); smaller is better.

<table><tr><td rowspan="2">Dataset</td><td colspan="2">Damerau-Levenshtein Distance</td></tr><tr><td>Mean</td><td>SD</td></tr><tr><td>BPI2013.Incidents</td><td>0.563</td><td>0.199</td></tr><tr><td>BPI2013.Problems</td><td>0.616</td><td>0.177</td></tr><tr><td>BPI2012 (completion events)</td><td>0.659</td><td>0.203</td></tr><tr><td>BPI2012.W (completion events)</td><td>0.703</td><td>0.205</td></tr><tr><td>BPI2012.W (all events)</td><td>0.697</td><td>0.211</td></tr><tr><td>BPI2012.A</td><td>0.545</td><td>0.241</td></tr><tr><td>BPI2012.O</td><td>0.532</td><td>0.191</td></tr></table>

Fig. 10 shows the tool in use with hidden states on the first level of the trained RNN for the BPI2012 dataset with 16 embedding dimensions. The event sequence “ADECLINED [EOC]” is selected in the timeline (top part of figure). The inputs that match the activation pattern of the selected event sequence are sequences of the same two events, shown at the bottom of the image. This cell appears to represent the ending of cases with declined loan applications. In some cases, another event occurs in between the “ADECLINED” and “[EOC]” and this input is represented by the same cell activation pattern. Other hidden state cells represent the events “WNABELLENOFFERTES”, “WCOMPLETERENANVRAAG”, and the sequence ”AACCEPTED AFI-NALIZED OSELECTED”.

## 7. Discussion and conclusion

This paper introduced the use of deep learning for process predic tion. Our approach does not rely on explicit process models and can be applied when models do not exist or are dificult to obtain. Our results, surpassing or close to the state-of-the-art and with crossvalidated precision in excess of 80% on many problems, demonstrate the feasibility and usefulness of this approach.

While one can perform prediction by mining a model from event logs, and mining decision rules for each process branch point [12,14], this has inherent drawbacks. Process mining algorithms trade off different quality criteria, such as fitness, precision, generalizability, and simplicity. The mined models are abstractions and intentionally imperfect representations of the underlying true process. This impairs predictive performance. Decision mining at process branch points or for trace prefixes [11] makes trade-offs between recall, precision, and parsimony, and may use simplifying assumptions such as linearity. This further impairs predictive performance. Explicit process models and decision rules are useful for understandability. At the same time, however, their intentional abstraction and parsimony makes them less suitable for prediction. In contrast, deep learning networks with their larger parameter space and non-linearity “skip” the intentionally imperfect representations between raw event logs and event prediction.

We chose RNNs for their natural fit to the sequence data of process event logs. An alternative to RNN are n-gram models, in which a non-recurrent neural network is trained on all fixed-length trace prefixes of length n. The RNN approach has the advantage of allowing prediction from trace prefixes of arbitrary length while also offering better prediction performance [18]. Alternatives to neural networks are probabilistic automatons such as HMM [12,14] and PFA [2]. Section 3.5 showed that the event logs chosen for this study have characteristics that make either of these techniques applicable. Our prediction results confirm this. While our RNN are not always superior, they surpass the performance of PFA in many cases. However, other processes may involve long-distance dependencies between events that are not found in our data. Such long-distance dependencies in an event log are likely to present problems for HMMs and n-gram models, but not for RNN [24].

![](/api/attachments/5AA7JVHR/fulltext/images/0e89f9c1534a52f455eb30dfbc693c952be61aa141362be22d822c860d3cbd2a.jpg)  
Fig. 10. LSTM visualization of states for declined loan application processes.

Deep learning approaches are susceptible to overfitting. The larger a neural network, the better it can capitalize on chance training data idiosyncrasies. With an embedding space of 500 dimensions and a small event log, Evermann et al. [9] report training data prediction precision in excess of 99%, showing clear overfitting. In this paper, we have also seen overfitting with similarly large embedding spaces. In the context of process model discovery, overfitting has its analogue in mined models with high fitness and precision, that are complex and not generalizable. And similar to quality tradeoffs in process model mining, deep learning also makes trade-offs. Prediction precision is traded off against generalizability (by overfitting) and simplicity (network size, embedding dimensionality). Just as model fitness must be evaluated in the context of other quality dimensions, predictive performance must be evaluated in the context of generalizability and model size. An assessment of overfitting through cross-validation is therefore essential.

Our approach constructs the RNN inputs by concatenating categorical, character string valued event attributes and then encoding these attributes via an embedding space. This is feasible only because of the small number of unique values for each attribute in our datasets. Because of this, the number of unique values of the concatenated input remains small. Hence, the embedding space dimensionality need not be large. While the names of executing activities and lifecycle transitions for most datasets usually have a small set of values, the set of resources or organizational groups may be much larger, which limits the feasibility of this approach. Application-specific event-level or case-level attributes can also be included in predictors and predictands simply by concatenating their values. This too is limited to cases where the set of unique values is small. Numerical attributes are dificult to handle in our approach unless they are encoded in a limited number of intervals, which may lead to significant information loss.

A different approach, first encoding individual attributes and subsequently concatenating the embedding vectors for input to the RNN, can keep the RNN input size small even when the number of unique values for some attributes is large, and also simplifies including numerical attributes. Exploring this alternative and its predictive performance, and determining ways to identify event- and case-level attributes that are useful as predictor variables, are important future work.

## Acknowledgments

The authors gratefully acknowledge the support of the Memorial University Center for Health Informatics and Analytics, St. John’s, Canada and the Hasso-Plattner-Institute at the University of Potsdam, Germany, in providing access to computing resources.

## References

[1] C. Houy, P. Fettke, P. Loos, W.M.P. van der Aalst, J. Krogstie, BPM-in-the-large - towards a higher level of abstraction in business process management EGES/GISP. Vol. 334 of IFIP Advances in Information and Communication Technology. Springer 2010 pn 233-244

[2] D. Breuker, M. Matzner, P. Delfmann, J. Becker, Comprehensible predictive models for business processes, MIS Q. 40 (4) (2016) 1009–1034.

[3] J. Schmidhuber, Deep learning in neural networks: an overview, Neural Netw. 61 (2015) 85–117.

[4] Y. LeCun, Y. Bengio, G. Hinton, Deep learning, Nature 521 (2015) 436–444.

[5] I. Sutskever, J. Martens, G.E. Hinton, Generating text with recurrent neural networks, ICML, Omnipress. 2011, pp. 1017–1024.

[6] A. Graves, Generating sequences with recurrent neural networks, CoRR abs/1308. (2013) 0850.

[7] W. Zaremba, I. Sutskever, O. Vinyals, Recurrent neural network regularization, CoRR abs/1409. (2014) 2329.

[8] S. Gregor, A.R. Hevner, Positioning and presenting design science research for maximum impact, MIS Q. 37 (2) (2013) 337–355.

[9] J. Evermann, J.-R. Rhese, P. Fettke, A deep learning approach for predicting process behaviour at runtime, PRAISE Workshop at the 14th International Conference on BPM, 2016.

[10] W.M.P. van der Aalst, M. Pesic, M. Song, Beyond process mining: from the past to present and future, in: B. Pernici (Ed.), Advanced Information Systems Engineering: 22nd International Conference, CAiSE 2010, Hammamet, Tunisia, June 7–9, 2010. Proceedings, Springer, Berlin, Heidelberg, 2010, pp. 38–52.

[11] M. Ceci, P.F. Lanotte, F. Fumarola, D.P. Cavallo, D. Malerba, Completion time and next activity prediction of processes using sequential pattern mining, Discovery Science - 17th International Conference, DS 2014, Bled, Slovenia, October 8–10, 2014. Proceedings, 2014. pp. 49–61.

[12] G.T. Lakshmanan, D. Shamsi, Y.N. Doganata, M. Unuvar, R. Khalaf, A Markov prediction model for data-driven semi-structured business processes, Knowl. Inf. Syst. 42 (1) (2015) 97–126.

[13] M. Le, B. Gabrys, D. Nauck, A hybrid model for business process event prediction, SGAI Conf., Springer. 2012, pp. 179–192

[14] M. Unuvar, G.T. Lakshmanan, Y.N. Doganata, Leveraging path information to generate predictions for parallel business processes, Knowl. Inf. Syst. 47 (2) (2016) 433–461.

[15] B. van Dongen, Business Process Intelligence 2012 Challenge Data Set, 2012, http://10.4121/uuid:3926db30-f712-4394-aebc-75976070e91f.

[16] B. van Dongen, Business Process Intelligence 2013 Challenge Data Set (Closed Problems), 2013, http://10.4121/uuid:c2c3b154-ab26-4b31-a0e8- 8f2350ddac11.

[17] B. van Dongen, Business Process Intelligence 2013 Challenge Data Set (Incident Management), 2013, http://10.4121/uuid:500573e6-accc-4b0c-9576- aa5468b10cee.

[18] T. Mikolov, S. Kombrink, L. Burget, Cernock<sup>ˇ</sup> y. J., S. Khudanpur, Extensions of\` recurrent neural network language model, in: Acoustics, Speech and Signal Processing (ICASSP), 2011 IEEE International Conference on, pp. 5528–5531.

[19] A. Graves, Supervised Sequence Labelling With Recurrent Neural Networks, Vol. 385 of Studies in Computational Intelligence Springer. 2012.

[20] S. Hochreiter, J. Schmidhuber, Long short-term memory, Neural Comput. 9 (8) (1997) 1735–1780.

[21] F.A. Gers, J. Schmidhuber, Recurrent nets that time and count, IJCNN (3), 2000. pp. 189-194

[22] K. Greff, R.K. Srivastava, J. Koutník, B.R. Steunebrink, J. Schmidhuber, LSTM: a search space odyssey, CoRR abs/1503 (2015) 04069.

[23] XES Working Group, IEEE standard for eXtensible Event Stream (XES) for achieving interoperability in event logs and event streams, IEEE Std. 2016, 1849–2016.

[24] H.W. Lin, M. Tegmark, Critical behavior from deep dynamics: a hidden dimension in natural language, CoRR abs/1606 (Jun. 2016) 06737.

[25] G.K. Zipf, Human Behavior and the Principle of Least Effort, 1949.

[26] S. Bahrampour, N. Ramakrishnan, L. Schott, M. Shah, Comparative study of deep learning software frameworks, CoRR abs/1511 (2015) 06435.

[27] N. Srivastava, G.F. Hinton, A. Krizheysky, I. Sutskever, R. Salakhutdinoy. Dropout: a simple way to prevent neural networks from overfitting, J. Mach. Learn. Res. 15 (1) (2014) 1929–1958.

[28] W.M.P. van der Aalst, M. Bichler, A. Heinzl, Open research in business and information systems engineering, Bus. Inf. Syst. Eng. 58 (6) (2016) 375–379.

[29] T. Hastie, R. Tibshirani, J. Friedman, The Elements of Statistical Learning: Data Mining, Inference, and Prediction, Springer Verlag, Berlin, Germany, 2009.

[30] A. Karpathy, The Unreasonable Effectiveness of Recurrent Neural Networks, 2016.Accessed 6 Dec. 2016.

[31] A. van den Oord, S. Dieleman, H. Zen, K. Simonyan, O. Vinyals, A. Graves, N. Kalchbrenner, A.W. Senior, K. Kavukcuoglu, Wavenet: a generative model for raw audio, CoRR abs/1609 (2016) 03499.

[32] A. Huang, R. Wu, Deep learning for music, CoRR abs/1606. (2016) 04930

[33] K. Choi, G. Fazekas, M.B. Sandler, Text-based LSTM networks for automatic music composition, CoRR abs/1604. (2016) 05358

[34] A.J.M.M. Weijters, J.T.S. Ribeiro, Flexible heuristics miner (FHM), CIDM. IEEE. 2011, pp. 310–317.

[35] J. Claes, G. Poels, Process mining and the ProM framework: an exploratory survey, Business Process Management Workshops, Vol. 132 of Lecture Notes in Business Information Processing, Springer. 2012, pp. 187–198.

[36] W.M.P. van der Aalst, A. Adriansyah, B.F. van Dongen, Replaying history on process models for conformance checking and performance analysis. Wiley Interdisc, Rew. Data Min. Knowl. Disc. 2 (2) (2012) 182–192.

[37] A. Karpathy, J. Johnson, F. Li, Visualizing and understanding recurrent networks, CoRR abs/1506 (2015) 02078.

[38] J. Li, X. Chen, E.H. Hovy, D. Jurafsky, Visualizing and understanding neural models in NLP, CoRR abs/1506 (2015) 01066.

[39] J. Yosinski, J. Clune, A.M. Nguyen, T. Fuchs, H. Lipson, Understanding neural networks through deep visualization, CoRR abs/1506 (2015) 06579.

[40] H. Strobelt, S. Gehrmann, B. Huber, H. Pfister, A.M. Rush, Visual analysis of hidden state dynamics in recurrent neural networks, CoRR abs/1606 (2016) 07461.

[41] L.v.d. Maaten, G. Hinton, Visualizing data using t-SNE, J. Mach. Learn. Res. 9 (Nov) (2008) 2579–2605.

Dr. Joerg Evermann received his PhD in Information Systems from the University of British Columbia. Prior to becoming a faculty member at Memorial University, Dr. Evermann was a lecturer in Information Systems with the School of Information Management at the University of Wellington, New Zealand. Dr. Evermann’s interests are in business process management, statistical research methods, and information integration. Dr. Evermann has published his research in more than 70 peer-reviewed publications. His work has appeared in high-quality journals, such as IEEE Transactions on Services Computing, IEEE Transactions on Software Engineering, IEEE Transactions on Knowledge and Data Engineering, Organizational Research Methods, Structural Equation Modeling, Journal of the AIS, Information Systems, and Information Systems Journal. Dr. Evermann has presented his work at international conferences and workshops, such as ICIS, AMCIS, CAiSE, ER, among others.

Jana-Rebecca Rehse works as a researcher at the Institute for Information Systems (IWi) at the German Research Center for Artificial Intelligence (DFKI). Before that, she was a research assistant at the same institute since 2011. Jana obtained a Bachelor’s Degree in Information Systems from Saarland University, Saarbrcken, Germany in 2012 and a consecutive Master’s Degree in 2015. In 2014, she spent six months as a visiting research scholar at Stevens Institute of Technology in Hoboken, NJ, where she conducted research for her Master’s thesis. Jana’s research interests include Business Process Management, in particular Reference Modeling, Process Mining and Design Science. She is interested in finding algorithmic solutions to practically relevant problems. The findings from her research have been published in outlets such as the International Journal on Software and Systems Modeling (SoSyM) and in various conference proceedings (e.g. WI, ECIS, and BPM Workshops).

Peter Fettke works as a professor for Business Informatics at Saarland University and is a principal researcher at the German Research Center for Artificial Intelligence (DFKI), both Saarbrcken, Germany. He is conducting research in the field of Business Informatics/Information Systems, an important, relatively new discipline at the intersection of Computer Science and Business Administration. His research interests focus on business process management and technologies and include business information systems modeling, business engineering, applications, and philosophy of information systems. He uses a broad spectrum of research methods comprising engineering methods/design science and empirical/experimental research approaches. Peter obtained a Master’s Degree in Business Informatics from the University of Mnster, Germany, a Ph.D. Degree in Business Informatics from the Johannes Gutenberg-University Mainz, Germany, and a Habilitation Degree in Business Informatics from Saarland University, Germany. In 2013 he became a DFKI Research Fellow. Peter has taught and researched previously at the Technical University of Chemnitz and the University Mainz, Germany.

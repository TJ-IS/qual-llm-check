---
otero_id: 5702
otero_key: "9YYJ3VQ8"
title: "Process mining on noisy logs — Can log sanitization help to improve performance?"
authors: "Hsin-Jung Cheng; Akhil Kumar"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.08.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Process mining on noisy logs — Can log sanitization help to improve performance?

Hsin-Jung Cheng <sup>a</sup>, Akhil Kumar <sup>b,</sup>⁎

<sup>a</sup> Department of Industrial Management, National Taiwan University of Science and Technology, Taipei 106, Taiwan

<sup>b</sup> Department of Supply Chain and Information Systems, Smeal College of Business, The Pennsylvania State University, University Park, PA 16802, USA

## a r t i c l e i n f o

Article history: Received 4 November 2014 Received in revised form 10 August 2015 Accepted 12 August 2015 Available online 21 August 2015

Keywords: Process mining Benchmarking Noisy data Log sanitization Metrics Rules

## a b s t r a c t

Process mining techniques are designed to read process logs and extract process models from them. However, real world logs are often noisy and such logs produce bad, spaghetti-like process models. We propose a technique to sanitize noisy logs by first building a classifier on a subset of the log, and applying the classifier rules to remove noisy traces from the log. The improvement in the quality of the resulting process models is evaluated on synthetic logs from benchmark models of increasing complexity on both behavioral and structural recall and precision metrics. The results show that mined models produced from such preprocessed logs are superior on several evaluation metrics. They show better fidelity to the reference models, and are also more compact with fewer elements. A nice feature of the rule based approach is that it generalizes to any noise pattern since the nature of noise varies from one log to another. The rules can also be explained and may be further modified manually We also give results from experiments with a real dataset

© 2015 Elsevier B.V. All rights reserved

## 1. Introduction

Process mining [1] is a technique that helps to extract process related knowledge (e.g., process models) from event logs and exploit it for further analysis. Event logs record the start and/or completion of various tasks in a process instance. The process models extracted from such logs using process mining algorithms are called “mined” models, and they describe the actual behavior of a business process. In the real world, process models have been extracted from logs in healthcare [2–4], local municipalities [5], semiconductor manufacturing [6], telephone repair [7], rental agencies [7], etc. In contrast to data mining, where the focus is on analyzing transaction data (about products, customers, sales, defects, etc.) to discover patterns and trends, process mining focuses on a different kind of patterns, i.e., those related to understanding relationships among activities in a specific business process. An improved understanding of process models through process mining leads to better decision making.

In process mining, our interest lies in understanding the structure and behavior of the relationships among activities. By analyzing process data in the form of actual process execution instances, we can discover patterns of how activities are performed with respect to one another.

This analysis is very helpful in understanding the evolution of process models and improving them. It also helps in checking if an actual process in the real world (say, a medical treatment process) conforms to a given process model, and, if not, the extent to which it deviates. Process mining and data mining have similar objectives, i.e., to discover patterns and knowledge from large amounts of data. However, in data mining the patterns relate to relationships among data values (e.g., sales are higher in winter than in summer), while in process mining the patterns relate to specific ordering of activities with respect to one another (e.g., payment occurs after shipment). By discovering and combining such patterns, process mining techniques are able to generate complete process models from logs.

As a simple example of process mining, consider the log of a customer's browsing behavior. By analyzing such a log and building a process model for it, one can gain a better understanding of whether the user does single-tasking or multi-tasking among sites, how many sites she visits in one session, if she revisits the same site(s) within a session, does she browse only or interact as well (say, by posting comments, or make purchases), etc. A medical treatment log can be “mined” to discover a process model that reflects normal procedures. Deviances from this model (for instance an omitted diagnostic test prior to surgery) may indicate lapses in treatment.

Real world logs are often noisy because some of their (sub-) traces are duplicated, incomplete, inconsistent, or reflect some other incorrect behavior. These problems can result from data entry problems, faulty data collection instruments, data transmission or streaming problems and other technology limitations. Traces may be incomplete when certain events are missed. They could be incorrect because of recording errors. Further, inconsistencies can arise from naming conventions. Noise can also appear from transcription errors when events arrive in the wrong order. Sometimes infrequent correct behavior is also confused with noise. Such behavior usually indicates the execution of exceptional paths in the process.

Thus, it can often become difficult to distinguish between noise and low-frequency correct behavior in an event log resulting in a mined model with less fidelity to the real model. With enterprises maintaining repositories containing hundreds or thousands of event logs for different business processes, distinguishing noise in a log from correct behavior is a major problem.

The initial process mining algorithms were designed for handling noise-free event logs. But later works proposed algorithms to address noisy event logs. Agrawal, Gunopulos, and Leymann [8] were the first to apply process mining to a workflow management system. They proposed a method that automatically derives a formal model of a process from an event log. Also, they attempted to deal with noise through their proposed directed graph based algorithm. Noise was introduced by inserting erroneous activities in the log, not logging some activities that occurred, or reporting some activities in out of order time sequence. Hwang and Yang [9] proposed another directed graph based algorithm for modeling the existing processes automatically by a noise tackling mechanism to tolerate noise in the log.

Weijters and van der Aalst [10] and Weijters et al. [11] introduced Heuristics Miner, a heuristic-based approach for process mining that detects short loops and non-free-choice structures from noisy logs by considering all task pair dependencies and their frequencies. This method is based on keeping track of the frequencies of causal relationships between adjacent tasks in a log and deriving a process model based on these relationships after discarding relationships that occur infrequently as errors based on a threshold value. The Genetic Miner based on genetic principles of mutation and crossover for process discovery was proposed by Medeiros et al. [12], and they showed by experiments that it performs reasonably well with noisy logs. It can also detect non-local relationships that are not explicit in event logs based on its global search ability. An extensive survey of processing mining methods appears in [13].

Previous benchmarking studies for evaluating process mining algorithms have evaluated Heuristic Miner [11], Genetic Miner [12] and also compared Alpha algorithm [1], and Alpha++ algorithm [14]. Our current work was inspired by these and other efforts; however, our main focus here is on understanding the extent to which noise removal or “log sanitization” helps to improve the mined models.

Here, we first develop benchmark models of increasing complexity for evaluating the performance of various algorithms on both noisefree and noisy logs. These synthetic logs are created from a noise generation model. Next, we test the performance of various algorithms on these models on two metrics with varying amounts of noise present in the log. Finally, we train a classifier to mark noisy records in a log and test the performance of the algorithms on the sanitized logs. Thus, we can gain insights into the behavior of process mining algorithms on noisy vs. sanitized logs. To the best of our knowledge this is the first effort of its kind.

This paper is organized as follows. Section 2 presents the basic notions used to represent a Petri net (PN), the concept of process mining and a framework for process mining research. Section 3 presents benchmark metrics and process models, and results for noisy logs. Section 4 starts with a noise generation model, and then describes a rule-based algorithm for removing noise from a log to sanitize it. The experimental setup and results comparing the mined models from noisy and sanitized logs with the reference models are discussed in Section 5. Section 6 gives results from a real dataset and Section 7 provides an overview of related work and limitations of our work. Finally, Section 8 concludes the paper.

## 2. Preliminaries

In this section we discuss Petri nets, process mining and how we generate a synthetic noisy log.

## 2.1. Petri net (PN)

A Petri net (PN) is a common tool for graphically and mathematically modeling the states of concurrent, parallel, asynchronous, and distributed controls systems, e.g., a process model [15]. PNs are directed bipartite graphs with two types of nodes (i.e., places and transitions) [15]. Places and transitions are depicted as circles and rectangles, respectively. The directed arcs are used to connect two nodes of different types in a PN. The definition and related concepts of PNs are as follows:

Definition 1. Petri net [15] A Petri Net is a tuple $N _ { 1 } = ( P , T , F )$ where

\\ P is a finite set of places.

\\ T is a finite set of transitions such that $P \cap T = \phi .$

$F \subseteq ( P \times T ) \cup ( T \times P )$ is a set of arcs (flow relation).

\\ A place $p \in P$ is an input place of a transition t ∈ T if and only if there exists a directed arc from p to $t , \mathrm { i } . e . , ( p , t ) \in F .$

\\ A place $p \in P$ is an output place of a transition t ∈ T if and only if there exists a directed arc from t to p, i.e., (t, p) ∈ F.

As shown in Fig. $1 , P = \{ p _ { 1 } , p _ { 2 } , \cdots , p _ { 1 3 } \} , T = \{ t _ { 1 } , t _ { 2 } , \cdots , t _ { 1 3 } \}$ , and F indicate all arcs that connect places and transitions. The marking (or state) $M _ { 1 }$ of a PN is represented by black tokens distributed over one or more places (see $p _ { 1 }$ in Fig. 1). A transition t is enabled if there is at least one token in each input place $p , ( p , t ) \in F .$ If an enabled transition t fires, it removes one token from each of its input places $p _ { 1 } , ( p _ { 1 } , t ) \in F$ and generates one token in each of its output places $p _ { 2 } , ( t , p _ { 2 } ) \in F .$

Based on the causal relationships among its elements four basic structure types of a PN can be classified as sequence (SEQ), parallel (AND), exclusive-choice (XOR), and iteration (Loop) as illustrated in Fig. 1.

## 2.2. Process mining concept and framework

Fig. 2 shows the concept of process mining. Information systems generate a lot of data that is stored in event logs. Such logs can be analyzed to detect abnormal behavior such as errors or exceptions in the form of missing, unexpected or mistimed events. Process mining techniques aim to extract process models from event logs to gain a better understanding of the actual process which is often different from the prescribed process. An event log records traces showing the sequence of tasks performed for a particular execution of a process case instance. We assume that every time a single task or activity occurs only one event is recorded. Sometimes a trace may also show, in addition to a task, the name or Id of an agent who performs it and a timestamp. To illustrate how process mining techniques work, an event log is shown in Table 1. It contains six traces (representing cases) of a process for obtaining an industrial engineer's license in Taiwan. From these traces, one could observe that a candidate must apply for a license (A) and then pass both the “Operations Management” (B) and “Quality Management” (C) Exams in any order to pass stage 1 (D). Subsequently, anyone out of work study, operations research and ergonomics exams (E–G) must be passed to obtain the license (H). Process mining techniques are based on such reasoning with the event logs to build a process model in the form of the PN model shown in Fig. 3.

![](/api/attachments/9YYJ3VQ8/fulltext/images/a65632a6b0ac6382f66df127dd432e2fcbab5380fbdb3a4188e3257c6a918c47.jpg)  
Fig. 1. Example of a Petri net with different types of process modeling structures

Although the algorithms vary widely in their approaches, a framework for understanding process mining algorithms may be broadly organized along two key dimensions as follows:

D1 Algorithms for noise-free logs (NF) vs. algorithms for mining noisy logs (N).

D2 Algorithms that consider quality of process models (Q) vs. algorithms that do not (NQ).

Table 2 summarizes the various algorithms into this framework. Algorithms such as Alpha [1] and Alpha++ algorithms [14] were designed for noise free logs. They mine a structured workflow model from a log by identifying sequence, parallel and choice relationships. Cook and Wolf [16] applied process mining to obtain a model from event logs in the software engineering context. They described three methods: based on neural networks, prefix trees, and Markov chains. Although their Markovian algorithm could deal with sequential patterns such as Markov chains, it could not suitably handle concurrent behavior. Later, Cook and Wolf [17] extended their work to the discovery of process models of concurrent processes. They proposed specific metrics, including entropy, event type counts, periodicity and causality, for extracting process models from an event stream.

Later algorithms, notably the Heuristics Miner [10] and the Genetic algorithm [12], were designed for noisy logs. Subsequent work explored different variations and approaches, and also introduced notions of quality. The notion of quality of a process model was first introduced by Rozinat and van der Aalst in terms of fitness and specificity [18]. Fitness or fidelity is the degree to which the model explains a log, and specificity or precision is the degree to which a model is specific to a given log. Evolutionary Tree Miner (ETM) was proposed as an extension of the Genetic algorithm [19]. It combines multiple aspects of quality such as fitness, simplicity, precision and generalization. The Fuzzy Miner creates hierarchical models at different levels of detail [20].

The Parikh language-based region miner [21] exploits the similarity between a process model and language models, and builds on the theory of regions that tries to synthesize a Petri net which can reproduce the language as precisely as possible. An Integer Linear Programming based algorithm is discussed in [21]. The idea behind the skeletal algorithm of Przybylek [22] is to express a problem in terms of congruences on a structure, build an initial set of congruences, and improve it by taking limited unions/intersections, until a suitable condition is reached. A drawback is that the algorithm is not able to mine nodes corresponding to parallel executions of a process. A quality-based process mining algorithm is discussed in [23]. This algorithm creates a block structured model based on 6 structures: sequence, parallel, choice, loop, self-loop and optional task/ block to maximize quality for a given noise level in a log. For more details on various process mining algorithms, see [13].

![](/api/attachments/9YYJ3VQ8/fulltext/images/6d2ab9164beb0dfb944ab261f0c5a989036750e237ced744202870b95054d85e.jpg)  
Fig. 2. Overview of how process mining works

## 3. Benchmark metrics and process models

Our general approach in this paper is to generate noisy logs from reference process models and then mine process models by applying process mining algorithms to both the noisy log and the sanitized version of the same log. By comparing the discovered models from these two logs with the original reference model we can understand the effect of sanitization on the noisy log. Hence, we need metrics to compare the similarity between any pair of process models. In the real world we might not always have a reference model, in which case we can evaluate a model by its own metrics of quality and correctness as discussed in Section 5. Nevertheless, by assuming that a reference model is available, our approach still allows us to determine the extent to which sanitization can help to improve the process mining performance. In addition to metrics, this section also introduces benchmark reference process models and gives results for noisy logs.

## 3.1. Benchmark metrics

To determine similarity between two process models, say a reference and a mined model, one must consider both the behavioral and structural similarity between them [12].

Table 1  
An event log with six process traces.

<table><tr><td>Case id</td><td>Process trace</td></tr><tr><td>1</td><td>ABCDEH</td></tr><tr><td>2</td><td>ACBDEH</td></tr><tr><td>3</td><td>ABCDFH</td></tr><tr><td>4</td><td>ACBDFH</td></tr><tr><td>5</td><td>ABCDGH</td></tr><tr><td>6</td><td>ACBDGH</td></tr></table>

![](/api/attachments/9YYJ3VQ8/fulltext/images/23007c17b9ddf1121f58b93a9beddd836a562b8bb6d1fcfd87dd00970d80e170.jpg)  
Fig. 3. A Petri-net model mined from the event log in Table 1.

The behavioral similarity metrics measure the similarity in behavior between two models in terms of precision and recall [12]. These metrics analyze the event log to quantify how similar the behavior of, say, the mined model is to that of its reference model. This is done by replaying each trace against the two models and calculating how many transitions (or tasks) are enabled in each model at the occurrence of every event in the trace. The more enabled tasks the two models have in common, the higher is the similarity between them. Both metrics are also based on the causality relations of the mined and reference models. A causality relation is derived from the Petri-net. A causality (or cause–effect) relation exists between two activities, say A1, A2, if the output of A1 is an input for A2. In Fig. $4 ( \mathsf { a } )$ , there is a causality relation between A and B (C, D or E). The above metrics use the number of causality relations the mined and the reference models have in common.

Definition 2. (Behavioral precision and recall) [12] Some parameters are defined as follows:

σ a trace in an event log.

$L ( \sigma )$ the number of occurrences of σ in an event log.

$\Nu _ { \mathrm { r } }$ and $\Nu _ { \mathrm { m } }$ the respective Petri nets for the reference and the mined models.

C and $C _ { \mathrm { m } }$ the respective causality relations for $\Nu _ { \mathrm { r } }$ and $\mathrm { N } _ { \mathrm { m } } .$

Now, the behavioral precision and recall are defined as:

$$
\mathrm{B} _ {\mathrm{p}} (\mathrm{L}, \mathrm{C} _ {\mathrm{r}}, \mathrm{C} _ {\mathrm{m}}) = \left(\sum_ {\sigma \in \mathrm{L}} \left(\frac {\mathrm{L} (\sigma)}{| \sigma |} \times \sum_ {\mathrm{i} = 0} ^ {| \sigma | - 1} \frac {| \text { Enabled } (\mathrm{C} _ {\mathrm{r}} , \sigma , \mathrm{i}) \cap \text { Enabled } (\mathrm{C} _ {\mathrm{m}} , \sigma , \mathrm{i}) |}{| \text { Enabled } (\mathrm{C} _ {\mathrm{m}} , \sigma , \mathrm{i}) |}\right)\right) / \sum_ {\sigma \in \mathrm{L}} \mathrm{L} (\sigma)
$$

$$
B _ {R} (L, C _ {r}, C _ {m}) = \left(\sum_ {\sigma \in L} \left(\frac {L (\sigma)}{| \sigma |} \times \sum_ {i = 0} ^ {| \sigma | - 1} \frac {| E n a b l e d (C _ {r} , \sigma , i) \cap E n a b l e d (C _ {m} , \sigma , i) |}{| E n a b l e d (C _ {r} , \sigma , i) |}\right)\right) / \sum_ {\sigma \in L} L (\sigma)
$$

where. Enabled $| ( \mathsf { C } _ { \Gamma } , \mathbf { O } , \dot { \mathbf { l } } )$ : the set of enabled activities when parsing the next event (or task) after position i in trace σ [12]. For the example of Fig. 4 which includes a trace $\sigma = \mathrm { \Omega } ^ { \ast } \mathrm { A E B C D F }$ ”, in the reference model (Fig. 4(a)), Enabled $( \mathsf { C } _ { \mathrm { r } } , \sigma , 1 ) = \{ \mathsf { B } , \mathsf { C } , \mathsf { D } , \mathsf { E } \}$ because this set of tasks is enabled after task A at position 1 is executed. So, |Enabled $( \mathsf { C } _ { \Gamma } , \sigma , \mathrm { i } ) | = 4$ However, in the mined model (Fig. 4(b)), Enabled $( \mathsf { C } _ { \mathrm { m } } , \mathsf { \sigma } , 1 ) = \{ \mathsf { B } , \mathsf { C } , \mathsf { D } \}$

A framework for characterizing various process mining algorithms

<table><tr><td></td><td>Noise-free logs (NF)</td><td>Noisy logs (N)</td></tr><tr><td rowspan="5">Quality aware (Q)</td><td>Alpha++ algorithm [14]</td><td>Directed graph based algorithm [8,9]</td></tr><tr><td>Parikh language-based region miner [21]</td><td>Heuristics Miner [11]</td></tr><tr><td>Skeletal-based algorithm [22]</td><td>Genetic algorithm [12]</td></tr><tr><td></td><td>Quality-based algorithm [23]</td></tr><tr><td></td><td>Event-based algorithms [16] [17]</td></tr><tr><td rowspan="2">Quality non-aware (NQ)</td><td>Alpha algorithm [1]</td><td>Heuristic process mining [10]</td></tr><tr><td>Evolutionary Tree Miner [19]</td><td></td></tr></table>

Thus, the set $S 1 = \mathrm { E n a b l e d } ( \mathrm { C _ { r } , \mathrm { \mathrm { 0 , i } } } )$ ∩ Enabled $( \mathsf { C } _ { \mathrm { m } } , \sigma , \mathrm { i } ) = \{ \mathsf { B } , \mathsf { C } , \mathsf { D } \}$ . Hence, $\left| { \mathsf { S } } 1 \right| = 3$

The value of both behavioral precision and recall metrics lies in the [0, 1] range. A value close to 1 indicates very high degree of similarity between the two models. The behavioral precision reflects how much of the behavior of the mined model is also in the reference model. The behavioral recall reflects how much of the behavior of the reference model also occurs in the mined model.

To appreciate the concept of behavioral precision and recall, consider the example in Fig. 4. It shows a reference model, a synthetic log (log L) of actual execution traces based on a reference model $( \mathrm { F i g . } 4 ( \mathsf { a } ) )$ , and a mined model (Fig. 4(b)) generated from the log. For this example:

$$
\begin{array}{l} B _ {P} (L, C _ {r}, C _ {m}) = ((2 / 6 ^ {*} (1 / 1 + 3 / 3 + 2 / 2 + 1 / 1 + 1 / 1 + 1 / 1) \\ \qquad + 3 / 6 ^ {*} (1 / 1 + 3 / 3 + 2 / 2 + 1 / 1 + 1 / 1 + 1 / 1) \\ \qquad + (2 / 6 ^ {*} (1 / 1 + 3 / 3 + 2 / 2 + 1 / 1 + 1 / 1 + 1 / 1) \\ \qquad + (2 / 6 ^ {*} (1 / 1 + 3 / 3 + 3 / 4 + 2 / 3 + 1 / 2 + 1 / 1) \\ \qquad + 3 / 6 ^ {*} (1 / 1 + 3 / 3 + 3 / 4 + 2 / 3 + 1 / 2 + 1 / 1) \\ \qquad + (2 / 6 ^ {*} (1 / 1 + 3 / 3 + 2 / 2 + 2 / 3 + 1 / 2 \\ \qquad + 1 / 1)) / 1 4 = 0. 9 1. \end{array}
$$

And,

$$
\begin{array}{l} B _ {R} (L, C r, C m) = ((2 / 6 ^ {*} (1 / 1 + 3 / 4 + 2 / 3 + 1 / 2 + 1 / 1 + 1 / 1) \\ \qquad + (3 / 6 ^ {*} (1 / 1 + 3 / 4 + 2 / 3 + 1 / 2 + 1 / 1 + 1 / 1) \\ \qquad + (2 / 6 ^ {*} (1 / 1 + 3 / 4 + 2 / 3 + 1 / 2 + 1 / 1 + 1 / 1) \\ \qquad + (2 / 6 ^ {*} (1 / 1 + 3 / 4 + 2 / 3 + 2 / 2 + 1 / 1 + 1 / 1) \\ \qquad + (3 / 6 ^ {*} (1 / 1 + 3 / 4 + 2 / 3 + 2 / 2 + 1 / 1 + 1 / 1) \\ \qquad + (2 / 6 ^ {*} (1 / 1 + 3 / 4 + 2 / 3 + 2 / 2 + 1 / 1 \\ \qquad + 1 / 1)) / 1 4 = 0. 8 6. \end{array}
$$

The results $( B _ { P } = 0 . 9 1$ and $B _ { R } = 0 . 8 6 )$ reflect that for the given log the mined model is close to the reference model on both the precision and recall metrics

For structural similarity, the structural precision and recall metrics [12] are used. The structural recall reflects the number of correct causality relations present in the mined model as a fraction of the total number of causality relations in the reference model. The structural precision reflects the fraction of correct causality relations present in the mined model.

Definition 3. (Structural precision and recall) [12] Let ${ \sf N } _ { \mathrm { r } } = ( { \sf P } _ { \mathrm { r } } , { \sf T } _ { \mathrm { r } } , { \sf F } _ { \mathrm { r } } )$ and $\mathsf { N } _ { \mathrm { m } } = ( \mathrm { P } _ { \mathrm { m } } , \mathrm { T } _ { \mathrm { m } } , \mathrm { F } _ { \mathrm { m } } )$ be respective Petri nets for the reference and mined models. Let $C _ { \mathrm { r } }$ and $C _ { \mathrm { m } }$ be the respective causality relations for $\Nu _ { \mathrm { r } }$ and $\mathrm { N } _ { \mathrm { m } } .$ The structural precision and structural recall are defined as:

$$
S _ {\mathrm{p}} (N _ {\mathrm{r}}, N _ {\mathrm{m}}) = \frac {| C _ {\mathrm{r}} \cap C _ {\mathrm{m}} |}{| C _ {\mathrm{m}} |}
$$

$$
S _ {R} (N _ {r}, N _ {m}) = \frac {| C _ {r} \cap C _ {m} |}{| C _ {r} |}.
$$

Both structural precision and recall are in the range [0, 1]. A value close to 1 means they are very similar structurally. Given N and $\Nu _ { \mathrm { m } }$ as the two Petri nets shown in Fig. 4, we can calculate the structural precision and recall metrics as follows:

![](/api/attachments/9YYJ3VQ8/fulltext/images/ade8d8fb577dffed20df03f038563817dca3606668d961c4979981221a7b9731.jpg)  
Fig. 4. Example of a reference model, a mined model, and a log L.

![](/api/attachments/9YYJ3VQ8/fulltext/images/84ce521ab7b5ce2e586f46515c65b256643f69d9360bbead1108849e0c4d4eaa.jpg)

The results $\left( S _ { \mathrm { R } } < S _ { \mathrm { p } } < 1 \right)$ reflect that the mined model has a higher structural precision than recall.

## 3.2. Benchmark process models

For benchmarking process mining algorithms, six reference process models of increasing complexity (levels 0 through 5) were created by us using four basic structures of a process (i.e., sequence, parallel, exclusive-choice, and loop). Fig. 5 shows these models as Petri-nets. Fig. 5(a) is a model with a straight sequence. Figs. 5(b) and (c), respectively, incorporate parallel and exclusive-choice structures into a sequence structure. Fig. 5(d) combines a parallel and an exclusivechoice structure into a sequence structure. Fig. 5(e) shows a model that contains a parallel structure, an exclusive-choice structure, a loop structure, and a sequence structure. Finally Fig. 5(f) shows a still more complex model with two interacting loops.

![](/api/attachments/9YYJ3VQ8/fulltext/images/fbd9cf890aa5dab81d1b40cd08a1bdc14e17e2858a944727ec0adf874a7124e4.jpg)  
Fig. 5. Six reference models used in benchmarking process mining algorithms.

Table 4  
Table 3  
Experimental results for Level 4 logs with noise (Average values for 5 × 10 experiments).

<table><tr><td>Level 4</td><td colspan="5">Alpha++</td><td colspan="5">HM</td></tr><tr><td>% of noise</td><td>0%</td><td>2%</td><td>5%</td><td>10%</td><td>20%</td><td>0%</td><td>2%</td><td>5%</td><td>10%</td><td>20%</td></tr><tr><td>Behav. Prec.</td><td>1</td><td>0.050</td><td>0</td><td>0</td><td>0</td><td>0.932</td><td>0.847</td><td>0.796</td><td>0.794</td><td>0.719</td></tr><tr><td>Behav. Recall</td><td>1</td><td>0.129</td><td>0</td><td>0</td><td>0</td><td>0.932</td><td>0.934</td><td>0.926</td><td>0.909</td><td>0.907</td></tr><tr><td>Struc. Prec.</td><td>1</td><td>0.244</td><td>0.168</td><td>0.072</td><td>0.012</td><td>1</td><td>0.955</td><td>0.922</td><td>0.849</td><td>0.753</td></tr><tr><td>Struc. Recall</td><td>1</td><td>0.630</td><td>0.180</td><td>0.130</td><td>0.040</td><td>1</td><td>0.880</td><td>0.870</td><td>0.855</td><td>0.820</td></tr></table>

## 3.3. Benchmarking algorithms on noisy logs

In this section we give results from testing two algorithms on our metrics with varying amounts of noisy data. We tested two wellknown algorithms: Alpha++ [14] and Heuristics Miner or HM [11, 10]. Alpha++ is based on using strict rules of causality to determine relationships among tasks in a process. Weijters et al. [11] presented HM in detail by extending a previous “Little Thumb” algorithm of Weijters and van der Aalst [10]. This algorithm is based on determining metrics for all pairs of tasks to compute dependency scores. Then heuristic rules are applied to dependency scores to detect direct causal relationships, and choice and parallel relationships, to create a mined model. The algorithm can run with default values, or a user can adjust parameters such as dependency threshold and positive observations threshold to ne tune the algorithm. These thresholds are the minimum cutoff values required for establishing dependency relations between activities. We generated synthetic logs with 1000 process traces in each one at 5 different noise levels: 0%, 2%, 5%, 10% and 20%. Noise was added by operations like deleting a random task, swapping two tasks, and duplicating a task. The noise generation model is described in detail shortly.

We found that HM can discover correct models from logs for reference models at levels 0 to 3 (i.e., behavioral precision and recall are both equal to 1) for all levels of noise above 0%. The performance of Alpha++ was far inferior in all cases even at small levels of noise. Since HM could give us perfect results, we focused our experiments on understanding the behavior of the algorithms at levels 4 and 5 where the reference models are more complex.

Table 3 shows the average results of the benchmark metrics for noisy logs generated from the level 4 model. Alpha++ does markedly better than HM for the noise-free log, but its performance becomes unacceptable even at small levels of noise. Thus, the performance of HM is clearly more interesting to study at length when noise is present in a log. For HM, the decline in the two recall metrics is small (less than 7%), while the decline in the precision metrics is slightly larger (about 22% or less) as the noise increases from 0% to 20%. In fact, behavioral recall is more than 90% even at 20% noise, which shows that a lot of the behavior is preserved. All metrics show a performance above 70% at 20% noise level.

The results for the synthetic logs generated from the level 5 model shown in Table 4 are less encouraging. Alpha++ again outperforms HM at 0% noise, but does very poorly even at 2% noise level to merit further consideration. HM declines as well, though less so, on all four metrics as the noise increases to 20%. In fact, the highest metric for HM at 20% noise has a behavior recall of

73%, while structural recall drops to 47%, suggesting that more than half of the structural information is lost. It is clear from the results that HM degrades more gracefully than Alpha++ in the presence of noise. In the next section we explore techniques for removing noise from logs.

## 4. Algorithm for removing noise (log sanitizing)

Now, we explore the idea of first removing noise from a log before extracting a process model from it. Our approach is illustrated in Fig. 6. A given log is divided into a marked sub-log (with a small fraction X% of traces) and an unmarked sub-log (with the remaining traces). We assume that the traces in the marked sub-log are examined manually by an individual, and the correct ones are marked as 1 and the noisy ones as 0. This marked sub-log can be used to build a rule-based classifier that identifies traces as noisy or correct by applying a set of rules. Then, the traces in the unmarked sub-log are marked by applying the classifier rules, and the ones marked noisy are removed to “sanitize” it. Next, we first describe our noise generation model to produce a noisy log and then our approach for making a classifier, and later give the results of experiments on sanitized logs.

## 4.1. Noise generation model

To simulate a noisy event log, three different types of noise generating operations are defined: (i) remove one randomly chosen task, (ii) duplicate one randomly chosen task, and (iii) interchange two randomly chosen tasks. Logs with 2%, 5%, 10%, and 20% of noisy records are generated where each noisy record contains one of these three types of noise. The pseudo-code for generating noise is shown in Table 5. For example, assume a noise-free trace t in the event log like “ABFCIGK” shown in Table 6. If r = 0, then a randomly selected task, say, task C, is deleted and this trace is modified to “ABFIGK.” If r = 1, then a randomly selected task, say, task F is duplicated and a noisy trace “ABFFCIGK” is produced. If r = 2, then two randomly selected tasks, say, A and K are interchanged and this trace becomes “KBFCIGA.” Other related papers also use a similar noise model [12,23]. Moreover, our approach is not specific to a noise model. The rules can characterize any reasonable model.

## 4.2. Algorithm PRISM for generating classification rules

PRISM is a rule-based algorithm [24] and it can induce modular rules with fewer redundancies [24] than the traditional decision tree algorithms [25]. PRISM is a separate-and-conquer kind of algorithm that produces rules such that the attributes in any pair of rules used for classification do not intersect, e.g.,:

Experimental results for Level 5 logs with noise (Average values for 5 × 10 experiments).

<table><tr><td>Level 5</td><td colspan="5">Alpha++</td><td colspan="5">HM</td></tr><tr><td>% of noise</td><td>0%</td><td>2%</td><td>5%</td><td>10%</td><td>20%</td><td>0%</td><td>2%</td><td>5%</td><td>10%</td><td>20%</td></tr><tr><td>Behav. prec.</td><td>1</td><td>0.109</td><td>0.041</td><td>0.020</td><td>0</td><td>0.924</td><td>0.656</td><td>0.551</td><td>0.469</td><td>0.463</td></tr><tr><td>Behav. recall</td><td>0.980</td><td>0.186</td><td>0.127</td><td>0.058</td><td>0</td><td>0.831</td><td>0.739</td><td>0.740</td><td>0.736</td><td>0.727</td></tr><tr><td>Struc. prec.</td><td>1</td><td>0.152</td><td>0.146</td><td>0.162</td><td>0.064</td><td>0.894</td><td>0.892</td><td>0.871</td><td>0.700</td><td>0.623</td></tr><tr><td>Struc. recall</td><td>0.818</td><td>0.504</td><td>0.355</td><td>0.305</td><td>0.141</td><td>0.818</td><td>0.591</td><td>0.525</td><td>0.502</td><td>0.471</td></tr></table>

![](/api/attachments/9YYJ3VQ8/fulltext/images/f92b0d988c4c5b21764416a9470bad3819840e02e19cbb73f12240115eefd496.jpg)  
Fig. 6. Overall approach for log sanitization.

$$
\begin{array}{l} \text {IF a = 1 AND b = 1 THEN class = x} \\ \text {IF c = 1 AND d = 1 THEN class = y.} \end{array}
$$

Table 7 shows the pseudo-code for the PRISM algorithm. First, a rule that covers a subset of the training examples is identified. Next, all traces covered by the rule are separated out from the training set. Then, PRISM recursively learns another rule that covers some of the remaining examples until no examples remain (i.e., the remaining traces are “conquered”) [26]. To evaluate performance of PRISM versus other algorithms for classification, we also considered J48, BFTree and Random Forest, but found that PRISM produced the best results. Moreover, PRISM is a rule-based algorithm. Since it generates rules a human expert can check them and also modify them. Non-rule based algorithms do not offer this benefit.

If two tasks in parallel are exchanged in a trace it is not possible to detect the noise introduced by it. Moreover, when certain loops are involved it may also make it impossible to detect noise. To illustrate, say, AGHFBCGIHJIFGK is a noisy trace because F has been deleted from the middle of GH (the original correct trace was AGFHFBCGIHJIFGK). However, because of the unique nature of the process model where F and G loop around H, the noise is indistinguishable as both GHF and GFH are correct sub-patterns in this trace as long as they are eventually followed by K. We believe that no algorithm can detect such ambiguities that arise due to the inherent nature of the process model and reduce the accuracy percentage. If we ignore such classification errors, the accuracy of PRISM would be even higher. Next, we will report results of process mining experiments on sanitized logs.

## 4.3. Results after applying PRISM rules to sanitize a noisy log

A trace in a process log is a string of task names in the order in which they are performed, e.g., ABCDEFGHIJK is an example log entry from the level 0 model in Fig. 5. Since this is a noise-free log entry it is classified as 1, as opposed to 0 for a noisy log entry such as DBCAEFGHIJK obtained if tasks A and D were swapped. A pair of consecutive log entries is an input attribute for the classification algorithm. Thus, AB, AC,…, BC, BD, BE,…, CD, CE, CF…, etc. are possible input attributes. Table 8 shows an example rule set for classification that was generated for a sample log of 200

The steps of generating a noisy log.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: An event log L, the percentage of generating noise P.
Output: A noisy log N.
(1)  $S \leftarrow$  set of tasks  $s_{1}, s_{2}, \ldots$  in L.
(2)  $N \leftarrow \varphi$ .
(3)  $T \leftarrow$  set of traces which were selected based on P.
(4) For each chosen trace t in L do:
(a) Randomly select an integer r between 0 and 2. Then:
(i) IF r = 0: Randomly remove one task s from t.
(ii) IF r = 1: Randomly duplicate one task s from t.
(iii) IF r = 2: Randomly interchange two tasks (say,  $s_{i}$  and  $s_{j}$ ) from t.
(b)  $N \leftarrow t$ 
(5) Return the noisy log N.
</div>

Table 6  
Three types of noisy traces

<table><tr><td colspan="2">Noise-free trace: ABFCIGK</td></tr><tr><td>Noisy trace</td><td>Reason for noise</td></tr><tr><td>ABFIGK</td><td>Missing task C</td></tr><tr><td>ABFFCIGK</td><td>Duplicated task F</td></tr><tr><td>KBFCIGA</td><td>Interchanged tasks A and K</td></tr></table>

process traces by running the PRISM algorithm implemented in the Weka tool [27]. This is a well-known and widely used open-source tool for data mining and is available at www.cs.waikato.ac.nz/ml weka. Table 8 shows a subset of classification rules generated by PRISM to remove noisy data in a synthetic log of 200 process traces marked either noisy or correct each with 10% of noise at level 5.

As an illustration of the classification accuracy of PRISM, we show the confusion matrix for a specific log, log 1 at level 5 with 10% noise, in Fig. 7(a). Moreover, Fig. 7(b) shows sample log entries that were classified into the four boxes of the confusion matrix and the rules that determined their classification. For this example the classification accuracy of PRISM is 88.5% from a training set of 200 traces.

Using its rule set, PRISM is capable of detecting duplicate tasks and labeling them as noisy such as II = 1, GG = 1, and KK = 1. PRISM is also able to detect most actually correct entries. However, since the training set is small (200 process traces) some incorrect entries go undetected. For instance, a noisy trace AAFGKBDI is detected as correct by applying rule 19, since a rule for the condition AA = 1 does not exist. On the other hand, the correct trace AGBFCKIJI is labeled as noisy by PRISM by applying rule 11.

## 5. Experiments and discussion of results

In this section, the experiments described above are repeated for the “sanitized” logs after using Weka to create rules and applying them to remove the noisy records from the log.

## 5.1. Experimental setup

To build a classifier with the Weka software [27], a marked sub-log of 200 traces is first converted into the appropriate file format (.arff), and then the PRISM algorithm is run on it. The algorithm splits this log into training and testing sets using a user-specified percentage, typically 67% and 33%, respectively. These are quite typical values.

```txt
Table 7
Pseudo-code for PRISM.
(1) For each class C
(A) Initialize E to the trace set
(B) While E contains traces in class C
(a) Create a rule R with an empty left-hand side that predicts class C
(b) Until R is perfect (or there are no more attributes to use) do
(I) For each attribute A not mentioned in R, and each value v
(i) Consider adding the condition A = v to the left-hand side of R
(ii) Select A and v to maximize the accuracy percentage
(II) Add A = v to R
(C) Remove the traces covered by R from E
```

Table 8  
PRISM rule set for classifying records in a Level 5 log with 10% noise. (classes: 0 — noisy; 1 — correct).

<table><tr><td>Rule #</td><td>PRISM rules</td><td>Rule #</td><td>PRISM rules</td></tr><tr><td>1</td><td>If  $\mathrm{{II}} = 1$  then class  $= 0$ </td><td>11</td><td>If CK = 1 and AG = 1 then class  $= 0$ </td></tr><tr><td>2</td><td>If GG = 1 then class  $= 0$ </td><td>12</td><td>If DF = 1 and AF = 1 then class  $= 0$ </td></tr><tr><td>3</td><td>If JJ = 1 then class  $= 0$ </td><td>13</td><td>If BG = 1 and GI = 1 and AB = 1 then class  $= 0$ </td></tr><tr><td>4</td><td>If BI = 1 then class  $= 0$ </td><td>14</td><td>If KB = 1 and FG = 0 and AF = 1 then class  $= 0$ </td></tr><tr><td>5</td><td>If DB = 1 then class  $= 0$ </td><td>15</td><td>If GK = 1 and BG = 1 then class  $= 1$ </td></tr><tr><td>6</td><td>If EE = 1 then class  $= 0$ </td><td>16</td><td>If JH = 1 and AF = 0 then class  $= 1$ </td></tr><tr><td>7</td><td>If GA = 1 then class  $= 0$ </td><td>17</td><td>If CG = 1 then class  $= 1$ </td></tr><tr><td>8</td><td>If HH = 1 then class  $= 0$ </td><td>18</td><td>If EI = 1 and GK = 1 and II = 0 then class  $= 1$ </td></tr><tr><td>9</td><td>If HK = 1 then class  $= 0$ </td><td>19</td><td>If DI = 1 and GA = 0 then class  $= 1$ </td></tr><tr><td>10</td><td>If KK = 1 then class  $= 0$ </td><td>20</td><td>If FC = 1 then class  $= 1$ </td></tr></table>

In the experiments described in this section, we focus on the level 5 reference model because it is the most complex one. For this model, we generated synthetic logs at 2%, 5%, 10%, and 20% noise levels with 200 traces in each log. In these logs the dirty/clean indicator was set to 0/1 manually. Then the rules were generated by running the PRISM algorithm in Weka. The average classification accuracy of PRISM was 97% at low noise but it decreased to 73.5% at 20% noise.

Table 9  
Number of process traces in sanitized log with PRISM rules (initially 1000).

<table><tr><td rowspan="2">% of noise</td><td colspan="2">Number of traces in sanitized log</td></tr><tr><td>Log 1</td><td>Log 2</td></tr><tr><td>2%</td><td>997</td><td>992</td></tr><tr><td>5%</td><td>975</td><td>980</td></tr><tr><td>10%</td><td>935</td><td>944</td></tr><tr><td>20%</td><td>834</td><td>839</td></tr></table>

Additionally, we generated 10 synthetic logs each with 1000 traces at 5 noise levels (i.e., 0%, 2%, 5%, 10% and 20%) for the level 5 reference model for testing the effectiveness of the noise removal algorithm on the benchmark metrics. These logs were first sanitized by applying the rules to the traces in them, thus fewer traces remained as shown in Table 9.

It should be noted that on applying the rules, some traces were labeled as correct and others as noisy, while some could not be classified as either. These unclassified traces were retained in the log. We ran tests both with including and excluding such traces, and found that retaining unclassified traces helps in discovery of better models.

## 5.2. Results

We tested the Alpha++ and HM algorithms implemented in the ProM 5.2 process mining framework [28] in our benchmarking experiments. These algorithms were selected because they are well-known and also use very different approaches for mining. Thus, the results would help us to contrast how these approaches perform with noisy logs. Alpha++ derives Petri nets from event logs using strict causality relationships, while HM is based on heuristics as explained earlier. For running our experiments the default parameter settings built into ProM were used. By running the algorithms in ProM on the input logs we obtain the mined models.

<table><tr><td></td><td>Predicted noisy</td><td colspan="2">Predicted correct</td></tr><tr><td>Actual noisy</td><td>38</td><td colspan="2">53</td></tr><tr><td>Actual correct</td><td>16</td><td colspan="2">847</td></tr><tr><td>Correctly Classified Instances</td><td>885</td><td>88.5</td><td>%</td></tr><tr><td>Incorrectly Classified Instances</td><td>69</td><td>6.9</td><td>%</td></tr><tr><td>Unclassified Instances</td><td>46</td><td>4.6</td><td>%</td></tr><tr><td>Total Number of Instances</td><td>1000</td><td></td><td></td></tr></table>

(a) Confusion matrix for classified instances

<table><tr><td rowspan="2"></td><td colspan="4">Log entry (trace)</td></tr><tr><td>Labeled as noisy</td><td>Rule number</td><td>Labeled as correct</td><td>Rule number</td></tr><tr><td rowspan="10">Actually noisy</td><td>AFKBDI</td><td>R14</td><td>AFGKEI</td><td>R18</td></tr><tr><td>AFBEGIIJHGFKIJI</td><td>R1</td><td>AFBGHCGIHGFK</td><td>R17</td></tr><tr><td>AGFHGBEFIKJIJI</td><td>R3</td><td>ABGFFHFEIGK</td><td>R15 or R18</td></tr><tr><td>ABIFJIGK</td><td>R4</td><td>AGFHGFCIJK</td><td>R20</td></tr><tr><td>AFBDGHGFIHFGGK</td><td>R2</td><td>AIFCGBJIHFGK</td><td>R17 or R20</td></tr><tr><td>ABGCIJIJIFJHFIGHGFHFGKK</td><td>R10</td><td>AGHFBCGIHJIFGK</td><td>R17</td></tr><tr><td>AFBCGFGFIHHGK</td><td>R8</td><td>AFBEIJGIHFGHGHFGK</td><td>R18</td></tr><tr><td>AFGHFGGBEIK</td><td>R2</td><td>AGFHBDDIGFK</td><td>R19</td></tr><tr><td>ABIGFIJIJDHFGK</td><td>R4</td><td>AGBCIKJHGIFF</td><td>R16</td></tr><tr><td>HFGAGBCFHGFHGIJIJIFK</td><td>R7</td><td>AAFGKBDI</td><td>R19</td></tr><tr><td rowspan="10">Actually correct</td><td>AFBGHDFGHFIJGHIGFK</td><td>R12</td><td>ABFCIGJKI</td><td>R20</td></tr><tr><td>ABGFEHGIFJIK</td><td>R13</td><td>AGBFDIHGFK</td><td>R19</td></tr><tr><td>AFGHGBDFHGIFHGFK</td><td>R12</td><td>AGFBKDIJI</td><td>R19</td></tr><tr><td>AGFHFBGCKI</td><td>R11</td><td>ABFCIGK</td><td>R20</td></tr><tr><td>AFGHGBDFKIJI</td><td>R12</td><td>AFGHFGHBGCIFHFGK</td><td>R15</td></tr><tr><td>AGFBHGFCKIJIJI</td><td>R11</td><td>ABFCIGHFGHGFK</td><td>R20</td></tr><tr><td>AFBGHFGHDFGHGFKI</td><td>R12</td><td>ABGFHCFIGK</td><td>R15</td></tr><tr><td>AGFBCKIJIJI</td><td>R11</td><td>AGFHBDIGFK</td><td>R19</td></tr><tr><td>AGFBHGFCKI</td><td>R11</td><td>AFGHFBDIGHFJIGHFGK</td><td>R19</td></tr><tr><td>ABGEFHGIFHGFK</td><td>R13</td><td>AGFBDIHJIJFIGHFGK</td><td>R19</td></tr></table>

(b) Example of log entries on classified results  
Fig. 7. Classification results in a Level 5 log (log 1) with 10% noise by using PRISM.

For each algorithm and at each noise level, we report results for the noisy and sanitized logs. Table 10 shows the average results on the trace behavior and structural metrics for the 10 synthetic logs at level 5.

From the results we observe that: (1) both algorithms perform better on all four metrics on the sanitized log as compared to the noisy log; (2) the performance gap for the sanitized vs. noisy log varies at different noise levels. In some cases it is close to 30%, but generally it ranges between 1% and 10% for HM, and is considerably higher for Alpha++; (3) Alpha++ shows greater improvement on the sanitized log than HM, yet HM is, still, for the most part, far superior to Alpha++ on both noisy and sanitized logs. Further, the results on the structural metrics for the sanitized log show that HM is able to preserve most of the structures in the reference model. Moreover, on sanitized logs HM is able to discover models that do not contain superfluous structures not present in the reference model.

It is evident that the approach described for sanitizing logs does indeed improve the performance of the process mining algorithms. Clearly, both Alpha++ and HM can mine better models from sanitized logs. While it is known that HM is more robust to noise than Alpha++ since it can take the non-local dependencies among tasks (i.e., how strongly a task is caused by any other task) into account, we found that even HM benefits from log sanitization.

Table 11 shows the average values for the number of places, transitions, and arcs at the four noise levels. For Alpha++, the number of places decreases as the noise level increases. On further investigation, we found that this occurs because Alpha++ gives an incorrect, trivial model with few, in some cases just two, places and all activities connecting to them.

## 5.3. Discussion

We benchmarked two process mining algorithms for noise-free, noisy, and sanitized logs. The noisy logs were sanitized using the

## Table 10

Experimental results for trace behavior and structure metrics. (Average values for Level 5 logs from 5 × 10 experiments).

<table><tr><td rowspan="2">Level 5</td><td colspan="2">Alpha++</td><td colspan="2">HM</td></tr><tr><td>Noisy log</td><td>Sanitized log</td><td>Noisy log</td><td>Sanitized log</td></tr><tr><td></td><td colspan="2">2% noise</td><td></td><td></td></tr><tr><td>Behavioral precision</td><td>0.109</td><td>0.160 (47%)</td><td>0.656</td><td>0.694 (6%)</td></tr><tr><td>Behavioral recall</td><td>0.186</td><td>0.255 (37%)</td><td>0.739</td><td>0.755 (2%)</td></tr><tr><td>Structural precision</td><td>0.152</td><td>0.240 (58%)</td><td>0.892</td><td>0.896 (0.4%)</td></tr><tr><td>Structural recall</td><td>0.504</td><td>0.627 (24%)</td><td>0.591</td><td>0.654 (11%)</td></tr><tr><td></td><td colspan="2">5% noise</td><td></td><td></td></tr><tr><td>Behavioral precision</td><td>0.041</td><td>0.154 (276%)</td><td>0.551</td><td>0.592 (7%)</td></tr><tr><td>Behavioral recall</td><td>0.127</td><td>0.315 (148%)</td><td>0.740</td><td>0.752 (2%)</td></tr><tr><td>Structural precision</td><td>0.146</td><td>0.152 (4%)</td><td>0.871</td><td>0.862 (-1%)</td></tr><tr><td>Structural recall</td><td>0.355</td><td>0.566 (59%)</td><td>0.525</td><td>0.563 (7%)</td></tr><tr><td></td><td colspan="2">10% noise</td><td></td><td></td></tr><tr><td>Behavioral precision</td><td>0.020</td><td>0.221 (1005%)</td><td>0.469</td><td>0.552 (18%)</td></tr><tr><td>Behavioral recall</td><td>0.058</td><td>0.413 (612%)</td><td>0.736</td><td>0.738 (0.3%)</td></tr><tr><td>Structural precision</td><td>0.162</td><td>0.172 (6%)</td><td>0.700</td><td>0.853 (22%)</td></tr><tr><td>Structural recall</td><td>0.305</td><td>0.557 (83%)</td><td>0.502</td><td>0.591 (18%)</td></tr><tr><td></td><td colspan="2">20% noise</td><td></td><td></td></tr><tr><td>Behavioral precision</td><td>0</td><td>0.194</td><td>0.463</td><td>0.501 (8%)</td></tr><tr><td>Behavioral recall</td><td>0</td><td>0.255</td><td>0.727</td><td>0.778 (7%)</td></tr><tr><td>Structural precision</td><td>0.064</td><td>0.164 (156%)</td><td>0.623</td><td>0.804 (29%)</td></tr><tr><td>Structural recall</td><td>0.141</td><td>0.695 (393%)</td><td>0.471</td><td>0.473 (0.4%)</td></tr></table>

(Values in parenthesis represent the percentage improvement from sanitization).

PRISM algorithm first to build a classifier. The reference process models are designed from basic structures such as sequence, parallel, exclusivechoice, and loop with increasing complexity from level 0 to level 5. The results of the experiments show that if the logs are sanitized first, both Alpha++ and HM can discover better models from sanitized logs. This discussion focuses on the HM algorithm since that is a better algorithm in the presence of noise.

To gain more insights, we analyzed a specific one of the 10 logs, labeled as log 1 in further detail. The experimental results for log 1 at 10% noise are shown in Table 12. The corresponding mined process models obtained by HM for the noisy and sanitized logs are shown in Fig. 8(a) and (b) respectively.

Notice that the mined model before sanitizing has several problems. The node J on the extreme left of Fig. 8(a) is completely disconnected. Moreover, the group of activities E–C–D–I at the top right of the figure is not connected properly to the rest of the process. It is also difficult to parse, suggesting that the mining algorithm is confused by the noise. The mined model after sanitizing shows significant improvement in all four metrics. In particular, structural precision is 1, i.e., 100% of its structure is preserved if the log is sanitized first. Moreover, it is more compact since the numbers of places, transitions, and arcs are reduced. This is a reflection of the intrinsic quality of the model [23]. On inspection there is one obvious arc that is missing in this model, as shown by the dashed line in Fig. 8(b). Clearly the sanitized log leads to a “nicer” model which captures much of the behavior of the Level 5 reference model (see Fig. 5(f)).

To further evaluate these mined models of Fig. 8, we checked them independently using the Workflow analysis tool, Woflan (WOrkFLowANalyzer). Woflan [29] is used to verify the correctness of a workflow process. It uses state-of-the-art techniques to find potential errors in the definition of a workflow process. Upon checking with Woflan the model from the unsanitized log failed the test with multiple errors, while the model from the sanitized log passed the test. This further goes to show that the mined model on the sanitized log is intrinsically superior to the one from the unsanitized log.

We also considered algorithms other than HM. In experiments with the Genetic Miner [12], it was found to be a very slow algorithm and its performance was erratic. It occasionally did better than HM, but overall, the HM algorithm was much more consistent and gave better results on average as was observed in [12] also. Hence, this algorithm was not studied further.

The Fuzzy Miner (FM) [20] offers a user a sliding scale to select a certain percentage of the log traces for mining. Thus, it is possible to ask FM to, say, use 90% of the traces to make a model. The assumption here is that FM would discard 10% of the traces that contain either noise, or infrequent but correct behavior, of the underlying process. FM generates a hierarchical model showing relationships among tasks, but the output is not sufficient to generate a full Petri-net model.

## Table 11

Experimental results for number of places, transitions, and arcs. (Average values for Level 5 logs from 5 × 10 experiments).

<table><tr><td rowspan="3">Level 5</td><td colspan="8">Alpha++</td></tr><tr><td colspan="4">Before sanitizing noise</td><td colspan="4">After sanitizing noise</td></tr><tr><td>2%</td><td>5%</td><td>10%</td><td>20%</td><td>2%</td><td>5%</td><td>10%</td><td>20%</td></tr><tr><td># of places</td><td>13.7</td><td>5.6</td><td>3.6</td><td>2.6</td><td>19.7</td><td>12.9</td><td>14.9</td><td>22.6</td></tr><tr><td># of transitions</td><td>11</td><td>11</td><td>11</td><td>11</td><td>11.2</td><td>11</td><td>11</td><td>11</td></tr><tr><td># of arcs</td><td>84.5</td><td>40.6</td><td>28.9</td><td>23.1</td><td>97.1</td><td>90.3</td><td>95</td><td>141.7</td></tr></table>

<table><tr><td rowspan="2"></td><td colspan="4">Before sanitizing noise</td><td colspan="4">After sanitizing noise</td></tr><tr><td>2%</td><td>5%</td><td>10%</td><td>20%</td><td>2%</td><td>5%</td><td>10%</td><td>20%</td></tr><tr><td># of places</td><td>22.1</td><td>22.2</td><td>22.4</td><td>19</td><td>20.8</td><td>21.4</td><td>22.5</td><td>21.3</td></tr><tr><td># of transitions</td><td>21.1</td><td>22.3</td><td>23.3</td><td>21.4</td><td>19.4</td><td>21.7</td><td>22.9</td><td>23.8</td></tr><tr><td># of arcs</td><td>62.9</td><td>66.5</td><td>68.8</td><td>55.8</td><td>57.6</td><td>63</td><td>66.9</td><td>65.9</td></tr></table>

Table 12  
Results for a specific Level 5 log (log 1) at 10% noise.

<table><tr><td rowspan="2">Level 5</td><td colspan="2">HM</td></tr><tr><td>Noisy log</td><td>Sanitized log</td></tr><tr><td>Behavioral precision</td><td>0.46</td><td>0.63</td></tr><tr><td>Behavioral recall</td><td>0.71</td><td>0.8</td></tr><tr><td>Structural precision</td><td>0.71</td><td>1</td></tr><tr><td>Structural recall</td><td>0.43</td><td>0.55</td></tr><tr><td># of places</td><td>22</td><td>20</td></tr><tr><td># of transitions</td><td>21</td><td>20</td></tr><tr><td># of arcs</td><td>66</td><td>60</td></tr></table>

Moreover, it is still not a real alternative to our approach since noise can get confused with infrequent correct behavior. Further, if our approach is used to preprocess a log, then FM will produce better results and it will be easier for the user to identify infrequent behavior.

Though we used a specific noise pattern in our experiments, the rulebased approach generalizes to any noise pattern. Thus, a classifier like PRISM can create rules for a different noise pattern from the one we selected from a marked sub-log. Another advantage of having rules for sanitization is that they can be checked manually, explained and also modified further to improve the classification accuracy even more.

![](/api/attachments/9YYJ3VQ8/fulltext/images/3c99bbc1a1f432764bc45431a299038d5ebcadda92f938e7cf731580282704b5.jpg)

(a) Before sanitizing (Places: 22; Transitions: 21; Arcs: 66)  
![](/api/attachments/9YYJ3VQ8/fulltext/images/ebe8992f96d52fb9f3e5459b3bfd251127244d7e26d5d54c5f1ccd6b0ba74cc6.jpg)  
(b) After sanitizing (Places: 20; Transitions: 20; Arcs: 60)  
Fig. 8. Mined models of ProM for HM before and after sanitizing the log. (level 5, log 1, 10% noise).

Table 13  
11 main tasks identified in the patents application process.

<table><tr><td>Event id</td><td>Description</td></tr><tr><td>A</td><td>Application captured on micro-film</td></tr><tr><td>B</td><td>Non-final rejection</td></tr><tr><td>C</td><td>Mail non-final rejection</td></tr><tr><td>D</td><td>Information disclosure statement filed</td></tr><tr><td>E</td><td>Request for extension of time granted</td></tr><tr><td>F</td><td>Response after non-final action</td></tr><tr><td>G</td><td>Notice of allowance data verification completed</td></tr><tr><td>H</td><td>Mail notice of allowance</td></tr><tr><td>I</td><td>Final rejection</td></tr><tr><td>J</td><td>Mail final rejection</td></tr><tr><td>K</td><td>Notice of appeal filed</td></tr></table>

Finally, a reference model may not exist in many real-life situations to compare the mined model against. In such situations, the models obtained before and after sanitizing the log can be compared with one another in terms of metrics like number of places, transitions, arcs, disconnected places and transitions, and overall quality. They can also be checked for errors using an analysis tool like Woflan. As we discussed above in the context of Fig. 8, such metrics can help establish intrinsic superiority of one model over another.

## 6. Experience with real data — a patent application process

In order to validate our approach with a real dataset, we accessed the United States patent application process data (available at http://portal. uspto.gov/external/portal/pair) and discuss our experiments with this data next.

We collected transaction data for patents of the category 435 (Chemistry: molecular biology and microbiology) under the United States Patent Classification issued between 2000 and 2005. There is a total of 31,682 patent transaction instances containing 518 unique tasks. We analyzed the dataset with a tool called Disco [30] to identify the most frequent tasks and most frequent sequential relationships among these tasks. From this analysis we identified a subset of 11 most frequent tasks shown in Table 13. Moreover, based on the output from Disco about the sequential relationships among tasks and our understanding of the process we developed a reference model as shown in Fig. 9. All the 11 frequent tasks are included in this model and all the flow paths represent meaningful execution scenarios.

Then, for validation we used a random subset of 1000 instances. All instances in a sub-subset of 100 instances were then marked as noisy or clean. Accordingly, 10 instances were identified and marked as “noisy” and the rest as “clean.” These 100 marked instances were used to generate PRISM rules. The rules were applied to the unmarked log and only the 827 instances marked as clean were retained. Subsequently, we ran the HMM algorithm to generate a process model from both the full or “dirty” log and the “clean” log. We found that the process model from the “clean” log was more compact and better. It had 30 places, 40 transitions, 122 arcs and 29 silent transitions. The corresponding values for the model from the “dirty” log were 31, 43, 130 and 32, respectively. In addition we also calculated the behavioral and structural precision and recall metrics for the two process models with respect to the reference model of Fig. 9. Both behavioral metrics showed improvement (precision by 2% and recall by 3%), while structural precision improved by 1%.

To be sure, this experiment suffers from shortcomings. In particular, we could not find a domain expert to assist us and had to rely on our own understanding of the process to mark the clean and noisy instances. We also developed the reference model ourselves. Nevertheless, the experiment still shows that our approach has practical value and though the improvement is modest yet it is noticeable across multiple metrics. A more extensive experiment with participation of domain experts is beyond the scope of our current work.

![](/api/attachments/9YYJ3VQ8/fulltext/images/d5eacd4599ef5feb7059c05a52e1036d61ad5bae0cdf849ef099af17d4a1be77.jpg)  
Fig. 9. A reference model for the patent application process.

## 7. Related work and limitations

In previous benchmarking studies, Weijters et al. [11] evaluated HM using 12,000 different event logs at six noise levels. Mederios et al. [12] did extensive benchmarks on the Genetic Miner, Heuristics Miner, and Alpha++. They showed that, overall, Heuristic Miner outperformed other algorithms for tackling noisy logs. Different notions of equivalence have been discussed to compare a reference process model against a mined model. The interesting ones focus on the dynamics of the model and not just on its syntactic structure (e.g., van Glabbeek and Weijland [31], van der Aalst and Basten [32]). The metrics we selected capture both behavioral and structural features of the models [33] and also provide a value for the degree of similarity in a continuous 0–1 range.

Some evaluation approaches related to process mining have also been proposed. Weerdt et al. [34] introduced an evaluation approach based on artificially generated negative events in benchmarking six process discovery techniques in consideration of noise-free logs and 20% noisy logs. This approach includes recall, precision, and F-measure to measure discovered process models. Wang et al. [35] presented an empirical evaluation framework towards a common benchmark based on behavioral and structural similarity for evaluating seven process mining algorithms without consideration of noise. Using structural and behavioral similarities to benchmark process mining algorithms, the authors further introduced a new framework that can efficiently select the most suitable process mining algorithm for a given enterprise [36].

While one would naturally expect a sanitized log to produce better mined models than an unsanitized one, our goal in this paper is to understand its potential value in the context of “noise-aware” algorithms in particular. Our experiments clearly showed that when the models are complex, such as our Level 5 reference model, even the performance of popular “noise-aware” algorithms like Heuristic Miner can be improved by sanitization. Another issue with “noise-aware” algorithms is that they find the model that best fits a certain percentage of log traces by discarding the rest as noise. However, as noted earlier such approaches have no way of knowing whether a discarded trace is actually “clean” and reflects a rare but correct instance, or is in fact noisy. Hence, they may arbitrarily discard a correct trace and lose useful information. While in some applications it may not matter, in others, say, those involving medical procedures and fraud investigation cases, it is important. Our approach rectifies this problem.

It is important to note several limitations of this study. In process mining, the errors related to tasks (such as tasks swapped, tasks removed, tasks duplicated) are most common. Therefore, our work only focused on common types of noise (i.e., “remove task”, “swap two tasks”, and “duplicate one randomly chosen task”) and did not consider the labeling errors and vocabulary differences herein. Hence, the labeling errors and vocabulary differences may result in log errors. Moreover, in our experiments with synthetic logs we selected 200 traces as the size of the sub-log for marking from a full log of 1000 traces. The size of this sub-log was chosen because it is not too large at 20% of the full log and allowed us to develop rules for noise detection. However, it is not possible to generalize what the exact size of the sub-log for marking should be. It is rather specific to the nature of the log and will depend on the size, noise level and noise characteristics of the full log. Hence, it has to be determined on a case by case basis, partly based on human judgment. Finally, our experiments with the real world dataset could not be validated with a domain expert.

## 8. Conclusions and future work

Process mining is a relatively new technique for extracting process models from actual execution logs to gain a better understanding of business processes in an organization and support decision making. Since logs are often noisy, process mining algorithms handle noise by generating a model that best fits a certain given percentage of records or instances and discarding the rest as noisy. This can lead to loss of instances that describe rare but valid process behavior captured in the log. This paper studies through extensive experiments how a rule based approach called log sanitization can help to improve the performance of a process mining algorithm. Hence, we described and evaluated a general approach for log sanitization that can work with any noise pattern. Given a log of traces, if a subset of traces is marked as correct or noisy then a rule-based classifier can be built on this marked sub-log. The rules can then be applied to sanitize the full log.

We showed that mined models extracted from sanitized logs have much greater fidelity to the “true” reference model than those from unsanitized logs on both behavioral and structural metrics. They are also more compact with fewer extraneous places, transitions and arcs. Further, on checking with a workflow analysis tool, we found that they have fewer syntactic errors. Thus, even if a “true” reference model is not available, one can compare the mined model from an unsanitized log against one from a sanitized one to argue that the latter is intrinsically better. We also evaluated our approach on a real dataset and reported the results that showed modest improvements.

Our benchmark included six process models; however, our results focused mainly on the most complex level 4 and 5 models. The benefit of sanitization was as high as 29% in some cases (less, on average) even for Heuristic Miner which is a noise-aware algorithm in the first place. Another advantage of our rule based approach for sanitization is that it is agnostic to the nature of noise and it can classify any noise pattern. Thus, if another kind of noise appears in the log, e.g., a random insertion of a task, it will be captured in a rule and thus flagged as noise. Rules can also be checked manually to see if they are meaningful, and further modified to improve sanitization quality and to ensure that process model behavior that occurs infrequently is not mislabeled as noise.

In future work, we would like to study how to extend the rule-based approach to rewrite noisy traces. For instance, one can examine the labeled noisy entries through rules and then mark and rearrange noisy parts of the trace. In this way, the noisy traces can also be used in process mining and their information is not lost. It would also be interesting to develop automated ways of noise detection that can allow a smart algorithm to detect and suggest noisy records to the user in a sub-log of the full log. This user can then verify that the proposed markings are correct and override them as needed.

## Acknowledgment

Hsin-Jung Cheng was a visiting researcher at Penn State from Taiwan when this work was done. She was partly supported by a grant from HP. Wen Yao wrote the code for the noise generation program. We also thank the anonymous reviewers for their constructive and helpful comments.

## References

[1] W.M.P. van der Aalst, A.J.M.M. Weijters, L. Maruster, Workflow mining: discovering process models from event logs, IEEE Transactions on Knowledge and Data Engineering 16 (9) (2004) 1128–1142

[2] R.S. Mans, M.H. Schonenberg, M. Song, W.M.P. van der Aalst, P.J.M. Bakker, Application of process mining in healthcare — a case study in a Dutch hospital, Proceedings of HEALTHINF 2008, International Conference on Health Informatics, INSTICC, 1 2008, pp. 118–125.

[3] R.S. Mans, M.H. Schonenberg, G. Leonardi, S. Panzarasa, A. Cavallini, S. Quaglini, W.M.P. van der Aalst, Process mining techniques: an application to stroke care, Studies in Health Technology and Informatics 136 (2008) 573–578.

[4] W.S. Yang, S.Y. Hwang, A process-mining framework for the detection of healthcare fraud and abuse, Expert Systems with Applications 31 (1) (2006) 56–68.

[5] J.C.A.M. Buijs, B.F. van Dongen, W.M.P. van der Aalst, Mining configurable process models from collections, in: F. Daniel, J. Wang, B. Weber (Eds.), BPM 2013. LNCS 8094, Springer, Heidelberg 2013, pp. 33–48.

[6] A. Rozinat, I.S.M. de Jong, C.W. Günther, W.M.P. van der Aalst, Process mining applied to the test process of wafer steppers in ASML, IEEE Transactions on Systems, Man, and Cybernetics—Part C: Applications and Reviews 39 (4) (2009) 474–479.

[7] R.P.J.C. Bose, W.M.P. van der Aalst, Trace alignment in process mining: opportunities for process diagnostics, in: R. Hull, J. Mendling, S. Tai (Eds.), BPM 2010. LNCS, 6336, Springer, Heidelberg 2010, pp. 227–242.

[8] R. Agrawal, D. Gunopulos, F. Leymann, Mining process models from workflow logs, Sixth International Conference on Extending Database Technology. LNCS, 1377, Springer-Verlag, Berlin 1998, pp. 469–483.

[9] S.Y. Hwang, W.S. Yang, On the discovery of process models from their instances, Decision Support Systems 34 (2002) 41–57

[10] A.J.M.M. Weijters, W.M.P. van der Aalst, Rediscovering workflow models from event-based data using little thumb Integrated Computer-Aided Engineering 10 (2) (2003) 151–162.

[11] A.J.M.M. Weijters, W.M.P. van der Aalst, A.K.A. de Medeiros, Process mining with heuristicsminer algorithm, BETA Working Paper Series, WP 166, Eindhoven University of Technology, Eindhoven, 2006.

[12] A.K.A. de Medeiros, A.J.M.M. Weijters, W.M.P. van der Aalst, Genetic process mining: an experimental evaluation, Data Mining and Knowledge Discovery 14 (2) (2007) 245–304.

[13] W.M.P. van der Aalst, Process Mining: Discovery, Conformance and Enhancement of Business Processes, 1st ed. Springer Publishing Company, 2011.

[14] L. Wen, W.M.P. van der Aalst, J. Wang, J. Sun, Mining process models with non-freechoice constructs, Data Mining and Knowledge Discovery 15 (2) (2007) 145–180.

[15] T. Murata, Petri nets: properties, analysis and applications, Proceedings of the IEEE 77 (4) (1989) 541–580.

[16] J.E. Cook, A.L. Wolf, Discovering models of software processes from event-based data, ACM Transactions on Software Engineering and Methodology 7 (3) (1998) 215-249.

[17] J.E. Cook, A.L. Wolf, Event-based detection of concurrency, Proceedings of the Sixth International Symposium on the Foundations of Software Engineering (FSE-6) Or lando, FL, 23(6) 1998, pp. 35–45.

[18] A. Rozinat, W.M.P. van der Aalst, Conformance checking of processes based on monitoring real behavior, Information Systems 33 (1) (2008) 64–95.

[19] J.C.A.M. Buijs, B.F. van Dongen, W.M.P. van der Aalst, On the role of fitness, precision, generalization and simplicity in process discovery, OTM Federated Conferences, 20th International Conference on Co-operative Information Systems (CoopIS 2012). LNCS, 7565, Springer, Berlin 2012, pp. 305–322.

[20] C.W. Günther, W.M.P. van der Aalst, Fuzzy mining — adaptive process simplification based on multi-perspective metrics, in: G. Alonso, P. Dadam, M. Rosemann (Eds.), BPM2007. LNCS, 4714, Springer, Heidelberg 2007, pp. 328–343.

[21] J.M.E.M. van der Werf, B.F. van Dongen, C.A.J. Hurkens, A. Serebrenik, Process discovery using integer linear programming, 29th International Conference on Applications and Theory of Petri Nets, Xi'an, China, Springer, Berlin, 2008.

[22] M.R. Przybylek, Skeletal algorithms in process mining, Studies in Computational Intelligence 465 (2013) 119–134.

[23] Z. Huang, A. Kumar, A study of quality and accuracy tradeoffs in process mining, IN-FORMS Journal on Computing 24 (2) (2012) 311–327.

[24] J. Cendrowska, PRISM: an algorithm for inducing modular rules, International Journal of Man-Machine Studies 27 (4) (1987) 349–370.

[25] F. Stahl, M. Bramer, M. Adda, P-Prism: a computationally efficient approach to scaling up classification rule induction, IFIP International Conference on Artificial Intelligence, 276, Springer, Milan 2008, pp. 77–86.

[26] J. Fürnkranz, Separate-and-conquer rule learning, Artificial Intelligence Review 13 (1) (1999) 3–54.

[27] I.H. Witten, E. Frank, M.A. Hall, Data Mining: Practical Machine Learning Tools and Techniques, 3rd edition Morgan Kaufmann, San Francisco, 2011.

[28] B.F. van Dongen, A.K.A. de Medeiros, H.M.W. Verbeek, A.J.M.M. Weijters, W.M.P. van der Aalst, The ProM framework: a new era in process mining tool support, in: G. Ciardo, P. Darondeau (Eds.), Application and Theory of Petri Nets 2005. LNCS, 3536, Springer-Verlag, Berlin 2005, pp. 444–454.

[29] H.M.W. Verbeek, T. Basten, W.M.P. van der Aalst, Diagnosing workflow processes using Woflan, The Computer Journal 44 (4) (2001) 246–279.

[30] Fluxicon, Disco, http://www.fluxicon.com.

[31] R.J. van Glabbeek, W.P. Weijland, Branching time and abstraction in bisimulation semantics, Journal of the ACM 43 (3) (1996) 555–600.

[32] W.M.P. van der Aalst, T. Basten, Inheritance of workflows: an approach to tackling problems related to change, Theoretical Computer Science 270 (1–2) (2002) 125–203.

[33] A.K.A. de Medeiros, W.M.P. van der Aalst, A.J.M.M. Weijters, Quantifying process equivalence based on observed behavior, Data and Knowledge Engineering 64 (1) (2008) 55–74.

[34] J. De Weerdt, M. De Backer, J. Vanthienen, B. Baesens, A robust F-measure for evaluating discovered process models, in: N. Chawla, I. King, A. Sperduti (Eds.), IEEE Symposium on Computational Intelligence and Data Mining (CIDM 2011), 148– 155, Paris, France, April 2011, IEEE, 2011.

[35] J. Wang, S. Tan, L. Wen, R.K. Wong, Q. Guo, An Empirical Evaluation of Process Mining Algorithms Based on Structural and Behavioral Similarities, In ACM SAC, Trento, 2012.

[36] J. Wang, R.K. Wong, J. Ding, Q. Guo, L. Wen, Efficient selection of process mining algorithms, IEEE Transactions on Services Computing 6 (4) (2012) 484–496.

Hsin-Jung Cheng is currently an engineer at the Computational Intelligence Technology Center, Industrial Technology Research Institute of Taiwan, R.O.C. She received her Ph.D. degree from Department of Industrial Management, National Taiwan University of Science and Technology, Taiwan, R.O.C. in 2015. Her research interests include process mining, data mining, parallel structures, business process management, meta-heuristic algorithms and workflow structure analysis.

Akhil Kumar is a professor of information systems at the Smeal College of Business at Penn State University. He received his Ph.D. from the University of California, Berkeley, and has previously been on the faculties at Cornell University and the University of Colorado, and also spent one year at Bell Labs, Murray Hill, NJ. His research interests are in workflow systems, process mining, web services, and healthcare IT. He has done pioneering work in data replication techniques and in advancement of XML based workflows. He has published more than 100 papers in academic journals and international conference proceedings. His work has appeared in ACM TMIS, ACM Transactions on Databases, ISR, JMIS, several IEEE Transactions, Decision Support Systems, and in other journals and conferences. His research has been supported by NSF, IBM and HP. He served as coprogram chair for CoopIS 2011. He has also served on several editorial boards and program committees.

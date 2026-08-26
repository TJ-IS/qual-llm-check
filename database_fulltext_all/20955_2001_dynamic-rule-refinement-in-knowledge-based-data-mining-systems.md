---
otero_id: 20955
otero_key: "BAHKRX33"
title: "Dynamic rule refinement in knowledge-based data mining systems"
authors: "Sang C Park; Selwyn Piramuthu; Michael J Shaw"
year: "2001"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00132-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Dynamic rule refinement in knowledge-based data mining systems

Sang C. Park <sup>a</sup>, Selwyn Piramuthu <sup>b</sup>, Michael J. Shaw <sup>c,)</sup>

<sup>a</sup> Industrial Management Department, Korea AdÕanced Institute of Science and Technology, 373-1 Kusong-Dong, Yusong-Ku, Taejon 305-701, South Korea

The Wharton School, UniÕersity of PennsylÕania, 1300 Steinberg Hall–Dietrich Hall, Philadelphia, PA 19104-6366, USA <sup>c</sup> Beckman Institute for AdÕanced Science and Technology, UniÕersity of Illinois at Urbana-Champagne, Room 2051, 405 N. Mathews AÕenue, Urbana, IL 61801, USA

## Abstract

The availability of relatively inexpensive computing power as well as the ability to obtain, store, and retrieve huge amounts of data has spurred interest in data mining. In a majority of data mining applications, most of the effort is spent in cleaning the data and extracting useful patterns in the data. However, a critical step in refining the extracted knowledge especially in dynamic environments is often overlooked. This paper focuses on knowledge refinement, a necessary process to obtain and maintain current knowledge in the domain of interest. The process of knowledge refinement is necessary not only to have accurate and effective knowledge bases but also to dynamically adapt to changes. KREFS, a knowledge refinement system, is presented and evaluated in this paper.

KREFS refines knowledge by intelligently self-guiding the generation of new training examples. Avoiding typical problems associated with dependency on domain knowledge, KREFS identifies and learns distinct concepts from scratch. In addition to improving upon features of existing knowledge refinement systems, KREFS provides a general framework for knowledge refinement. Compared to other knowledge refinement systems, KREFS is shown to have more expressive power that renders its applicability in more realistic applications involving the management of knowledge. q 2001 Elsevier Science B.V. All rights reserved.

Keywords: Knowledge refinement; Data mining

## 1. Introduction

The decreasing cost of computing, the ease of collecting and storing data, advances in DBMS technologies, as well as the extensive set of available analytical tools have been instrumental in generating interest in data mining applications. In addition to traditional top-down data analyses including wellfounded application queries and report generation, bottom-up discovery-driven data analyses have been gaining popularity. Both individuals as well as organizations are beginning to explore possible ways to extract useful patterns that may be present in data to facilitate faster, more accurate, and better business decisions.

Given the strategic advantage in data mining as a valuable decision support tool, the projected growth of data mining applications in a short period of time is not surprising. The Meta Group has estimated the market for data mining applications to reach US\$8.1 billion by the year 2001 Financial Post, OctoberŽ 1999 . In a majority of data mining applications, a. commonly known estimate is that between 70% and 80% of the resources are spent on pre-processing the data 8 . This includes integrating existing sources of <sup>w</sup> <sup>x</sup> data, supplementing the existing data with other necessary data, selecting the relevant data, preparing the data including data conversions, forming new attributes, as well as means to handle noisy, incomplete, duplicate, or missing data. Only the remaining small percentage is used for actually discovering patterns in the data. After all this, only a small fraction of the supposedly useful information discovered from the data are useful and actionable in reality. This is further exacerbated by the dynamic nature of most real-world environments that results in obsolescence of extracted knowledge. This necessitates careful examination and refinement of extracted knowledge over time. Thus, the process of knowledge refinement is necessary to maintain accurate, effective, and useful knowledge base that is dynamically updated as per changes in the environment. Knowledge refinement is especially critical in maintaining accurate and robust knowledge in a dynamic environment.

Notable knowledge refinement systems include SEEK 30 , SEEK2 15 , FOIL 33 , GOLEM 26 ,<sup>w x</sup> <sup>w x</sup> <sup>w x</sup> <sup>w x</sup> and KBANN 36 . Most of these systems are cus-<sup>w</sup> <sup>x</sup> tomized for specific applications, and application to other domains is difficult in general. The specific details of the strengths and limitations of these systems are discussed in Section 3.

We develop a general knowledge refining system, KREFS, to overcome limitations identified in existing systems. In the next section, we provide a brief overview of data mining. In Section 3, we discuss the strengths and weaknesses of existing knowledge refinement systems. An overview of KREFS, the proposed knowledge refinement system, is provided in Section 4. Comparative analysis of KREFS’ relative performance over an existing knowledge refinement system is presented in Section 5. A real-world bankruptcy prediction data is used to illustrate the performance of KREFS in Section 6. Section 7 concludes this paper with a brief discussion.

## 2. Data mining

Data mining is defined as the nontrivial extraction of implicit, previously unknown, and potentially useful information from data 13 . Specific methods<sup>w</sup> <sup>x</sup> used in data mining applications include statistical pattern recognition e.g., Refs. 14,16,18 , associa-Ž <sup>w</sup> <sup>x</sup>. tion rules e.g., Refs. 1,2,7,37 , recognizing sequen-Ž <sup>w</sup> <sup>x</sup>. tial or temporal time series patterns e.g., Refs. Ž . Ž <sup>w</sup> <sup>x</sup> 4,5,22 , clustering or segmentation, e.g., Ref. 12 ,. Ž <sup>w</sup> <sup>x</sup>. data visualization e.g., Refs. 21,24,35 , and classi-Ž <sup>w</sup> <sup>x</sup>. fication e.g., Refs. 3,9,20 .Ž <sup>w</sup> <sup>x</sup>.

A typical example application for association rules is market basket analysis. The goal here is to find patterns across a large number of transactions to understand buying patterns. For example, in the financial domain, these methods can be used to analyze customers’ account portfolios to identify financial services that are often utilized together. This information can then be used to create service packages targeting appropriate customers, to serve them more efficiently. While association rules involve transactions that occur at a single point in time, sequential or temporal analyses involve transactions that occur across time. Here, in addition to the characteristics of the transactions themselves, the order or sequence in which they occur is important. An application of this method could be to identify patterns and predict characteristics of future transactions based on current transactions, as in likely sequences of purchases for direct marketing. Clustering or segmentation methods identify groups of related records that are homogeneous or identical in some respect. An application could be to target segments of a population for a sales campaign based on their demographics and previous purchasing behavior. Data visualization is used to cluster related records based on certain dimensions of interest. However, the method gets unwieldy as the number of dimensions in the data increases.

Classification is perhaps one of the most popular method of choice in data mining applications. Methods such as decision trees, neural networks, and genetic algorithms have been widely used for classification purposes. Using past data from the domain, these methods develop models that can be used to predict future events. Some common applications include credit scoring applications, credit card fraud detection, and stock portfolio selection.

![](/api/attachments/BAHKRX33/fulltext/images/7b0ff6c8b58ce2b2ef311d338e6ab41982283265581ffb5ac6809f7962c6e6de.jpg)  
Fig. 1. Data mining framework.

Framework of a typical data mining system is given in Fig. 1. It should be noted that knowledge refinement is not an integral part of a typical data mining system. The first stage involves preprocessing raw data. This could take several forms including handling procedures for missing and incomplete data, selecting variables to be considered further e.g., Refs. 19,23 , and constructing higher-Ž <sup>w</sup> <sup>x</sup>. order variables from other primitive variables e.g.,Ž . Ž Ref. 27 . The pre-processed data are then used as<sup>w</sup> <sup>x</sup>. input to one or a combination of several pattern extraction systems. Commonly used methods for pattern extraction include decision trees, neural networks, regression analysis, clustering methods, data visualization methods, and time series analysis. The patterns thus extracted at this stage are then stored in knowledge bases and used as input for decision-making processes.

Most data mining applications involve knowledge that change over time. One of the problems encountered in data mining applications is that of stale knowledge, caused primarily by the static nature of knowledge generated in these applications. This could be alleviated either by regenerating the entire knowledge base or by periodically refining the knowledge as and when deemed appropriate. The former option is clearly very expensive in terms of resources required, including time. The latter option is relatively inexpensive since the periodic updates to the knowledge base generally tend to be minimal in most applications. There is thus a need for methods to periodically refine knowledge bases, and this study develops a framework to address this issue.

## 3. Background on knowledge refinement

We characterize knowledge refining systems in terms of their knowledge representation, consistency in refining process compared to the process of initial knowledge base development, domain knowledge dependence, and the direction of refinement genera-Ž tion, specialization, or both . Generalization refers to. the process of expansion of the scope of applicability of a given piece of knowledge. Conversely, specialization refers to the process of restricting the scope of applicability. Knowledge can be either in propositional binary or predicate continuous value repre-Ž . Ž . sentation. While SEEK, SEEK2, and KBANN employ propositional attribute value representation, FOIL and GOLEM turn to predicate representation. The main strength of the propositional representation lies in its simplicity. But, this convenience leads to implementation limitations—a new proposition is created every time a new attribute value is added. It is also difficult to establish relationships between propositions since they only assume true or false values. In terms of maintenance, predicate value representation is more efficient and flexible. Yet there is no standard process for creating predicates, and generalization and<sup>r</sup>or specialization of knowledge is not straightforward as in the case of propositional representation. If knowledge is represented as propositions, simply checking for the existence of a proposition is enough; but for predicate representation, the existence of predicates as well as the range of values covered by these predicates must be checked.

The next question is whether or not the refining system utilizes the same process used to develop the initial knowledge base. While some systems consistently follow the steps used in generating the initial knowledge base, others employ ad-hoc processes Ž .SEEK and SEEK2 . This is critical because the bias introduced at the knowledge base development stage could be different from that at the knowledge refinement stage, compromising the quality of the knowledge base. Here, bias refers to the idiosyncrasies of the representation and the learning algorithm. In other words, the choice of the representation e.g., Ž IF–THEN rules, semantic diagrams, neural network representation as well as the algorithm used to learn . the patterns in the data biases the knowledge that can be learned and represented.

FOIL and GOLEM depend heavily on domain knowledge during the refinement process. When contradictory new data are encountered, new ‘literal’ or predicate conditions are added to distinguish one from the other. As opposed to this top-down, subjective, model-driven approach, other refining systems rely solely on training examples bottom-up, data- Ž driven approach . The degree of subjectivity is less-. ened in some refining systems although there still exists a small degree of subjectivity in terms of selection criteria SEEK and SEEK2 , rule extractingŽ . heuristic KBANN , and stopping conditions for re-Ž . finement KREFS .Ž .

Table 1 summarizes the characteristics of each system. These systems have different forms of knowledge representation and have employed different rule refinement processes. Depending on their own application areas, they carry strengths and weaknesses. Largely, these systems can be divided into propositional and predicate value representation systems.

## 3.1. Propositional Õalue representation systems

## 3.1.1. SEEK and SEEK2

SEEK was intended to interactively help an expert solve a problem by offering potential solutions to sub-problems. SEEK uses ‘criteria table representation’ to represent knowledge. SEEK2 is an improvement over SEEK in that it does not have the capability to solve a refinement problem on its own. Also, a more general knowledge representation format using production IF–THEN rules is used in SEEK2. Ž .

Experimental tests on existing knowledge, to determine the number of false positives and false negatives, provide information to decide whether to generalize or specialize existing knowledge. When the number of cases of false positive examples exceeds the number of false negative examples, the existing knowledge is specialized, otherwise generalization occurs. False positive examples of a given class are defined as the case when a testing example is classified as being in a given class when it actually belongs to another class. On the other hand, false negative examples of the class should be classified as the given class, but are classified as the other. The implication of this rule refinement is quite straightforward. If the screening device is too coarse gen-Ž eral that many unnecessary objects false positive. Ž objects can enter the region, then make the screen-. ing stricter by adding more barriers specialization .Ž . On the other hand, if the screening is so strict that many objects belonging to the region cannot come in Ž . Ž false negative examples , loosen the screening generalization ..

In the case of specialization, the most frequently used clauses propositions or descriptors are addedŽ .

Table 1  
Characteristics of knowledge refining systems

<table><tr><td></td><td>SEEK, SEEK2</td><td>FOIL, GOLEM</td><td>KBANN</td><td>KREFS</td></tr><tr><td>Knowledge representation</td><td>Propositional</td><td>Predicate</td><td>Propositional</td><td>Predicate</td></tr><tr><td>Consistency of refinement</td><td>Inconsistent</td><td>Consistent</td><td>Consistent</td><td>Consistent</td></tr><tr><td>Domain knowledge dependency</td><td>Independent</td><td>Dependent</td><td>Independent</td><td>Independent</td></tr><tr><td>Direction of refinement</td><td>Specialization or generalization</td><td>Specialization</td><td>Specialization</td><td>Specialization then reconstruction</td></tr></table>

to the rule. Statistically, the most frequently used clauses have the greatest potential to specialize the rule. It is true, however, that this new clause may fail to specialize the given rule. Thus, this rough hillclimbing method is unreliable. Moreover, if there is a slight difference between the number of false positive and false negative examples in the worstŽ situation, the numbers can be the same , the refine-. ment direction cannot be determined. The hill-climbing method used cannot guarantee global optima in its search for the ideal set of propositions in its knowledge.

## 3.1.2. Knowledge-based artificial neural network ( )KBANN

KBANN is a hybrid learning system that combines explanation-based learning 25,11 , and neural<sup>w</sup> <sup>x</sup> network algorithms. It tries to combine the strength of these two systems. The disadvantage of lengthy training time of neural networks are alleviated by using explanation-based learning EBL to produce Ž . initial rules rapidly from a small number of training examples. Then, the neural net refines the knowledge and identifies ignored important features, thus improving the quality of the acquired knowledge.

This hybrid algorithm has been shown to be efficient and accurate. It is faster than an artificial neural network in building the rules, and results in more accurate knowledge compared to EBL. Its other advantage is that it is not destructive in the rule refining process. The neural net refines the existing rule by adding important but ignored conditions. However, this non-destructive nature can be a disadvantage if the knowledge is to be modified on a large scale. Moreover, the maintenance cost is high if the application dictates frequent modification since training the neural network is inevitable eventually regardless of its reduced convergence time. Training the neural network is very expensive in terms of time due to the iterative nature of training algorithms for neural networks. Its other disadvantage is that its rule representation is limited to propositional representation only.

## 3.2. Predicate Õalue representation systems

## 3.2.1. FOIL and GOLEM

Derived from ID3 31 , FOIL 33 is an attribute<sup>w x</sup> <sup>w x</sup> value learning system that learns clauses from training examples by repeatedly adding corresponding attributes that cover part of the training examples. Its domain knowledge consists of clauses that explain each set of examples. FOILs representation of a rule has been shown to be efficient and the process of refining the rule is included in the knowledge building process. Though its representation is easy to implement and relatively efficient, its success is heavily dependent on the broad and secure domain knowledge that is hard to achieve in its completeness in many cases. As its process of refinement is parallel to that of building the knowledge base, careful and time-consuming effort for obtaining background knowledge are required before building the system.

Muggleton and Feng 26 present a more struc- <sup>w</sup> <sup>x</sup> tured method of learning algorithm quite similar to Quinlan’s FOIL. By developing Plotkin’s 28,29 <sup>w</sup> <sup>x</sup> concepts of relatiÕe least general generalization ( ) rlgg , they try to avoid the restrictions of both Quinlan’s FOIL and Plotkin’s rlgg system. Plotkin’s notion of rlgg replaces search by the process of constructing a unique clause covering a given set of examples. While FOIL works with both positive and negative examples, their system GOLEM can workŽ . without this limitation. It can work with just one positive or negative example.

Its main advantage is in avoiding timeless searches in the construction of clauses. It uses existing clauses while selecting new clauses to add. When a required clause is not present in the existing domain knowledge, there is no other way to generate this necessary clause. Regardless of this weakness, FOIL and GOLEM carry good features: they are predicate representation systems and their refinement methods are consistent with the method they use to generate the rules in their knowledge base. This consistency avoids additional time and cost incurred in maintaining different systems for building and refining knowledge.

## 4. The proposed knowledge refinement system

## 4.1. The KREFS framework

The knowledge refinement framework under which KREFS operates is given in Fig. 2. The framework is assembled from four major modules.

![](/api/attachments/BAHKRX33/fulltext/images/2f170041b0671f27e07eec52642e8fd031493c8fc8033efd34adcddc53217ed2.jpg)  
Fig. 2. The KREFS knowledge management framework.

Each of these works in consort to produce the final refined knowledge as output. Being just a generic overall framework, Fig. 2 is not specific about the methodologies that are used in each of the modules. However, it is not of concern here since each of those modules by themselves are complex and a description of the possible sub-components that could constitute these modules is beyond the scope of this paper. In this paper, we are particularly interested in one of the modules—the knowledge refinement module—as represented in Fig. 2.

KREFS, as presented in this study, essentially requires ‘clean’ data for further processing. As in most data mining applications, the input to the system is raw unprocessed data. The raw data itself could be directly from sensors, checkout registers in stores, demographic and other customer information from files, response to questionnaires, among others. Most data warehouses that are repositories for such data tend to contain data on more characteristics Ž . represented as variables than are necessary for a given data mining application. Although some of the characteristics may clearly be included or elimi-Ž nated for from further consideration, sometimes it. Ž . is necessary to include the ones that are not clearly in the list to be discarded in the hope that they might contain potentially useful information. In addition to selecting the variables to be considered further, the data set itself has to be checked for any missing or incomplete values. The pre-processing stage might also involve generating additional higher-order variables to improve the information content of the resulting data.

Once cleaned and pre-processed, the data passes on to the next module where implicit ‘useful’ patterns are extracted. This stage could involve anywhere from a single simple analytical methodology to a suite of methods that work together to extract or discover patterns from data. KREFS uses induced decision trees to extract patterns from data. The extracted knowledge then passes to the next module where knowledge refinement takes place. Since knowledge refinement itself is an iterative process, a performance element evaluates the intermediate re-Ž . fined knowledge and feeds back the resulting performance scores to the knowledge refinement module. The knowledge refinement module then suggests additional training examples based on those examples that were classified incorrectly. These examples are input to the decision tree inducer to obtain additional decision rules. These rules are merged with the knowledge base from the previous iteration. This process is repeated until a pre-specified performance e.g., 10% classification accuracy is reached.Ž . The resulting knowledge forms the output from the system. It should be noted that knowledge refinement is not a one-shot procedure. Periodic evaluation and refinement of knowledge is necessary to avoid problems associated with stale knowledge.

## 4.2. KREFS and hyperspace

Knowledge REFinement System KREFS has theŽ . practicality inherent in predicate value representation. In KREFS, existing knowledge suggests the direction to search for additional training examples. KREFS was developed within the context of a pattern-directed environment, where knowledge is represented in rule or decision tree form for eachŽ . pattern in the system. Each rule represents a unique state of the system as a condition and the best strategy as an action. Here, state refers to a snapshot of the system taken at any given point in time. KREFS generates production rules of the form:

## IF condition THEN action,

where condition may be a compound condition represented in conjunctive normal form, say, age ofŽ open accounts<sup>)</sup>10 years and recent credit in-. Ž quiries<sup>-</sup>2 , where ‘age of open accounts’ and ‘re-. cent credit inquiries’ are measures characterizing the system of interest. The action refers to the best strategy pursued with a given for example, theŽ lending risk objective when these conditions exist.. An example rule might then be:

IF age of open accounts Ž . <sup>)</sup>10 years

## & recent credit inquiries Ž . <sup>-</sup> 2 THEN grant loan.

We could visualize these conditions as hyperplanes establishing borders in a hyperspace. Examples supporting this concept belong to this hyperspace. An example that lies within this hyperspace is a positive example of the represented pattern, while an example falling outside this hyperspace is a negative example. A false positive example is one that falls inside the hyperspace, yet for which the given strategy is not the best. A false negative example is one that falls outside the hyperspace, yet for which the given strategy is the best.

Continuing with this hyperspace of n dimensions, we can visualize further partitioning of the space through inductive learning e.g., C4.5 34 . We splitŽ <sup>w</sup> <sup>x</sup>. the hyperspace on one axis at the point where the newly created hyper-plane results in maximum information gain. The information gain of a hyper-plane is: $B ^ { 0 } \mathrm { ~ - ~ } M _ { k }$ where $B ^ { 0 } = - p ^ { \mathrm { p o s } } \log _ { 2 } p ^ { \mathrm { p o s } } -$ $p ^ { \mathrm { n e g } } \log _ { 2 } p ^ { \mathrm { n e g } }$ , and $p ^ { { \mathrm { p o s } } }$ is the proportion of the total number of positive examples of the given strategy to the total number of training examples before splitting and $p ^ { \mathrm { n e g } }$ is the proportion of the total number of negative examples of the given strategy to the total number of training examples before splitting. $B ^ { 0 }$ is the measurement of instability of all training examples. $M _ { k }$ is the sum of instability of two hyperspaces created by the given hyper-plane :

$$
M _ {k} = \sum_ {i} w _ {i k} B _ {k} ^ {i},
$$

where $w _ { i k }$ is the proportion of training examples in the hyperspace created by the hyper-plane and $B _ { k } ^ { i }$ is the measurement of instability of hyperspace . A small number of supporting training examples leads to overgeneralization of the sparsely populated hy- Ž . perspace. Adding more representative training examples can materialize a more compact hyperspace, and precise hyper-planes.

The goal of rule refinement in KREFS is to reduce the error due to these over-generalized rules. This refining process continues until it reaches minimum prediction error of threshold value say, 10% .Ž . False positive testing examples are used to identify the gray suspicious area. New additional trainingŽ . examples are obtained from the gray area. Each iteration of refinement is expected to induce a new rule by splitting and specializing the existing hyperspace covered by a rule or introducing another axis Ž . dimension . These refinement processes lead to specialization of the knowledge. Sometimes two juxtaposed hyperspaces of the same strategy can be merged—a case of generalization of the rule by enlarging the hyperspace of the rule. KREFS initiates minor local changes to existing knowledge. It is Ž . quite possible, however, to have major structural changes in number of dimensions and hyper-planes. These changes can lead to major disruption through creation of a new knowledge base.

KREFS has several good features: it has a predicate value representation form that is more flexible than that of propositional representation; its refinement process is consistent with that of knowledge generation. The primary advantages of KREFS are its independence of domain knowledge and its automatic guidance in suggesting directions or regions to obtain additional training examples for knowledge refinement.

## 4.3. Rule refinement process

In a given learning environment, a rule r is represented by a pattern m in the system and a strategy actionŽ . Ž d. Learned knowledge R a set of production rules $\mathbf { r } _ { i } )$ is generated from  Ž E a set of examples $\mathrm { e } _ { i }$ covered by $\mathbf { r } _ { i } )$ . A pattern $M _ { i }$ Ž a hyperspace is divided into. $P _ { i }$ and $C _ { i } .$ . In hyperspace $P _ { i }$ is an induced possibly over-generalized hyperspace Ž . that needs to be tested and refined. $C _ { i }$ is the rest of the area in the hyperspace supported by the examples in that hyperspace. Based on $P _ { i } ,$ , a set of testing points are selected, and then a set of testing examples S is generated using these testing points and all available action strategies.

Refining hyperspace continues until the prediction error Ž . h resulting from overgeneralization reaches a pre-specified minimum value $\left( \alpha \right)$ . If the error is still high, a set of false positive test examples from S above as well as supporting positive examples to identify the suspicious region in the hyperspace is used. Additional training examples are obtained from the suspicious region. Knowledge is refined with the set of all training examples including additional new training examples.

The procedure for generating additional training examples utilizes the same inductive learner to identify the over-generalized hyperspace of patterns. Then additional training patterns are selected from the suspicious region gray area in the hyperspace. Ž . Additional training examples are obtained using selected patterns with their most appropriate corresponding strategies. As knowledge refinement process proceeds, the new rules are integrated in the knowledge base. When inconsistencies arise between the current knowledge base and the newly generated rules, the most general rules are kept. The staleŽ . rules in the knowledge base that are no longer valid are eliminated periodically.

This knowledge refinement process is summarized as follows Ž . Algorithm refine rule .

Step 1. Initialization: Set $n = 1 , \ R ^ { 1 }$ as the initial knowledge, and $C _ { i } ^ { n }$ the source patterns for generating this initial knowledge.

Ž . Step 2. Evaluation: a For each $r _ { i } \in R ^ { n }$ , determine $C _ { i } ^ { n }$ , and $P _ { i } ^ { n } = M _ { i } ^ { n } - C _ { i } ^ { n }$ . Determine the set of testing patterns $T _ { i } ^ { n } \subset \bigcup _ { i } { } ^ { R _ { n } } P _ { i } ^ { n }$ such that $\left| T ^ { n } \right| = k .$ bŽ . Generate set $S ^ { n }$ consisting of k testing examples obtained from $T ^ { n }$ for each strategy in D. Determine the prediction accuracy by using $R ^ { n }$ on $S ^ { n }$

Step 3. Termination: If $\alpha \geq h$ , stop. Else, go to Step 4.

Ž .Step 4. Iteration: a For each $r _ { i } \in R ^ { n }$ , determine the set of testing patterns $W _ { i } ^ { n } \subset T _ { i } ^ { n }$ for which $d _ { i }$ is not found to be the best action strategy or classifica-Ž . tion . Let $N _ { i } ^ { n } = \{ ( W _ { i 1 } ^ { n } , d _ { i 1 } ) , \dots , ( W _ { i W i } ^ { n } , d _ { i W i } ) \}$ be the corresponding set of testing examples where ${ W } _ { i 1 } ^ { n }$ denotes the subset of patterns for which the best strategy was found to be $d _ { i j } , j = 1 , \ldots , W _ { i } , d _ { i j } \neq d _ { i } ,$ and $W _ { i }$ is the number of such subsets. b For eachŽ . $r _ { i } \in R ^ { n }$ , generate a set of rules $R _ { i } ^ { n }$ using the inductive learning algorithm with $e _ { i } ^ { n } \cup N _ { i } ^ { n }$ as the set of training examples.

Update the set of selection rules or knowledge: $R ^ { n + \bar { 1 } } = R _ { n } \cup \left( \cup _ { i } ^ { R ^ { n } } R _ { i } ^ { n } \right)$ . For $i = 1 , \ldots , R ^ { n }$ , determine $M _ { i } ^ { n } = \bigcup _ { i 1 } ^ { W _ { i } } M _ { i 1 } ^ { N }$ and $\begin{array} { r } { C _ { i } ^ { n } = \bigcup _ { i } ^ { W _ { i } } W _ { i 1 } ^ { n } } \end{array}$

Ž .c Set $n \gets n + 1$ , and go to Step 2.

## 5. Comparing knowledge refinement systems

We study the relative performance of an existing knowledge refinement system against the proposed system when applied to the same problem set. We use FOIL as a representative system for evaluating KREFS since they both use predicate representation. FOIL learns clauses expressed in terms of relationship between arguments from training examples. It is expressed in the form: $C  L _ { 1 } , L _ { 2 } , L _ { 3 } , . . . , L _ { n } .$ The clause is grown by adding a new literal $L _ { i } .$ The FOIL algorithm is as follows:

1. Initialize the local training set $T _ { 1 }$ to the current training set and let $i = 1$

2. While $T _ { i }$ contains negative tuples examples :Ž .

2.1. Find a literal $L _ { i }$ to add to the right-hand side of the clause.

2.2. Generate a new training set $T _ { i + 1 }$ based on those tuples in $T _ { i }$ that satisfy $L _ { i }$

If $L _ { i }$ introduces new variables, each tuple from $T _ { i }$ may give rise to several expanded tuples in $T _ { i + 1 }$

The label of each tuple in $T _ { i + 1 }$ is the same as that of the parent tuple in $T _ { i } .$

3. Increment i and go to Step 2.

Consider a learning concept of whether a node can be reached from another in a directed graph Fig.Ž 3 . The example clauses learned by FOIL include the. following:

Intermediate clauses: Can-reachŽ . X 1, X 2

§Linked-toŽ . X 1, X 2

Final clauses: Can-reachŽ . X 1, X 2

§Linked-toŽ . Ž . X 1, X 3 , Can-reach X 3, X 2

A major disadvantage of FOIL is its reliance on domain knowledge. Deriving literals like ‘Linked-to’ or ‘Can-reach’ is not an easy task. In KREFS, the burden of domain knowledge dependency is alleviated. As long as training examples are represented in tabular format, the concept is learned and refined automatically. To illustrate KREFS’ wide applicability, we will convert the graph to a form suitable for

KREFS and illustrate its learning and refining capability.

Attributes

<table><tr><td>chara</td><td>logical (out, in, inter)</td></tr><tr><td>charb</td><td>logical (out, in, inter)</td></tr><tr><td>numouta</td><td>integer</td></tr><tr><td>numina</td><td>integer</td></tr><tr><td>numoutb</td><td>integer</td></tr><tr><td>numinb</td><td>integer</td></tr><tr><td>distab</td><td>integer</td></tr><tr><td>deptha</td><td>integer</td></tr></table>

where a™b: a is a source node and b is a destination node; chara is the characteristic of source node a; ‘out’ nodes are supply nodes; ‘in’ nodes are demand nodes that only receive; ‘inter’ nodes are intermediate nodes transporting the inflow to the outflow in the network; charb is the characteristic of destination node b; numouta is the number of outflows of source node a; numina is the number of inflows of source node a; numoutb is the number of outflows of destination node b; numinb is the number of inflows of destination node b; distab is the minimum number of nodes between ‘a’ and ‘b’ plus

![](/api/attachments/BAHKRX33/fulltext/images/8b6dc980a941e9745594ace34ecbcedd0ed609a36d299af252e660769ad672b2.jpg)  
Fig. 3. A directed graph.

1; and deptha is the maximum number of outflow nodes from node a. There are two classes: ‘reachable’ yes , and ‘unreachable’ no . Training exam-Ž . Ž . ples Appendix A are tagged as ‘ab’ to identifyŽ . source and destination i.e., 01: the source node is 0,Ž and the destination node is 1 . Appendix B provides . detailed explanation<sup>r</sup>illustration of the steps involved in this process. Initially, 10 rules were generated from the data:

```txt
r₁: (distab < 4) & (chara = in) → no (unreachable)
r₂: (distab < 4) & (chara = inter) & (numoutb < 2) → yes (reachable)
r₃: (distab < 4) & (chara = inter) & (numoutb ≥ 2) & (charb = inter) & (numouta < 2) → no (unreachable)
r₄: (distab < 4) & (chara = inter) & (numoutb ≥ 2) & (charb = inter) & (numouta ≥ 2) & (distab < 1) → no (unreachable)
r₅: (distab < 4) & (chara = inter) & (numoutb ≥ 2) & (charb = inter) & (numouta ≥ 2) & (distab ≥ 1) → yes (reachable)
r₆: (distab < 4) & (chara = inter) & (numoutb ≥ 2) & (charb = out) → no (unreachable)
r₇: (distab < 4) & (chara = out) → yes (reachable)
r₈: (distab ≥ 4) & (numinb < 2) → no (unreachable)
r₉: (distab ≥ 4) & (numinb ≥ 2) & (deptha < 3) → no (unreachable)
r₁₀: (distab ≥ 4) & (numinb ≥ 2) & (deptha ≥ 3) → yes (reachable).
```

A testing example of 75: out, in, 2, 0, 0, 1, 3, 1, no unreachable contradicts rule 7, rŽ .  <sup>s</sup>Ž . distab<sup>-</sup>4 and chara Ž . <sup>s</sup> out . Since there is one more testing 4 example that is correctly identified by the knowledge, the prediction error rate is 50%. KREFS is initiated to refine the knowledge. The new rules refined by KREFS are:

```txt
IF (deptha < 2) & (numinb < 2) THEN no.
IF (deptha < 2) & (numinb ≥ 2) & (distab < 3) & (chara = in) THEN no.
IF (deptha < 2) & (numinb ≥ 2) & (distab < 3) & (chara = inter, out) THEN yes.
IF (deptha < 2) & (numinb ≥ 2) & (distab ≥ 3) THEN no.
IF (deptha ≥ 2) & (charb = in) THEN yes.
```

```txt
IF (deptha ≥ 2) & (charb = inter) & (distab < 1)
THEN no.
IF (deptha ≥ 2) & (charb = inter) & (distab ≥ 1)
THEN yes.
IF (deptha ≥ 2) & (charb = out) THEN no.
```

These refined rules explain the reachability in the directed graph without errors. Compared to FOIL, the acquired knowledge does not take a clean-cut form in representing the concept. Yet, KREFS identifies the concept ‘reachable’ via the existence of adjacent transmitting node in terms of ‘ depthaŽ . <sup>G</sup> 2 and charbŽ . <sup>s</sup>in ’. The condition of ‘deptha<sup>-</sup>2’ restricts the case of direct node connection. As refinement proceeds, knowledge refined by KREFS will capture the distinct concept ‘reachable’.

## 6. KREFS for bankruptcy prediction

## 6.1. A bankruptcy prediction example

This data set consists of descriptions of 182 Belgian companies, half of which went bankrupt during the period 1987–1989. The other half non-bankrupt companies are of comparable assets and sales, belonging to similar industries. The data were extracted from a CD-ROM published by the Belgian National Bank, covering the financial reports of all Belgian companies over 5 years. The following Funds Flow components ratios of the following with total cash Ž flow are used in this study: 1 net operating flow, . Ž . Ž . Ž . Ž . 2 net investment flow, 3 dividends, 4 fixed coverage expenditures, 5 changes in receivables,Ž . Ž . Ž . 6 change in inventories, 7 change in other current assets, 8 change in payables, 9 change in otherŽ . Ž . current liabilities, 10 change in net financial andŽ . Ž . 11 change in net other assets and liability. Besides funds flow components, we also included additional financial variables such as the ratio of the total cash flow<sup>r</sup>total asset, accumulated depreciation<sup>r</sup>fixed asset, and sales trend. These variables are represented as $x _ { 1 } , \ldots , x _ { 1 4 }$ . We represent the bankrupt cases as 1 and the non-bankrupt cases as 0.

Since the data set was already archived, preprocessing of data mainly involved selecting the appropriate variables of interest as well as removing those cases with missing values. The cleaned data

IF (x1 < 30) & (x7 < 22) THEN 1.

IF (x1 < 20) & (x7≥ 22) THEN 0.

IF (20 ≤ x1 < 30) & (x6 < 25) & (x2 ≥ 24) & (22 ≤ x7) THEN 0.

IF (20 ≤ x1 < 30) & (x6 ≥ 25) & (x10 < 28) & (22 ≤ x7) THEN 1.

IF (20 ≤ x1 < 30) & (x6 ≥ 25) & (22 ≤ x7) & (x10 ≥ 28) & (x11 < 22) THEN 1.

IF (20 ≤ x1 < 30) & (x6 ≥ 25) & (22 ≤ x7) & (x10 ≥ 28) & (x11 ≥ 22) THEN 0.

IF (30 ≤ x1) & (21 ≤ x4) & (x12 < 31) THEN 1.

IF (30 ≤ x1) & (21 ≤ x4) & (x12 ≥ 31) & (×13 < 36) & (x8 < 24) THEN 0.

IF (30 ≤ x1< 35) & (21 ≤ x4) & (x12 ≥ 31) & (x13 < 36) & (x8 ≥ 24) & (x3<25) THEN 0

IF (35 ≤ x1) & (21 ≤ x4) & (x12 ≥ 31) & (x13 < 36) & (x8 ≥ 24) & (x3 < 25) THEN 1.

IF (30 ≤ x1) & (21 ≤ x4) & (x12 ≥ 31) & (x13 < 36) & (x8 ≥ 24) & (x3 ≥ 25) THEN 1.

IF (30 ≤ x1) & (21 ≤ x4 < 22) & (x12 ≥ 31) & (x13 ≥ 36) THEN 0.

IF (30 ≤ x1< 37) & (22 ≤ x4) & (x12 ≥ 31) & (x13 ≥ 36) & (x11 < 24) THEN 1.

IF (37 ≤ x1) & (22 ≤ x4) & (x12 ≥ 31) & (x13 ≥ 36) & (x11 < 24) THEN 0.

IF (30 ≤ x1) & (22 ≤ x4) & (x12 ≥ 31) & (x13 ≥ 36) & (x11 ≥ 24) THEN 1.

IF (20 ≤ x1 < 27) & (x7 ≥ 22) & (x6 < 25) & (x2 < 24) & (x12 < 32) THEN 1.

IF (27 ≤ x1 < 30) & (x7 ≥ 22) & (x6 < 25) & (x2 < 24) & (x12 < 32) THEN 0.

IF (20 ≤ x1 < 30) & (x7 ≥ 22) & (x6 < 25) & (x2 < 24) & (x12 ≥ 32) THEN 0.

IF (30 ≤ x1) & (x4 < 21) THEN 0.

Fig. 4. Rules generated before knowledge refinement.

IF (x1 < 20) & (x7 ≥ 22) THEN 0.

IF (20 ≤ x1 < 30) & (x6 < 25) & (x2 ≥ 24) & (22 ≤ x7) THEN 0.

IF (20 ≤ x1 < 30) & (x6 ≥ 25) & (22 ≤ x7) & (x10 < 28) THEN 1.

IF (20 ≤ x1 < 30) & (x6 ≥ 25) & (22 ≤ x7) & (x10 ≥ 28) & (x11 < 22) THEN 1.

IF (20 ≤ x1 < 30) & (x6 ≥ 25) & (22 ≤ x7) & (x10 ≥ 28) & (x11 ≥ 22) THEN 0.

IF (30 ≤ x1) & (21 ≤ x4) & (x12 < 31) THEN 1.

IF (30 ≤ x1) & (21 ≤ x4) & (x12 ≥ 31) & (x13 < 36) & (x8 < 24) THEN 0.

IF (30 ≤ x1< 35) &(21 ≤ x4) & (x12 ≥ 31) & (x13 < 36) & (x8 ≥ 24) & (x3 < 25) THEN 0.

IF (35 ≤ x1) & (21 ≤ x4) & (x12 ≥ 31) & (x13 < 36) & (x8 ≥ 24) & (x3 < 25) THEN 1.

IF (30 ≤ x1) & (21 ≤ x4) & (x12 ≥ 31) & (x13 < 36) & (x8 ≥ 24) & (x3 ≥ 25) THEN 1.

IF (30 ≤ x1) & (21 ≤ x4 < 22) & (x12 ≥ 31) & (x13 ≥ 36) THEN 0.

IF (30 ≤ x1<37) & (22 ≤ x4) & (x12≥ 31) & (x13 ≥ 36) & (x11 <24) THEN 1.

IF (37 ≤ x1) & (22 ≤ x4) & (x12≥ 31) & (x13 ≥ 36) & (x11 <24) THEN 0.

IF (30 ≤ x1) & (22 ≤ x4) & (x12≥ 31) & (x13 ≥ 36) & (x11 ≥ 24) THEN 1.

IF (20 ≤ x1 < 30) & (x6 < 25) & (x2 < 24) & (22 ≤ x7 < 25) THEN 0.

IF (20 ≤ x1 < 30) & (x6 < 25) & (x2 < 18) & (25 ≤ x7) THEN 0.

IF (20 ≤ x1 < 30) & (x6 < 25) & (18 ≤ x2 < 24) & (25 ≤ x7) THEN 1.

IF (30 ≤ x1) & (x4 < 16) THEN 1.

IF (30 ≤ x1) & (16 ≤ x4< 21) & (x7 < 26) THEN 0.

IF (30 ≤ x1) & (16 ≤ x4< 21) & (x7≥ 26) THEN 1.

Fig. 5. Rules generated after rule refinement.

are then fed to the pattern extraction module, which is an inductive decision tree generator in this study. The initial rules thus induced by the inductive learner are given in Fig. 4. It should be noted that the bias introduced by the method used to generate the initial knowledge base is not of concern here since KREFS does not depend on the quality of the initial knowledge base. The fact that real-valued data are used for inductive learning is also not of concern in this study since the process of generating the initial knowledge base as well as the iterative refinement process used in KREFS operate with the same bias, and the purpose here is to illustrate the operationalization of KREFS and not to optimize performance of KREFS.

Except for variables $x _ { 5 } , \ x _ { 9 } .$ , and $x _ { 1 4 }$ , the remaining eleven variables are represented in the induced rules given above. KREFS then proceeded to refine the rules, with the classification error rate on testing examples at 25% after the first iteration beforeŽ knowledge refinement . This error rate is much higher. than the pre-specified error rate of 10%. This necessitates another or a few more iteration s of KREFS.Ž . Ž . After an average of about three iterations, KREFS did converge to a lower error rate. KREFS continued the process until the classification error rate on testing examples was below 10%, which was our prespecified threshold. The final error rate was 8.33%, and the corresponding set of final decision rules are given in Fig. 5.

In the case illustrated in Figs. 4 and 5, the variables selected to be included in the knowledge base are the same as those that were included after the first iteration before knowledge refinement . This isŽ . purely coincidental, and it is possible to have fewer or more variables in the final knowledge base compared to the content of the knowledge base after the first iteration. It is interesting to note that the first 15 rules in both the above sets are the same. These 15 rules probably contain the core information as represented in the knowledge base. KREFS’ knowledge refinement process modified and added to the last four rules in the original knowledge base, to form six new rules as given in the last six lines in the final knowledge base Table 2 .Ž .

To alleviate any bias due to sampling, we used 10-fold cross-validation of this data. The results provided in Figs. 4 and 5 correspond to the first set of the 10 evenly split random samples. Table 2 is a summary of classification results on testing examples for all 10 sets in 10-fold cross-validation. The initial number of examples in all these 10 sets is an average of 18.2 10% of the 182 examples, due to 10-foldŽ cross-validation , with 18 in eight of the sets and 19. in the remaining two sets. Across iterations of KREFS, the number of examples in the testing set is varied depending on the number of misclassified examples before knowledge refinement, to facilitate better generalization in fewer iterations.

Table 2  
Classification performance on testing examples

<table><tr><td></td><td>Classification (%) without knowledge refinement</td><td>Classification (%) after knowledge refinement</td></tr><tr><td>1</td><td>75.00</td><td>91.67</td></tr><tr><td>2</td><td>66.67</td><td>93.75</td></tr><tr><td>3</td><td>58.33</td><td>90.00</td></tr><tr><td>4</td><td>75.00</td><td>91.67</td></tr><tr><td>5</td><td>75.00</td><td>91.67</td></tr><tr><td>6</td><td>58.33</td><td>95.00</td></tr><tr><td>7</td><td>41.67</td><td>92.86</td></tr><tr><td>8</td><td>33.33</td><td>90.63</td></tr><tr><td>9</td><td>50.00</td><td>91.67</td></tr><tr><td>10</td><td>66.67</td><td>93.75</td></tr></table>

The final set of rules is not concise compared to the knowledge base after the first iteration. Clearly, the final set of rules is better and more accurate compared to the original set of rules developed during the very first iteration. Although the modifications to the knowledge base that occurred since it was originally developed do not seem to be major, it does have an appreciable effect on the generalizability of these decision rules. For critical applications, such as in evaluating bank loans for predicting bankruptcy in the future, any improvement in the quality of knowledge or information extracted from raw data can make the difference between a bad and a good loan. This applies even to cases where there has not been any elapse in time since first extracting useful information through data mining.

## 7. Conclusion

Data mining systems are becoming a necessity to extract useful information from huge amounts of archived data in order to achieve competitive advantage. This study focused on knowledge refinement, which is a rather neglected component of data mining systems. Without knowledge refinement, ‘useful information extracted by data mining systems at an earlier point in time is bound to become stale. The importance of a knowledge refinement component in data mining systems cannot be understated.

In this paper, we have conducted a comparative study on knowledge refinement systems including the proposed KREFS. The notable refinement systems include SEEK, SEEK2, FOIL, GOLEM, and KBANN. KREFS has more expressive power compared to SEEK, SEEK2, and KBANN, which are propositional value representation systems. This advantage enables KREFS to be widely applicable in more realistic applications. As opposed to KBANN’s limitation in further refinement when all training examples are exhausted, KREFS keeps refining its knowledge by intelligently self-guiding the generation of new training examples. Typical problems of dependency on domain knowledge that is inherent in systems like FOIL or GOLEM are not found in KREFS. Rather, KREFS can identify the distinct concept from scratch. The flexibility, wide applicability, and more accurate knowledge refinement process of KREFS are illustrated in this study.

One of the limitations of KREFS is that it is based on the premise that training examples with desired characteristics as per the dictates of the algorithm will be available. Although this seems like a hard constraint, the characteristics desired are broad enough to allow for ease of obtaining necessary training examples. Nevertheless, this still remains a limitation. A possible extension to KREFS would be to take into account objective s specified by the userŽ . while refining the rules. For example, the user can request KREFS to generate rules that are parsimonious.

w x <sub>6</sub> <sup>w</sup> <sup>x</sup> <sub>10</sub> <sup>w</sup> <sup>x</sup> <sub>17</sub> <sup>w</sup> <sup>x</sup> <sub>32</sub> <sup>w</sup> <sup>x</sup> <sub>38</sub>

## 8. Uncited references

Appendix A. Training examples

<table><tr><td>01</td><td>out</td><td>inter</td><td>2</td><td>0</td><td>1</td><td>1</td><td>1</td><td>4</td><td>yes</td></tr><tr><td>03</td><td>out</td><td>inter</td><td>2</td><td>0</td><td>2</td><td>1</td><td>1</td><td>4</td><td>yes</td></tr><tr><td>76</td><td>out</td><td>inter</td><td>2</td><td>0</td><td>1</td><td>2</td><td>1</td><td>1</td><td>yes</td></tr><tr><td>78</td><td>out</td><td>in</td><td>2</td><td>0</td><td>0</td><td>2</td><td>1</td><td>1</td><td>yes</td></tr><tr><td>02</td><td>out</td><td>in</td><td>2</td><td>0</td><td>0</td><td>2</td><td>2</td><td>4</td><td>yes</td></tr><tr><td>05</td><td>out</td><td>in</td><td>2</td><td>0</td><td>0</td><td>1</td><td>3</td><td>4</td><td>yes</td></tr><tr><td>08</td><td>out</td><td>in</td><td>2</td><td>0</td><td>0</td><td>2</td><td>4</td><td>4</td><td>yes</td></tr><tr><td>04</td><td>out</td><td>inter</td><td>2</td><td>0</td><td>2</td><td>1</td><td>2</td><td>4</td><td>yes</td></tr><tr><td>06</td><td>out</td><td>inter</td><td>2</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>yes</td></tr><tr><td>12</td><td>inter</td><td>in</td><td>1</td><td>1</td><td>0</td><td>2</td><td>2</td><td>1</td><td>yes</td></tr><tr><td>32</td><td>inter</td><td>in</td><td>2</td><td>1</td><td>0</td><td>2</td><td>1</td><td>3</td><td>yes</td></tr><tr><td>45</td><td>inter</td><td>in</td><td>2</td><td>1</td><td>0</td><td>1</td><td>1</td><td>2</td><td>yes</td></tr><tr><td>68</td><td>inter</td><td>in</td><td>1</td><td>2</td><td>0</td><td>2</td><td>1</td><td>1</td><td>yes</td></tr><tr><td>46</td><td>inter</td><td>inter</td><td>2</td><td>1</td><td>1</td><td>2</td><td>1</td><td>2</td><td>yes</td></tr><tr><td>48</td><td>inter</td><td>in</td><td>2</td><td>1</td><td>0</td><td>2</td><td>2</td><td>2</td><td>yes</td></tr><tr><td>34</td><td>inter</td><td>inter</td><td>2</td><td>1</td><td>2</td><td>1</td><td>1</td><td>3</td><td>yes</td></tr><tr><td>35</td><td>inter</td><td>in</td><td>2</td><td>1</td><td>0</td><td>1</td><td>2</td><td>3</td><td>yes</td></tr><tr><td>36</td><td>inter</td><td>inter</td><td>2</td><td>1</td><td>1</td><td>2</td><td>2</td><td>3</td><td>yes</td></tr><tr><td>38</td><td>inter</td><td>in</td><td>2</td><td>1</td><td>0</td><td>2</td><td>3</td><td>3</td><td>yes</td></tr><tr><td>68</td><td>inter</td><td>in</td><td>1</td><td>2</td><td>0</td><td>2</td><td>1</td><td>1</td><td>yes</td></tr><tr><td>13</td><td>inter</td><td>inter</td><td>1</td><td>1</td><td>2</td><td>1</td><td>2</td><td>1</td><td>no</td></tr><tr><td>14</td><td>inter</td><td>inter</td><td>1</td><td>1</td><td>2</td><td>1</td><td>3</td><td>1</td><td>no</td></tr><tr><td>15</td><td>inter</td><td>in</td><td>1</td><td>1</td><td>0</td><td>1</td><td>4</td><td>1</td><td>no</td></tr><tr><td>18</td><td>inter</td><td>in</td><td>1</td><td>1</td><td>0</td><td>2</td><td>5</td><td>1</td><td>no</td></tr><tr><td>33</td><td>inter</td><td>inter</td><td>2</td><td>1</td><td>2</td><td>1</td><td>0</td><td>3</td><td>no</td></tr><tr><td>55</td><td>in</td><td>in</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>no</td></tr><tr><td>20</td><td>in</td><td>out</td><td>0</td><td>2</td><td>2</td><td>0</td><td>2</td><td>0</td><td>no</td></tr><tr><td>27</td><td>in</td><td>out</td><td>0</td><td>2</td><td>2</td><td>0</td><td>4</td><td>0</td><td>no</td></tr><tr><td>50</td><td>in</td><td>out</td><td>0</td><td>1</td><td>2</td><td>0</td><td>3</td><td>0</td><td>no</td></tr><tr><td>57</td><td>in</td><td>out</td><td>0</td><td>1</td><td>2</td><td>0</td><td>3</td><td>0</td><td>no</td></tr><tr><td>80</td><td>in</td><td>out</td><td>0</td><td>2</td><td>2</td><td>0</td><td>4</td><td>0</td><td>no</td></tr><tr><td>87</td><td>in</td><td>out</td><td>0</td><td>2</td><td>2</td><td>0</td><td>1</td><td>0</td><td>no</td></tr><tr><td>25</td><td>in</td><td>in</td><td>0</td><td>2</td><td>0</td><td>1</td><td>3</td><td>0</td><td>no</td></tr><tr><td>07</td><td>out</td><td>out</td><td>2</td><td>0</td><td>2</td><td>0</td><td>4</td><td>4</td><td>no</td></tr><tr><td>28</td><td>in</td><td>in</td><td>0</td><td>2</td><td>0</td><td>2</td><td>4</td><td>0</td><td>no</td></tr><tr><td>52</td><td>in</td><td>in</td><td>0</td><td>1</td><td>0</td><td>2</td><td>3</td><td>0</td><td>no</td></tr><tr><td>40</td><td>inter</td><td>out</td><td>2</td><td>1</td><td>2</td><td>0</td><td>2</td><td>2</td><td>no</td></tr><tr><td>30</td><td>inter</td><td>out</td><td>2</td><td>1</td><td>2</td><td>1</td><td>1</td><td>3</td><td>no</td></tr><tr><td>10</td><td>inter</td><td>out</td><td>1</td><td>1</td><td>2</td><td>0</td><td>1</td><td>1</td><td>no</td></tr><tr><td>17</td><td>inter</td><td>out</td><td>1</td><td>1</td><td>2</td><td>0</td><td>5</td><td>1</td><td>no</td></tr><tr><td>47</td><td>inter</td><td>out</td><td>2</td><td>1</td><td>2</td><td>0</td><td>2</td><td>2</td><td>no</td></tr><tr><td>67</td><td>inter</td><td>out</td><td>1</td><td>2</td><td>2</td><td>0</td><td>1</td><td>1</td><td>no</td></tr><tr><td>21</td><td>in</td><td>inter</td><td>0</td><td>2</td><td>1</td><td>1</td><td>1</td><td>0</td><td>no</td></tr><tr><td>26</td><td>in</td><td>inter</td><td>0</td><td>2</td><td>1</td><td>2</td><td>3</td><td>0</td><td>no</td></tr><tr><td>53</td><td>in</td><td>inter</td><td>0</td><td>1</td><td>2</td><td>1</td><td>2</td><td>0</td><td>no</td></tr></table>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
For each  $r_{i}$ , identify  $M_{i}$ .
</div>

<table><tr><td>56</td><td>in</td><td>inter</td><td>0</td><td>1</td><td>1</td><td>2</td><td>2</td><td>0</td><td>no</td></tr><tr><td>84</td><td>in</td><td>inter</td><td>0</td><td>2</td><td>2</td><td>1</td><td>2</td><td>0</td><td>no</td></tr><tr><td>23</td><td>in</td><td>inter</td><td>0</td><td>2</td><td>2</td><td>1</td><td>1</td><td>0</td><td>no</td></tr><tr><td>54</td><td>in</td><td>inter</td><td>0</td><td>1</td><td>2</td><td>1</td><td>1</td><td>0</td><td>no</td></tr><tr><td>86</td><td>in</td><td>inter</td><td>0</td><td>2</td><td>1</td><td>2</td><td>1</td><td>0</td><td>no</td></tr><tr><td>20</td><td>in</td><td>out</td><td>0</td><td>2</td><td>2</td><td>0</td><td>2</td><td>0</td><td>no</td></tr><tr><td>24</td><td>in</td><td>inter</td><td>0</td><td>2</td><td>2</td><td>1</td><td>2</td><td>0</td><td>no</td></tr><tr><td>63</td><td>inter</td><td>inter</td><td>1</td><td>2</td><td>2</td><td>1</td><td>2</td><td>1</td><td>no</td></tr><tr><td>70</td><td>out</td><td>out</td><td>2</td><td>0</td><td>2</td><td>0</td><td>4</td><td>1</td><td>no</td></tr><tr><td>71</td><td>out</td><td>inter</td><td>2</td><td>0</td><td>1</td><td>1</td><td>5</td><td>1</td><td>no</td></tr><tr><td>72</td><td>out</td><td>in</td><td>2</td><td>0</td><td>0</td><td>2</td><td>4</td><td>1</td><td>no</td></tr></table>

## Appendix B. Refining procedure by KREFS for identifying reachability between two nodes

Initial rules are induced from the training examples.

```txt
IF (distab < 4) & (chara = in) THEN no.
IF (distab < 4) & (chara = inter) & (numoutb < 2)
THEN yes.
IF (distab < 4) & (chara = inter) & (numoutb ≥ 2)
& (charb = inter) & (numouta < 2) THEN no.
IF (distab < 4) & (chara = inter) & (numoutb ≥ 2)
& (charb = inter) & (numouta ≥ 2) & (distab < 1)
THEN no.
IF (distab < 4) & (chara = inter) & (numoutb ≥ 2)
& (charb = inter) & (numouta ≥ 2) & (distab ≥ 1)
THEN yes.
IF (distab < 4) & (chara = inter) & (numoutb ≥ 2)
& (charb = out) THEN no.
IF (distab < 4) & (chara = out) THEN yes.
IF (distab ≥ 4) & (numinb < 2) THEN no.
IF (distab ≥ 4) & (numinb ≥ 2) & (deptha < 3)
THEN no.
IF (distab ≥ 4) & (numinb ≥ 2) & (deptha ≥ 3)
THEN yes.
```

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Step 1
Identify each  $r_{i}$ .
 $r_{1}$ : (distab &lt; 4) &amp; (chara = in) → no (unreachable)
 $r_{2}$ : (distab &lt; 4) &amp; (chara = inter) &amp; (numoutb &lt; 2)
→ yes (reachable)
</div>

```txt
r₃: (distab < 4) & (chara = inter) & (numoutb ≥ 2)
& (charb = inter) & (numouta < 2) → no (unreachable)
r₄: (distab < 4) & (chara = inter) & (numoutb ≥ 2)
& (charb = inter) & (numouta ≥ 2) & (distab < 1)
→ no (unreachable)
r₅: (distab < 4) & (chara = inter) & (numoutb ≥ 2)
& (charb = inter) & (numouta ≥ 2) & (distab ≥ 1)
→ yes (reachable)
r₆: (distab < 4) & (chara = inter) & (numoutb ≥ 2)
& (charb = out) → no (unreachable)
r₇: (distab < 4) & (chara = out) → yes (reachable)
r₈: (distab ≥ 4) & (numinb < 2) → no (unreachable)
r₉: (distab ≥ 4) & (numinb ≥ 2) & (deptha < 3) → no (unreachable)
r₁₀: (distab ≥ 4) & (numinb ≥ 2) & (deptha ≥ 3)
→ yes (reachable)
```

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$M_{1} = (\text{distab} &lt; 4) \&amp; (\text{chara} = \text{in})$ $M_{2} = (\text{distab} &lt; 4) \&amp; (\text{chara} = \text{inter}) \&amp; (\text{numoutb} &lt; 2)$ $M_{3} = (\text{distab} &lt; 4) \&amp; (\text{chara} = \text{inter}) \&amp; (\text{numoutb} \geq 2) \&amp; (\text{charb} = \text{inter}) \&amp; (\text{numouta} &lt; 2)$ $M_{4} = (\text{distab} &lt; 4) \&amp; (\text{chara} = \text{inter}) \&amp; (\text{numoutb} \geq 2) \&amp; (\text{charb} = \text{inter}) \&amp; (\text{numouta} \geq 2) \&amp; (\text{distab} &lt; 1)$ $M_{5} = (\text{distab} &lt; 4) \&amp; (\text{chara} = \text{inter}) \&amp; (\text{numoutb} \geq 2) \&amp; (\text{charb} = \text{inter}) \&amp; (\text{numouta} \geq 2) \&amp; (\text{distab} \geq 1)$ $M_{6} = (\text{distab} &lt; 4) \&amp; (\text{chara} = \text{inter}) \&amp; (\text{numoutb} \geq 2) \&amp; (\text{charb} = \text{out})$ $M_{7} = (\text{distab} &lt; 4) \&amp; (\text{chara} = \text{out})$ $M_{8} = (\text{distab} \geq 4) \&amp; (\text{numinb} &lt; 2)$ $M_{9} = (\text{distab} \geq 4) \&amp; (\text{numinb} \geq 2) \&amp; (\text{deptha} &lt; 3)$ $M_{10} = (\text{distab} \geq 4) \&amp; (\text{numinb} \geq 2) \&amp; (\text{deptha} \geq 3)$
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
From the initial rules, rule 7 $\{\mathbf{r}_7 = (\mathrm{distab} &lt; 4)\&amp;$ (chara $=$ out)} is chosen as suspicious rule to be refined.
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$B = C_{7} \lor$  (false positive condition from above tree)
 $B = (\text{distab} &lt; 4) \&amp; (\text{chara} = \text{out}) \&amp; (\text{distab} \geq 2) \&amp; (\text{deptha} &lt; 3)$
</div>

Now, additional testing examples are generated. $P _ { 1 }$ has the same condition as $M _ { 7 }$ that were not used in previous training examples.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$p_{1}=\{p_{11}:75\text{ out in }200131, p_{12}:76\text{ out inter }201211\}$
</div>

## Step 2

Build P, sum of $p _ { i } .$

Now, we set $P = p _ { 1 }$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$P=\{p_{11}\colon\text{out in 2 0 0 1 3 1}, p_{12}\colon\text{out inter 2 0 1 2 1}$ 
1}
</div>

## Step 3

Select a set of k testing points from P.

Now, we select all elements in P as testing points from P.

## Step 4

Perform a series of simulation on these selected points, and generate k testing examples, S. The testing points get its class through simulation.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$p_{11}$ : out in 2 0 0 1 3 1 no  
$p_{12}$ : out inter 2 0 1 2 1 1 yes
</div>

## Step 5

Calculate the prediction error on S using R.

$$
p _ {1 1}
$$

This is a point inside the hyperspace defined by $M _ { 7 }$

The error rate is 50%.

## Step 6

As the error rate is higher than minimum allowable rate of 10%, do the following.

6.1: Select a set of possible additional training patterns, B, using the set of false positives $p _ { 1 1 }$

6.1.1: $p _ { 1 1 }$ are false positives that have different class. Now $\hat { N } _ { i } = \{ p _ { 1 1 } \}$

6.1.2: Using $E _ { i }$ and $N _ { i } ,$ generate a set of rules, $R _ { i }$ by inductive learning.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$E_{i} = 01,03,76,78,02,05,04,06$ $N_{i} = 74$ $E_{i}$ U $N_{i} = \{01,03,76,78,02,05,04,06,74\}$
</div>

```txt
01 out inter 2 0 1 1 1 4 yes
03 out inter 2 0 2 1 1 4 yes
76 out inter 2 0 1 2 1 1 yes
78 out in 2 0 0 2 1 1 yes
02 out in 2 0 0 2 2 4 yes
05 out in 2 0 0 1 3 4 yes
04 out inter 2 0 2 1 2 4 yes
06 out inter 2 0 1 2 3 4 yes
75 out in 2 0 0 1 3 1 no
```

By inductive learning using above examples, we get $R _ { i }$ :

```txt
IF (distab < 2) THEN yes.
IF (distab ≥ 2) & (deptha < 3) THEN no.
IF (distab ≥ 2) & (deptha ≥ 3) THEN yes.
```

As per this decision tree, if distab<sup>G</sup>2 and deptha <sup>-</sup>3, the class<sup>s</sup>‘unreachable’.

6.2: Select training examples with above condition.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$F = \{73, 74\}$ $F = \{73: \text{out inter } 202131, 74: \text{out inter } 2021$ $21\}$
</div>

6.3: Identify the class of each F by simulation.

```txt
A = {73: out inter 2 0 2 1 3 1 no, 74: out inter 2 0 2 1 2 1 no}
6.4: Refine R with E + A.
The new rule set is:
IF (deptha < 2) & (numinb < 2) THEN no.
IF (deptha < 2) & (numinb ≥ 2) & (distab < 3) & (chara = in) THEN no.
IF (deptha < 2) & (numinb ≥ 2) & (distab < 3) & (chara = inter,out) THEN yes.
IF (deptha < 2) & (numinb ≥ 2) & (distab ≥ 3) THEN no.
IF (deptha ≥ 2) & (charb = in) THEN yes.
```

IF deptha Ž . Ž . Ž . <sup>G</sup> 2 & charb <sup>s</sup> inter & distab <sup>-</sup> 1 THEN no.

IF depthaŽ . Ž . Ž . <sup>G</sup> 2 & charb <sup>s</sup> inter & distab <sup>G</sup> 1 THEN yes.

IF depthaŽ . Ž . <sup>G</sup>2 & charb<sup>s</sup>out THEN no.

6.5: Refinement process is stopped as the minimum error rate of 10% is reached.

## References

<sup>w</sup> <sup>x</sup> 1 R. Agrawal, H. Mannila, R. Srikant, H. Toivonen, I. Verkamo, Fast discovery of association rules, in: U. Fayyad, G. Piatetsky-Shapiro, P. Smyth Eds. , Advances in Knowl-Ž . edge Discovery and Data Mining, MIT Press, Cambridge, MA, 1996, pp. 229–248.

<sup>w</sup> <sup>x</sup> 2 A. Amir, R. Feldman, R. Kashi, A new and versatile method for association generation, Information Systems 22 6–7Ž . Ž . 1997 333–347.

<sup>w</sup> <sup>x</sup> 3 C. Apte, S. Weiss, Data mining with decision trees and decision rules, Future Generation Computer Systems 13 2–3Ž . Ž .1997 197–210.

<sup>w</sup> <sup>x</sup> 4 D. Berndt, J. Clifford, Finding patterns in time series: a dynamic programming approach, in: U. Fayyad, G. Piatetsky-Shapiro, P. Smyth Eds. , Advances in Knowledge Dis-Ž . covery and Data Mining, MIT Press, Cambridge, MA, 1996, pp. 229–248.

<sup>w</sup> <sup>x</sup> 5 C. Bettini, Time-dependent concepts representation and reasoning using temporal description logics, Data and Knowledge Engineering 22 1 1997 1–38.Ž . Ž .

<sup>w</sup> <sup>x</sup>6 J.G. Carbonell, R.S. Michalski, T.M. Mitchell, An overview of machine learning, in: R.S. Michalski Ed. , Machine Ž . Learning: An Artificial Intelligence Approach, vol. 1, Tioga, Palo Alto, 1983, pp. 3–23.

<sup>w</sup> <sup>x</sup> 7 D.W. Cheung, V.T. Ng, A.W. Fu, Y.J. Fu et al., Efficient mining of association rules in distributed databases, IEEE Transactions on Knowledge and Data Engineering 8 6Ž . Ž .1996 911–922.

<sup>w</sup> <sup>x</sup> 8 L.G. Cooper, G. Giuffrida, Turning datamining into a management science tool: new algorithms and empirical results, Management Science 46 2 2000 249–264. Ž . Ž .

<sup>w</sup> <sup>x</sup> 9 M.W. Craven, J.W. Shavlik, Using neural networks for data mining, Future Generation Computer Systems 13 2–3Ž . Ž . 1997 211–229.

<sup>w</sup> <sup>x</sup> 10 G.F. DeJong, An approach to learning from observation, in: R.S. Michalski Ed. , Machine Learning: An Artificial Intel-Ž . ligence Approach, vol. 2, Morgan Kaufman, Los Altos, 1986, pp. 571–590.

<sup>w</sup> <sup>x</sup> 11 G.F. DeJong, R.J. Mooney, Explanation based learning: an alternative view, Machine Learning 1 1 1986 145–176.Ž . Ž .

<sup>w</sup> <sup>x</sup> 12 D.H. Fisher, Knowledge acquisition via incremental conceptual clustering, Machine Learning 2 2 1987 139–172.Ž . Ž .

<sup>w</sup> <sup>x</sup> 13 W.J. Frawley, G. Piatetsky-Shapiro, C.J. Matheus, Knowledge Discovery in Databases: An Overview, in: U. Fayyad,

G. Piatetsky-Shapiro, P. Smyth Eds. , Knowledge DiscoveryŽ . in Databases, AAAI<sup>r</sup>MIT Press, Cambridge, MA, 1991, pp. 1–27.

<sup>w</sup> <sup>x</sup> 14 K. Fukunaga, Statistical Pattern Recognition, Academic Press, New York, 1990.

<sup>w</sup> <sup>x</sup> 15 A. Ginsberg, S. Weiss, P. Politakis, A generalized approach to automate knowledge based refinement, Proceedings of 9th IJCAI, Los Angeles, California, vol. 2, 1985, pp. 18–23.

<sup>w</sup> <sup>x</sup> 16 P. Helman, J. Bhangoo, A statistically based system for prioritizing information exploration under uncertainty, IEEE Transactions on Systems Man and Cybernetics, Part-A: Systems and Humans 27 4 1997 449–466.Ž . Ž .

<sup>w</sup> <sup>x</sup> 17 J. Holland, Escaping brittleness: the possibility of general purpose learning algorithms applied to parallel rule-based systems, in: R.S. Michalski Ed. , Machine Learning: An Ž . Artificial Intelligence Approach, vol. 2, Morgan Kaufman, Los Altos, 1986, pp. 593–623.

<sup>w</sup> <sup>x</sup> 18 J.R.M. Hosking, E.P.D. Pednault, M. Sudan, A statistical perspective on data mining, Future Generation Computer Systems 13 2–3 1997 117–134.Ž . Ž .

<sup>w</sup> <sup>x</sup>19 G.H. John, R. Kohavi, K. Pfleger, Irrelevant features and the subset selection problem, Proceedings of the Eleventh International Conference on Machine Learning, 1994, pp. 121– 129.

<sup>w</sup> <sup>x</sup> 20 G.H. John, P. Miller, R. Kerber, Stock Selection using Rule Induction, IEEE Expert 1996 52–58, October.Ž .

<sup>w</sup> <sup>x</sup> 21 D.A. Keim, H.P. Kriegel, Visualization techniques for mining large databases: a comparison, IEEE Transactions on Knowledge and Data Engineering 8 6 1996 923–938.Ž . Ž .

<sup>w</sup> <sup>x</sup> 22 S.H. Kim, H.J. Noh, Predictability of interest rates using data mining tools: a comparative analysis of Korea and the US, Expert Systems with Application 13 2 1997 85–95.Ž . Ž .

<sup>w</sup> <sup>x</sup> 23 P. Langley, Selection of relevant features in machine learning, Proceedings of the AAAI Fall Symposium on Relevance, 1994, pp. 1–5.

<sup>w</sup> <sup>x</sup> 24 H.-Y. Lee, H.-L. Ong, Visualization support for data mining, IEEE Expert 1996 69–75, October.Ž .

<sup>w</sup> <sup>x</sup> 25 T.M. Mitchell, R.M. Keller, S.T. Kedar-Cabelli, Explanation based learning: a unifying view, Machine Learning 1 1Ž . Ž .1986 47–80.

<sup>w</sup> <sup>x</sup> 26 S. Muggleton, C. Feng, Efficient induction of logic programs, in: S. Muggleton Ed. , Inductive Logic Program-Ž . ming, Academic Press, San Diego, CA, 1992, pp. 281–298.

<sup>w</sup> <sup>x</sup> 27 S. Piramuthu, H. Ragavan, M.J. Shaw, Feature construction to improve the performance of neural networks, Management Science 44 3 1998 416–430.Ž . Ž .

<sup>w</sup> <sup>x</sup>28 G.D. Plotkin, A note on inductive generalization, in: B. Meltzer, D. Mitchie Eds. , Machine Intelligence, vol. 5,Ž . North-Holland, Amsterdam, 1970, pp. 153–163.

<sup>w</sup> <sup>x</sup>29 G.D. Plotkin, A further note on inductive generalization, in: B. Meltzer, D. Michie Eds. , Machine Intelligence, vol. 6,Ž . North-Holland, Amsterdam, 1971, pp. 101–124.

<sup>w</sup> <sup>x</sup> 30 P. Politakis, S. Weiss, Using empirical analysis to refine system knowledge bases, Artificial Intelligence 22 1984 Ž . 23–48.

<sup>w</sup> <sup>x</sup> 31 J.R. Quinlan, Induction of Decision Trees, Machine Learning 1 1986 81–106.Ž .

<sup>w</sup> <sup>x</sup> 32 J.R. Quinlan, Decision trees and multi-valued attributes, Machine Learning 11 1988 305–318.Ž .

<sup>w</sup> <sup>x</sup> 33 J.R. Quinlan, Learning logical definitions from relations, Machine Learning 5 1990 239–266.Ž .

<sup>w</sup> <sup>x</sup> 34 J.R. Quinlan, C4.5 Programming for Machine Learning, Morgan Kaufmann, Los Altos, 1993, pp. 17–26.

<sup>w</sup> <sup>x</sup> 35 B. Robertson, Biz Viz, Computer Graphics World 1991Ž . 45–50, September.

<sup>w</sup> <sup>x</sup> 36 J.W. Shavlik, G.G. Towell, An approach to combining explanation-based and neural learning algorithms, Connection Science 1 1989 233–255.Ž .

<sup>w</sup> <sup>x</sup> 37 R. Srikant, R. Agrawal, Mining generalized association rules, Future Generation Computer Systems 13 2–3 1997 161–Ž . Ž . 180.

<sup>w</sup> <sup>x</sup>38 M. Stone, Cross-validatory choice and assessment of statistical prediction, Journal of Royal Statistical Society 36 1974Ž . 111–147.

Sang Chan Park is an associate professor in Industrial Engineering at Korea Advanced Institute of Science and Technology KAIST .Ž . His current research interests include BtoB EC, TQM, educational technology and engineering, BPR, SCM, CRM, SEM, APS, ERP, PDM, and MES. He has published several related articles in IEEE Transactions, DSS, EJOR, Annals of OR, and Expert Systems with Applications.

Selwyn Piramuthu is currently a visiting associate professor at the Operations and Information Management department of the University of Pennsylvania. His interests are in machine learning and its applications in finance and manufacturing.

Michael J. Shaw is a Professor of Information Systems in the Department of Business Administration at the University of Illinois, Urbana-Champaign. He is also Director of the Center for Information Systems and Technology Management as well as on the research faculty of Beckman Institute for Advanced Science and Technology. His major research interests are related to electronic commerce and information technology for supply-chain management.

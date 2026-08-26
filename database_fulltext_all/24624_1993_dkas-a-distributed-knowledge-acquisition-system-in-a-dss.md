---
otero_id: 24624
otero_key: "XVTYHA45"
title: "DKAS: A Distributed Knowledge Acquisition System in a DSS"
authors: "Melody Yihwa Kiang; Robert T. Chi; Kar Yan Tam"
year: "1993"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1993.11517978"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# DKAS: A Distributed Knowledge Acquisition System in a DSS

Melody Yihwa Kiang, Robert T. Chi & Kar Yan Tam

To cite this article: Melody Yihwa Kiang, Robert T. Chi & Kar Yan Tam (1993) DKAS: A Distributed Knowledge Acquisition System in a DSS, Journal of Management Information Systems, 9:4, 59-82, DOI: 10.1080/07421222.1993.11517978

To link to this article: http://dx.doi.org/10.1080/07421222.1993.11517978

![](/api/attachments/XVTYHA45/fulltext/images/5611c028af32da802a621d6057ccf43a57c32ba9637d245b6838ade15d1710ff.jpg)

Published online: 16 Dec 2015.

![](/api/attachments/XVTYHA45/fulltext/images/3efcad477be6f4c0c4ae451e7fad12e47dc9e87c1b5fc94bdde2d6b708ada67a.jpg)

Submit your article to this journal ↗

![](/api/attachments/XVTYHA45/fulltext/images/3877a08766b2280a10f465275e682f6684bc76abf4c3b845b03f2ca40f31262e.jpg)

View related articles ↗

# DKAS: A Distributed Knowledge Acquisition System in a DSS

MELODY YIHWA KIANG, ROBERT T. CHI, AND KAR YAN TAM

MELODY YIHWA KIANG is an Assistant Professor of Decision and Information Systems at Arizona State University. She received her M.S. from the University of Wisconsin, Madsion, and her Ph.D. in management science and information systems from the University of Texas, Austin. Her research emphasizes the development and applications of artificial intelligence techniques to a variety of management problems. Dr. Kiang has published papers in Management Science, The Journal of the Operational Research Society, Applications in Management Science, Journal of Computer Science in Economics and Management, and other journals. She is currently an associate editor of Decision Support Systems and is one of the guest editors of a special issue of that journal on qualitative reasoning in business, finance, and economics. She is a member of TIMS and IEEE.

ROBERT T. CHI is an Assistant Professor of Information Systems at California State University at Long Beach. He received his M.S. from the University of Wisconsin, Madison, and his Ph.D. in management science and information systems from the University of Texas, Austin. His research interests include artificial intelligence (AI) application in management and finance, distributed AI, decision support systems, and executive information systems. Dr. Chi has published in Journal of Expert Systems with Applications, The Journal of the Operational Research Society, Annuals of OperationalResearch, International Journal of Intelligent Systems, Journal of Knowledge Based Systems, and other professional journals. He is a member of TIMS and DSI.

KAR YAN TAM received a B.S. in mathematics and computer science from the University of Illinois, Urbana, an M.S. in computer science and a Ph.D. in management information systems from Purdue University. He is currently a faculty member and a Weilun Fellow at the Hong Kong University of Science and Technology. Before joining HKUST he was Assistant Professor of Information Systems at the University of Texas, Austin. He has also held a Research Scientist position at Electronic Data Systems (EDS) where he conducted research in software engineering methodologies and tools. His research interests include AI applications in finance and manufacturing, decision support systems, and information systems development. He has published in Management Science, Information Systems Research, Decision Support Systems, Information and Management, European Journal of Operational Research, The Journal of the Operational Research Society, International Journal of Production Research, Journal of Manufacturing Systems, Omega, Financial Management, and other professional journals. Dr. Tam has served on the program committees of many professional conferences and workshops. He is currently on the editorial board of

Acknowledgment: This research was supported in part by a grant from the Small Grants Program at Arizona State University, College of Business. The opinions are those of the authors.

Decision Support Systems and is the guest editor of a special issue of that journal on neural networks. He is a member of TIMS and IEEE.

ABSTRACT: Knowledge acquisition is the process of accumulating new information and relating it to what is already known. Knowledge acquisition has been regarded as the bottleneck in knowledge-based systems development. In this paper, a distributed knowledge acquisition system (DKAS) is introduced for automating decision rules construction from a set of examples in a decision support system. DKAS has the potential to include various learning mechanisms and employs a multi-agent and parallel processing paradigm. The implementation of a DKAS integrates inductive and deductive learning methods that use different learning strategies. A stock selection problem is used to demonstrate the effectiveness of DKAS in solving classification type problems. The performance of the DKAS in portfolio management is compared to the performance of the NYSE and the S&P 500. The results indicate that the rules derived from using the DKAS outperform both the NYSE and the S&P 500.

KEY WORDS AND PHRASES: decision support systems, deductive learning, distributed knowledge acquisition system, inductive learning, portfolio management.

## 1. Introduction

MOST KNOWLEDGE-BASED SYSTEMS DISCUSSED IN THE LITERATURE employ static decision knowledge provided by domain experts. The process of knowledge acquisition, however, can be lengthy and is generally regarded as the bottleneck in knowledge-based systems development [4]. Attempts have been made to alleviate the bottleneck problem by employing learning processes that include the acquisition of new declarative knowledge [2, 38], the development of problem-solving skills through instruction or practice [29], and the discovery of new facts and theories through observation and experimentation [40]. For example, CONIS [38] is one system that employs an inductive learning method to acquire knowledge from examples in the domains of congressional voting records and the Pacific Basin economy. Shaw and Gentry [31] used three inductive learning methods to generate decision rules in decision support systems (DSS): the AQ-Star method, the Tree-induction method, and the probabilistic learning method.

Previous research has demonstrated the applicability of inductive learning in some selected domains, yet it has been criticized for the following reasons:

1. A large number of training examples are required;

2. The current inductive learning methods cannot incorporate existing domain knowledge into the learning process;

3. The generated rules may be biased due to the lack of representative training examples.

Further, previous learning systems employ only single learning mechanisms that are less effective and restricted in a narrowly defined problem domain. Simon [35] proposed the limitation of human problem solvers as “The capacity of the human mind for formulating and solving complex problems is very small compared with the size of the problems whose solution is required for objectively rational behavior in the real world—or even for a reasonable approximation to such objective rationality." The limitation of a human mind's processing capacity is called bounded rationality. "Bounded rationality implies that both the information a person can absorb and the detail of control he may wield is limited. As tasks grow larger and more complex, means must be found to effectively limit the increase of information a person sees and the complexity of control" [6].

Machine learning systems have extended the “rationality” of single human learners, but still have limited learning capacities. The learning mechanism can process only a limited number of instructions within a given time period. In other words, in order to maintain the efficiency of information processing, the problem domain of learning is usually restricted to a narrowly defined area. Hence, previous machine learning systems exhibit symptoms similar to the bounded rationality exhibited by human learners when processing capacities are exceeded.

DKAS is an intelligent learning system built upon a multi-agent and distributed problem processing environment and has the capability to perform learning in complex problem domains. Since DKAS employs a distributed architecture, more learning agents can be included in the system. As a result, the defects of individual learning systems can be compensated by each other. For example, the integration of inductive learning agents and deductive learning agents has the advantages of requiring fewer training examples and making use of existing domain theories. In this research, a portfolio management problem is used and the results suggest that DKAS can effectively identify high performance stocks based on companies' financial reports.

The rest of this paper is organized as follows. In section 2, a review of the current research on learning strategies and distributed artificial intelligence (DAI) is presented. This is followed by a detailed discussion of the framework of the distributed knowledge acquisition system. In section 4, the stock selection example is presented and the result is compared with market indexes. The paper concludes with some observations concerning the limitations of DKAS and the direction for future research.

## 2. Current Research on Machine Learning and Distributed Artificial Intelligence (DAI)

THERE ARE SIX STRATEGIES TO MECHANIZE THE PROCESS of learning from the machine learning perspective. They are (1) rote learning [29], (2) similarity-based learning (SBL) or learning by examples [17, 18, 25, 40], (3) learning by observation [5], (4) learning by analogy [15], (5) explanation-based learning (EBL) [4, 20], and (6) environmental learning [34]. Among these different learning strategies, similarity-based learning and explanation-based learning are two strategies that have attracted considerable interest in recent years. SBL is an inductive learning mechanism that learns rules by synthesizing the common features among a large set of training examples on a syntactic basis. In contrast, EBL employs a deductive learning mechanism that uses an existing domain theory consisting of production rules to explain and generalize a single training example. In general, there are two categories of learning systems: inductive learning systems and deductive learning systems. Both are discussed in the following subsections.

## 2.1. The Inductive Learning Approach

The inductive learning approach is a branch of machine learning research dealing with the acquisition of concept descriptions from examples. A similarity-based learning method, the most popular inductive learning algorithm, is the process of inferring the general description of a class from the description of individual objects of the class by examining the similarities and differences among a large number of examples. The basic idea is that the learning system takes a number of instances that include positive and negative instances, and compares them to create a generalized concept description capable of describing all positive examples and excluding all negative ones. Such learning systems have been widely used to acquire knowledge for systems that perform classification tasks $[15, 16]$ .

The actual process of the inductive learning system is as follows: In order to get a correct concept description in accordance with the examples, a hypothesis concept description is first chosen to cover positive examples and to exclude negative examples. As the process continues, new examples are fed in and the learner keeps updating the hypothesis to make it consistent with new examples, until all training examples are consistent with the learned concept description. However, since there may be no concept description that can satisfy all positive examples and reject all negatives, the concept that satisfies a given portion of examples may be accepted, depending on the learning strategy.

Although ID3 [25], a similarity-based learning method, has been applied successfully to classification problems such as disease diagnosis in plants [17], the primary problem with inductive learning methods is that they need a large amount of examples to generate a concept description. This approach also fails to make use of the existing knowledge of the problem domain as part of the classification criteria.

## 2.2. The Deductive Learning Approach

In the last few years another approach has become popular in the machine learning field—explanation-based learning (EBL) $[4, 23]$ , a deductive learning method. This learning approach involves intensive application of existing knowledge to explain and generalize a single example and thereby acquire operational concept descriptions and problem-solving knowledge $[3, 19, 26]$ . An EBL program takes a positive instance as the training example, explains this example using the existing knowledge base called the domain theory, and produces a generalized concept description as the final output. The basic premise of explanation-based learning is that it is possible to form a justified generalization of a positive training example provided the learning system is endowed with some explanatory capabilities. However, the disadvantage of EBL is that the building and analysis of explanations requires extremely detailed knowledge of the problem domain. Applications of explanation-based learning can be found in the VLSI circuit design [21], the satellite control system [23], and the stories understanding mechanisms [3].

In contrast to the SBL approach, the EBL method uses existing domain knowledge to explain why an instance is a member of a concept. In this approach, only a positive training example is needed and a domain theory, which consists of a set of production rules, is used to explain these examples. The explained example then will be generalized as the learned concept description. The main problem of this approach is that it is incompetent to deal with inexplicable features of the problem domain.

## 2.3. The Integration of Inductive and Deductive Learning Methods

Although both SBL and EBL systems are quite successful in dealing with different tasks, each learning approach has its own advantages and disadvantages in terms of efficiency and effectiveness. The inductive learning method requires a large number of examples and cannot use the advantage of the existing knowledge of the problem, while the deductive learning method requires a complete theory of the domain. The concept of the integrated learning system was originally proposed by Michalski and Stepp [18]. The idea was first to provide the inductive learner with some knowledge about the relative importance of the features used in the representation of instances. Such a learner would then be able to focus its generalization process solely on those features identified as important. In recent years, there have been several research projects dedicated to integrating inductive and deductive learning methods [12, 24]. They all attempt to use the explanation mechanism to separate the causally relevant features from those that are purely coincidental, and to use the inductive learning to focus on the unexplained aspects of the problem.

A psychological experiment by Ahn and Brewer [1] suggests that human learners employ both inductive and deductive methods and that the successful use of these procedures is determined by the characteristics of the information to be learned. It also suggests that in a problem domain without known causal structure, multiple examples are more likely to lead to a successful inductive mechanism. While there is some existing knowledge about the underlying causal structure of the problem domain, the use of appropriate background knowledge can usually lead to a successful deductive learning system. The above argument suggests that people use different learning mechanisms to acquire different aspects of the learned concept, which concurs with the concept of the integrated learning system.

The problem now is how to integrate different learning methods to work cooperatively to achieve the same goal. The research developed in the distributed artificial intelligence area has suggested ways effectively to integrate multiple problem-solving agents. We believe that those mechanisms can be applied to integrate multiple learning methods in a similar fashion.

## 2.4. Distributed Artificial Intelligence (DAI)

Previous DAI studies classified distributed problem solving into two forms: (1) task sharing and (2) result sharing [36]. In task-sharing systems, problem-solving agents assist each other by sharing the computational load for the execution of subtasks of the overall problem. In result-sharing systems, agents assist each other by sharing partial results that are based on somewhat different perspectives on the overall problem. Each form is discussed in the following sections.

## 2.4.1. Task-sharing Systems

In task-sharing systems the overall problem to be solved is decomposed into several smaller subproblems (see figure 1). Cooperation is achieved by sharing the computational load of the overall problem. Each subproblem is assigned to a particular agent that will asynchronously perform its own functions and submit a solution synchronously with other agents. The contract-net protocol developed by Smith [37] proposed a framework that is designed to allow agents to submit bids. Any agent that receives a task announcement message can reply with a bid, indicating how well the task will be accomplished. The agent (usually the coordinator) that announced the task collects these bids and awards the task to the bidder with the highest bid. Other task-sharing system examples are the office information system proposed by Woo and Lachovsky [41], the scheduling system by Shaw and Whinston [33], the object-oriented multiple agent planning system by Kamel and Syed [11], and the system developed by Lesser and Corkill [13].

Generally speaking, task-sharing methods are most useful for problem domains where it is appropriate to define a hierarchy of tasks or levels of data abstraction [36]. Such problems can usually be decomposed into a set of independent subproblems.

## 2.4.2. Result-sharing Systems

Result sharing is a form of cooperation in which individual problem-solving agents assist each other by sharing partial results, based on somewhat different perspectives of the overall problem $[36]$ . In this type of system, control is typically “data-oriented.” At any instant, the computation done by a certain agent is used to satisfy an unknown variable that is needed for the computation of another subtask (see figure 2). Therefore, an explicit hierarchy of task–subtask relationships does not exist between individual agents. Typically, one of the agents acts as the group planner (or the coordinator), and each of the other agents sends all pertinent information to this agent in order to form a global plan for problem solving. The main issue of these systems is how to guide and coordinate the interactions among the participating agents so that the problem can be solved jointly by the group.

In general, result-sharing DAI systems are most useful in problem domains in which (1) results achieved by one node influence or constrain those that can be achieved by another node (i.e., the results are relevant to each other), (2) sharing of results drives the system to converge to a solution of the problem (i.e., results received from remote nodes do not cause oscillation), and (3) sharing of results drives the system to a correct solution of the problem [36].

Depending on the nature of the problem domain, different types of problems can be best approached by different learning strategies. In this research, we propose a framework of DKAS based on the task-sharing approach. A detailed description of the framework is presented in the following section.

![](/api/attachments/XVTYHA45/fulltext/images/e24a4b28d874e50519c575fe87d196abcb02f6e39e8c34f7190cb3f8ebdc2d15.jpg)  
Figure 1. Framework Task-Sharing Systems

![](/api/attachments/XVTYHA45/fulltext/images/f5f74c95b3ee979468e6969e1d9f1a6922d11d8aecc0fe9d43172be4c926924e.jpg)  
Figure 2. Framework of Result-Sharing Systems

## 3. The Framework of a Distributed Knowledge Acquisition System

DISTRIBUTED KNOWLEDGE ACQUISITION IS CONCERNED with cooperative knowledge acquisition by a decentralized group of agents. The agents in a distributed knowledge acquisition environment may range from simple processing elements to complex entities exhibiting rational behavior. Moreover, the knowledge acquisition is cooperative in that mutual sharing of information is necessary to allow the group as a whole to produce a final solution. Finally, the group of agents is decentralized in that both control and data are logically and often geographically distributed. Distributed knowledge acquisition is also characterized by the following unique properties [8]: (1) Modularity—the complexity of a learning system increases rapidly as the size of its knowledge increases. Partitioning the system into N subsystems reduces the complexity by significantly more than a factor of N. The resultant system is easier to develop, test, and maintain. (2) Speed—the subsystems can operate in parallel. (3) Reliability—the system can continue to operate even if part of it fails. (4) Simplicity—it is easier to find expertise in narrow domains. (5) Reusability—a small, independent learning system could be a part of many distributed learning systems and its expertise would not have to be re-implemented for each.

In DKAS, a multi-agent, distributed processing setting is employed. Since the action of one agent usually affects some other agents, the coordination among agents in a system becomes most important. The objective of coordination is to regulate the interactions among agents and to control the sequence of these interactions [32]. A DKAS contains a learning coordinator, a meta knowledge base, and a set of learning agents (see figure 3).

![](/api/attachments/XVTYHA45/fulltext/images/9b9b590736dcbbb9908287282c5534aaadbfada3bb708bde54c49b1d04cc3758.jpg)  
Figure 3. The Distributed Knowledge Acquisition Process

(1) The learning coordinator is the key component for distributed learning. It provides a global view of the problem-solving status to other agents. Having a local view and incomplete information, individual agents must coordinate with other agents with the help of the coordinator to achieve globally coherent and efficient solutions. The learning coordinator communicates directly or indirectly with other learning agents through communication channels.

(2) The meta knowledge base contains the learning coordination strategies of DKAS. Those strategies, including task decomposition, task assignment, and coordination approaches, are maintained by domain experts. This allows each agent the chance to review the strategy when conflict occurs. It also allows the coordinator to modify the strategies if the environment has changed. Meta knowledge can only be modified by the learning coordinator, but can be retrieved by all agents.

(3) The learning agents in a DKAS can be heterogeneous and work in parallel. Although different learning agents may utilize different learning methods, all of them take input from the outside environment and generate knowledge (rules) to support the knowledge system. In the prototype system we implemented, two learning agents, ID3 (an inductive learning agent) and EBL (a deductive learning agent), are included.

## 3.1. The Distributed Learning Process

A DKAS employs a task-sharing mechanism (see figure 4) that allows the learning coordinator to decompose the task into subtasks and assign subtasks to different learning agents based on their qualifications. Generally speaking, the coordination process performed by the learning coordinator consists of four steps (see figure 3):

(1) Task decomposition involves dividing a major task into subtasks based on the rules stored in the meta knowledge base. The attributes of each instance are separated into subsets and each subset is customized to fit each learning agent's expertise. For example, attributes of instances can be divided into inductive attributes and deductive attributes, and each set can be further divided into a manageable size for individual learning agents. The domain theory stores the knowledge acquired from human experts to provide the basis for performing deductive learning.

To simplify our discussion, we assume that the attributes for different learning agents are mutually exclusive. This will avoid the problem of deriving conflicting results from different learning agents. All the attributes that have appeared in the acquired expert knowledge are considered deductive attributes while the others (appearing in the attributes that describe the instances but not in the acquired expert knowledge) are classified as inductive attributes. An index built to distinguish between them is stored in the meta knowledge base. Consider the following domain theory that consists of two rules in the domain theory of deductive learning agents:

$$
\begin{array}{c} {A \& B \to C} \\ {C \& X \to Z} \end{array}
$$

A, B, C, and X are the premises of rules, while C and Z are the conclusions. Since premises have potential to be used to deduce target concept, the premise set $\beta = [A, B, C, X]$ can be used as the meta knowledge to screen out inductive attributes from deductive attributes. Based on this meta knowledge, the learning coordinator can divide and send a subset of each instance containing the attributes in the premise set to the deductive learning agent, and the other attributes of the same instances to the inductive learning agent. Based on the above information, an input data set containing eight attributes, $\{A, B, D, E, F, G, H, X\}$ , will be divided into two subsets: one contains only deductive attributes, $\partial=\{A,B,X\}$ ; the other contains only inductive attributes, $\Omega=\{D,E,F,G,H\}$ . If the meta knowledge also suggests that no more than three attributes can be assigned to each agent for processing efficiency, then $\Omega$ will be further divided into two subgroups (i.e., $\Omega_{1}$ and $\Omega_{2}$ ). The rules in the meta knowledge base are sequentially applied by the learning coordinator to decompose tasks. Since the example is relatively simple, only two steps have been performed to decompose the task. Figure 5 shows the process of task decomposition in DKAS.

![](/api/attachments/XVTYHA45/fulltext/images/8bfa4d6cd31f0425814350806db738e04cf3364e554513787a01cc16d7020651.jpg)  
Figure 4. The Framework of a Distributed Knowledge Acquisition System

(2) Task assignment's function is to allocate subproblems to appropriate agents for further processing. The appropriate agent is selected by the coordinator based on meta knowledge. Usually, subtasks are assigned based on the availability and the capability of learning agents. For example, we should always allocate deductive learning tasks to deductive agents and inductive learning tasks to inductive agents.

(3) The parallel learning process consists of the following: after a subtask is assigned to a certain learning agent, the learning agent will then perform learning based on the data supported. Since learning agents are organized in a distributed fashion, parallel problem solving becomes possible. This means each learning agent can perform its own assigned subtask concurrently without interfering with other learning agents.

(4) Knowledge integration combines learning results from all learning agents to form a final output that can be used as the knowledge base for a decision support system. In this paper, the deduced concept and induced concept are integrated using “and” operand.

![](/api/attachments/XVTYHA45/fulltext/images/c42d3d279b25436219619e6b0b5631f1763b92a2be26e4341a6b31d9bbd2f7c4.jpg)  
Figure 5. The Process of Task Decomposition

To illustrate the potential of using a distributed learning system in business, we implemented a prototype of DKAS by including only two learning agents (deductive and inductive learning agents) in the system.

## 4. Implementation and Evaluation

STOCK PERFORMANCE PREDICTION HAS LONG BEEN A POPULAR RESEARCH TOPIC in accounting, finance, and other business-related fields. In stock market analysis, there are two distinct schools of thought: fundamental analysis [28] and technical analysis [14]. Fundamental analysis is based on the premise that any security has an intrinsic value at any given time. This value is a function of underlying economic values. Fundamental analysts analyze sales data, managerial ability, and the competition by examining various financial reports of the company to estimate its future business conditions. They evaluate stocks by considering all available information; if a stock is currently priced below an analyst's appraisal, it is regarded as a good buy. Technical analysts, however, study the behavior of the market itself. It is referred to as the science of recording, usually in graphic form, the actual history of trading (price changes, volume of transactions, etc.). In this research, we focus mainly on fundamental analysis that attempts to spot those “undervalued” stocks.

Previous research in fundamental analysis mainly focused on using statistical methods to relate the performance of a stock with some measurable parameters such as financial ratios, and to suggest signals to buy or sell as the values of these parameters changed $[27]$ . Due to the complex nature of this problem, only limited success has been achieved by previous research. A major problem is the scarcity of human expertise $[7]$ . It is difficult to elicit trading rules from experts who are experienced portfolio managers and security analysts for two reasons. First, knowledge of this kind is a valuable asset to these professionals. To protect themselves, obviously, these professionals are not willing to disclose their expertise. Second, even if a human expert were willing to do so, he or she might find it difficult to articulate his or her knowledge in unambiguous terms so that a knowledge engineer can properly encode it in some knowledge representation form. The unwillingness toward knowledge disclosure, coupled with the inability to articulate that knowledge, poses a major problem to expert systems development in this area. Indeed, this problem is not exclusive to portfolio management but is typically found in other application domains. DKAS is especially designed for the problem of limited expert knowledge, which can be explained and utilized by the deductive learning agent, and for a large volume of historical data that can be analyzed by the inductive learning agent. The goal concept description to be learned from the DKAS approach is to identify stocks with high growth potential, which are hereafter referred to as “good stocks.” The result of the process is to have the knowledge base of DKAS contain rules learned from both deductive and inductive learning agents to screen qualified stocks.

## 4.1. Experimental Design and Procedures

To demonstrate the effectiveness of the DKAS method in stock performance prediction, we acquired trading rules, constructed portfolios based on the rules, and compared their performances with some market indexes. The objective of the portfolio is to invest in stocks with high-growth potential. This criterion is operationalized by defining a high-growth stock as one that doubles in price within one year. We selected stocks that meet this criterion as positive examples; stocks that do not are negative examples. Our training sample consists of stocks traded in the NYSE over the period 1980 through 1984. In total, three criteria were used in selecting positive examples: (1) the stock's price has doubled in one year; (2) the fiscal year-end of the firm is December 31; and (3) the relevant investment returns and financial statements were available. Stocks that satisfied these criteria were retrieved from the COMPUSTAT database. As a result, a total of 98 positive examples of high-growth stocks were identified. For each positive example, a negative example was selected to pair with it, making an equal proportion of both classes of examples. Since the number of high-growth stocks constituted only a small portion of all the stocks quoted on the NYSE in any single year, the results may be biased by the negative examples chosen.

In order to reduce this possibility, five different sets of negative examples each containing 98 examples were randomly selected, resulting in five training samples. For each stock, financial ratios of the firm at year-end and the firm's stock price were collected from the COMPUSTAT and CRSP database. Statistics of one positive example set and five negative example sets are shown in Table 1.

The deductive learning agent in DKAS is responsible for learning the deductive concept from training examples. As described earlier in this paper, deductive concepts can be learned by referencing the existing knowledge of the problem under analysis. In other words, the source of the deductive learning process is mainly based on the knowledge acquired from domain experts. Previous research in stock analysis has proposed some general rules for screening stocks $[27]$ . In this research, the guidelines suggested by the previous research of O'Neil and Reinganum $[22, 27]$ were used as the basis of our domain theory for the deductive learning agent. To convert those guidelines into a format that can be understood by the deductive learning agent (e.g., EBL), some transformation processes are needed. Additional expert knowledge in stock analysis is required in order to accomplish the process. However, the detailed discussion of the transformation process is beyond the scope of this paper. The following shows the three rules derived from the domain experts:

Rule 1: shares\_outstanding(X,Y) & Y ≤ 40,000,000 → appreciation(X,yes)

Rule 2: relative\_strength(X, Y) & Y ≥ 15% → potential\_value(X, yes)

Rule 3: change\_in\_quarterly\_earnings(X,Y) & Y ≥ -1 → earning\_capability(X,yes)

Based on the above rules, we can describe a qualified stock as having good appreciation, good potential value, and good earning capability:

Rule 4: appreciation(X,yes) & potential\_value(X, yes) & earning\_capability(X,yes) → qualified\_stock(X)

Since the example used is relatively simple, the explanation-based learning process is performed manually. We hand-derived the following rule based on the above domain theory:

IF (shares outstanding ≥ 40,000,000

AND relative strength ≥ 0.15

AND change in quarterly earnings ≥ -1)

THEN good stock

Five other important features that do not have an existing rule per se were also identified and listed. In contrast to the deductive learning process, the source of the inductive learning process is based mainly on historical data. The tree induction procedure (e.g., ID3 [25]) is applied to acquire the inductive concept based on the values of these five features:

1. Current price ratio: The ratio of the current quarter's closing price to the highest price in the past two years.

Table 1 Statistics of Training Samples

<table><tr><td rowspan="2">Variable name</td><td colspan="2">Positive</td><td colspan="4">Negative</td></tr><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>Shares outstanding*</td><td>13.9(23.3)</td><td>31.4(69.5)</td><td>29.4(50.9)</td><td>44.5(89.5)</td><td>31.6(40.5)</td><td>28.6(51.7)</td></tr><tr><td>Price ratio</td><td>0.9(0.08)</td><td>0.8(0.1)</td><td>0.8(0.1)</td><td>0.8(0.2)</td><td>0.8(0.1)</td><td>0.8(0.1)</td></tr><tr><td>Return on equity</td><td>0.1(0.42)</td><td>0.2(0.1)</td><td>0.2(0.1)</td><td>0.2(0.1)</td><td>0.2(0.1)</td><td>0.2(0.1)</td></tr><tr><td>Net current asset ratio</td><td>-5.2(18.1)</td><td>-5.3(17.4)</td><td>-3.1(13.1)</td><td>-3.3(18.8)</td><td>-5.1(18.6)</td><td>-6.7(19.3)</td></tr><tr><td>Price-to-book ratio</td><td>1.7(3.4)</td><td>1.4(1.2)</td><td>1.6(1.1)</td><td>1.4(1.2)</td><td>1.5(0.9)</td><td>1.7(1.4)</td></tr><tr><td>Relative strength</td><td>0.3(0.2)</td><td>0.0(0.1)</td><td>0.0(0.1)</td><td>0.0(0.1)</td><td>0.0(0.1)</td><td>0.0(0.1)</td></tr><tr><td>Change in quarterly earnings</td><td>0.8(2.6)</td><td>0.7(4.6)</td><td>0.1(0.9)</td><td>0.3(1.9)</td><td>0.0(0.6)</td><td>0.1(0.6)</td></tr><tr><td>Market capitalization**</td><td>460.5(831.5)</td><td>1,060.6(2,605.2)</td><td>1,092.5(2,744.5)</td><td>2,063.2(5,899.9)</td><td>1,697.4(2,979.7)</td><td>1,207.2(3,046.0)</td></tr></table>

Standard deviations are enclosed in parentheses; \* measured in million shares; \*\* measured in million dollars.  
2. Return on equity: Net income divided by stock's equity.  
3. Net current asset value: Net current asset per common share outstanding.  
4. Price-to-book ratio: The ratio of the market value of equity to its book value.  
5. Market capitalization: Number of common shares outstanding multiplied by the stock's closing price at the end of current quarter.

## 4.2. Discussion of Results

The ID3 procedure was applied to each sample and the resulting tree structures were further combined with the result of EBL to generate five different stock prediction rules as shown in the appendix. Although the structures of the induction part of the rules are quite different among those five rules, in general they all agree that the current price ratio is the most significant feature in predicting stock return.

Five portfolios were constructed for each year using each of the five screening rules. All portfolios were constructed by screening the COMPUSTAT and CRSP databases for information reported at the closing quarter. Buy signals were generated if a firm satisfied the rule. A simple buy-and-hold strategy was used, with a fixed one-year holding period, and positions were taken on the last trading day of March each year.

Table 2 Comparison of Annual Returns in Each Holding Period

<table><tr><td rowspan="2">Holding period</td><td colspan="8">Annual returns (%)</td></tr><tr><td>NYSE Composite</td><td>S&amp;P 500</td><td>Rule 1</td><td>Rule 2</td><td>Rule 3</td><td>Rule 4</td><td>Rule 5</td><td>Average of rules</td></tr><tr><td>3/85–3/86</td><td>31.2</td><td>28.9</td><td>51.77</td><td>53.29</td><td>51.77</td><td>46.13</td><td>49.57</td><td>50.51</td></tr><tr><td>3/86–3/87</td><td>20.5</td><td>22.0</td><td>13.71</td><td>20.29</td><td>16.35</td><td>16.31</td><td>14.96</td><td>16.32</td></tr><tr><td>3/87–3/88</td><td>-8.5</td><td>-8.0</td><td>-4.37</td><td>1.78</td><td>0.97</td><td>-3.25</td><td>-5.64</td><td>-2.10</td></tr><tr><td>3/88–12/88</td><td>8.8</td><td>9.8</td><td>8.48</td><td>5.16</td><td>6.53</td><td>12.17</td><td>9.27</td><td>8.32</td></tr><tr><td>Total</td><td>52</td><td>52.7</td><td>69.59</td><td>80.52</td><td>75.62</td><td>71.36</td><td>68.16</td><td>73.05</td></tr></table>

\* Annual returns based on a nine-month period.

This ensures that information of the last quarter has already been published and the strategy has not capitalized on insider information. The monthly return of each portfolio was then computed for the twelve-month period, assuming an equal initial investment in each stock. We simulated the trading process for more than three years (March 1985 through December 1988), then compared the returns of each portfolio with the returns of the NYSE Composite Index and the S&P 500 index over the same period.

As shown in Table 2, the total annual returns of the five portfolios outperformed both the NYSE Composite index and the S&P 500 in each of the four holding periods. The average returns of the portfolios exceeded those of NYSE Composite and S&P 500 by 19.31 percent and 21.6 percent in the period March 1985 to March 1986, respectively, and 6.4 percent and 5.9 percent in the period March 1987 to March 1988, respectively.

A careful inspection of the results reveals that there is no particular rule that always outperformed the others in all four holding periods. For example, rule 2 yielded the highest return from March 1985 to March 1986 and March 1987 to March 1988 but degraded substantially from March 1988 to December 1988. On the contrary, rule 4 had the lowest return from March 1985 to March 1986 but yielded the highest return from March 1988 to December 1988. If the reasons for the change in performance are known, we can apply different trading strategies at different time periods and the total return of the portfolio can be improved further. Namely, if we employ rule 2 during the first three periods and change to rule 4 in period four, then the total annual return will be 87.53 percent, which is 35.53 percent higher than the NYSE Composite index and 34.83 percent higher than the S&P 500 index. Figure 6 depicts the change of market indexes from March 1985 to March 1988. To relate the performance of rules to the change in the market, we noticed that rule 2 yielded the highest return during a bull market (March 1985 to August 1987) but yielded the lowest return during a bear market (September 1987 to December 1988) (see figure 6) while rule 4 yielded relatively low returns (but still higher than the market return) during a bull market but performed better than others during a bear market.

One possible explanation for the difference is that rule 2 represents the trading strategy of aggressive investors looking for high capital growth stocks while rule 4 characterizes the trading strategy utilized by conservative investors that are more risk-alert and tend to invest in stable stocks. The higher returns earned by the investment strategy may reflect the compensation for bearing additional risk [27]. Consistent with the result of further analysis, rule 4 does have a relatively low risk factor compared with all other rules (see Table 3). Different investors can choose different investment strategies (rules) that are consistent with his or her goals and personal circumstances. Also, the same investor can employ different strategies based on the market situation. This observation gives some insight into the timing of different trading strategies (e.g., rules) and their sensitivity to market condition.

The above comparison is not complete since part of the return can be explained by the extra risk taken. A more rigorous way to evaluate the performance of a portfolio is to take both risk and return into consideration. In this study, three performance indexes are used: the Sharpe index [30], the Jensen index [9], and the Treynor index [39]. They are based on the return variance framework that allows a set of portfolios to be ranked and compared with a naive market standard. Since the indexes require a riskless benchmark in their calculation, the one-month T-bill is used as a proxy to a risk-free market. The risk-free rate of the one-month T-bill rate is converted to a monthly return $r_{f}$ by calculating $(r_{y}/12)\{(r_{y}/12)\}$ , where $r_{y}$ is the asked yield on one-month T-bills.

The Sharpe index $S_{p}$ is defined as the ratio of the risk premium per unit of variability. Jobson and Korkie [10] have shown that an unbiased estimator of the Sharpe index can be calculated as:

$$
S _ {p} = S \left[ \frac {N}{N + 0 . 7 5} \right],
$$

where S is the ratio of the mean excess return to standard deviation of return, and N is the number of return intervals.

The Treynor index is based on the market model in which returns of a portfolio are regressed on the returns of the market over some historical period. The variability of the portfolio with respect to the market is measured by the beta coefficient in the regression. Given a beta, $\beta_{p}$ , for a portfolio, the Treynor index $T_{p}$ is defined as:

$$
T _ {p} = S \frac {\overline {{{r}}} _ {p} - \overline {{{r}}} _ {f}}{\beta_ {p}},
$$

where the numerator is the mean excess return and the denominator is $\beta_{p}$ .

The Jensen index is based on the Capital Asset Pricing Model (CAPM) and also uses

Downloaded by [University of Pennsylvania] at 18:24 09 May 2016

NYSE and S&P 500 Indexes  
![](/api/attachments/XVTYHA45/fulltext/images/3104f87440a9e88c92cd42785b50312d6e5d7940a044542a76aa50fe60d54a11.jpg)  
Figure 6. The Change of Market Indexes from March 1985 to December 1988

Table 3 Performance Ranking Using Sharpe Index, March 1985 through December 1988

<table><tr><td>Trading rule(s)</td><td>(1) Average (%)</td><td>(2) Standard deviation (%)</td><td>(3) Sharpe&#x27;s index</td><td>(4) Rank</td></tr><tr><td>Rule 1</td><td>1.50</td><td>6.81</td><td>0.07</td><td>3</td></tr><tr><td>Rule 2</td><td>1.76</td><td>6.89</td><td>0.11</td><td>1</td></tr><tr><td>Rule 3</td><td>1.60</td><td>6.98</td><td>0.08</td><td>2</td></tr><tr><td>Rule 4</td><td>1.52</td><td>6.57</td><td>0.08</td><td>2</td></tr><tr><td>Rule 5</td><td>1.53</td><td>6.91</td><td>0.07</td><td>3</td></tr><tr><td>S&amp;P 500</td><td>1.12</td><td>5.53</td><td>0.02</td><td>4</td></tr><tr><td>NYSE Composite</td><td>1.11</td><td>6.53</td><td>0.02</td><td>4</td></tr><tr><td>30-day T-bill</td><td>1.01</td><td>0.34</td><td>0.00</td><td>5</td></tr></table>

\* The Sharpe index is estimated by $SN / (N + 0.75)$ where $S$ is calculated as the mean excess return divided by the standard deviation of return and $N$ is the number of observations.

the portfolio's beta to measure its risk. The index $J_{p}$ measures the differential between a portfolio's realized returns and that predicated by the CAPM ex post. The index can be estimated by the following regression equation:

$$
r _ {p t} - r _ {f t} = J _ {p} + (r _ {m t} - r _ {f t}) \beta_ {p} + e _ {p t},
$$

where $r_{ft}$ and $r_{mt}$ are the respective risk-free return and return on a market proxy in period t. The $e_{pt}$ 's have an average value of zero, and $J_{p}$ is the intercept of the regression line.

Although these single-parameter portfolio measures have been challenged on many different grounds, from having unrealistic assumptions to estimation problems, they nevertheless provide a robust yardstick for performance measurement, especially when the different indexes are cross-validated.

The average monthly return and the standard deviation of return for each portfolio during the period of March 1985 through December 1988 are shown in columns 1 and 2 of Table 3, with the Sharpe index used to initially rank the funds. The rank based on Sharpe's index shows that all five portfolios outperformed both the NYSE Composite index and the S&P 500 index, with rule 2 ranked first and the market indexes lowest on the list. Similar rankings can be obtained if only column 1 (e.g., the average) is considered. Both the S&P 500 and NYSE indexes have lower percentages in the risk factor (represented by the standard deviation), which is consistent with our expectation that the index is more diversified than any of the portfolios, therefore it should have a smaller standard deviation and generate lower returns as well. However, the excessive returns of our portfolios are more than enough to compensate the higher risk taken by their trading strategies, and the final ranking of the returns (after being justified by Sharpe's index) remains about the same.

The Sharpe index is appropriate for measuring the performance of a single portfolio, provided that it is the owner's only asset. On the other hand, the Treynor and Jensen indexes have been suggested for measuring the performance of a larger portfolio. That is, the portfolio under investigation is only a part of the investor's total assets. The Treynor and Jensen indexes of each portfolio are shown in Tables 4 and 5, respectively. Since both measurements are based on the CAPM, which requires a market proxy, two lists of rankings, one based on the NYSE composite index and the other on the S&P 500, are provided.

As shown in Tables 4 and 5, the same rankings are observed using both performance measures, regardless of the market proxy chosen. Although the rankings of the five portfolios using the Treynor and Jensen indexes deviated slightly from that of the Sharpe index, the general order was still maintained, which is that the portfolios outperformed the market when risk was taken into account. The results support the use of a DKAS in stock performance evaluation and show that the rules acquired by the DKAS yield higher returns than the general market indexes (which are watched closely by financial analysts).

## 5. Limitations and Future Research

IN THIS RESEARCH, A GENERAL FRAMEWORK OF THE DISTRIBUTED knowledge acquisition system is proposed to assist the knowledge acquisition process when building a decision support system. A prototype of a DKAS is implemented to learn rules of inductive and deductive features based on historical data and existing knowledge from domain experts, respectively. The portfolio management problem was used to illustrate the potential of using the DKAS in solving complex business problems when only limited knowledge about the problem domain is available and additional regularities (rules) can be induced from historical data. The performance of the rules generated by the DKAS is tested using three popular indexes (e.g., Sharpe, Jensen, and Treynor) and the results are, in general, superior to the average market return represented by the NYSE Composite and S&P 500 indexes.

Compared with other machine learning approaches, the DKAS framework has the following advantages: (1) More learning agents: while other learning systems often employ one, or at most two, learning methods, there is no limitation on the number of learning agents that can be incorporated into a DKAS. (2) Modulated learning agents: the learning agents in DKAS are loosely coupled and hence have minimal dependency among them. Therefore, any one learning agent easily can be replaced by another learning agent when the environment changes. (3) Improved learning efficiency: another advantage of the minimal dependency is that the learning processes can be done in parallel and the total processing time can be substantially reduced.

In this paper we have simplified our discussion by including only two learning agents and utilizing some special constraints in guiding the task decomposition and result integration processes. The actual building of a full-scale DKAS is not a trivial problem. There are several important design issues that need to be addressed:

1. The number of learning agents to be included. It is clear that the more learning agents we have, the more powerful the system will be in terms of the type of problems that can be handled. However, it takes time and effort to communicate and coordinate among different learning agents and as the system grows more time is required to interface among agents. The complexity of the coordinating mechanism needed to support the cooperative reasoning process will also increase. Care should be taken in deciding the number of agents to be included. Each learning agent needs to be justified by a careful cost–benefit analysis to ensure the added benefit of the new learning agent is more than enough to offset the increased overhead.

Table 4 Performance Ranking Using Treynor Index, March 1985 through December 1988

<table><tr><td>Market proxy</td><td colspan="2">NYSE Composite index</td><td colspan="2">S&amp;P 500</td></tr><tr><td>Stock screening rules</td><td>Treynor index</td><td>Rank</td><td>Treynor index</td><td>Rank</td></tr><tr><td>Rule 1</td><td>0.48</td><td>5</td><td>0.36</td><td>5</td></tr><tr><td>Rule 2</td><td>0.65</td><td>3</td><td>0.50</td><td>3</td></tr><tr><td>Rule 3</td><td>0.82</td><td>1</td><td>0.60</td><td>1</td></tr><tr><td>Rule 4</td><td>0.51</td><td>4</td><td>0.39</td><td>4</td></tr><tr><td>Rule 5</td><td>0.73</td><td>2</td><td>0.55</td><td>2</td></tr><tr><td>S&amp;P 500</td><td>—</td><td>—</td><td>0.110</td><td>6</td></tr><tr><td>NYSE Composite</td><td>0.100</td><td>6</td><td>—</td><td>—</td></tr></table>

\* Treynor index is calculated by dividing the mean excess return by beta.

Table 5 Performance Ranking Using Jensen Index, March 1985 through December 1988

<table><tr><td>Market proxy</td><td colspan="2">NYSE Composite index</td><td colspan="2">S&amp;P 500</td></tr><tr><td>Stock screening rules</td><td>Jensen index</td><td>Rank</td><td>Jensen index</td><td>Rank</td></tr><tr><td>Rule 1</td><td>0.0030</td><td>5</td><td>0.0026</td><td>5</td></tr><tr><td>Rule 2</td><td>0.0046</td><td>3</td><td>0.0042</td><td>3</td></tr><tr><td>Rule 3</td><td>0.0059</td><td>1</td><td>0.0055</td><td>1</td></tr><tr><td>Rule 4</td><td>0.0032</td><td>4</td><td>0.0029</td><td>4</td></tr><tr><td>Rule 5</td><td>0.0052</td><td>2</td><td>0.0048</td><td>2</td></tr><tr><td>S&amp;P 500</td><td>—</td><td>—</td><td>0.0000</td><td>6</td></tr><tr><td>NYSE Composite</td><td>0.0000</td><td>6</td><td>—</td><td>—</td></tr></table>

The Jensen index is estimated from the least-square regression of fund excess returns on market excess returns.

2. The resolution of conflicts among learning agents. In our example, we assumed that the attributes handled by different learning agents are mutually exclusive. However, a more general system should allow the same attribute to be analyzed by different learning agents. If different recommendations were suggested by different learning agents, how should we decide which direction to follow? One way to approach this problem is to rank the learning agents and construct the rule according to priority.

Although the integration of inductive and deductive learning agents can alleviate some of the problems of using only an inductive learning method (e.g., requires a large number of training examples and cannot incorporate existing domain knowledge into the learning process) the problem of biased rules due to nonrepresentible training examples still exists. Further extensions of a DKAS can be made by including more intelligent learning agents (i.e., environmental learning) into the DKAS to cover other dimensions of the problem and to improve the knowledge acquisition capability. In addition, other components of DKAS also can be improved by incorporating multiple units of the same component, each employing a different algorithm.

## REFERENCES

1. Ahn, W., and Brewer, W.F. Similarity-based and explanation-based learning of explanatory and nonexplanatory information. Proceedings of the Tenth Annual Conference of the Cognition Science Society (1988).

2. Chi, R.T., and Kiang, M. Knowledge acquisition from an incomplete domain theory—an application on stock market. Journal of Computer Science in Economics and Management, 5 (1992), 1–21.

3. DeJong, G.F. Acquiring schemata through understanding and generalizing plans. Proceedings of the Eighth International Joint Conference on Artificial Intelligence, Karlsruhe, West Germany, August 1983, pp. 462–464.

4. DeJong, G.F., and Mooney, R.J. Explanation-based learning: an alternative view. Machine Learning, 1, 2 (1986), 145–176.

5. Fisher, D.H., and Langley, P. Approaches to conceptual clustering. Proceedings of the Ninth International Joint Conference on Artificial Intelligence, Los Angeles, 1985.

6. Fox, M. An organizational view of distributed systems. IEEE Transactions on Systems, Man, and Cybernetics, 11, 1 (January 1981).

7. Holsapple, C.; Tam, K.Y.; and Whinston, A.B. Adapting expert system technology to financial management. Financial Management, 17, 3 (1988), 12–22.

8. Huhns, M.N., ed. Distributed Artificial Intelligence, vol. 1. Los Altos, CA: Morgan Kaufmann, 1988.

9. Jensen, M.C. Risk-the pricing of capital assets, and the investment of portfolios. Journal of Business, 42, 2 (1969), 167–185.

10. Jobson, J.D. and Korkie, B. Performance hypothesis testing with the Sharpe and Treyner measures. Journal of Finance, 36, 4 (1981), 889–908.

11. Kamel, M., and Syed, A. An object-oriented multiple agent planning system. In L. Gasser and M.N. Huhns (eds.), Distributed Artificial Intelligence, vol. 2. San Mateo, CA: Morgan Kaufmann, 1989.

12. Lebowiz, M. Integrated learning: controlling explanation. Cognition Science, 10, 2 (1986), 219–240.

13. Lesser, V.R., and Corkill, D.D. Functionally accurate, cooperative distributed systems. IEEE Transactions on Systems, Man, and Cybernetics, 1 (1981), 81–96.

14. Meyers, T. The Technical Analysis Course: A Winning Program for Stock & Future Traders & Investors. Chicago: Probus, 1989.

15. Michalski, R.S.; Carbonell, J.G.; and Mitchell, T.M., eds. Machine Learning: An Artificial Intelligence Approach. Palo Alto, CA: Tioga, 1983.

16. Michalski, R.S.; Carbonell, J.G.; and Mitchell, T.M., eds. Machine Learning: An Artificial Intelligence Approach, vol. 2. Los Altos, CA: Morgan Kaufmann, 1986.

17. Michalski, R.S., and Chilausky, R.L. Learning by being told and learning by examples: an experimental comparison of two methods of knowledge acquisition in the context of developing an expert system for soybean disease diagnosis. International Journal of Policy Analysis and Information Systems, 4, 2 (1980).

18. Michalski, R.S., and Stepp, R.E. Automated construction of classifications: conceptual clustering versus numerical taxonomy. IEEE Transactions on Pattern Analysis and Machine Intelligence, 5, 4 (1983), 396–409.

19. Minton, S.N., and Carbonell, J.G. Strategies for learning search control rules: an explanation-based approach. Proceedings of the Tenth International Joint Conference on Artificial Intelligence, Milan, 1987, pp. 228–235.

20. Mitchell, T.M.; Keller, R.; and Kedar-Cabelli, S. Explanation-based generation: a unifying view. Machine Learning, 1, 1 (1986), 47–80.

21. Mitchell, T.M.; Mahadevan, S.; and Steinberg, L. LEAP: a learning apprentice system for VLSI design. International Meetings on Advances in Learning, Les Arc, France, 1986.

22. O'Neil, W.J. How to Make Money in Stocks. New York: McGraw-Hill, 1988.

23. Pazzani, M.J. Explanation-based learning for knowledge-based systems. Proceedings of the Knowledge Acquisition for Knowledge-based System Workshop, Alberta, Canada, 1986.

24. Pazzani, M.J. Induction causal and social theories: a prerequisite for explanation-based learning. Proceedings of the 1987 International Machine Learning Workshop, 1987, pp. 230–241.

25. Quinlan, J.R. Induction of decision trees. Machine Learning, 1, 1 (1986), 81–106.

26. Rajamoney, S., and DeJong, G.F. Active explanation reduction: an approach to the multiple explanations problem. Proceedings of the Fifth International Conference on Machine Learning (1988), 242–255.

27. Reinganum, M.R. The anatomy of a stock market winner. Financial Analysis Journal (1988), 16–28.

28. Ritchie, J. Fundamental Analysis: A Back-to-the-Basics Investment Guide to Selecting Quality Stocks. Chicago: Probus, 1989.

29. Samuel, A.L. Some studies in machine learning using the game of checkers. IBM Journal of Research and Development, 3 (1959), 210–229.

30. Sharpe, W.F. Mutual fund performance. Journal of Business, 39, 1 (1966), 119-138.

support: a comparative analysis. Computer Science in Economics and Management, 3 (1990), 147–165.

32. Shaw, M. Mechanisms for cooperative problem solving and multi-agent learning in distributed artificial intelligence systems. Proceedings of the 10th International Workshop on DAI, Bandera, Texas, October 1990.

33. Shaw, M., and Whinston, A.B. A distributed knowledge-based approach to flexible automation: the contract-net framework. International Journal of Flexible Manufacturing Systems, (1988), 85–104.

34. Shen, W., and Simon, H.A. Rule creation and rule learning through environmental exploration. Proceedings of the 11th IJCAI, 1989.

35. Simon, H.A. Models of Man. New York: Wiley, 1957.

36. Smith, R.G., and Davis, R. Frameworks for cooperation in distributed problem solving. IEEE Transactions on Systems Man and Cybernetics, 11, 1 (1981).

37. Smith, R. The contract-net protocol: high-level communication and control in a distributed problem solver. IEEE Transactions on Computers, 29 (December 1980), 1104–1113.

38. Tam, K.Y. Automated construction of knowledge-bases from examples. Information Systems Research, 1, 2 (1990), 144–167.

39. Treynor, J.L. How to rate management of investment funds. Harvard Business Review, 43, 1 (1965), 63–75.

40. Winston, P.H., ed. Learning structural description from examples. In Psychology of Computer Vision. New York: McGraw-Hill, 1975.

41. Woo, C., and Lochovsky, F. Supporting distributed office problem solving in organizations. ACM Transactions on Office Information Systems (July 1986), 185–204.

AND change in quarterly earnings ≥ -1
AND ((current price ratio ≤ 0.8223
AND price to book ratio > 0.95975
AND return on equity > 0.40095)
OR (current price ratio > 0.8223
AND (market capitalization ≤ 187.4515
OR return on equity ≤ 0.0852
OR (price to book ratio > 0.89985
AND net current asset value ≤ -0.3751))))

THEN buy

Rule 2

```txt
IF (shares outstanding ≤ 40,000,000
AND relative strength ≥ 0.15
AND change in quarterly earnings ≥ -1
AND ((current price ratio ≤ 0.87
AND price to book ratio > 0.9747
AND ((market capitalization ≤ 89.4042
AND return on equity > 0.1311)
OR (market capitalization > 89.4042
AND return on equity > 0.2619)))
OR (current price ratio > 0.87
AND (return on equity ≤ 0.0985
OR price to book ratio > 1.34125
OR net current asset value > 4.6595))))
```

THEN buy

## Rule 3

```txt
IF (shares outstanding ≤ 40,000,000
AND relative strength ≥ 0.15
AND change in quarterly earnings ≥ -1
AND (current price ratio > 0.7548
AND (return on equity ≤ 0.0951
OR market capitalization ≤ 164.1595
OR price to book ratio > 1.3708)))
THEN buy
```

Rule 4

IF (shares outstanding ≤ 40,000,000 AND relative strength ≥ 0.15

AND change in quarterly earnings ≥ -1
AND ((current price ratio ≤ 0.881
AND ((price to book ratio ≤ 2.08945
AND return on equity > 0.1495
AND net current asset value ≤ 6.91835
AND market capitalization ≤ 402.97425)
OR (price to book ratio > 2.08945
AND market capitalization ≤ 823.3962)))
OR (current price ratio > 0.881
AND (market capitalization ≤ 559.81095
OR return on equity ≤ 0.0512
OR net current asset value ≤ -35.62625
OR price to book ratio > 3.61125))))

THEN buy

Rule 5

IF (shares outstanding ≤ 40,000,000
AND relative strength ≥ 0.15
AND change in quarterly earnings ≥ -1
AND ((current price ratio ≤ 0.8797
AND (price to book ratio > 1.07015
AND (market capitalization ≤ 195.15815
OR return on equity > 0.4063)))
OR (current price ratio > 0.8797
AND ((return on equity ≤ 0.16685
AND net current asset value ≤ 15.892)
OR (return on equity > 0.16685
AND market capitalization
≤ 3345.02675
AND (price to book ratio > 2.6949
OR net current asset value
≤ -26.4861)))))))

THEN buy

The program was coded in Common Lisp and run on a Macintosh microcomputer.

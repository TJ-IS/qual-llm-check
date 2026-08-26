---
otero_id: 11486
otero_key: "ZH4C8SX2"
title: "On Risk Management with Information Flows in Business Processes"
authors: "Xue Bai; Ramayya Krishnan; Rema Padman; Harry Jiannan Wang"
year: "2013"
journal: "Information Systems Research"
doi: "10.1287/isre.1120.0450"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [130.132.123.28] On: 18 May 2015, At: 01:56 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

## HSR

![](/api/attachments/ZH4C8SX2/fulltext/images/e7e2cf8d4973fdeddf7995539e596d212504cc8f4f177367cc8dfdfd2dc59ffd.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## On Risk Management with Information Flows in Business Processes

Xue Bai, Ramayya Krishnan, Rema Padman, Harry Jiannan Wang

To cite this article:

Xue Bai, Ramayya Krishnan, Rema Padman, Harry Jiannan Wang (2013) On Risk Management with Information Flows in Business Processes. Information Systems Research 24(3):731-749. http://dx.doi.org/10.1287/isre.1120.0450

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2013, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/ZH4C8SX2/fulltext/images/bc6469e6826e823e2d6df00248d66f45a9b1b33a5237f4d1b0963521a6aa1a8b.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# On Risk Management with Information Flows in Business Processes

Xue Bai Department of Operations and Information Management, School of Business, University of Connecticut, Storrs Connecticut 06269, xue.bai@uconn.edu

Ramayya Krishnan The H. John Heinz III College, Carnegie Mellon University, Pittsburgh, Pennsylvania 15213, rk2x@cmu.edu

Rema Padman

The H. John Heinz III College, Carnegie Mellon University, Pittsburgh, Pennsylvania 15213, rpadman@cmu.edu

Harry Jiannan Wang

Department of Accounting and Management Information Systems, Alfred Lerner College of Business and Economics, University of Delaware, Newark, Deleware 19716, hjwang@udel.edu

his article investigates the economic consequences of data errors in the information flows associated with business processes. We develop a process modeling-based methodology for managing the risks associated with such data errors. Our method focuses on the topological structure of a process and takes into account its effect on error propagation and risk mitigation using both expected loss and conditional value-at-risk risk measures. Using this method, optimal strategies can be designed for control resource allocation to manage risk in a business process. Our work contributes to the literature on both ex ante risk management-based business process design and ex post risk assessments of existing business processes and control models. This research applies not only to the literature on and practice of process design and risk management but also to business decision support systems in general. An order-fulfillment process of an online pharmacy is used to illustrate the methodology.

Key words: business process management; control; information flow; expected loss; conditional value at risk History: Alok Gupta, Senior Editor; Vijay Khatri, Associate Editor. This paper was received on April 5, 2011, and was with the authors 8 months for 2 revisions. Published online in Articles in Advance November 8, 2012.

## 1. Introduction

Research has long recognized the importance of welldesigned business processes in organizations (Basu and Kumar 2002, Hammer and Champy 1993, Zhao et al. 2005). Legal mandates, such as the Sarbanes-Oxley Act, have led to a focus on documenting and analyzing the risk associated with errors in the information flow in business processes. The Sarbanes-Oxley Act requires a firm’s CEO and CFO to certify the reliability of the data reported in the financial statements, as well as the reliability and documentation of the information system that produced those data (Pasley 2002). According to CFO magazine (Richter 2007), 75% of the 160 CIOs surveyed in North America and Europe ranked the high cost of clean data as one of the main barriers to information management strategic plans. Defective information and poor-quality data have been the leading causes of process failure, as have information scrap and rework, which have cost companies in the United States alone \$1.5 trillion or more (English 2009). Similar issues with data errors also arise in healthcare processes (De Lusignan 2009, Forster et al. 2008, Kohn et al. 2000, Stein et al. 2000), in which patient safety has become a major concern. Improving the quality of data in electronic medical records and reducing medication errors have become important priorities for healthcare professionals.

Although research on business processes is extensive and diverse in the information systems literature, seldom have researchers studied business processes with the objective of managing the economic consequences of the data errors introduced by the process. In this article, we develop a decision-theoretic methodology to manage the risks arising from data errors in the information flow in business processes. This methodology extends the formal process-oriented ontology that Krishnan et al. (2005) introduced by including attributes about information flow and errors at the task level, at which information transformation processes actually take place, along with the cost and effectiveness of control procedures that are designed to prevent or detect errors in information flow. This extension enables a quantitative assessment of the risks associated with data errors and the design of optimal control allocation strategies that limit risks while minimizing cost.

Our methodology contains two novel aspects. First, it develops a risk-aware process modeling framework to analyze the data error risks in the information flow in a business process. This framework takes into account the structural features of a business process and therefore facilitates the modeling of the economic impact of an error on processes downstream from where the error occurred. Second, the model permits use of either expected loss, with its focus on average losses, or conditional value at risk (CVaR), with its focus on losses that have serious economic consequence, as risk measures to provide flexibility in achieving risk management objectives. The methodology provides a well-founded, quantitative approach to risk assessment and mitigation in business processes. Our work contributes to the literature on both ex ante risk management–based business process design and ex post risk assessments of existing business processes and control models.

The paper has two objectives. First, it seeks to model the key features of elements such as controls and data errors and incorporates the graphical structure of a business process in the analysis of risk. The objective is to derive insight about the interaction between graphical structure of the business process, its role in error propagation, and the location decision related to controls taking into account both their effectiveness and the economic consequences of the data errors. Second, it applies this approach to develop a decision support tool, which can be used to determine the amount of control resources to deploy at a given location in a business process. These two components of the paper address an important and novel problem, and develop both insight through analysis and a computational tool that demonstrably provides valuable decision support.

## 2. Literature Review

Risk management in business process management (BPM) is an important issue in the BPM literature. zur Muehlen and Rosemann (2005) provide a risk taxonomy that includes different error types, error areas, and risk types. They discuss four different types of risk management strategies—namely, mitigation, avoidance, transfer, and acceptance/assumption— with examples in BPM. zur Muehlen and Ho (2005) present a list of common risks encountered in and between different phases in the BPM life cycle, such as analysis, design, implementation, execution, monitoring, and controlling. Our work focuses on data errors in business process information flows and their economic consequences and develops optimal control allocation strategies to mitigate the risk caused by the data errors, a topic that, to the best of our knowledge, has not been discussed in the BPM literature.

## 2.1. Business Process Modeling

Business process modeling is an important area of BPM research. Basu and Blanning (2000) introduced the metagraph, which has been widely applied to model business processes, workflows, and decision support. Van der Aalst (1998) applied Petri nets to model and verify workflows. Several Petri net extensions have been proposed, including colored Petri nets, timed Petri nets, and hierarchical Petri nets, to model workflow attributes, temporal behavior of workflow, workflow events, and subworkflows (Liu et al. 2002, 2007; Van der Aalst 1998). Petri nets have also been applied to verify various structural properties of process models, such as soundness, liveness, safeness, and deadlock (Van der Aalst 1998). The unified modeling language activity diagram (Object Management Group 2011a), business process model and notation (BPMN) (Object Management Group 2011b), and event-driven process chains (EPC) (Scheer 2000) have also been used to model business processes in practice. Our work builds on this literature and demonstrates how process models can be extended to incorporate features required to conduct quantitative risk analysis. Thus, we use Petri nets to model business processes because it has welldeveloped process modeling semantics and associated analytical techniques (Kiepuszewski et al. 2000; Van der Aalst 1998, 2000; Van der Aalst and Ter Hofstede 2005). In particular, we leverage Petri nets to formally model business processes to study error propagation in process information flow and perform risk analysis. We use BPMN to graphically represent business processes.

## 2.2. Risk Metrics

In enterprise risk management, risk is broadly defined as any possible event or circumstance that can have a negative influence on the enterprise (Enterprise Risk Management Committee 2003). Commonly used risk metrics include the Expected Loss (Berger 1980), value at risk (VaR) (Duffie and Pan 1997), and CVaR. Expected loss is a satisfactory measure of risk in cases in which the loss can be viewed as normally distributed with a fixed standard deviation. However, in cases in which the loss distribution is skewed, other risk characteristics, such as quantile estimation or the variance of a loss distribution, need to be taken into account (Corbett 2004, Wang et al. 2008). In the case of loss because of erroneous information, the empirical loss distributions manifest both skewness and discreteness. Managing risks by minimizing expected loss is not an adequate strategy, because the loss associated with errors above a threshold may be significantly larger than that below the threshold. To accommodate such characteristics of loss distributions, our study considers two risk measures: expected loss and CVaR.

The objective of using CVaR (Rockafellar and Uryasev 2000; Rockafellar et al. 2006a, b) as a risk metric is to manage the risk of high losses. The notion of CVaR evolved from VaR, which was first devised by the risk metric group of J. P. Morgan & Company (1996) as a methodology for credit risk assessment. In a financial context, VaR is an estimate of the maximum potential loss, at a certain confidence level $\beta ,$ that a dealer or an end user of a financial instrument experiences during a standardized period (Duffie and Pan 1997). Although VaR has been widely used to measure risk, it has serious limitations. For example, it does not provide any information about the amount of loss exceeding the VaR. For some distributions, the loss beyond the point of VaR may be only a little worse; for others with “fat tails” skewed to the right, the loss beyond VaR may be devastating. In addition, VaR is only computationally tractable for normal distributions (Corbett 2004). For losses that are not “normally” distributed or have a finite number of scenarios, VaR is a nonsmooth, nonconvex, and multiextremum function of the decision variable (Duffie and Singleton 2003, Mausser and Rosen 1999). Given these characteristics, solving an optimization problem with VaR as an objective function is difficult.

In contrast, CVaR (Rockafellar and Uryasev 2000) has more desirable properties than VaR. The value of the CVaR of a loss distribution at a riskiness threshold (5 is essentially the expected value of the -tail of the loss distribution. Acerbi (2002) demonstrates important properties of CVaR, including the asymptotic convergence of the statistical estimates of CVaR. Research has also shown that CVaR is a coherent measure and that it is a subadditive measure, unlike VaR (Pflug 2000, Rockafellar and Uryasev 2000). Furthermore, CVaR is a convex function under quite general assumptions (Acerbi 2002). Therefore, computationally for continuous distributions, CVaR optimization problems lead to convex programming problems. For a finite discrete distribution, the optimal solution can be computed by solving linear programming problems. Perhaps most important, solving CVaR minimization problems simultaneously finds both the minimum CVaR and the corresponding VaR (Rockafellar and Uryasev 2000). Our work considers both expected loss and CVaR in measuring the economic consequences of data errors in the information flow of a business process. The risk management model we develop is able to address the risks measured not only by the expected loss but also by the losses beyond a certain threshold.

## 3. Problem Description

In this section, we use the order-fulfillment process of an online pharmacy as an illustrative example to introduce our research problem and the key concepts relevant to our model. Figure 1 presents the orderfulfillment process using BPMN. The key tasks in the process are as follows:

1. On receiving an order request from customer, staff member enters the order information into the order management system.

2. Staff member enters payment information, such as insurance information and payment method, into the system.

3. Staff member checks customer’s contract information and, if necessary, creates or updates the information.

4. Pharmacist approves the prescriptions.

5. If there is enough supply, the prescription is fulfilled by sending the order for dispensing.

6. If there is not enough supply and the order is urgent, the medication is sent to an alternative source for quick dispensing.

7. If there is not enough supply and the order is not urgent, the order is submitted to the wholesaler.

8. The medicines are sorted and shipped to the customer.

9. Staff member checks customer’s insurance information.

10. Claims, if covered by insurance, are sent to insurance companies.

11. Claims, if not covered by insurance, are sent to the customer.

12. Staff member prepares voucher packages.

13. Accountant updates accounting ledgers.

The semantics of the control flow constructs in Figure 1, including $f _ { 1 } , j _ { 1 } , b _ { 1 } , b _ { 2 } , b _ { 3 } , m _ { 1 } , m _ { 2 } ,$ , and $m _ { 3 } ,$ will be formally discussed in §4.

## 3.1. Information Flow and Data Errors

The information flow in a business process is the flow of informational units passing through a sequence of tasks in a process. Errors may be introduced into the data contained in an information unit because of mistakes, omissions, software glitches, or fraud. We refer to the incorrect, missing, or spurious data in an information unit as an error. Errors can be categorized into different types. We adopt the seven error types that are most commonly used in the auditing literature: completeness, existence, valuation, occurrence, rights and obligations, classification, and cutoff (Lea et al. 1992). Completeness<sup>1</sup> errors occur when not all relevant information exists in the transaction. Existence errors are present when some of the reported information in the transaction is spurious and should not be recognized. Valuation<sup>2</sup> errors occur when the book value of an otherwise valid transaction is incorrect. Occurrence errors are present when not all transactions that should be recorded are recorded. Rights and obligations errors are present when assets do not correctly represent the rights of the company or liabilities do not correctly represent the company’s obligations as of a given date. Classification errors occur when components of the reporting statements are misclassified by type or account. Cutoff errors occur when transaction records are processed during an incorrect period or are not processed in a timely manner.

Figure 1 The Order-Fulfillment Process of an Online Pharmacy  
![](/api/attachments/ZH4C8SX2/fulltext/images/b297f2b8ea58376701d8e37b865ac4c965f74f149c18e474b802508d4424cfcb.jpg)

## 3.2. Risk

Risk arises from the potential negative consequences caused by data errors in the information flow. Risk takes the form of monetary costs, legal penalties, or operational inefficiencies (Marinos 2004). For example, incorrect medication dispensations caused by incorrect titration information may potentially result in adverse drug events. Such events lead to additional administrative costs to the pharmacy and legal liability. Inaccurate and incomplete transactional data result in increased effort directed toward nonproductive inquiry and reporting functions. In cases in which data in the repositories are periodically used to generate performance indicators for business reporting and decision making, working with erroneous data can result in suboptimal decisions. For example, errors in inventory data may lead to inaccurate decisions in reordering, staffing, and pricing. We consider risk as the sum of the economic consequences caused by data errors in the information flow.

## 3.3. Control

Business control procedures monitor and maintain process performance, providing a means to mitigate risk. Our work focuses on information-related control procedures. In auditing practice, control procedures have preventive, detective, and corrective functions (Wand and Weber 1989). Examples of controls include manual or automated check, performance reviews, restricted access, and segregation of duties (ISACA 2007). A business process has a range of control procedures available to prevent, detect, or correct errors in the information flow. Each control procedure is able to detect and/or correct a specific set of error types at specific task locations. By placing various control procedures at different task locations of a process, a control system can reduce errors and ultimately mitigate risks. Furthermore, the quantity of control resources involved in performing a control procedure has associated cost-and-error detection implications.

## 3.4. Optimal Control Strategy

The objective of risk management is to find optimal strategies for control resource allocation in a process to minimize the risk because of data errors under budget constraints. In the pharmacy setting (Figure 1), in which the control application involves mainly manual checking and reviewing, finding the optimal control allocation requires trading off costs and benefits among alternative allocations. For example, decisions must be made among competing allocations of labor hours at task 2 to review accuracy of transaction pricing against supporting pricing documents; at task 3 to check for the existence of unusual order contract terms, future medication orders at incorrect charge or discounts, or price/term exceptions; and at task 13 to review revenue adjustments and ensure that they are processed correctly. To analyze optimal control strategies in the process information flow, in the next section, we formally define the key elements of our process model.

## 4. The Model

In this section, we first develop a process modeling framework. Within the framework, we then develop the mathematical formulations for error propagation, control costs and effectiveness, risks, and risk management.

## 4.1. Modeling Business Processes

Our process model adopts the formal definitions of Petri nets and workflow nets from Van der Aalst (1998). The Petri net specification permits a precise statement of the class of process models to which our models apply and enable direct translation to the notation used in process modeling systems.

Definition 1 (Petri Net). <sub>A</sub> <sub>Petri</sub> <sub>net</sub> <sub>PN</sub> <sub>is</sub> <sub>a</sub> <sub>triple</sub> $( P , T , F )$ , in which

• P is a finite set of places,

• T is a finite set of transitions $( P \cap T = \emptyset )$ , and

$F \subseteq ( P \times T ) \cup ( T \times P )$ is a set of arcs.

A place p is called an input place of a transition t if and only if there is a directed arc from p to t. Place p is called an output place of transition t if and only if there is a directed arc from t to p. Furthermore, •t is used to denote the set of input places for a transition $t ; t ^ { \bullet } , \bullet p ,$ and $p ^ { \bullet }$ have similar meanings. A place contains zero or more tokens at any time. Tokens in Petri nets represent objects, which are information units in this study. The attributes of objects, which are called data, represent the values of those tokens, often referred to as token colors. Information units propagate through a business process by following various paths. A path is formally defined as follows.

Definition 2 (Path). <sub>Let</sub> $P N = ( P , T , F )$ be a Petri net. A path from a node $n _ { 1 }$ to a node $n _ { k } , n _ { i } \in P \cup T ,$ , is a sequence $\left. n _ { 1 } , n _ { 2 } , \ldots , n _ { k } \right.$ such that $\langle n _ { i } , n _ { i + 1 } \rangle \in F ,$ for $1 \leq i \leq k - 1$ (Van der Aalst 1998).

Paths connect nodes, P ∪ T , by a sequence of arcs F . A Petri net is said to be strongly connected if and only if for every pair of nodes $n _ { i }$ and $n _ { j } ,$ there is a path leading from $n _ { i }$ to $n _ { j }$ . A workflow net (WF-net) is a special type of Petri net that can be used to model business processes, as defined as follows (Van der Aalst 1998).

Definition 3 (WF-Net). <sub>A</sub> <sub>Petri</sub> <sub>net</sub> $P N = ( P , T , F )$ is a workflow net (WF-net) if and only if

• PN has two special places: i and o. Place i is a source place: $\bullet i = \emptyset$ . Place o is a sink place: $o \bullet = { \mathcal { D } } .$

• If a transition t<sup>∗</sup> is added to PN to connect place o with i (i.e., $t ^ { * } = \{ o \}$ and $t ^ { * } \bullet = \{ i \} )$ , the resultant Petri net is strongly connected.

Definition 3 ensures that processes modeled as WF-nets have one starting node, one ending node, and no dangling nodes. Definition 3 enables us to model business processes formally. More specifically, we model tasks using transitions; routing constructs, such as fork (AND-Split), join (AND-Join), branch (XOR-Split), and merge (XOR-Join), represent transitions (fork and join) or places (branch and merge) (Van der Aalst 1998). These routing constructs are well-known concepts, so we refer readers to Van der Aalst (1998) for formal semantics.

Definitions 1, 2, and 3 provide the essential elements for mathematical formulations of error propagation and risk management problems in the process information flow. Note that Definition 3 directly supports the most commonly used control flow patterns—namely, sequence, parallel split, synchronization, exclusive choice, and simple merge, as Figure 2 shows.

Advanced patterns, such as multichoice (OR-Split) and multimerge (OR-Join), can be converted into combinations of different basic patterns. For example, an OR-Split can be represented using an AND-Split immediately followed by an XOR-Split in each of the subsequent branches (Van der Aalst et al. 2003). Business processes with structures that cannot be modeled using the five basic patterns and their combinations have been discussed in workflow patterns research (Russell et al. 2006, Van der Aalst et al. 2003) and include multiple instance patterns, state-based patterns, cancellation patterns, and so on. Although WF-nets can be used to model advanced control flow patterns, doing so is not the focus of this article. Rather, we present a specific application of WF-nets in the context of the information flow in a business process. Considering that the five patterns

Figure 2 Basic Control Flow Patterns (Van der Aalst 1998)  
![](/api/attachments/ZH4C8SX2/fulltext/images/eb41ca666376fc615943c61a6b8901d1f9aca3c5c28b6228857f3151358858e7.jpg)  
shown in Figure 2 are the only set of patterns supported by the 14 major commercial process modeling tools/languages that Russell et al. (2006) evaluate, our process modeling framework using WF-nets is sufficiently expressive.  
the transition probability between any pair of pro cess nodes. Let $V : = [ v _ { i j } ]$ be the transition probability matrix for all pairs of tasks. Each element of $V ,$ $v _ { i j } ,$ reflects the transition probability that an information unit output from task i reaches task $j .$ Here, we present a set of rules for deriving a transition probability $( v _ { i j } )$ between tasks i and j with different routing patterns in between, as Figure 2 shows. In the sequence pattern (Figure 2(a)), because there is only one possible path between the two tasks, the transition probability $v _ { i j }$ between tasks i and $j$ is the product of all adjacent transition probabilities (atp) on that path. In the parallel split pattern (Figure 2(b)), after task 1 is completed, tasks 2 and 3 are executed in parallel. Given that an information unit instance cannot be directly passed from task 2 to task $^ { 3 , }$ or vice versa, two copies of the instance are created and passed to tasks $\hat { 2 }$ and $^ { 3 , }$ respectively, after the completion of task 1. This is consistent with the way tokens are handled in a WF-net. Therefore, the transition probability between tasks 1 and $\textit { 2 } \left( v _ { 1 2 } \right)$ equals the transition probability between tasks 1 and $\overline { { { \bf { \Lambda } } } } _ { 3 } \left( v _ { 1 3 } \right)$ , which takes the value of 1. In the synchronization pattern (Figure 2(c)), the two copies of the same data items outputted from tasks 1 and 2 are consolidated into one data item, which is then passed to task 3. Thus, the transition probability between tasks 1 and $3 \ ( v _ { 1 3 } )$ equals the transition probability between tasks 2 and 3 $\left( v _ { 2 3 } \right)$ , which also takes the value of 1. In the exclusive choice pattern (Figure $2 ( \mathrm { d } ) )$ , after task 1 reaches completion, either task 2 or task 3 is executed, which means that an information unit instance follows either of the two paths from task 1 to task 2 or task $^ { 3 , }$ with probabilities $p$ and $1 - p .$ , respectively. Thus, the transition probability between tasks 1 and 2 $\left( v _ { 1 2 } \right)$ is $p ,$ while the transition probability between tasks 1 and $3 \left( v _ { 1 3 } \right)$ is $1 - p .$ . In the simple merge pattern (Figure $2 ( \mathrm { e } ) )$ , an information instance goes from task 1 or task 2 to task 3 for each process instance. Therefore, the transition probability between tasks 1 and 3

4.1.1. Transition Probability. In the presence of different workflow patterns, an information unit may flow through different paths in a process. Consequently, errors introduced into the data in an information unit will flow along one or more paths, and the likelihood of the error reaching another task is different depending on the paths. To accurately capture the impact of an error in an information unit, the net impact of an error should take into account the various paths through which the information unit could flow between any two tasks. In this section, we define two types of transition probabilities in a process: the adjacent transition probability and the transition probability based on Definitions 2 and 3. We then use the transition probability matrix to measure the impact of error propagation in the next section.

Let $\bar { P } N = ( P , T , \bar { F ) }$ be a process modeled as a WFnet, and let D be the set of related information units. Given an information unit $d \in D ,$ , and two adjacent process nodes $n _ { i }$ and $n _ { j } , n _ { i } , n _ { j } \in P \cup T , \left. n _ { i } , n _ { j } \right. \in F _ { \negmedspace }$ , the adjacent transition probability, $a t p ( n _ { i } , n _ { j } , d , \dot { p } )$ , reflects the probability $p$ for an instance of the information unit $d$ output by a node $n _ { i }$ to reach a node $n _ { j } .$ For example, in the order-fulfillment process, $a t p ( b _ { 1 }$ 1 t , order, 0.9) represents the likelihood that for each instance of the information unit (e.g., the order for medication), output from the decision routing construct $b _ { 1 }$ will reach task 5 (“fulfill prescription”) with the probability 0.9. In practical settings, the adjacent transition probability of a pair of adjacent process nodes can be estimated using aggregated frequencies of transaction flows from periodic work logs.

Given the adjacent transition probability measures between any pair of tasks in a process, we can define $( v _ { 1 3 } )$ equals the transition probability between tasks 2 and 3 $( v _ { 2 3 } ) .$ , with the value of 1. If there are no paths between task i and $j ,$ the transition probability $v _ { i j }$ is 0. For any process that can be represented as a well-structured WF-net, these rules can be applied recursively as reduction rules to compute the transition probabilities between any two tasks (Hee and Reijers 2000, Sadiq and Orlowska 2000, Van Dongen et al. 2007).

WF-nets permit formal verification of the structural properties of process models, such as reachability, soundness, and structuredness (Kiepuszewski et al. 2000; Laue and Mendling 2010; Van der Aalst 1998, 2000). Given the importance of structuredness as a design principle for achieving correctness in process models and its application in the most commonly adopted process modeling standard BPEL (business process execution language) (Laue and Mendling 2010, Mendling et al. 2008), we assume that the processes we study herein are well-structured WF-nets (Van der Aalst 1998). A well-structured WF-net only contains properly nested splits and joins, such that each split has a corresponding join of the same type (Laue and Mendling 2010). A well-structured process supports the five routing patterns shown in Figure 2 (Kiepuszewski et al. 2000, Laue and Mendling 2010). We refer readers to Van der Aalst (1998) for a formal definition of structuredness.

4.1.2. Impact of Error Propagation. An information unit may take multiple paths from start to finish in a process. Different paths consist of different sequences of task executions for an information unit. In a path, if task $j$ is executed after task i and no other tasks are executed between i and $j ,$ we can state that task $j$ is one step after task $i ,$ task i is one step before task $j ,$ and there is one step between tasks i and $j .$ It is possible that the number of steps between two tasks varies in different paths. The error propagation metric we introduce next takes into account the impact of errors in all possible paths. Assume that in the process model, the length of the longest paths for an information unit from start to finish is K steps. The transition probability of an information unit between any pair of tasks that are exactly $k$ steps from each other is expressed as an entry in $\check { V } ^ { k } .$ , where $V ^ { k }$ denotes V raised to the kth power. We define $V ^ { k }$ as the k-step transition probability matrix. The matrix $\Gamma ,$ the error propagation potential matrix, is the sum of all the k-step transition probability matrices:

$$
\Gamma = \sum_ {k = 1} ^ {K} V ^ {k}.
$$

As an entry of $\Gamma , \ \gamma _ { i j }$ measures the overall propagation impact of an error that arises at task i and reaches a downstream task $j .$ The intuition is that if one data error is introduced at task $i , \ \gamma _ { i j }$ copies of the error will be transmitted to a downstream task $j .$ We define $\gamma _ { i j }$ as the propagation potential from task i to task $j .$ Appendix A provides an illustration of how we derive propagation parameters for the basic routing patterns. (All appendices for this paper can be found as supplemental material available at http://dx.doi.org/10.1287/isre.1120.0450).

The magnitude of $\gamma _ { i j }$ has important implications for the loss the errors introduced by task i inflict on a downstream task $j .$ In addition, we define the sum of the ith column of $\Gamma$ as the in-degree propagation potential of task $i ,$ such that $\begin{array} { r } { \gamma _ { + i } = \sum _ { j } \gamma _ { j i } , } \end{array}$ , which measures the overall impact of the predecessors of i on passing errors to i. Similarly, we define the sum of the ith row of $\Gamma$ as the out-degree propagation potential of task $i ,$ such that $\begin{array} { r } { \gamma _ { i + } = \sum _ { j } \gamma _ { i j } , } \end{array}$ which measures the overall impact of task i on passing errors to downstream tasks.

## 4.2. Modeling Control Procedures

We now present a model of a control procedure as a resource used to deploy procedures to prevent, detect, and correct data errors. $\mathrm { A }$ control resource is the combination of labor and capital resources used in applying a control procedure. In our context, the resource being allocated is audit hours. We define the level of input as the ratio of the actual amount of control resources used to the total amount of control resources available to perform a control procedure. A concrete example is the sampling procedure of business documents, such as invoices, to detect errors. The level of control resource allocated to the sampling procedure is the ratio of the actual number of auditors and computer equipment involved in the procedure to the total number of auditors and computer equipment available. Let ${ x _ { i m } } \left( 0 \leq x _ { i m } \leq 1 \right)$ denote the input level of control resource at task i for error type m. When no control resources are applied at task i for error type m, we set $x _ { i m } = 0 ;$ when all available control resources at task i for error type m have been applied, we set $x _ { i m } = 1 ;$ and $0 < x _ { i m } < 1$ when a portion of the available control resources has been applied.

4.2.1. Control Effectiveness. We define the effectiveness of a control procedure as the probability that a control procedure is able to detect an existing error. The effectiveness of control depends on the level of the control resource input applied. The higher the level of input, the more effective a control procedure is at detecting errors in the information flow. In the sampling procedure example described previously, the larger the sample size chosen, the greater the control resources required, and the more likely that errors will be caught.

In addition to the level of resource input, the in-degree of the task node of the process graph at which it is located also affects the effectiveness of a control procedure. For example, a control procedure deployed at a task with multiple information inflows may be more effective than a procedure deployed at a task with a single information inflow, because combining information from multiple sources makes error detection procedures, such as comparative checking, easier. Furthermore, control procedures at tasks in which multiple information flows converge are capable of detecting multiple errors simultaneously through batch processing. Thus, the effectiveness of a control procedure depends not only on the resource allocation but also on the node (i.e., task) at which it is located in the process graph. A task location with a greater in-degree propagation potential possesses a higher probability of catching errors.<sup>3</sup>

Let $\alpha _ { i m }$ denote the effectiveness of a control procedure that is deployed at task i to catch errors of type m. In general, the application context determines the form of $\alpha _ { i m }$ . We choose $\alpha _ { i m }$ to be a Cobb-Douglas function of the input level of control resources:

$$
\begin{array}{c} \alpha_ {i m} (x _ {i m}) = g _ {i m} \gamma_ {+ i} \cdot x _ {i m} ^ {a _ {i m}}, \\ 0 \leq x _ {i m} \leq 1, \quad 0 <   g _ {i m} \gamma_ {+ i} \leq 1, \quad a _ {i m} > 0. \end{array}
$$

The family of Cobb-Douglas functions suits our modeling context because it embraces a wide range of both convex and concave function formulations. The exponent $a _ { i m }$ represents the output elasticity of control resources. The value of $a _ { i m }$ is determined by available technology involved in the control procedure, and the value of $a _ { i m }$ determines the convexity or concavity of the effectiveness function. When $0 < a _ { i m } < 1 ,$ the effectiveness function is concave, which indicates diminishing gains in effectiveness on marginal resource input; when $a _ { i m } > 1$ , the effectiveness function is convex, which indicates increasing effectiveness on marginal resource input; and when $a _ { i m } = 1 .$ the effectiveness function is linear, which indicates constant effectiveness on the marginal resource input. Prior research has applied Cobb-Douglas functions to problems in a wide variety of practical settings and, from a modeling standpoint, has shown that they are robust in many applications (Cobb and Douglas 1928, Varian 1992).

The in-degree propagation potential $\gamma _ { + i }$ captures the structural impact of a process on the control effectiveness. The product $g _ { i m } \gamma _ { + }$ <sub>i</sub> quantifies the maximum effectiveness that a control procedure can achieve at task i for error type m, where $0 \leq g _ { i m } \gamma _ { + i } \leq 1$ . The parameter $g _ { i m }$ is a normalizing factor that rescales the maximum effectiveness of a control procedure into the interval between 0 and 1. We use the effectiveness function $\alpha _ { i m } ( x _ { i m } )$ to compute the probability of errors after applying the control procedures.

4.2.2. Control Cost. The cost of a control procedure represents the total cost of control resources for detecting and correcting errors in an information unit. If we use the sampling procedure again to provide context, the larger the sample size chosen, the more the resources involved, and the greater is the cost to execute the procedure. Let $\omega _ { i m } ( x _ { i m } )$ denote the cost per information unit at task i for error type m. Similar to the effectiveness function, we define $\omega _ { i m } ( x _ { i m } )$ as a Cobb-Douglas function of $x _ { i m } \mathrm { : }$

$$
\omega_ {i m} (x _ {i m}) = c _ {i m} \cdot x _ {i m} ^ {b _ {i m}}, 0 \leq x _ {i m} \leq 1, b _ {i m} > 0, c _ {i m} > 0,
$$

where $c _ { i m }$ is the average control cost when all available control resources for error type m at task i have been fully applied. The exponent $b _ { i m }$ measures the cost elasticity of control resource input, and it is determined by the cost factors of the control resources involved. Similarly, $b _ { i m }$ determines the marginal cost per unit input of control resources. The cost function can be either concave or convex.

## 4.3. Modeling Risk

We consider two risk measures in our model: the expected loss and the conditional value at risk.

4.3.1. Expected Loss. Let $e _ { i m }$ be the random binary variable that denotes the presence or absence of an error incidence of type m introduced by task i. We calculate the loss because of an error as a product of the random variable $e _ { i m }$ and the magnitude of the expected negative consequence of a specific error type $s _ { i m }$ (Berger 1980):

$$
l (e _ {i m}) = e _ {i m} s _ {i m}.
$$

Note that errors are introduced into the information flow by tasks, and they then propagate along the paths to their downstream tasks. An error introduced by task i, when left undetected, has a negative impact on the tasks downstream of i. For example, in the order-fulfillment process, an error of inaccurate information on the dosage at the order entry task, if left undetected, will affect the operations of order management, shipping, handling, and billing. This propagated error has a greater negative impact than it would without propagation. Note that the consequences of the same data error vary depending on the tasks it reaches. Let $s _ { i j m } ^ { \prime }$ be the magnitude of the negative consequence of error type m introduced by task i that reaches task $j .$ The relationship between $s _ { i m }$ and $s _ { i j m } ^ { \prime }$ is expressed as follows:

$$
s _ {i m} = \frac {\sum_ {j} \gamma_ {i j} s _ {i j m} ^ {'}}{\sum_ {j} \gamma_ {i j}}.
$$

Assuming that $e _ { i m }$ follows a Bernoulli trial with probability $p _ { i m } ,$ the expected loss for a process with control procedures applied is thus the sum of the expected losses over tasks for all types of errors:

$$
\mathbf {E} (l (x)) = \sum_ {i, m} (1 - g _ {i m} \gamma_ {+ i} x _ {i m} ^ {a _ {i m}}) p _ {i m} s _ {i m} \sum_ {j} \gamma_ {i j}.\tag{1}
$$

Appendix B.1 details the derivation of Equation (1).

4.3.2. -CVaR. The VaR at a significance level $\beta$ is called -VaR; similarly, the CVaR at a significance level $\beta$ is called -CVaR. For a given loss distribution and the decision space $X ,$ , the -CVaR for a given decision $x , x \in X$ , is essentially the expected value of the $( 1 - \beta ) { \tt - } \mathrm { t a i l }$ of the cumulated loss distribution $( \mathrm { i . e . , }$ the expected loss in the $1 - \beta \mathrm { - t a i l } )$ . Rockafellar and Uryasev (2000) prove that the minimization of CVaR, $\mathcal { O } _ { \beta } ( x )$ on a feasible set X can be converted into the minimization of a function, $F _ { \beta } ( x , r )$ on the set of $X \times R \cdot$

$$
\min _ {x \in X} \phi_ {\beta} (x) \equiv \min _ {r \in R; x \in X} F _ {\beta} (x, r),
$$

for a given $\beta ,$ where

$$
F _ {\beta} (x, r) = r + \frac {\mathbf {E} \{[ \sum_ {i , m} \tilde {e} _ {i m} (x _ {i m}) s _ {i m} - r ] ^ {+} \}}{1 - \beta}.\tag{2}
$$

Appendix B.2 details the derivation of Equation (2). Next, we present the two optimization formulations based on the expected loss and CVaR measures.

## 4.4. Problem Formulation

We formulate the optimization problem as follows: Given the control effectiveness and control costs, we find the optimal level of resource input at each task for each error type $x ^ { * }$ , such that the objective risk ì is minimized under a budget constraint B:

$$
\begin{array}{l l} \text {(P0)} & \underset {x \in X} {\min} \Omega \\ & \text {s.t.} C \leq B; \\ & 0 \leq x _ {i m} \leq 1, \quad \forall i, m. \end{array}
$$

The term $C \le B$ is the budget constraint. The budget B is the maximum dollar amount available to detect and fix errors, and C is the sum of control costs across tasks and error types, $\begin{array} { r } { C = \sum _ { i , m } \omega _ { i m } ( x _ { i m } ) } \end{array}$ . The term $0 \leq$ $x _ { i m } \leq 1$ is the resource input–level constraint. The target risk ì can be instantiated as the expected loss or the CVaR.

The expected loss is a reasonable objective function when the loss can be modeled as normally distributed with a fixed standard deviation. In the context of business process information flow, losses associated with erroneous information can be such that the loss associated with errors above a threshold is significantly larger than that below the threshold. To account for such differences in loss, we treat both the expected loss and the CVaR as the objective functions of the model.

The “expected-loss-optimal” model determines the optimal control resource allocation $x ^ { * }$ by minimizing the expected loss. We specify the model as follows:

$$
\begin{array}{l l} \text {(P1)} & \underset {x \in X} {\min} \mathbf {E} (l (x)) \\ & \text {s.t.} \mathbf {C} \leq B; \\ & 0 \leq x _ {i m} \leq 1, \quad \forall i, m. \end{array}
$$

The $' \prime \beta \mathrm { { - } C V a R \mathrm { { - } o p t i m a l " } }$ model finds the optimal control resource allocation $x ^ { * }$ by minimizing the CVaR at the significance level $\beta .$ We specify the model as follows:

$$
\begin{array}{l l} \min _ {r \in R,   x \in X} & F _ {\beta} (x, r) \\ \text {s.t.} & \mathbf {C} \leq B; \\ & r \leq \mathbf {E} (l (x)); \\ & 0 \leq x _ {i m} \leq 1, \quad \forall   i, m. \end{array}\tag{P2}
$$

The term $r \leq E ( l ( x ) )$ guarantees that the threshold value of VaR, $r ,$ is met. In the next section, we analyze how the structure of a process affects the optimal control resource allocations in the expected-loss-optimal and $\beta { \mathrm { - C V a R } } .$ -optimal models.

## 5. The Impact of Process Structure on Optimal Control Allocation

This section investigates the impact of the structural factor, â , which encodes information about the structure of a business process, on the optimal control allocation, $X ^ { * }$ . To do so, we need to isolate the structural factor from other factors, such as the correlations between control effectiveness parameters, between control cost parameters, and between the error consequence parameters. Thus, we derive our analytical results under the following conditions:

1. The effectiveness $\alpha _ { i m }$ of a control procedure is independent of the effectiveness of any other control procedure $\alpha _ { i ^ { \prime } m ^ { \prime } }$ where $i \neq i ^ { \prime }$ or $m \neq m ^ { \prime }$

2. The cost $\omega _ { i m }$ of a control procedure is independent of the cost of any other control procedure $\omega _ { i ^ { \prime } m ^ { \prime } } ,$ where $i \neq i ^ { \prime }$ or $m \neq m ^ { \prime }$

3. There are no correlated consequences of errors across types or tasks $( \mathrm { i . e . , ~ } l _ { i m }$ is independent of $l _ { i ^ { \prime } m ^ { \prime } } )$ where $i \stackrel { \cdot } { \neq } i ^ { \prime }$ or m 6= m<sup>0</sup>.

4. The resource-input elasticity of control effectiveness $a _ { i m }$ is proportional to that of control cost $b _ { i m }$ across task locations and error types in the system $( \mathrm { i . e . , ~ } a _ { i m } / b _ { i m } = \tau , \forall i , m )$

These four conditions enable us to study the impact of the process structure in isolation of other factors and, therefore, to show analytically how the optimal control allocation changes in response to the structural variations of a business process. Under these conditions, both (P1) and (P2) can be solved optimally using Lagrangian methods. Next, we present our analytical results of the structural impact on the expectedloss-optimal and -CVaR-optimal control strategies and discuss the implications of the results for the routing patterns (see Figure 2) that form the structure of a process. Appendix C details the steps for solving (P1) and (P2).

## 5.1. Structural Effect in Expected-Loss-Optimal Control Strategy

The expected-loss-optimal control strategy assigns a higher level of control resource input to task locations with greater in-degree $( \gamma _ { + i } )$ and out-degree $( \gamma _ { i + } )$ propagation potentials, holding all other factors constant. The intuition is that a location with a greater in-degree propagation potential receives a greater volume of information flow and, therefore, potentially more errors from the preceding tasks; similarly, a greater volume of information flow emanates from a location with a greater out-degree propagation potential, which in turn potentially propagates more errors to the downstream tasks. The allocated control procedures are more effective at such locations because they can detect more errors and better prevent potential error propagations.

<sup>Proposition</sup> <sup>1.</sup> For an arbitrary process structure with N tasks, the optimal control resource input level for an error type m at task i that minimizes the expected loss is proportional to the in-degree and out-degree propagation potentials of task i:

$$
x _ {\mathbf {E} _ {i m}} ^ {*} (\Gamma) \propto (\gamma_ {+ i} \gamma_ {i +}) ^ {\theta_ {\mathbf {E} _ {i m}}}, \quad \forall m.
$$

The exponent $\theta _ { \mathbf { E } _ { i m } }$ specifies the marginal impact of a structural factor on the optimal control resource allocation at task i for error type m. The greater the value of $\theta _ { { \bf E } _ { i m } } ,$ the more significant is the impact. The magnitude of $\theta _ { \mathbf { E } _ { i m } }$ depends on whether an interior optimal solution exists for the (P1) model. When an interior optimal solution $x _ { i m } ^ { * }$ exists, $\theta _ { \mathbf { E } _ { i m } } = 1 / ( a _ { i m } -$ $b _ { i m } )$ at the optimal solution; otherwise, $\overset { \underset { \textstyle } { : } \underset { \textstyle \theta _ { \mathbf { E } _ { i m } } } { = } } = 1 .$ , and the optimal solution is at the boundary $x _ { i m } ^ { * } = 1$ Appendix C.1 details the conditions under which an optimal interior solution exists.

Next, we apply Proposition 1 to the basic control routing patterns shown in Figure 2. Each of the corollaries discussed next applies to a routing pattern.

Appendix C presents the formal proofs of the corollaries. For a sequential process with N tasks $( \mathrm { e . g . , }$ the example shown in Figure $2 ( \mathsf { a } ) )$ , let $i , j = 1 , \dots , \bar { N }$ be the indexes of the ordering of the tasks, where ${ } ^ { \prime \prime } i < j { } ^ { \prime \prime }$ indicates that task i is performed before task j.

<sup>Corollary</sup> <sup>1.</sup> For a sequential process structure with N tasks, holding all other factors constant, the ratio of the optimal control resource input for an error type m between tasks i and j that minimizes the expected loss is

$$
\frac {x _ {\mathbf {E} _ {i m}} ^ {*}}{x _ {\mathbf {E} _ {j m}} ^ {*}} = \frac {(i (1 + N - i)) ^ {\theta_ {\mathbf {E} _ {i m}}}}{(j (1 + N - j)) ^ {\theta_ {\mathbf {E} _ {j m}}}}, \quad \forall m.\tag{3}
$$

The ratio $x _ { \mathbf { E } _ { i m } } ^ { * } / x _ { \mathbf { E } _ { i m } } ^ { * }$ measures the relative importance of task i to task j for control resource allocation. For tasks i and j that have the same probability of introducing errors of type m, (i.e., $p _ { i m } = p _ { j m } , \forall m )$ , and for the controls at tasks i and j that are equally cost effective, the highest input of control resources is toward the middle of the process paths. This result comes strictly from the structural factor of the process. By holding all other factors constant, we can focus the analysis on the structural aspect of the process and center the impact of process structures on the optimal input level of control resources.

Intuitively, control procedures would seem more effective at the tasks toward the beginning or the end of the process. However, the functionalities of a control are twofold: first, to catch and eliminate errors that are introduced by upstream tasks and, second, to prevent errors that are introduced by upstream tasks from propagating to downstream tasks. The overall effectiveness of a control is greater at the middle nodes than at either end in a sequential process, and therefore these middle nodes are the best locations to allocate control resources.

For a process structure including fork/join or branch/merge with N tasks (e.g., the examples shown in Figure 2(b)–2(e)), let $i = 1 , \ldots , N - 1$ be the indexes of the tasks that are on the branches, and let i = N be the task right before fork/branch or after join/merge.

<sup>Corollary</sup> <sup>2.</sup> For a process structure including fork/ join or branch/merge with N tasks, holding all other factors constant, the ratio of the optimal control resource input for any error type m between tasks i and N that minimizes the expected loss is

$$
\frac {x _ {\mathbf {E} _ {i m}} ^ {*}}{x _ {\mathbf {E} _ {N m}} ^ {*}} = \frac {2 ^ {\theta_ {\mathbf {E} _ {i m}}}}{(N (N - 1)) ^ {\theta_ {\mathbf {E} _ {N m}}}}, \quad \forall m.\tag{4}
$$

For a process structure with fork/join or branch/ merge, the highest input level of control resources is at the forking/branching node or joining/merging node of the process. This result is intuitive because, compared with nodes on the branches, the joining/ merging nodes have greater in-degree propagation potential and the forking/branching nodes have greater out-degree propagation potential. When we hold all other factors constant between a joining/ merging node task and a forking/branching node task, tasks located at the joining/merging point of the process obtain more information by having multiple information inputs. Similarly, tasks located at the forking/branching point of the process propagate more information by having multiple information outputs. Consequently, control procedures can perform more effectively by batch processing or comparative checking techniques.

## 5.2. Structural Effect in -CVaR-Optimal Control Strategy

The optimal solution for the -CVaR-optimal model shows a similar pattern to that in the expected-lossoptimal model: The relative importance of tasks i and j is proportional to the product of the in-degree propagation potential $( \gamma _ { + i } )$ and the out-degree propagation potential $( \gamma _ { i + } )$ , holding all other factors constant.

<sup>Proposition</sup> <sup>2.</sup> For an arbitrary process structure with N tasks, the optimal level of control resource input for an error type m that minimizes CVaR at task i is proportional to the in-degree and out-degree propagation potentials of task i:

$$
x _ {\phi_ {i m}} ^ {*} (\Gamma) \propto (\gamma_ {+ i} \gamma_ {i +}) ^ {\theta_ {\phi_ {i m}}}, \quad \forall m.
$$

Similarly, the value of $\theta _ { \phi _ { i m } }$ specifies the marginal impact of the structural factor on the optimal control resource allocation at task i for error type m. The greater the value of $\theta _ { \phi _ { i m } } ,$ the more significant is the impact. The magnitude of $\theta _ { \phi _ { i m } }$ depends on whether an interior optimal solution exists for the (P2) model. The conditions under which an interior optimal solution exists for (P2) are different from those for (P1), which are detailed in Appendix C.2.

By applying Proposition 2 to the basic routing patterns, we have the following corollaries: For a sequential process with N tasks (e.g., the example shown in Figure 2(a)), let $i , j = 1 , \dots , N$ be indexes of the ordering of the tasks, where $i < j$ indicates that task i is performed before task j.

<sup>Corollary</sup> <sup>3.</sup> For a sequential process structure with N tasks, holding all other factors constant, the ratio of the optimal level of control resource input for an error type m between tasks i and j that minimizes CVaR is

$$
\frac {x _ {\phi_ {i m}} ^ {*}}{x _ {\phi_ {j m}} ^ {*}} = \frac {(i (1 + N - i)) ^ {\theta_ {\phi_ {i m}}}}{(j (1 + N - j)) ^ {\theta_ {\phi_ {j m}}}}, \quad \forall m.\tag{5}
$$

Equation (5) shows the same pattern as Equation (3), in that the highest level of control resource input is optimally toward the middle of the routing pattern.

For a process structure including fork/join or branch/merge with N tasks (e.g., the examples shown in Figure $2 ( \mathrm { b } ) { - } 2 ( \mathrm { e } ) )$ , let $i = 1 , \ldots , N - 1$ be the indexes of the tasks that are on the branches, and let $i = N$ be the task right before fork/branch or after join/merge.

<sup>Corollary</sup> <sup>4.</sup> For a process structure including fork/ join or branch/merge with N tasks, holding all other factors constant, the ratio of the optimal level of control resource input for any error type m between tasks i and N that minimizes CVaR is

$$
\frac {x _ {\phi_ {i m}} ^ {*}}{x _ {\phi_ {N m}} ^ {*}} = \frac {2 ^ {\theta_ {\phi_ {i m}}}}{(N (N - 1)) ^ {\theta_ {\phi_ {N m}}}}, \quad \forall m.\tag{6}
$$

Equation (6) shows the same pattern as Equation (4), in that the highest level of control resource input is at the forking/branching or joining/merging point of the process.

## 5.3. Relationship Between Expected-Loss-Optimal and -CVaR-Optimal Solutions

Recall that CVaR is the expected value of (1 − )-tail of the cumulated loss distribution. When $\beta \to 0 ,$ the value of CVaR converges to the value of expected loss; that is,

$$
\lim _ {\beta \to 0} \phi_ {\beta} = \mathbf {E} (l).
$$

If an optimal solution of the CVaR-optimal model at the level $\beta = 0$ exists, the optimal solution of the model equals the optimal solution of the expected-loss-optimal model; that is, if $x _ { \phi _ { i m , \beta = 0 } } ^ { * }$ exists, $x _ { \phi _ { i m , \beta = 0 } } ^ { * } = x _ { \mathbf { E } _ { i m } } ^ { * }$ . Thus, we have the following proposition (Appendix C.3 presents the formal proof of Proposition 3):

<sup>Proposition</sup> <sup>3.</sup> For a process with an arbitrary routing pattern, $i f x _ { \phi _ { i m , \beta = 0 } } ^ { * }$ exists, then

$$
\theta_ {\mathbf {E} _ {i m}} ^ {*} = \theta_ {\phi_ {i m, \beta = 0}} ^ {*}; \qquad \frac {x _ {\mathbf {E} _ {i m}} ^ {*}}{x _ {\mathbf {E} _ {j m}} ^ {*}} = \frac {x _ {\phi_ {i m , \beta = 0}} ^ {*}}{x _ {\phi_ {j m , \beta = 0}} ^ {*}}, \quad \forall i, j, m.
$$

In the next section, we illustrate our methodology using the order-fulfillment process of an online pharmacy. We then discuss the computational results.

## 6. Case Study

In this section, we validate our approach by calibrating our model using the data of an online pharmacy’s order-fulfillment process. We present the procedure of applying our approach with the help of a prototype system developed to provide a friendly graphical user interface for process modeling and risk parameter specification. A typical procedure of applying our approach consists of five steps, as indicated by the numbers in Figure 3, as follows:

Figure 3 Procedure of Applying Our Approach  
![](/api/attachments/ZH4C8SX2/fulltext/images/1d63e531726a1eb784ffa90354b7dcc267f87441ff46efaad07f82b6e91242fc.jpg)

• Step 1. In this step, process analysts and risk managers collaborate online to create a business process model with risk management parameters. Appendix D.1. presents a screenshot of our process modeling tool. We extend an open-source, Webbased collaborative process modeling tool named Oryx BPMN modeler (http://www.oryx-editor.org) with risk management modeling capability. In particular, we develop a risk management BPMN stencil extension, which adds additional properties to tasks and control flow links to specify different types of error probability, error consequences, and error volume transition probabilities. This tool enables multiple people to work on a process model using Web browsers (e.g., the process analyst first draws the process model, and then the risk manager adds the risk parameters to the model).

• Step 2. After the process model is fully specified with risk management parameters, it can be exported into different XML formats, such as XPDL, RDF, Petri nets, and EPC, for interoperability with other process modeling and/or advanced process analysis tools.

• Step 3. The process model exported from the modeling tool is converted into different matrices (as we define herein), such as the volume transition matrix, error propagation potential matrix, error probability matrix, and error consequence matrix, in text formats for optimization analysis. We developed a format transformation tool to convert process models with risk parameters in RDF format into various matrices in text files.

• Step 4. In this step, we use the optimization toolbox of the MATLAB to import the matrices produced in step 3 to conduct various experiments. We describe these in detail in the next section.

• Step 5. We import the MATLAB experiments results (e.g., the control resource values for different tasks) into the modeling tool to show the graphical process model.

Next, we show a detailed case study of applying our approach using a data set we collected from an online pharmacy.

## 6.1. Order-Fulfillment Process Revisited

We instantiate the model using the data collected from the order-fulfillment process of an online pharmacy introduced previously. On average, the pharmacy fulfills 1,200 medication orders every month. The data consist of descriptions of the 13 internal tasks, their path dependencies, and information transformation processes, which we model using our prototype system as shown in Figure 1. For each medication order, the data contain the historical records of error instances, categorized into error types, frequency of error occurrence, and the average cost per error per type, and are entered into the system as task properties. For each control activity performed in the orderfulfillment process, the data provide descriptions of control activities, that is, the frequency and average cost of control. Data on the effectiveness of control are estimated from the internal control logs and the external auditing reports on the internal control performance.

From the path relationships and volume transition among the tasks shown in Figure 1, our prototype system generates the transition probability matrix V and propagation matrix â, as presented in Figure 4. The parameters are estimated from the transition probabilities among the 13 internal tasks. For example, the first column and the first row of both matrices represent task 1; the last column and the last row of both matrices represent task 13.

A total of 47 error instances, categorized in seven error types, occurred in the order-fulfillment process. Appendix D.2. provides a detailed description of the seven error types that occurred in the orderfulfillment process. We use the historical data on error frequencies to estimate $p _ { i m } ,$ which we then use to sample error instances in the experiments. Figure 5 presents the matrices of the estimated error probabilities $p _ { i m }$ and error consequences $s _ { i m } .$ . In both matrices, the columns correspond to error types, and the rows correspond to task locations. The seven columns list the parameters for valuation errors, completeness errors, existence errors, occurrence errors, rights and obligations errors, classification errors, and cutoff errors, respectively. The ith row lists the parameters for task i. The parameters of error consequences vary across tasks and error types.

Figure 4 Transition Probability and Error Propagation Matrices for the Order-Fulfillment Process

$$
V := [ v _ {i j} ] = \left[ \begin{array}{c c c c c c c c c c c c} 0 & 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & . 9 & . 0 8 & . 0 2 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & \end{array} \right]
$$

The control procedures we performed in the process include random sampling of order entries throughout the process, auditing potential medication errors, auditing medications entering the dispensing system against the order sheets, checking order information for the refill cycles, and checking the items on the delivery sheet against the items in the respective bag. The resources required for each of the control procedures include either some or all of the following three types: staff members, audit training sessions, and IT systems and equipment. The control cost includes the wages, compensation of audit trainers and trainees, and expenditure for IT equipment. The total cost of a control procedure is the sum of the costs of the required resources per order multiplied by the number of monthly orders. The marginal cost per unit input of control resource $b _ { i m }$ equals 1, indicating a linear marginal cost per unit of control resource input. Table 1 lists the estimated cost of controls provided by the pharmacy.

$$
\Gamma := [ \gamma_ {i j} ] = \left[ \begin{array}{c c c c c c c c c c c c c} 0 & 1 & 2 & 2 & 1. 8 & . 2 & . 2 & 2. 2 & 2. 2 & 1. 7 6 & . 4 4 & 2. 2 & 2. 2 \\ 0 & 0 & 0 & 1 & . 9 & . 0 8 & . 0 2 & 1. 1 & 1. 1 & . 8 8 & . 2 2 & 1. 1 & 1. 1 \\ 0 & 0 & 0 & 1 & . 9 & . 0 8 & . 0 2 & 1. 1 & 1. 1 & . 8 8 & . 2 2 & 1. 1 & 1. 1 \\ 0 & 0 & 0 & 0 & . 9 & . 0 8 & . 0 2 & 1. 1 & 1. 1 & . 8 8 & . 2 2 & 1. 1 & 1. 1 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & . 8 & . 2 & 1 & 1 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & . 8 & . 2 & 1 & 1 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & . 8 & . 2 & 1 & 1 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ \text {if} \text {when} \text {if} \text {when} \text {if} \text {when} \text {if} \text {when} \text {if} \text {when} \text {if} \text {when} \text {if} \text {when} \text {if} \text {when} \text {if} \text {when} \text {if} \text {when} \text {if} \text {when}. \\ \text {if} \text {when} \text {if} \text {when} \text {if} \text {when} \text {if} \text {when} \text {if} \text {when}. \\ \text {if} \text {when} \text {if} \text {when} \text {if} \text {when}. \\ \text {if} \text {when}. \\ \text {if} \text {when}. \\ \text {if} \text {when}. \\ \text {if} \text {when}. \\ \text {if} \text {when}. \\ \text {if} \text {when}. \\ \text {if} \text {when}. \\ \text {if} \text {when}. \\ \text {if} \text {when}. \\ {\mathrm{if}} \end{array} \right]
$$

The pharmacy expects that better-trained staff members perform tasks with fewer mistakes, with improved performance consistent across tasks and error types. The estimated maximum effectiveness of each control procedure equals $g _ { i m } \gamma _ { + i } ,$ where $\gamma _ { + i }$ comes from matrix â in Figure 4. The scale factor for the maximum control effectiveness in our case study is 0.05 $( \mathbf { i . e . } , \ g _ { i m } = 0 . 0 5 )$ . The maximum control effectiveness $g _ { i m } \gamma _ { + i }$ is less than one for all $i , m ,$ indicating that the data errors cannot be completely eliminated from the process. We estimate the expected marginal effectiveness $a _ { i m }$ by taking the average across tasks and error types, which in our case is $a _ { i m } = 0 . 5$ . With the calibrated parameters, we solve the linear programming for (P1) and (P2) in MATLAB to obtain the numerical results.

## 6.2. Computational Results and Analyses

We generate the order-fulfillment process using the calibrated parameters on process structure, error

Figure 5 Error Probabilities and Consequences Matrices for the Order-Fulfillment Process

$$
[ p _ {i m} ] = \left[ \begin{array}{c c c c c c c} 2. 0 \% & 0. 1 \% & 0. 5 \% & 1 \% & 0 & 0 & 0 \\ 0. 3 \% & 0 & 0 & 0. 1 \% & 0 & 0 & 0 \\ 0 & 0. 1 \% & 0 & 0. 1 \% & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0. 2 \% & 0 & 0 \\ 0. 3 \% & 0 & 0 & 0. 1 \% & 0 & 0 & 0 \\ 0. 3 \% & 0 & 0 & 0. 1 \% & 0 & 0 & 0 \\ 0. 0 2 \% & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0. 5 \% & 0 \\ 0. 0 2 \% & 0. 5 \% & 0 & 0 & 0 & 0 & 0 \\ 7. 5 \% & 0. 2 \% & 0. 0 2 \% & 0 & 0 & 0 & 0 \\ 0. 0 2 \% & 0 & 0 & 0. 0 2 \% & 0 & 0 & 0 \\ 0 & 0. 1 \% & 0. 1 \% & 0 & 0 & 0. 1 \% & 0 \\ 0. 1 \% & 0 & 0 & 0 & 0 & 0. 1 \% & 0. 0 1 \% \end{array} \right];
$$

$$
[ s _ {i m} ] = \left[ \begin{array}{c c c c c c c} 2 5 0 & 1 0 0 & 1 0 0 & 1 0 0 & 0 & 0 & 0 \\ 1 0 0 & 0 & 0 & 2 5 0 & 0 & 0 & 0 \\ 0 & 1 0 0 & 0 & 2 5 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 5 0 0 & 0 & 0 \\ 1 0 0 & 0 & 0 & 1 0 0 & 0 & 0 & 0 \\ 1 0 0 & 0 & 0 & 1 0 0 & 0 & 0 & 0 \\ 1, 0 0 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 4 0 & 0 \\ 1 0 0 & 5 0 & 0 & 0 & 0 & 0 & 0 \\ 3 0 & 5 0 & 2, 5 0 0 & 0 & 0 & 0 & 0 \\ 1, 0 0 0 & 0 & 0 & 2 5 & 0 & 0 & 0 \\ 0 & 2 5 & 2 5 & 0 & 0 & 2 5 & 0 \\ 2 5 & 0 & 0 & 0 & 0 & 2 5 & 5 0 \end{array} \right].
$$

Table 1 Task-Specific Cost Factors of the Control Procedures and the Parameter Estimates

<table><tr><td>Task i</td><td>The cost factors ($ per order)</td><td>Estimates ( $c_{im}$ ,  $b_{im}$ ) $c_{im} = c_i$ , ∀ m; $b_{im} = 1$ , ∀ i, m</td></tr><tr><td>1, 2, 3, 9</td><td>$0.5 per order per staff member$ 0.1 per order on training sessions$0.125 per order on computer support</td><td>(0.725, 1)</td></tr><tr><td>4</td><td>$1 per order per staff member$0.25 per order on training sessions$0.15 per order on computer support</td><td>(1.4, 1)</td></tr><tr><td>5, 6, 7, 8,10, 11</td><td>$0.5 per order per staff member$0.05 per order on training sessions$ 0.05 per order on computer support</td><td>(0.6, 1)</td></tr><tr><td>12,13</td><td>$1 per order per staff member$0.2 per order on training sessions$0.15 per order on computer support</td><td>(1.35, 1)</td></tr></table>

probabilities, error consequences, and the cost and effectiveness of control procedures. In total, 1,200 informational units are simulated for each experiment. We run three sets of experiments, each with one of three budget levels: a small budget $( B = \$ 5,000)$ , a medium budget $( B = \$ 25,000$ , and a large budget $( B = \$ 45,000$ . For each set of experiments, we compare four control allocation strategies: no control resource allocation, random control resource allocation, expected-loss-optimal allocation, and -CVaR-optimal allocation. We report the resultant loss distributions, the objective risk measures, and the optimal solutions for the four strategies for each set of the experiments.

6.2.1. Comparing Loss Distributions. Figure 6 presents the probability density functions (PDFs, left panels) of the loss and the corresponding cumulative distribution functions (CDFs, right panels) of the loss based on the four control allocation strategies for the three budget levels, respectively. Figure 6 provides the following two observations.

1. Reduction in multimodality. When no controls are applied, the PDFs of the loss are multimodal, with a taller mode corresponding to lower values of the loss and a shorter mode corresponding to higher values of the loss. We observe that controls reduce multimodality considerably, independent of the budget level. The taller modes shift to the left, assigning more probability to smaller monetary losses, and the shorter modes become negligible.

In particular, the modes corresponding to the expected-loss-optimal and -CVaR-optimal strategies shift substantially to the left and grow taller. This suggests that applying our proposed control strategies leads to a healthier risk outlook for the company, in terms of expected loss and conditional value at risk. Accordingly, we note that by applying controls, the tails of the corresponding CDFs shrink to the left.

2. A thinner tail by -CVaR-optimal strategy. Independent of the budget constraint, we observe that the CDF corresponding to the -CVaR-optimal strategy has a thinner tail—in fact, the thinnest tail of all experiments. Note that in all experiments, the CDFs corresponding to the -CVaR-optimal strategy (the dotted lines with plus markers) cross the CDFs corresponding to the expected-loss-optimal strategy (the dashed red lines with circular markers) to reach the cumulative density of one at a lower value of the loss. This result suggests that the -CVaRoptimal strategy helps reduce losses at the tail of a distribution, as might be expected.

6.2.2. Comparing Outcome Risk Measures. Table 2 presents the outcome risk measures achieved by the four control strategies. The results show two trade-off patterns in the outcome risk measures.

1. Trade-off between the outcome risk measures. The results show that the outcome risk measures are not all minimized in any of the control strategies. In all the experimental results, minimizing one measure results in higher values in other measures. For example, if the pharmacy wants to minimize the expected loss with a small control budget (the top table, B = \$510005 using the expected-loss-optimal strategy, the resulting expected loss is the lowest of all (\$18,821.2), and the resultant CVaR is higher (\$116,226.2) than the CVaR value achieved with the -CVaR-optimal strategy (\$113,470.1). Conversely, if the pharmacy wants to minimize the expected loss beyond the VaR at the 90th percentile, the resulting CVaR value is the lowest of all (\$113,470.1), and the resultant expected loss (\$19,765.2) is higher than that with the expected-lossoptimal strategy (\$18,821.2). Similar patterns occur in the medium and large budget cases.

2. Trade-off between costs and risks. The results also show a trade-off between the cost of control and the resulting risk mitigation. As the budget of control increases, the risk reduction increases; however, the marginal risk reduction decreases. For example, for the expected-loss-optimal strategy with a small control budget (the top table, B = \$510005, the marginal reduction in the resultant expected loss is 4281385000 − 1818210235/51000 = 1091, and the marginal reduction in the resultant CVaR is 41721143033 − 11612260255/ 51000 = 11033. For the expected-loss-optimal strategy with a medium-level budget (the middle table, $B ^ { ' } = \$ 25 ,000$ the marginal reduction in the resultant expected loss is 4241609029 − 810560375/251000 = 0066, and the marginal reduction in the resultant CVaR is $( 1 3 4 , 0 6 7 . 0 \breve { 8 } - 5 5 , 8 6 1 . 7 8 ) / 2 5 , 0 0 0 = 3 . 1 7 .$ . The -CVaR-optimal strategies show similar patterns for the three different budget levels in Table 2 as well. Finally, compared with the random control strategy, the expected-loss-optimal and -CVaR-optimal strategies consistently achieve greater risk reduction in all resulting risk measures with the same control expenditure in all experiments.

Figure 6 The PDFs and Corresponding CDFs of the Loss Based on the Four Control Allocation Strategies  
![](/api/attachments/ZH4C8SX2/fulltext/images/ac4595d23577de227a3567d8fc7da488e0ff946afb22eb5c3205a53aa8b78ddf.jpg)

Table 2 Outcome Risk Measures by the Four Control Allocation Strategies

<table><tr><td>Control strategy (B = $5,000)</td><td>Exp. loss E/(I(x*))</td><td>CVaR  $\phi_{\beta}(x^{*})$ </td><td>Cost C(x*)</td></tr><tr><td>No control</td><td>28,385.00</td><td>172,143.33</td><td>0.00</td></tr><tr><td>Random control</td><td>23,984.30</td><td>150,601.75</td><td>5,000.00</td></tr><tr><td>Min exp. loss</td><td>18,821.23</td><td>116,226.25</td><td>5,000.00</td></tr><tr><td>Min CVaR</td><td>19,765.25</td><td>113,470.13</td><td>5,000.00</td></tr><tr><td>Control strategy (B = $25,000)</td><td>Exp. loss E/(I(x*))</td><td>CVaR  $\phi_{\beta}(x^{*})$ </td><td>Cost C(x*)</td></tr><tr><td>No control</td><td>24,609.29</td><td>134,067.08</td><td>0.00</td></tr><tr><td>Random control</td><td>18,182.59</td><td>101,489.43</td><td>25,000.00</td></tr><tr><td>Min exp. loss</td><td>8,056.37</td><td>55,861.78</td><td>25,000.00</td></tr><tr><td>Min CVaR</td><td>11,458.99</td><td>52,230.10</td><td>25,000.00</td></tr><tr><td>Control strategy (B = $45,000)</td><td>Exp. loss E/(I(x*))</td><td>CVaR  $\phi_{\beta}(x^{*})$ </td><td>Cost C(x*)</td></tr><tr><td>No control</td><td>23,237.83</td><td>141,180.42</td><td>0.00</td></tr><tr><td>Random control</td><td>8,234.46</td><td>43,412.38</td><td>45,000.00</td></tr><tr><td>Min exp. loss</td><td>2,934.20</td><td>23,175.74</td><td>45,000.00</td></tr><tr><td>Min CVaR</td><td>4,457.38</td><td>18,439.51</td><td>45,000.00</td></tr></table>

6.2.3. Optimal Control Resource Allocation. We present the numerical results of the optimal control resource allocations at two levels: the task level and the task-and-error-type level. For the task level, we present a vector ${ \vec { x } } ,$ which consists of the row sums of the matrix $[ x _ { i m } ]$ . For the task-and-error-type level, we present the matrix $[ x _ { i m } ]$ for each set of experiments. For each element of ${ \vec { x } } , \ x _ { i }$ is the sum of the ith row of the matrix $\begin{array} { r } { \left[ x _ { i m } \right] ( \mathrm { i } . \mathbf { e } . , x _ { i } = \sum _ { m } x _ { i m } ) } \end{array}$ . Table 3 lists the task-level control resource allocation solutions suggested by the three different control strategies for each set of the experiments. Tables E1–E9 in Appendix E show the solutions for the task-and-error-type control resource input $[ x _ { i m } ]$ for each set of experiments. The results suggest the following:

1. Controls that lie between many paths play a key role in alleviating error propagation. The resources employed in a control procedure at a task are positively correlated with the connectivity of the task. Task 4 (Pharmacists approve prescription) has significant resource input in both optimal control resource allocation strategies. In contrast, the two downstream branching tasks of task 4, task 5 (If there is enough supply, the prescription is fulfilled by sending the order for dispensing), and task 6 (Urgent order of out-of-stock medications is sent to an alternate source for dispensing) have little control resource applied in nearly all the optimal control strategies. This is an intuitive outcome because by applying a control procedure to a task that appears on many paths of a process, the control is more likely to detect existing errors and prevent them from propagating to the rest of the process.

2. Sources of multiple error types are critical control locations. Task 1 (Staff member enters the order information into the order management system) consistently has the highest level of control resource allocation. One of the most important reasons for this outcome is that task 1 has the potential to introduce many types of errors. In addition, compared with other tasks, the frequencies of error occurrence at task 1 are among the highest for each error type; the corresponding error consequences are most significant as well. This observed result indicates that the level of control resources optimally placed at a task is positively correlated with frequencies of error occurrences and error consequences.

3. Ceteris paribus, optimal control favors cost-effective resources. When the marginal effectiveness of each control procedure is the same, the optimal control resource allocation strategy is achieved by applying more resources at task locations in which the control procedures are less costly. For example, the amount of resources applied at task 1 is significantly larger than that at task 4. This is partially because the wage of a staff member who operates control procedures at task 1 is less than that of a pharmacist who operates control procedures at task 4.

Table 3 Task Level Control Resource Allocations Suggested by Four Strategies

<table><tr><td>Control strategy</td><td> $x_{1}$ </td><td> $x_{2}$ </td><td> $x_{3}$ </td><td> $x_{4}$ </td><td> $x_{5}$ </td><td> $x_{6}$ </td><td> $x_{7}$ </td><td> $x_{8}$ </td><td> $x_{9}$ </td><td> $x_{10}$ </td><td> $x_{11}$ </td><td> $x_{12}$ </td><td> $x_{13}$ </td></tr><tr><td colspan="14">Amount of control resources utilized at individual tasks ( $B = \$5,000$ )</td></tr><tr><td>No control</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>Random control</td><td>0.06</td><td>0.02</td><td>0.02</td><td>0.01</td><td>0.02</td><td>0.06</td><td>0.03</td><td>0.05</td><td>0.07</td><td>0.03</td><td>0.05</td><td>0.07</td><td>0.03</td></tr><tr><td>Min exp. loss</td><td>0.38</td><td>0.00</td><td>0.02</td><td>0.03</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.01</td><td>0.01</td><td>0.02</td><td>0.00</td><td>0.00</td><td>0.05</td></tr><tr><td>Min CVaR</td><td>0.16</td><td>0.00</td><td>0.13</td><td>0.13</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.02</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.01</td></tr><tr><td colspan="14">Amount of control resources utilized at individual tasks ( $B = \$25,000$ )</td></tr><tr><td>No control</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>Random control</td><td>0.03</td><td>0.24</td><td>0.10</td><td>0.16</td><td>0.20</td><td>0.11</td><td>0.21</td><td>0.31</td><td>0.05</td><td>0.29</td><td>0.19</td><td>0.39</td><td>0.18</td></tr><tr><td>Min exp. loss</td><td>1.00</td><td>0.02</td><td>0.19</td><td>0.26</td><td>0.00</td><td>0.00</td><td>0.01</td><td>0.10</td><td>0.14</td><td>0.19</td><td>0.00</td><td>0.00</td><td>0.42</td></tr><tr><td>Min CVaR</td><td>0.49</td><td>0.01</td><td>0.23</td><td>0.73</td><td>0.04</td><td>0.00</td><td>0.06</td><td>0.08</td><td>0.05</td><td>0.55</td><td>0.00</td><td>0.00</td><td>0.04</td></tr><tr><td colspan="14">Amount of control resources utilized at individual tasks ( $B = \$45,000$ )</td></tr><tr><td>No control</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>Random control</td><td>0.60</td><td>0.20</td><td>0.59</td><td>0.17</td><td>0.13</td><td>0.12</td><td>0.58</td><td>0.30</td><td>0.26</td><td>0.56</td><td>0.14</td><td>0.60</td><td>0.31</td></tr><tr><td>Min exp. loss</td><td>1.00</td><td>0.27</td><td>0.09</td><td>0.53</td><td>0.00</td><td>0.13</td><td>0.04</td><td>0.33</td><td>0.32</td><td>0.48</td><td>0.00</td><td>0.04</td><td>0.85</td></tr><tr><td>Min CVaR</td><td>1.00</td><td>0.79</td><td>0.00</td><td>1.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.40</td><td>0.43</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.37</td></tr></table>

## 7. Discussion

## 7.1. Contributions to Literature and Practice

Business process risk management has received increasing attention in recent years, because of corporate scandals, e.g., UBS rogue trader scandal (Murphy 2011); Olympus scandal (Bacani 2011, p. 3) and legislative mandates, e.g., Sarbanes-Oxley Act and Basel II. However, the disciplines of business process management and risk management remain largely disjoint (Conforti et al. 2011). Although conceptual models of process risk management have been proposed (e.g., zur Muehlen and Ho 2005, zur Muehlen and Rosemann 2005), formal approaches and theoretically sound methodologies and tools to manage process related risks need further development. Our work contributes to the BPM literature by formally integrating data risk management with business process modeling and analysis.

The information flow perspective of business processes has been extensively studied in the business processes modeling and analysis literature, such as workflow data patterns (Russell et al. 2004), data flow anomalies (Sun et al. 2006), and interactions among information elements (Basu and Blanning 2000). Our paper focuses on managing risks associated with errors introduced into the information flow of a business process. The methodology developed in our paper provides a formal framework for the quantitative analysis of data error risks in information flows and identifying optimal control resources allocation strategies for risk mitigation. The focus on formal risk analysis distinguishes our work from prior research on information flows in business processes.

Research on workflow resource patterns (Russell et al. 2005) has studied the various ways in which resources are represented and utilized in workflows. For example, the capability-based distribution pattern states that work items (tasks) can be distributed to resources based on their specific capabilities recorded in the associated organizational model, such as degree, certification, and experiences. Our work demonstrates that the topology of a process model impacts the economic consequences of data errors and sources of multiple data errors are critical control locations. By incorporating both the topology of the process and the location and data error probabilities of process tasks, our work extends workflow resource pattern research.

Our work has important practical implications for incorporating risk modeling into different phases of the BPM lifecycle. During the process design phase, our approach requires explicit modeling of data risks based on historical logs. This identifies tasks that are of high potential risk and enables process managers to consider design modifications that incorporate control procedures that provide mandatory additional data verification and checking. During the process enactment phase, data error risks at different tasks can be updated dynamically based on new process data so that simulations can be conducted continuously to enable process managers to better allocate control resources. During the process diagnosis phase, data error risks can be monitored so that process managers can take proactive actions to prevent future loss, e.g., if more data errors are detected in certain tasks during a period of time, the system can alert the process manager to the situation so that she or he can find the root causes of the anomaly and take proper actions, such as assigning more experienced staff to handle the task and/or redesigning process forms to reduce data entry errors.

## 7.2. Limitations

This study has three limitations. First, the four conditions listed in §5 are necessary conditions for the closed-form solutions of (P1) and (P2). The purpose of these conditions is to provide structural results of our model, which can then lead to insights into the impact of the structural factor, ceteris paribus, on the optimal control allocation. In practical settings, these conditions may not hold, and optimal solutions exist only in numerical forms. Second, the process models we studied herein are assumed to be well structured. Although well-structured processes support all five basic workflow patterns (see Figure 2) and can represent most commonly used transactional processes (Laue and Mendling 2010), our proposed model cannot be directly applied to processes with complex structural patterns (Russell et al. 2006) or unstructured processes (Liu and Kumar 2005). Future work should examine how complex process patterns affect data error propagation and influence overall process risk and control allocation strategies. New quantitative means of modeling risks in unstructured processes need to be further explored and developed. Third, applying our modeling approach to process models in application contexts other than the one we studied can be used both to validate the approach as well to create a new set of research problems at the intersection of risk and process management.

## 8. Conclusion

We have proposed a process modeling–based methodology for managing risks associated with data errors in the information flow of business processes. Our methodology focuses on the structural aspect of business processes in error propagation and optimal control resource allocation. The optimization formulation of our model treats both expected loss and the high losses (i.e., CVaR) as risk management objectives. We demonstrate the utility of our model through a case of an order-fulfillment process. The computational results show that our model is able to identify optimal control allocation strategies for different risk management objectives of a business process. Our methodology provides an effective and viable means of managing the risks associated with data errors in the process information flow. It also lends itself to implementations within process workbenches and adds analytical rigor to existing process modeling tools.

The modeling framework we proposed is well suited to application in corporate settings. In these settings, stability in the process parameters can be expected because of a fairly large and stable volume of transactions over time and when monitoring logs are required and their reliability is certified by external companies. The parameters of the optimization model, including transition probabilities, error probabilities, loss because of errors, control cost and effectiveness, and transaction volumes, are regularly assessed and readily available from periodic performance reports. They can be calibrated with reasonable confidence using historical data and monitoring logs. The implementation of our methodology in practice involves three steps: model parameterization through historical work logs; identification of the optimal control resource allocation strategy for budget and risk constraints, given the parameter estimates; and scenario analyses through parameter manipulation. We optimally solve the problem formulations in our study in step 2 by taking the error introduction probabilities as given or obtainable from the data. In such a case, the error generation process does not affect the optimal solution. However, if a firm wants to conduct scenario analyses at a process design phase, as in step 3, the model requires a statistical sampling process to generate error instances that can reasonably approximate the error structure estimated from the work logs. The effectiveness of the optimal policies can be tested by replicating our analysis in what-if scenarios.

Our work can be extended in multiple directions. The prototype system developed can be refined and enhanced to provide better support for risk-aware process modeling and analysis. In particular, the simulation functions of MATLAB can be integrated into the process modeling tool via MATLAB APIs so that process risk specification, risk analysis, and control resources allocation are conducted in an integrated environment. The sensor-based approach (see Conforti et al. 2011) can be adopted to capture and monitor data errors and to adjust control resource allocation strategies accordingly in real time. Our work can be leveraged to extend existing dynamic task assignment mechanisms (see Reijers et al. 2007) to achieve risk-aware task assignments. For example, according to our approach, different tasks in a process have different risk levels and require different amounts of control resources. At the same time, different organizational resources, such as auditors, have different levels of expertise. Therefore, intelligent algorithms can be designed to identify and select resources with the most appropriate experience for tasks with high potential risk, to reduce overall process risk. Finally, when our methodology is implemented and deployed, process risks can be monitored to provide insights into process decision making, such as risk-reduction-oriented process redesign and employee performance evaluation, based on the number of data errors they generate.

## Supplemental Material

Supplemental material to this paper is available at http://dx .doi.org/10.1287/isre.1120.0450.

## References

Acerbi C (2002) Spectral measures of risk: A coherent representation of subjective risk aversion. J. Banking Finance 26(7):1505–1518.

Bacani C (2011) Olympus scandal: Bye, old guard, hello 0 0 0 old guard? CFO Innovation Asia (October 31).

Basu A, Blanning RW (2000) A formal approach to workflow analysis. Inform. Systems Res. 11(1):7–36.

Basu A, Kumar A (2002) Research commentary: Workflow management issues in e-business. Inform. Systems Res. 13(1):1–14.

Berger J (1980) Statistical Decision Theory: Foundations, Concepts, and Methods (Springer-Verlag, New York).

Cobb CW, Douglas PH (1928) A theory of production. Amer. Econom. Rev. 18(1):139–165.

Conforti R, Fortino G, La Rosa M, Ter Hofstede AHM (2011) History-aware, real-time risk detection in business processes. On the Move to Meaningful Internet Systems, Lecture Notes in Computer Science, Vol. 7044 (Springer-Verlag, Berlin), 100–118.

Corbett RB (2004) A view of the future of risk management. Risk Management 6(3):51–56.

De Lusignan S (2009) Improving data quality and clinical records: Lessons from the UK National Programme about structure, process and utility. Luzar-Stiler V, Jarec I, Bekic Z, eds. Proc. 31st Internat. Conf. Inform. Tech. Interfaces (University of Zagreb, Univesity Computing Centre–SRCE, Zagreb, Croatia), 13–14.

Duffie D, Pan J (1997) An overview of value at risk. J. Derivatives 4(3):7–49.

Duffie D, Singleton KJ (2003) Credit Risk: Pricing, Measurement, and Management (Princeton University Press, Princeton, NJ).

English L (2009) Information quality tipping point: Plain English about information quality. Proc. ITI 2009 31st Int. Conf. Inform. Technology Interfaces, June 22–25, 2009, Cavtat, Croatia, 13–14.

Enterprise Risk Management Committee (2003) Overview of enterprise risk management. Casualty Actuarial Society, http:// www.casact.org/area/erm/overview.pdf.

Forster M, Bailey C, Brinkhof MWG, Graber C, Boulle A, Spohr M, Balestre E, May M, Keiser O, Jahn A (2008) Electronic medical record systems, data quality and loss to follow-up: Survey of antiretroviral therapy programmes in resource-limited settings. Bull. World Health Organ. 86(12):939–947.

Hammer M, Champy JA (1993) Reengineering the Corporation: A Manifesto for Business Revolution (HarperCollins, New York).

Hee KMv, Reijers HA (2000) Using formal analysis techniques in business process redesign. Business Process Management, Lecture Notes in Computer Science, Vol. 1806 (Springer-Verlag, Berlin), 142–160.

ISACA (2007) Control Objectives for Information and Related Technology (COBIT). ISACA & IT Governance Institute, Rolling Mendows, IL.

J. P. Morgan & Company (1996) RiskMetrics—Technical Document, 4th ed. (Morgan Guaranty Trust Company, New York).

Kiepuszewski B, Ter Hofstede AHM, Bussler C (2000) On structured workflow modelling. Wangler B, Bergman L, eds. Proc. 12th Int. Conf. Adv. Inform. Systems Engrg., Stockholm, Sweden, 431–445.

Kohn LT, Corrigan JM, Donaldson MS (2000) To err is human: Building a safer health system. A report of the Committee on Quality of Health Care in America. Committee on Quality of Health Care in America, Institute of Medicine, http://books .nap.edu/openbook.php?record\_id=9728.

Krishnan R, Peters J, Padman R, Kaplan D (2005) On data reliability assessment in accounting information systems. Inform. Systems Res. 16(3):307–326.

Laue R, Mendling J (2010) Structuredness and its significance for correctness of process models. Inform. Systems E-Bus. Management 8(3):287–307.

Lea RB, Adams SJ, Boykin RF (1992) Modeling of the audit risk assessment process at the assertion level within an account balance. Auditing: J. Practice Theory 11(Supplement):152–179.

Liu D, Wang J, Chan S, Sun J, Zhang L (2002) Modeling workflow processes with colored Petri nets. Comput. Indust. 49(3):267–281.

Liu R, Kumar A (2005) An analysis and taxonomy of unstructured workflows. Proc. 3rd Internat. Conf. Bus. Process Management, Nancy, France, 268–284.

Liu R, Kumar A, Van der Aalst W (2007) A formal modeling approach for supply chain event management. Decision Support Systems 43(3):761–778.

Marinos G (2004) Data quality: A risk-based approach. Inform. Management (August 1), http://www.information -management.com/issues/20040801/1007208-1.html?zkPrintable= 1&nopagination=1.

Mausser H, Rosen D (1999) Beyond VaR: Triangular risk decomposition. Algo Res. Quart. 2(1):31–43.

Mendling J, Lassen K, Zdun U (2008) On the transformation of control flow between block-oriented and graph-oriented process modelling languages. Internat. J. Bus. Process Integration and Management 3(2):96–108.

Murphy M (2011) UBS trader Adoboli held over US\$2 bn loss. Financial Times (September 15).

Olson JE (2003) Data Quality: The Accuracy Dimension (Morgan Kaufmann, Burlington, MA).

Object Management Group (2011a) UML Specification, http://www .omg.org/spec/UML/2.4.l/.

Object Management Group (2011b) Business Process Model and Notation Specification, http://www.omg.org/spec/BPMN/ 2.0/.

Pasley K (2002) Protecting financial information: Sarbanes-Oxley. SOA Compliance Whitepaper, http://www.compliancehome .com/whitepapers/SOX/abstract10846.html.

Pflug GCh (2000) Some remarks on the value-at-risk and the conditional value-at-risk. Uryasev S, ed. Probabilistic Constrained Optimization: Methodology and Applications (Kluwer Academic Publishers, Dordrecht, The Netherlands).

Reijers H, Jansen-Vullers M, zur Muehlen M, Appl W (2007) Workflow management systems + swarm intelligence = dynamic task assignment for emergency management applications.

Alonso G, Dadam P, Rosemann M, Proc. 5th Internat. Conf. Bus. Process Management (Springer-Verlag, Berlin, Heidelberg).

Richter A (2007) The high cost of clean data. http://www.cfo.com/ article.cfm/9705501/c\_2984274/?f=archives.

Rockafellar RT, Uryasev S (2000) Optimization of conditional valueat-risk. J. Risk 2(3):21–42.

Rockafellar RT, Uryasev S, Zabarankin M (2006a) Generalized deviations in risk analysis. Finance and Stochastics 10(1):51–74.

Rockafellar RT, Uryasev S, Zabarankin M (2006b) Optimality conditions in portfolio analysis with general deviation measures. Math. Programming 108(2):515–540.

Russell N, Ter Hofstede AHM, Van der Aalst W, Mulyar N (2006) Workflow control-flow patterns: A revised view. BPM Center Report BPM-06-22, BPMcenter.org, 06–22.

Russell N, Ter Hofstede AHM, Edmond D, Van der Aalst WMP (2004) Workflow data patterns. QUT Technical report, FIT-TR-2004-01, Queensland University of Technology, Brisbane, Australia.

Russell N, Van der Aalst WMP, Ter Hofstede AHM, Edmond D (2005) Workflow resource patterns: Identification, representation and tool support. Pastor O, Falcão e Cunha J, eds. Proc. 17th Internat. Conf. Adv. Inform. Systems Engrg., Porto, Portugal.

Sadiq W, Orlowska ME (2000) Analyzing process models using graph reduction techniques. Info. Systems 25(2):117–134.

Scheer A-W (2000) ARIS—Business Process Modeling (Springer, Berlin, Heidelberg).

Stein HD, Nadkarni P, Erdos J, Miller PL (2000) Exploring the degree of concordance of coded and textual data in answering clinical queries from a clinical data repository. J. Amer. Medical Informatics Assoc. 7(1):42–54.

Strong DM, Lee YW, Wang RY (1997) 10 Potholes in the road to information quality. IEEE Comput. 30(8):38–46.

Sun SX, Zhao JL, Nunamaker JF, Sheng ORL (2006) Formulating the data flow perspective for business process management. Inform. Systems Res. 17(4):374–391.

Van der Aalst WMP (1998) The application of Petri nets to workflow management. J. Circuits, Systems Comput. 8(1):21–66.

Van der Aalst WMP (2000) Workflow verification: Finding controlflow errors using Petri-net-based techniques. Business Process Management: Models, Techniques, and Empirical Studies, Lecture Notes in Computer Science, Vol. 1806 (Springer-Verlag, Berlin), 161–183.

Van der Aalst WMP, Ter Hofstede AHM (2005) A YAWL: Yet another workflow language. Inform. Systems 30(4):245–275.

Van der Aalst WMP, Ter Hofstede AHM, Kiepuszewski B, Barros AP (2003) Workflow patterns. Distributed and Parallel Databases 14(3):5–51.

Van Dongen B, Jansen-Vullers M, Verbeek H, Van der Aalst WMP (2007) Verification of the SAP reference models using EPC reduction, state-space analysis, and invariants. Comput. Indust. 58(6):578–601.

Varian HR (1992) Microeconomic Analysis (W. W. Norton & Company, New York).

Wand Y, Weber R (1989) A model of control and audit procedure change in evolving data processing systems. The Accounting Rev. 64(1):87–107.

Wang J, Chaudhury A, Rao HR (2008) A value-at-risk approach to information security investment. Inform. Systems Res. 19(1):106–120.

Zhao JL, Brown GW, Carey MJ, Kumar A, Spohrer JC, Tanniru M (2005) Services science: Services innovation research and education. Chang CK, Zhang LJ, eds. Proc. 2005 IEEE Internat. Conf. Services Comput. (IEEE Computer Society, Los Alamitos, CA).

zur Muehlen M, Ho D (2005) Risk management in the BPM lifecycle. Bussler CJ, Haller A, eds. Proc. Workshop Bus. Process Design (Springer-Verlag, Berlin, Heidelberg), 454–466.

zur Muehlen M, Rosemann M (2005) Integrating risks in business process models. Campbell B, Underwood J, Bunker D, eds. Proc. Australasian Conf. Inform. Systems (Assoc. Inform. Systems, Atlanta), 1–10.

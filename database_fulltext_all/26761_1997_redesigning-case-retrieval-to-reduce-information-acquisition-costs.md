---
otero_id: 26761
otero_key: "F4ZBG5YY"
title: "Redesigning Case Retrieval to Reduce Information Acquisition Costs"
authors: "Vijay S. Mookerjee; Michael V. Mannino"
year: "1997"
journal: "Information Systems Research"
doi: "10.1287/isre.8.1.51"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR Information Systems Research

![](/api/attachments/F4ZBG5YY/fulltext/images/a78166e989c2a3573ec7ab968d9942f52975ed6f462d63882766c5a2be7d34bc.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Redesigning Case Retrieval to Reduce Information Acquisition Costs

Vijay S. Mookerjee, Michael V. Mannino,

## To cite this article:

Vijay S. Mookerjee, Michael V. Mannino, (1997) Redesigning Case Retrieval to Reduce Information Acquisition Costs. Information Systems Research 8(1):51-68. http://dx.doi.org/10.1287/isre.8.1.51

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article's accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1997 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/F4ZBG5YY/fulltext/images/962053fe218958336cda46df70281508b6ca395d75327efdb63a8a34ead8f38f.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Redesigning Case Retrieval to Reduce Information Acquisition Costs

Vijay S. Mookerjee • Michael V. Mannino

Department of Management Science, DJ-10, University of Washington, Seattle, Washington 98195
mookerje@u.washington.edu
zmann@u.washington.edu

Retrieval of a set of cases similar to a new case is a problem common to a number of machine learning approaches such as nearest neighbor algorithms, conceptual clustering, and case based reasoning. A limitation of most case retrieval algorithms is their lack of attention to information acquisition costs. When information acquisition costs are considered, cost reduction is hampered by the practice of separating concept formation and retrieval strategy formation.

To demonstrate the above claim, we examine two approaches. The first approach separates concept formation and retrieval strategy formation. To form a retrieval strategy in this approach, we develop the $CR_{lc}$ (case retrieval loss criterion) algorithm that selects attributes in ascending order of expected loss. The second approach jointly optimizes concept formation and retrieval strategy formation using a cost-based variant of the ID3 algorithm ( $ID3_{c}$ ). $ID3_{c}$ builds a decision tree wherein attributes are selected using entropy reduction per unit information acquisition cost.

Experiments with four data sets are described in which algorithm, attribute cost coefficient of variation, and matching threshold are factors. The experimental results demonstrate that (i) jointly optimizing concept formation and retrieval strategy formation has substantial benefits, and (ii) using cost considerations can significantly reduce information acquisition costs, even if concept formation and retrieval strategy formation are separated.

(Case Based Systems; Case Retrieval Algorithms; Information Costs; Cost Reduction; Joint Versus Separate Optimization)

## 1. Introduction

In recent years, large databases of cases have become an important part of many inductive expert systems. A number of machine learning approaches using case histories have been proposed including nearest neighbor algorithms (Aha et al. 1991), conceptual clustering (Gennari et al. 1989), and case based reasoning (Kolodner 1991). Usage of these algorithms is reported in areas such as industry and occupation code classification (Creecy et al. 1992), real estate appraisal (Gonzalez and Laureano-Ortiz 1992), market surveillance (Barletta and Buta 1991), assembly planning (Zarley 1991), and sales prediction (Stottler 1994).

We motivate the problem studied here with an example of a case based system designed to support customers with problems using a backup tape drive for a personal computer (see Figure 1). This hypothetical system is similar to reported help desks for the VMS operating system (Simoudis 1992) and personal computer software (Breese and Heckerman 1995). The first step in developing the system is to cluster the cases into categories to identify faults such as "Incomplete Installation," "Incompatible Driver," "Incompatible Parallel Port," and "Tape Drive Malfunction." Solutions recorded for cases in the "Incomplete Installation" cluster could include "Reinstall Tape Drive Software" and "Reconfigure Tape Drive Software." The second step is to form concepts for each cluster. Concept formation generates functions or concept definitions that assign new cases to clusters. For example, the concept definition for the "Incomplete Installation" cluster may use rules with attributes such as Operating\_System\_Version, Tape\_Drive\_Version, Loads\_Ok, and Menu\_Missing.

Figure 1 Case Based Systems For Tape Drive Help Desk  
![](/api/attachments/F4ZBG5YY/fulltext/images/5ccedc0f1388c7f43c67d2ebfe4819e5e72c6bc1dbaddb0c07b1ac16a087cef3.jpg)

The final step in developing the help desk is to determine a retrieval strategy that specifies how information should be collected. A retrieval strategy may be represented as a total order or a context (a partial order). A total order is a list of attributes to collect. For example, a total order is: Tape\_Drive\_Version, Loads\_Ok, and Menu\_Missing. A context is a decision tree in which the next attribute collected depends on the values observed for the previous attributes. For example, a context is: first collect Loads\_Ok, then collect Menu\_Missing if Loads\_Ok is true, else collect Tape\_Drive\_Version.

The support engineer at the help desk may query a user until a matching cluster of cases can be identified. The system would retrieve the most similar cases in the cluster that match the new case. The engineer would then adapt the solutions to determine appropriate actions. Adaptation is typically left to the user because humans have been found to be better than computers at adapting cases to solve new problems (Kolodner and Simpson 1989, Allen 1994). After determining the solution for the new case, the system may add unique cases and solutions to the case base for future consulting use.

The tape drive example is typical of a case based system that involves sequential decision making. When a user calls about a problem, the details are not known until a support engineer asks questions and conducts diagnostic probes. Some attributes such as the software version and tape drive model are easy to obtain. Other attributes such as asking the user to check for a parallel port conflict may be more difficult. Still other attributes may involve the support engineer logging onto the remote system to generate diagnostic information.

Help desks are a special case of troubleshooting where the goal is to repair a faulty device such as an automobile engine or commercial software. Case based systems are increasingly being used for troubleshooting applications because previous cases are a good explanatory tool and case bases can be easier to develop and maintain than rule based systems (Allen 1994). Reports of case based systems for troubleshooting are described in (Simoudis 1992, Breese and Heckerman 1995, Heckerman et al. 1995).

In this paper, we are concerned with concept and retrieval strategy formation. Specifically, we examine the practice of forming the retrieval strategy for a given set of concepts. The most important contribution of the paper is to demonstrate that jointly optimizing the tasks of concept formation and retrieval is superior to optimizing the retrieval strategy independent of the concepts. To our knowledge, this is the first study that clearly demonstrates this design limitation in existing case retrieval algorithms. The alternative presented here, the $ID3_{c}$ algorithm, jointly develops concept definitions and a retrieval strategy in the form of a decision tree. Attributes in the decision tree are selected based on entropy reduction per unit information acquisition cost.

The second contribution of this paper is to demonstrate that information acquisition costs can be significantly reduced even if concept formation and retrieval strategy formation are separated. For the second contribution, we develop the $CR_{lc}$ (case retrieval loss criterion) algorithm that finds a retrieval strategy using the notion of the expected loss of an attribute. The expected loss of an attribute is the probability of unnecessarily collecting an attribute times its information acquisition cost.

The rest of this paper is organized as follows. Section 2 reviews research on the economics of case based systems and expert systems. Section 3 discusses approaches that separate concept formation and retrieval strategy formation. Section 4 describes joint concept formation and retrieval strategy formation. Section 5 reports on experiments comparing the different case retrieval approaches. Section 6 summarizes the paper and discusses future research directions.

## 2. Economics of Case Based Systems

In this section, we review research on economic considerations in expert systems and discuss how the economic performance of a case based system may be measured.

2.1. Economic Considerations in Previous Research Although most research on Case Based Systems emphasizes computational efficiency and accuracy, attention has recently been paid to reducing information acquisition costs. Simoudis (1992) has developed a retrieval procedure for help-desk retrieval problems. This procedure has two limitations that may lead to higher information acquisition costs than necessary. First, the usefulness of a costly attribute is not measured across a set of potentially matching cases. Second, the retrieval procedure separates concept formation from retrieval strategy formation. The significance of the second limitation will be demonstrated later. Several other studies have used retrieval processes with similar limitations (Hammond 1986, Koton 1988).

Although economic considerations are uncommon in the Case Based Systems area, they are more prevalent in other kinds of expert systems. Moore and Whinston (1986, 1987) have proposed a decision theoretic framework, applicable to a variety of deductive expert systems. For rule-based expert systems, the focus has been to reduce information costs without affecting decision making performance (Pattipati and Alexandridis 1992, Dos Santos and Mookerjee 1993). Similar objectives have been used to develop a retrieval strategy for Bayesian Belief Networks (Breese and Heckerman 1995, Heckerman et al. 1995). For inductive expert systems, both cost minimization (Nunez 1991) and value maximization (Mookerjee and Dos Santos 1993) have been attempted.

## 2.2. Measuring Economic Performance

From an economic standpoint, a Case Based System may be evaluated in terms of its expected cost to support problem solving. This cost is the sum of two costs: (i) expected information acquisition costs and (ii) expected classification cost. Information acquisition cost only includes the direct costs of supplying attributes requested by the system to retrieve a set of similar cases. It excludes the costs of constructing the case base because such costs are fixed, more typically associated with knowledge engineering. The expected classification cost is the sum of the expected cost of correct and incorrect assignment of cases to clusters.

The use of classification costs in evaluating a case based system is quite complex. After a case is assigned to a cluster, two activities occur before the case can be solved. First, a set of most similar cases is chosen from the cluster. Second these cases are adapted by the user to solve the problem. Since two nonidentical cases can be assigned to the same cluster, the two sets of most similar cases may be different. Even if the most similar sets are identical, the adaptation process can lead to different solutions. Due to these complications, assignment to the same cluster does not ensure the same solution. Hence the eventual costs of correct and incorrect assignments can be difficult to assess.

Given the difficulties in specifying classification costs, we use expected classification accuracy as a measure of system performance. Expected classification accuracy is estimated by the proportion of correct assignments made by the system in a sample of unseen cases. An external source, such as an expert, determines if an assignment is correct.

From the preceding discussion, two distinct measures of system performance emerge: (i) information acquisition cost, and (ii) classification accuracy. In this study, we attempt to reduce expected information acquisition costs without sacrificing classification accuracy.

Table 1 Input Attributes and Descriptions

<table><tr><td>Attribute Name</td><td>Description</td></tr><tr><td>Operating_System</td><td>Multi-valued</td></tr><tr><td>Tape_Drive_Model</td><td>Multi-valued</td></tr><tr><td>Backup_Software_Version</td><td>Multi-valued</td></tr><tr><td>Loads_Ok</td><td>Boolean</td></tr><tr><td>Menu_Missing</td><td>Boolean</td></tr><tr><td>Drive_Recognized</td><td>Yes, No, Partial</td></tr><tr><td>Port_Conflict</td><td>Boolean</td></tr><tr><td>Bi-directional_Port</td><td>Boolean</td></tr></table>

## 3. Separation of Concept Formation and Retrieval

In this section, we present background on concept formation in Case Based Systems. This discussion is followed by a definition of the case retrieval problem. We then present two heuristic solutions to this problem: $CR_{f}$ , the baseline algorithm for the study, and $CR_{lc}$ , the loss criterion algorithm.

## 3.1. Concept Formation

Concept formation or case indexing as it is sometimes referred to (Kolodner 1991), is the problem of organizing cases to enable the efficient retrieval of similar cases. In many case based systems, the concept definition for a cluster is referred to as the norm of the cluster. A norm consists of a set of attribute-value pairs. A cluster and its norm are referred to as a node.

An attribute-value pair in a norm is usually selected using two probabilities (Kolodner 1991, Becker 1973, Hall 1989): (i) predictive probability, and (ii) predictable probability. These probability measures have been used in a number of working systems such as EPAM (Feigenbaum 1963), UNIMEM (Lebowitz 1987), COB-

WEB (Fisher 1987), CLASSIT (an extension of COBWEB) (Gennari et al. 1989), and Mediator (Kolodner and Simpson 1989).

The predictive probability can be denoted by $P(N_{k}|A_{i}=v_{ij})$ , where $A_{i}$ is an attribute, $v_{ij}$ is the jth state of the attribute, and $N_{k}$ is the kth node. The predictive probability of an attribute-value pair is estimated by the number of cases of a node matching the pair divided by the total number of cases of the node. Thus, a predictive probability of 1 means that all cases with this attribute value belong to the node.

The predictable probability can be denoted by $P(A_{i} = v_{ij} | N_{k})$ . This probability is estimated as the number of cases at a node matching the attribute-value pair divided by the number of cases across all nodes matching the attribute-value pair. Thus, a predictable probability of 1 means that every case of the node has this value for the attribute.

The probability measures for an attribute-value pair must exceed specified construction thresholds to be used in a norm. For example, a construction threshold of 0.67 for the predictable probability is used in Mediator (Kolodner and Simpson 1989). Construction thresholds are similar in purpose to pruning in decision tree induction. Pruning leads to more general rules (that is, rules with fewer attribute-value pairs) that often have higher classification accuracy than specialized rules.

We extend the tape drive example described in the introduction to demonstrate norm formation. Table 1 shows a number of attributes that may be useful in diagnosing a tape drive problem. Hypothetical predictable and predictive probability measures for some attribute-value pairs are shown in Table 2.

Let us assume that construction thresholds of 0.67 are used for both the predictive and predictable probabilities. Applying these thresholds to the “Incomplete

Table 2 Predictive and Predictable Probability Measures for Two Nodes

<table><tr><td>Incomplete Installation (II) P(value|II); P(II|value)</td><td>Incompatible Driver (ID) P(value|ID); P(ID|value)</td></tr><tr><td>Loads_Ok = No [0.70; 0.90]</td><td>Loads_Ok = Yes [0.99; 0.30]</td></tr><tr><td>Menu_missing = Yes [0.68; 0.90]</td><td>Menu_missing = No [0.99; 0.10]</td></tr><tr><td>Drive_Recognized = No [0.80; 0.30]</td><td>Drive_Recognized = Partial [0.95; 0.67]</td></tr><tr><td>Port_Conflict = No [0.20; 0.20]</td><td>Port_Conflict = Yes [0.70; 0.75]</td></tr><tr><td>Bi-directional_Port = Yes [0.5; 0.1]</td><td>Bi-directional_Port = No [0.85; 0.50]</td></tr></table>

Installation" node, we reject the attribute-value pairs Drive\_Recognized = No, Port\_Conflict = No, and Bi-directional\_Port = Yes. Thus the norm for "Incomplete Installation" is represented by the following conjunction of attribute-value pairs: [Loads\_Ok = No, Menu\_missing = Yes]. Similarly the norm for the "Incompatible Driver" node is: [Drive\_Recognized = Partial, Port\_Conflict = Yes].

## 3.2. Case Retrieval Problem

The case retrieval problem involves finding an optimal information acquisition order. An information acquisition order consists of two orders: a node order and a set of attribute orders, one for each node. A node order specifies the sequence in which nodes should be considered for matching. An attribute order specifies the sequence in which norm attributes should be collected to match the norm. An optimal information acquisition order has the least expected cost among all possible orders. More precisely, the case retrieval problem is defined as:

## Objective

Minimize EAC(S, N, η, α, f, Cost) where $\alpha,\eta$

EAC(S, N, η, α, f, Cost) is the expected attribute acquisition cost,

$S$ is a set of cases,

$N$ is a set of nodes,

$\eta$ is a node order,

$\alpha$ is a set of attribute orders,

$f$ is a matching function; $f$ maps a case and a norm to a Boolean,

Cost is a function; Cost maps an attribute to its attribute acquisition cost

Comment 1. The above model does not include classification accuracy in either the objective function or constraints. If norms do not overlap, then the information acquisition order will not affect classification accuracy. Two norms overlap if there are cases that can match both norms. However, even with overlapping norms, the order does not typically affect classification accuracy. In a later section, we experimentally observe that a cost based ordering has a slightly positive impact on classification accuracy. Since this impact is not substantial, the impact of information acquisition order on classification accuracy is ignored.

Comment 2. The specific matching function (f) used in this study is known as X of N (Hanson and Bauer 1986). In X of N matching, a node is matched if at least X of N terms in the norm match the attribute-value pairs of the case. The search continues to the next node in the order when less than X attribute-value pairs match the current norm. The search terminates unsuccessfully if all nodes are searched without a match. The value X divided by N is known as the matching threshold. $^{1}$

Comment 3. The solution space for this problem is much too large to enumerate. A feasible solution consists of a node order and a set of attribute orders. If there are p nodes and q attributes per norm, then there are p! node orders and for each node, there are q! attribute orders. Hence, there are a total of $(q!)^{p}(p!)$ feasible solutions.

In §§3.3 and 3.4, we describe two heuristic algorithms (CR $_{f}$ and CR $_{lc}$ ) to determine a good information acquisition order. These algorithms assume: (i) attribute acquisition costs are independent, and (ii) nodes are non-hierarchical and mutually exclusive. Each algorithm has two phases, one to construct the node order and the other to construct the set of attribute orders. Before presenting the algorithms, we introduce some basic notation.

## Notation

$N_{m}\in N$ : node $m,m = 1,\dots ,p,$

Freq $(N_{m})$ : number of cases in the cluster at node $N_{m}$

$\mathrm{TC} = \Sigma_{m=1}^{p} \operatorname{Freq}(N_m)$ : total number of cases in the clusters,

Norm $(N_{m})$ : Norm is a function that provides the norm of a node,

$A_{j}\in A$ : jth attribute, $j = 1,\dots ,n$

Attrs(Norm( $N_m$ ): Attrs is a function that provides the set of attributes in the norm of a node,

Stage $i$ : a condition when $i$ nodes have been selected, $i = 0, \ldots, p - 1$ ,

NR(i): set of nodes remaining at stage i,

NC(i): set of nodes chosen in previous stages, $\forall i(\mathrm{NR}(i) \cup \mathrm{NC}(i)) = N.$

## 3.3. The $\mathbf{CR}_{\mathrm{f}}$ Algorithm

The $CR_{f}$ algorithm uses two simple heuristics to order the nodes and attributes within a node. Nodes are sorted in descending order by the number of cases at the node. The first node searched is the one with the most cases and hence the most likely to match a new case. Within each node, norm attributes are sorted in the descending order of predictable probability. Thus, the first attribute acquired is the one most likely to match a case if the case is a member of the node. In the $CR_{f}$ algorithm, the next node and attribute are selected using the node frequency selection heuristic (NFSH) and the attribute frequency selection heuristic (AFSH).

$$
\operatorname{NFSH} (i) = \underset {m} {\operatorname{Max}} (\operatorname{Freq} (N _ {m})), \quad N _ {m} \in \operatorname{NR} (i),\tag{1}
$$

$$
\operatorname{AFSH} (i, N _ {m}, \alpha) = \underset {j} {\operatorname{Max}} (\operatorname{ASP} (A _ {j}, N _ {m}, i)),
$$

$$
A _ {j} \in \operatorname{AR} (N _ {m}, \alpha) \quad \text { where }\tag{2}
$$

$\alpha$ : is the set of attributes that have already been selected in the norm of node $m$ , $\mathrm{AR}(N_m, \alpha)$ : the set of remaining (not selected) attributes = $\text{Attrs}(\text{Norm}(N_m)) - \alpha$ .

ASP( $A_{j}, N_{m}, i$ ) is the attribute stage probability of attribute $A_{j} \in \text{Attrs}(\text{Norm}(N_{m}))$ at stage $i = P[A_{j} = V | N_{m}]$ (the predictable probability) if $A_{j} \notin \text{Attrs}(\text{Norm}(N_{k}))$ , $N_{k} \in NC(i) = 1$ , otherwise.

The complexity of the $CR_{f}$ algorithm is governed by the complexity of sorting p nodes and sorting an average of q attributes per norm. Formally, the complexity is $O(p \log p + p (q \log q))$ , where the complexity of sorting n items is $n \log n$ .

The $CR_{f}$ algorithm is a simple and efficient one among those that do not use cost information. In addition, the retrieval strategy in the $CR_{f}$ algorithm approximates the search used in many case based systems, including COBWEB (Fisher 1987), MEDIATOR (Kolodner 1988), UNIMEM (Lebowitz 1987), etc. In these systems, the order in which nodes are searched depends on the frequency of cases in the nodes.

## 3.4. The $\mathbf{CR}_{\mathrm{lc}}$ Algorithm

Like the $CR_{f}$ algorithm, the $CR_{lc}$ algorithm heuristically computes a node order followed by an attribute order for each node. Unlike the $CR_{f}$ algorithm, it uses cost information to construct the orders. Another difference between $CR_{f}$ and $CR_{lc}$ is that $CR_{f}$ only considers how likely a match will occur at a particular node. $CR_{lc}$ , on the other hand, also considers how useful the attributes are to matching at other nodes.

The $CR_{lc}$ algorithm uses heuristics to greedily search for node and attribute orderings. Greedy means that node and attribute selections are irrevocable decisions, that is, there is no backtracking. At each step, the algorithm chooses the node (attribute) that minimizes the heuristic value. An optimal solution cannot be guaranteed by greedy search. Sometimes, choosing a node (attribute) with a larger heuristic value may lead to an lower overall cost than that of a greedy selection process.

Because of the detailed nature of the $CR_{lc}$ algorithm, we first present the node ordering component of $CR_{lc}$ followed by its attribute ordering component. For the node ordering component, we begin with the basic heuristic and then extend it to account for threshold matching. We then present the entire node ordering algorithm and analyze its computational complexity. Finally, we present the attribute ordering component.

3.4.1. Node Ordering. In $CR_{lc}$ , nodes are arranged in ascending order by a heuristic that we call the loss criterion. At the initial stage (that is, selecting the first node), the node with the smallest loss criterion value is selected. At the next stage, the loss criterion values of the remaining nodes are recomputed and the node with the lowest value is chosen. Thus for p nodes, there are p - 1 node selection stages. The loss criterion value of a node is the sum of its attribute loss criterion values times the probability that the node will not match (failure probability). The failure probability is one minus the node probability. The node probability is the number of cases in the node's cluster divided by the total number of cases.

The loss criterion of an attribute is its loss probability times its cost. The loss probability of an attribute is the probability of not needing the attribute to assign a case to a node. The cost of obtaining an attribute depends on the stage of ordering the nodes. The cost of obtaining an attribute at stage i is zero if the attribute was collected in a previous stage. Otherwise, the cost is the given attribute cost.

Formal definitions of the node loss criterion and attribute loss criterion are given below. We begin with some new notation:

NRE(A $_{j}$ , i): set of remaining nodes at stage i where the norm excludes A $_{j}$ = {N $_{m}$ |N $_{m}$ ∈ NR(i) ∧ A $_{j}$ ∈ Attrs(Norm(N $_{m}$ ))}.

Cost $(A_{j})$ : Cost is a function that provides the cost to collect attribute $A_{j}$ .

$\text{SCost}(A_j, i)$ : Scost is a function that provides the cost of acquiring attribute $A_j$ at stage $i = 0$ , if $A_j \in \cup_{N_m \in NC(i)} \text{Attrs}(\text{Norm}(N_m)) = \text{Cost}(A_j)$ otherwise.

$LC(N_{m}, i)$ : loss criterion of node $N_{m}$ at stage i (definition below).

ALC( $A_{j}, i$ ): loss criterion of attribute $A_{j}$ at stage $i$ (definition below).

ALP( $A_{j}, i$ ): loss probability of attribute $A_{j}$ at stage $i$ (definition below).

The loss criterion LC is formally defined as:

$$
\operatorname{LC} \left(N _ {m}, i\right) = \left[ 1 - \frac {\operatorname{Freq} \left(N _ {m}\right)}{\operatorname{TC}} \right] \sum_ {A _ {j} \in \operatorname{Attrs} \left(\operatorname{Norm} \left(N _ {m}\right)\right)} \operatorname{ALC} \left(A _ {j}, i\right),\tag{3}
$$

$$
\operatorname{ALC} (A _ {j}, i) = \operatorname{ALP} (A _ {j}, i) * \operatorname{SCost} (A _ {j}, i),\tag{4}
$$

$$
\mathrm{ALP} (A _ {j}, i) = \sum_ {N _ {m} \in \mathrm{NRE} (A _ {j, 1})} \frac {\operatorname{Freq} (N _ {m})}{\mathrm{TC}}.\tag{5}
$$

At stage i, the node ordering algorithm chooses the node that minimizes $\operatorname{LC}(N_{m}, i)$ for all nodes in the set $\operatorname{NR}(i)$ .

3.4.1.1. Example. To depict the loss criterion, consider the following hypothetical example with three nodes representing $N_{1} = "incomplete installation," N_{2} = "incompatible driver,"$ and $N_{3} = "tape drive failure."$ Assume that the attributes $A_{1}$ (Port\_Conflict) and $A_{5}$ (Bi-directional\_Port) are difficult to acquire. Low cost attributes are $A_{2}$ (Loads\_Ok), $A_{3}$ (Menu\_Missing), and $A_{4}$ (Drive\_Recognized). Calculation results and expressions for the loss criterion are shown below. In the first stage, $N_{3}$ is chosen because it has the lowest loss. In the second stage, only nodes $N_{1}$ and $N_{2}$ would be considered because node $N_{3}$ has already been selected. Note that $CR_{f}$ would select node $N_{2}$ in stage 1 because it has the highest frequency of cases.

$$
\begin{array}{c} \operatorname{Norm} (N _ {1}) = \{\langle A _ {1}, \text {True} \rangle , \langle A _ {2}, \text {False} \rangle \}, \\ \operatorname{Norm} (N _ {2}) = \{\langle A _ {1}, \text {False} \rangle , \langle A _ {4}, \text {True} \rangle \langle A _ {5}, \text {False} \rangle \}, \end{array}
$$

$$
\operatorname{Norm} (N _ {3}) = \{\langle A _ {2}, \text { False } \rangle , \langle A _ {3}, \text { True } \rangle \},
$$

$$
\operatorname{Freq} \left(N _ {1}\right) = 2 5, \quad \operatorname{Freq} \left(N _ {2}\right) = 4 5, \quad \operatorname{Freq} \left(N _ {3}\right) = 3 0,
$$

$$
\operatorname{Cost} (A _ {1}) = 2 0, \quad \operatorname{Cost} (A _ {2}) = 3,
$$

$$
\operatorname{Cost} (A _ {3}) = 5, \quad \operatorname{Cost} (A _ {4}) = 6, \quad \operatorname{Cost} (A _ {5}) = 8.
$$

The loss criterion for node 1 is

$$
\begin{array}{r l} \mathrm{LC} (N _ {1}, 0) & = [ \mathrm{ALP} (A _ {1}, 0) * \mathrm{SCost} (A _ {1}, 0) \\ & + \mathrm{ALP} (A _ {2}, 0) * \mathrm{SCost} (A _ {2}, 0) ] * [ 1 - \{\mathrm{Freq} (N _ {1}) / \mathrm{TC} \} ], \\ & \mathrm{ALP} (A _ {1}, 0) = \mathrm{Freq} (N _ {3}) / \mathrm{TC} = 0. 3; \\ & \mathrm{ALP} (A _ {2}, 0) = \mathrm{Freq} (N _ {2}) / \mathrm{TC} = 0. 4 5, \\ & \mathrm{LC} (N _ {1}, 0) = (0. 3 * 2 0 + 0. 4 5 * 3) * 0. 7 5 = 5. 5 1. \end{array}
$$

The loss criterion for node 2 is

$$
\begin{array}{r l} \mathrm{LC} (N _ {2}, 0) & = [ \mathrm{ALP} (A _ {1}, 0) * \mathrm{SCost} (A _ {1}, 0) \\ & + \mathrm{ALP} (A _ {4}, 0) * \mathrm{SCost} (A _ {4}, 0) \\ & + \mathrm{ALP} (A _ {5}, 0) * \mathrm{SCost} (A _ {5}, 0) ] \\ & \times [ 1 - \{\text {Freq} (N _ {2}) / \mathrm{TC} \} ], \end{array}
$$

$$
\mathrm{ALP} (A _ {1}, 0) = \operatorname{Freq} (N _ {3}) / \mathrm{TC} = 0. 3,
$$

$$
\begin{array}{l} \mathrm{ALP} (A _ {4}, 0) = \mathrm{Freq} (N _ {1}) / \mathrm{TC} + \mathrm{Freq} (N _ {3}) / \mathrm{TC} = 0. 5 5, \\ \mathrm{ALP} (A _ {5}, 0) = \mathrm{Freq} (N _ {1}) / \mathrm{TC} + \mathrm{Freq} (N _ {3}) / \mathrm{TC} = 0. 5 5, \\ \mathrm{LC} (N _ {2}, 0) = (0. 3 * 2 0 + 0. 5 5 * 6 + 0. 5 5 * 8) * 0. 5 5 = 7. 5 4. \end{array}
$$

The loss criterion for node 3 is

$$
\begin{array}{r l} \mathrm{LC} (N _ {3}, 0) & = [ \mathrm{ALP} (A _ {2}, 0) * \mathrm{SCost} (A _ {2}, 0) \\ & + \mathrm{ALP} (A _ {3}, 0) * \mathrm{SCost} (A _ {3}, 0) ] * [ 1 - \{\mathrm{Freq} (N _ {3}) / \mathrm{TC} \} ], \\ \mathrm{ALP} (A _ {2}, 0) & = \mathrm{Freq} (N _ {2}) / \mathrm{TC} = 0. 4 5, \end{array}
$$

$$
\begin{array}{r l} \mathrm{ALP} (A _ {3}, 0) & = \mathrm{Freq} (N _ {1}) / \mathrm{TC} + \mathrm{Freq} (N _ {2}) / \mathrm{TC} = 0. 7, \\ \mathrm{LC} (N _ {3}, 0) & = [ 0. 4 5 * 3 + 0. 7 * 5 ] * 0. 7 = 3. 4 0. \end{array}
$$

3.4.1.2. Threshold Matching. The attribute loss criterion defined in Equation (4) does not reflect the use of threshold matching in case retrieval. Recall that with threshold matching only a fraction of the norm attributes need be matched. Thus, even if an attribute is an element of a norm, it may not be needed to make a matching decision. The number of norm attributes and the matching threshold determine if an attribute is needed to make a matching decision. For example, if there are three norm attributes and the matching threshold is 0.66, then only two attributes are needed to make a matching decision.

Consider an attribute $A_{j}$ whose attribute loss criterion needs to be evaluated at stage i (ALC( $A_{j}, i$ )). There are two sets of nodes remaining at this stage: (i) those that do not contain $A_{j}$ , denoted by NRE( $A_{j}, i$ ), and (ii) those that contain $A_{j}$ , denoted by NRI( $A_{j}, i$ ). The probability of making a classification decision without needing $A_{j}$ is given by the sum of: (i) the probability of making a decision in the set NRE( $A_{j}, i$ ), and (ii) the probability of making a decision in the set NRI( $A_{j}, i$ ) without needing $A_{j}$ .

Let

$XE_{m}$ denote the event that a classification decision has been made at node $N_{m}$ in the set $\mathrm{NRE}(A_{j}, i)$ (that is, the matching threshold at the norm of the node $N_{m}$ has been exceeded),

$XI_{m}$ denote the event that a classification decision has been made at node $N_{m}$ in the set $\mathrm{NRI}(A_{j}, i)$ (that is, the matching threshold at the norm of node $N_{m}$ has been exceeded),

$$
\begin{array}{l} P (X E _ {m}) = \operatorname{Freq} (N _ {m}) / \mathrm{TC}; N _ {m} \in \operatorname{NRE} (A _ {j}, i), \\ P (X I _ {m}) = \operatorname{Freq} (N _ {m}) / \mathrm{TC}; N _ {m} \in \operatorname{NRI} (A _ {j}, i), \end{array}
$$

Y denote the event that the attribute $A_{j}$ has not been collected,

$PE =$ probability that a decision is made in the set $\mathrm{NRE}(A_{j},i)$ and $A_{j}$ is not collected

$$
\begin{array}{l} = P (X E _ {m} \cap Y) = P (X E _ {m}) * P (Y | X E _ {m}) = P (X E _ {m}); \\ \because P (Y | X E _ {m}) = 1, \end{array}
$$

$PI =$ probability that a decision is made in the set $\mathrm{NRI}(A_{j},i)$ and $A_{j}$ is not collected

$$
= P (X I _ {m} \cap Y) = P (X I _ {m}) * P (Y | X I _ {m}),
$$

$P(Y|XI_{m})$ is the probability that attribute $A_{j}$ is not needed given that the norm of the node $N_{m}$ is matched.

We estimate $P(Y \mid XI_{m})$ as the number of minimal conjunctions in $N_{m}$ that do not contain $A_{j}$ divided by the total number of minimal conjunctions in $N_{m}$ .² A conjunction is minimal if it does not contain any more attributes than the number required by the matching threshold. The set of these minimal conjunctions can be denoted by:

$\mathrm{CONJ}(A_{j}, N_{m}) = \{\mathrm{CONJ}_{q} | \mathrm{CONJ}_{q}$ is a minimal conjunction of the norm of node $N_{m}$ and $A_{j} \notin \mathrm{CONJ}_{q}\}$ , and $\mathrm{CONJ}(N_{m}) = \{\mathrm{CONJ}_{q} | \mathrm{CONJ}_{q}$ is a minimal conjunction of the norm of node $N_{m}\}$ .

Hence,

$$
\begin{array}{r l} P (Y \mid X I _ {m}) & = \mathrm{FRAC} (A _ {j}, N _ {m}) = \frac {\left| \mathrm{CONJ} (A _ {j} , N _ {m}) \right|}{\left| \mathrm{CONJ} (N _ {m}) \right|} \\ & = \frac {| \mathrm{Norm} (N _ {m}) | ^ {- 1} C _ {\lceil | \mathrm{Norm} (N _ {m}) | * \mathrm{MT} \rceil}}{| \mathrm{Norm} (N _ {m}) |} C _ {\lceil | \mathrm{Norm} (N _ {m}) | * \mathrm{MT} \rceil} \\ & = \frac {| \mathrm{Norm} (N _ {m}) | - \lceil | \mathrm{Norm} (N _ {m}) | * \mathrm{MT} \rceil}{| \mathrm{Norm} (N _ {m}) |} \quad \text {where,} \end{array}
$$

$|X|$ is the cardinality of set $X$ ,

FRAC( $A_{j}$ , $N_{m}$ ): FRAC is a function that provides the fraction of minimal conjunctions in the norm of a node that contain $A_{j}$ .

MT is the matching threshold, $\mathbf{MT} \leq 1$ .

We revise the attribute loss probability in Equation (5) to account for threshold matching effects. In the revised expression, the probability of not needing the attribute in norms that contain it (the With Probability, WP) is added to the expression in Equation (5). Thus the revised definition of attribute loss probability is:

$$
\begin{array}{l} \operatorname{ALP} (A _ {j}, i) = \sum_ {N _ {m} \in \operatorname{NRE} (A _ {j}, i)} \frac {\operatorname{Freq} (N _ {m})}{\mathrm{TC}} \\ + \operatorname{WP} (A _ {j}, i) \quad \text { where } \end{array}\tag{6}
$$

$$
\mathrm{WP} \left(A _ {j}, i\right) = \sum_ {N _ {m} \in \mathrm{NRI} \left(A _ {j}, i\right)} \operatorname{FRAC} \left(A _ {j}, N _ {m}\right) * \frac {\operatorname{Freq} \left(N _ {m}\right)}{\mathrm{TC}}.\tag{7}
$$

Continuing with the previous example, we show impact of the new ALP expression on $\mathrm{LC}(N_{1},0)$ . Note that $\mathrm{LC}(N_{2},0)$ will also be affected. In the example, assume that MT is 0.66. In the revised calculation, $N_{2}$ alone will be used in the right hand side of Eq. (7) for the first norm attribute of node $N_{1}$ .

$$
\begin{array}{l} \operatorname{LC} (N _ {1}, 0) = [ \operatorname{ALP} (A _ {1}, 0) * \operatorname{SCost} (A _ {1}, 0) \\ \quad + \operatorname{ALP} (A _ {2}, 0) * \operatorname{SCost} (A _ {2}, 0) ] * [ 1 - \{\operatorname{Freq} (N _ {1}) / \operatorname{TC} \} ], \end{array}
$$

$$
\begin{array}{r l} \mathrm{ALP} (A _ {1}, 0) & = \mathrm{Freq} (N _ {3}) / \mathrm{TC} + \mathrm{WP} (A _ {1}, 0) \\ & = 0. 3 + \mathrm{WP} (A _ {1}, 0), \\ \mathrm{WP} (A _ {1}, 0) & = \{\mathrm{Freq} (N _ {2}) / \mathrm{TC} \} * \mathrm{FRAC} (A _ {1}, N _ {2}) \\ & = 0. 4 5 * 0. 3 3 = 0. 1 5, \\ \mathrm{ALP} (A _ {2}, 0) & = \mathrm{Freq} (N _ {2}) / \mathrm{TC} = 0. 4 5, \\ \mathrm{LC} (N _ {1}, 0) & = (0. 4 5 * 2 0 + 0. 4 5 * 3) * 0. 7 5 = 7. 7 6. \end{array}
$$

Note that the loss criterion value of a node will always increase (never decrease) due to partial matching. With partial matching there is a positive probability that an attribute in a norm will not be needed. Hence, the ALP for attributes should increase due to partial matching and thus the LC for the node should increase. In the above example, the loss criterion value for node 1 increased from 5.51 to 7.76. This was due to partial matching using a matching threshold of 0.66.

3.4.1.3. Algorithm and Analysis. Figure 2 depicts the CR $_{lc}$ node ordering algorithm. The algorithm is simple because most computation occurs in calculating the loss criterion (LC). The outer loop iterates over the node selection stages. The inner loop computes the loss criterion for each node not selected in a previous stage. After processing each stage, the attribute costs of the norm attributes of the selected node are set to zero.

The complexity of the $CR_{lc}$ node ordering algorithm is dominated by the loss criterion computation. The outer loop (2.) executes p - 1 times, once for each node except for the last node in the ordering. The inner loop (2.3) executes p/2 times because on the average there are p/2 nodes that have not been selected. There are two implied loops in the LC computation. To calculate the LC for each node, the attribute loss criterion is calculated r times, assuming r attributes per norm on the average. To compute the attribute loss criterion, each unselected node must be visited resulting in an average of p/2 nodes visited. Thus, the complexity of the $CR_{lc}$ node ordering algorithm is $O(rp^{3})$ .

3.4.2. Attribute Ordering. For each selected node, an attribute ordering can be computed using a loss criterion calculated for the attributes of the node's norm. The loss criterion is the probability of not needing the attribute to make a matching decision at the node (attribute loss probability) times the cost of the attribute.

## Figure 2 Algorithm $CR_{kc}$ Node Ordering

```txt
Input
N: set of nodes

Output
S: the list of nodes ordered by the loss criterion

Procedure
1. S := φ;
2. For t = 0 to |N| - 2
2.1 BestLC := HIGHVALUE;
2.2 M := Remove(N, S); M is the set of remaining nodes obtained by removing the nodes in list S from set N
2.3 For each m ∈ M
2.3.1 NewLC := LC(m, t),
2.3.2 if NewLC < BestLC then
2.3.2.1 BestNode := m;
2.3.2.2 BestLC := NewLC,
2.4 S := Append(S, BestNode); append BestNode to S
2.5 Assign 0 to the costs of norm attributes of BestNode;
3. S := Append(S, Remove(N, S)), append the last remaining node to S
4. Return S,
```

This attribute loss probability is the sum of the probabilities of the minimal conjunctive terms of the norm that do not contain the attribute of interest, but exceed the matching threshold.

Computing and storing conditional probabilities for minimal conjunctive terms would make the attribute loss criterion exponentially complex. Therefore, we have implemented a simple heuristic in its place. The attributes are ordered by one minus their predictable probability times their cost. The predictable probability is a measure of an attribute's usefulness given the node. Note that the cost is zero if an attribute has been collected in a previous stage. More precisely, the Attribute Cost Selection Heuristic (ACSH) is defined below:

$$
\begin{array}{r l} & \mathrm{ACSH} (i, N _ {m}, \alpha) \\ & = \underset {j} {\operatorname{Min}} (1 - P [ A _ {j} = V | N _ {m} ] * \mathrm{SCost} (A _ {j}, i)), \\ & A _ {j} \in \mathrm{AR} (N _ {m}, \alpha) \quad \text { where } \end{array}\tag{7}
$$

$P[A_{j}=V|N_{m}]$ is the predictable probability of attribute $A_{j}$ of node $N_{m}$ .

The overall complexity of the loss criterion algorithm $(\mathrm{CR}_{\mathrm{lc}})$ is $O(\mathrm{LC}_{\mathrm{NO}} + p \, \mathrm{LC}_{\mathrm{AO}})$ . In the expression for complexity, p is the number of nodes and $LC_{NO}$ and $LC_{AO}$ are the complexities of the node and attribute ordering components of $CR_{lc}$ . The complexity of $LC_{NO}$ is $O(rp^{3})$ as described in §3.4.1.3. The complexity of $LC_{AO}$ is $O(r \log r)$ because on the average r attributes per norm are sorted by their predictable probability. Therefore, the overall complexity of the loss criterion algorithm is polynomial in the number of nodes and attributes.

## 4. Joint Concept Formation and Retrieval

In contrast to case based systems, $ID3_{c}$ jointly computes a decision tree that combines concept definitions and an information acquisition context. Attributes are collected in an order depending upon the case and the strategy prescribed in the decision tree. The $ID3_{c}$ algorithm demonstrates that combining concept formation and retrieval strategy formation can significantly reduce information acquisition costs.

Decision tree induction algorithms, such as ID3 (Quinlan 1986), typically construct a decision tree using a recursive partitioning approach. The attribute names used to label nonleaf nodes are determined using an attribute selection criterion and a set of cases. Once a nonleaf node has been labeled, q outgoing arcs are created at this node, where q is the number of possible states of the attribute. The set of cases used to label the nonleaf node is then partitioned into q subsets, where the state of the labeling attribute is the same within each subset. Creation of nonleaf nodes continues along each path of the tree until a stopping condition is reached, at which stage a leaf node is created. Leaf nodes are labeled using a classification function. A more detailed description of the above induction process is presented in Appendix A1.

The design of the ID3 $_{c}$ algorithm is identical to that of the ID3 algorithm except for a modification in the manner in which attributes are selected (the attribute selection criterion). In the ID3 algorithm, attributes are selected based solely upon their information content, measured by the reduction in information entropy (Shannon and Weaver 1949). The attribute that provides the highest reduction in information entropy is selected. On the other hand, the ID3 $_{c}$ algorithm selects attributes based upon information content per unit information acquisition cost. Thus, the attribute selection criterion used in the ID3 $_{c}$ algorithm, is the entropy reduction expression used in ID3 divided by the information acquisition cost for the attribute. A more precise definition of the attribute selection criterion is presented in Appendix A2.

In summary, the attribute selection criterion for $ID3_{c}$ is designed to reduce the expected cost of classifying a case. The same criterion in ID3 is, on the other hand, designed to reduce the expected number of attributes needed to classify a case.

## 5. Experimental Comparison

In this section we describe simulation experiments to study: (i) joint versus separate optimization of concept formation and retrieval (that is, $ID3_{c}$ versus $CR_{lc}$ and $CR_{f}$ ), and (ii) frequency based versus cost based case retrieval (that is, $CR_{f}$ versus $CR_{lc}$ ). The primary measure of performance of an algorithm is the expected information acquisition cost to assign a case to a cluster. Accuracy and number of attributes collected are secondary measures. We discuss factors affecting performance, experimental design, experimental data, experimental procedures, and results.

## 5.1. Factors Affecting Performance

To explore performance differences between the algorithms, we use two quantitative variables or covariates: (i) attribute cost coefficient of variation, and (ii) matching threshold. The qualitative variable, namely algorithm, is coded using two 0–1 indicator variables.

5.1.1. Algorithm. There are three algorithms used in this study: (i) $CR_{f}$ , (ii) $CR_{lc}$ , and, (iii) $ID3_{c}$ . We expect $CR_{lc}$ to dominate $CR_{f}$ because the former uses costs in computing an order while the latter does not. We also expect $ID3_{c}$ to dominate $CR_{lc}$ because $ID3_{c}$ jointly optimizes concept formation and retrieval strategy formation whereas $CR_{lc}$ separately optimizes these tasks. Thus we expect the following:

PROPOSITION 1. ID3c should incur lower information acquisition costs than CR $_{lc}$ which should incur lower costs than CR $_{f}$ .

5.1.2. Attribute Cost Coefficient of Variation. In some situations, certain attributes can be much costlier than others; that is, attribute cost coefficient of variation can be high. In these situations, it may prove extremely important to select a particular information acquisition strategy. When attribute costs vary, an algorithm that develops concepts and/or a retrieval strategy considering attribute costs would perform at a relative advantage over one that ignores attribute costs. At higher coefficient of variation, we expect $CR_{f}$ costs to increase relative to $CR_{lc}$ costs because $CR_{lc}$ is sensitive to costs while $CR_{f}$ is not. Similarly, we expect the coefficient of variation to affect the relative performance of $ID3_{c}$ versus $CR_{lc}$ because $ID3_{c}$ considers costs in concept formation whereas $CR_{lc}$ does not.

PROPOSITION 2. The cost performance difference between $CR_{f}$ and $CR_{lc}$ becomes larger as the attribute cost coefficient of variation increases.

PROPOSITION 3. The cost performance difference between $CR_{lc}$ and $ID3_{c}$ becomes larger as the attribute cost coefficient of variation increases.

5.1.3. Matching Threshold. We define degree of search in a case retrieval algorithm as the average number of attributes collected to match a case. The degree of search can be controlled by varying the matching threshold. For a case to match at a norm, the number of case attributes that match with norm attributes must be greater than or equal to the matching threshold. Increasing the matching threshold increases the extent of fit. The use of a matching threshold in case retrieval is similar to pruning in decision tree induction (Quinlan 1987). However, the analogy is not exact because pruning techniques typically employ significance testing, whereas matching thresholds do not.

Matching threshold is a factor relevant only to the case retrieval algorithms. Since the node ordering component of $CR_{f}$ does not consider partial matching, its performance relative to $CR_{lc}$ could be poor if there is more potential for partial matching (that is, when matching threshold is low). However, as matching threshold increases, the potential for partial matching reduces and the relative performance of $CR_{f}$ with respect to $CR_{lc}$ can be expected to improve.

PROPOSITION 4. $\mathrm{CR_{lc}}$ performs better than $\mathrm{CR_f}$ in the entire range, but the cost performance difference between $\mathrm{CR_f}$ and $\mathrm{CR_{lc}}$ becomes smaller as the matching threshold increases.

## 5.2. Experimental Design

The response function for our model is:

$$
\begin{array}{r l} E (\text { Cost }) & = \beta_ {0} + \beta_ {1} (\text { CV }) + \beta_ {2} (\text { MT }) + \beta_ {3} (i 1) \\ & + \beta_ {4} (i 2) + \{\text { interaction - terms } \}. \end{array}\tag{9}
$$

The response variable, $E(\text{Cost})$ , is calculated as the average information acquisition cost of assigning an unseen case to a cluster. $^{3}$ The covariate CV (coefficient of variation of the attribute costs) is chosen between 0 and 0.5. The other covariate, MT (matching threshold), is chosen between 0.5 and 1. The indicator variables $i1$ and $i2$ are 0, 1 variables coded as follows: ID3 $_{c}$ : $i1 = 1$ , $i2 = 0$ ; CR $_{f}$ : $i1 = 0$ , $i2 = 1$ ; and CR $_{lc}$ : $i1 = i2 = 0$ . Finally, {interaction-terms} represents the following second and third order terms: $\beta_{5}(i1^{*}\text{CV})$ , $\beta_{6}(i2^{*}\text{CV})$ , $\beta_{7}(i1^{*}\text{MT})$ , $\beta_{8}(i2^{*}\text{MT})$ , $\beta_{9}(\text{CV}^{*}\text{MT})$ , $\beta_{10}(i1^{*}\text{CV}^{*}\text{MT})$ , and $\beta_{11}(i2^{*}\text{CV}^{*}\text{MT})$ .

## 5.3. Experimental Data

Four experiments were conducted to investigate Propositions 1 through 4. The main difference in these experiments is that different data sets were used. Two of the four data sets were artificially generated and the remaining two were taken from real domains. All the data sets are preclassified, and the classes are non-overlapping. Since we were not interested in the clustering component of case based systems, the cases in a cluster were chosen as those with the same class.

The artificial data sets were generated by a program based on specifications described in (Bisson 1991). The data set generator can control the number of cases, classes, attributes, states per attribute, and the complexity of rule sets for each class. Data set 1 contains 4 equally distributed classes and 10 input attributes. Data set 2 contains 8 moderately skewed classes and 15 input attributes. Half the cases in data set 2 are uniformly distributed between two classes while the remaining cases are uniformly distributed among the other 6 classes. Both artificial data sets share the following characteristics: (i) the number of cases is 200, (ii) the average number of states per attribute is 3 (between 2 and 5), and (iii) the average size of the rule sets is 2 rules per class with 3 attributes per rule.

The two real domain data sets, Zoo and Lymphography, were selected from the Repository of Machine Learning Databases and Domain Theories (Murphy and Aha 1991). Both data sets have a reasonable number of attributes and classes. In addition, they have only nominal attributes. The Zoo data set has 7 classes, 16 attributes (mostly Boolean), and 101 cases. The Lymphography data set has 4 classes, 18 attributes (mix of Boolean and nominal with a few states), and 148 cases. In this data set, 2 classes are infrequent compared to the other classes. Both real domain data sets have some noise from conflicting cases. Two cases conflict if they have identical values for the input attributes but different values for the class.

<table><tr><td colspan="3">Table 3 Norm Construction Thresholds</td></tr><tr><td>Data Set</td><td>Predictive Probability</td><td>Predictable Probability</td></tr><tr><td>Lymph</td><td>0.5</td><td>0.5</td></tr><tr><td>Zoo</td><td>0.5</td><td>0.4</td></tr><tr><td>DS1</td><td>0.46</td><td>0.32</td></tr><tr><td>DS1</td><td>0.5</td><td>0.38</td></tr></table>

## 5.4. Experimental Procedure $^{4}$

The two case retrieval algorithms use norms that are computed by applying norm construction thresholds, namely, the predictable probability and the predictive probability. Rather than use arbitrary construction threshold values, we selected values to achieve maximum classification accuracy in a pilot study.

In the pilot study, both norm construction values were independently varied in steps of 0.1 from 0.2 to 0.9. For each combination of values for the thresholds, we drew 66% cases from the data set and constructed norms using these cases. The remaining (34%) cases were assigned to clusters, resulting in one observation for classification accuracy. The average accuracy across 25 splits was then taken. The best values for each data set were used for norm construction thresholds in the main experiments (see Table 3).

The following procedure, recommended by Weiss and Kulikowski (1991), was used to generate observations. A data set was randomly split into a training set (66% of cases) and a holdout set (34% of cases). The training set was used to construct norms for clusters of cases with the same class. The same training set was used to construct node and attribute orders using the $CR_{f}$ and $CR_{lc}$ algorithms, and a decision tree using the $ID3_{c}$ algorithm. The two sets of norms and the decision tree were then used to assign cases in the holdout set.

Table 4 Parameter Estimates for Lymph Data

<table><tr><td colspan="6">R-square 0.9178; Adj R-sq 0.9149</td></tr><tr><td>Variable</td><td>DF</td><td>Parameter Est.</td><td>Std. Error</td><td>t-value</td><td>P-value</td></tr><tr><td>INTERCEPT</td><td>1</td><td>14.330270</td><td>0.73800292</td><td>19.418</td><td>0.0001</td></tr><tr><td>CV</td><td>1</td><td>-8.471102</td><td>2.21343471</td><td>-3.827</td><td>0.0002</td></tr><tr><td>i1</td><td>1</td><td>45.301786</td><td>2.62000580</td><td>17.291</td><td>0.0001</td></tr><tr><td>i2</td><td>1</td><td>38.962328</td><td>2.44214934</td><td>15.954</td><td>0.0001</td></tr><tr><td>CV*i1</td><td>1</td><td>10.398777</td><td>3.83378138</td><td>2.712</td><td>0.0071</td></tr><tr><td>MT*i1</td><td>1</td><td>-12.392094</td><td>3.13026939</td><td>-3.959</td><td>0.0001</td></tr><tr><td>MT*i2</td><td>1</td><td>-16.056501</td><td>3.13026939</td><td>-5.129</td><td>0.0001</td></tr></table>

Because the choice of a training set can affect the performance of the three algorithms, the algorithms were run on 25 different, randomly generated training sets. One observation for each of the three algorithms was the average cost across the 25 training sets. To avoid random differences occurring from the choice of the training set, the same 25 training sets were used for each observation.

For a given data set, the experiment generated 300 observations, 100 for each algorithm. Each observation was the average cost over 25 splits. To reduce unnecessary variance in the response variable, the values for CV and MT were held constant over the 25 splits of an observation. In addition, since the average cost of the attributes is not a factor of interest, it was held constant over all observations and data sets.

Table 5 Parameter Estimates for Zoo Data

<table><tr><td colspan="6">R-square 0.9867; Adj R-sq 0.9864</td></tr><tr><td>Variable</td><td>DF</td><td>Parameter Est.</td><td>Std. Error</td><td>t-value</td><td>P-value</td></tr><tr><td>INTERCEPT</td><td>1</td><td>11.183819</td><td>0.31553049</td><td>35.444</td><td>0.0001</td></tr><tr><td>CV</td><td>1</td><td>-5.585208</td><td>0.94634603</td><td>-5.902</td><td>0.0001</td></tr><tr><td>i1</td><td>1</td><td>66.447159</td><td>1.12017403</td><td>59.319</td><td>0.0001</td></tr><tr><td>i2</td><td>1</td><td>47.427607</td><td>1.04413214</td><td>45.423</td><td>0.0001</td></tr><tr><td>CV*i1</td><td>1</td><td>3.315684</td><td>1.63911941</td><td>2.023</td><td>0.0440</td></tr><tr><td>MT*i1</td><td>1</td><td>-34.639359</td><td>1.33833539</td><td>-25.882</td><td>0.0001</td></tr><tr><td>MT*i2</td><td>1</td><td>-22.131908</td><td>1.33833539</td><td>-16.537</td><td>0.0001</td></tr></table>

## 5.5. Results

The parameter estimates for the response function in Equation (9) for the four data sets are presented in Tables 4, 5, 6 and 7 respectively. In these tables, only those variables that were found to be significant at a P-value of 0.10 or below are shown.

Table 8 shows the response functions for the various algorithms and the data sets. To obtain a specific response function (for example for $CR_{f}$ and Lymph), set i1 = 1 and i2 = 0 in Equation (9) and substitute parameter values from Table 4. Table 8 shows that the $ID3_{c}$ algorithm was cheaper than the $CR_{lc}$ algorithm that in turn was cheaper than the $CR_{f}$ algorithm. Hence, Proposition 1 is supported.

Table 8 reveals support for Proposition 2, but only partial support for Proposition 3. Concerning proposition 2, note that as CV increases, the performance difference between $CR_{f}$ and $CR_{lc}$ becomes larger. Concerning Proposition 3, note the differential effect of CV in the artificial and real data sets. An increase in CV causes the performance of $CR_{lc}$ to deteriorate relative to $ID3_{c}$ in DS1 and DS2. In contrast, the performance difference is not affected by CV in Zoo and Lymph. Note, however, that in Zoo and Lymph, $ID3_{c}$ dominates $CR_{lc}$ even at low levels of CV. This finding implies that a high CV is not required for $ID3_{c}$ to outperform $CR_{lc}$ .

For the Zoo, DS1 and DS2 data sets, increasing MT reduces the performance difference between $CR_{f}$ and $CR_{lc}$ . As MT becomes close to one, the effect of partial matching on the case retrieval algorithms vanishes. Since $CR_{f}$ ignores partial matching, its performance becomes closer to $CR_{lc}$ at high values of MT. For the Lymph data set, however, this effect of MT does not hold. Thus Proposition 4 is supported for 3 of the 4 data sets.

Table 6 Parameter Estimates for DS1 Data

<table><tr><td colspan="6">R-square 0.9714; Adj R-sq 0.9707</td></tr><tr><td>Variable</td><td>DF</td><td>Parameter Est.</td><td>Std. Error</td><td>t-value</td><td>P-value</td></tr><tr><td>INTERCEPT</td><td>1</td><td>14.153754</td><td>0.25084285</td><td>56.425</td><td>0.0001</td></tr><tr><td>CV</td><td>1</td><td>-5.135621</td><td>0.85431220</td><td>-6.011</td><td>0.0001</td></tr><tr><td>i1</td><td>1</td><td>31.623122</td><td>0.73051499</td><td>43.289</td><td>0.0001</td></tr><tr><td>i2</td><td>1</td><td>19.915360</td><td>0.73051499</td><td>27.262</td><td>0.0001</td></tr><tr><td>CV*i1</td><td>1</td><td>6.016483</td><td>1.20817990</td><td>4.980</td><td>0.0001</td></tr><tr><td>CV*i2</td><td>1</td><td>4.491410</td><td>1.20817990</td><td>3.718</td><td>0.0002</td></tr><tr><td>MT*i1</td><td>1</td><td>-20.399257</td><td>0.85431220</td><td>-23.878</td><td>0.0001</td></tr><tr><td>MT*i2</td><td>1</td><td>-12.066499</td><td>0.85431220</td><td>-14.124</td><td>0.0001</td></tr></table>

INFORMATION SYSTEMS RESEARCH
Vol. 8, No. 1, March 1997

Table 7 Parameter Estimates for DS2 Data

<table><tr><td colspan="6">R-square 0.9760; Adj R-sq 0.9755</td></tr><tr><td>Variable</td><td>DF</td><td>Parameter Est.</td><td>Std. Error</td><td>t-value</td><td>P-value</td></tr><tr><td>INTERCEPT</td><td>1</td><td>16.809552</td><td>0.13330435</td><td>126.099</td><td>0.0001</td></tr><tr><td>CV</td><td>1</td><td>-9.563200</td><td>0.45400351</td><td>-21.064</td><td>0.0001</td></tr><tr><td>i1</td><td>1</td><td>18.138876</td><td>0.38821448</td><td>46.724</td><td>0.0001</td></tr><tr><td>i2</td><td>1</td><td>9.335724</td><td>0.38821448</td><td>24.048</td><td>0.0001</td></tr><tr><td>CV*i1</td><td>1</td><td>9.514370</td><td>0.64205792</td><td>14.819</td><td>0.0001</td></tr><tr><td>CV*i2</td><td>1</td><td>8.084477</td><td>0.64205792</td><td>12.592</td><td>0.0001</td></tr><tr><td>MT*i1</td><td>1</td><td>-14.705913</td><td>0.45400351</td><td>-32.392</td><td>0.0001</td></tr><tr><td>MT*i2</td><td>1</td><td>-12.309786</td><td>0.45400351</td><td>-27.114</td><td>0.0001</td></tr></table>

To depict performance difference magnitudes, we show the impact of MT and CV on the cost and accuracy of the three algorithms for the Lymph data set. Each point in these graphs is the average of 25 splits. Figure 3 shows that MT has no substantial effect on the cost difference between the two case retrieval algorithms. In some parts of the range, the difference increases whereas in other parts the difference decreases slightly. The dome shaped curves of Figure 3 can be explained as follows. Initially, as MT increases, more attributes need to be collected to match a case. Hence, the average cost per case initially increases. However, increasing MT beyond a point causes more early node failures, leading to a decrease in the average cost per case.

Figure 4 shows that the impact of CV on the relative cost performance of the three algorithms is not substantial. As CV increases, there is a slight increase in the cost performance difference between the two case retrieval algorithms. There is, however, no substantial cost difference between $CR_{lc}$ and $ID3_{c}$ in the entire CV range.

Figures 5 and 6 demonstrate the effect of MT and CV on accuracy. Figure 5 shows that increasing MT causes substantial overfitting by the case retrieval algorithms. At low levels of MT, the case retrieval algorithms have slightly lower accuracy than ID3 $_{c}$ . CR $_{lc}$ has better accuracy than CR $_{f}$ at low MT levels because CR $_{lc}$ has a more global strategy for choosing the node order. As MT increases, the accuracy difference disappears as the orders either become the same or cease to affect accuracy. Figure 6 shows that increasing CV has no effect on the accuracy of the case retrieval algorithms. However, when CV increases, ID3 $_{c}$ collects more cheap attributes and tends to overfit.

<table><tr><td colspan="4">Table 8 Response Functions</td></tr><tr><td colspan="2">Lymph</td><td colspan="2">Zoo</td></tr><tr><td> $E(Cost) = 59.66 + 1.92*CV - 12.39*MT$ </td><td> $(CR_f)$ </td><td> $E(Cost) = 77.62 - 2.27*CV - 34.64*MT$ </td><td> $(CR_f)$ </td></tr><tr><td> $E(Cost) = 53.29 - 8.47*CV - 16.05*MT$ </td><td> $(CR_{lc})$ </td><td> $E(Cost) = 58.60 - 5.58*CV - 22.13*MT$ </td><td> $(CR_{lc})$ </td></tr><tr><td> $E(Cost) = 14.33 - 8.47*CV$ </td><td> $(ID3_c)$ </td><td> $E(Cost) = 11.18 - 5.58*CV$ </td><td> $(ID3_c)$ </td></tr><tr><td colspan="2">DS1</td><td colspan="2">DS2</td></tr><tr><td> $E(Cost) = 45.77 + 0.88*CV - 20.39*MT$ </td><td> $(CR_f)$ </td><td> $E(Cost) = 34.94 - 0.05*CV - 14.71*MT$ </td><td> $(CR_f)$ </td></tr><tr><td> $E(Cost) = 34.06 - 0.64*CV - 12.06*MT$ </td><td> $(CR_{lc})$ </td><td> $E(Cost) = 26.14 - 1.48*CV - 12.31*MT$ </td><td> $(CR_{lc})$ </td></tr><tr><td> $E(Cost) = 14.15 - 5.13*CV$ </td><td> $(ID3_c)$ </td><td> $E(Cost) = 16.80 - 9.56*CV$ </td><td> $(ID3_c)$ </td></tr></table>

Figures 7 and 8 demonstrate the effect of MT and CV on the number of attributes collected by the different algorithms. As expected, the number of attributes collected is highly correlated with cost. Since we do not vary the average cost in these experiments, at low levels of CV, the cost is almost perfectly correlated with the number of attributes collected. Near the high end of the CV range, ID3 $_{c}$ collects slightly more attributes to exploit the availability of cheap attributes.

![](/api/attachments/F4ZBG5YY/fulltext/images/38d5503f32ee475633fef5d5365f08fa79c2c2836c4ebdff1de3e66194c935d4.jpg)

## 5.6. Discussion

There are two major lessons to draw from this study. First, substantial cost differences between the algorithms indicate that separating concept formation and retrieval strategy formation is a design limitation. It seems unlikely that an algorithm that separates these systems. However, given two possible interventions: (i) designing a better retrieval strategy, and (ii) jointly performing concept formation and retrieval strategy formation, the second intervention appears to have a larger impact.

Figure 4 Impact of CV on Cost  
![](/api/attachments/F4ZBG5YY/fulltext/images/16712b4be602258efff91945f265f1832bde34be4f67760c6a0ce714e6a5b2fe.jpg)  
INFORMATION SYSTEMS RESEARCH
Vol. 8, No. 1, March 1997

![](/api/attachments/F4ZBG5YY/fulltext/images/2840089e4356ca6fa04a39c3b284e048fd65b3694882a3624161cf869f44af9c.jpg)

tasks can compete with an algorithm that jointly performs these tasks. Second, cost considerations can significantly reduce information acquisition costs, even if concept formation and retrieval strategy formation are  
![](/api/attachments/F4ZBG5YY/fulltext/images/ccb280c527387ad378f53642004a530b5823c78baecfc1c11a1e9eb1916a8fa3.jpg)

Figure 7 Impact of MT on Attributes Collected  
![](/api/attachments/F4ZBG5YY/fulltext/images/e48fc9041eba3415b92f6b57e143a673261448ef5748a397c1d23ce9b216967c.jpg)  
separated. The substantial cost difference between cost and frequency based retrieval supports this conclusion. System designers must therefore pay careful attention to the design of the retrieval strategy in case based

![](/api/attachments/F4ZBG5YY/fulltext/images/ceccc26632545cdf42c45a2e826e5e0304f1cffebfcad8f0dcbedd80beacaac5.jpg)

Before leaving this section, we raise two broad issues concerning cost considerations in case based systems. The first issue is the distinction between sequential and parallel acquisition of attributes. As mentioned earlier, the results in this paper apply to case based systems where information can be acquired sequentially and hence information costs are variable. However, even when information costs appear fixed, a variety of factors may require that information costs be treated as variable instead of fixed. These factors include: (i) changes in the competitive environment due to deregulation, (ii) unbundling of product and information costs by firms, (iii) explicit pricing of information by vendors of information services (for example, search agents on the Internet), and (iv) outsourcing of information collection. Thus, reducing variable information costs could become an important addition to a manager's responsibilities.

The second issue concerns estimating the information costs required by the models developed here. Estimating information costs may not always be easy. Estimation difficulties include: (i) sequential dependencies between the cost of acquiring attributes, (ii) variance in the cost of collecting an attribute, and (iii) the relationship between the quality of information and the cost. Although this study used a simple model of information costs, we believe that our qualitative results will extend to more complex models of information costs.

## 6. Summary and Conclusion

We studied the problem of incorporating information acquisition costs into case retrieval algorithms. In a number of business and engineering tasks, attribute costs are significant and unequal, and information acquisition may occur sequentially. A retrieval strategy that ignores the cost of acquiring information may be suboptimal.

A major difficulty with lowering the cost in case based systems is that concept formation and retrieval strategy formation are separated. To study the implications of this limitation, we developed two cost sensitive algorithms, $CR_{lc}$ and $ID3_{c}$ , representative of separate and joint concept formation and retrieval strategy formation. We experimentally compared the cost sensitive algorithms to a frequency based algorithm ( $CR_{f}$ ). Our results demonstrated that the cost sensitive algorithms produced significantly lower costs than $CR_{f}$ and that $ID3_{c}$ costs dominated $CR_{lc}$ costs.

A useful extension of this research would be to study the performance of instance algorithms focusing on whether information acquisition costs can be lowered without significantly reducing accuracy. Instance algorithms are a special challenge because they search the entire space of concept definitions to return the K nearest neighbors using a distance measure rather than a threshold. The challenge is to develop a decision theoretic framework that evaluates whether more search in the norm space is useful given the current accuracy and cost incurred.

Other extensions could include the use of economic considerations in the design of other machine learning techniques. Future research should also address topics such as the effects of different measurement assumptions for costs and benefits, functional relationships between the accuracy of different attributes and acquisition costs, and acquisition costs dependent on the order in which attributes are acquired. Such research would increase the effectiveness of machine learning techniques for business decision making. $^{5}$

$^{5}$ This paper has greatly benefited from the comments and suggestions offered by the associate editor and the three reviewers. We would also like to thank Radha Mookerjee and Cathrine Askilsrud for their suggestions. This project was partially supported by a summer grant to each of the authors from the School of Business, University of Washington.

## Appendix A1

Formally, the induction process can be described using the following definitions. Let

D represent the set of cases in the training set,

$A_{1}, A_{2}, \ldots, A_{n}$ tare n observable attributes that may be used to classify an object,

$x_{i1}, x_{i2}, \ldots, x_{iq}$ are $q$ possible states for attribute $A_i$ , $c_{1}, c_{2}, \ldots, c_{m}$ are $m$ possible ways in which an object may be classified, is a subset of cases in the training set; referred to as the "current set,"

$k(L)$ is a classification function that determines how a leaf node is labeled,

INFORMATION SYSTEMS RESEARCH
Vol. 8, No. 1, March 1997

$g(A_{i},L)$ is a criterion value for attribute $A_{i}$ , given $L$ ,

w is a cut-off value that is used to determine when a leaf node should be created.

The steps in an induction algorithm are described below. Initially, no nodes have been created.

Step 1. Set $L = D$ .

Step 2. Using $L$ , select attribute $A_{j}$ such that, $g(A_{j}, L) \geq g(A_{i}, L)$ , for $i = 1, 2, \ldots, n$ . If $g(A_{j}, L) \leq w$ , go to Step 5.

Step 3. Create a nonleaf node labeled $A_{j}$ . Generate $q$ arcs originating at this node. Label each arc by a state of the attribute $A_{j}$ . Assuming $q$ states for each attribute arcs are labeled $x_{jk}$ , for $k = 1, 2, \ldots, q$ .

Step 4. For each arc $x_{jk}$ determine $M \subseteq L$ , such that $A_j = x_{jk}$ for every case in $M$ . Set $L = M$ . Go to Step 2.

Step 5. Create a leaf node. Label this leaf node $c_{\lambda}$ such that $k(L) = c_{\lambda}$ where $c_{\lambda} \in \{c_1, c_2, \ldots, c_m\}$ .

Step 6. If leaf nodes have been created in all paths of the tree, stop; else, return to Step 4.

## Complexity

The complexity of the above induction process is exponential in the number of attributes but polynomial in the size of the training set (Quinlan 1986). The maximum number of partitions that can be evaluated is $O(q^n)$ , where $q$ is the average number of states per attribute and $n$ is the total number of attributes. The maximum number of partitions occurs in a complete tree in which each path is of length $n - 1$ . Generally, induced trees are much smaller than a complete tree. For each partition evaluated, a sequential scan of the training set is required. The average partition size is proportional to TC, the number of cases in the training set. Therefore, the complexity of the above induction process is $O(\mathrm{TC} \cdot q^n)$ .

## Appendix A2

There are three important factors that must be considered in the design of an induction algorithm: (a) the attribute selection criterion, (b) the stopping rule, and (c) the classification function. The attribute selection criterion determines the attribute to label a nonleaf node. The stopping rule determines when it is no longer beneficial to create nonleaf nodes in a path of the tree. The classification function determines how a leaf node should be labeled. In this appendix, we describe the attribute selection criterion, stopping rule and classification function used by the ID3 $_{c}$ algorithm.

## Attribute Selection Criterion

Formally, the expression for the attribute selection criterion in the ID3 $_{c}$ algorithm can be described as below:

$$
g (A _ {i}, L) = \frac {\mathrm{EN} (L) - \mathrm{EN} (A _ {i} , L)}{\mathrm{Cost} (A _ {i})}, \quad \text { where }
$$

$\mathrm{EN}(L) = -\Sigma_{r=1}^{m} f(c_r, L) \log_2 f(c_r, L)$ is the initial entropy, $\mathrm{EN}(A_t, L) = \Sigma_{k=1}^{q} f(A_t = x_{ik}, L) \mathrm{EN}(L | A_t = x_{ik})$ is the entropy after observing $A_t$ , $\mathrm{EN}(L | A_t = x_{ik}) = -\Sigma_{r=1}^{m} f(c_r, L | A_t = x_{ik}) \log_2 f(c_r, L | A_t = x_{ik})$ is the entropy in the partition $L | A_t = x_{ik}$ ,

$f(c_{r}, L)$ is the proportion of cases in $L$ belonging to the class $c_{r}$ ,

$f(A_{i} = x_{ik}, L)$ is the proportion of cases in $L$ where the attribute $A_{i} = x_{ik}$ , and,

$f(c_{r}, L \mid A_{t} = x_{ik})$ is the proportion of cases in the subset of cases $L$ given $A_{t} = x_{ik}$ , belonging to the class $c_{r}$ .

The algorithm selects the attribute with the highest criterion value, that is, select $A_{\psi}$ such that $g(A_{\psi}, L) \geq g(A_{i}, L)$ , $i = 1, 2, \ldots, n$ . Thus the ID3 $_{c}$ algorithm chooses the attribute with the maximum information content per unit dollar spent in observing the attribute. The attribute selection criterion used by ID3 $_{c}$ is designed to achieve a level of accuracy comparable to ID3 at lower cost.

## The Stopping Rule

The stopping rule of the algorithm is the same as that of the ID3 algorithm. The cut-off value w is zero for this algorithm. Thus, the stopping rule for $ID3_{c}$ is:

Stop if:

$g(A_{t},L) = 0$ for all unobserved attributes.

## The Classification Function

The classification function used by the algorithm is the same as that used by the ID3 algorithm. This algorithm chooses the class with the highest frequency in the current set of cases to label a leaf node. Thus, the classification function $(k(L))$ used by ID3 $_{c}$ can be described as:

Choose $c_{\lambda}$ such that $f(c_{\lambda}, L) \geq f(c_{r}, L), r = 1, 2, \ldots, m$ .

## References

Aha, D., D. Kibler, and M. Albert, "Instance-Based Learning Algorithms," Machine Learning, 6 (1991), 37–66.

Allen, B., "Case Based Reasoning: Business Applications," Comm. ACM 37, 3 (March 1994), 40–42.

Barletta, R. and P. Buta, "Market Surveillance Using Case Based Reasoning," Proc. First International Conf. on AI Applications on Wall Street, New York, October 1991, 116–121.

Becker, J., "A Model for the Encoding of Experiential Information," in R. Schank and K. Colby (Eds.), Computer Models of Thought and Language, Freeman, San Francisco, CA, 1973, 396–435.

Bisson, H., "Evaluation of Learning Systems: An Artificial Data-Based Approach," Proc. European Working Session on Machine Learning, Y. Kodratoff (Ed.), Springer-Verlag, Berlin, Federal Republic of Germany, 1991.

Breese, J. and D. Heckerman, "Decision-Theoretic Case-Based Reasoning," IEEE Trans. on Systems, Man, and Cybernetics, 26 (1996), 838-842.

Creecy, R., B. Masand, S. Smith, and D. Waltz, "Trading MIPS and Memory of Knowledge Engineering," Comm. ACM, 35, 8 (August 1992), 48–64.

Dos Santos, B. and V. Mookerjee, "Expert System Design: Minimizing Information Acquisition Costs," in Decision Support Systems, Vol. 9, North-Holland, Amsterdam, 1993, 161–181.

Feigenbaum, E., "The Simulation of Verbal Behavior," in E. Feigenbaum and J. Feldman (Eds.), Computers and Thought, McGraw-Hill, New York, 1963.

Fisher, D., "Knowledge Acquisition via Incremental Conceptual Clustering," Machine Learning, 2 (1987), 139–172.

Gennari, J., P. Langley, and D. Fisher, "Models of Incremental Concept Formation," Artificial Intelligence, 40 (September 1989), 11–62.

Gonzalez, A. and R. Laureano-Ortiz, "A Case-Based Reasoning Approach to Real Estate Property Appraisal," in Expert Systems with Applications, Vol. 4, Pergamon Press, 1992, 229–246.

Hall, R., "Computational Approaches to Analogical Reasoning: A Comparative Analysis," Artificial Intelligence, 39 (1989), 39–120.

Hammond, K., Case Based Planning: An Integrated Theory of Planning, Learning, and Memory, Ph.D. Thesis, Yale University, New Haven, CT, 1986.

Hanson, S., and M. Bauer, "Machine Learning, Clustering, Polymorphy," in L. Kanal and J. Lemmer (Eds.), Uncertainty and Artificial Intelligence, North-Holland, Amsterdam, 1986.

Heckerman, D., J. Breese, and K. Rommelse, "Troubleshooting Under Uncertainty," Comm. ACM, 38, 3 (March 1995), 49–57.

Kolodner, J., "Improving Human Decision Making Through Case-Based Decision Making," AI Magazine, American Association of Artificial Intelligence, 12, 2 (1991), 52–68.

— and R. Simpson, "The MEDIATOR: An Analysis of an Early Case-Based Problem Solver," Cognitive Sci., 13, 4 (1989), 507–549.

Koton, P., Using Experience in Learning and Problem Solving, Ph.D. Thesis, Massachusetts Institute of Technology, Cambridge, MA, 1988.

Lebowitz, M., "Experiments with Incremental Concept Formation: UNIMEM," Machine Learning, 2 (1987), 103–138.

Mookerjee, V. and B. Dos Santos, "Inductive Expert System Design Maximizing System Value," Information Systems Research, 4, 2 (August 1993), 111–140.

Moore, J. and A. Whinston, "A Model of Sequential Decision Making—Part I," Decision Support Systems, 2, 4 (1986), 285–307.

— and —, "A Model of Sequential Decision Making—Part II," Decision Support Systems, 3, 1 (1987), 47–72.

Murphy, P. and D. Aha, UCI Repository of Machine Learning Databases, University of California, Department of Information and Computer Science, Irvine, CA, 1991.

Nuñez, M., "The Use of Background Knowledge in Decision Tree Induction," Machine Learning, 6 (1991), 231–50.

Patttipati, K. and M. Alexandridis, "Application of Heuristic Search and Information Theory to Sequential Fault Diagnosis," IEEE Trans. Systems, Man, and Cybernetics, 20, 4 (July/August 1990), 872–887.

Quinlan, J., "Induction of Decision Trees," Machine Learning, 1 (1986), 81–106.

——, "Simplifying Decision Trees," International J. Man Machine Studies, 27 (1987), 221–234.

Shannon, C. and W. Weaver, The Mathematical Theory of Communication, University of Illinois Press, 1949, (published in 1964).

Simoudis, E., "Using Case-Based Retrieval for Customer Technical Support," IEEE Expert 7, 5 (October 1992), 7–12.

— and J. Miller, "The Application of CBR to Help Desk Applications," in Proc. Workshop on Case Based Reasoning, 1991, 25–36.

Stottler, R., "CBR for Cost and Sales Prediction," AI Expert, 9, 8 (1994), 24–33.

Weiss, M. and C. Kulikowski, Computer Systems that Learn: Classification and Prediction Methods from Statistics, Neural Nets, Machine Learning, and Expert Systems, Morgan, Kaufmann Publishers, San Mateo, CA, 1991.

Zarley, D., "A Case-Based Process Planner for Small Assemblies," in Proceedings. Case-Based Reasoning Workshop, Washington, D.C., May 1991, 363–373.

Andrew B. Whinston, Associate Editor. This paper was received on July 20, 1994 and has been with the authors 7 months for 2 revisions.

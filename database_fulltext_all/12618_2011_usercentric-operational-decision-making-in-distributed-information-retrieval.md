---
otero_id: 12618
otero_key: "UH64YKGP"
title: "Usercentric Operational Decision Making in Distributed Information Retrieval"
authors: "Kartik Hosanagar"
year: "2011"
journal: "Information Systems Research"
doi: "10.1287/isre.1100.0287"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## 6SR

![](/api/attachments/UH64YKGP/fulltext/images/963b2b72ece7d197aa6013cde9edff42d01ce06ee2f9cc8bfe64ffeca7463200.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Usercentric Operational Decision Making in Distributed Information Retrieval

Kartik Hosanagar,

To cite this article:

Kartik Hosanagar, (2011) Usercentric Operational Decision Making in Distributed Information Retrieval. Information Systems Research 22(4):739-755. http://dx.doi.org/10.1287/isre.1100.0287

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2011, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/UH64YKGP/fulltext/images/d2a66953e26a7d4f8abc92ab2dc4b5bacbebb02d861096eff8e14f80e6f7c4eb.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Usercentric Operational Decision Making in Distributed Information Retrieval

Kartik Hosanagar Operations and Information Management, The Wharton School of the University of Pennsylvania, Philadelphia, Pennsylvania 19103, kartikh@wharton.upenn.edu

nformation specialists in enterprises regularly use distributed information retrieval (DIR) systems that query Ia large number of information retrieval (IR) systems, merge the retrieved results, and display them to users. There can be considerable heterogeneity in the quality of results returned by different IR servers. Further, because different servers handle collections of different sizes and have different processing and bandwidth capacities, there can be considerable heterogeneity in their response times. The broker in the DIR system has to decide which servers to query, how long to wait for responses, and which retrieved results to display based on the benefits and costs imposed on users. The benefit of querying more servers and waiting longer is the ability to retrieve more documents. The costs may be in the form of access fees charged by IR servers or user’s cost associated with waiting for the servers to respond. We formulate the broker’s decision problem as a stochastic mixed-integer program and present analytical solutions for the problem. Using data gathered from FedStats—a system that queries IR engines of several U.S. federal agencies—we demonstrate that the technique can significantly increase the utility from DIR systems. Finally, simulations suggest that the technique can be applied to solve the broker’s decision problem under more complex decision environments.

Key words: distributed information retrieval (IR); personalization; utility theory; optimal operational decisions; source selection; query termination; stochastic modeling

History: Seungjin Whang, Senior Editor; Debabrata Dey, Associate Editor. This paper was received on December 20, 2007, and was with the authors 15 <sup>1</sup> months for 2 revisions. Published online in Articles in Advance June 14, 2010.

## 1. Introduction

Organizations spend large sums to build and deploy information systems (IS) and have a vested interest in ensuring the widespread adoption and effective use of these systems. Prior research in IS has studied the factors that affect users’ adoption and usage of information systems (e.g., Davis et al. 1989) and demonstrated that design characteristics have a major influence on adoption decisions and usage behavior (e.g., Xiao and Benbasat 2007). A natural direction for IS research, therefore, is to study and prescribe design choices that can increase the value from and usage of specific information systems. In this paper, we study key design decisions, tied to operational decision making, for a distributed information retrieval (DIR) system.

The last few years have witnessed an explosive growth in the amount of information being stored electronically. Access to this information is crucial for information-intensive firms. DIR systems are widely used to provide information specialists and other employees with access to distributed information repositories. In a DIR system, a broker queries multiple distributed data sources to gather relevant information in response to a query. These distributed data sources may each be IR systems. Given a query, the goal of each of these IR systems is to identify and display the local documents most relevant to the query. The objective of the DIR system is to provide unified access to all relevant resources on the network but give the impression of a single IR database (Fuhr 1999). For example, a patent metasearch system may be used to query several distributed patent databases such as USPTO<sup>1</sup> and WIPO.<sup>2</sup> Similarly, a portal called FedStats<sup>3</sup> is often used to access statistics from over 100 U.S. federal agencies including NIH, USDA, and census bureau. Similar systems are widely deployed in law firms and financial institutions to provide centralized access to multiple data collections. Other examples include library management systems that provide access to multiple distributed digital libraries and some comparison shopping engines that query multiple store websites in real time to gather price and product information.

Key operational issues that must be addressed during a distributed IR task include which data sources or IR servers to query, how long to wait for responses, and which results to display (Baeza-Yates and Ribiero-Neto 1999, Fuhr 1999, Montgomery et al. 2004). IR servers need to be selected carefully because there can be considerable heterogeneity in the quality of results returned by different servers and the access fee charged by them. Furthermore, each of the IR servers has considerable processing to do locally in response to a query, which can result in high response times. Hence, a broker may find it optimal to terminate a search even before all queried servers have responded if it believes that the user’s benefit from waiting is outweighed by the cost of waiting. Finally, the broker must determine which of the retrieved results to display. These operational decisions are key design decisions available to brokers in DIR systems and are likely to impact users’ adoption and usage decisions (Basartan 2001, Si and Callan 2004, Montgomery et al. 2004). For example, a recent survey of users of patent metasearch systems identified comprehensive coverage and slow response times as two major issues with current systems.<sup>4</sup> These are both impacted by the broker’s operational decisions.

In this paper, we address optimal operational decisions—which servers to query, how long to wait for responses, and which retrieved results to display— for brokers in distributed IR, by taking into account user preferences and historical performance of the distributed sources. We formulate the broker’s decision problem as a stochastic mixed-integer program and present an analytical solution. We illustrate its application using data from a real-world DIR context and demonstrate that the gains from the technique can be significant.

Our research contributes to two distinct streams— the design of distributed IR systems in the computer science community and user preference modeling in electronic environments in the IS community. Although a number of interesting technical challenges in the design of DIR systems have been addressed by IR researchers, user models are often absent or not very sophisticated. Our research presents a novel application of utility theory to IR and bridges utilitycentric considerations studied in management science with computational aspects from IR research. The proposed approach also emphasizes how intelligent operational decision making can help improve the performance of information systems. In turn, this will help increase their adoption and improve enterprise return on investment from deploying these systems.

The rest of this paper is organized as follows. In §2, we review related work. In §3, we develop a decision-theoretic formulation to model the tradeoffs and present an analytical solution to the problem. In §4, we apply data from a real-world DIR application and evaluate the performance improvement that optimal decision making can provide. Section 5 discusses issues tied to implementation and concludes by highlighting directions for future work.

## 2. Prior Work

In this section, we review three streams of work most relevant to our study of usercentric decision making in DIR—(1) impact of design choices on system adoption, (2) operational decisions in DIR with a special emphasis on decision-theoretic approaches, and (3) models of user preferences and costs.

Impact of Design on Adoption. A rich stream of work has studied factors that affect users’ adoption decisions and postadoptive usage of information systems. Building on theories from social psychology, the technology acceptance model (Davis et al. 1989) indicates that users’ intention to adopt a system depends primarily on its perceived usefulness and perceived ease of use. Recent studies have also identified the factors that influence the continued usage of these systems (Jasperson et al. 2005, Bhattacharjee 2001). Bhattacharjee (2001) identifies the (mis)match between preadoption expectations and perceived usefulness of continued use as a primary driver of postadoptive usage decisions. Design factors clearly influence the perceived usefulness of information systems and influence both adoption decisions and postadoptive usage behavior. For example, Xiao and Benbasat (2007) and Al-Natour et al. (2006) show that users’ evaluations of automated shopping agents is influenced by design characteristics such as the agent’s decision process.

The operational decisions of which servers to query and how long to wait for responses are key design decisions available to a broker in a DIR system.<sup>5</sup> These decisions influence the comprehensiveness of the results and the user’s wait time, both of which are known to impact the user’s evaluation of the system (e.g., Basartan 2001).

Operational Decisions in DIR. The process of determining the servers to query is termed source selection. Callan et al. (1995) represent each server by its terms and document frequencies to rank order and select the servers. Other popular source selection techniques include gGIOSS resource-ranking algorithm (Gravano and Garcia-Molina 1995) and ReDDE (Si and Callan 2003). Once results have been retrieved from different sources, they need to be merged. When the data sources are cooperative, the results can be merged based on the server-specific relevance scores and normalizing statistics provided by the servers. In noncooperative environments, more sophisticated techniques, including regression-based techniques (Le Calve and Savoy 2000, Si and Callan 2002) and Bayesian models (Aslam and Montague 2001), are used. These techniques involve offline analysis of the IR servers during a resource representation phase. The analysis is used to develop decision rules for merging retrieved results in a fast manner.

The most relevant papers in this stream are the ones applying decision-theoretic approaches. These include work by Fuhr (1999) on a decision-theoretic approach to source selection and by Voorhees et al. (1995) on an approach to select sources and merge results based on historical data. Etzioni et al. (1996) also study the optimal sequence in which to query information sources in a sequential query problem where the broker pays each information source in order to query it. Si and Callan (2004) propose a deterministic dynamic programming (DP) based algorithm for source selection.<sup>6</sup>

Our paper complements this stream of work but introduces an important perspective. We develop a model of user preferences and introduce a utility-theoretic framework to guide the decisions. Models of user preferences have been largely absent in the IR literature. Montgomery et al. (2004) also integrate computational and behavioral considerations to study operational decisions made by shopbots. However, the solutions were derived for the case in which servers have i.i.d. response time and i.i.d. utilities, which is a restrictive assumption for general DIR systems where servers can be highly heterogeneous. Further, the results were specifically for the shopbot context and do not generalize to distributed IR. In contrast, our objective is to solve the decision problem for a broker in a DIR system, to account for server heterogeneity, and to develop an operational algorithm that can be implemented in a computationally efficient manner.

Modeling User Preferences and Costs. The formulation of a utility-theoretic framework for a DIR system requires specifying the user’s decision strategy and modeling the value from information as well as costs associated with waiting for responses and evaluating information. We draw from various streams of research to model these components.

Svenson (1979) provides an overview of several decision strategies used by consumers in multialternative, multiattribute choice problems. These strategies vary in terms of their cognitive effort and ability to produce a good outcome (“accuracy”). For example, the elimination by aspect strategy, which compares attribute values against user-specified thresholds, requires little effort but also has low accuracy (Johnson and Payne 1985). In contrast, the additive compensatory strategy, which allows a high value of one attribute to compensate for a low value of another, is highly accurate but requires significant effort (Bettman et al. 1998). An important distinction of the IR environment is that documents are typically sorted by relevance score, which in turn simplifies the user decision process. Further, users are not necessarily interested in choosing one document. Users may process multiple documents and derive value from each of these documents. Because documents are sorted in decreasing order of relevance, a common assumption in the IR environment is that users process documents sequentially (Fuhr 1999). It is also well known that users do not process all displayed documents. The cognitive cost of processing information determines a user’s stopping rule (Browne et al. 2007). A number of normative and heuristic strategies have been proposed to specify stopping rules in information processing and search. Our specification draws from normative approaches in which users process information until the marginal cost of processing information exceeds the marginal benefit (Stigler 1961 and related work). Under constant marginal costs, this strategy is also consistent with the level cutoff heuristic studied by Feinberg and Huber (1996) in which only the alternatives that offer a minimal level of utility are evaluated.

To apply the normative strategy described above, it is important to quantify the cognitive cost incurred by users. Several model-based evaluation methods have been proposed in human-computer interaction (HCI) research to compute estimates of user effort when interacting with a system. The most prominent among these models is GOMS, an approach that identifies the procedures/methods a user must use to operate a system (Card et al. 1983). The procedures are expressed in terms of elementary operators, and the user effort is estimated in terms of the total number of elementary operators required for the task. The simplest GOMS models include keystroke-level models (Card et al. 1983) that focus on keystroke-level operators, and more sophisticated versions include CPM-GOMS (Gray et al. 1993), which model cognitive, perceptual, and motor operators performed in operating the system. NGOMSL (Kieras 1997) provides a naturallanguage syntax for GOMS representation. Other evaluation approaches include cognitive architecture models such as Soar and EPIC (see Byrne 2007 for a survey). These papers primarily focus on the impact of interface design choices on user effort, which includes, and is often dominated by, motor actions such as keystrokes. In contrast, we do not focus on interface design issues in this study and are more interested in measuring cognitive costs of information processing. A related stream of work on information processing provides some answers. Several studies (for example, Chase 1978, Johnson and Payne 1985) have tried to decompose the cognitive effort into units of elementary information processes, and Shugan (1980) has proposed a metric for the cognitive cost based on a count of these elementary processes. We apply a similar metric and introduce its notation in §3.

Prior work has also shown that waiting time influences consumer perception of services (e.g., Hui and Tse 1996). Consistent with that, user studies on the Web also show that consumers incur significant costs in waiting for websites to respond (Dellaert and Kahn 1999, Galletta et al. 2006). Accordingly, theoretical studies investigating operational aspects of information systems have incorporated waiting costs associated with user delay (e.g., Mendelson and Whang 1990).

In summary, the prior literature reveals three themes. First, the broker’s operational decisions are important design variables for DIR systems and can have a major impact on adoption/usage of these systems. Second, there has been work on operational decision making in the IR community, but an important utility-theoretic perspective has been missing from the literature. Third, there exist welldeveloped theories and models of users’ waiting and information-processing costs that have much to contribute in this regard.

## 3. Decision-Theoretic Framework

To fix a context, we consider a DIR deployment in an enterprise setting wherein the IS manager is interested in maximizing the expected surplus from the system. Specifically, the broker makes operational decisions in order to maximize the expected surplus for any given query. Further, we assume that each of the individual IR systems index different collections with nonoverlapping documents. Figures 1a and 1b illustrate the framework we propose for the broker’s operational decisions. First, the broker analyzes past data on distribution of response times and relevance scores of documents retrieved from various servers and generates decision rules for source selection and query termination (Figure 1a). These rules identify the servers to query and the wait time for each query class and user. A query class is a topic area (e.g., “public policy”) with query complexity information (e.g., a simple query may be defined as a non-Boolean query with fewer than five terms per query). The user can be an individual user of the DIR system or a class of users that have been identified to be similar. The specific choice of whether individual-level or segment-level customization is done will depend on the amount of data available per user and computational costs associated with processing user information. We discuss this issue further in §5. When a query is received, the broker identifies the query class and user segment and then determines which servers to query and how long to wait for responses (Figure 1b). These decisions are based on the decision rules from the prior offline analysis. Finally, the broker merges the results and displays them to the user.

Figure 1 Decision Process for the Broker  
![](/api/attachments/UH64YKGP/fulltext/images/72f44982880eaae1d22fc5302a1364c445b00372fb84c3545cc5904da1214bb9.jpg)

(b) Online (real-time) analysis  
![](/api/attachments/UH64YKGP/fulltext/images/bcc5b345facb49fb166032c7838c3ecc5fe44f34c11c308e6a288ee6190b72fb.jpg)

## 3.1. Notation and Assumptions

Let N denote the total number of servers that can be queried. ${ \bf q } = ( q _ { 1 } , q _ { 2 } , \dots , q _ { N } )$ is a vector that denotes the servers queried, with $q _ { i } = 1$ if server i is queried and $q _ { i } = 0$ otherwise. $t _ { i }$ denotes the response time of server i. The response time of servers cannot be predicted precisely; $\mathrm { i . e . , } t _ { i }$ is a stochastic variable. $F _ { i } ( \ u )$ denotes the probability distribution function $( \mathrm { i . e . , }$ cdf) for the response time of server i. T denotes the broker’s wait time. Server i is retrieved if $q _ { i } = 1$ and $t _ { i } \leq T , \ d _ { i }$ denotes the number of documents returned by server i when it is retrieved. We model the retrieval of documents from individual servers as a batch process, as is common with most IR systems. That is, either all $d _ { i }$ documents are retrieved or none are retrieved. The total number of servers queried is denoted Q and the total number of documents retrieved is denoted D $\begin{array} { r } { ( \sum q _ { i } = Q \le N , } \end{array}$ $\begin{array} { r } { D = \sum I _ { \{ q _ { i } = 1 , t _ { i } \leq T \} } \cdot d _ { i } ) } \end{array}$ . The user derives some utility from the information, but incurs costs associated with waiting for responses and evaluating the results. Further, the servers may impose a fee per query. We now introduce notation to model these benefits and costs. Our notation is summarized in Table 1.

Utility from Information. The user’s utility from a document is a function of various attributes including relevance, novelty, and credibility (Larcker and Lessig 1980, Moenart and Souder 1996). This is consistent with the design of real-world IR systems that compute the relevance score accounting for factors such as document relevance and credibility of the source.

Table 1 Summary of Notation

$$
(q _ {i} = 1)
$$

$$
(q _ {i} = 0)
$$

$$
Q
$$

$$
(q = (q _ {1}, q _ {2}, \dots , q _ {N}))
$$

$$
T
$$

$$
(Q = \sum q _ {i})
$$

$$
t _ {i}
$$

$$
F _ {i} (\cdot)
$$

$$
d _ {i}
$$

$$
D
$$

$$
g _ {j i} (\cdot)
$$

$$
\acute {U} _ {j, i, k}
$$

$$
U _ {j, k: D}
$$

$$
\mathbf {U} _ {j}
$$

$$
j ^ {\prime} \mathrm{s}
$$

$$
k \in \{1, 2, \dots , d _ {i} \}
$$

$$
i,
$$

$$
S _ {j}
$$

$$
U _ {j, D - 1: D}, \dots , U _ {j, 1: D}))
$$

$$
(\mathbf {U} _ {j} = (U _ {j, D: D},
$$

$$
P
$$

$$
\xi_ {j}
$$

$$
\lambda_ {j}
$$

$$
\acute {A}
$$

$$
j ^ {\prime} \mathrm{s}
$$

$$
\eta_ {i}
$$

$$
j ^ {\prime} \mathrm{s}
$$

We therefore use the terms relevance score and utility interchangeably.

At the time the broker queries the servers, the utility of documents that will be returned by a server are not known and are hence treated as random variables. Once documents are retrieved from the servers, the utility—i.e., the relevance scores from the retrieved documents—can be computed by the broker. Accordingly, we assume that before the documents are retrieved, the broker only knows the probability distribution function $G _ { i i } ( \cdot )$ of user $j ^ { \prime } \mathbf { s }$ utility from a document returned by server $i \ ( g _ { j i } ( \cdot )$ is the corresponding pdf). These can be determined by the broker based on past queries. Once documents are retrieved, the relevance scores are known. $U _ { j , i , k }$ denotes the user’s utility from the kth document returned by server $i ,$ where $k \in \{ 1 , 2 , \ldots , d _ { i } \}$ . We assume that the broker displays the retrieved documents in decreasing order of relevance score, which reflects a common practice in IR systems. Given D retrieved documents, $U _ { j , k : D }$ is used to denote user $j ^ { \prime } \mathbf { s }$ utility from the document ranked k in a sorted list of documents. That is, $U _ { j , D ; D } \geq U _ { j , D - 1 ; D } \geq \cdots \geq U _ { j , 2 ; D } \geq U _ { j , 1 ; D }$ . The vector $\mathbf { U } _ { j } = ( U _ { j , D : D } , U _ { j , D - 1 : D } , \ldots , U _ { j , 1 : D } )$ denotes the relevance scores of the retrieved documents. Finally, in order to evaluate the user’s benefit from the displayed information, we need to understand the user’s stopping criterion when evaluating the displayed results. Here, as in Fuhr (1999), we assume that the user views the top P documents sequentially. The utility to the user from the top $P$ results given that D documents are retrieved is given by $\begin{array} { r } { \sum _ { k = 1 } ^ { P ^ { \smile } } U _ { j , D - k + 1 : D } . } \end{array}$ The sum of individual utilities specification is commonly assumed in the literature (Si and Callan 2004, Fuhr 1999). However, P is endogenously determined in our model; i.e., it depends on the quality of the documents displayed.

Cost of Waiting for Responses. The total waiting time for the user is primarily composed of the broker wait time, network latency, and postprocessing time. The network latency cannot be significantly influenced by the broker’s operational decisions.<sup>7</sup> Thus, we drop network latency for the purposes of our decision model because it is a variable that does not influence our decisions. Also, we assume that the postprocessing time to merge retrieved results is negligible compared to the broker’s wait time. Most merging algorithms rely on offline analysis of the IR servers during a resource representation phase, which is used to develop decision rules for merging retrieved results in a fast manner. The few approaches that require the broker to download documents from the IR servers and process them in real time (e.g., Kirsch 1995) are considered time consuming and inefficient (Si and Callan 2003). Thus, we ignore postprocessing costs in our model and represent the user’s waiting cost as $\xi _ { j } T ,$ where $\xi _ { j }$ denotes the user’s disutility of waiting 1 second and T is the broker’s wait time.<sup>8</sup> This assumes a linear waiting cost, as in Mendelson and Whang (1990). In environments where offline analysis is infeasible and significant postprocessing is necessary, our model will need to be modified to incorporate the postprocessing costs.

Cost of Evaluating Information. The user’s cognitive cost associated with comparing P results, each with A attributes, is modeled as $\lambda _ { j } A P ,$ , where $\lambda _ { j }$ is the user’s cost of evaluating one result along one attribute. This function is based on the metric for the cost of thinking proposed by Shugan (1980) that has previously been applied to measure cost of evaluating online information $( \mathrm { e . g . }$ , Montgomery et al. 2004).<sup>9</sup> The metric is based on the number of elementary information processes (EIPs) involved in processing information. Different users incur the same number of EIPs. Heterogeneity in user cognitive costs is captured by heterogeneity in $\lambda _ { j } .$ . Our use of a cognitive cost function that is linear in P is due to its common use in marketing and the tractability it affords our analytical model. In the online appendix,<sup>10</sup> we consider more complex information evaluation criteria and nonlinear cognitive cost functions.

Server-Querying Fee. Lastly, the cost incurred in querying the servers is given by $\textstyle \sum _ { i = 1 \ldots N } \eta _ { i } q _ { i }$ , where $\eta _ { i }$ is the cost of querying server i. Note that this cost can be zero $( \eta _ { i } = 0 )$ for one or more servers.<sup>11</sup> Even though the organization, rather than the specific user, incurs the query fee, we incorporate the server-querying fee in the surplus function to capture the IS manager’s objective of maximizing the net surplus from the DIR system.

Given these different terms, the net surplus (S) given the query set (q), wait time (T ), and documents evaluated (P ) is

$$
S _ {j} = \left(\sum_ {k = 1.. P} U _ {j, D - k + 1: D}\right) - \sum_ {i = 1.. N} \eta_ {i} q _ {i} - \xi_ {j} T - \lambda_ {j} A P.\tag{1}
$$

The surplus function assumes piecewise separability of the individual components (utility from information, costs of querying, waiting, and of evaluating information). Given a query, the broker makes operational decisions to maximize the expected surplus.

## 3.2. Decision Problem

We now proceed to formulate the decision problem. We model it as a two-stage sequential process. In the first stage, we determine which servers to query (q) and how long to wait for responses (T ). At the time these two decisions are made, the server response times (t ) and document relevance scores are stochastic variables. The broker sorts the retrieved results in descending order of relevance scores. In the second stage, we determine the number of documents the user will evaluate, which in turn determines the net surplus. At this decision time, the documents have already been retrieved, and thus relevance scores of documents are known. We solve this sequential optimization problem in reverse order. That is, we first estimate the number of documents evaluated by the user (P ) given a set of retrieved results. Based on the estimate, we then determine q and T .

Stage 2: Estimating Documents Evaluated by User 4P 5. It is important to determine P in order to compute the user’s benefit from the information, which in turn influences the optimal choice of q and T . In Stage 2, the query fee and waiting cost have already been incurred and are sunk at this point. To determine the user’s evaluation set, we only consider the utility from the retrieved documents and the evaluation cost. We assume that users evaluate the documents sequentially and stop once they encounter a document with utility less than the marginal evaluation cost $\lambda _ { j } A$ . Thus, starting with the document with the highest relevance score, we repeatedly add documents into the evaluation set as long as the documents offer utility greater than $\lambda _ { j } A$ . The value of P thus obtained, which we denote by $P _ { j } ( \mathbf { U } _ { j } )$ , also maximizes the user’s surplus. That is,

$$
P _ {j} (U _ {j}) = \max _ {P} \left\{\left(\sum_ {k = 1.. P} U _ {j, D - k + 1: D}\right) - \lambda_ {j} A P \mid \mathbf {U} _ {j} \right\}.\tag{2}
$$

At the time of issuing a query, the broker does not know the utilities of documents that will be returned by the different servers, and therefore does not know the exact documents that will be evaluated. The probability that a successfully retrieved document from server i will eventually be evaluated by user $j$ is $( 1 - G _ { j i } ( \lambda _ { j } A ) )$ . Thus, if server $i _ { 1 }$ stochastically dominates server $i _ { 2 } ( G _ { j i _ { 1 } } ( x ) \leq G _ { j i _ { 2 } } ( x )$ 1 ∀ x5, then the probability that a document from $i _ { 1 }$ will be in the evaluation set given that $i _ { 1 }$ has been retrieved is greater than the corresponding probability for $i _ { 2 } .$ . Further, the expected utility from any server conditional on retrieval, $\mathrm { i . e . , }$ the utility from its documents less the evaluation cost, can be computed as follows (proof in the appendix):

<sup>Lemma</sup> <sup>1.</sup> The expected utility from a server conditional on retrieval is $\begin{array} { r } { \overline { { U } } _ { j i } = d _ { i } ( \int _ { \lambda _ { j } A } ^ { \infty } ( \overset {  } { x } - \lambda _ { j } A ) g _ { j i } ( x ) d x ) } \end{array}$

Recollect that only documents that offer utility greater than $\lambda _ { j } A$ are evaluated. Thus, $\overline { { U } } _ { j i }$ is the expected surplus from the $d _ { i }$ documents returned by server i. We now apply Lemma 1 to solve the broker’s operational decisions in Stage 1 when the utility and response times are unknown.

Stage 1: Determining Servers to Query and Query Termination Time. There are clear trade-offs in choosing the servers to query and the wait time. If the broker does not query a good server, then the server is not retrieved and user surplus is unnecessarily reduced. Alternatively, if the broker queries irrelevant servers, access fees may be unnecessarily imposed. Similarly, the broker may decide to terminate a search, but a highly relevant document may have been retrieved half a second later. Alternatively, the broker may choose to wait for a server’s response, but may find that it ends up taking too long to respond, or that the actual relevance of the documents is considerably lower than anticipated. We now formulate the problem of determining q and T to address these trade-offs.

Given the solution $P _ { j } ( \mathbf { U } _ { j } )$ computed in Stage 2, the user’s realized surplus given $\mathbf { U } _ { j }$ is

$$
\begin{array}{c} S _ {j} \mid \mathbf {U} _ {j} = \Bigg \{\bigg (\sum_ {i = 1.. N} q _ {i} \cdot I _ {\{t _ {i} \leq T \}} \cdot \bigg (\sum_ {k = 1} ^ {d _ {i}} I _ {\{U _ {j, i, k} \geq \lambda_ {j} A \}} \\ \cdot (U _ {j, i, k} - \lambda_ {j} A) \bigg) \bigg) - \sum_ {i = 1.. N} \eta_ {i} q _ {i} - \xi_ {j} T \Bigg \}. \end{array}\tag{3}
$$

Where $I _ { \{ t _ { i } \leq T \} }$ is an indicator variable that identifies if server i is retrieved, and $\begin{array} { r } { \sum _ { k = 1 } ^ { d _ { i } } { I _ { \{ U _ { j , i , k } \geq \lambda _ { j } A \} } \cdot ( U _ { j , i , k } - } } \end{array}$ $\lambda _ { j } A )$ is the net utility from the documents returned by server i (i.e., utility from evaluated documents less the evaluation cost). The last two terms in (3) represent the query fee and waiting cost. At the time, the broker decides on the query set and wait time, the set of retrieved servers and the utility from their documents are unknown due to the uncertainty in the response times, $t _ { i }$ and relevance scores $U _ { j , i , k } .$ The expected surplus in Stage 1, when server response times and document utilities are unknown, is

$$
\begin{array}{l} E S _ {j} (\mathbf {q}, T) = \bigg (\sum_ {i = 1.. N} q _ {i} \cdot F _ {i} (T) \cdot E \bigg [ \sum_ {k = 1} ^ {d _ {i}} I _ {\{U _ {j, i, k} \geq \lambda_ {j} A \}} \\ \qquad \cdot (U _ {j, i, k} - \lambda_ {j} A) \bigg ] \bigg) - \sum_ {i = 1.. N} \eta_ {i} q _ {i} - \xi_ {j} T \\ = \bigg (\sum_ {i = 1.. N} q _ {i} \cdot F _ {i} (T) \cdot \overline {{U}} _ {j i} \bigg) - \sum_ {i = 1.. N} \eta_ {i} q _ {i} - \xi_ {j} T \end{array}\tag{4}
$$

where $E S _ { j } ( \mathbf { q } , T )$ denotes the expected surplus, $q _ { i }$ indicates whether server i is queried, $F _ { i } ( T )$ is the probability that the server is retrieved given that it has been queried, and $\boldsymbol { \overline { { U } } } _ { j i }$ the expected surplus from the $d _ { i }$ documents returned by server $i ,$ as specified in Lemma 1. Because the utility function is additive (sum of utility from evaluated documents) and the marginal evaluation cost is constant in our model, (4) nicely separates out each server’s net contribution to the overall surplus.<sup>12</sup> The optimization problem in Stage 1 is $\mathrm { \ g i v e n }$ by

$$
\max _ {q, T} \{E S _ {j} (\mathbf {q}, T) \}.\tag{5}
$$

The optimization problem in (5) is a stochastic mixed-integer program. Computing the first-order condition of (4) with respect to $T ,$ we get

$$
\sum_ {i = 1.. N} q _ {i} f _ {i} (T ^ {*}) \overline {{U}} _ {j i} = \xi_ {j}.\tag{6}
$$

At the same time, the expected benefit from querying server i is $F _ { i } ( T ) { \bar { U } } _ { j i }$ whereas the cost of querying it is $\eta _ { i }$ . Thus,

$$
q _ {i} ^ {*} = \left\{ \begin{array}{l l} 1 & \text { if } F _ {i} (T) \overline {{U}} _ {j i} \geq \eta_ {i}, \\ 0 & \text { otherwise }. \end{array} \right.\tag{7}
$$

<sup>Proposition</sup> <sup>1.</sup> The optimal query set and wait time are characterized by Equations (6) and (7).

Equation (6) indicates that at the optimal $T ^ { * }$ the marginal expected benefit from waiting an additional time unit is equal to the marginal cost of waiting. Equation (7) highlights that a server is queried if and only if the probability that it is retrieved times the expected utility from its evaluated documents exceeds the server’s query fee. Note that the objective function (5) need not be globally concave, so it may not be straightforward to identify the optimal joint solution of (6) and (7). We investigate the concavity below and present an algorithm to determine the optimal decision variables.

From (7), server i is queried if $F _ { i } ( T ) \geq \eta _ { i } / { \overline { { U } } } _ { j i } .$ Let $I _ { \{ F _ { i } ( T ) \geq \eta _ { i } / \overline { { U } } _ { j i } \} }$ be an indicator variable that denotes whether i is queried. Then (5) can be rewritten as follows:

$$
\begin{array}{c} \max _ {T} \Bigg \{\Bigg (\sum_ {i = 1.. N} I _ {\{F _ {i} (T) \geq \eta_ {i} / \overline {{U}} _ {j i} \}} F _ {i} (T) \overline {{U}} _ {j i} \Bigg) \\ - \sum_ {i = 1.. N} \eta_ {i} I _ {\{F _ {i} (T) \geq \eta_ {i} / \overline {{U}} _ {j i} \}} - \xi_ {j} T \Bigg \}. \end{array}\tag{8}
$$

Consider the derivative of (8) with respect to T :

$$
\begin{array}{l} \bigg (\sum_ {i = 1.. N} I _ {\{F _ {i} (T) \geq \eta_ {i} / \overline {{U}} _ {j i} \}} f _ {i} (T) \overline {{U}} _ {j i} \bigg) - \xi_ {j} \\ + \bigg (\sum_ {i = 1.. N} [ F _ {i} (T) \overline {{U}} _ {j i} - \eta_ {i} ] I _ {\{F _ {i} (T) \geq \eta_ {i} / \overline {{U}} _ {j i} \}} ^ {\prime} \bigg). \end{array}\tag{9}
$$

Thus, a small increase in T is associated with three effects. First, for the servers that are already in the query set $( I _ { \{ F _ { i } ( T ) \geq \eta _ { i } / \overline { { U } } _ { i i } \} } )$ , it increases the probability that they will respond by $f _ { i } ( T )$ , and thus there is a marginal benefit of $f _ { i } ( T ) { \bar { U } } _ { j i }$ from each of these servers. Next, there is a cost $- \dot { \xi } _ { j }$ that is the user cost of waiting an additional time unit. Finally, a small increase in T can result in an additional server being added to the query set if there exists a server with $F _ { i } ( T ) = \eta _ { i } / \bar { U } _ { j i } \stackrel { - } { - } \Delta$ . Otherwise, there is no change in the set of servers in the query set. That is, $I _ { \{ F _ { i } ( T ) \geq \eta _ { i } / \overline { { U } } _ { j i } \} } ^ { \prime }$ is generally zero except at $T = T _ { i } = F _ { i } ^ { - 1 } ( \eta _ { i } / \bar { U } _ { i i } )$ when server i gets added into the query set. Note that even though a new server enters the query set at this T and $I _ { \{ F _ { i } ( T ) \geq \eta _ { i } / \overline { { U } } _ { j i } \} } ^ { \prime }$ is nonzero, that server makes no immediate contribution to the surplus because $F _ { i } ( T ) = \eta _ { i } / \overline { { U } } _ { j i }$ for that server, and thus the third term in (9) remains zero. However, the server is now in the query set and will help increase the marginal benefit of waiting (i.e., first term in (9)) for higher values of T .

We illustrate this in Figure 2. Initially, when T is small, no server satisfies (7) and the query set is empty. Thus, there is only a marginal cost of waiting $( \bar { - } \pmb { \xi } _ { j } )$ , but no marginal benefit. At some $T = T _ { [ 1 ] } ,$ a server satisfies (7) and enters the query set resulting in a discontinuous change in the slope of the expected surplus ES . Specifically, the marginal benefit once the server has entered the query set is now given by the increase in the probability that the server responds, multiplied by the expected surplus from the server (term 1 in Equation (9)), and the marginal cost remains $- \xi _ { j }$ . If we continue to increase the broker wait time, then at some $T = T _ { [ 2 ] } \geq T _ { [ 1 ] } ,$ another server enters the query set. The marginal benefit from an increase in T now consists of the expected utility times the change in the response probability for two servers. The marginal cost remains $- \xi _ { j }$ . As we increase T , this process repeats. Clearly, the derivative of the objective function with respect to T is not defined at the boundary points $\{ T _ { [ 1 ] } , \bar { T _ { [ 2 ] } } , \dots , T _ { [ N ] } \}$ and the objective function need not be locally concave either.

Figure 2 Expected Surplus Against Broker Wait Time, T  
![](/api/attachments/UH64YKGP/fulltext/images/a1e4734daedf9cbf031716e87df5bbc7653dae918d0a0f5c6010e99b92ea9656.jpg)

Fortunately, it is possible to exploit some properties of the problem to formulate a computationally scalable algorithm to determine the optimal q and T . To do this, we first prove the following proposition in the appendix.

Proposition 2. <sub>Suppose</sub> ${ \cal T } _ { i } ~ = ~ F _ { i } ^ { - 1 } ( { \eta _ { i } } / { \overline { { U } } _ { j i } } )$ , ∀ i ∈ $\{ 1 , 2 , \ldots , N \}$ . If server l is in the optimal query set, then all servers with $T _ { i } \leq T _ { l }$ are also in the optimal query set.

<sup>Corollary</sup> <sup>1.</sup> The optimal query set is nondecreasing in the broker wait time T .

Proposition 2 simplifies the computational complexity associated with computing the expected surplus for any choice of T . For each candidate value of $T ,$ there are $2 ^ { N }$ possible query sets to consider when there are N servers. With just 30 servers, that represents over a billion combinations. However, Proposition 2 rules out most of these combinations. To apply Proposition $^ { 2 , }$ we first compute $T _ { i } = F _ { i } ^ { - 1 } ( \eta _ { i } / \overline { { U } } _ { i } )$ for all servers and sort them in an ascending order. Let $T _ { [ l ] }$ be the lth lowest $T _ { i }$ for $l \in \{ 1 , 2 , \ldots , \mathbf { \bar { N } } \}$ . For example, $T _ { [ 1 ] } = \mathrm { a r g } \mathrm { m i n } _ { i = \{ 1 . . N \} } \{ F _ { i } ^ { - 1 } ( \eta _ { i } / \overline { { U } } _ { j i } ) \}$ . For $T < T _ { [ 1 ] } ,$ the query set is empty because no server satisfies (7). For $\dot { T } \in \lbrack T _ { [ 1 ] } , T _ { [ 2 ] } ) .$ , the query set consists only of the server with the lowest $T _ { i \cdot }$ . For $T \in [ T _ { [ 2 ] } , T _ { [ 3 ] } )$ , the query set consists of the two servers with $T _ { i } \stackrel { \cdot  } { < } T _ { [ 3 ] }$ and so on. Thus, there is a unique query set associated with each $T$ as described above. This observation allows us to reduce the search space.

<sup>Corollary</sup> <sup>2.</sup> The maximum expected surplus cannot be realized at any of the boundary points $T _ { i } = F _ { i } ^ { - 1 } ( \eta _ { i } / \overline { { U } } _ { j i } )$

The proof is in the appendix. Based on Corollary $^ { 2 , }$ we now search for local maxima in each of these N regions. That is, in each of the regions $T \in [ T _ { [ i ] } , T _ { [ i + 1 ] } )$ wherein the expected surplus and its derivative are

## Figure 3 Algorithm for Determining the Query Set and Wait Time

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1. Input  $\eta_{i}, \overline{U}_{ji}, F_{i}$  for all N servers and  $\xi_{j}$  for user
2. Sort N servers in ascending order of  $T_{i} = F_{i}^{-1}(\eta_{i}/\overline{U}_{ji})$ .  $T_{[l]}$  is lth lowest  $T_{i}$ .  $T_{[N+1]} = T_{Max}$ 
3. Set Optimum_Surplus to 0 and q to  $(0,0,\ldots,0)$ 
4. Set Optimum_T to 0 and Optimum_q to  $(0,0,\ldots,0)$ 
5. Set l to 1
6. While  $T \leq T_{[Max]}$  do
7. Update q and set  $q_{i}=1$  for server with lth lowest  $T_{i}$ 
8. Set  $T = T_{[l]}$ 
9. While  $T \leq T_{[l+1]}$ 
10. If  $(\sum_{\{i|q_{i}=1}\mathcal{F}_{i}(T)\overline{\mathcal{U}}_{ji}) - \sum_{\{i|q_{i}=1\}}\eta_{i}-\xi_{j}T &gt; Optimum\_Surplus$ 
11. Set Optimum_Surplus to  $(\sum_{\{i|q_{i}=1}\mathcal{F}_{i}(T)\overline{\mathcal{U}}_{ji}) - \sum_{\{i|q_{i}=1\}}\eta_{i}-\xi_{j}T$ 
12. Set Optimum_T to T
13. Set Optimum_q to q
14. EndIf
15. Set  $T = T + \nabla T$ 
16. EndWhile
17. Set l to  $l+1$ 
18. Endwhile
19. Output Optimum_q and Optimum_T
20. Halt
</div>

continuous in $T ,$ we identify local maxima that satisfy the following necessary and sufficient conditions,

$$
\sum_{\{i  |  i\in N,  i\leq N,  T_{i}\leq T\}}f_{i}(T^{*})\overline{U}_{ji} = \xi_{j}\quad \text{and}\\ \sum_{\{i  |  i\in N,  i\leq N,  T_{i}\leq T\}}f_{i}^{\prime}(T^{*})\overline{U}_{ji} <   0.\tag{10}
$$

The global solution is given by computing the maximum among these local maxima. When the properties of $f _ { i } ( \ u )$ do not permit direct computation of the local maxima, one can use numerical techniques such as iterating through T with a small step size. An algorithm is provided in Figure 3. Because the technique requires the evaluation of N query sets rather than a search over all $2 ^ { N }$ query sets, it scales rather well with the number of candidate servers.

Proposition 3. <sub>If</sub> <sub>all</sub> $f _ { i } ( \cdot )$ are decreasing, then $E S _ { j }$ is locally concave in each of the regions $T \in [ T _ { [ i ] } ^ { \sim } , T _ { [ i + 1 ] } )$

Response times of Web servers often follow an exponential distribution that has a decreasing probability density function. In these cases, given the local concavity, more efficient techniques can be used to compute the local maxima in each of the regions $T \in \dot { [ } T _ { [ i ] } , T _ { [ i + 1 ] } )$

## 3.3. Comparative Statics

Several additional properties of the optimal solution can be analytically derived. The most important property in order to derive the comparative statics is supermodularity.

<sup>Lemma</sup> <sup>2.</sup> The broker’s objective function is supermodular in its decisions (q, T ).

The proof is in the appendix. Supermodularity implies complementarity between the decision variables. That is, having more of one variable increases the marginal returns to having more of the other. This is reflected in Equations (6) and (7). Querying more servers increases the marginal return from waiting longer. Simultaneously, a longer wait time increases the returns from querying a server. Using the properties of supermodular functions, we obtain the following results on the impact of the exogenous variables on the optimal query set and wait time (all proofs are in the appendix).

<sup>Proposition</sup> <sup>4.</sup> The optimal query set and wait time are nonincreasing in waiting cost, .

Suppose the marginal cost of waiting is denoted $\xi _ { 1 } .$ The optimal wait time, $T _ { 1 } ^ { * } { \mathrm { . } }$ , is obtained by setting the marginal cost equal to the marginal benefit of waiting as shown in Figure 4. If the marginal cost of waiting increases to $\xi _ { 2 } > \xi _ { 1 } ,$ , then this results in a decrease in the optimal wait time to $T _ { 1 } ^ { * }$ (obtained by setting the marginal benefit equal to the marginal cost, as in Figure 4). The decrease in the wait time reduces the expected benefit from querying each server. This can result in a decrease in the number of servers queried in accordance with (7). If fewer servers are queried, this in turn can result in a second-order effect. A decrease in the number of servers queried reduces the marginal benefit of waiting (denoted $\mathbf { M B } _ { 2 }$ in Figure 4). This further reduces the optimal wait time to $T _ { 3 } ^ { * } < T _ { 2 } ^ { * }$ as shown in Figure 4, and in turn affects the number of servers queried and so on. Thus, the net effect is that the query set and wait time are nonincreasing in $\xi .$

Figure 4 Effect of an Increase in Marginal Cost of Waiting 4  
![](/api/attachments/UH64YKGP/fulltext/images/07a3230a1dd6d6f318c0521fec2503fa5b361fb4cacf062f1820f2a993c30ba4.jpg)

<sup>Proposition</sup> <sup>5.</sup> The optimal query set and wait time are nonincreasing in user cognitive cost, .

<sup>Proposition</sup> <sup>6.</sup> The optimal query set and wait time are nonincreasing in access fee $\eta _ { i } , f o r$ all i.

An increase in  results in a decrease in the number of documents evaluated by a user. This reduces the marginal value of waiting and also the marginal value of querying the servers. Thus, the wait time and query set are nonincreasing in . Similarly, an increase in any server’s access fee can result in the elimination of that server from the broker’s query set. Given the complementarity between query set and wait time, this in turn reduces the optimal wait time.

## 4. Empirical Illustration of Gain from Optimal Decision Making

In this section, we use simulations to measure gains from optimal decision making. To instantiate the simulation parameters, we use data from FedStats, which is a real-world DIR application. Our choice of this application context is due to its prior use in DIR research and the availability of data.

## 4.1. Federated Search (FedStats)

FedStats is a portal that provides unified access to information and statistics from over 100 federal agencies, including NIH, USDA, and the Census Bureau. FedStats was previously designed as a singledatabase architecture with information from all agencies replicated in a central database. Since 2003, Fed-Stats has adopted a distributed architecture wherein the broker forwards the query to IR servers of different agencies and merges the results. Avrahami et al. (2006) provide a good review of the advantages of the DIR architecture.

To apply our techniques, we calibrated the relevance score and response time distributions using data gathered over 33 days in February/March 2006. Each day, our software agent queried the IR servers of 15 federal agencies and gathered server response times for 26 queries. The queries and IR servers are the same as in Avrahami et al. (2006). The mean and standard deviation of the response time of the IR servers are in Table 2. The response time of the IR servers is modeled very well as a Gamma distribution, the parameters of which were estimated using maximum-likelihood estimation (MLE). We also extracted the top 20 documents that the servers returned in response to a query and computed the centralized relevance score for each document.<sup>13</sup> The centralized relevance score reflects the expected utility of a document. Because these are computed in a centralized manner, comparison of document relevance scores across IR servers is meaningful. In the following analysis, we only focus on relevance scores computed for the following queries (crime rates, domestic violence, hate crime, homeless, suicide, unemployment rate) because they are broadly from the same topic area. Table 2 lists the mean and standard deviation of the relevance scores of retrieved documents at the servers. The relevance scores for the top six servers are well described as Gamma distributions, whereas the remaining servers have Normally distributed relevance scores. The parameters of these distributions were also estimated by MLE.

Table 2 Summary Statistics for Server Response Time and Document Relevance Scores

<table><tr><td rowspan="2">Agency</td><td colspan="2">Response time</td><td colspan="2">Relevance score</td></tr><tr><td>Mean</td><td>Std. dev.</td><td>Mean</td><td>Std. dev.</td></tr><tr><td>1 Bureau of Justice</td><td>0.41</td><td>0.81</td><td>0.2</td><td>0.12</td></tr><tr><td>2 Housing and Urban Development</td><td>1.8</td><td>4.00</td><td>0.17</td><td>0.07</td></tr><tr><td>3 ChildStats</td><td>1.7</td><td>4.50</td><td>0.2</td><td>0.04</td></tr><tr><td>4 Social Security Administration</td><td>0.27</td><td>1.09</td><td>0.1</td><td>0.07</td></tr><tr><td>5 National Science Foundation</td><td>1.14</td><td>0.33</td><td>0.06</td><td>0.06</td></tr><tr><td>6 Bureau of Economic Analysis</td><td>1.38</td><td>2.78</td><td>0.05</td><td>0.04</td></tr><tr><td>7 Economic Research Service</td><td>1.14</td><td>2.06</td><td>0.18</td><td>0.03</td></tr><tr><td>8 Bureau of Labor</td><td>0.39</td><td>1.39</td><td>0.15</td><td>0.02</td></tr><tr><td>9 National Institute of Drug Abuse</td><td>0.6</td><td>0.48</td><td>0.18</td><td>0.04</td></tr><tr><td>10 National Center for Education Stats</td><td>1.21</td><td>1.24</td><td>0.24</td><td>0.09</td></tr><tr><td>11 National Center for Health Stats</td><td>0.87</td><td>0.74</td><td>0.20</td><td>0.04</td></tr><tr><td>12 Environmental Protection Agency</td><td>0.4</td><td>1.77</td><td>0.17</td><td>0.04</td></tr><tr><td>13 Federal Reserve</td><td>1.48</td><td>0.95</td><td>0.14</td><td>0.03</td></tr><tr><td>14 National Inst. for Child Health &amp; Development</td><td>0.61</td><td>0.38</td><td>0.16</td><td>0.03</td></tr><tr><td>15 Energy Information Administration</td><td>0.88</td><td>0.41</td><td>0.02</td><td>0.004</td></tr></table>

Although the servers have a low mean response time, the variance is quite high. Further, the heterogeneity among the servers in terms of both the response time and relevance scores is worth noting. Some servers such as the NSF IR server (server #5) respond fast and have low variance in the response time. The NSF server took more than five seconds to respond in 0 out of 858 searches. Unfortunately, the documents returned by NSF do not generally have high relevance scores for queries in our topic area. In contrast, some other IR servers such as those of Housing and Urban Development (HUD) and Bureau of Economic Analysis (BEA) take much longer to respond. The HUD server took more than 10 seconds to respond in 1.63% of the searches. However,

HUD documents are generally very relevant. The BEA server took more than 10 seconds to respond in 3.2% of the searches. At the same time, BEA documents are not very relevant for queries in the chosen topic area. Hence, the broker may be better off not querying the BEA server.

## 4.2. Optimal Decisions

We now illustrate how to compute the optimal operational decisions using the FedStats data set. Even though server response time and relevance score distributions $( f _ { i } ( T ) , \bar { g } _ { j i } ( \cdot ) )$ are obtained from real-world data, servers’ query fees and the user’s waiting cost and cognitive cost need to be additionally specified. Our analytical model permits arbitrary values for these variables, but for the purposes of the simulation we use some plausible values in our base case and conduct additional sensitivity analysis. In §5, we additionally discuss how these parameters can be estimated. For our base case, we assume that the cost of evaluating a document is two and a half times the cost of waiting a second $\left( \lambda = 2 . 5 \xi \right)$ . This choice replicates the setting in Montgomery et al. (2004). We also bootstrap the value of $\xi = 0 . 1$ so that the realized values of P in our simulations are typically between 5 and 25. Finally, we set the cost of querying the servers to 0.1 for all the servers in the base case (i.e., $\eta _ { i } = 0 . 1$ for all i5, which implies that the per-query fee charged by a server is of the same order of magnitude as the cost of waiting one second and the cost of evaluating one document.<sup>14</sup> Note that the querying fees are typically known a priori and the modeler can easily plug in appropriate values during implementation.

In Table 3, we compute the expected surplus $\begin{array} { r } { \overline { { U } } _ { j i } = } \end{array}$ $\begin{array} { r } { d _ { i } ( \int _ { \lambda _ { i } A } ^ { \infty } ( x - \lambda _ { j } A ) g _ { j i } ( x ) \bar { d } x ) } \end{array}$ from each server if it is retrieved. In addition, we compute the waiting time $( T _ { i } = F _ { i } ^ { - 1 } ( \eta _ { i } / \overline { { U } } _ { j i } ) )$ at which it is optimal to query the server. Interestingly, only three servers, namely those of the Bureau of Justice, Housing and Urban Development, and National Center for Educational Stats, have a finite $T _ { i }$ for the topic area and above parameters.

Table 3 Expected Surplus and Minimum Wait Time to Consider Querying a Server

<table><tr><td>Agency</td><td>Expected surplus $(\overline{U}_{ji})$ </td><td>Minimum wait time needed to query $(T_i = F_i^{-1}(\eta_i/\overline{U}_{ji}))$ </td></tr><tr><td>1 Bureau of Justice</td><td>0.583</td><td>0.001</td></tr><tr><td>2 Housing and Urban Development</td><td>0.128</td><td>2.076</td></tr><tr><td>3 ChildStats</td><td>0.051</td><td>∞</td></tr><tr><td>4 Social Security Administration</td><td>0.045</td><td>∞</td></tr><tr><td>5 National Science Foundation</td><td>0.019</td><td>∞</td></tr><tr><td>6 Bureau of Economic Analysis</td><td>0.001</td><td>∞</td></tr><tr><td>7 Economic Research Service</td><td>0.002</td><td>∞</td></tr><tr><td>8 Bureau of Labor</td><td>0.000</td><td>∞</td></tr><tr><td>9 National Institute of Drug Abuse</td><td>0.013</td><td>∞</td></tr><tr><td>10 National Center for Education Stats</td><td>0.622</td><td>0.198</td></tr><tr><td>11 National Center for Health Stats</td><td>0.040</td><td>∞</td></tr><tr><td>12 Environmental Protection Agency</td><td>0.007</td><td>∞</td></tr><tr><td>13 Federal Reserve</td><td>0.000</td><td>∞</td></tr><tr><td>14 National Inst. for Child Health &amp; Development</td><td>0.000</td><td>∞</td></tr><tr><td>15 Energy Information Administration</td><td>0.000</td><td>∞</td></tr></table>

The expected surplus for other servers is not sufficient to offset the query fee even if the broker wait time is high enough. If the query fees are reduced to $\eta _ { i } = 0 . 0 2 5$ , then servers 3, 4, and 11 may also be worth querying if the broker wait time is reasonably high (i.e., $\overline { { U } } _ { j i } > 0 . 0 2 5$ for these servers). The table can be used to quickly identify the servers to query for any arbitrary set of querying costs $\left\{ \eta _ { 1 } , \eta _ { 2 } , \dots , \eta _ { N } \right\}$

Figure 5 plots the expected surplus against the wait time. For $\hat { T } < 0 . 0 0 1$ , the query set is empty and the expected surplus is negative. For $T \in [ \bar { 0 . 0 0 1 } , 0 . 1 9 8 )$ the query set consists of only server 1. At $T = 0 . 1 9 8$ server 10 also enters the query set and we observe a sudden increase in the slope of the expected surplus function. Similarly, at $\bar { T } = 2 . 0 7 6 ,$ server 2 also enters the query set. The query set does not change subsequently. The expected surplus is maximized at $T ^ { * } = 2 \bar { . } 3 1 8$ , and the optimal query set consists of servers 1, 2, and 10. These operational decisions can be easily computed given data on past performance of the servers and the user parameters.

We now conduct some sensitivity analysis to determine the impact of exogenous parameters on the expected surplus at the optimal operational decisions. Figure 6 presents the impact of the waiting cost and the query fee. First we compute the expected surplus obtained from the operational algorithm derived in §3 (this is labeled “Algorithm”). Simultaneously, we also compute the expected surplus obtained from a simple but reasonable heuristic in which we query all servers and wait for five seconds for the servers to respond (labeled “Heuristic”). Clearly, an increase in the waiting cost or the query fee decreases the expected surplus even if the operational decisions are optimally adjusted. At the same time, we observe that the decay in the expected surplus under optimal operational decisions is not as drastic as that observed with the naïve heuristic. The algorithm is successful in responding to an increase the user waiting cost or server fees and ensures that the expected surplus continues to remain positive. In contrast, the naïve heuristic quickly deteriorates in performance when there are nontrivial costs.

Figure 5 Expected Surplus Against Broker Wait Time (Assuming Optimal Query Set q<sup>∗</sup>4T 5)  
![](/api/attachments/UH64YKGP/fulltext/images/13d86167ce6fd90b88f75334dada695d888d90224dfbe51a4c7f26540c4c84fd.jpg)

Figure 7 presents a similar plot of the expected surplus against the cognitive cost of evaluating information and the user waiting cost. It is evident that the cognitive cost can have a significant impact on the

Figure 6 Impact of Waiting and Querying Costs on Expected Surplus Under Optimal Operational Decisions and Naïve Heuristic  
![](/api/attachments/UH64YKGP/fulltext/images/8d74757c1dffa63457140d2ed38e75bbebb130aef84ba0f7cfa673f3f6cf9d17.jpg)

Figure 7 Impact of Waiting and Cognitive Costs on Expected Surplus  
![](/api/attachments/UH64YKGP/fulltext/images/f0cbf020b05e130f39fab046859ea7b2c1ebec0b51ac6ec58dbc991b431ecaf5.jpg)  
expected surplus. This is because the parameter $\lambda _ { j }$ impacts the value realized from each and every document that is retrieved as opposed to the waiting cost (incurred once for the entire query) and the query fees (once per server). Yet again, the expected surplus under optimal operational decisions can be significantly higher than that under the naïve heuristic when the costs are nontrivial.

## 5. Discussion and Conclusions

In this paper, we formulated the decision problem for a broker in distributed IR, derived a solution that can be implemented in a computationally efficient manner, and extended the approach to more complex decision environments. We demonstrated that user surplus can be significantly enhanced by using the approach. From a managerial standpoint, the key insight is that improved user modeling can help managers in deploying DIR systems that generate greater user satisfaction. The design of intelligent information systems will contribute to increased adoption of systems, and in turn generate higher return on investment from enterprise IS.

We now discuss implementation challenges with the proposed approach and conclude by discussing future directions for research. Our model assumes that it is possible to estimate the user utility (i.e., estimate ${ U _ { j k } } , { \xi } _ { j } , { \lambda } _ { j } )$ . This raises two important questions tied to implementation. The first relates to techniques that can be employed to estimate these parameters and the granularity at which these parameters can be estimated. A second question relates to the impact of uncertainty in the estimated parameters.

With regard to techniques for estimating user preferences, there are a number of approaches that can be used in implementing the model. In the IR community, a recent focus has been the design of personalized IR systems that personalize search results using models of user interests based on previously issued queries and previously visited Web pages (Teevan et al. 2005). These techniques allow the computation of user-specific relevance scores. An additional approach available is the use of models that estimate utility weights using prior choice/clicks data. Examples include the individual-level multinomial probit model of Rossi et al. (1996), estimated using a hierarchical Bayesian approach, and the random-effects approach (e.g., see Gonul and Srinivasan 1993). An alternative to individual-level parameter estimation is to identify preferences and composition of different user segments. In an enterprise setting, a segment may be users within a division. In cases where segments are not easily specified in advance, latent segments and their preferences can be estimated (see Kamakura and Russell 1989 and Andrews et al. 2002). In these models, user preferences can be represented by those of the user’s latent segment. Recently, flexible mixture models have been proposed in which a user may belong to multiple segments, and the user’s preferences represented as a continuous mixture of the preferences of each segment to which the user belongs (e.g., Varki and Chintagunta 2004 and a similar clustering model by Blei et al. 2003). Finally, another appealing option is the use of conjoint analysis. In conjoint analysis, respondents are presented with options that simultaneously vary two or more attributes and are asked to indicate their preferences among these options (e.g., one option may entail waiting for an additional second and another may entail evaluating an additional document). Respondents’ preference orderings are then used to estimate the utility part-worths. The technique has been widely adopted by marketing researchers and practitioners (see Green et al. 2001 for a detailed survey). A conjoint task can be designed for users of a DIR system to estimate how users trade-off the benefit from a document with cognitive and waiting costs.

Another important issue relates to uncertainty in the estimates. That is, what is the impact of errors in $U _ { j k } , \xi _ { j } ,$ or $\lambda _ { j } ?$ If the errors are i.i.d. with zero mean, then the optimal decisions need not change as long as the expected surplus function in §3 is additive and piecewise separable. However, it may be possible to exploit the error structure under some circumstances. Furthermore, it would be useful to conduct sensitivity analysis to measure the impact of small changes in parameters on the optimal decisions. This can help determine whether to strictly implement the decisions generated by the model or to use the solution as an indicator of the neighborhood in which the optimal solution may lie.

There are several interesting avenues for future research. In this paper, we considered an IR broker that is interested in maximizing net surplus without any other constraints. There may be other objective functions and resource constraints worth modeling. Future work can explore these alternative formulations, including those in which the broker’s objective and the user’s objective are not perfectly aligned. One of the key assumptions that ensure tractability of the current model is the constant marginal cost of evaluating documents. When the cost function is convex, the net utility from a server depends on the relative position of its documents in the display set. This in turn implies that the net utility from a server depends on which other servers are retrieved. Such interserver interactions make the analytical treatment of the problem difficult. Nevertheless, simulation results presented in the online appendix suggest that the insights from the current model can be applied and heuristics based on the analytical results can produce reasonably good results.

We restricted our analysis to federated search, wherein the overlap in results across servers is minimal. Another interesting extension will be to develop algorithms for environments in which there is considerable overlap across servers. Another interesting direction is to extend the formulation to hierarchical environments, i.e., DIR systems in which a metabroker queries multiple brokers that in turn query individual IR servers. Finally, we considered a static wait time for the broker. The approach does not account for information a broker may gather in real time during a specific retrieval. For example, during a particular search, a broker may have retrieved the top few documents early on but will end up waiting until the recommended waiting period has elapsed or all servers have responded. In this situation, the broker may be better off terminating the search early because it knows that the servers expected to be most relevant have already responded. Hosanagar (2005) presents an adaptive approach to allow the broker to adjust the decisions in real time. Other adaptive techniques and metaheuristics to evaluate these alternatives can also prove useful.

## 6. Electronic Companion

An electronic companion to this paper is available as part of the online version that can be found at http:// isr.journal.informs.org/.

## Acknowledgments

Luo Si provided valuable guidance regarding design of Fedstats’ DIR system. In addition, the author thanks Monique Guignard-Spielberg, Ramayya Krishnan, Gautam Pant, participants of the 2005 ACM SIGIR conference, and anonymous referees for helpful discussions on prior versions of this work.

## Appendix

<sup>Lemma</sup> <sup>1.</sup> The expected utility from a server conditional on retrieval is $\begin{array} { r } { \overline { { U } } _ { j i } = d _ { i } ( \dot { \int _ { \lambda _ { i } A } ^ { \infty } } ( x - \lambda _ { j } A ) \dot { g } _ { j i } ( x ) d x ) } \end{array}$

<sup>Proof.</sup> Based on the stage 2 analysis, every document from a retrieved server that has utility $U _ { j k } > \lambda _ { j } A$ is evaluated. The remaining documents returned by a retrieved server are not evaluated by the user. Thus, for every server that is retrieved, the sum total of the utility from all evaluated documents less the cognitive cost of evaluation is

$$
\begin{array}{l} \overline {{U}} _ {j i} = d _ {i} \left(G _ {i} \left(\lambda_ {j} A\right) \cdot 0 + \int_ {\lambda_ {j} A} ^ {\infty} x g _ {j i} (x) d x - \lambda_ {j} A \int_ {\lambda_ {j} A} ^ {\infty} g _ {j i} (x) d x\right) \\ = d _ {i} \left(\int_ {\lambda_ {j} A} ^ {\infty} \left(x - \lambda_ {j} A\right) g _ {j i} (x) d x\right). \end{array} \tag {1}\tag{11}
$$

In (11), $G _ { i } ( \lambda _ { j } A )$ is the probability that a document returned by server i has utility $U _ { j k } \le \dot { \lambda } _ { j } A$ . Such a document is not evaluated, and hence provides no utility to the user. $\textstyle { \int _ { \lambda _ { i } A } ^ { \infty } x g _ { j i } ( x ) }$ dx is the expected utility from a document that satisfies the evaluation threshold $U _ { j k } > \lambda _ { j } A$ . Finally, $\textstyle { \int _ { \lambda _ { i } A } ^ { \infty } g _ { j i } ( x ) }$ dx is the probability that a document will be evaluated. Thus, $\begin{array} { r } { \overline { { U } } _ { j i } = d _ { i } ( \int _ { \lambda _ { i } A } ^ { \infty } ( x - \lambda _ { j } A ) g _ { j i } ( x ) d x ) } \end{array}$ is net utility realized from the $d _ { i }$ documents returned by server i less the cognitive cost. <sup></sup>

Proposition 2. <sub>Suppose</sub> $T _ { i } = F _ { i } ^ { - 1 } ( \eta _ { i } / \overline { { U } } _ { i } )$ . If server l is in the optimal query set, then all servers with $\begin{array} { r } { T _ { i } \leq T _ { l } } \end{array}$ are also in the optimal query set.

<sup>Proof.</sup> Equation (7) indicates that server i is queried if $F _ { i } ( T ) \overline { { U } } _ { j i } \geq \eta _ { i }$ . That ${ \mathrm { i } } \mathbf { s } ,$ server i is queried if

$$
T \geq F _ {i} ^ {- 1} (\eta_ {i} / \bar {U} _ {i j}) = T _ {i}.\tag{12}
$$

Suppose server l is in the optimal query set. It then follows that the following condition is met: $T \geq T _ { l }$ . In turn, this implies that (12) is satisfied for all servers with $T _ { i } \leq T _ { l } .$ , and thus all such servers are also in the optimal query set. <sup></sup>

<sup>Corollary</sup> <sup>1.</sup> The optimal query set is nondecreasing in the broker wait time T .

<sup>Proof.</sup> As the broker wait time T increases, any server that already satisfies (12) continues to do so. The result is immediate. <sup></sup>

<sup>Corollary</sup> <sup>2.</sup> The maximum expected surplus cannot be realized at any of the boundary points $T _ { i } = F _ { i } ^ { - 1 } \big ( \dot { \eta } _ { i } / \overline { { U } } _ { j i } \big )$

<sup>Proof.</sup> From Equation (7), we know that server i is queried only when $T \geq T _ { i } = \dot { F } _ { i } ^ { - 1 } ( \eta _ { i } / \hat { U } _ { i i } )$ . Clearly, if $\begin{array} { r } { \overline { { U } } _ { j i } = 0 , } \end{array}$ then the server is never queried. So, we only focus on the servers with $\begin{array} { r } { \overline { { U } } _ { j i } > 0 } \end{array}$ . Let us consider one of the boundary points $T = T _ { l } = F _ { l } ^ { - 1 } ( \eta _ { l } / \overline { { U } } _ { i l } )$ 5. Recollect from Equation (9) that the slope of the expected surplus at any given T is

$$
\begin{array}{l} \bigg (\sum_ {i = 1.. N} I _ {\{F _ {i} (T) \geq \eta_ {i} / \bar {U} _ {j i} \}} f _ {i} (T) \overline {{U}} _ {j i} \bigg) - \xi_ {j} \\ \qquad + \bigg (\sum_ {i = 1.. N} [ F _ {i} (T) \overline {{U}} _ {j i} - \eta_ {i} ] I _ {\{F _ {i} (T) \geq \eta_ {i} / \bar {U} _ {j i} \}} ^ {\prime} \bigg). \end{array}\tag{13}
$$

Thus, the slope of the expected surplus with respect to T at $T = T _ { l } ^ { - }$ is

$$
\sum_ {\{i \mid i \in \mathrm{N},   i \leq N,   T _ {i} \leq T _ {l} ^ {-} \}} f _ {i} (T _ {l}) \overline {{U}} _ {j i} - \xi_ {j}.\tag{14}
$$

Similarly, the slope at $T = T _ { l } ^ { + }$ is

$$
\begin{array}{c} \sum_ {\{i \mid i \in \mathrm{N},   i \leq N,   T _ {i} \leq T _ {l} ^ {+} \}} f _ {i} (T _ {l}) \overline {{U}} _ {j i} - \xi_ {j} \\ = \bigg \{\sum_ {\{i \mid i \in \mathrm{N},   i \leq N,   T _ {i} \leq T _ {l} ^ {-} \}} f _ {i} (T _ {l}) \overline {{U}} _ {j i} - \xi_ {j} \bigg \} + f _ {l} (T _ {l}) \overline {{U}} _ {j l}. \end{array}\tag{15}
$$

Given that the pdf $f _ { l } ( T _ { l } )$ and $\boldsymbol { \overline { { U } } } _ { j i }$ are always positive, the slope at $T = T _ { l } ^ { + }$ is always greater than the slope at $T = T _ { l } ^ { - }$ for all l. If $T _ { l }$ represents a local maximum for the expected surplus, it follows that the slope at $T _ { l } ^ { - }$ is greater than or equal to zero. Given that the surplus at $T _ { l } ^ { + }$ is even higher, it follows that $E S _ { i } ( T _ { l } ^ { + } ) > E S _ { i } ( T _ { l } ^ { - } )$ 5 whenever $T _ { l }$ is a local maximum. Thus, $T _ { l }$ cannot be the global maximum. <sup></sup>

Proposition 3. <sub>If</sub> <sub>all</sub> $f _ { i } ( \cdot )$ are decreasing, then S is locally concave in each of the regions $T \in [ T _ { [ l ] } , \ T _ { [ l + 1 ] } )$

<sup>Proof.</sup> Consider any region $T \in [ T _ { [ l ] } , T _ { [ l + 1 ] } )$ . In this region a total of l servers are queried. The specific query set is also identified by ordering the servers in increasing order of $T _ { i } =$ $F _ { i } ^ { - 1 } ( \eta _ { i } / \overline { { U } } _ { j i } ) ,$ as described earlier. The second-order derivative of the expected surplus with respect to T is given by

$$
\sum_ {\{i \mid i \in \mathbf {N},   i \leq N,   T _ {i} \leq T \}} f _ {i} ^ {\prime} (T ^ {*}) \overline {{U}} _ {j i}.\tag{16}
$$

Because all $f _ { i } ( \cdot )$ are decreasing and all $\overline { { U } } _ { j i }$ are positive, it follows that the above equation is necessarily negative. Thus, S is locally concave in each region $T \in [ T _ { [ l ] } , \overline { { T _ { [ l + 1 ] } } } )$ . 

<sup>Lemma</sup> <sup>2.</sup> The broker’s objective function is supermodular in its decisions $( \mathbf { q } , T )$ .

<sup>Proof.</sup> Define an $( N ~ + ~ 1 )$ )-dimensional sublattice $( q _ { 1 } , q _ { 2 } , \dots , q _ { N } , T )$ such that $q _ { i } \in \{ 0 , 1 \}$ and T is a finite real number. The objective function (i.e., the expected surplus) is denoted $f ( q _ { 1 } , q _ { 2 } , \dots , q _ { N } , T )$ . Consider two points $( q _ { 1 } , q _ { 2 } , \dots , q _ { N } , T )$ and $( q _ { 1 } ^ { \prime } , q _ { 2 } ^ { \prime } , \dots , q _ { N } ^ { \prime } , T ^ { \prime } )$ in this sublattice. Denote these points by $( q , T )$ and $( q ^ { \prime } , T ^ { \prime } )$ 5. Assume without loss of generality that $T \geq T ^ { \prime }$

The objective function is supermodular in the decision variables if $f [ ( q , T ) \vee ( q ^ { \prime } , \dot { T ^ { \prime } } ) ] + f [ ( q , T ) \wedge ( q ^ { \prime } , T ^ { \prime } ) ] \geq$ $f ( q , T ) + f ( q ^ { \prime } , T ^ { \prime } )$ , where $\left( q , T \right) \lor \left( q ^ { \prime } , T ^ { \prime } \right)$ is the join of $( q , T )$ and $( q ^ { \prime } , T ^ { \prime } ) .$ , and $\left( q , T \right) \wedge \left( q ^ { \prime } , T ^ { \prime } \right)$ is the meet of the two points (Topkis 1998). The join is given by $( q , T ) \vee$ $( q ^ { \prime } , \dot { T ^ { \prime } } ) = ( \mathrm { { m a x } } \dot { [ { q } _ { 1 } , { q } _ { 1 } ^ { \prime } ] } , { \mathrm { m a x } } [ { { q } _ { 2 } , { q } _ { 2 } ^ { \prime } } \dot { ] } , \dots , { \mathrm { m a x } } \dot { [ { q } _ { N } , { q } _ { N } ^ { \prime } ] } , \dot { T } )$ and is denoted $( { \overline { { q } } } , T )$ . Similarly, the meet is given by $( q , T ) \wedge$ $( q ^ { \prime } , T ^ { \prime } ) = ( \mathrm { m i n } [ q _ { 1 } , q _ { 1 } ^ { \prime } ] , \mathrm { m i n } [ q _ { 2 } , q _ { 2 } ^ { \prime } ] , \dots , \mathrm { m i n } [ q _ { N } , q _ { N } ^ { \prime } ] , \dot { T ^ { \prime } } )$ and is denoted $( \overline { { q , } } T ^ { \prime } )$ . Note that each of the $q _ { i }$ is a binary variable. Hence, by definition,

$$
\overrightarrow {q _ {i}} + \overleftarrow {q _ {i}} = q _ {i} + q _ {i} ^ {\prime};\tag{17}
$$

$$
\begin{array}{l} f (\overleftarrow {q}, T ^ {\prime}) + f (\overrightarrow {q}, T) = \left(\sum_ {i = 1.. N} \overleftarrow {q _ {i}} F _ {i} (T ^ {\prime}) \overline {{U}} _ {j i} + \sum_ {i = 1.. N} \overrightarrow {q _ {i}} F _ {i} (T) \overline {{U}} _ {j i}\right) \\ - \xi (T + T ^ {\prime}) - \sum_ {i = 1.. N} \eta_ {i} (\overleftarrow {q _ {i}} + \overrightarrow {q _ {i}}). \end{array} \tag {18}
$$

Using (18),

$$
\begin{array}{l} f (\overleftarrow {q}, T ^ {\prime}) + f (\overrightarrow {q}, T) - f (q, T) - f (q ^ {\prime}, T ^ {\prime}) \\ = \sum_ {i = 1.. N} \overline {{U}} _ {j i} (\overleftarrow {q _ {i}} F _ {i} (T ^ {\prime}) + \overrightarrow {q _ {i}} F _ {i} (T) - q _ {i} F _ {i} (T) - q _ {i} ^ {\prime} F _ {i} (T ^ {\prime})). \end{array}\tag{19}
$$

To prove supermodularity, we then need to show that

$$
\overleftarrow {q _ {i}} F _ {i} (T ^ {\prime}) + \overrightarrow {q _ {i}} F _ {i} (T) \geq q _ {i} F _ {i} (T) + q _ {i} ^ {\prime} F _ {i} (T ^ {\prime}).\tag{20}
$$

That is, we need to show

$$
(\overrightarrow {q _ {i}} - q _ {i}) F _ {i} (T) \geq (q _ {i} ^ {\prime} - \overleftarrow {q _ {i}}) F _ {i} (T ^ {\prime}).\tag{21}
$$

Substituting $q _ { i } ^ { \prime } = \overline { { q _ { i } } } + \overline { { q _ { i } } } - q _ { i }$ from (17) into (21),

$$
(\overrightarrow {q _ {i}} - q _ {i}) F _ {i} (T) \geq (\overrightarrow {q _ {i}} - q _ {i}) F _ {i} (T ^ {\prime}).\tag{22}
$$

We know that (22) is always true because $\widehat { q _ { i } } \geq q _ { i }$ and $T \geq T ^ { \prime }$ Thus, it follows that the objective function is supermodular in $( q _ { 1 } , q _ { 2 } , \dots , q _ { N } , T )$ . 

<sup>Proposition</sup> <sup>4.</sup> The optimal query set and wait time are nonincreasing in user cost of waiting, .

<sup>Proof.</sup> Given that the objective function is supermodular in $( q _ { 1 } , q _ { 2 } , \dots , q _ { N } , T )$ , it would suffice to show that the function exhibits decreasing differences in $( q _ { 1 } , q _ { 2 } , \dots , q _ { N } , T , \xi )$ (Topkis 1998). The surplus function exhibits decreasing differences if, for all $( q , \bar { T } ) \geq ( q ^ { \prime } , T ^ { \prime } )$ and $\xi \ge \xi ^ { \prime } .$

$$
f (q, T, \xi) - f (q, T, \xi^ {\prime}) \leq f (q ^ {\prime}, T ^ {\prime}, \xi) - f (q ^ {\prime}, T ^ {\prime}, \xi^ {\prime}).\tag{23}
$$

That is, we need to show

$$
- \xi T + \xi^ {\prime} T \leq - \xi T ^ {\prime} + \xi^ {\prime} T ^ {\prime}\tag{24}
$$

$$
\text { or } T \geq T ^ {\prime};\tag{25}
$$

(25) is true by definition, implying that the optimal decisions are nonincreasing in $\xi . \bar { \ } \dot { \ } \dot { \ } $

<sup>Proposition</sup> <sup>5.</sup> The optimal query set and wait time are nonincreasing in user cognitive cost, $\lambda _ { j }$

<sup>Proof.</sup> Before we prove this proposition, we first prove that $\begin{array} { r } { \bar { U } _ { j i } = d _ { i } ( \int _ { \lambda _ { i } A } ^ { \infty } ( x - \dot { \lambda } _ { j } A ) g _ { j i } ( x ) \dot { d x } ) } \end{array}$ is decreasing in $\lambda _ { j } .$ . Suppose $\lambda \geq \lambda ^ { \prime }$ . Then we have

$$
\begin{array}{c} \overline {{U}} _ {j i} (\lambda_ {j} ^ {\prime}) = d _ {i} \bigg (\int_ {\lambda_ {j} ^ {\prime} A} ^ {\infty} (x - \lambda_ {j} ^ {\prime} A) g _ {j i} (x) d x \bigg) \\ = d _ {i} \bigg (\int_ {\lambda_ {j} ^ {\prime} A} ^ {\lambda_ {j} A} (x - \lambda_ {j} ^ {\prime} A) g _ {j i} (x) d x \\ + \int_ {\lambda_ {j} A} ^ {\infty} (x - \lambda_ {j} ^ {\prime} A) g _ {j i} (x) d x \bigg) \end{array}\tag{26}
$$

(27)

$$
\begin{array}{l} = d _ {i} \bigg (\int_ {\lambda_ {j} ^ {\prime} A} ^ {\lambda_ {j} A} (x - \lambda_ {j} ^ {\prime} A) g _ {j i} (x) d x \\ \qquad + \int_ {\lambda_ {j} A} ^ {\infty} (x - \lambda_ {j} A + \lambda_ {j} A - \lambda_ {j} ^ {\prime} A) g _ {j i} (x) d x \bigg) \\ = d _ {i} \bigg (\int_ {\lambda_ {j} ^ {\prime} A} ^ {\lambda_ {j} A} (x - \lambda_ {j} ^ {\prime} A) g _ {j i} (x) d x + \int_ {\lambda_ {j} A} ^ {\infty} (\lambda_ {j} A - \lambda_ {j} ^ {\prime} A) g _ {j i} (x) d x \\ \qquad + \int_ {\lambda_ {j} A} ^ {\infty} (x - \lambda_ {j} A) g _ {j i} (x) d x \bigg) \\ = d _ {i} \bigg (\int_ {\lambda_ {j} ^ {\prime} A} ^ {\lambda_ {j} A} (x - \lambda_ {j} ^ {\prime} A) g _ {j i} (x) d x \\ \qquad + \int_ {\lambda_ {j} A} ^ {\infty} (\lambda_ {j} A - \lambda_ {j} ^ {\prime} A) g _ {j i} (x) d x \bigg) + \overline {{U}} _ {j i} (\lambda_ {j}). \end{array}\tag{28}
$$

<sub>i</sub>4x5dx

(29)

(30)

Note that both the integrals above are positive. Thus, $\overline { { U } } _ { j i } ( \lambda _ { j } ^ { \prime } ) \geq \overline { { U } } _ { j i } ( \lambda _ { j } )$ for $\lambda \geq \lambda ^ { \prime }$ . Thus, $\overline { { U } } _ { j i }$ is decreasing in $\lambda _ { j }$ . We now proceed to prove Proposition 5.

To prove Proposition 5, we need to show that the surplus function exhibits decreasing differences in $( q _ { 1 } , q _ { 2 } , . . , q _ { N } , T , \lambda )$ . This is true ${ \mathrm { i f } } ,$ for all $\left( q , T \right) \geq \left( q ^ { \prime } , T ^ { \prime } \right)$ and $\lambda \ge \lambda ^ { \prime }$

$$
f (q, T, \lambda) - f (q, T, \lambda^ {\prime}) \leq f (q ^ {\prime}, T ^ {\prime}, \lambda) - f (q ^ {\prime}, T ^ {\prime}, \lambda^ {\prime}).\tag{31}
$$

Substituting the surplus function and simplifying,

$$
\begin{array}{l} \sum_ {i = 1.. N} q _ {i} F _ {i} (T) \overline {{U}} _ {j i} (\lambda_ {j}) - \sum_ {i = 1.. N} q _ {i} F _ {i} (T) \overline {{U}} _ {j i} (\lambda_ {j} ^ {\prime}) \\ \leq \sum_ {i = 1.. N} q _ {i} ^ {\prime} F _ {i} (T ^ {\prime}) \overline {{U}} _ {j i} (\lambda_ {j}) - \sum_ {i = 1.. N} q _ {i} ^ {\prime} F _ {i} (T ^ {\prime}) \overline {{U}} _ {j i} (\lambda_ {j} ^ {\prime}) \end{array}\tag{32}
$$

or

$$
\begin{array}{l} \sum_ {i = 1.. N} (q _ {i} F _ {i} (T) - q _ {i} ^ {\prime} F _ {i} (T ^ {\prime})) \overline {{U}} _ {j i} (\lambda_ {j}) \\ \leq \sum_ {i = 1.. N} (q _ {i} F _ {i} (T) - q _ {i} ^ {\prime} F _ {i} (T ^ {\prime})) \overline {{U}} _ {j i} (\lambda_ {j} ^ {\prime}). \end{array}\tag{33}
$$

Given that $\textstyle { \overline { { U } } } _ { j i }$ is decreasing in $\lambda _ { j } ,$ Equation (33) is satisfied by definition of $( q ^ { \prime } , T ^ { \prime } , \lambda ^ { \prime } )$ . Thus, Proposition 5 is true. <sup></sup>

<sup>Proposition</sup> <sup>6.</sup> The optimal query set and wait time are nonincreasing in access fee  , for all i.

<sup>Proof.</sup> The surplus function exhibits decreasing differences if for all $( q , \mathsf { \bar { T } } ) \geq ( q ^ { \prime } , T ^ { \prime } )$ 5 and $\eta \geq \eta ^ { \prime }$ 1

$$
f (q, T, \eta) - f (q, T, \eta^ {\prime}) \leq f (q ^ {\prime}, T ^ {\prime}, \eta) - f (q ^ {\prime}, T ^ {\prime}, \eta^ {\prime}).\tag{34}
$$

Note that  is a vector (just like q). Substituting the surplus function and simplifying,

$$
- \sum_ {i = 1.. N} \eta_ {i} q _ {i} + \sum_ {i = 1.. N} \eta_ {i} ^ {\prime} q _ {i} \leq - \sum_ {i = 1.. N} \eta_ {i} q _ {i} ^ {\prime} + \sum_ {i = 1.. N} \eta_ {i} ^ {\prime} q _ {i} ^ {\prime},\tag{35}
$$

$$
- \sum_ {i = 1.. N} (\eta_ {i} - \eta_ {i} ^ {\prime}) q _ {i} \leq - \sum_ {i = 1.. N} (\eta_ {i} - \eta_ {i} ^ {\prime}) q _ {i} ^ {\prime}.\tag{36}
$$

Because $\eta _ { i } \geq \eta _ { i } ^ { \prime }$ and $q _ { i } \geq q _ { i } ^ { \prime }$ for all i, (36) is always true. Thus, Proposition 6 holds. <sup></sup>

## References

Al-Natour, S., I. Benbasat, R. T. Cenfetelli. 2006. The role of design characteristics in shaping perceptions of similarity: The case of online shopping assistants. J. Assoc. Inform. Systems 7(12) 821–861.

Andrews, R. L., A. Ainslie, I. S. Currim. 2002. An empirical comparison of logit choice models with discrete versus continuous representations of heterogeneity. J. Marketing Res. 39 479–487.

Aslam, J. A., M. Montague. 2001. Models for metasearch. Proc. 23rd Annual ACM SIGIR Conf. Res. Development Inform. Retrieval, New Orleans.

Avrahami, T. T., L. Yao, L. Si, J. Callan. 2006. The FedLemur project: Federated search in the real world. J. Amer. Soc. Inform. Sci. Tech. 57(3) 347–358.

Baeza-Yates, R., B. Ribeiro-Neto, eds. 1999. Modern Information Retreival. ACM Press, New York, 249–254.

Basartan, Y. 2001. Amazon versus the shopbot: An experiment about how to improve the shopbots. Working paper, Graduate School of Industrial Administration, Carnegie Mellon University, Pittsburgh.

Bettman, J. R., M. F. Luce, J. W. Payne. 1998. Constructive consumer choice processes. J. Consumer Res. 25 187–217.

Bhattacherjee, A. 2001. An empirical analysis of the antecedents of electronic commerce service continuance. Decision Support Systems 32 201–214.

Blei, D., A. Ng, M. Jordan. 2003. Latent Dirichlet allocation. J. Machine Learning Res. 3 993–1002.

Browne, G., M. Pitts, J. Wetherbe. 2007. Cognitive stopping rules for terminating information search in online tasks. MIS Quart. 31(1) 89–104.

Byrne, M. D. 2007. Cognitive architectures. A. Sears, J. Jacko, eds. The Human-Computer Interaction Handbook, 2nd ed. Lawrence Erlbaum Associates, Mahwah, NJ, 93–113.

Callan, J. P., Z. Lu, W. B. Croft. 1995. Searching distributed collections with inference networks. Proc. 18th Annual Internat. ACM SIGIR Conf., Seattle.

Card, S., T. Moran, A. Newell. 1983. The Psychology of Human-Computer Interaction. Lawrence Erlbaum Associates, Hillsdale, NJ.

Chase, W. G. 1978. Elementary information processes. W. K. Estes, ed. Handbook of Learning and Cognitive Processes, Vol. 5. Human Information Processing. Lawrence Erlbaum Associates, Hillsdale, NJ, 19–90.

Davis, F. D., R. P. Bagozzi, P. R. Warshaw. 1989. User acceptance of computer-technology: A comparison of two theoretical models. Management Sci. 35(8) 982–1003.

Dellaert, B., B. Kahn. 1999. How tolerable is delay? Consumers’ evaluations of internet web sites after waiting. J. Interactive Marketing 13(1) 41–54.

Dey, D. 2003. Record matching in data warehouses: A decision model for data consolidation. Oper. Res. 51(2) 240–254.

Dey, D., S. Sarkar, P. De. 1998. A probabilistic decision model for entity matching in heterogeneous databases. Management Sci. 44(10) 1379–1395.

Etzioni, O., S. Hanks, T. Jiang, R. Karp, O. Madani, O. Waarts. 1996. Efficient information gathering on the Internet. Proc. Sympos. Foundations Comput. Sci. (FOCS), Washington, DC, 234–243. http://portal.acm.org/citation.cfm?id=875492.

Feinberg, F. M., J. Huber. 1996. A theory of cutoff formation under imperfect information. Management Sci. 42(1) 65–84.

Fuhr, N. 1999. A decision-theoretic approach to database selection in networked IR. ACM Trans. Inform. Systems 17(3) 229–249.

Galletta, D. F., R. Henry, S. McCoy, P. Polak. 2006. When the wait isn’t so bad: The interacting effects of Web site speed, familiarity, and breadth. Inform. Systems Res. 17(1) 20–37.

Gonul, F., K. Srinivasan. 1993. Modeling multiple sources of heterogeneity in multinomial logit models: Methodological and managerial issues. Marketing Sci. 12 213–229.

Gravano, L., H. Garcia-Molina. 1995. Generalizing gloss to vectorspace databases and broker hierarchies. Proc. 21st Internat. Conf. Very Large Databases (VLDB), Zurich.

Gray, W. D., B. E. John, M. E. Atwood. 1993. Project Ernestine: Validating a GOMS analysis for predicting and explaining real-world task performance. Human-Comput. Interaction 8(3) 237–309.

Green, P. E., A. M. Krieger, Y. Wind. 2001. Thirty years of conjoint analysis: Reflections and prospects. Interfaces 31(3) S56–S73.

Johnson, E. J., J. W. Payne. 1985. Effort and accuracy in choice. Management Sci. 31(4) 395–414.

Hosanagar, K. 2005. A utility theoretic approach to determining optimal wait times in distributed information retrieval. Proc. ACM SIGIR Conf., Salvador, Brazil.

Hui, M., D. K. Tse. 1996. What to tell consumers in waits of different lengths: An integrative model of service evaluation. J. Marketing 60 81–90.

Jasperson, J., P. Carter, R. W. Zmud. 2005. A comprehensive conceptualization of the post-adoptive behaviors associated with IT-enabled work systems. MIS Quart. 29(3) 525–557.

Johnson, E. J., J. W. Payne. 1985. Effort and accuracy in choice. Management Sci. 31 394–414.

Kamakura, W. A., G. J. Russell. 1989. A probabilistic choice model for market segmentation and elasticity structure. J. Marketing Res. 26 379–390.

Kieras, D. 1997. A guide to GOMS model usability evaluation using NGOMSL. M. Helander, T. Landauer, P. Prabhu, eds. Handbook of Human-Computer Interaction. Elsevier Science, Amsterdam, 733–766.

Kirsch, S. T. 1995. Document retrieval over networks wherein ranking and relevance scores are computed at the client for multiple database documents. U.S. Patent 5,659,732, filed May 17, 1995, issued August 19, 1997.

Krishnan, R., X. Li, D. Steier, L. Zhao. 2001. On heterogeneous database retrieval: A cognitively guided approach. Inform. Systems Res. 12(3) 286–301.

Larcker, D., V. Lessig. 1980. Perceived usefulness of information: A psychometric examination. Decision Sci. 11(1) 121–134.

Le Calve, A., J. Savoy. 2000. Database merging strategy based on logistic regression. Inform. Processing Management 36(3) 341–359.

Mendelson, H., S. Whang. 1990. Optimal incentive-compatible priority pricing for the M/M/1 queue. Oper. Res. 38 870–883.

Moenart, R., W. Souder. 1996. Context and antecedents of information utility at the R&D/marketing interface. Management Sci. 42(11) 1592–1610.

Montgomery, A., K. Hosanagar, R. Krishnan, K. Clay. 2004. Designing a better shopbot. Management Sci. 50(2) 189–206.

Rossi, P., R. E. McCulloch, G. M. Allenby. 1996. The value of purchase history data in target marketing. Marketing Sci. 15(4) 321–340.

Shugan, S. 1980. The cost of thinking. J. Consumer Res. 7(September) 99–111.

Si, L., J. Callan. 2002. Using sampled data and regression to merge search engine results. Proc. ACM SIGIR Conf., Tampere, Finland.

Si, L., J. Callan. 2003. Relevant document distribution estimation method for resource selection. Proc. ACM SIGIR 2003. ACM, New York. http://portal.acm.org/citation.cfm?id=860490.

Si, L., J. Callan. 2004. Unified utility maximization framework for resource selection. Proc. 13th Internat. Conf. Inform. Knowledge Management, Washington, DC.

Stigler, G. J. 1961. Economics of information. J. Political Econom. 69(June) 213–225.

Svenson, O. 1979. Process descriptions of decision making: The effect of information display. Acta Psych. 23(65) 165–179.

Teevan, J., S. T. Dumais, E. Horvitz. 2005. Personalizing search via automated analysis of interests and activities. Proc. ACM SIGIR Conf., ACM, New York.

Topkis, D. 1998. Supermodularity and Complementarity. Princeton University Press, Princeton, NJ.

Varki, S., P. Chintagunta. 2004. The augmented latent class model: Incorporating additional heterogeneity in the latent class model for panel data. J. Marketing Res. 41 226–233.

Voorhees, E., N. K. Gupta, B. Johnson-Laird. 1995. Learning collection fusion strategies. Proc. 18th Annual Internat. ACM SIGIR Conf., Seattle. http://portal.acm.org/citation.cfm ?id=215357.

Xiao, B., I. Benbasat. 2007. E-commerce product recommendation agents: Use, characteristics, and impact. MIS Quart. 31(1) 137–209.

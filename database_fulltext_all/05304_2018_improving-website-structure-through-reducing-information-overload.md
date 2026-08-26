---
otero_id: 5304
otero_key: "DGRGJBPK"
title: "Improving website structure through reducing information overload"
authors: "Min Chen"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.03.009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
<table><tr><td>PII:</td><td>S0167-9236(18)30057-5</td></tr><tr><td>DOI:</td><td>doi:10.1016/j.dss.2018.03.009</td></tr><tr><td>Reference:</td><td>DECSUP 12944</td></tr><tr><td>To appear in:</td><td>Decision Support Systems</td></tr><tr><td>Received date:</td><td>1 November 2017</td></tr><tr><td>Revised date:</td><td>12 February 2018</td></tr><tr><td>Accepted date:</td><td>27 March 2018</td></tr></table>

## Accepted Manuscript

Improving website structure through reducing information overload

Min Chen

![](/api/attachments/DGRGJBPK/fulltext/images/3414a7881dbd5ccc71db5b8cb9fffb4f0604b11e525e670ee207756e13beb0b5.jpg)

Please cite this article as: Min Chen , Improving website structure through reducing information overload. The address for the corresponding author was captured as affiliation for all authors. Please check if appropriate. Decsup(2017), doi:10.1016/j.dss.2018.03.009

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Improving Website Structure through Reducing Information Overload

Min Chen School of Business, George Mason University 4400 University Drive, MS5F4, Fairfax, VA 22030, mchen15@gmu.edu

## Abstract

It is well known that website success relies heavily on its usability. Previous studies find that website usability depends greatly upon its visual complexity which has significant effects on users’ psychological perception and cognitive load. In this study, we use a page’s outdegree (the number of links in a page) as one measurement for its visual complexity. In general, outdegrees should be kept not too high in page design as large outdegrees are often signs of high page complexity which can adversely affect user navigation. This is particularly desirably and critical for maintaining website structures, because as a website evolves over time, the need for information also changes. Website structures must be updated periodically to align with users’ information needs. In this process, obsolete links should be removed to avoid clustering of links that could cause information overload to users. However, the need to slim down website structures and reduce page complexity is understudied in the literature. In this paper, we propose a mathematical programming (MP) model that reduces information load by removing links from highly clustered pages while minimizing the impact to users. Results from extensive tests on a real dataset indicate that the model not only significantly reduces page complexity with little impact on user navigation, but also can be solved effectively. The model is also tested on large synthetic datasets to demonstrate its remarkable scalability.

Index Terms— website navigability, visual complexity, information overload, mathematical programming.

## 1 INTRODUCTION

With the rapid advancements in the Internet technologies, websites have become an unparalleled platform for people to explore information and acquire knowledge. It is well known that website success is highly dependent on its usability [1], [2], [3]. Poor usability is a key element in many high-profile site failures [4] and can turn away users even if its information is of high quality [5]. Previous studies find that website usability depends greatly upon its visual complexity [6], [7], [8], which has a significant effect on users’ psychological perception and cognitive load [9], [10].

Visual complexity has multifaceted dimensions and can be measured by elements such as the amount of text, the number of links and graphics, etc. [11]. In this study, we use a page’s outdegree (i.e., the number of links in a page) as a proximity for the visual complexity of page content. Outdegree is a widely used metric in a number of prior studies and large outdegrees are signs of high page complexity that can adversely affect user navigation [9], [10], [11], [12]. Therefore, outdegrees sho d be kept not too high in page design to help users quickly locate relevant links. This is particularly desirable and critical for maintaining website structure because as websites evolve over time, the need for information also changes. Website structures ers’ information needs. Thus, it is important to consider hyperlinks as a design element during website maintenance.

There is an abundant literature on improving website navigability, and the methods can be classified into two categories in general: (1) restitution of a completely new web structure [13], [14], [15], [16], [17], (2) introducing extra links to the current structure [18]. Nevertheless, such methods either cause substantial disorientation to existing users because of the radical changes to the site structure or complicate the existing structure because of the insertion of many new links, causing information overload to users and difficulty in locating appropriate links during navigation. Thus, it is important to consider “slimming down” website structures to enhance users’ browsing efficiency.

# ACCEPTED MANUSCRIPT

In this paper, we propose a mathematical programming (MP) model that reduces users’ cognitive load by removing links from highly clustered pages while minimizing the impact to user navigation. Consistent with prior studies that model outdegree as a constraint [13], [14], [16], [17], [18], our MP model also requires a page’s outdegree to be constrained by an upper bound. As such, excessive links from pages violating the outdegree constraint must be removed to reduce visual complexity. Though link removal helps reduce navigate. Intuitively, the effects on user navigation are not the same across all links. In particular, some links are ill-designed or improperly placed, so they are not essential to user navigation and removing them would not affect users much. But for the popular links that are frequently traversed, removing them would affect users greatly. As such, though many links can be selected for removal, they must be selected in a way such that the impact to user navigation is not substantial. In this paper, we measure the impact to user navigation by the number of user sessions that would be affected from the link removal. Therefore, our model is formulated such that the links selected for removal would affect as few user sessions as possible. This helps down” the website structure while introducing the least changes to user navigation.

Since our model focuses on easing user navigation by modifying the existing structure of a website, it is particularly appropriate for persistent informational websites which have a predefined site structure and static and stable contents over time. Examples of organizations that use informational websites include universities, tourist attractions, hospitals, federal agencies, and sports organizations [19], [20]. On the other hand, websites that use predominantly dynamic pages or have volatile contents may not be suitable for our method. This is because there is no predefined site structure to be improved and a steady state might never be reached in user traversal patterns in such websites, so it may not be possible to use the log data to improve the site structure [16]. See section 5.3 for a detailed discussion on this issue.

# ACCEPTED MANUSCRIPT

Though we also consider outdegree as a constraint, we model it in a way that is notably different from previous studies: the outdegree constraint can be specified to be “slack” in the sense that not all pages have to be subject to it, that is, some pages can be excluded from consideration if reducing their complexity entails a very high cost, i.e., affecting a larger number of users. As will be shown later in the experiments, such “flexibility” enables our model to strategically select the most appropriate pages to improve, which is key to keeping the number of affected sessions at a very low level.

We perform extensive experiments on a dataset collected from a real website. The results show that our model not only can slim down website structures with little impact to user navigation, it also produces optimal solutions effectively, suggesting that our model is practical to real world websites. We then compare it with two heuristics and find that our model greatly outperforms the heuristics in all parameter values tested. Interestingly, the margin is much higher when allowing for a little flexibility in the outdegree constraint. This show that our MP model is able to take full advantage as compared to the heuristic-based approaches. We also test our model with very large synthetic datasets and the solution times are remarkably low, ranging from just over one second to 32.67 seconds. Moreover, the solution times increase modestly as the size of the dataset increases, indicating the remarkable scalability of the proposed MP model.

In summary, this research makes the following contributions. First, we explore the problem of mitigating information overload with only minimal impact to users, an important question that is understudied in the literature. Second, we show that our MP model not only greatly outperforms heuristicbased approaches but also generates optimal solutions very fast. The experiments on large synthetic data indicate that it also scales up very well. Third, our model allows for exclusion of some “high-impact” pages from consideration and can tactically select the most appropriate pages to improve, thereby taking full benefits from this flexibility.

The rest of the paper is organized as follows. Section 2 reviews related studies. Section 3 defines the problem and presents the model formulation with illustrative examples. Section 4 describes the datasets, reports and evaluates the results from extensive experiments. Section 5 discusses issues related to this research and section 6 concludes the paper.

## 2 RELATED WORK

Our research is closely related to the literature that examines how to improve website navigability using user navigation data. The prior studies primarily focus on methods to enhance user navigation by reconstructing a new website structure based user traversal paths, and they are known as reorganization approaches for this reason.

Fu et al. [13] describe an approach to completely reorganize web pages with the objective of providing users with their desired information in fewer clicks. This approach considers only local structures rather than the entire website, so the new structure may not be necessarily optimal for all users. Gupta et al. [16] annealing to re-link web pages to improve navigability. It aims to re-create a link structure that has the best feasible click ratio, which is defined as the session click ratio averaged over all sessions. However, this heuristic-based approach does not yield optimal solutions and takes a long time to run even for a small website. Lin [14] develops integer programming models to reorganize a website based on the cohesion between pages to reduce information overload and search depth for users. In addition, a two-stage heuristic is developed to reduce the computation time. Despite the effort to improve its efficiency, this heuristic still requires very long computation times to solve, especially for the website containing many links. Besides, the models were tested only on randomly generated websites, which were generated with overly simple structures that have little resemblance to real websites. Therefore, its applicability on real world websites remains doubtful.

Lin and Tseng [15] propose an ant colony system to reorganize website structures. Although their approach resolves the efficiency problem in [14] and can provide solutions in a relatively short computation time, the sizes of the synthetic websites and real website tested in [15] are still relatively small, posing questions on its scalability to large-sized websites. A recent study by Yin and Guo [17] develops an enhanced tabu search to tackle the website structure optimization problem. However, this metaheuristic approach can tests on a simple website (143 pages).

The main drawback of reorganization approaches is the radical changes to the current website structure, which can cause substantial user disorientation because of the radical changes to website structures as the result of a complete reorganization. Compounded by the lack of a usability study on the new structure, reorganization approaches are often criticized for their applicability on real world websites. And for this obvious reason, it is not suitable for updating and maintaining of website structure on a progressive basis.

Recognizing the drawbacks, Chen and Ryu [18] examine how to improve user navigation without changing the current structure substantially. The proposed model can enhance user navigation considerably by adding a relatively small number of new links and editing some of the existing links. However, the model does not impose a hard constraint on page outdegree. As such, each time when the method is applied, new links that are introduced may be added to pages that are already highly complicated. This can lead to clusters of links which bring in difficulty to read and comprehend the page contents. Since page outdegrees may also grow rapidly as a result, this method may exacerbate visual complexity issues when applied repeatedly over time.

There have been several studies emerged in the recent years. Paranjape et al. [21] develop an automatic approach that is language- and website-dependent for suggesting missing but potentially highly used hyperlinks for a website. West et al. [22] propose a method that harnesses human navigation traces and finds missing links to enhance

Wikipedia’s navigability. Scaria et al. [23] build statistical models to predict whether a user will complete or abandon a navigation process. Dimitrov et al. [24] investigate link features and their effects on link popularity to provide insight into what makes a link successful on Wikipedia. Kumar and Jenamani [25] propose a deviation minimization framework and use modified simulated annealing and ant colony optimization algorithms to achieve a tradeoff between the designer-defined context and the user-defined context. Xuan et al. [26] develop three methods for formally defining and mining a websites interests based on a hierarchical structure.

## 3 PROBLEM FORMULATION

## 3.1 Problem Description

To analyze users’ traversal patterns on a website, the web log files need to be demarcated into user sessions, where a session is a group of activities performed by a user during his/her visit to a website [27]. Previous work uses timeout methods to demarcate sessions from log files, we follow this and use the pagestay timeout heuristic described in [28], [29] to identify sessions. Specifically, we identify target pages by assessing if the time spent on it is greater than a timeout threshold. The intuition is that a user generally spends more time reading on the documents relevant to their targets [30].

We illustrate in Fig. 1 a hypothetical website that has 8 pages. Let $S _ { 1 } = \{ ( 1 , 2 ) , ( 2 , 5 ) , ( 5 , 8 ) \} , S _ { 2 } =$ , and $S _ { 3 } = \{ ( 1 , 4 ) , ( 4 , 5 ) , ( 5 , 8 ) \}$ be three user sessions identified from the log file.

![](/api/attachments/DGRGJBPK/fulltext/images/90b67a2fdb9ec4e978c8dc9c1ba105861cf56df6a95cbf3e35f894d682998cd5.jpg)  
Fig. 1. A website with eight pages

Note that for easy exposition, we describe a session by using an ordered set of links traversed in it instead of a sequence of visited pages. For example, a user in $S _ { 1 }$ starts from page 1, and then visits pages 2, 5, and 8 in sequence. Our model allows webmasters to specify an outdegree threshold for each page, which is the maximum number of links allowed for that page. Now suppose a simplified example where the outdegree threshold is set to 2 for all pages. It is immediate from Fig. 1 that we just have to remove links from pages 1, 4 and 5 as only they have more than 2 links.

There are various choices to remove links which could lead to different impact on users. Take page 1 for example, we can delete link and this has no effect on any of the three sessions. Or we can delete link instead in which case $S _ { 3 }$ is affected. Though it is possible that the user can reach the target via other routes, s/he would incur additional time and effort to do so, because according to information foraging theory, the user can no longer follow the path that appears most likely to lead to the target [31], [32]. Finally, if link is deleted then both $S _ { 1 }$ and $S _ { 2 }$ would be affected.

Though making the link removal decision for one page seems easy, the complexity of the decision problem will increase substantially as the sizes of pages and sessions increase. Thus, this calls for a formal analysis on how to delete appropriate links to mitigate information overload while minimizing the impact to user navigation.

## 3.2 The Model

We model a website as a directed graph with pages represented as nodes and links as arcs. As such, our problem can be regarded as a special graph optimization problem. Let be the set of all pages/nodes and $\lambda _ { i j } ,$ , where $i , j \in N .$ , denotes the linkage information, with $\lambda _ { i j } = 1$ indicating a link from to , denoted by , exists, and $\lambda _ { i j } = 0$ otherwise. The outdegree of is $\begin{array} { r } { w _ { i } = \sum _ { j \in N } \lambda _ { i j } } \end{array}$

It is worth noting that not all links are subject to consideration for removal because of the nature of website design. First, some pages can be more popular and frequently accessed by users, thus links to them

# ACCEPTED MANUSCRIPT

must be placed in other pages to allow for fast user access. Examples include homepages, search pages, contact pages, etc. A common design practice is to group them as a “module” (e.g., for navigational purposes) in a design template. As such, they usually have a very high indegree (defined as the total number of incoming links) and are hence called “top-indegree” nodes, denoted by $N ^ { T }$ . Since such links are a part of the design template that will exist in virtually every page, they are excluded from consideration for removal. As $E = \left\{ ( i , j ) \colon \lambda _ { i j } = \right.$ 1, $\forall i \in N , j \in N \backslash N ^ { T } \}$ . Second, our improvements are meant to be applied on pages experiencing information overload, and as in the prior work [16], [17], [18], they are commonly identified by an outdegree threshold, denoted by $d _ { i } .$ . It is the number of links for a page, above which the page complexity is considered high enough to cause information overload to users. Intuitively, only the nodes exceeding the outdegree threshold are relevant to our decision. Such nodes are termed “relevant nodes” and are denoted by $N ^ { R } =$ $\{ i \in N \colon w _ { i } > d _ { i } \}$ . The other nodes have fewer links and do not suffer fro information overload problems, so they are irrelevant to our decision. Let $N ^ { I } = N \backslash N ^ { R }$ be the set of irrelevant nodes.

Just like not every node is relevant to our decision, not every link can be removed to reduce page complexity. Following the discussion above, for a link to be a candidate for removal, its destination node ( ) must not be a top-indegree node and its originating node ( ) must be a relevant node (i.e., outdegree is larger than $d _ { i } )$ . Formally, we define $E ^ { C } = \{ ( i , j ) \in E \colon i \in N ^ { R }$ and $j \in N \backslash N ^ { T } \}$ as the set of candidate links that can be deleted to reduce page complexity on relevant nodes. Intuitively, the higher the outdegree, the more links must be deleted to meet the goal. Formally, for a relevant node $i \in N ^ { R } .$ , it is said to be improved if at least $( w _ { i } - d _ { i } )$ links are deleted from it. In practice, $d _ { i }$ is context-dependent and can vary across web pages. While this is a function of the website in general, it is worth noting that setting $d _ { i }$ to be too small would significantly affect user navigation, thereby bringing into question the potential advantages of reducing information overload in the first place.

# ACCEPTED MANUSCRIPT

Demarcating log files generates the set T of all user sessions containing traversal paths (ordered sequences of nodes/pages) that are enabled by web links. For a session $S \in T$ and we define as an ordered set of web links traversed in and , for $1 \leq k \leq | L ( S ) |$ as the th link visited in . We then define parameters $a _ { i j k } ^ { S }$ to be 1 if $( k , S ) = ( i , j )$ , and 0 otherwise. In other words, $a _ { i j k } ^ { S } = 1$ if and only if link $( i , j )$ is the th visited link in . Further, we define variable $\boldsymbol { c } _ { k } ^ { S }$ which will be set to one if the solution indicates deleting the th link in $S ,$ and 0 otherwise. As to be explained later, the use of $a _ { i j k } ^ { S }$ is to build connections between variables $x _ { i j }$ and $c _ { k } ^ { S } ,$ , where the first uses global indices and the latter is defined using local indices. While log files in general contain a large number of user sessions, not all links are necessarily traversed by users. We define $E ^ { T } = \{ ( i , j ) \in E \colon \exists S \in T$ such that $( i , j ) \in L ( S ) \}$ as the set of traversed links, and $E ^ { N } = E \backslash E ^ { T }$ as the set of nontraversed links. We further define $\sigma _ { i j } = 1 \mathrm { i f } ( i , j ) \in E ^ { T }$ and $0 \mathrm { i f } ( i , j ) \in E ^ { N }$

# ACCEPTED MANUSCRIPT

While removing candidate links from $E ^ { C }$ can reduce page outdegree and make it easier to read and comprehend the content, this would inevitably affect user navigation as users can no longer traverse these links to reach their targets after removal. For a session $S \in T ,$ it is said to be affected if at least one link traversed in is selected for removal. Our problem is to determine whether to delete a link $( i , j ) \in E$ . Let $x _ { i j } \in \{ 0 , 1 \}$ denote the decision variable such that $x _ { i j } = 1$ indicates deleting the link and $x _ { i j } = 0$ otherwise. $x _ { i j }$

Table 1. Summary of Notations

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td>S</td><td>A session that contains an ordered set of pages traversed by a user.</td></tr><tr><td>T</td><td>The set of all identified sessions.</td></tr><tr><td>L(S)</td><td>An ordered set containing the web links traversed in S.</td></tr><tr><td>N</td><td>The set of all nodes/pages.</td></tr><tr><td>wi</td><td>The current outdegree of page i.</td></tr><tr><td>di</td><td>The outdegree threshold for page i.</td></tr><tr><td>NR</td><td>The set of relevant nodes, i.e., nodes with an outdegree (wi) larger than the threshold (di).</td></tr><tr><td>δ</td><td>Node improvement threshold, i.e., the number of relevant nodes that must be improved.</td></tr><tr><td>λij</td><td>1 if page i has a link to page j in the current structure; 0 otherwise.</td></tr><tr><td>σij</td><td>1 if link (i,j) has been traversed in user sessions; 0 otherwise.</td></tr><tr><td>E</td><td>The set of links that are considered for removal.</td></tr><tr><td>EC</td><td>The set of candidate links, i.e., links that reduce outdegree on relevant nodes when removed.</td></tr><tr><td>aSijk</td><td>1 if (i,j) is the kth link traversed in session S; 0 otherwise.</td></tr><tr><td>xij</td><td>1 if the link (i,j) is selected for removal; 0 otherwise.</td></tr><tr><td>cSk</td><td>1 if the kth link in session S is selected for removal; 0 otherwise.</td></tr><tr><td>r(S)</td><td>1 if a session S is affected by link removal; 0 otherwise.</td></tr></table>

# ACCEPTED MANUSCRIPT

given threshold. Let $r ( S ) \in \{ 0 , 1 \}$ denote the variable such that $r ( S ) = 1$ indicates is affected, and $n _ { i } \in \{ 0 , 1 \}$ denote the variable such that $n _ { i } = 1$ indicates node is improved. Table 1 provides a summary of the notations used in this paper.

The problem of mitigating information overload on a website while minimizing the impact to user navigation is formulated as the mathematical programming model below:

$$
\text { Minimize } \sum_ {S \in T} r (S) - \sum_ {(i, j) \in E} x _ {i j} \left(1 - \sigma_ {i j}\right) \varepsilon
$$

subject to

$$
c _ {k} ^ {S} = \sum_ {(i, j) \in E ^ {C}} a _ {i j k} ^ {S} x _ {i j}; k = 1, 2, \dots , | L (S) |, \forall S \in T\tag{1}
$$

$$
\sum_ {k = 1} ^ {| L (S) |} c _ {k} ^ {S} - M r (S) \leq 0; \forall S \in T\tag{2}
$$

$$
\sum_ {j: (i, j) \in E ^ {C}} x _ {i j} + M (1 - n _ {i}) \geq (w _ {i} - d _ {i}), \forall i \in N ^ {R}\tag{3}
$$

$$
\sum_ {i \in N ^ {R}} n _ {i} \geq \delta\tag{4}
$$

$$
x _ {i j}, r (S), n _ {i} \in \{0, 1 \}.\tag{5}
$$

The objective function consists of two components. The first term is the number of sessions that are affected by removal of links. Noting that not all links are necessarily traversed in user sessions and that deleting a nontraversed link would has no effect on users. Therefore, we introduce the second term $\begin{array} { r } { \sum _ { ( i , j ) \in E } x _ { i j } \big ( 1 - \sigma _ { i j } \big ) \varepsilon } \end{array}$ , where is a very small number, in the objective function to let the model select all eligible nontraversed links. Without this term, some nontraversed links may not be selected for removal because whether to remove them would then have no effect on the objective function. To see this, let $E ^ { N C } = E ^ { N } \backslash E ^ { C }$ be the set of nontraversed links that are not in the set of candidate links for removal. When the second term is not present, removing all links $( i , j ) \in E ^ { N C }$ is the same as removing none of them, because

doing so neither helps reduce outdegree (since they are not candidate links) nor affects user navigation (since they are not traversed by users). This could lead to a number of optima. As such, we impose a very small cost on not removing a link from $E ^ { N C }$ in the objective function so that the model will select all nontraversed links for removal regardless of whether they are from relevant nodes.

Constraint (1) defines variable $c _ { k } ^ { S } ,$ , which is set to 1 if the th link in is removed, i.e., $a _ { i j k } ^ { S } = x _ { i j } = 1$ , for some $( i , j ) \in E ^ { C }$ , and 0 otherwise. It uses $a _ { i j k } ^ { S }$ to build connections between variables $x _ { i j }$ and $c _ { k } ^ { S } ,$ , because the objective function contains $x _ { i j }$ which uses global indices ( and ) to label pages, whereas the constraint (2) is defined by variable $c _ { k } ^ { S }$ which uses different indices ( and ) to identify a link’s position in a session.

Constraint (2) captures whether a session $S \in T$ is affected by link removal. Specifically, the first term is the number of links selected for removal in . In the second term, is a very large number and is an indicator variable that is set to 1 if at least a link in will be removed and 0 otherwise.

Constraint (3) identifies for each relevant node $N ^ { R }$ , whether the reduction of its outdegree meets the target, which is defined as deleting at least $( w _ { i } - d _ { i } )$ links from . The use of (a very large number) ensures that variable $n _ { i }$ can be set to 1 if at least $( w _ { i } - d _ { i } )$ links are removed from node and 0 otherwise. It is worth noting here that the logic of the formulation is not affected by the outdegree threshold used, that is, the value $d _ { i }$ $i \in N ^ { R }$ or not. Therefore, for simplicity, we will use a single value denoted by as the threshold in our experiments.

Constraint (4) requires that at least relevant nodes are improved with reduced page complexity, where $\delta \in [ 0 , | N ^ { R } | ]$ is a number set by webmasters. Intuitively, setting $\delta = 0$ implies none is improved and setting $\delta = | N ^ { R } |$ requires all relevant nodes be improved. Note that while setting a larger value for entails more nodes are improved, it also requires more links to be removed, thereby affecting a large number of sessions. Constraint (5) imposes that decision variables are binary.

# ACCEPTED MANUSCRIPT

Note that a special case of the MP model when $\varepsilon = 0 , \delta = | N ^ { R } |$ and $( w _ { i } - d _ { i } ) = 1$ can be viewed as the hitting set problem. That is, when the objective is to improve all relevant nodes by deleting at least one candidate link from them, the formulation reduces to a hitting set problem, which is stated as follows: Given a ground set and a collection of subset , the objective is to find the smallest subset $H \subseteq X$ of elements that “hits” every set of , i.e., $\cap A \neq \emptyset$ for every $A \in F$ . It is equivalent to the set-covering problem which is known to be NP-complete [33]. In our MP model, is the ground set containing all user sessions. For a relevant node $i \in N ^ { R } .$ , the set of sessions that will be affected by removing a candidate link from node is $A = \{ S \in T \colon E ^ { c } \cap L ( S ) \neq \emptyset \}$ . The collection of the sets of such sessions for all relevant nodes in $N ^ { R }$ is denoted by . The objective of our formulation when $\varepsilon = 0 , \delta = | N ^ { R } |$ and $( w _ { i } - d _ { i } ) = 1$ is to find the smallest subset

![](/api/attachments/DGRGJBPK/fulltext/images/25f6dd0a7c24571d2716735ff8af9c0bb768c46fdeb3dd45014a263cc569856d.jpg)

Fig. 2. Web page connectivity information of a hypothetical website with 6 pages $H \subseteq T$ that hits every subset of $F , { \mathrm { i . e . } }$ , $\cap A \neq \emptyset$ for every $A \in F$

## 3.3 Illustrative Examples

In this section, we use examples to illustrate how the choices of different parameter values could affect the problem size, the solution spaces, and the optimal solutions of our model. Consider a hypothetical website of 6 pages whose connectivity information is represented in a matrix as shown in Fig 2. The linkage information is shown in entry values, where 1s indicate that a row node has a link to a column node and 0s indicate otherwise. Therefore, the outdegree of page can be obtained by summing the entry values in row $n _ { i } .$ . For example, page 6 has a link to pages 1, 3, and 4, i.e., $\lambda _ { 6 1 } = \lambda _ { 6 3 } = \lambda _ { 6 4 } = 1$ , and hence its outdegree is $w _ { 6 } = 3$ . Table 2 shows the outdegree of each page. We designate $n _ { 1 }$ as the homepage and a top-indegree node which can be accessed from every page.

Table 2. Outdegree  
Table 3. The set of traversed links

<table><tr><td>Node</td><td>Outdegree</td><td>ID</td><td>Links traversed in each session</td></tr><tr><td> $n_1$ </td><td>5</td><td> $S_1$ </td><td>{(1, 4), (4, 2), (2, 1), (1, 5), (5, 2)}</td></tr><tr><td> $n_2$ </td><td>4</td><td> $S_2$ </td><td>{(4, 3), (3, 5), (5, 1), (1, 2), (2, 4)}</td></tr><tr><td> $n_3$ </td><td>3</td><td> $S_3$ </td><td>{(2, 1), (1, 4), (4, 3), (3, 5)}</td></tr><tr><td> $n_4$ </td><td>4</td><td> $S_4$ </td><td>{(6, 3), (3, 2), (2, 1), (1, 5), (5, 6)}</td></tr><tr><td> $n_5$ </td><td>5</td><td> $S_5$ </td><td>{(4, 1), (1, 5), (5, 6), (6, 4)}</td></tr><tr><td> $n_6$ </td><td>3</td><td> $S_6$ </td><td>{(5, 3), (3, 2), (2, 4), (4, 1)}</td></tr></table>

Table 3 shows a set of six user sessions, each of which represents a path comprising the links clicked $S _ { 1 }$ starts from page 1 and then traverses 5 links. Now consider a case where the webmaster sets the outdegree threshold to and $\delta = | N ^ { R } |$ , which requires that the structure be improved so that no page has more than 4 links. In this case, only two nodes $( \mathrm { i } . \mathrm { e } . , n _ { 1 }$ and $n _ { 5 } )$ are relevant as they have more links than the threshold. Table 4 lists the candidate links for each relevant node. To achieve the targeted outdegree, at least one link has to be removed from each node. Noting that links to $n _ { 1 }$ are not considered because it is the homepage and a top-indegree node.

We set $\varepsilon = 1 . 0 \mathrm { E } - 6$ and $M = 1 . 0 \mathrm { E } 7$ in the example. Solving the math program gives the optimal solution $x _ { 1 6 } = x _ { 2 5 } = x _ { 2 6 } = x _ { 4 5 } = x _ { 5 4 } = 1$ , with other variables being 0, and $\Sigma _ { S \in T } \ r ( S ) = 0$ . Note that no session is affected as a result because none of the removed links is traversed in any user session.

The solution will change accordingly when the outdegree threshold is altered. Table 5 shows the relevant nodes and their respective candidate links if the outdegree threshold decreases to . Noticeably, there are two more relevant nodes $( n _ { 2 }$ and $n _ { 4 } )$ that need improvements. They were not relevant to our decision earlier because their outdegrees did not exceed the threshold at . Neverthless, they become relevant under the new outdegree threshold at . Another important change is for nodes $n _ { 1 }$ and $n _ { 5 } ,$ at requirement, i.e., $( w _ { 1 } - d ) = ( w _ { 5 } - d ) = 2$

Solving the math program yields the optimal solution $x _ { 1 2 } = x _ { 1 6 } = x _ { 2 5 } = x _ { 2 6 } = x _ { 4 5 } = x _ { 5 2 } = x _ { 5 4 } = 1$ , with other variables being 0. Compared to the previous case, two more links, i.e., (1, 2) and (5, 2), are removed and doing so also affects two sessions, i.e., $S _ { 1 }$ and $S _ { 2 } ,$ because of the reduced outdegree threshold (or a higher requirement). Since improving all nodes is often very costly, it is reasonable to set (the node improvements threshold) below $| N ^ { R } |$ . This allows the model to improve a subset of nodes instead of all nodes, which substantially reduces the impact on users, as will be shown in the experiment later. To illustrate, we keep $d = 3$ but lower to $\delta = | N ^ { R } | * 0 . 7 5 = 3 . \mathrm { T h } \epsilon$ optimal solution becomes $x _ { 1 2 } = x _ { 1 6 } = x _ { 2 5 } = x _ { 2 6 } = x _ { 4 5 } = x _ { 5 4 } =$ $S _ { 1 }$ $\delta$ affected sessions but also a larger solution space, as shown in the example and to be evidenced by the

Table 4. Candidate links for $d = 4$

<table><tr><td>Nodes</td><td>Candidate links</td></tr><tr><td> $n_1$ </td><td> $\{(1, 2), (1, 4), (1, 5), (1, 6)\}$ </td></tr><tr><td> $n_5$ </td><td> $\{(5, 2), (5, 3), (5, 4), (5, 6)\}$ </td></tr></table>

Table 5. Candidate links for $d = 3$

<table><tr><td>Nodes</td><td>Candidate links</td></tr><tr><td> $n_1$ </td><td> $\{(1, 2), (1, 4), (1, 5), (1, 6)\}$ </td></tr><tr><td> $n_2$ </td><td> $\{(2, 4), (2, 5), (2, 6)\}$ </td></tr><tr><td> $n_4$ </td><td> $\{(4, 2), (4, 3), (4, 5)\}$ </td></tr><tr><td> $n_5$ </td><td> $\{(5, 2), (5, 3), (5, 4), (5, 6)\}$ </td></tr></table>

## 4 COMPUTATIONAL EXPERIMENTS AND PERFORMANCE EVALUATIONS

## 4.1 Experiments on Real Dataset

We first conduct experiments on a real dataset from the Music Machines website (http://machines.hyperreal.org), which is publicly available and widely used in the literature [13], [16], [18]. It spans a period of four months and has millions of requests. Table 6 shows the number of pages in the website that had outdegrees within a specified range. This website has 816 pages in total, of which 731 have an outdegree of 20 or less, and the majority of the remaining pages have 40 links or less.

Table 6. Outdegree statistics

<table><tr><td>Outdegree</td><td>Number of pages</td></tr><tr><td>&gt;80</td><td>2</td></tr><tr><td>61–80</td><td>2</td></tr><tr><td>41–60</td><td>11</td></tr><tr><td>21–40</td><td>70</td></tr><tr><td>11–20</td><td>580</td></tr><tr><td>0–10</td><td>151</td></tr><tr><td>Total</td><td>816</td></tr></table>

Table 7. Session characteristics

<table><tr><td rowspan="2">Number of links</td><td colspan="2">Number of sessions</td></tr><tr><td>t =2min.</td><td>t =5min.</td></tr><tr><td>2</td><td>13,338</td><td>11,952</td></tr><tr><td>3</td><td>6,478</td><td>6,075</td></tr><tr><td>4</td><td>3,695</td><td>3,516</td></tr><tr><td>5</td><td>2,305</td><td>2,215</td></tr><tr><td>6–10</td><td>4,200</td><td>4,292</td></tr><tr><td>&gt;10</td><td>1,077</td><td>1,180</td></tr><tr><td>Total</td><td>31,093</td><td>29,230</td></tr></table>

Before applying our MP model on the log file data, we first followed the log preprocessing steps described in the prior work ( [13], [18]) to filter irrelevant information from log files. We then used a pagestay timeout heuristic to demarcate sessions. Specifically, we identify target pages by assessing whether the time on it is higher than a predefined timeout threshold and use it to demarcate user sessions. Page-stay time is a common measurement for page relevance to users [30], [34], [35]. In the context of web mining, the pagestay timeout heuristic along with other time-oriented heuristics are widely used for session identification [13], [16], [27], [29], [36], and are shown to be very robust with respect to variations of the threshold values [37]. Two commonly-used time thresholds (2 and 5 minutes) were used in our tests to examine how results changes with respect to different parameter values. Table 7 shows the number of sessions comprising a given number of clicks under each time threshold. Noting that increasing time threshold decreases the number of sessions identified but leads to more links per session.

We set , and vary the outdegree threshold ( ), the node improvement threshold ( ) to examine how results change with respect to these parameters. The math programs were coded in AMPL and solved using CPLEX/AMPL 12.7 on a PC running Windows 10 on an Intel Core i7-6700 processor. Table 8 reports the experiment results. The times for solving optimal solutions range from about one second to less than 15 seconds, indicating that our model is very effective and practical for real world websites. Note that the real website considered in our paper is significantly larger than the average website size [38] and most datasets in the literature, e.g., Gupta et al. [16] and Lin and Tseng [15], etc.

The outdegree threshold determines which pages/nodes need improvements, i.e., are relevant to our decision. To study how the number of relevant nodes would influence the result, we used three outdegree threshold values (15, 20 and 30), as shown in the column “OD THR ( )”. Besides being used in previous studies [18], [13], the threshold values were chosen because they represent three important cases: denotes the average outdegree, represents roughly the 90th percentile, and serves for the case that considers improvements on only the pages suffering very severe information overload problems.

Intuitively, a lower threshold value entails a higher requirement, which translates into more nodes to be improved. As discussed and shown earlier, it can be very costly to improve all nodes up to the outdegree threshold, so we introduced a parameter ( ) which allows the model to strategically select some of the relevant nodes to improve with a much less impact on users. This node improvement threshold is expressed as a percentage of total relevant nodes and is indicated in column “Node imp. THR ( )”. We consider three different values in the experiments, where $\delta = 1 0 0 \%$ is the best-case scenario, $\delta = 9 0 \%$ is a case with little impact to user navigation, and $\delta = 9 5 \%$ is an intermediate case that allows for exclusion of some “outliers”. For example, setting to 100% requires that all relevant nodes be improved while setting it to 90% indicates the model selectively improve at least 90% of all relevant nodes.

Table 8. Results from real world dataset

<table><tr><td>Time THR (t)</td><td>OD THR (d)</td><td>No. of relevant nodes</td><td>Node imp. THR (δ)</td><td>Sessions affected</td><td>Sessions affected (%)</td><td>Total links removed</td><td>Traversed links removed</td><td>Time (sec.)</td></tr><tr><td rowspan="9">2 min.</td><td rowspan="3">30</td><td rowspan="3">35</td><td>100%</td><td>5,827</td><td>18.74%</td><td>2,863</td><td>175</td><td>2.78</td></tr><tr><td>95%</td><td>1,617</td><td>5.20%</td><td>2,801</td><td>113</td><td>2.33</td></tr><tr><td>90%</td><td>282</td><td>0.91%</td><td>2,779</td><td>91</td><td>1.42</td></tr><tr><td rowspan="3">20</td><td rowspan="3">85</td><td>100%</td><td>11,668</td><td>37.53%</td><td>2,965</td><td>277</td><td>6.51</td></tr><tr><td>95%</td><td>1,150</td><td>3.70%</td><td>2,838</td><td>150</td><td>1.81</td></tr><tr><td>90%</td><td>239</td><td>0.77%</td><td>2,723</td><td>35</td><td>1.55</td></tr><tr><td rowspan="3">15</td><td rowspan="3">164</td><td>100%</td><td>16,680</td><td>53.65%</td><td>3,058</td><td>370</td><td>13.58</td></tr><tr><td>95%</td><td>1,822</td><td>5.86%</td><td>2,864</td><td>176</td><td>4.08</td></tr><tr><td>90%</td><td>346</td><td>1.11%</td><td>2,727</td><td>39</td><td>2.03</td></tr><tr><td rowspan="5">5 min.</td><td rowspan="3">30</td><td rowspan="3">35</td><td>100%</td><td>5,356</td><td>18.32%</td><td>2,973</td><td>177</td><td>1.89</td></tr><tr><td>95%</td><td>1,623</td><td>5.55%</td><td>2,811</td><td>115</td><td>1.72</td></tr><tr><td>90%</td><td>279</td><td>0.95%</td><td>2,789</td><td>93</td><td>1.42</td></tr><tr><td rowspan="2">20</td><td rowspan="2">85</td><td>100%</td><td>10,986</td><td>37.58%</td><td>2,974</td><td>278</td><td>7.11</td></tr><tr><td>95%</td><td>1,155</td><td>3.95%</td><td>2,847</td><td>151</td><td>1.55</td></tr></table>

## ACCEPTED MANUSCRIPT

<table><tr><td></td><td></td><td>90%</td><td>245</td><td>0.84%</td><td>2,731</td><td>35</td><td>1.28</td></tr><tr><td>15</td><td>164</td><td>100%</td><td>15,868</td><td>54.29%</td><td>3,065</td><td>369</td><td>14.72</td></tr><tr><td></td><td></td><td>95%</td><td>1,805</td><td>6.18%</td><td>2,872</td><td>176</td><td>4.33</td></tr><tr><td></td><td></td><td>90%</td><td>348</td><td>1.19%</td><td>2,733</td><td>37</td><td>2.03</td></tr></table>

The column “Sessions affected” reports the number of sessions that are affected by the removal of links, where a session is deemed affected if at least one link in that session is removed. For example, if we set time threshold to , outdegree threshold to $d = 2 0 ,$ , then we end up with 85 relevant nodes. And if objective is to improve all of them $( \delta = 1 0 0 \% )$ , then the changes to be made will affect 11,668 sessions, or alternatively, 37.53% of all user sessions. The number reported in column “Total links removed” can be further decomposed into two groups: (1) the links sed by users in at lea ion, and (2) the nontraversed links. Recall that our model removes all aversed links bec not visited by any user and are N hence not influential to user navigati is example, f 2,965 links must be removed, among which 277 are links traversed by some users. I orth noting that among the 2,688 nontraversed links that are removed, not all links will contribute to reducing the outdegree on relevant nodes because many of these links are removed from irrelevant nodes which have no more than links.

The number of affected sessions decreases significantly as the node improvement threshold ( ) decreases. A primary reason is that the model will no longer have to improve all relevant nodes as we relax the requirement to allow some nodes to be excluded from consideration. In our test, when , , and $\delta = 1 0 0 \% ,$ , the model must consider all 85 relevant nodes. The number declines to 81 as decreases to 95%. Even though only 4 nodes become irrelevant, this has a profound impact to user navigation: the number of affected sessions decreases from 11,668 to just 1,150, a reduction of over 90%. Obviously, this enables the model to “strategically” exclude the nodes that require a very high cost to improve from consideration,

which significantly reduces the impact on users. In addition, we also observe reductions in solution times and removed links with a decrease in because of the lower number of nodes that must be improved.

Outdegree threshold can be viewed as a targeted requirement on page complexity and has a great impact on the model result. Specifically, a higher requirement can be specified by imposing a smaller outdegree threshold, which results in more changes to user navigation, as shown in Table 8. For example, when and $\delta = 1 0 0 \%$ , lowering from 20 to 15 almost doubles the number of relevant nodes (85 vs. 164) and leads to a huge jump in affected session (37.53% vs. 53.65%). The solution times also increases because lowering outdegree threshold not only increases the number of relevant nodes but also requires more links to be removed from these nodes, that is, $( w _ { i } - d _ { i } )$ increases too. This will greatly increase the search space and hence requires more time to solve the problem.

It is worth noting that though both the outdegree threshold ( ) and node improvement threshold ( ) contribute to defining relevant nodes, their impacts to user sessions are notably different. For example, when and $d = 2 0$ increasing from 95% to 100% improves only 4 more nodes but would affect 10,518 ( ) more sessions. In contrary, if we instead lower to 15, this not only improves a lot more nodes ( vs. 4) but also affects far fewer sessions (672 vs. 10,518). This happens because the characteristics of nodes and links are not uniform. Some nodes have many more links than others, as shown in Table 6, and similarly, some links are more important (popular) and hence are visited more often than others. Thus, improving these nodes or removing these links would have a more profound impact to user navigation than others. The use of node improvement threshold allows for exclusion of these high-impact nodes and links and such a strategic exclusion has proven to be crucial in keeping the number of affected sessions at a very low level.

Table 8 also indicates that the use of different time thresholds does not seem to change the result materially. In general, more sessions (in terms of percentage) are affected when while keeping other parameters the same, but the differences are negligible. For example, when setting and , 5.86% of user sessions are affected at and this increases to 6.18% at . This happens because the use of a larger

time threshold leads to identification of fewer sessions with an increased average session size (as shown in Table 7), that is, there will be more candidate links per session. This intuitively increases the likelihood that a session is affected by link removal. But this difference is very marginal indicating that time threshold will unlikely influence much of the results.

## 4.2 Some Observation and Insights into Problem Size and Efficiency

It follows from the MP model formulation that there are $( | E | + | T | + | N ^ { R } | )$ binary variables and $( | T | + | N ^ { R } | + 1 )$ constraints. While the sizes of a website and user sessions can be very large in practice, it turns out that the solution times taken to solve the math programs on the real world data are low. This is because the formulation can be reduced to a much smaller one in the context of our problem. We make several observations related to the problem size to explain the fast solution times in our experiments.

## 4.2.1 Relevant Nodes

Recall that a node is relevant to our decision only if it has more links than the outdegree threshold ( ). This leads to many irrelevant nodes (denoted as  ) being eliminated from consideration in our MP model, that is, nodes $i \in N ^ { I }$ are not considered in our formulation. As a result, the number of relevant nodes that will be improved and considered by the MP model is usually not too large. The choice of outdegree threshold can have significant impacts on relevant nodes. Generally, increasing it leads to fewer relevant nodes while decreasing it has the opposite effect. As shown in Table 8, when decreases from 20 to 15, the number of relevant nodes increases from 85 to 164.

## 4.2.2 Relevant Candidate Links

Theoretically, any existing link not involving a top-indegree node can be considered in our decision problem without a preprocessing step, leading to a total number of links (variables). This number can be very large even for a small website. However, as explained earlier, not every link in are eligible for reducing the outdegree of relevant nodes. Specifically, two types of links are excluded from consideration:

# ACCEPTED MANUSCRIPT

(1) outgoing links from irrelevant nodes (whose outdegree is no more than $d ) .$ , i.e., $( i , j ) \colon i \in N ^ { I } \left( 2 \right)$ links having a top-indegree destination node, i.e., $( i , j ) { : } j \in N ^ { T }$ , where $N ^ { I }$ and $N ^ { T }$ are irrelevant node set and topindegree node set, respectively, as defined earlier. By eliminating these links from consideration, the set of candidate links (denoted by $E ^ { C } )$ that may be selected to meet the goal can be significantly smaller. We preprocess the session data to identify candidate links instead of considering all possible links in a website, and this significantly reduces the search space for our model. Further, the number of links for each session was observed to be not very large (a session has less than 4 links on average) and this leads to a relatively small solution space for individual sessions.

It turns out that even many of the candidate links can also be eliminated from consideration because they are not relevant to our decision. Particularly, for a candidate link that has not been traversed by a user, removing it would have no effect on user sessions. In other words, nontraversed candidate links do not affect any sessions and hence are automatically set for removal, i.e., $x _ { i j } = 1$ in the optimal solution $\forall ( i , j ) \in$ $( E ^ { C } \cap E ^ { N } )$ . Thus, the set of candidate links relevant to the decision are those traversed by users, which is termed as relevant candidate links and denoted by $E ^ { R } = \{ ( i , j ) \in E ^ { C } \backslash E ^ { N } \}$ whose cardinality could be relatively small even for a large website. In the real data, about 40% of links are indeed traversed in user sessions, with the remaining being nontraversed links that can be removed without affecting users. While the problem size can be reduced in our model formulation, the remaining formulation continues to have a large number of variables and constraints.

## 4.3 Comparison with Heuristics

While prior studies have proposed methods to improve website navigability, they were developed for a very different purpose rather than designed with the idea of mitigating information overload. For example, even though Lin [14] also uses mathematical programming (MP) models, the objective function is a completely different one. In simple terms, our objective is to minimize the cost (defined as the number of

# ACCEPTED MANUSCRIPT

affected user sessions) incurred to reduce information overload while Lin’s models generate a new website with maximal frequency summations regardless of the changes (cost) to be made. Other related studies are similar and use different metrics in their objective functions or constraints. As such, a direct comparison of our model with prior work is not feasible. To provide some comparisons, we instead consider two heuristics and use them to compare with our model. Both heuristics start by removing nontraversed links as they are not MP model which also removes all nontraversed links. Noting that doing so helps reduce outdegrees on both relevant and irrelevant nodes. While some of the relevant nodes are improved with a reduced outdegree satisfying the threshold, there are plenty of other relevant nodes that need further improvements, which will have to come from removing traversed links.

The two heuristics differ greatly in how to select traversed links to remove. The first heuristic randomly selects a traversed link, and it does so till all required relevant nodes are improved. We call it the “random” heuristic. The second heuristic is more intelligent. It first creates a map of traversed links (as the key) and the number of sessions that involves this link (as the value), which we call as “frequency”. It then sorts the map in the requirement is met. This is named the “least frequency” heuristic. We compare our model with both heuristics and report the results in Table 9.

Table 9. Comparison of our model with two heuristics

<table><tr><td rowspan="2">Time THR (t)</td><td rowspan="2">OD THR (d)</td><td rowspan="2">Node imp. THR (δ)</td><td colspan="2">Optimal</td><td colspan="2">Random heuristic</td><td colspan="2">Least freq. heuristic</td></tr><tr><td>Sessions affected</td><td>Traversed links removed</td><td>Sessions affected</td><td>Traversed links removed</td><td>Sessions affected</td><td>Traversed links removed</td></tr><tr><td>2 min.</td><td>20</td><td>100%</td><td>37.53%</td><td>277</td><td>61.52%</td><td>277</td><td>37.71%</td><td>277</td></tr><tr><td></td><td></td><td>98%</td><td>15.39%</td><td>205</td><td>63.21%</td><td>276</td><td>26.90%</td><td>265</td></tr></table>

## ACCEPTED MANUSCRIPT

<table><tr><td></td><td></td><td>95%</td><td>3.70%</td><td>150</td><td>57.66%</td><td>241</td><td>9.58%</td><td>201</td></tr><tr><td></td><td></td><td>90%</td><td>0.77%</td><td>35</td><td>36.34%</td><td>147</td><td>1.98%</td><td>135</td></tr><tr><td></td><td>15</td><td>100%</td><td>53.65%</td><td>370</td><td>73.84%</td><td>370</td><td>54.29%</td><td>370</td></tr><tr><td></td><td></td><td>98%</td><td>14.26%</td><td>241</td><td>71.55%</td><td>358</td><td>32.13%</td><td>335</td></tr><tr><td></td><td></td><td>95%</td><td>5.86%</td><td>176</td><td>62.90%</td><td>313</td><td>17.42%</td><td>282</td></tr><tr><td></td><td></td><td>90%</td><td>1.11%</td><td>39</td><td>37.16%</td><td>150</td><td>4.04%</td><td>178</td></tr><tr><td>5 min.</td><td>20</td><td>100%</td><td>37.58%</td><td>278</td><td>60.40%</td><td>278</td><td>37.67%</td><td>278</td></tr><tr><td></td><td></td><td>98%</td><td>16.73%</td><td>206</td><td>65.35%</td><td>276</td><td>27.31%</td><td>266</td></tr><tr><td></td><td></td><td>95%</td><td>3.95%</td><td>151</td><td>47.55%</td><td>224</td><td>8.89%</td><td>198</td></tr><tr><td></td><td></td><td>90%</td><td>0.84%</td><td>35</td><td>35.12%</td><td>152</td><td>2.45%</td><td>141</td></tr><tr><td></td><td>15</td><td>100%</td><td>54.29%</td><td>369</td><td>72.10%</td><td>369</td><td>54.75%</td><td>369</td></tr><tr><td></td><td></td><td>98%</td><td>15.22%</td><td>240</td><td>70.81%</td><td>344</td><td>36.77%</td><td>345</td></tr><tr><td></td><td></td><td>95%</td><td>6.18%</td><td>176</td><td>58.60%</td><td>308</td><td>17.51%</td><td>279</td></tr><tr><td></td><td></td><td>90%</td><td>1.19%</td><td>37</td><td>42.56%</td><td>167</td><td>4.80%</td><td>185</td></tr></table>

The comparison shows our method clearly outperforms both heuristics: the affected sessions are lower in our method in all categories, implying that the user navigation is least impacted by our model. This is not entirely surprised as our model solves for optimal solutions whereas the other two are heuristic-based. It is, however, interesting to see that such a dominance is much more prominent as decreases. For example, when , , and , the changes made by our MP model would affect 37.53% of the sessions, and the numbers for the random heuristic and least frequency heuristic are 61.52% and 37.71%, respectively. When lowering to 95%, our MP model would affect only 3.7% of the sessions, whereas the number for the

# ACCEPTED MANUSCRIPT

least frequency heuristic is 9.58%, nearly tripling ours. The random heuristic has the worst performance, requiring changes that would impact 57.66% of the sessions, which is 15 times higher than ours.

The results are also robust across different parameter values. For example, when and , it is clear from Table 9 that our method is also far more superior than the two heuristics at different values. While the difference between our model and the least frequency heuristic is not striking at $\delta = 1 0 0 \%$ , the margin increases significantly when a little flexibility is allowed. We consider a new threshold at $\delta = 9 8 \%$ to provide a sharp contrast. For example, when and , lowering from 100% to 98% allows exclusion of only one page from consideration. Though this seems a very small change, it reduces the number of affected sessions in our model by more than half (16.73% vs. 37.58%). More remarkably, it represents a very large margin in performance compared to the least frequency heuristic (16.73% vs. 27.31%). As explained earlier, this flexibility enables our model to strategically select the most appropriate nodes to improve which proves to be crucial in minimizing the impact on users. Although the heuristics also benefit from a lower , they are unable to take full advantage to maximize this benefit because they lack this “strategic” and optimization capability.

## 4.4 Synthetic Datasets

Besides the real dataset that is fair large compared to related studies [15], [16], we also generated synthetic/artificial datasets that are even much larger to evaluate our model’s scalability. For this reason, the artificial website structures were generated with similar statistical characteristics with the real dataset. Specifically, the real website has an average outdegree of about 14 but the outdegree distribution is highly right skewed (see Table 6). Additionally, the experiments reported in Table 8 show that only about 10% and 20% of the nodes exceed the outdegree threshold at 20 and 15 respectively. For the artificial websites to have a statistical similarity, the outdegree of each node is drawn from a normal distribution with both the mean and standard deviation being 15 and a constraint is imposed to ensure only 10% and 20% of the nodes have more than 20 and 15 links, respectively. Once the limits are reached, if the next outdegree drawn from the normal distribution is larger than the thresholds, it is reassigned with a random value between 1 and 15.

Note that this method differs greatly from those used in prior studies. For example, Lin and Tseng [15] first generate a complete graph of all nodes and assign a random number between 0 and 1 to each directed edge. Then, the edges with the smallest values are selected, resulting in an average outdegree of . The websites generated from this approach have poor resemblance to real websites. First, the outdegree distribution is highly symmetric, not reflecting the reality of the right skewed distribution. Second, the variance in outdegree is usually very small, which fails to capture the fact that certain pages are essential for user navigation and will have many more links than others.

Similar to website structures, user sessions are generated to closely resemble the real data. First, because the average links per session was about 4 in the real data, in the synthetic data the session length is drawn from a normal distribution using 4 as both the mean and stan ard deviation. Second, it is intuitive that no every page is a target or an origin of a user session. rough analysis of session data, we found roughly 20% of the nodes can be considered as targets/origins and they typically have higher outdegrees (about 30% higher) than the average. To preserve this property in synthetic datasets, we first identify the sets of target and origin nodes. Their sizes are limited to 20% of all nodes and they are randomly selected with a preference on those with a higher outdegree, leading to an average outdegree that is about 30% higher than the overall average. Third, we found that the frequency of target and origin nodes are not uniform: certain nodes show up as target or origin nodes much more frequently in user sessions than others. So, we approximate the frequency using a normal distribution so that some nodes have a much higher probability of serving as the target or origin nodes than others. For a user session, once its length is assigned and target and origin nodes are selected, a random path with the respective length is identified starting from the origin to the target using the connectivity information obtained from the generated artificial websites.

Three websites consisting of 1,000, 2,000, and 5,000 web pages were constructed in the experiments. Each of the three artificial websites was tested with 50,000, 100,000, 300,000 and 600,000 sessions and two nodes improvement thresholds (95% and 90%), resulting in 24 different categories. In each category, two datasets were generated and the results were averaged over the two sets. We note that the synthetic datasets generated here are not only considerably larger than those used in related papers such as [15], they also have similar statistical properties to the real website.

Table 10. Experiment on synthetic datasets

<table><tr><td></td><td colspan="4">Website size = 1,000</td><td colspan="4">Website size = 2,000</td><td colspan="4">Website size = 5,000</td></tr><tr><td></td><td colspan="2">δ = 95%</td><td colspan="2">δ = 90%</td><td colspan="2">δ = 95%</td><td colspan="2">δ = 90%</td><td colspan="2">δ = 95%</td><td colspan="2">δ = 90%</td></tr><tr><td>Session Size</td><td>Sessions affected</td><td>Time (Sec.)</td><td>Sessions affected</td><td>Time (Sec.)</td><td>Sessions affected</td><td>Time (Sec.)</td><td>Sessions affected</td><td>Time (Sec.)</td><td>Sessions affected</td><td>Time (Sec.)</td><td>Sessions affected</td><td>Time (Sec.)</td></tr><tr><td>50,000</td><td>3.31%</td><td>1.20</td><td>1.17%</td><td>1.15</td><td>3.40%</td><td>1.27</td><td>1.34%</td><td>1.21</td><td>3.08%</td><td>1.54</td><td>1.24%</td><td>1.60</td></tr><tr><td>100,000</td><td>3.35%</td><td>2.75</td><td>1.36%</td><td>2.41</td><td>3.76%</td><td>2.78</td><td>1.65%</td><td>2.73</td><td>3.12%</td><td>2.93</td><td>1.17%</td><td>2.59</td></tr><tr><td>300,000</td><td>3.71%</td><td>12.12</td><td>1.8%</td><td>9.93</td><td>3.78%</td><td>10.81</td><td>1.42%</td><td>8.43</td><td>3.29%</td><td>11.10</td><td>1.37%</td><td>9.01</td></tr><tr><td>600,000</td><td>2.70%</td><td>25.38</td><td>1.08%</td><td>22.69</td><td>4.61%</td><td>32.67</td><td>2.00%</td><td>25.86</td><td>4.21%</td><td>26.10</td><td>1.85%</td><td>22.68</td></tr></table>

The math programs for the synthetic data were coded and tested in the same setting as the one for the real data. We experimented the model with the outdegree threshold on each synthetic dataset and report the results in Table 10. Noticeably, the times for generating optimal solutions are low for all cases, ranging from 1.15 second to 32.67 seconds. This indicates that the MP model is not only easily scalable to an even larger extent but also very robust to a wide range of problem sizes and parameter values.

# ACCEPTED MANUSCRIPT

Session sizes play a very important role in solution times. For a website of 5,000 pages, when = 90% it takes only 1.6 seconds to solve for optimal solution with 50,000 sessions whereas it takes 22.68 seconds to solve with 600,000 sessions. This is anticipated because an increase in session size leads to an increase in both constraints and variables, which considerably expands the solution space. The node improvement threshold ( ) is also shown to have an impact on solution times. In general, a higher leads to longer solution times, While the solution times increases on datasets of larger sizes, they seem to increase on a reasonable pace.

## 5 DISCUSSIONS

## 5.1 Outdegree Threshold (d)

The outdegree threshold of a page can be loosely viewed as the maximum information overload website [18]. In general, webpages can be classified into two categories based on their usages [16]: (1) index pages (e.g., homepage) whose primary purpose is to facilitate user navigation, and (2) content pages which commonly contain the information users are interested in and search for. While the outdegree for the former can be set high becaus f their pivotal role in user navigation, it should be kept low for the latter to avoid adverse impact on users’ reading and comprehension of relevant information. Since this requires a good understanding of both the organizational structure of the client and users’ navigation preferences, domain knowledge and expertise from web designers or webmasters are generally required in this case.

While this provides a general guideline on identifying proper outdegree threshold values for pages based on their purposes, finding out optimal outdegree thresholds is still nontrivial since they are contextspecific and organization-dependent. Thus, prior studies (e.g., [13], [14], [16], [18]) typically use different threshold values to test how the results are sensitive to the parameter values. Following this practice, in this paper, we used the same outdegree values as in previous studies ( [13], [18]) because they also represent

three important cases: the average webpage outdegree (d=15), the 90th percentile (d=20), and pages with severe information overload problems (d=30).

As shown in the experiments, a lower outdegree threshold imposes a higher requirement on the site structure because it not only increases the number of relevant nodes but also requires more links to be removed from these nodes. Consequently, this results in more changes to user navigation and longer solution times because of the increased search space. In practice, small outdegree thresholds appropriate in the initial stages of website maintenance when the site structure is simple and webpages tend to have less content and few links. As the website evolves and new links and contents are added, the threshold can be increased accordingly. This allows for gradual improvements to the site structure and steady reduction in page complexity without significantly affecting user navigation by considering the heterogeneity in information needs and website characteristics in different phases of its maintenance.

## 5.2 Node Improvement Threshold ( )

The node improvement threshold defines among all relevant pages how many must be improved to result in a higher reduction of information overload, our experiments showed that this is done at a significantly higher cost as the number of impacted user sessions will increase considerably. Sometimes, the additional benefits from using a larger threshold can be too little to justify the increased costs. For example, as shown in Table 8, when and , increasing from 95% to 100% leads to only 4 more pages improved but the user sessions impacted increase by nearly 9 times. This suggests that while it works together with the outdegree threshold to define the required level of information overload reduction, their impacts to user sessions are notably different: the node improvement threshold has a greater impact to results even with a small change. This is because the node improvement threshold allows for exclusion of

some “high-impact” nodes and links, which, when considered in the model, will cause a more profound impact to user navigation than others.

To examine how the results are sensitive to the threshold values, our experiments on the real dataset used three values in which $\delta = 1 0 0 \%$ is the best-case scenario, $\delta = 9 0 \%$ is a case with little impact to user navigation, and $\delta = 9 5 \%$ denotes an intermediate case between the two. In the comparison with heuristics, we also considered a new threshold at $\delta = 9 8 \%$ to provide a sharp contrast and to illustrate how this seemingly small flexibility would have a significant impact on the results.

In practice, webmasters need to cautiously consider the tradeoff between desired reduction in information overload and the potential negative impact on users’ browsing experience when identifying the appropriate node improvement thresholds. A cost benefit analysis that compares the “benefits” and “costs” of using different thresholds can be useful for this purpose. In the context of our problem, we can view the number of impacted user sessions as the cost and the number of improved pages as the benefit. The benefitcost ratio (BCR) that is used for the analysis of the cost effectiveness of different options can be expressed as (number of improved pages weight)/(number of affected sessions), where weight denotes the relative importance of reduced information overload over adverse impact on navigation. As a result, we can approximate the BCRs for different values and find the one that is the most cost-effective and provides a good tradeoff. It is worth noting that our experiments consistently showed that setting a nearly perfect target (e.g., setting $\delta = 1 0 0 \% )$ would introduce radical changes to users (about 40% to 60% affected sessions), thus we recommend against setting at (or very close to) 100% as this may not be a good choice for the purpose of progressive improvements.

## 5.3 Website Type and Information Content

There are two general ways to improve website navigability: modify the site structure to ease the navigation for typical users, often referred to as transformation approaches, or dynamically reconstitute pages

# ACCEPTED MANUSCRIPT

and deliver customized contents to individual users based on information such as their profiles, often referred to as personalization approaches [18]. Our MP model is concerned primarily with transformation approaches and is particularly suitable for improving and maintaining persistent informational websites (also known as “static websites”) which have static contents and a predetermined structure. The websites employing personalization approaches are called “dynamic websites” because they deliver dynamic and databases. Such websites have volatile contents and their users may not have a clear target when browsing. Because there is no predefined structure and a steady state might not be in user traversal patterns in these websites, it may not be possible to use the users log data to enhance their navigation structures. As such, our method may not be appropriate for websites tha der predominantly dynamic pages or have volatile contents. For reviews on personalization approaches, see [39] and [40].

It is important to note that these two types of websites are meant to complement each other, not to replace the other, because they serve for different purposes and have their respective pros and cons. Static websites can provide simple, straightforward information and a unified user experience to a broad audience [41], and are very useful to users who have specific information targets [16]. Dynamic websites are suitable for the interactions with users and applications that require adaptive contents based on users’ behavior [42]. Thus, dynamic websites have gained increased popularity with the boom of E-commerce as they are specially fit for applications such as online social networks, E-commerce, newspaper and magazines. On the other hand, static websites continue to be an essential component and a prevalent choice for organizations such as universities, tourist attractions, hospitals, federal agencies, and sports organizations, etc.

## 6 CONCLUSIONS

We propose a mathematical programming (MP) model that appropriately removes links to reduce users’ cognitive load while minimizing the impact to user navigation. Our model is particularly useful for informational websites whose users have particular information goals [19], [20] and whose contents are relatively stable over time. The tests on a real dataset showed that our model not only can provide significant improvements to website structure without substantial impact to user navigation, it also produces optimal solutions quickly, suggesting that it is very effective to real world websites. The comparison with two heuristic-based approaches showed that our model greatly outperforms the heuristics. We have also tested all datasets tested, demonstrating its remarkable scalability.

The paper can be extended in several directions. First, the identification of sessions can be affected by the choice of page-stay timeout threshold. Even though our model is shown to be very robust across different time thresholds, techniques that can accurately identify users and sessions are very important and future studies may focus on developing such techniques. Second, our model has a constraint for outdegree threshold, which is motivated by cognitive reasons. The model can be further improved by considering additional constraints that can be identified using data mining methods [43]. Third, excessive links or clusters of links are one dimension of information overload and visual complexity, other dimensions such as Further studies can focus on reducing information overload caused by these factors. Last, we used the same outdegree threshold value across all pages in the experiments. Even though the logic of the formulation is not affected by the outdegree threshold values used, we note that they are highly dependent on the purpose of the pages and the website and are context-specific and organization-dependent. Therefore, behavioral and experimental studies that examine the optimal outdegree threshold for different settings can also be interesting future research directions.

## REFERENCES

## ACCEPTED MANUSCRIPT

[1] X. Fang and C. Holsapple, "An Empirical Study of Web Site Navigation Structures’ Impacts on Web Site Usability," Decision Support Systems, vol. 43, no. 2, p. 476–491, 2007.

[2] Y. Lee and K. Kozar, "Understanding of website usability: Specifying and measuring constructs and their relationships," Decision Support Systems, vol. 52, no. 2, pp. 450-463, 2012.

[3] D. F. Galletta, R. Henry, S. McCoy and P. Polak, "When the Wait isn’t So Bad: The Interacting Effects of Website Delay, Familiarity, and Breadth," Information Systems Research, vol. 17, no. 1, p. 20–37, 2006.

[4] J. Palmer, "Web Site Usability, Design, and Performance Metrics," Information Systems Research, vol. 13, no. 2, p. 151–167, 2002.

[5] V. McKinney, K. Yoon and F. Zahedi, "The Measurement of Web-Customer Satisfaction: An Expectation and Disconfirmation Approach," Information Systems Research, vol. 13, no. 3, p. 296–315, 2002.

[6] J. Nielsen, Designing Web Usability: The Practice of Simplicity, Indianapolis, IN: New Riders Publishing, 2000.

[7] Y. Hwang and D. Kim, " Customer self-service systems: the effects of perceived Web quality with service contents on enjoyment, anxiety, and e-trust Source,," Decision Support Systems, vol. 43, no. 3, pp. 746-760, 2007.

[8] V. Venkatesh and R. Agarwal, "From Visitors into Customers: A Usability-Centric Perspective on Purchase Behavior in Electronic Channels," Management Science, vol. 52, no. 3, p. 367–382, 2006.

[9] G. Geissler, G. Zinkhan and R. Watson, "Web home page complexity and communication effectiveness," Journal of the Association for Information, vol. 2, no. 1, pp. 1-47, 2001.

[10] Q. Wang, S. Yang, M. Liu, Z. Cao and Q. Ma, "An eye-tracking study of website complexity from cognitive load perspective," Decision Support Systems, vol. 62, pp. 1-10, 2014.

[11] L. Deng and M. Pool, "Affect in Web Interfaces: A Study of the Impacts of Web Page Visual Complexity and Order," MIS Quarterly, vol. 34, no. 4, pp. 711-730, 2010.

[12] S. Nadkarni and R. Gupta, "A Task-Based Model of Perceived Website Complexity," MIS Quarterly, vol. 31, no. 3, pp. 501-524, 2007.

[13] Y. Fu, M. Shih, M. Creado and C. Ju, "Reorganizing Web Sites Based on User Access Patterns," Intelligent Systems in Accounting, Finance and Management, vol. 11, no. 1, p. 39–53, 2002.

[14] C. Lin, "Optimal Web Site Reorganization Considering Information Overload and Search Depth," European Journal of Operational Research, vol. 173, no. 3, p. 839–848, 2006.

[15] C. Lin and L. Tseng, "Website reorganization using an ant colony system," Expert Systems with Applications, vol. 37, no. 12, pp. 7598-7605, 2010.

[16] R. Gupta, A. Bagchi and S. Sarkar, "Improving Linkage of Web Pages," INFORMS Journal on Computing, vol. 19, no. 1, p. 127–136, 2007.

[17] P. Yin and Y. Guo, "Optimization of multi-criteria website structure based on enhanced tabu search and web usage mining," Applied Mathematics and Computation, vol. 219, no. 24, pp. 11082-11095, 2013.

[18] M. Chen and Y. Ryu, "Facilitating Effective User Navigation through Website Structure Improvement," IEEE Transactions on Knowledge and Data Engineering, vol. 25, no. 3, pp. 571-588, 2013.

[19] J. Morrison, P. Pirolli and S. Card, "A taxonomic analysis of what world wide web activities significantly impact people’s decisions and actions," in Proceedings of the ACM Conference on Human Factors in Computing Systems, Seattle, WA, 2001.

[20] S. Cebi, "Determining importance degrees of website design parameters based on interactions and types of websites," Decision Support Systems, vol. 54, no. 2, pp. 1030-1043, 2013.

[21] A. Paranjape, R. West, L. Zia and J. Leskovec, "Improving Website Hyperlink Structure Using Server Logs," in Proceedings of the Ninth ACM International Conference on Web Search and Data Mining, 2016.

[22] R. West, A. Paranjape and J. Leskovec, "Mining Missing Hyperlinks from Human Navigation Wide Web, Florence, Italy, 2015.

[23] A. Scaria, R. Philip, R. West and J. Leskovec, "The last click: why users give up information network navigation," in Proceedings of the 7th ACM international conference on Web search and data mining, New York, USA, 2014.

[24] D. Dimitrov, P. Singer, F. Lemmerich and M. Strohmaier, "What makes a link successful on wikipedia?," in Proceedings of the 26th International Conference on World Wide Web, 2017.

[25] V. Kumar and M. Jenamani, "Context preserving navigation redesign under Markovian assumption for responsive websites," Electronic Commerce Research and Applications, vol. 21, pp. 65-78, 2017.

[26] J. Xuan, X. Luo, J. Lu and G. Zhang, "Explicitly and implicitly exploiting the hierarchical structure for mining website interests on news events," Information Sciences, vol. 420, pp. 263- 277, 2017.

[27] R. Cooley, B. Mobasher and J. Srivastava, "Data Preparation for Mining World Wide Web

## ACCEPTED MANUSCRIPT

Browsing Patterns," Knowledge and Information Systems, vol. 1, p. 1–27, 1999.

[28] R. Srikant and Y. Yang, "Mining Web Logs to Improve Web Site Organization," in Proceedings of the 10th International Conference on World Wide Web, Hong Kong, 2001.

[29] M. Spiliopoulou, B. Mobasher, B. Berendt and M. Nakagawa, "A Framework for the Evaluation of Session Reconstruction Heuristics in Web-Usage Analysis," INFORMS Journal on Computing, vol. 15, no. 2, pp. 171-190, 2003.

[30] M. Morita and Y. Shinoda, "Information filtering based on user behavior analysis and best match text retrieval," in Proceedings of the 17th Annual International ACMSIGIR Conference on Research and Development in Information Retrieval, Ireland, 1994.

[31] P. Pirolli and S. K. Card, "Information Foraging," Psychological Review, vol. 106, no. 4, p. 643– 675, 1999.

[32] C. Olston and E. Chi, "ScentTrails: Integrating Browsing and Searching on the Web," ACM Transaction on Computer-Human Interaction, vol. 10, no. 3, pp. 177-197, 2003.

[33] M. Garey and D. Johnson, Computers and Intractability: A Guide to the Theory of NP-Completeness, San Francisco, CA: W. H. Freeman, 1979.

[34] D. Oard and J. Kim, "Modeling information content using observable behavior," in Proceedings of the ASIST Annual Meeting, 2001.

[35] M. Claypool, P. Le, M. Waseda and D. Brown, "Implicit interest indicators," in Proceedings of the 6th International Conference on Intelligent User Interfaces, 2001.

[36] H. Liu and V. Keselj, "Combined mining of web server logs and web contents for classifying user navigation patterns and predicting users’ future requests," Data and Knowledge Engineering, vol. 61, no. 2, p. 304–330, 2007.

[37] B. Berendt, B. Mobasher, M. Spiliopoulou and J. Wiltshire, "Measuring the accuracy of sessionizers for web usage analysis," in Proceedings of the Web Mining Workshop at the 1st SIAM International Conference on Data Mining, Chicago, 2001.

[38] Boutell, "WWW FAQs: How many websites are there?," Feburary 2007. [Online]. Available: http://www.boutell.com/newfaq/misc/sizeofweb.html.

[39] S. Jagan and S. Rajagopalan, "A Survey on Web Personalization of Web Usage Mining," International Research Journal of Engineering and Technology, vol. 2, no. 1, 2015.

[40] B. Mobasher, "Data Mining for Personalization," in The Adaptive Web: Methods and Strategies of Web Personalization, A. K. W. N. P. Brusilovsky, Ed., Berlin-Heidelberg, Springer-Verlag, 2007, pp. 90-135.

## ACCEPTED MANUSCRIPT

[41] M. Pritchard, "Static vs Dynamic Websites," 2017. [Online]. Available: http://killerinfographics.com/blog/static-vs-dynamic-websites.html. [Accessed 2018].

[42] P. Jain, "Static Vs Dynamic Website: Advantages And Disadvantages," 27 6 2017. [Online] Available: https://www.weblinkindia.net/blog/static-vs-dynamic-website-advantagesdisadvantages. [Accessed 2018].

[43] B. Padmanabhan and A. Tuzhilin, "On the Use of Optimization for Data Mining: Theoretical interactions and eCRM opportunities," Management Science, vol. 49, no. 10, p. 1327–1343, 2003.

# ACCEPTED MANUSCRIPT

## BIOGRAPHICAL NOTE

Min Chen is an assistant professor of information systems at the School of Business, George Mason University. He received his Ph.D. from the Jindal School of Management, University of Texas at Dallas. His research interests include economics of information systems, information security, optimization methods and data mining. His research has appeared in Information Systems Research and IEEE Transactions on Knowledge and Data Engineering and has been presented at premier conferences.

## Highlights

# Improving Website Structure through Reducing Information Overload

Min Chen School of Business, George Mason University 4400 University Drive, MS5F4, Fairfax, VA 22030, mchen15@gmu.edu

 A math programming model for mitigating information overload to web users

 An effective method for website maintenance

 Extensive experiments on both real and synthetic datasets

 Superior performance over heuristics and remarkable scalability on very large datasets

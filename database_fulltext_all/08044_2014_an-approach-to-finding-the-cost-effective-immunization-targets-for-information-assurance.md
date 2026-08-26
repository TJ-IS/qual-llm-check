---
otero_id: 8044
otero_key: "75KV72SY"
title: "An approach to finding the cost-effective immunization targets for information assurance"
authors: "Guannan Liu; Jin Zhang; Guoqing Chen"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.08.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An approach to <sup>fi</sup>nding the cost-effective immunization targets for information assurance

Guannan Liu <sup>a</sup>, Jin Zhang <sup>b,</sup>⁎, Guoqing Chen <sup>a</sup>

<sup>a</sup> Department of Management Science and Engineering, School of Economics and Management, Tsinghua University, Beijing 100084, China Department of Management Science and Engineering, School of Business, Renmin University of China, Beijing 100872, China

## a r t i c l e i n f o

Article history: Received 10 February 2013 Received in revised form 3 August 2014 Accepted 7 August 2014 Available online 19 August 2014

Keywords: Information assurance Network immunization Savability Cost-effective immunization targets (CEIT)

## a b s t r a c t

Information assurance is increasing in importance as threats abound in the highly connected world of e-business. For enterprises, the goal is to achieve a secure information environment in a cost-effective manner. This paper focuses on the issue of how to cost-effectively immunize an enterprise's network to prevent threats (e.g., virus, rumor) from invading and spreading. An approach, namely Cost-Effective Immunization Targets (CEIT) is proposed as a means to identify the cost-effective immunization targets and provide direct cost/bene<sup>fi</sup>t trade-off solutions for practitioners. In the approach, a novel concept, savability, is introduced as an extension of return on security investment (ROSI), with the reduced expected infection probability as mitigated risks through immunization. Meanwhile, a bond percolation process, which can be done in just a single graph traversal, is incorporated to simplify the estimation of expected infection probability in place of repeated diffusion simulations. Theoretica analysis proves that the proposed approach can approximate the optimal solutions within a de<sup>fi</sup>nite lower bound. Finally, experiments on real-world information network datasets reveal that the algorithm CEIT outperforms other immunization strategies in both homogeneous and heterogeneous cost cases. Further, a case study indicates that the CEIT-identi<sup>fi</sup>ed immunization targets are more likely to ‘save’ the important nodes with high potential infection loss, avoiding redundant immunization

© 2014 Elsevier B.V. All rights reserved

## 1. Introduction

With the rapid development of information technology (IT) and Internet applications, many traditional stand-alone information systems (IS) have been replaced by or extended to Web-based systems. In today's e-business environment, massive data communication and business transactions <sup>fl</sup>ow across the Internet. Hence, most industries and business sectors are highly connected, ranging from manufacturing and <sup>fi</sup>nancial services, to retail, healthcare and so on. The connections have been further strengthened with new features such as mobility, virtualization, personalization, social networks, and rich-media data.

In the context of this connected world, a system can be viewed and treated as either a physical or a virtual network. Particularly, from the perspective of a company, all transactions are executed and transferred online, along with staff communications via email or other web applications. The company can then be treated as a connected information network, therefore, understanding how information <sup>fl</sup>ows and how to work with it for managerial effectiveness in an information network has recently become a focal point. The viewpoints of the studies on information <sup>fl</sup>ow in information networks can be two-fold. One is from a positive-effect perspective in light of information diffusion. That is, how information spreads across the network, what the centric nodes are in in<sup>fl</sup>uencing others (e.g., opinion leaders), and their impacts (e.g., on social business, communication, advertising) could be among the major issues of concern [1,2]. The other viewpoint is from a negative-effect perspective in light of information assurance. The major issues of concern include how a threat propagates within a network (e.g., virus infection, rumor spreading), what the most risky nodes are in causing severe harm, and how to limit their impacts (e.g., on business continuity) [3–5]. Notably, these two perspectives call for addressing a common issue that relates to the mechanism of information <sup>fl</sup>ow in a network, along with other issues relating to speci<sup>fi</sup>c problems and contextual features.

As far as information assurance is concerned, while a network facilitates communications and enables online transactions as normal traf<sup>fi</sup>c, it also faces challenges in being attacked or infected by computer viruses, breaches, malware, etc. Meanwhile, rumors, gossip or unveri<sup>fi</sup>ed information can also propagate in the network through the informational routes. It has been reported that information security breaches increased nearly 50% [6], and according to a recent survey by PwC, 93% of large organizations have suffered from breaches in 2011 [7]. Considering breaches, one of the commonly encountered threats currently, they may cause incidents such as system breakdowns, denial of services (DoS), data/infrastructure inaccessibility etc., leading to a remarkable amount of organizational expenses. For example, viruses such as ILOVEYOU, Code Red, SQL slammer, Sasser, etc. gave rise to business costs on the order of billions of dollars [8]. ICSA Labs reported that more than 83% of companies had suffered from a business loss between 10,000 and 1,000,000 dollars [9]. With respect to rumors in the workplace, they can also potentially damage reputations and affect the productivity of an organization [10]. Generally, it is apparent that because those online business and Web 2.0-based companies are more connective in operational activities and communication channels, information spreads much faster in the networks than in traditional ways. As a result, the threats and risks they face are deemed ever greater.

Having become more and more aware of the high risks of negativeeffect information, many companies are investing an increasing amount of money and resources in the hope of working with a safer network environment to guarantee normal operations. Among the many measures and strategies being implemented, immunization is a common and effective way to prevent malicious information from spreading. The IT/IS management of a company is usually responsible for the network and information assurance, thus it would generally patch the computers regularly or pre-install anti-virus software on some computers. Moreover, the IT/IS management also wants to target some working units to take measures immediately when fake/malicious information is likely to propagate within the network. However, companies are usually constrained by limited resources for information assurance. According to a survey of CIOs, the annual budget speci<sup>fi</sup>cally for information security comprised only 10% of their total IT budgets, although this amount had increased in recent years [11]. Generally speaking, because immunization can be rather costly, it is dif<sup>fi</sup>cult for managers to make effective decisions on reducing expected loss from threats and incidents based on limited resources [12]. Therefore, a strategy for identifying the costeffective immunization targets is badly needed.

In recent years, research efforts have been made to cope with related problems. Some researchers discussed the problem from an economic view, attempting to ascertain the optimal decisions on how much to invest in information assurance from a macro perspective [13–16]. Others devised various immunization strategies, in which the static network structure was a focal point in choosing immunization targets [17–20]. In this paper, we take a combined view in our investigation. That is, both the network connectivity and the dynamic diffusion process, along with immunization cost and potential loss related to information assurance incidents, are incorporated in seeking the immunization targets. Therefore, we introduce a concept, namely, savability, to evaluate the economic ef<sup>fi</sup>ciency of immunizing any network node, taking both homogeneous and heterogeneous cases into account.

In concrete terms, the main ideas and contributions of our proposed approach could be described as follows:

1. Finding the cost-effective immunization targets is a novel problem that has emerged from the information assurance practices in companies. In contrast to the previous literature that focuses on how much to invest in information assurance, the formulated problem aims to decide whether a single information unit is worth being im munized from a micro level, taking both the network structure and the dynamic diffusion process into consideration. The obtained immunization set can help information assurance practitioners allocate the limited budget more wisely.

2. To solve the cost-effective immunization problem, a greedy method (i.e., algorithm CEIT) is developed because the problem is NP-hard. A novel concept, savability, is introduced in the method to measure the return on investment of immunizing a node, with both immunization cost and infection loss considered. As for the core part of CEIT, i.e., estimating the expected infection probability, we innovatively apply a bond percolation process to replace repeated independent cascade diffusion simulations, so that the estimation of expected infection probability is simpli<sup>fi</sup>ed and the time complexity is greatly reduced.

3. Theoretical analysis has proved that the proposed algorithm is guaranteed to approximate the optimal solutions within a de<sup>fi</sup>nite lower bound. Additionally, experiments on real-world information network datasets have demonstrated that the proposed algorithm achieves greater expected reduced infection loss than other immunization strategies.

In the rest of the paper, Section 2 reviews the literature related to our work, Section 3 formulates the problem and introduces the diffusion and cost models, Section 4 proposes the Cost-Effective Immunization Targets (CEIT) algorithm, Section 5 presents the experimental results, and Section 6 applies the proposed algorithm to a real information assurance practice. Finally, the study is concluded in Section 7.

## 2. Related work

Recent years have witnessed a substantial amount of research on computer virus and rumor spreading. Many of these studies model the phenomenon in the spirit of epidemiology for investigating the propagation patterns and prevalence threshold in various types of networks and contexts [21–25]. It has been found that, for a network, immunization is an effective way to lower the epidemic threshold [26]. Thus, immunization can help prevent computer virus and rumors from prevailing and lower the <sup>fi</sup>nal infection size. Considerable effort had been devoted to identifying better immunization strategies. For instance, Target immunization aims to immunize the highly connected nodes, and it has been demonstrated that it outperformed other strategies on scale free networks [17]. Holme et al. [27] presented betweenness strategy in dealing with complex networks, which centered on the betweenness centrality of edges or nodes. Acquaintance immunization, in which random neighbors of a randomly selected node are immunized without requirements for global information of the network [18], is also an effective immunization strategy. Subsequently, further research has been conducted regarding improvements in immunization strategies, resulting in a variety of extensions [28,19,20]. In brief, these research attempts barely employ static network structural information to choose the immunization targets.

The immunization resource is usually limited for an organization [12]. Therefore, how to optimally allocate the limited resources within the network remains to be an important issue. There exist some studies on the economics of information security. Sonnenreich [13] presented a quantitative model to calculate return on security investment (ROSI), which can be used to measure the cost-ef<sup>fi</sup>ciency of security investment. Anderson et al. discussed the economics of information security from a broad perspective [14], followed by a variety of concrete economic models concerning the cost and loss in information security investment. Gorden and Loeb employed a cost-bene<sup>fi</sup>t analysis to determine the optimal level of resources to devote to securing information [15]. Lee et al. [16] presented an economic model from the bene<sup>fi</sup>t of a customer, and they derived the optimal investment decisions for <sup>fi</sup>rms. Kleczkowski et al. minimized the total cost of treatment and prevention by performing simulations, and derived an optimal control size [29]. Although the economics of information assurance is discussed in these studies, these models are established generally without considering the speci<sup>fi</sup>c network structure where the nodes are usually assumed to be homogeneous and treated equally. The problems they solved may only help practitioners to decide how much they should invest in information assurance from a global perspective, while the question of whether an information unit or a node within the network is worth being immunized remains unanswered. In contrast, our proposed approach combines the cost analysis with the connectivity of each node, as well as the dynamic diffusion process, to help companies make a cost-effective decision on choosing immunization targets.

Finally, it is worth mentioning that this research problem is also related to the in<sup>fl</sup>uence maximization problem, which is oriented to seed k nodes that could maximize the in<sup>fl</sup>uenced size under certain diffusion models. Firstly discussed by Richardson and Domingos [30], Kempe et al. then proved that the problem is NP-hard and proposed a greedy approximation method [31] through diffusion simulations. Further, a number of studies followed in the same direction. Leskovec et al. proposed the CELF algorithm [32] that could largely reduce the evaluation time by exploiting the submodularity property of the problem. They also associated each seeding node with a certain cost and maximized the ‘reward’ of the set of seeding nodes. Chen et al. [33] further reduced the running time and proposed a new heuristic method, i.e., DegreeDiscount, that could achieve an acceptable performance. More work has been found in adapting from the original greedy method to improve algorithmic ef<sup>fi</sup>ciency and solve speci<sup>fi</sup>c problems under different contexts [3]. Notably, the problem we aim to solve is in a different setting compared with the in<sup>fl</sup>uence maximization problem. The objective for our problem is to minimize the loss resultant from virus and information propagation with limited immunization resources.

## 3. The cost-effective immunization problem

## 3.1. Problem definition

As mentioned above, without proper preventive measures, the threat of computer viruses or rumors could evolve into a major disaster and cause a huge loss to an organization. Speci<sup>fi</sup>cally, companies face two types of expenditures concerning information assurance incidents [6]. One is the cost devoting to preventing virus from invading (immunization cost), and the other is the potential loss that stems from infection and remediation measures (infection loss). We associate each node s with a cost $c _ { s }$ if immunized, and meanwhile let $\mathcal { L } _ { i }$ be infection loss for an infected node i. Let $\mathcal { G } = ( \nu , \mathcal { E } )$ <sup>L</sup>be an undirected information network, <sup>G ¼ Vð ÞE</sup>with being a set of nodes representing information nodes or business units in an organization, and being a set of edges each of which de-<sup>E</sup>notes the communication and interaction between every two nodes.

Assume that a small set of nodes $\nu _ { 0 }$ is initially infected, either by a <sup>V</sup>virus or a piece of information. Then, the infected nodes could potentially infect other nodes that have direct communications with them. The infection occurs in a cascade way and <sup>fi</sup>nally reaches the set of nodes $\mathcal { T } ( \nu _ { 0 } )$ . A preventive measure to immunize a set of nodes is taken before infection actually occurs. The immunization for the set contributes to the cost $c ( \boldsymbol { S } )$ , while it can only be implemented within a budget of ω. $\mathsf { L e t } \mathcal { T } ( \gamma _ { 0 } , S )$ <sup>S</sup>denote the set of nodes with respect to the immunization set ${ \mathcal { S } } .$ <sup>V ÞS</sup>. Then, the goal is to minimize the total infection loss by <sup>S</sup>immunizing a set of nodes bounded by a constraint of immunization budget ω.

Thus, the problem can be formulated as,

$$
\min_{\substack{\sum_{i\in \mathcal{I}(\mathcal{V}_{0},\mathcal{S})}\mathcal{L}_{i} + c(\mathcal{S})\\ \text{st.} c(\mathcal{S})\leq \omega}}.\tag{1}
$$

Here, for the sake of simplicity (without affecting the generality of Eq. (1)), we assume that the immunization cost is additive, $\operatorname { i . e . , } c ( S ) =$ $\textstyle \sum _ { s \in S } c _ { s }$ <sup>ð Þ ¼S</sup>. In practical information assurance, the real immunization <sup>S</sup>cost could decrease marginally. For example, an anti-virus software company may offer an organization some discounts if more computers are installed with the software. In this regard, the model could be changed with a different cost function form for the whole batch of the immunization set. If the nodes are immunized in a sequence, the nodes immunized later can sequentially enjoy a discount $r _ { \mathbf { \theta } _ { \mathbf { \theta } } } ^ { n }$ , where r denotes the discount rate, and n denotes the number of nodes that have been immunized. In this case, the marginal decreasing effect of immunization cost could be modeled using a different cost function from that in Eq. (1).

## 3.2. Diffusion models

Traditional epidemiology research adopts SIS (susceptible-infectedsusceptible) and SIR (susceptible-infected-recovered) models to study virus propagation, i.e., nodes are divided into distinct compartments and transit from one state to another with certain probability in the system [34]. These models have also been extended to the investigation of computer virus and rumor spreading [21,5]. Basically a homogeneous or scale-free network is generally assumed in these models. These models could capture the propagation patterns in a macro level through analytical solutions derived from mean-<sup>fi</sup>eld equations, however, the infection detail of each node is ignored. In this regard, they are not considered to be ideal diffusion models to investigate immunization strategies, because immunization decisions need to be made with detailed information of each infected node.

In a general scope, independent cascade (IC) is a common model to describe information and virus diffusion [31]. This is particularly applicable in the contexts of internet applications, dynamic networking, and social networks [3,33,32]. It has also been applied in the <sup>fi</sup>eld of epidemics [35]. IC starts with several initially infected nodes $\nu _ { 0 }$ and decomposes diffusion into discrete time processes. When node v is infected at time t, it has a chance to infect its non-infected neighbor w $( w \in$ neighbors(v)) with an independent probability $p _ { v , w \ast }$ . The newly infected nodes at t could further propagate the virus to the non-infected neighbors in the same manner, and the process terminates until no new infection occurs. In this paper we exploit the IC model as the propagation mechanism to study immunization strategies in the network.

## 3.3. Cost of information assurance

As has been mentioned previously, companies usually have limited IT staff and budget for securing information and application systems. In consideration of both immunization cost and infection loss, we have two different scenario cases, namely, the homogeneous case and the heterogeneous case, each with a different cost setting.

## 3.3.1. Homogeneous case

In the homogeneous case, we assume that immunization cost $c _ { s }$ for any node $s \in { \mathcal { S } }$ and infection loss $\mathcal { L } _ { i }$ for any node $i \in \mathcal { T } _ { p } ( \mathcal { V } _ { 0 } , S )$ are the <sup>S L I ð ÞV S</sup>same respectively. Therefore, in this case the total infection loss equals the infection size multiplied by the unit loss, and the total immunization cost equals the size of the immunization set multiplied by the unit cost. As a result, the problem can be simpli<sup>fi</sup>ed as minimizing the infection size $\mathcal { T } ( \nu _ { 0 } , S )$ with a constraint of immunization size $| S | \le k$ , where $k = \omega / c .$

## 3.3.2. Heterogeneous case

Existing studies did not consider the heterogeneous cost of different nodes. However, in the real-world information assurance practice, cost and infection loss are not easy to estimate for different nodes or business units. This is because the cost and loss concerning information assurance are not always de<sup>fi</sup>nite in monetary terms. Meanwhile, different nodes may have distinctive connections, thus they play different roles within the network. For instance, the email network of a company may consist of employees and interactions between them. In the company's email network, managers usually have more connections with others than their subordinates, and con<sup>fi</sup>dential commercial <sup>fi</sup>les are more likely to be transferred by them. Another example is the role of certain secretaries, who are indispensable in a sense that they disseminate information to staff in multiple departments including VIPs. Therefore, it would create huge losses if their email accounts were infected. This means that different nodes may possess diverse levels of importance, resulting in heterogeneous infection loss and immunization cost.

In this paper, we exploit a cost function to model the heterogeneity of different units/nodes and approximate the cost for these immunized nodes $s \in { \mathcal { S } }$ with respect to their relative importance within an organization's network.

$$
c (s) = 1 + \alpha \left(1 - e ^ {- \beta \cdot \psi (s)}\right)\tag{2}
$$

where $\psi ( s )$ denotes the importance for node s, and α and β are adjusting parameters. The function form of the cost is assumed according to typical economic research with concavity property [15,36–38] as $\frac { \partial c ( s ) } { \partial \psi ( s ) } > 0$ and $\frac { \partial ^ { 2 } c ( s ) } { \partial \psi ( s ) ^ { 2 } } < 0$ <sup>ð Þ</sup>, meaning that the cost is increasing while the marginal <sup>ð Þ</sup>cost is decreasing with the node's importance. When $\psi ( s ) = 0 ,$ , the immunization cost c(s) remains at the lowest value 1. When the degree is extremely large, the immunization cost approaches the upper bound $1 + \alpha .$ It can be easily seen that when $\beta = 0$ , the heterogeneous case could degrade to the homogeneous case as $c ( s ) \equiv 1$ for all nodes.

Usually the degree of connectivity represents the extent to which the nodes are linked. Thus, it partly re<sup>fl</sup>ects the importance level of the nodes within the network. Accordingly, high-degree nodes are considered more signi<sup>fi</sup>cant and expensive in implementing information assurance measures than other nodes in the network. In this case, importance can be measured through the degrees of nodes, i.e., $\psi ( s ) = $ deg(s). Moreover, the importance of nodes in a network can also be determined by some other factors such as volume of communication traf<sup>fi</sup>c, information content, etc. These factors could be captured by changing or extending the arguments of ψ(·) according to the practical situations.

In the proposed function form, the two parameters α and β have actual meanings corresponding to the costly immunization in practice. The function curves with different α and β values are displayed in Fig. 1. As seen in Fig. 1, α determines the upper limit of the curve, representing the immunization investment devoted on each unit; β determines how fast the curve converges to the upper limit, representing the cost distribution with respect to the node importance. For instance, when $\beta = 0 . 3$ , the cost curve reaches the near maximal value very fast, indicating that most nodes receive almost the same level of immunization investment except for a small portion of insigni<sup>fi</sup>cant nodes; when $\beta = 0 . 0 5$ , the slope of the curve becomes <sup>fl</sup>at, which corresponds to the situation that immunization cost is distributed strictly according to the node's importance in the network, with large variance in cost values. From the perspective of information assurance practice, the practitioners could determine the two parameters based on the information assurance budget and their expert knowledge concerning the organizational structure, i.e., the cost distribution with respect to different node importance. For example, in a hierarchical company where information <sup>fl</sup>ows strictly in a tree structure, each layer has a different role in information diffusion, thus the immunization cost for different nodes can vary greatly. In this regard, the value of β can be set small in order to distinguish the cost variety. However, in a company with a <sup>fl</sup>at organization structure where information <sup>fl</sup>ows freely within the network, any node may have the chance to infect other nodes and become infected, leading to the setting of a greater value for $\beta .$

![](/api/attachments/75KV72SY/fulltext/images/7a7682320e39ba16b7a74ba64aece1565458715e76660d63d052832c646d77de.jpg)  
Fig. 1. Heterogeneous cost function with respect to different α and β values

Similarly, infection loss $\mathcal { L } _ { i }$ for any infected node $i \in \mathcal { T } ( \mathcal { V } _ { 0 } , S )$ can also vary over the importance of nodes. A similar function form assumed for the heterogeneous infection loss could be $\mathcal { L } _ { i } = 1 + \alpha ^ { \prime } \Big ( 1 { - } \mathrm { e } ^ { - \beta ^ { \prime } \cdot \psi ( i ) } \Big )$ where α′ and $\beta ^ { \prime }$ <sup>L ¼ þ</sup>are adjusting parameters as well. Furthermore, other forms of cost and loss functions according to the requirements of information assurance practice may also be applied, which would not in<sup>fl</sup>uence the implementation of the proposed algorithm.

## 4. Proposed algorithm

## 4.1. Greedy method

One straightforward way to solve the cost-effective immunization problem in Eq. (1) is to exhaustively search for all of the combinations of the nodes within the immunization budget ω and then compare the infection loss with respect to these different sets. However, the problem is generally NP-hard in complexity, and due to the large number of nodes in the network, only an approximation algorithm could be used to solve the problem.

Greedy methods usually search for local optimal solutions in each greedy step to approximate the global optimal solutions. Thus, a greedy method could also be developed to search for the cost-effective immunization set . This can be realized with an initial empty set, followed by iteratively identifying one node that can ‘save’ other nodes most cost-effectively to add it to the set until the immunization budget is reached. Therefore, a critical task in this method is to design an appropriate function to evaluate the economic ef<sup>fi</sup>ciency of investing in immunizing a node.

## 4.2. Savability

Concerning the bene<sup>fi</sup>t to a company, the cost devoted to immunizing the information network can be regarded as an investment in information assurance that aims to lower the potential risks. Therefore, the cost–bene<sup>fi</sup>t analysis is usually exploited to analyze the rationality of investment. Sonnenreich et al. [13] de<sup>fi</sup>ned return on security investment as ROSI = (risk exposure · % risk mitigated solution cost) / solution cost. Then with the two types of cost under both homogeneous and heterogeneous cases, the ROSI to measure the economic ef<sup>fi</sup>ciency of immunizing node k can be estimated. Let k denote the set of <sup>Að Þ</sup>nodes that are ‘saved’ through immunizing node k, then the risk mitigated of immunizing k is indeed the reduced infection loss, that is, the total loss of k if not immunized otherwise. Then the ROSI of immu-<sup>Að Þ</sup>nizing k can alsobe viewed as node k's ability to save other nodes. Here, we introduce the concept of savability, which can be de<sup>fi</sup>ned as follows.

## De<sup>fi</sup>nition 1. Savability

The savability of a node k is de<sup>fi</sup>ned as the return on security investment of immunizing k, denoted as $s _ { a } ( k )$

$$
s _ {a} (k) = \frac {\sum_ {i \in \mathcal {A} (k)} \mathcal {L} _ {i}}{c (k)}\tag{3}
$$

Different immunization strategies can be compared based on the concept of savability. As an example, Fig. 2 depicts a virus diffusion graph. Suppose that node 1 is initially infected, and each edge in this graph is activated so that the virus could spread throughout. Therefore, all of the nodes would be infected without proper immunization measures. Intuitively, nodes 3, 5, and 6 are all good choices since the infection size can be largely reduced if they are immunized before the virus breaks out. If node 3 is immunized, the nodes on its right would never get infected; and it is the same for nodes 5 and 6. In the homogeneous case, each node has the same immunization cost, then node 3 is the best choice because it saves the most nodes (i.e., nodes 3, 5, 6, 7, 8) with $s _ { a } = 5 .$ . In the heterogeneous case, node 3 may not be the best choice because high degree nodes generally cost more. Let $\alpha =$ $5 , \beta = 0 . 1$ in accordance with Eq. (2), and the infection loss is assumed to be homogeneous for all nodes $( \mathrm { i } . \mathsf { e } . , \beta ^ { \prime } = 0 )$ . Then the immunization cost for these nodes are $c ( 3 ) = 2 . 6 5 , c ( 5 ) = 1 . 9 1 , c ( 6 ) = 2 . 3 0$ . Thus, savability for immunizing the three nodes are $s _ { a } ( 3 ) = 5 / 2 . 6 5 =$ $1 . 8 9 , s _ { a } ( 5 ) = 4 / 1 . 9 1 = 2 . 1 0 , s _ { a } ( 6 ) = 3 / 1 . 3 1 = 1 . 3 1$ respectively. Apparently, node 5 (rather than node 3) is a better choice in the heterogeneous cost case.

![](/api/attachments/75KV72SY/fulltext/images/bd741b6831c1f54989071a8426292bbfd822d7fb34ef0b9a1d4eac1d5da37702.jpg)  
Fig. 2. Diffusion graph.

## 4.3. Expected infection probability

Information and viruses spread in a random process, thus whether a node can be ‘saved’ by an immunization target is uncertain. As for Eq. (3), the numerator (i.e., the mitigated risks of immunizing k) should be estimated in a different way because the set of k cannot be directly obtained.

Although immunizing a node cannot guarantee ‘saving’ a speci<sup>fi</sup>c node, the probability of some nodes being infected would de<sup>fi</sup>nitely be lowered due to the immunization. Therefore a desirable metric to measure the extent to which a node is ‘saved’ should be the lowered probability of the node being infected through immunization. From the perspective of mathematical expectation, we can <sup>fi</sup>rstly de<sup>fi</sup>ne the expected infection probability of a node as follows.

## De<sup>fi</sup>nition 2. Expected infection probability

The expected infection probability of a node is the expected probability of the node being infected in all situations of initial infection.

According to the de<sup>fi</sup>nition of expected infection probability, independent cascade simulations can initially be performed to derive the infection results for each node. Considering all situations of initial infection, each independent cascade simulation should be triggered with a different initially infected node, so there are initial situations in <sup>jVj</sup>total (i.e., the number of nodes in the network). To obtain the estimated expectation value, the simulation has to be replicated for multiple R times. Then the expected infection probability of a node i can simply be estimated as the frequency of getting infected in the total R simulation times:

$$
\operatorname * {P r} _ {i} = \frac {\# i \text {   is   infected }}{R \cdot | \mathcal {V} |}.\tag{4}
$$

When a node is immunized, it would not get infected and all the nodes connecting to it are secured. Therefore, when estimating the expected infection probability with respect to an immunization set , those immunized nodes can be removed from the graph before the diffusion simulation process, and $\operatorname* { P r } _ { i } ( S )$ can be obtained according to Eq. (4).

With the estimated expected infection probability for each node i, the expected reduced infection loss of i, if k is added to the original immunization set $s ,$ can be calculated as,

$$
\mathcal {R} _ {i} (k) = \mathcal {L} _ {i} \cdot [ \operatorname * {P r} _ {i} (\mathcal {S}) - \operatorname * {P r} _ {i} (\mathcal {S} \cup k) ]\tag{5}
$$

Here $\mathcal { R } _ { i } ( k )$ can also be viewed as the revenue of the ‘saved’ node i by investing on immunizing node k. Furthermore, the total cost savings from investing on the immunization candidate k should be the sum of the revenues of all the nodes in the network. Given the de<sup>fi</sup>nition of savability, the savability of immunizing candidate k is,

$$
s _ {a} (k) = \frac {\sum_ {i \in \mathcal {V S} , i \neq k} \mathcal {R} _ {i} (k)}{c _ {k}}.\tag{6}
$$

Thus, the savability function $s _ { a } ( \cdot )$ can be used as the evaluation function to choose the local optimal solutions for the cost-effective immunization problem. That is, at every iteration, the node k<sup>∗</sup> that maximizes $s _ { a } ( \cdot )$ will be added to the immunization set, $\mathrm { i . e . }$

$$
k ^ {*} = \underset {j \in \mathcal {V} \backslash \mathcal {S}} {\operatorname{argmax}} s _ {a} (j)\tag{7}
$$

To further illustrate how the greedy method is formulated with the evaluation function, a methodological framework is depicted in Fig. 3. It starts with the immunization budget and an information network, along with an empty immunization set. Within the budget, diffusion simulations are implemented multiple times to derive the expected infection probability with respect to each immunization candidate, and then the savability is evaluated for the immunization candidate. Subsequently, the node with maximum savability is added to the immunization set, and the iteration ends when the immunization set exceeds the budget. Note that evaluating savability for each node is the core of the greedy method, which calls for estimating the expected infection probability of all of the other nodes. This can be done through repeated Monte Carlo simulations, which, however, are regarded to be quite time consuming. This further motivates us to introduce a more ef<sup>fi</sup>cient method for estimating the expected infection probability, which will be discussed in the next subsection.

## 4.4. Enhanced expected infection probability estimation

Infection is supposed to occur independently with probability $p _ { v , w }$ through the edge vw in discrete time in the independent cascade model. Therefore, Newman [23] proposed bond percolation (BP) process in graphs. In the process, whether the infection could diffuse across each edge is pre-determined, according to a speci<sup>fi</sup>c probability distribution. It is also shown that the process can be well mapped to a typical SIR model [23,4]. With the bond percolation process, independent cascade simulations in graphs can be implemented in a much simpler way [4].

In the bond percolation process, a coin with bias of $p _ { v , w }$ is <sup>fl</sup>ipped on each edge to determine whether it is ‘active’. The ‘active’ edges are treated as the routes that allow actual infection from one end to the other of the edge. Then by removing the ‘inactive’ edges we obtain a diffusion graph.

As illustrated in Fig. 4, we have an original graph in Fig. 4(a), then we can perform the bond percolation process with a uniform probability p on each edge. Edges (1, 5), (1, 7), and (8, 10) become ‘inactive’, then we can remove these edges and obtain the diffusion graph as shown in Fi

<sup>G</sup>Through the bond percolation process, the diffusion graph can be <sup>G</sup>derived from the original graph , which corresponds to a complete dif-<sup>G</sup>fusion process. It can be easily seen that given the initial infected node, all the other nodes in the graph $\mathcal { G } ^ { \prime }$ that have paths to it would <sup>fi</sup>nally get <sup>G</sup>infected. For example, if node 1 is initially infected as shown in Fig. 4(b), nodes 2, 4, 6–10 would all get infected and the <sup>fi</sup>nal infection size is 8 because they are all reachable from node 1. Nodes 3 and 5 lie in a different connected component consisting of only two nodes, thus they would not become infected. Therefore, through the bond percolation process, we know exactly which nodes would get infected given the initial infected node. Notably, the nodes in the same connected component subgraph can be reachable from each other. Then we have the following property.

![](/api/attachments/75KV72SY/fulltext/images/deeda634b031ee09af765c001323f5ca294fa325121fff535cf48a3e432add60.jpg)  
Fig. 3. Framework of the greedy method.

Property 1. All the nodes contained in a connected component of would <sup>G</sup>get infected only if any node within this component is initially infected. Denote $C C ( \nu _ { i } ; \mathcal { G } ^ { \prime } )$ as the connected component that includes node $\nu _ { i \cdot }$ Then we have, $C C ( \nu _ { i } ; \mathcal { G } ^ { \prime } ) \subseteq \mathcal { T } _ { p } ( \mathcal { V } _ { 0 } ) , \mathrm { i f } \nu _ { i } \in \mathcal { V } _ { 0 }$

With this property, the connected component subgraphs of the diffusion graph $\mathcal { G } ^ { \prime }$ manifest all the possibilities of nodes being infected. This can be obtained by a single traversal of . Again, take the diffusion <sup>G</sup>graph in Fig. 4(b) as an example, nodes 1, 2, 4, and 6–10 are in the same connected component, meaning that they would all become infected provided that any of them are initially infected.

According to Property 1, when node v is located in the same connected component of the diffusion graph $\mathcal { G } ^ { \prime }$ with the initially infected node $\nu _ { 0 } ,$ <sup>G</sup>it would become infected. Hence, the frequency that v gets infected is indeed the size of the component that it locates in, i.e., $| C C ( \nu ; \mathcal { G } ^ { \prime } ) |$ . Therefore, the expected infection probability of node v $\left( \mathrm { i } . \mathrm { e } . , \mathrm { P r } _ { \nu } \right)$ can be estimated as the size of the connected component that contains v divided by the total number of nodes in the network, as demonstrated in Eq. (8).

$$
\operatorname * {P r} _ {v} = \frac {\left| C C (v ; \mathcal {G} ^ {\prime}) \right|}{| \mathcal {V} |}\tag{8}
$$

For example, as shown in Fig. 4(b), there are 10 nodes in total. Because node 1 is in a component of size 8, its expected infection probability is estimated to be $8 / 1 0 = 0 . 8 ;$ likewise, the expected infection probability of node 3 is estimated to be $2 / 1 0 = 0 . 2$

Correspondingly, an enhanced estimation procedure could be conducted in the following way. First, the bond percolation process is performed on the original graph with probability distribution P on all <sup>G</sup>of the edges in order to derive the diffusion graph $\mathcal { G } _ { P } ^ { \prime }$ . Next, traverse $\mathcal { G } _ { P } ^ { \prime }$ <sup>G</sup>and obtain the set of connected component subgraphs $C C _ { i } ,$ <sup>G</sup>the union of which just equals the set of the nodes, $\mathrm { i . e . , } \cup _ { i = 1 } ^ { m } C C _ { i } = \mathcal { V } ,$ where m is the number of connected components in $\mathcal { G } _ { P } ^ { \prime }$ <sup>¼</sup>. After deriving the set of connected component subgraphs from $\mathcal { G } _ { P } ^ { \prime } ,$ <sup>G</sup>, the expected infection probability of node v, i.e., $\mathrm { P r } _ { v } ,$ <sup>G</sup>can be directly estimated in light of Eq. (8). Meanwhile, the expected infection probability is the same for all the other nodes that lie in the same connected component $C C ( \nu ; \mathcal { G } _ { P } )$ with v. Concretely, this procedure is detailed in Algorithm 1 (eProbEstimation).

With the eProbEstimation procedure, it is no longer necessary to implement repeated simulations with each node being initially infected. Thus, the estimation time is greatly reduced.

(a) Before percolation

(b) After percolation

![](/api/attachments/75KV72SY/fulltext/images/ce8520ed664885dd2ae637e554361a9e00aadb580736a684f3c7ce2f77e61294.jpg)  
Fig. 4. Example of bond percolation.

## Algorithm 1. eProbEstimation

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1: Input: graph  $\mathcal{G}(\mathcal{V},\mathcal{E})$ , infection probability distribution P, node v, iteration round R.
2: Output: the expected infection probability  $Pr_{v}$  of node v,
the connected component subgraphs v lies in  $CC(v;\mathcal{G}_{P})$ 
3: for j=1 to R do
4:  $G_{P} \leftarrow$  perform BP process with P on G
5: connected component subgraphs  $CC \leftarrow$  traverse  $G_{P}$ 
6:  $CC(v;G_{P}) \leftarrow$  the component subgraph v lies in
7:  $Pr_{v} + = |CC(v;G_{P})|/|\mathcal{V}|$ 
8: end for
9:  $Pr_{v} = Pr_{v}/R$
</div>

## 4.5. Algorithm CEIT

As has been discussed in previous sections, we design a measure savability to evaluate the economic ef<sup>fi</sup>ciency of immunization candidates. In addition, the bond percolation process is used to simplify the estimation of the expected infection probability. Subsequently, a new greedy method CEIT to solve the original problem can be formulated, which is detailed in Algorithm CEIT.

## Algorithm 2. Algorithm CEIT

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1: initialize network $\mathcal{G}(\mathcal{V},\mathcal{E})$, infection loss $\mathcal{L}$, immunization cost $c$, initialize $\mathcal{S}=\emptyset$
2: while $c\leq\omega$ do
3:    set $sa_{j}=0$ for each $v_{j}\in\mathcal{V}\setminus\mathcal{S}$
4: $\mathcal{G}^{\prime},\mathcal{V}^{\prime}\leftarrow\mathcal{V}\setminus\mathcal{S}$
5:    for each vertex $v_{j}\in\mathcal{V}\setminus\mathcal{S}$ do
6:    $\mathrm{Pr}_{v_{j}}, CC(v_{j};\mathcal{G}_{P})=\mathrm{eProbEstimation}(\mathcal{G}^{\prime},v_{j},p)$
7:    $\mathcal{G}^{\prime\prime},\mathcal{V}^{\prime\prime}\leftarrow CC(v_{j};\mathcal{G}_{P})\setminus\{v_{j}\}$
8:    for $v_{c}\in\mathcal{V}^{\prime\prime}$ do
9:    $\mathrm{Pr}_{v_{c}}=\mathrm{eProbEstimation}(\mathcal{G}^{\prime\prime},v_{c},p)$
10:    $sa_{j}=sa_{j}+\mathcal{L}_{c}(\mathrm{Pr}_{v_{j}}-\mathrm{Pr}_{v_{c}}(\mathcal{S}\cup v_{j}))$
11:    end for
12:    $sa_{j}=sa_{j}/c_{j}$
13:    end for
14:    $k^{*}=\operatorname{argmax}_{v_{i}\in\mathcal{V}\setminus\mathcal{S}}sa_{i}$
15:    $\mathcal{S}=\mathcal{S}\cup k^{*}$
16:    $c+=c_{k^{*}}$
17: end while
18: return $\mathcal{S}$
</div>

As illustrated in lines 5–13 of Algorithm CEIT, each candidate node $\nu _ { j }$ has to be temporarily added to the immunization set in evaluating its savablity. Speci<sup>fi</sup>cally, the node $\nu _ { j }$ and all of the links connected to it are removed from the immunized graph ${ \mathcal { G } } _ { \mathrm { ~ , ~ } } ^ { \prime }$ , with a subgraph ${ \mathcal { G } } ^ { \prime \prime }$ remaining. Then the procedure eProbEstimation on ${ \mathcal { G } } ^ { \prime \prime }$ is performed to derive <sup>G</sup>the expected infection probability for each node in the same connected component with v . In accordance with Property 1, immunizing a certain node could ‘save’ only the nodes contained in the same component with it, while the expected infection probability of others outside the component would remain the same. Hence, only the nodes $v _ { c } \in \mathcal { V } ^ { \prime \prime }$ can contrib-<sup>V</sup>ute to the candidate's savability and need to be considered. It reveals the fact that the nodes lying in the large connected component are more likely to be chosen as immunization candidates, since they are enabled to ‘save’ more nodes.

As shown in Fig. 4(b), the graph has already been percolated. We then implement Algorithm CEIT on the graph as an example. First, as mentioned above, the expected infection probability for each of the nodes 1, 2, 4, 6–10 is $8 / 1 0 = 0 . 8$ , and that for nodes 3 and 5 it is $2 / 1 0 = 0 . 2 .$ . Next, we temporarily immunize each node to calculate its savability. By immunizing node 1, the node and all its links are removed, then nodes 2 and 4 become separated from the original component, as a result their expected infection probability drops from 0.8 to $1 / 1 0 = 0 . 1 $ Nodes 6–10 are still connected with each other, the infection probability drops to $\textstyle { 1 4 / 1 0 = 0 . 4 } .$ . For nodes 3 and 5, since they are located in a different component, immunizing 1 has no effect on them. Assuming that the cost and infection loss are homogeneous $( \mathrm { i . e . }$ , remains constant at 1) for all the nodes, the savability of node 1 is: $s _ { a } ( 1 ) = ( 0 . 8 - 0 . 1 ) \times$ $2 + ( 0 . 8 \mathrm { ~ - ~ } 0 . 5 ) \times 5 = 2 . 9$ . If we immunize node 6, the original component is split into two: a component with nodes 1, 2, and 4 and a component with nodes 7–10; so the savability of node 6 is: $s _ { a } ( 6 ) =$ $( 0 . 8 ~ - ~ 0 . 3 ) \times 3 ~ + ~ ( 0 . 8 ~ - ~ 0 . 4 ) \times 4 = 3 . 1$ . Likewise we can get the savability for node $8 , s _ { a } ( 8 ) = ( 0 . 8 - 0 . 4 ) \times 4 + ( 0 . 8 - 0 . 1 ) +$ $( 0 . 8 \mathrm { ~ - ~ } 0 . 2 ) \times 2 = 3 . 5$ . The savability for the other nodes can also be calculated, but they cannot compete with nodes 1, 6, and 8. Therefore, in the homogeneous cost case, node 8 is the optimal choice. While in the heterogeneous case, savability should be calculated with respect to corresponding cost functions, thus the strategy might be different.

Compared to the static network structure based immunization strategies, Algorithm CEIT does not merely search for the nodes with high connectivity. As a matter of fact, the procedure can be viewed as a weighted voting system. In this voting system, each ‘saved’ node can vote for the immunization candidates according to the extent to which they are ‘saved’ (i.e., the reduced expected infection probability), while the important nodes with higher infection losses enjoy greater weights. Therefore, CEIT gives consideration to both the ‘saved’ quantity and quality based on the dynamic diffusion process, which conforms to the pursuit of cost-effectiveness. Meanwhile, CEIT achieves a satisfactory running time with the procedure of eProbEstimation. Through the eProbEstimation procedure, the averaging operations for all initial infection scenarios can be done in a single graph traversal at a time complexity level of $O ( | \mathcal { V } | + | \mathcal { E } | )$ . Since we need to evaluate the candidate <sup>O Vj þ jEð Þj j</sup>immunization targets one by one, which makes the whole time complexity at a level of $\mathcal { O } ( k R | \mathcal { V } | ( | \mathcal { V } | + | \mathcal { E } | ) )$ . This is much more ef<sup>fi</sup>cient than it would be without the percolation process.

## 4.6. Theoretical analysis

This section provides a theoretical analysis of the properties of the evaluation function Sa(·) so as to demonstrate its submodularity, which is important for guaranteeing a desirable approximation to the optimal solutions with the proposed algorithm.

## Theorem 1. Sa(·) is a submodular function.

## Proof. The proof of the theorem can be found in Appendix A.

As proved in [39], if the evaluation function of a greedy algorithm is a submodular and non-decreasing set function, it can guarantee achieving at least a constant fraction $( 1 - 1 / \mathsf { e } )$ of the optimal solutions. Theorem 1 has proved the submodularity property of the function Sa(·). Moreover, in the homogeneous cost case, Sa(·) is non-decreasing. As far as the proposed algorithm is concerned, the results of the derived immunization set in the homogeneous case can provide an at least $( 1 - 1 / \mathsf { e } )$ approximation to the optimal solutions. For the heterogeneous cost case, the non-decreasing property of the evaluation function does not hold. It has been proved in [40] that a better solution between the homogeneous and heterogeneous cases can also guarantee a near optimal solution with a lower bound for the budgeted max-cover problem. Thus, for the cost-effective immunization problem with heterogeneous cost, by comparing the immunization set with heterogeneous cost settings $\boldsymbol { S } _ { h e t e r }$ and the set obtained from homogeneous case settings $S _ { h o m o }$ , the <sup>S S</sup>set with higher savability can then be obtained, i.e., $S ^ { * } = \operatorname * { a r g m a x } \{ S a ( S _ { h o m o } ) , S a ( S _ { h e t e r } ) \} . \ : S ^ { * }$ can still guarantee a $\scriptstyle { \frac { 1 } { 2 } } ( 1 - 1 / e )$ approximation to the optimal solutions.

In sum, although the proposed algorithm is in a greedy manner, which only guarantees the local optimum, the approximated solutions from the proposed approach can theoretically guarantee near optimal solutions with a de<sup>fi</sup>nite lower bound.

## 5. Experiments

## 5.1. Experimental setup

The experiments were conducted with three real world information networks, namely, an email network of a research institute EUMail [41], a blog reading network GDMB and a collaboration network CCMP [41]. Table 1 summarizes the main properties of the networks.

Table 1 Statistics of network datasets.

<table><tr><td>Dataset</td><td>Nodes</td><td>Edges</td><td>Avg. degree</td><td>Avg. clustering coef.</td></tr><tr><td>EUMail</td><td>32529</td><td>55261</td><td>3.40</td><td>0.112</td></tr><tr><td>GDMB</td><td>21775</td><td>110535</td><td>10.15</td><td>0.415</td></tr><tr><td>CCMP</td><td>23133</td><td>93497</td><td>8.08</td><td>0.633</td></tr></table>

## 5.1.1. EUMail network dataset

Emails are widely used communication channels, but the email network often faces information assurance incidents such as breaches, worms, and other malicious information due to its high frequency and widespread use. Thus, immunizing the email network from an organization level is quite necessary. The EUMail network is an email network of a research institute in Europe [41], with email accounts as nodes and communications between these accounts as edges. Because the original dataset contains only a small part of email accounts that both sent and received emails within the time span concerned [41], we extracted the largest strongly connected component only retrained bi-directional edges to conduct the experiments. Through this preprocessing, we are left with a network of 32,529 nodes and 55,261 edges.

## 5.1.2. GDMB network dataset

The GDMB network dataset is a blog reading network collected from the internal blog system of one of the largest mobile operators in south China. The corporation established an internal blog system in 2006, and each staff owns a personal account. The staff can publish articles and read or comment on others' blogs. In just a few years, the blog system has become a popular way for the staff of the corporation to communicate to each other both at work and in leisure time. However, some negative or fake information can also propagate in the blog network due to a lack of proper supervision and handling, which may be harmful to the organization. Thus, it is important to take immunization as an effective measure to secure the normal operation of the blog system. We collected the blog reading data of 30 months from March 2008 to September 2010, constituting a blog reading network. In the network, each user i is regarded as a node, and the network contains an undirected edge from i to j if they had ever read each other's blogs in a reciprocated manner within the time span. Totally, the network is composed of 27,958 nodes and 137,814 edges.

## 5.1.3. CCMP network dataset

The CCMP network dataset consists of 23,133 nodes and 186,936 edges [41]. It re<sup>fl</sup>ects the collaborations between authors in Condense-Matter Physics category from the e-print of arXiv covering papers in the period from January 1993 to April 2003. Collaboration networks are often used to conduct experiments on information diffusion [33], as it represents the communication between scholars. Each scholar is treated as a node in the network, and if scholar i and scholar j have ever co-authored a paper, an undirected edge is established between i and j.

All the experiments were performed on the Desktop with Intel(R) Core(TM) i3-2100 CPU(3.10 GHz) and 4 GB of memory running the Microsoft Windows 7 Ultimate operating system.

## 5.2. Comparison strategies

In the experiments, algorithm CEIT of the proposed approach was compared with four other immunization strategies, namely Target immunization, Betweenness immunization, DegreeDiscount and Random immunization. They are all typical immunization strategies commonly used in research and practice.

• Target immunization: In Target immunization, the nodes with high degrees are immunized in priority. It is regarded to be a simple but effective method for scale-free networks, as has been proved analytically [17].

• Betweenness immunization: Betweenness centrality of a node v is the sum of fractions of all pairs of shortest paths that pass through v [42]. It can be calculated by the following equation.

$$
C _ {B} (v) = \sum_ {s \neq v \neq t \in \mathcal {S}} \frac {\sigma (s , t | v)}{\sigma (s , t)}\tag{9}
$$

where $\sigma ( s , t )$ denotes the number of shortest paths between nodes s and t, and σ(s, t|v) denotes such paths passing through node v. Removing the nodes in a descending order of betweenness centrality is effective in attacking a scale-free network [27], which can also be used as an immunization strategy. In the experiments, we also compared the infection loss of our algorithm with that of Betweenness immunization.

• DegreeDiscount: DegreeDiscount is a heuristic method proposed by Chen et al. [33]. It was originally designed for in<sup>fl</sup>uence maximization problems. The general idea is that once u is selected as the diffusion seed node, when considering u's neighbor v as seed node, we should not count on the edge vu towards the degree of v, just like a discount on the degree of v. This method can be viewed as an improvement of Target immunization. We simply made a discount on the degree if the neighborhood is immunized. Denote dd(v) as the discounted degree of node v, and N(v) as the set of v's neighbors, then dd(v) can be calculated according to Eq. (10). This forms a new heuristic strategy by immunizing the nodes in the descending order of dd(v).

$$
d d (v) = d e g (v) - | N (v) \cap \mathcal {S} |\tag{10}
$$

• Acquaintance immunization: Acquaintance immunization is a random strategy where a proportion of nodes is randomly picked and a random neighbor of each picked node is immunized [18].

The evaluation metric for comparison of various strategies is the optimization goal as set in Eq. (1), where the immunization cost can be regarded as a constant approaching the budget ω. Thus only the expected infection loss is compared.

## 5.3. Experiment results with the homogeneous case

Infection usually occurs in a random process. Thus, determining infection probability is not an easy task. As a matter of fact, estimation of infection probability has been extensively discussed in the literature [43–45]. It can be in<sup>fl</sup>uenced by various factors such as the history of interaction between nodes, the network structure, the pro<sup>fi</sup>les of the nodes, etc. Our proposed algorithm is applicable in any settings of infection probability because the probability would not in<sup>fl</sup>uence the procedures in deriving the immunization set. For the sake of better comparisons, we <sup>fi</sup>rstly set a uniform infection probability $p = 0 . 0 5$ for each network dataset. As indicated in [33], p cannot be set too large $( \mathrm { e . g . , } p > 0 . 1 )$ , otherwise the network is insensitive to any strategies because most of the nodes in the network would become infected in this setting. To generalize the experiment settings, we also conducted experiments with other infection probability settings $p \in ( 0 . 0 3 , 0 . 0 8 ] .$

We then performed independent cascade simulations on the networks with the immunization sets generated from the different strategies. We randomly picked 10 nodes to get them initially infected. The simulations were ran 10,000 times to derive the expected infection loss with respect to different immunization sets.

The results with the homogeneous case are displayed in Fig. 5. To make it clearer and comparable, we calculate the proportion of reduced infection loss in comparison with the non-immunized situation. Thus, the curves in the upper represent the performance of the better immunization strategies. It can be easily seen that the proposed Algorithm CEIT outperformed other strategies in all of the network datasets.

![](/api/attachments/75KV72SY/fulltext/images/98191ce5e9298a31204ab90f2f0caa91629e2aea698ca1cc5ed1f543c3b1485a.jpg)

GDMB  
![](/api/attachments/75KV72SY/fulltext/images/d0ce09fec3785d13bf1fe2bd210206ac3b577bdfadc3fa999b03f7c09e6257eb.jpg)  
Fig. 5. Experiment results with the homogeneous case.

![](/api/attachments/75KV72SY/fulltext/images/baa7bd34ac1eeb0701a932def6d6a906f653768ed15588d2c5491b5f2cfe3a2c.jpg)

Acquaintance immunization performed badly as a baseline strategy. Strategies of Betweenness, Target and DegreeDiscount were better, but had different performances on different networks, and were still signi<sup>fi</sup>cantly worse than CEIT. In general, CEIT reduced the infection loss by 5%–10% compared to the others.

Furthermore, additional experiments were conducted with $p \in ( 0 . 0 3 , 0 . 0 8 ]$ . The general patterns of the reduced infection loss under different probability settings are the same with the case of $p =$ 0.05. Take the EUMail network as an example, we <sup>fi</sup>xed the number of immunization targets $k = 6 0$ to run diffusion simulations, and calculated the expected reduced infection loss for different infection probability values. Fig. 6 demonstrates the results that CEIT performed best in different probability settings.

Note that when immunizing just a few nodes, such as 10 or fewer, the chosen targets are likely to be the nodes with high connectivity, e.g., nodes with high degree of betweenness. It has been proved in [46] that the network would be decomposed into small pieces if highly connective nodes would be attacked, because they are responsible for most connections and connect several communities. Therefore, immunizing theses nodes would contribute greatly to reducing the infection loss, and we see a similar performance in all of the methods when the immunization size is small. However, when the immunization size increases, our proposed approach has signi<sup>fi</sup>cantly better performance than the other heuristic immunization strategies. This is because methods such as Target and Betweenness consider only static network structure, they cannot differentiate nodes with similar connectivity. In contrast, CEIT chooses immunization targets by dynamically calculating each node's contribution in reducing the expected infection loss of other nodes.

![](/api/attachments/75KV72SY/fulltext/images/3921d8fdfcf702b36b538171aa61b273b17d79770a1cc8b60f0ecd4a3217d3b9.jpg)  
Fig. 6. Infection loss with different probability settings for .

As shown in the experimental results, the reduced expected infection loss increases with more immunization resources invested. However, the marginal reduced infection loss decreases with the increase of immunization budget. If the budget continues to increase, the savability of the newly added immunization candidate k can <sup>fi</sup>nally decrease to lower than one, meaning that the marginal cost surpasses the marginal bene<sup>fi</sup>t from investing in immunization, i.e., $\textstyle \sum _ { i \in { \mathcal { A } } ( k ) } { \mathcal { L } } _ { i } > c ( k )$ . To avoid <sup>Að Þ L ð Þ</sup>such inef<sup>fi</sup>cient and redundant immunization, we have to add one stopping rule in the algorithm, i.e., when the savability of all of the immunization candidates is lower than one, the algorithm should stop and return the immunization set. In this way, the optimization goal set in Eq. (1) can be guaranteed even if the budget is enough to immunize all of the nodes in the network. As a matter of fact, companies have limited immunization budget in most cases, and savability of the newly added immunization target is usually greater than one. Thus, the entire budget should be invested in immunization to achieve the minimal value of the optimization goal, $\operatorname { i . e . , } c ( S ) \equiv \omega .$

## 5.4. Results with the heterogeneous case

Immunization strategies can be different under the heterogeneous cost case as discussed in previous sections. In this subsection we conduct experiments with the cost functions proposed in Section 3.3. As for the two types of cost associated with information assurance, we treated the network datasets differently in terms of the cost and loss in reality.

## 5.4.1. Heterogeneous immunization cost

Immunization for the blog reading network GDMB is referred to supervision and control of the information on the blogs in practice. The blog system administrators have to make efforts to read articles of some blogs in order to monitor and handle the information spread of concern in the network. This can be regarded as immunization cost because it consumes labor force in reading blogs. Therefore, it is reasonable to assume that the immunization cost is related to the number of articles in a blog. The average number of blog articles of all users was 174.96, and the maximal was 16,976. According to the function in Eq. (2), we let the argument ψ(·) be the number of articles, and set $\alpha = 1 0 , \beta = 0 . 0 0 0 3$ . The infection loss for each node remains constant at ${ \mathcal { L } } = 1$ in this experiment.

For the CCMP dataset, we assumed that the immunization cost of each node was correlated with degree, $\mathfrak { i . e . , } \psi ( k ) = d e g ( k )$ . Let α = 30 and $\beta = 0 . 0 0 5$ , then immunizing a node with high connectivity was supposed to incur a cost of nearly 30, while the cost vary over different node degrees in a moderate scale. Likewise, the loss for each infected node also remains constant at ${ \mathcal { L } } = 1 .$

Fig. 7(a) displays the total infection loss with a bunch of immunization budgets ω on both GDMB and CCMP through diffusion simulations. Similar to the homogeneous case, Algorithm CEIT outperformed the other immunization strategies in the heterogeneous cost settings. Within a certain amount of immunization budget, like ω = 300 in GDMB, the reduced infection loss from CEIT exceeded Target by 12%, while Betweenness was 18% lower. Results are similar for CCMP, in which Target (5–10% lower) and Betweenness (10–15% lower) could not compete with CEIT.

Generally speaking, in the heterogeneous cost case, the size of immunization set determined by CEIT is always larger than that in Target immunization and some other network structure based strategies, because it preferred those ‘cheap’ but highly rewarding nodes. It searched for the immunization targets in a most cost-effective way, i.e., to ‘save more nodes with limited immunization budgets. Therefore, the nodes with moderate immunization cost but also playing indispensable roles in saving other nodes are more likely to be chosen by Target. Take the example in Fig. 4, where node 6 is not comparable in degree with nodes 1 and 8, and the calculated savability under the homogeneous cost case is not as great as node 8 either; however, CEIT would prefer such nodes because its savability under the heterogeneous immunization cost is the largest.

(a) Results of heterogeneous Results of heterogeneousGDMB  
![](/api/attachments/75KV72SY/fulltext/images/6ff67ff65751866396e320945874124a7550711615da70c122601f5fca6e718f.jpg)

(b) Results of heterogeneous Results of heterogeneoCCMP  
![](/api/attachments/75KV72SY/fulltext/images/89de7cdf2c480e2467088236187a9436261581d25f27818f6366a443b4316e7a.jpg)  
Fig. 7. Experiment results of heterogeneous case.

## 5.4.2. Heterogeneous infection loss

When an email address is infected by worms, breaches or some malicious information, losses may emerge from losing information or receiving fake information. Since different email accounts possess distinct importance in the network, the infection loss should also be related to their importance. For the EUmail network, we assumed that the infection loss of a node is related to its degree, i.e., the number of email accounts it has connections with. Let $\alpha ^ { \prime } = 1 0$ and $\beta ^ { \prime } = 0 . 1 5$ and we can implement CEIT to derive the immunization set. We then ran diffusion simulations on the network and calculated the expected infection loss according to the loss function. Fig. 8 depicts the results with respect to different immunization strategies under heterogeneous infection loss.

We can see from Fig. 8 that CEIT performed best among all the immunization strategies with heterogeneous infection loss. When the number of immunization targets reached 50 $( \mathrm { i } . \mathbf { e } . , k = 5 0 ) ,$ , the proposed algorithm CEIT could achieve a reduction in infection loss by 5% more than Betweenness, and 10% more than Target and DegreeDiscount.

## 5.5. Discussion on the results

As reported in the experimental results, CEIT achieved the highest reduction in infection loss under different cost settings. Compared with the baseline methods, CEIT possesses the following characteristics by introducing the concept savability. First, the evaluation of savability depends on dynamic diffusion process. The nodes with high connectivity but do not play important roles in preventing diffusion would not enjoy high savability. Second, savability incorporates both immunization cost and infection loss, formulated as the return on security investment, thus the chosen immunization targets are with cost-ef<sup>fi</sup>ciency consideration. Third, an improved voting mechanism enables everyone to speak for the ones that can ‘save’ him. Thus, only the nodes that are concerned with overall interest (not limited to local interest) would get high savability and be chosen by CEIT.

Moreover, the proposed approach has applied the bond percolation process to devise the procedure eProbEstimation. Thus, the time of estimating the expected infection probability is reduced. The computation time of estimating the expected infection probability of nodes in a single iteration was tested for the three datasets. The time of the repeated simulations for the three datasets all surpassed 20 s (CCMP: 21.75 s, GDMB: 21.75 s, EUMail: 87.51 s). The proposed eProbEstimation greatly lowers the computation time for calculating the expected infection probability, with the computation time remaining at a level of 1 s (CCMP: 0.94 s, GDMB: 1.29 s, EUMail: 0.68 s).

![](/api/attachments/75KV72SY/fulltext/images/03c0ff584b6bdbf9071e7e45d244be8e269ea57726ff26d48a18a30f247b566b.jpg)  
Fig. 8. Experiments of heterogeneous infection loss for EUmail.

The overall computation time for the network in the experiments was at the level of $1 0 ^ { 4 } \ : s$ s, while the time required by Betweenness is at $1 0 ^ { 3 }$ second-level and the other immunization methods remained at a level of around $1 0 ^ { 1 } s$ . Though we see that, from the experiments, the proposed algorithm took more time than did the other immunization strategies, it is still worthwhile due to signi<sup>fi</sup>cant advantages of the proposed algorithm in pursuit of immunization targets at near optimal solutions as discussed in Section $4 . 6 ,$ with both cost and loss considered. Meanwhile, the immunization problem discussed in this paper is meant to be pre-immunization. That is, IT/IS management needs to take certain protective measures before real attacks occur, in order to mitigate potential risks. For example, they install anti-virus software/ <sup>fi</sup>rewalls on some computers, or else they need to regularly patch some important machines. These protective tasks can be regulated as periodic/routine tasks which do not require online/real-time computation. Thus, given the network structure and immunization budget, the algorithm could return the cost-effective immunization set in a limited time frame for practical applications.

## 6. Case study

In this section, we applied CEIT to an actual information assurance practice as case study. A Chinese educational institution uses email systems as the most important communication channel. The IT/IS of<sup>fi</sup>ce of the institution is responsible for the administration of the email server and the information assurance for the email network. Their daily work includes monitoring email traf<sup>fi</sup>c, detecting spams, and also reminding the users of potential viruses, worms, etc. In this study, these protection activities can all be viewed as immunization strategies. However, the IT/IS of<sup>fi</sup>ce could only afford limited labor force to monitor and immunize a part of the email accounts in an ad hoc manner. Thus, which accounts to immunize becomes a problem that the of<sup>fi</sup>ce has to encounter in its daily work.

To apply the proposed CEIT in the real email networks, we should <sup>fi</sup>rstly know about the network structure of information <sup>fl</sup>ow in the email systems, as well as the importance of each email account in terms of cost and potential infection loss. and finally the budget for the immunization resources. The available email logs within a time span of one month (i.e., September, 2012) provide the necessary information needed for implementing CEIT. The email accounts were anonymized with random numbers for privacy concerns. Each account in the email logs is regarded as a node, and the communication between any two accounts is regarded as an edge, which comprise an information network. For the sake of clarity, only the largest strongly connected component and the bi-directional edges in the network are retained. As a result, the network is composed of 3325 nodes and 17,637 edges. Except for the network, the detailed email logs of the research institute also provides us with the communication frequencies for all pairs of nodes. We added together the communication frequency as the weight for each edge. Thus, we assume that the infection probability is correlated with the weight because the communication frequency can be interpreted as tie strength of the edge. Speci<sup>fi</sup>cally, the infection probability on the edge vw can be calculated with a function $p _ { { \nu } , w } = 1 \_ 0 . 9 9$ $\mathrm { e } ^ { - 0 . \overset { \cdot } { 0 } 1 * f _ { v , w } }$ , where $f _ { v , w }$ denotes the communication frequency between nodes v and w. The importance of a node can be measured by the total communication frequency with all of its neighbors, i.e., $\psi ( s ) = { }$ $\sum w \in N ( \nu ) { f _ { \nu , w } } ,$ and the infection loss of the node can then be calculated according to Eq. (2) with $\alpha ^ { \prime } = 1 0$ and $\beta ^ { \prime } = 0 . 0 0 8$

With the above settings, we can derive the immunization set by implementing CEIT. Diffusion simulations were executed for multiple times to validate the ef<sup>fi</sup>ciency of the immunization targets. The performance was also compared with other strategies on the measure of proportion of reduced infection loss. Fig. 9 demonstrates the results, from which we can easily see that CEIT signi<sup>fi</sup>cantly reduced more infection loss than the others.

![](/api/attachments/75KV72SY/fulltext/images/0be36ccf261208b03044baa89d766f3c66ff33a087937f0db55692ec6c73ff93.jpg)  
Fig. 9. Simulation results on infection loss for the school's email network.

We then proceeded to investigate the network structure of the email network and visualize the immunization targets in the network. To make the network structure more readable, we partitioned the network into several communities, and painted the nodes in a same community with the same color. Meanwhile, the layout of nodes was also related to the community structure, where the nodes in the same community were displayed in a shorter distance. The network structure is displayed in Fig. 10, and then we enlarged the immunized nodes $( k = 5 0 )$ ) and painted them with different colors for different strategies respectively. The big yellow and green nodes were the targets chosen by the pro posed approach CEIT. We discovered that most of these nodes did not have high degrees, but they usually connected the nodes with high potential loss in different communities. For example, the node labeled 2499 in fact represents an institute leader's email account. Although it was not with many connections, it interacted frequently with different communities such as faculty and staff. Similarly, node 2228 is the account of the chief director of the institution's teaching of<sup>fi</sup>ce, which connects the faculties' and students' communities. Node 1126 represents the director of the IT/IS of<sup>fi</sup>ce, who is responsible for coping with IT issues of all the members in the institute. In general, the potential reduced infection loss for immunizing such nodes would be high because they connect different communities. However, the big red nodes are the only immunization targets that are chosen by Target due to their high degrees of connections. Notably, some of them lie in the same community such as nodes 1739, 2999, and others near them. Because they are tightly connected to each other, once one is immunized, the probability for others being infected would be low, resulting in low immunization ef<sup>fi</sup>ciency. Another example is node 404, which represents the account of the alumni of<sup>fi</sup>ce. It sent out emails to thousands of alumni every week. However, this node was not chosen by CEIT because of its inef<sup>fi</sup>- ciency in saving nodes with potential high infection loss. To sum up, those members playing multi-roles and communicating frequently with important information units should be the major immunization targets in the investigation.

![](/api/attachments/75KV72SY/fulltext/images/d775b6cd95cb93e63f8c2c8fd6ae18cb9c6b8a998aa7bfcae0e32f0561ed71ea.jpg)  
Fig. 10. Network structure of the email network. Zoom in to see the connections of the node 2499

## 7. Conclusions

This paper has formulated the information assurance problem as a cost-effective immunization problem, which minimizes the total expected infection loss by immunizing a few nodes with a limited budget. Different from existing efforts, the proposed approach has taken the network structure and dynamic diffusion process, along with cost analysis into consideration. Moreover, a new concept, namely, savability, has been introduced and used as the evaluation function in the greedy method to generate the cost-effective immunization targets. It has been further proven that the obtained immunization set guarantees approximating the optimal solutions with a de<sup>fi</sup>nite lower bound.

With social media permeating every aspect of companies such as communication and marketing, they are now positioned in connected networks with employees, customers, etc., rather than isolated physical networks. Thus, they are faced with more information assurance incidents emerging from these networks. The proposed approach has aimed at helping organization managers make better decisions with respect to the allocation of the immunization budget within the information network. Security practitioners may use the proposed CEIT algorithm to position the cost-effective immunization targets to reduce the potential information assurance risks. In addition, different forms of cost and loss have been considered; therefore practitioners could apply various cost and loss functions to better <sup>fi</sup>t the real situations in their own organizations.

The work could be extended in the following ways in the future. Firstly, more data details such as the interaction logs of any two nodes, the nodes' statuses, and the nodes' pro<sup>fi</sup>les could be exploited to depict the information diffusion paths in the network. Secondly, we can further investigate the estimation of infection probabilities to capture the infection process in a more precise way. Additionally, the proposed approach can be employed to identify the most costeffective seeds, or opinion leaders in launching marketing campaigns in social networks by setting the objective function as maximizing revenues of marketing.

## Acknowledgments

The work was partly supported by the MOE Project of Key Research Institute of Humanities and Social Sciences at Universities (12JJD630001), the National Natural Science Foundation of China (71110107027, 71402186), and the Tsinghua University Initiative Scienti<sup>fi</sup>c Research Program (20101081741).

## Appendix A. Proof of submodularity for Sa(·)

To prove the submodularity for the function $S a ( \cdot ) ,$ , we <sup>fi</sup>rstly prove the following lemma.

$$
\text { Lemma   1. } \operatorname * {P r} _ {i} (\mathcal {T}) - \operatorname * {P r} _ {i} (\mathcal {T} \cup k) \leq \operatorname * {P r} _ {i} (\mathcal {S}) - \operatorname * {P r} _ {i} (\mathcal {S} \cup k), \text { if } \mathcal {S} \subset \mathcal {T}.
$$

Proof. Given two immunization sets $s \subset \tau$ , and let $\mathcal { R } = \mathcal { T } \backslash { S } .$ . Assume <sup>S T R ¼ T S</sup>that the original network has been percolated, i.e., we are left with a diffusion network $G _ { p }$ with each edge activated by infection probability $p .$ Then we <sup>fi</sup>rstly immunize nodes in by removing the nodes in from $G _ { p } .$ <sup>S S</sup>. The network is then decomposed into several disjointed connected components, $G _ { p } \backslash S = \cup C C _ { i }$ . Thus according to Eq. (4), $\operatorname* { P r } _ { i } ( S ) =$ $| c c ( i ; G _ { p } \backslash S ) | / | V | .$ <sup>S ¼ ð Þ ¼S</sup>. Then we continue to immunize node k, there are two <sup>j S j j</sup>cases for node k.

• If k has no path to $c c ( i ; G _ { p } \backslash S )$ , removing k would have no in<sup>fl</sup>uence on <sup>S</sup>the probability of node i being infected. In this situation, $\mathrm { P r } _ { i } ( S ) - \mathrm { P r } _ { i }$ $( S \cup k ) = 0 ,$ , and obviously $\operatorname* { P r } _ { i } ( \mathcal { T } ) - \operatorname* { P r } _ { i } ( \mathcal { T } \cup k ) = 0$ since $s \subset \tau$

<sup>ð Þ ¼S</sup>• If k has path to $c c ( i ; G _ { p } \backslash S )$ <sup>ð ÞT ð Þ ¼T S T</sup>, removing k would lower the probability of node i being infected. By removing $k ,$ some nodes' paths towards i are cut off, making xtiti lie in a new component $c c \big ( i ; G _ { p } \backslash ( S \cup k ) \big )$ , and <sup>ð ÞS</sup>the nodes being cut off the paths towards i are in the set $U =$ $( c c ( i ; G _ { p } \backslash S ) \backslash c c ( i ; G _ { p } \backslash ( S \backslash k ) )$ . Therefore the lowered probability is $\mathrm { P r } _ { i }$ $( S ) - \operatorname* { P r } _ { i } ( S \cup k ) = \lvert U \rvert / \lvert V \rvert$ <sup>Þ</sup>. Next we immunize nodes in R to obtain $\mathrm { P r } _ { i }$ $( { \mathcal { T } } ) { \mathrm { - } } \operatorname* { P r } _ { i } ( { \mathcal { T } } \cup k ) .$ <sup>¼j j j j</sup>, again there are two sub cases for the nodes in R. For any $r \in R ,$ if $r { \in } c c ( i ; G _ { p } { \backslash } ( S \cup k ) )$ , removing r would not change the nodes in U. Thus $\begin{array} { r } { \dot { \mathsf { P r } } _ { i } ( { \mathcal { S } } \cup r ) - \operatorname* { P r } _ { i } ( ( { \mathcal { S } } \cup r ) \cup k ) = \operatorname* { P r } _ { i } ( { \mathcal { S } } ) - \operatorname* { P r } _ { i } ( { \mathcal { S } } \cup k ) = } \end{array}$ $| U | / | V |$ . While for $r \in U ,$ <sup>ð ÞS ð Þ ¼ð ÞS ð ÞS ð Þ ¼S</sup>, removing it would result in a smaller set of <sup>j j j j</sup>nodes in U, i.e., removing r would cut off the paths of some nodes towards i, meaning that these nodes would not infect i, which makes the marginal bene<sup>fi</sup>t of immunizing k smaller. Thus, $\operatorname* { P r } _ { i } ( S \cup r ) -$ $\operatorname* { P r } _ { i } ( ( { \mathcal { S } } \cup r ) \cup k ) { \mathrm { < P r } } _ { i } ( { \mathcal { S } } ) - \operatorname* { P r } _ { i } ( { \mathcal { S } } \cup k )$ <sup>ð ÞS</sup>in this case. Then to sum up, for any $r \in R , \mathrm { P r } _ { i } ( S \cup r ) - \mathrm { P r } _ { i } ( ( S \cup r ) \cup k ) \le \mathrm { P r } _ { i } ( S ) - \mathrm { P r } _ { i } ( S \cup k )$ . Thus, $\operatorname* { P r } _ { i } ( \mathcal { T } ) -$ $\operatorname* { P r } _ { i } ( { \mathcal { T } } \cup k ) \leq \operatorname* { P r } _ { i } ( S ) - \operatorname* { P r } _ { i } ( S \cup k )$

Therefore, in both situations for $k ,$ we have $\operatorname* { P r } _ { i } ( \mathcal { T } ) - \operatorname* { P r } _ { i } ( \mathcal { T } \cup k ) \leq$ $\operatorname* { P r } _ { i } ( { \mathcal { S } } ) - \operatorname* { P r } _ { i } ( { \mathcal { S } } \cup k ) , { \mathrm { i f ~ } } { \mathcal { S } } \subset T .$

<sup>ð ÞS ð ÞS S T</sup>We use a <sup>fi</sup>gure to better illustrate this lemma. As shown in Fig. A.11, the nodes in the set have already been immunized and i is left in the <sup>S</sup>connected component. If node k is then immunized, the nodes on its left (nodes 5, 7, 8, 9 and r ) just form the set U, contributing to the marginal bene<sup>fi</sup>t of immunizing k; while i stays in the new connected component (nodes $1 – 4 , 6 , 1 0 , k , r _ { 1 } )$ . If extitr has path to $k ,$ such as node $r _ { 1 } , \mathrm { i t }$ has no in<sup>fl</sup>uence on U. Thus the marginal bene<sup>fi</sup>t of immunizing k remains the same. However, if r has path to any nodes in U, as $r _ { 2 } ,$ , nodes 8 and 9 are then blocked to infect i. Therefore immunizing r decreases the marginal bene<sup>fi</sup>t of immunizing k.

Proof of Theorem 1. To prove that $S a ( \cdot )$ is submodular, we should prove that $S a ( S \cup k ) { - } S a ( S ) { \geq } S a ( T \cup k ) { - } S a ( T )$ , if $s \subset \tau$ . According <sup>ð ÞS ð ÞS ð ÞT ð ÞT S T</sup>to the de<sup>fi</sup>nition of the function Sa(·), the marginal savability by immunizing k with already immunized is $S a ( S ) { - } S a ( S \cup k ) = $ <sup>S ð ÞS∑i∈V5 ;i≠k</sup> <sup>Li</sup> <sup>Pri</sup>ð Þ S <sup>−Pr</sup> ð Þ <sup>i</sup>ð Þ S<sup>∪k</sup> . As has been shown in Lemma 1, C $\operatorname* { P r } _ { i } ( \mathcal { T } ) -$ $\operatorname* { P r } _ { i } ( { \mathcal { T } } \cup k ) { \overset { \underset {  } { } } { \leq } } \operatorname* { P r } _ { i } ( S ) - \operatorname* { P r } _ { i } ( S \cup k )$ , so we have $\begin{array} { r l } { \sum _ { i \in V \setminus S , i \ne k } L _ { i } ( \operatorname { P r } _ { i } ( S ) - } & { { } } \end{array}$ $\begin{array} { r } { \operatorname* { P r } _ { i } ( \operatorname { S U } k ) ) { \geq } \sum _ { i \in V \backslash T , i \neq k } L _ { i } ( \operatorname* { P r } _ { i } ( { T } ) - \operatorname* { P r } _ { i } ( { T } \cup k ) ) } \end{array}$ . Therefore, $S a ( S \cup k ) -$ $S a ( S ) { \geq } S a ( \mathcal { T } \cup k ) { - } S a ( \mathcal { T } )$

![](/api/attachments/75KV72SY/fulltext/images/21d4faf5928f2ab29bb89b9ff395038d9c1164373aee0665622b8a9b40ad351d.jpg)  
Fig. A.11. Example illustrates the proof of Lemma 1.

## References

[1] S. Wu, J.M. Hofman, W.A. Mason, D.J. Watts, Who says what to whom on Twitter, Proceedings of the 20th International Conference on World Wide Web, WWW '11, ACM, New York, NY, USA, 2011, pp. 705–714.

[2] Y.-M. Li, Y.-L. Shiu, A diffusion mechanism for social advertising over microblogs, Decision Support Systems 54 (1) (2012) 9–22.

[3] C. Budak, D. Agrawal, A. El Abbadi, Limiting the spread of misinformation in social networks, Proceedings of the 20th International Conference on World Wide Web, WWW '11, ACM, New York, NY, USA, 2011, pp. 665–674.

[4] M. Kimura, K. Saito, R. Nakano, Extracting in<sup>fl</sup>uential nodes for information diffusion on a social network, Proceedings of the National Conference on Arti<sup>fi</sup>cial Intelligence, vol. 22, 2007, p. 1371.

[5] D. Trpevski, W.K.S. Tang, L. Kocarev, Model for rumor spreading over networks, Physical Review E 81 (2010) 056102.

[6] L.A. Gordon, M.P. Loeb, L. Zhou, The impact of information security breaches: has there been a downward shift in costs? Journal of Computer Security 19 (2011) 33–56.

[7] PwC, Information security breaches survey, Tech. Rep. PwC, 2012.

[8] T. August, T. Tunca, Who should be responsible for software security? A comparative analysis of liability policies in network environments, Management Science 57 (5) (2011) 934–959.

[9] ICSA Labs., ICSA Labs 9th annual computer virus prevalence survey, Tech. Rep. ICSA Labs, 2004, (URL http://www.icsalabs.com/).

[10] P. Donovan, How idle is idle talk? One hundred years of rumor research, Diogenes 54 (1) (2007) 59–82.

[11] S. Chai, M. Kim, H.R. Rao, Firms' information security investment decisions: stock market evidence of investors' behavior, Decision Support Systems 50 (4) (2011) 651–661.

[12] W.H. Baker, L.P. Rees, P.S. Tippett, Necessary measures: metric-driven information security risk assessment and decision making, Communications of the ACM 50 (10) (2007) 101–106.

[13] W. Sonnenreich, J. Albanese, B. Stout, Return on security investment (ROSI)—a practical quantitative model, Journal of Research and Practice in Information Technology 38 (1) (2006) 45–56.

[14] R. Anderson, T. Moore, The economics of information security, Science 314 (5799) (2006) 610–613.

[15] L.A. Gordon, M.P. Loeb, The economics of information security investment, ACM Transactions on Information and System Security 5 (4) (2002) 438–457, http://dx. doi.org/10.1145/581271.581274.

[16] Y.J. Lee, R.J. Kauffman, R. Sougstad, Pro<sup>fi</sup>t-maximizing <sup>fi</sup>rm investments in customer information security, Decision Support Systems 51 (4) (2011) 904–920

[17] R. Pastor-Satorras, A. Vespignani, Immunization of complex networks, Physical Review E 65 (3) (2002) 036104.

[18] R. Cohen, S. Havlin, D. Ben-Avraham, Ef<sup>fi</sup>cient immunization strategies for computer networks and populations, Physical Review Letters 91 (2003) 247901.

[19] L.K. Gallos, F. Liljeros, P. Argyrakis, A. Bunde, S. Havlin, Improving immunization strategies, Physical Review E 75 (2007) 045104.

[20] H. Tong, B. Prakash, C. Tsourakakis, T. Eliassi-Rad, C. Faloutsos, D. Chau, On the vulnerability of large graphs, 2010 IEEE 10th Int. Conf. on Data Mining (ICDM), 2010.pp.1091-1096

[21] H. Yuan, G. Chen, J. Wu, H. Xiong, Towards controlling virus propagation in information systems with point-to-group information sharing, Decision Support Systems 48 (1) (2009) 57–68.

[22] C.C. Zou, W. Gong, D. Towsley, Code red worm propagation modeling and analysis, Proceedings of the 9th ACM Conference on Computer and Communications Security, CCS '02, ACM, New York, NY, USA, 2002, pp. 138–147.

[23] M.E.J. Newman, Spread of epidemic disease on networks, Physical Review E 66 (2002) 016128.

[24] Y. Moreno, M. Nekovee, A.F. Pacheco, Dynamics of rumor spreading in complex networks, Physical Review E 69 (2004) 066130.

[25] H. Yuan, G. Liu, G. Chen, On modeling the crowding and psychological effects in network-virus prevalence with nonlinear epidemic model, Applied Mathematics and Computation 219 (5) (2012) 2387–2397.

[26] Z. Dezső, A.-L. Barabási, Halting viruses in scale-free networks, Physical Review E 65 (2002) 055103.

[27] P. Holme, B.J. Kim, C.N. Yoon, S.K. Han, Attack vulnerability of complex networks, Physical Review E 65 (2002) 056109.

[28] Y. Chen, G. Paul, S. Havlin, F. Liljeros, H.E. Stanley, Finding a better immunization strategy, Physical Review Letters 101 (2008) 058701.

[29] A. Kleczkowski, K. Oles, E. Gudowska-Nowak, C.a. Gilligan, Searching for the most cost-effective strategy for controlling epidemics spreading on regular and smallworld networks, J. R. Soc. Interface (2011).

[30] M. Richardson, P. Domingos, Mining Knowledge-sharing Sites for Viral Marketing, KDD '02, ACM, New York, NY, USA, 2002. 61–70.

[31] D. Kempe, J. Kleinberg, E. Tardos, Maximizing the Spread of In<sup>fl</sup>uence Through a Social Network, KDD '03, ACM, New York, NY, USA, 2003. 137–146.

[32] J. Leskovec, A. Krause, C. Guestrin, C. Faloutsos, J. VanBriesen, N. Glance, Costeffective Outbreak Detection in Networks, KDD '07, ACM, New York, NY, USA, 2007.420-429

[33] W. Chen, Y. Wang, S. Yang, Ef<sup>fi</sup>cient In<sup>fl</sup>uence Maximization in Social Networks, KDD '09 ACM New York NY USA 2009. 199–208

[34] J. Kephart, S. White, D. Chess, Computers and epidemiology, IEEE Spectrum 30 (5) (1993) 20–26.

[35] M. Kimura, K. Saito, H. Motoda, Blocking links to minimize contamination spread in a social network, ACM Transactions on Knowledge Discovery Data 3 (2) (2009) 9: 1–9:23.

[36] M.L. Brandeau, G.S. Zaric, A. Richter, Resource allocation for control of infectious diseases in multiple independent populations: beyond cost-effectiveness analysis, Journal of Health Economics 22 (4) (2003) 575–598.

[37] C. Ioannidis, D. Pym, J. Williams, Investments and trade-offs in the economics of information security, 5628 (2009) 148–166

[38] D.N. Marco Cremonini, Understanding and in<sup>fl</sup>uencing attackers' decisions: implications for security investment strategies, Proc. of the 5th Annual Workshop on Economics and Information Security, WEIS, Cambridge, UK, 2006.

[39] G.L. Nemhauser, L.A. Wolsey, M.L. Fisher, An analysis of approximations for maximizing submodular set functions—I, Mathematical Programming 14 (1) (1978) 265–294.

[40] S. Khuller, A. Moss, J.S. Naor, The budgeted maximum coverage problem, Information Processing Letters 70 (1) (1999) 39–45.

[41] J. Leskovec, J. Kleinberg, C. Faloutsos, Graph evolution: densi<sup>fi</sup>cation and shrinking diameters, ACM Transactions on Knowledge Discovery from Data 1 (1) (2007) 2.

[42] L. Freeman, A set of measures of centrality based on betweenness, Sociometry (1977) 35–41.

[43] A. Goval E. Bonchi L.V. Lakshmanan Learning influence probabilities in social networks, Proceedings of the Third ACM International Conference on Web Search and Data Mining, ACM, 2010, pp. 241–250.

[44] K. Saito, R. Nakano, M. Kimura, Prediction of information diffusion probabilities for independent cascade model, Knowledge-based Intelligent Information and Engineering Systems, Springer, 2008, pp. 67–75.

[45] X. Fang, P.J.-H. Hu, Z.L. Li, W. Tsai, Predicting adoption probabilities in social networks, Information Systems Research 24 (1) (2013) 128–145.

[46] R. Albert, H. Jeong, A.-L. Barabási, Error and attack tolerance of complex networks Nature 406 (6794) (2000) 378–382

Guannan Liu is currently a Ph.D. candidate in management science and engineering at the School of Economics and Management, Tsinghua University, Beijing, China. His research interests include data mining, social networks and business intelligence. His work has been published in the journals such as Applied Mathematics and Computation, Neurocomputing.

Jin Zhang is an Assistant Professor in the School of Business, Renmin University of China. He received his Ph.D. degree in management science and engineering from the School of Economics and Management, Tsinghua University, Beijing, China, in 2013. His current research interests include data mining and business intelligence, web search, and soft computing. His work has been published in journals such as IEEE Transactions on Neura Networks, Knowledge-Based Systems, and Science in China

Guoqing Chen received the Ph.D. degree in managerial informatics from the Catholic University of Leuven, Leuven, Belgium, in 1992. He is currently a professor on information systems with the School of Economics and Management, Tsinghua University, Beijing, China. His current research interests include data mining and business intelligence, e-business, and fuzzy logic. His work has been published in journals such as Decision Support Systems, Information Sciences, IEEE Transactions on Fuzzy Systems, Fuzzy Sets and Systems, IEEE Intelligent Systems, and Communications of the ACM.

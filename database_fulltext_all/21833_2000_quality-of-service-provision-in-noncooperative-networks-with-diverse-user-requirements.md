---
otero_id: 21833
otero_key: "M4QRM2SK"
title: "Quality of service provision in noncooperative networks with diverse user requirements"
authors: "K. Park; M. Sitharam; S. Chen"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00078-0"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Quality of service provision in noncooperative networks with diverse user requirements

K. Park <sup>a,),1</sup>, M. Sitharam <sup>b,2</sup>, S. Chen <sup>a,3</sup>

Department of Computer Sciences, Purdue UniÕersity, West Lafayette, IN 47907, USA

<sup>b</sup> Department of Computer and Information Science and Engineering, UniÕersity of Florida, GainesÕille, FL 32611, USA

## Abstract

This paper studies the quality of service QoS provision problem in noncooperative networks where applications or usersŽ . are selfish and routers implement generalized processor sharing based packet scheduling. We formulate a model of QoS provision in noncooperative networks where users are given the freedom to choose both the service classes and traffic volume allocated, and heterogenous QoS preferences are captured by a user’s utility function. We present a comprehensive analysis of the noncooperative multi-class QoS provision game, giving a complete characterization of Nash equilibria and their existence criteria, and show under what conditions they are Pareto- and system-optimal. We show that, in general, Nash equilibria need not exist, and when they do exist, they need not be Pareto- nor system-optimal. For certain ‘‘resource-plentiful’’ systems, however, we show that the world indeed can be nice with Nash equilibria, Pareto optima, and system optima collapsing into a single class. We study the problem of facilitating effective QoS in systems with multi-dimensional QoS vectors containing both mean- and burstiness-related QoS measures. We extend the game-theoretic analysis to multi-dimensional QoS vector games and show under what conditions the aforementioned results carry over. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: Quality of service; Multi-class QoS provision; Noncooperative network game; Heterogeneous user requirements

## 1. Introduction

## 1.1. Background

With the increased deployment of high-speed local- and wide-area networks carrying a multitude of information from e-mail to bulk data to voice, audio, and video, provisioning adequate quality of service Ž . QoS to the diverse application base has become an important problem 3,13,27,33 . This paper describes<sup>w</sup> <sup>x</sup> a QoS provision architecture suited for best-effort environments, based on ideas from microeconomics and noncooperative game theory.

We construct a noncooperative multi-class QoS provision model where users are assumed to be selfish, and packets are routed over switches where, as a function of their enscribed priority, differentiated service is delivered. The diverse spectrum of application QoS requirements is modeled using utility functions. Users or applications<sup>4</sup> can choose both the service classes and the traffic volumes assigned to them. The interaction of users behaving selfishly in accordance with their QoS preferences leads to a noncooperative game whose dynamic properties we seek to understand.

The traditional approach to QoS provision uses resource reservations along a route to be followed by a traffic stream so that the stream’s data rate and burstiness can be suitably accommodated. Although research abounds 8–10,12,13,18,28,33,35,36 , analytic tools for computing QoS guarantees rely on shaping of input traffic to preserve well-behavedness across switches that implement some form of packet scheduling discipline such as generalized processor sharing GPS , also known as weighted fair queueingŽ . <sup>w</sup> <sup>x</sup> 11,35 . Real-time constraints of multimedia traffic and the scale-invariant burstiness associated with self-similar network traffic 29,37,39,48 limit the<sup>w</sup> <sup>x</sup> shapability of input traffic while at the same time reserving bandwidth that is significantly smaller than the peak transmission rate. Thus, QoS and utilization stand in a trade-off relationship with each other 37<sup>w</sup> <sup>x</sup> and transporting application traffic over reserved channels, in general, incurs a high cost.

This makes it important to organize today’s besteffort bandwidth, as examplified by the Internet, into stratified services with graded QoS properties such that the QoS requirements of a compendium of applications can be effectively met. This is particularly useful for applications that possess diverse but — to varying degrees — flexible QoS requirements. It would be overkill to transport such traffic over reserved channels. On the other hand, relying on homogenous best-effort service, characteristic of today’s Internet, would be equally unsatisfactory. A dual architecture capable of supporting reserved and stratified best-effort service is needed which, in turn, helps amortize the cost of inefficiencies stemming from overprovisioned resources for guaranteed traffic through the filling-in effect 25 .<sup>w</sup> <sup>x</sup>

Recently, microeconomic<sup>r</sup>game-theoretic approaches to resource allocation have received significant interest with application domains spanning a number of different contexts 7,15,16,19,21,24,<sup>w</sup> 26,30,34,38,41,42,45,46 . The overall goal of this<sup>x</sup> area is to formulate a resource allocation problem in the framework of microeconomics and game theory, and show that under certain conditions, the system achieves ‘‘desirable’’ allocations from stabilibity, fairness, and optimality points-of-view. The latter are important in making stratified best-effort bandwidth practically usable by QoS-sensitive applications: predictable service, both in terms of dynamic stability and the rendering of appropriate QoS, are crucial prerequisites to feasibly realizing such an architecture.

The models and approaches proposed in the literature differ along several dimensions, some of the important ones being whether applications or users are assumed to be cooperative or selfish, whether pricing is used or not, and how much computing responsibility is delegated to the user. Several papers have addressed the issue of multi-class QoS provision in high-speed networks 7,22,31,38,41,42 . Some<sup>w</sup> <sup>x</sup> of the works employ a cooperative framework or place significant computing responsibilities on the part of the user 31,41 , some investigate the effect of pricing incentives 7 , and others represent <sup>w</sup> <sup>x</sup> flow<sup>r</sup>congestion control and routing models that only partially address the quality of service problem <sup>w</sup> <sup>x</sup> 22,34,42 .

Our approach differs from previous works in two significant ways. First, we give a comprehensive noncooperative resource allocation model for multiclass QoS provision where users are endowed with heterogenous QoS preferences and make decisions based on selfish user needs. Second, users are allowed to choose both the service classes and traffic volumes assigned to them at a router or switch and the properties associated with utility functions are derived from the networking context. The latter leads to non-concave utility functions and we analyze its impact on the resulting game structure.

Our model, although principally intended to model resource sharing and arbitration at a router — the building block of wide area networks — in the context of QoS provision, is more general in nature and can be applied to other settings including the delivery of packaged network services by an Internet Service Provider ISP . Specifically, assuming that aŽ . service provider exports a number of different services — platinum, gold, silver, bronze — to the user, it is generally the case that the more users subscribe to a particular service class the less the quality of service experienced in that class due to congestion effects. The behavioral characteristics of such a system when users have heterogenous preferences and act selfishly to optimize individual utility falls within the framework of the model studied here.

## 1.2. Basic notations and modeling assumptions

Our results rely on a set of elementary assumptions which are described next. The formal network QoS provision game is defined in Section 2. We are given n applications or users and m service classes where each user $i \in [ 1 , n ]$ has a traffic demand given by its mean data rate $\lambda _ { i }$ . Each user can choose where and how much of its traffic to apportion to the m service classes given by its allocation vector $\varLambda _ { i } =$ $( \lambda _ { i 1 } , \lambda _ { i 2 } , \ldots , \lambda _ { i m } ) ^ { T }$ where $\lambda _ { i j } \geq 0$ and $\Sigma _ { i } \lambda _ { i j } = \lambda _ { i }$

The QoS achieved in service class $j \in [ 1 , m ]$ is determined by a QoS function $c _ { j } \ ( \mathrm { e . g . }$ , packet loss rate , and. $c _ { j }$ is monotone in $q _ { j }$ where $\begin{array} { r } { q _ { j } = \sum _ { i } \lambda _ { i j } . } \end{array}$ The generalization to multi-dimensional QoS vectors is shown in Section 3.4. Each user is endowed with a utility function $U _ { i } ( \lambda _ { i j } , \ : c _ { j } )$ which indicates the satisfaction received by user i when sending volume $\lambda _ { i j }$ of traffic receiving QoS level $c _ { j }$ through service class j. We assume that $U _ { i }$ is monotone in $\lambda _ { i j } , c _ { j } .$

The above assumptions are fairly natural given that all that we have said is that the QoS associated with a service class deteriorates when more traffic is pumped into it, users disapprove of bad service quality, and users don’t mind sending more if the ‘‘cost’’ is the same. Two simple observations follow from the above. First, since $c _ { j }$ is a function of the allocation vectors $\varLambda _ { 1 } , \ \varLambda _ { 2 } , \ldots , \ \dot { \ } \varLambda _ { n } ,$ by function composition, $U _ { i }$ is a function of the allocation vectors and the latter constitute the only independent variables. Second, by composition of monotone functions, $U _ { i }$ remains monotone in $\lambda _ { i j } .$ . These implied facts will become relevant later.

## 1.3. Summary of new results

Before we state the results, three notions are of import to their understanding defined formally inŽ Section 2.3 : Nash equilibrium, Pareto optimum, and. system optimum. Roughly speaking, a configuration is a Nash equilibrium if each player cannot improve its individual lot through unilateral actions affecting its traffic allocations. Thus, if every player finds herself in such a ‘‘local optimum,’’ then from the noncooperative perspective, the system is at an impasse — i.e., stable rest point. A configuration is a Pareto optimum if in order to improve the lot of some player, the lot of others must be sacrificed. A configuration is system-optimal if the sum of the individual lots is maximized.

## 1.3.1. Nash equilibria and existence conditions

We give a complete characterization of Nash equilibria and their existence conditions. We show that Nash equilibria need not exist and we show that this is attributable to the non-concave — in particular, quasi-concave<sup>5</sup> but not concave — nature of utility functions arising in the general networking context. For the special case of unsplittable games, however, where a user’s traffic flow is prohibited from being split into separate subflows going into different service classes, we show that Nash equilibria always exist.

## 1.3.2. Relationship to Pareto and system optimality

We analyze the conditions under which Nash equilibria — if they exist — are Pareto- and system-optimal. The latter is shown to be related to the Pareto optimality of a certain normal form configuration derived from Nash equilibria. We also show that there are Nash equilibria that are Paretobut not system-optimal, and that there exist Nash equilibria that are not Pareto-optimal and vice versa.

## 1.3.3. Resource-plentiful systems

We show that for certain ‘‘resource-plentiful’’ systems, Nash equilibria, Pareto optima, and system optima all coincide collapsing into a single class. This item is interesting from the perspective that it gives a sufficient condition under which Nash equilibria are guaranteed to be desirable in the optimality sense. We also show that for resource-plentiful systems a certain self-optimization procedure leads to quick, robust convergence to globally optimal Nash equilibria.

## 1.3.4. Extension to multi-dimensional QoS Õectors

We extend the game-theoretic analysis to multidimensional QoS vector games containing s<sup>G</sup>1 different QoS measures. The monotonicity assumptions described in Section 1.2 are generalized to the s-dimensional QoS vector case. We show that the main results carry over if a uniformity assumption is placed either on application preference or on QoS vector functions.

## 1.4. Related work

1.4.1. Microeconomic approaches to resource allocation

In recent years, there has been a surge of work in ‘‘microeconomic approaches to resource allocation’’ where ideas and tools from microeconomics and game theory have been applied in the formulation and solution of problems arising in flow control, routing, file allocation, load balancing, multi-commodity flow, and quality of service provision, among others 7,15,16,21,22,24,26,30,34,38,41,42,45,46 . A<sup>w</sup> <sup>x</sup> collection of papers covering a broad range of topics can be found in Ref. 6 . A brief survey of some of <sup>w</sup> <sup>x</sup> the literature is provided in Ref. 14 . Some standard <sup>w</sup> <sup>x</sup> references to game theory and microeconomics include Refs. 1,17,40,43,44 .<sup>w</sup> <sup>x</sup>

Many of the earlier papers, including some recent ones 15,16,26,31,41 , have espoused a cooperative<sup>w</sup> <sup>x</sup> game theory framework to model user interactions and derive results based on Pareto optimality. Although fruitful to investigate due to the powerful tools available in cooperative game theory, a potential drawback of this approach is the assumption that users or applications behave cooperatiÕely in networking contexts. For the long-term establishment of virtual circuits or the leasing of telephone lines, the cooperative user model may indeed be viable.<sup>6</sup> However, for best-effort applications that comprise much of today’s Internet traffic, users are largely anonymous with respect to thousands of other users who concurrently share network resources at any given time, and a noncooperative framework, where each user is assumed to optimize individual performance based on his or her limited available information about the network state is better suited.

The noncooperatiÕe framework can be traced as far back as 1981 to a paper by Yemini 49 who has<sup>w</sup> <sup>x</sup> since been more strongly associated with the cooperative approach. The noncooperative network resource allocation approach has been actively pursued by Lazar et al. beginning in the late 1980s 2,20<sup>w</sup> <sup>x</sup> with more recent work carried out jointly with Korilis and Orda 21–24,34 . Their main work has <sup>w</sup> <sup>x</sup> revolved around an optimal flow control problem, and the development of techniques needed to show the existence of Nash equilibria 22 . Korilis et al.<sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> 23,24 have also looked at the problem of using interventions by an impartial external entity — the network manager — to steer a system toward Nash equilibria that are system-optimal. Of special interest is Orda et al.’s work on routing games 34 which is<sup>w</sup> <sup>x</sup> intimately related to the multi-class QoS provision model studied in this paper. This is further explicated below.

Another significant thrust in noncooperative network games is due to recent work by Shenker 42<sup>w</sup> <sup>x</sup> where it is shown how choosing a packet scheduling discipline can influence the nature of the Nash equilibria attained. In the context of a congestion control model, it is shown that for a large class of packet scheduling disciplines, a configuration being Nash need not imply that it is Pareto-optimal. A packet scheduling discipline called Fair Share is described and it is shown to lead to Nash equilibria with desirable properties including uniqueness and reachability by a class of self-optimization procedures.

On the implementation side, the work of Waldspurger et al. 45 deserves attention since it is one of<sup>w</sup> <sup>x</sup> the few works that have built a nontrivial working system — CPU allocation and load balancing in workstation networks — and demonstrated that a system based on microeconomic principles can indeed work in practice. Other implementations worth noting include Wellman’s work on multicommodity flow problems 46,47 .<sup>w</sup> <sup>x</sup>

## 1.4.2. QoS-related network games

Several papers have addressed the specific issue of multi-class QoS provision in high-speed networks using microeconomic models 7,19,31,41 . In Refs. <sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> 31,41 , utility functions are defined with link bandwidth and switch buffers acting as substitutable resources. Pareto-optimal allocation of resources among service classes is affected either by the network exercising admission control 41 or by users<sup>w</sup> <sup>x</sup> performing purchasing decisions 31 . In both ap- <sup>w</sup> <sup>x</sup> proaches, it is assumed that QoS guarantees are computable, given specific resource reservations. As stated earlier, an important goal of our approach is to shield the user from having to make complex computations to estimate service quality.

In Ref. 7 , a general framework for investigating <sup>w</sup> <sup>x</sup> pricing in networks is proposed with service discipline and pricing policy acting as design variables. Simulation results are shown that depict the existence of ‘‘desirable’’ price ranges related to system optimality. The simulations were carried out using a 2-service class packet scheduling algorithm where a shared FIFO queue was partitioned into two segments with high-priority packets being queued at the front and low-priority packets being queued at the back. Four types of applications with different QoS requirements were tested with priority settings set either to 1 or 2.

## 1.4.3. Comparison with congestion control models by Korilis et al. and Shenker

The flow or congestion control models of Korilis and Lazar 22 and Shenker 42 represent a form of <sup>w x</sup> <sup>w x</sup> quality of service provision and we explicate the differences between our model and theirs, given that all three follow the noncooperative framework. The main difference between the models by Korilis et al. and Shenker, and the model studied in the paper is that, indeed, theirs is a flow<sup>r</sup>congestion control model. Phrased in the language of the QoS provision model defined in Section 1.2 a formal definition isŽ given in Section 2.3 , both Refs. 22 and 42 corre-. <sup>w x</sup> <sup>w x</sup> spond to the situation where $n = m$ , each player i is permanently assigned to the fixed serviceclass $i ,$ and either $\lambda _ { i i } \geq 0 \ [ 4 2 ]$ or $0 \leq \lambda _ { i i } \leq \lambda _ { i }$ <sup>w x</sup> 22 , but in both cases, $\lambda _ { i j } = 0$ for $i \neq j .$ . That is, a player, being tied to a fixed service class, has the option of controlling how much traffic 42 — or using what time sched-<sup>w</sup> <sup>x</sup> ule 22 — to send his traffic but<sup>w</sup> <sup>x</sup> not where. Since delay or any other performance measure will deteriorate with increased traffic volume, but volume itself, keeping other things fixed, will generally increase utility, there is an optimum volume assignment — i.e., optimal flow or congestion control — that maximizes player i’s utility.

In our model, there is no a priori fixed 1–1 correspondence of players to service classes. Indeed, the very essence of the QoS provision problem is to give each player $i \in [ 1 , n ]$ the freedom to choose where she wants to send her traffic, from service class 1 all the way to service class m. Hence, our QoS provision model is more general and fundamentally different from the flow control models in its implications, being more complex and producing equilibria structures that are different from those of Refs. 22,42 .<sup>w</sup> <sup>x</sup>

## 1.4.4. Comparison with Orda et al.’s routing model

In Ref. 34 , Orda et al. present a noncooperative <sup>w</sup> <sup>x</sup> routing game where a set of users with fixed throughput demands have a choice of assigning their flow to a set of parallel links or routes. Although motivated by different contexts, assuming independence between the parallel links — i.e., the performance characteristics e.g., queueing delay on someŽ . link or route depends only on the aggregate traffic volume assigned to it — a 1–1 correspondence can be established between Orda et al.’s routing model and the QoS provision model studied here.

Phrased in our language, the set of parallel links correspond to the service classes $j \in [ 1 , m ] ,$ and a user $i \ ' \mathrm s$ average throughput demand $\lambda _ { i }$ is assigned to the m routes given by the assignment vector $\boldsymbol { \varLambda _ { i } } = ( \lambda _ { i 1 } , \lambda _ { i 2 } , \ldots , \lambda _ { i m } )$ . Orda et al. then define a cost function $J _ { j } ^ { i }$ which corresponds to our utility function $U _ { i } ( \lambda _ { i j } , c _ { j } ) .$ . Both depend on the player i as well as the

Ž . service class or route j. Since $J _ { j } ^ { i }$ is interpreted as a cost function, their’s is a minimization problem.

Orda et al. study the routing game under three successively more restrictive assumptions on the cost function $J _ { j } ^ { i }$ Ž . called type-A, type-B, and type-C . In type-B and type-C, the costfunction $J _ { j } ^ { i }$ takes on the form $\lambda _ { i j } c _ { j } ( q _ { j } )$ , thus losing its dependence on i except for the weighting term $\lambda _ { i j } .$ . As is formally defined in Section 2.3, in our QoS provision game, the utility function has the form $\lambda _ { i j } U _ { i } ( c _ { j } ( q _ { j } ) )$ ; thus, the utility’sdependence on heterogenous user preferences is preserved. Hence the results proved in Ref. <sup>w</sup> <sup>x</sup> 34 for type-B and type-C functions correspond to a population of users with homogenous preferences, and thus do not carry over to the more general QoS provision game studied here.

As for type-A games where dependence on individual preferences is preserved, the assumption is made that $J _ { j } ^ { i }$ is convex concave in our context inŽ . $\lambda _ { i j }$ . However, as has been explicated in Section 1.2, the two monotonicity assumptions $\mathrm { ~ \ - ~ } c _ { j }$ is increasing in $q _ { j }$ and $U _ { i }$ is decreasing in $c _ { j } -$ which are basic postulates applicable to most networking contexts of interest, are incompatible with the assumption that $J _ { j } ^ { i }$ is convex is $\lambda _ { i j } .$ In fact, a simple consequence of the monotonicity assumption is that $J _ { j } ^ { i }$ is quasi-conÕex in $\lambda _ { i j } .$ This is so since the composition of the two monotone functions again relates $U _ { i }$ monotonically decreasing toŽ . $\lambda _ { i j } ,$ and monotone functions are trivially quasi-convex. Convexity and quasi-convexity, in the QoS provision context, however, can lead to different consequences.

## 1.4.5. Many-switch systems

In Refs. 4,5 , we describe an architecture for<sup>w</sup> <sup>x</sup> noncooperative multi-class QoS provision in manyswitch systems<sup>7</sup> or wide area networks. Motivated by the analytical results and insights of this paper, we use the single-switch model as a building block in constructing a scalable architecture for multi-class QoS provision in WAN environments. We solve the end-to-end QoS provision problem in many-switch systems and the inter-switch couplings they introduce using distributed control that shields the user from complex computations while preserving the basic premise of selfishness. We show that the network system is able to provide predictable, stratified service without resource reservation and is adaptive under stationary and nonstationary changes to network state.

The rest of the paper is organized as follows. In Section 2, we describe the overall set-up and formulate the network QoS provision model. Section 2.3 discusses the differences between our model and the model of Orda et al. 34 , and the impact of het-<sup>w</sup> <sup>x</sup> erogenous preferences in bringing about non-concave utilities. This is followed by Section 3 which gives a game-theoretic analysis of the QoS provision game structure. Section 3.3 discusses the resourceplentiful case and Section 3.4 extends the game-theoretic analysis to multi-dimensional QoS vectors. The proofs of our results are contained in a separate Appendices A, B and C for the reader’s reference. We conclude with a discussion of our results and future work.

## 2. Noncooperative network qos provision game

## 2.1. Network model

The network model is depicted in Fig. 1. A switch or router is shared by two traffic classes — reserÕed and nonreserÕed Ž . or best-effort — where the former constitutes background or cross traffic and the latter is the aggregate application traffic. That is, $\lambda ^ { \mathrm { N R } } = \Sigma _ { i = 1 } ^ { n } \lambda _ { i }$ where $\lambda _ { 1 } , \lambda _ { 2 } , \ldots , \lambda _ { n }$ are the mean arrival rates of n application traffic sources. The service rate of the system is given by $\mu$ and we will assume that the switch implements a form of GPS packet scheduling with service weights $\alpha _ { 1 } , \alpha _ { 2 }$ $\ldots , \alpha _ { m }$ where $\alpha _ { j } \ge 0 , \ j \in [ 1 , m ]$ , and $\Sigma _ { j = 1 } ^ { m } \alpha _ { j } = 1$

![](/api/attachments/M4QRM2SK/fulltext/images/8c72d1e0bfc27ea0954ab9e95e3f1f1fd227101f9dcd16fdaaaefcb48aec7de9.jpg)  
Fig. 1. Dual traffic classification at output-buffered switch with shared priority queue implementing weighted fair queueing.

Here, m denotes the number of service classes. The total service rate $\mu$ is split between the two traffic classes $\mu = \mu ^ { R } + \dot { \mu } ^ { N R }$ . Service class j of the nonreserved traffic class thus receives a service rate of $\alpha _ { i } \mu ^ { N R }$

In keeping with the ATM framework, we assume fixed-size packets i.e., Ž . cells and we employ output-buffered switches. We implement a generic form of weighted fair queueing achieving perfect isolatedness and conservation of work. The latter come into effect when performing simulations. We ignore efficient implementation considerations of WFQ, treating the processing cost at switches as fixed. The assumption of fixed-size packets simplifies the faithful rendering of service rates commensurate with the weigths $\alpha _ { 1 } , \ldots , \alpha _ { m } .$

## 2.2. Application model

## 2.2.1. Utility function

Given a generic network model where packets are tagged by priority labels receiving differentiated service at switches, we need a framework and control mechanism which is able to exploit this feature to provide service to applications with diverse QoS needs such that the collective good of the whole system is maximized. A utility function is a map U: $\mathbb { R } ^ { s } \to \mathbb { R } _ { + } , \ s \geq 1$ , from QoS vectors to the nonnegative reals indicating the level of satisfaction or utility a certain quality of service brings to an application or user. It is a purely theoretical tool to reason about application behavior assuming certain qualitative shapes about its preferences. Fig. 2 shows two candidate utility functions, on the left, for ‘‘nonurgent’’ e-mail, and on the right, for a real-time video application. The packet loss rates have been exaggerated for illustrative purposes.

![](/api/attachments/M4QRM2SK/fulltext/images/2931d28e3884883a1a4f9573787510bc90e02b6aaf60fb2773a1d2d9a172c057.jpg)

The shapes of the utility functions indicate that non-urgent e-mail is much more tolerant to high packet loss, and unless the loss rate is ‘‘exceedingly’’ high, the e-mail application is almost equally satisfied whether the loss rate is 0 or somewhat higher. The video application, on the other hand, can only tolerate much smaller loss rates, and its utility is concentrated toward 0.

## 2.2.2. Selfishness

Selfishness, in our context, will mean that each application $i \in [ 1 , n ]$ will try to take actions so as to maximize its individual utility $U _ { i } .$ . The forms for $U _ { i }$ as well as user $i \ ' \mathrm { s }$ decision variables for the multiclass QoS provision problem are defined in Section 2.3.

## 2.3. Definition of network QoS proÕision game

## 2.3.1. QoS proÕision problem

Assume we are given m service classes and n applications or players represented by their mean arrival rates $\lambda _ { 1 } , \ldots .$ and utility functions $U _ { 1 } , \dots , U _ { n }$ . We arrive at a resource allocation problem in the following way. Let $\lambda _ { i j } \geq 0 , i \in [ 1 , n ] , j \in$ <sup>w</sup> <sup>x</sup> 1, m , denote the traffic volume of the ith application assigned to service class j. Thus, $\begin{array} { r } { \lambda _ { i } = \sum _ { j = 1 } ^ { m } \lambda _ { i j } . } \end{array}$

![](/api/attachments/M4QRM2SK/fulltext/images/83fc14618f7dc19f2d7102fba5f08908b1fa811a80acc17de790b20ef1a0f2bf.jpg)  
Fig. 2. Utility functions. E-mail application left and video application right . Ž . Ž .

That is, application i is given the freedom to choose which service classes to assign her traffic to and how much. We also consider the special case when traffic assignments are restricted to be ‘‘all in one bag,’ i.e., $\lambda _ { i j } \in \{ \lambda _ { i } , 0 \}$ , for all $j \in [ 1 , m ]$

Let $\varLambda = \left( \lambda _ { i j } \colon i , j \right)$ denote the resource assignment matrix, and let $c _ { 1 } , c _ { 2 } , \ldots , c _ { m }$ be the packet loss rates of the m service classes. Each packet loss rate is a function of ,

$$
c _ {j} = c _ {j} (\Lambda), \quad j \in [ 1, m ].
$$

Assuming isolatedness cf. Section 1.2 , we haveŽ . $c _ { j } = c _ { j } ( { q } _ { j } )$ where $\begin{array} { r } { q _ { j } = \sum _ { i = 1 } ^ { n } \lambda _ { i j } } \end{array}$ is the total traffic volume assigned to class j. This relation is only approximate for work conserving switches. The precise modeling of nonlinearities arising from work conservation, although interesting in its own right, is a general issue not specific to our context, and we will ignore its effect in this paper.

We will also make the assumption that $c _ { j }$ is monotone in $q _ { j } , \mathrm { i . e . , } \mathrm { d } c _ { j } \setminus q _ { j } \geq 0 .$ , a property satisfied by virtually all service disciplines of interest.<sup>8</sup> We will also assume that $\mathrm { d } U _ { i } \setminus \mathrm { d } c \leq 0$ . That is, making the packet loss rate smaller<sup>9</sup> can never decrease the utility experienced by player i.

The model can be extended to the case when application QoS requirements are represented by multi-dimensional QoS vectors $\mathbf { x } \in \mathbb { R } ^ { s } , s \geq 1$ . For example, in addition to packet loss rate, x may specify delay requirements as well as restrictions on their fluctuations such as jitter. It turns out that the analysis of the multi-dimensional case reduces to the scalar case under certain conditions, and we will proceed with packet loss rate c as the sole QoS indicator.

The weighted utility of application i, given assignment , is defined as

$$
\overline {{U}} _ {i} (\Lambda) = \sum_ {j = 1} ^ {m} \lambda_ {i j} U _ {i} (c _ {j}).
$$

Note that the utility function used in Section 1.2, $U _ { i } ( \lambda _ { i j } , \ c _ { j } )$ , corresponds to $\lambda _ { i j } U _ { i } ( c _ { j } )$ . Subject to the above constraints, the static optimization problem can be formulated as

$$
\max _ {\Lambda} \overline {{U}} (\Lambda) = \sum_ {i = 1} ^ {n} \overline {{U}} _ {i} (\Lambda).\tag{2.1}
$$

This is a nonlinear programming problem with equality constraints.

2.3.2. Nash equilibria, Pareto optima, and system optima

Any $\varLambda ^ { \ast }$ that satisfies Eq. 2.1 is calledŽ . systemoptimal. Thus, system optimality corresponds to optimizing the usual resource allocation objective function. An assignment $\varLambda ^ { \ast }$ is Pareto-optimal if for all $\varLambda ,$

$$
\forall i \colon \overline {{U}} _ {i} (\Lambda^ {*}) \leq \overline {{U}} _ {i} (\Lambda) \Rightarrow \forall i \colon \overline {{U}} _ {i} (\Lambda^ {*}) = \overline {{U}} _ {i} (\Lambda).
$$

That is, Pareto optimality states that total utility $\overline { U }$ can only be improved at the expense of one or more individual utility $\overline { { U } } _ { i } .$ . In general, Pareto optimality does not imply system optimality. But, clearly, being system-optimal implies is Pareto-optimal.

The formulation of Nash equilibrium needs a further definition. Given , let $\begin{array} { r } { \boldsymbol { { \cal { \Lambda } } } _ { i } = ( \lambda _ { i 1 , } \lambda _ { i 2 } , } \end{array}$ $\ldots , \lambda _ { i m } )$ denote the ith player’s assignment vector. $\varLambda _ { i }$ is also called the strategy of player i. Let

$$
\mathscr {L} _ {i} (\Lambda) = \left\{\Lambda^ {\prime}: \Lambda_ {k} ^ {\prime} = \Lambda_ {k}, k \neq i, \text { and } \| \Lambda_ {i} ^ {\prime} \| _ {1} = \lambda_ {i} \right\}
$$

where $\left\| { \boldsymbol { x } } \right\| _ { 1 } = \sum _ { j = 1 } ^ { m } \left\| { \boldsymbol { x } } _ { j } \right\|$ . That is, ${ \mathcal { L } } _ { i } ( \varLambda )$ is the set of all unilateral strategies for player i.

An assignment $\varLambda ^ { * }$ is a Nash equilibrium if $\forall i \in [ 1 , n ] , \mathbf { \bar { \forall } } \varLambda \in \mathcal { L } _ { i } ( \varLambda ^ { * } ) .$

$$
\overline {{{U}}} _ {i} (\Lambda) \leq \overline {{{U}}} _ {i} (\Lambda^ {*}).
$$

That is, in a Nash equilibrium, player i cannot improve its individual utility $\overline { { U } } _ { i }$ by unilaterally changing its strategy.

In general, a system-optimal assignment need not be a Nash equilibrium and little can be said about the relation between system optimality, Pareto optimality, and Nash equilibria. In the context of the noncooperative network environment where every player acts selfishly, we are interested in characterizing assignments that are Nash since they represent stable fixed points of the system — i.e., equilibria. From a resource allocation perspective, we would also like to know under what conditions Nash equilibria are Pareto- and system-optimal.

## 2.3.3. Simplifying assumption

To make the analysis tractable, we will work with Ž . unit step utility functions where for each player $i \in [ 1 , n ]$ 9

$$
U _ {i} (c) = \left\{ \begin{array}{l l} 1, & \text { if } c \leq \theta_ {i}, \\ 0, & \text { otherwise }. \end{array} \right.
$$

Here $\theta _ { i } \geq 0$ is a threshold that represents the ith application’s preference. Since $c _ { j } = c _ { j } ( q _ { j } ) , j \in [ 1 , m ] ,$ there exist $b _ { i j } \geq 0$ such that

$$
U _ {i} \big (c _ {j} (q _ {j}) \big) = \left\{ \begin{array}{l l} 1, & \text { if } q _ {j} \leq b _ {i j}, \\ 0, & \text { otherwise }. \end{array} \right.
$$

With a slight abuse of notation, we will sometimes write $U _ { i } ( q _ { j } )$ for the composite function when the distinction is clear from the context.

## 2.3.4. Non-concaÕe utilities

The simplification is reasonable from two perspectives. First, from the technical side, we do not lose very much by sacrificing continuity of the utility function since Lemma 3.5 — which shows the existence of 2-application<sup>r</sup>2-service class games with no Nash equilibria — can be shown to hold even when $U _ { i }$ is continuous and quasi-concave but not con- Ž cave in each. $\lambda _ { i j }$ . This also holds for Theorem $3 . 6 ,$ which generalizes Lemma 3.5 to n-application<sup>r</sup>mservice class games. The crucial factor in proving non-existence is the quasi-concavity property that allows $U _ { i }$ to be concave and convex over local segments and thus produce ‘‘holes’’ when forming convex combinations. In particular, even though $U _ { i }$ is quasi-concave in each $\lambda _ { i j } , \overline { { U } } _ { i } = \Sigma _ { j } \lambda _ { i j } U _ { i }$ need not be quasi-concave.

Second, threshold or step utility functions have been implicitly applied in practical and analytical settings to model and encode<sup>r</sup>convey QoS preferences. For example, hard real-time systems, as defined in the real-time systems literature, have this ‘‘all or nothing’’ property. Furthermore, irrespective of whether the user of an application possesses a step utility preference or not, when interacting with a network system through an application, the user must ultimately code and convey her preference to the underlying system. Bounds on packet loss rate, delay, jitter, and other QoS measures have been used to encode application traffic QoS requirements in different contexts including ones where they are used to compute resource reservations and in some commercial applications 32 .<sup>w</sup> <sup>x</sup>

## 3. Properties of noncooperative QoS provision game

## 3.1. Nash equilibria and existence conditions

This section investigates the structure of Nash equilibria giving a complete characterization of Nash equilibria in the noncooperative multi-class QoS provision game as well as their existence conditions. First, let us impose a total order on the n players given by

$$
i \leq i ^ {\prime} \Leftrightarrow \theta_ {i} \leq \theta_ {i ^ {\prime}}.
$$

Unless otherwise stated, we will assume such a fixed order in the rest of the paper. Following is a simple but often used fact on the induced ordering of the traffic volume thresholds $b _ { i j } .$ It is a consequence of the total ordering of $\theta _ { i }$ and the monotonicity of $c _ { j } .$

Proposition 3.1. $\forall i \in [ 1 , n - 1 ] , \ \forall j \in [ 1 , m ] , \ b _ { i j } \leq$ $b _ { i + 1 j } .$

Next, we define certain subsets of service classes — parameterized by user i — that come into play when characterizing Nash equilibria. Let $I _ { i } ^ { + } = \{ j \in$ <sup>w</sup> <sup>x</sup> 1, m : $q _ { j } > b _ { i j } , \lambda _ { i j } > 0 \} , I _ { i } ^ { - } = \{ j \in [ 1 , m ] \colon$ $q _ { j } < b _ { i j } \}$ and $I _ { i } ^ { 0 } { \stackrel {  } { = } } \{ j \in { \stackrel {  } { [ 1 , m ] } } \colon q _ { j } = b _ { i j } \}$ . That is, $I _ { i } ^ { + }$ denotes the set of service class indices where player i has assigned a positive flow and the total traffic volume allocated exceeds player $i \ ' \mathrm s$ threshold. Thus, user i attains 0 utility in these service classes. Conversely for $I _ { i } ^ { - }$ and $I _ { i } ^ { 0 }$ , however, it is not required that user i have a nonzero assignment in these classes. Let $\begin{array} { r } { \boldsymbol { q } _ { j } ^ { i } = \boldsymbol { \Sigma } _ { k \neq i } \lambda _ { k j } } \end{array}$ . That is, $q _ { j } ^ { i }$ is the traffic volume assigned to service class j not counting player i’s Ž . contribution if any . Hence, $q _ { j } = \lambda _ { i j } + q _ { j } ^ { i }$

Let $J _ { i } ^ { + } = \{ j \in [ 1 , m ] \}$ $q _ { j } ^ { i } \geq \dot { b } _ { i j } \}$ and $J _ { i } ^ { - } = \{ j \in$ <sup>w</sup> <sup>x</sup> 1, m : $q _ { j } ^ { i } < b _ { i j } \}$ . Hence, $J _ { i } ^ { \mp }$ is the set of service classes where, irrespective of player $i \ ' s$ actions, player i cannot garner any utility. Let $J _ { i } ^ { * } = \{ j \in$ <sup>w</sup> <sup>x</sup> 1, m : $\begin{array} { r } { b _ { i j } - q _ { j } ^ { i } = \operatorname* { m i n } _ { k \in J _ { i } ^ { - } } b _ { i k } - q _ { k } ^ { i } \} . ~ J _ { i } ^ { * } } \end{array}$ is the subset of service classes of $J _ { i } ^ { - }$ where the positive utility achievable by user i is minimal.

The next two results give uniform upper bounds on the individual utility of a fixed player where uniformity is with respect to all unilateral strategy changes by the player. Recall that the latter is denoted by ${ \mathcal { L } } _ { i } ( \varLambda )$ where  is any configuration.

Proposition 3.2. GiÕen , $i \in { \ o { I I } } , n ] ,$ let $v _ { i } =$ $\Sigma _ { j \in J _ { i } ^ { - } } b _ { i j } - q _ { j } ^ { i }$ . Then

$$
\forall \Lambda^ {\prime} \in \mathscr {L} _ {i} (\Lambda), \quad \overline {{U}} _ {i} (\Lambda^ {\prime}) \leq v _ {i}.
$$

Proposition 3.3. GiÕen $\varLambda , i \in I I , n J ,$ let $\lambda _ { i } > v _ { i }$ and ${ J _ { i } } ^ { + } = \emptyset$ . Then $\exists _ { i } ^ { * } \in J _ { i } ^ { * }$ such that

$$
\forall \Lambda^ {\prime} \in \mathscr {L} _ {i} (\Lambda), \quad \overline {{U}} _ {i} (\Lambda^ {\prime}) \leq v _ {i} - \left(b _ {i j ^ {*}} - q _ {j ^ {*}} ^ {i}\right).
$$

The two propositions are used in the proof of the following theorem which gives a complete characterization of Nash equilibria.

Theorem 3.4 Ž .Nash characterization . is a Nash equilibrium iff $\forall i \in I I , n J$ ( )either a ${ I _ { i } } ^ { + } \mathrm { { = } } \emptyset , o r , \ ( b )$ ${ I _ { i } } ^ { - } = \emptyset , ~ { J _ { i } } ^ { + } \neq \emptyset , ~ { J _ { i } } ^ { - } \subseteq I _ { i } ^ { o } , ~ o r , ~ ( c ) ~ { I _ { i } } ^ { - } = \emptyset , ~ { J _ { i } } ^ { + } = \emptyset$ $\exists j ^ { * } \in J _ { i } ^ { * }$ such that $J _ { i } ^ { - } \{ j ^ { * } \} \subseteq I _ { i } ^ { o }$

In words, for each player i, one of three conditions must hold: a user either achieves full individual utility $\lambda _ { i } \left( \mathrm { p a r t \left( a \right) } \right)$ , or partial utility $\begin{array} { r } { \nu _ { i } = \sum _ { j \in J _ { i } ^ { - } } b _ { i j } - } \end{array}$ $q _ { j } ^ { i } \cdots \mathrm { d u m p i n g } ^ { , }$ the excess traffic $\lambda _ { i } - \upsilon _ { i }$ into one or more service classes belonging to $J _ { i } ^ { + } \ \left( \mathrm { p a r t \ ( b ) } \right)$ , or partial utility $\pmb { \nu } _ { i } - ( b _ { i j ^ { * } } - q _ { i ^ { * } } ^ { i } )$ with excess traffic being assigned to one of the service classes in $J _ { i } ^ { * }$ Žpart Ž .. c . Service classes belonging to $J _ { i } ^ { + }$ form the most natural dumping ground for channeling excess traffic since player i cannot derive utility from $j \in J _ { i } ^ { + }$ no matter what. If $J _ { i } ^ { + } { = } \emptyset , J _ { i } ^ { * }$ takes on a surrogate role.

The next lemma gives a simple sufficiency condition for 2-application<sup>r</sup>2-service class games in which Nash equilibria do not exist.

Lemma 3.5. Consider the family of 2-application<sup>r</sup> 2-serÕice class systems such that the thresholds $b _ { i j }$ on the total traffic Õolume of the serÕice classes satisfy $b _ { I j } < b _ { 2 j } , j = 1 , 2 \ : ( \mathrm { i . e . }$ , the ordering of Proposition 3.1 is strict . Furthermore, assume the follow-.

ing inequalities hold: ( )a $\lambda _ { 2 } < b _ { I I } + b _ { I 2 } , \left( b \right) \lambda _ { 2 } + \lambda _ { I }$ $> b _ { 2 I } + b _ { 2 2 } > b _ { I I } + b _ { I 2 } , ( c ) \lambda _ { 2 } > m a x \vert b _ { I I , } b _ { I 2 } \vert . T h e n ,$ for such choices of $\lambda _ { i } , ~ b _ { i j }$ , no Nash equilibrium exists.

Games satisfying the above conditions are easy to construct, and the reason that there are no Nash equilibria is because the game leads to a limit cycle. This type of behavior has also been observed in simulation studies. Next we generalize the ‘‘Nash Non-Existence condition’’ to n-application<sup>r</sup>mservice class games. The proof of Theorem 3.6 can be reduced to Lemma 3.5 and is a straightforward consequence.

Theorem 3.6 Ž . Nash non-existence . Consider a napplication<sup>r</sup>m-serÕice class game where the ordering implied by Proposition 3.1 is strict. If there are players i and i with $i ^ { * } > i ^ { \prime }$ satisfying $( a ) \ \Sigma _ { i \neq \mathrm { i ^ { \prime } } } \lambda _ { i }$ $< \Sigma _ { j } b _ { i ^ { \prime } j } , ( b ) ~ { \Sigma } _ { i } \lambda _ { i } > { \Sigma } _ { j } b _ { i ^ { * } j } , ( c ) ~ { \Sigma } _ { i \leq { \mathrm { i ^ { \prime } } } } \lambda _ { i } + { \Sigma } _ { i > { \mathrm { ~ } i ^ { * } } } \lambda _ { i } <$ min ${ } _ { j } b _ { i ^ { * } j } ,$ , then no Nash equilibrium exists.

Whereas Lemma 3.5 and Theorem 3.6 constituted simple, easily constructable conditions for Nash non-existence, the next theorem gives a complete characterization of n-application<sup>r</sup>m-service class games for which Nash equilibria do exist.

Theorem 3.7 Ž . Nash existence . Consider a n-application<sup>r</sup>m-serÕice class game where the ordering implied by Proposition 3.1 is strict. Then a Nash equilibrium exists if and only if at least one of the following holds: a Each player is ‘‘domitable;’’ ( ) $i . e . , \ \forall i , \ \Sigma _ { i ^ { \prime } \neq i } \lambda _ { i ^ { \prime } } \geq \Sigma _ { j } b _ { i j } .$ ( ) . b Let $i ^ { * } = m i n { \it / i . \mathrm { ~ } J _ { i } ^ { \mathrm { ~ - ~ } } \ne }$ œ} 0 . There is a configuration  such that $\forall i > i ^ { * }$ $I _ { i } ^ { + } = \varnothing$ , and one of the three conditions of Theorem 3.4 holds for player $i ^ { * }$ .

The above characterization has several interesting features. First, the theorem states that if any Nash equilibrium exists at all, then, in fact, a Nash equilibrium exists possibly different satisfying conditionsŽ . that are much more restrictive than those of Theorem 3.4. Second, removing the existential quantifier in Ž . <sup>10</sup> part b of the theorem is not possible without replacing it by another existential quantifier of similar scope. This is due to the fact that the problem of checking if a Nash equilibrium exists — given the parameters of a game — is NP-complete.<sup>11</sup> The proof of hardness relies on the hardness of checking whether there is a configuration satisfying constraint Ž . b in the theorem. The latter, in turn, is proved using a reduction from minimum cost multicommodity network flow with step cost functions.

The relevance of these remarks is that, even though it is possible to completely characterize QoS provision games for which a Nash equilibrium exists, it is not possible to give an effectiÕe characterization in the sense of feasible computability. Thus, control algorithms, even if privy to information about the network state, cannot, in general, accurately determine whether a network system with given resources and user demands is prone to instability in the Nash sense.

Let us consider a retricted QoS provision game where each user must channel his entire traffic into a single service class. That is, traffic is unsplittable. When viewed in the routing context, this would correspond to a circuit-switched system where a connection, once assigned a route, must follow the path during the entire lifetime of the connection. In our model, this corresponds to placing the further restriction that $\lambda _ { i j } \in \{ 0 , \lambda _ { i } \}$ for all users i and service classes $j .$ Interestingly, for this restricted game, we can show that a Nash equilibrium always exists.

Theorem 3.8 Ž . Unsplittable games . Any unsplittable game has a Nash equilibrium.

Relating back to the issue of concavity and Nash existence, for unsplittable games, the problem of having to consider function values over convex combinations when utility is quasi-concave does not arise since the domain is discrete. Existence, however, does not mean that a Nash equilibrium is always reached starting from any initial configuration. In Section 3.3, Theorem 3.15, we show that for certain ‘‘resource-plentiful’’ systems, there is robust convergence to Nash equilibria from any initial state.

## 3.2. Relationship to Pareto and system optimality

In this section, we characterize the relationship between Nash equilibria, Pareto optima, and system optima for the multi-class QoS provision game. First, we state a useful lemma that can be used to relate Pareto optimality of a configuration to system optimality.

For a configuration , an equivalent assignment $\varLambda ^ { \prime }$ can be found with the same total utility so that the players are partitioned into two sets around a unique, dividing player $i _ { A ^ { \prime } }$ . The first set consists of players with indices larger than $i _ { A ^ { \prime } }$ with respect to the ordering induced by Proposition 3.1, with all players having full utility. The second set consists of players with smaller indices than $i _ { A ^ { \prime } } ,$ , all of them having zero utility. The third set is the singleton set $\{ i _ { \varLambda ^ { \prime } } \}$ consisting of the dividing player who has partial utility. We will call such an assignment a normal form of .

Lemma 3.9 Ž . Normal form . Let be a configuration with $\overline { { U } } ( A ) < \Sigma _ { i = I } ^ { n } \lambda _ { i }$ . Let $i _ { \varLambda } \equiv m a x { \mathit { l i } } . { \ \overline { { U } } } _ { i } ( \varLambda ) <$ $\lambda _ { i } { \mathit { 3 } }$ Then ' with $\overline { { U } } ( A ^ { \prime } ) = \overline { { U } } ( A )$ ( ) such that a $\begin{array} { r } { \forall i < i _ { A ^ { \prime } } , \overline { { U } } _ { i } ( A ^ { \prime } ) = 0 , } \end{array}$ ( ) and b $\forall i > i _ { \Lambda ^ { \prime } } , \overline { { U } } _ { i } ( \Lambda ^ { \prime } ) = \lambda _ { i }$

The usefulness of the normal form of a configuration including Nash comes into play when check- Ž . ing for system optimality of a Nash assignment. This is so since, as we shall see, it is sufficient to check Pareto optimality of the normal form to establish system optimality of the original configuration. Moreover, a normal form is easy to obtain from the original Nash configuration construction in the proof Ž of Lemma 3.9 and checking for Pareto optimality is . generally easier than checking for system optimality.

Theorem 3.10 Ž . Pareto- and system-optimal . GiÕen a configuration , let  be its normal form. Then is system-optimal iff is Pareto-optimal.

An immediate corollary of the theorem is that a Nash equilibrium is system-optimal iff its normal form is Pareto-optimal. Although Theorem 3.10 gives an interesting relationship between Pareto optimality and system optimality and is useful for reasoning about Nash equilibria in other contexts, it falls short of further exploiting potential structure specific to Nash equilibria. It is an open question whether there is some ‘‘independence’’ relation between Nash equilibria and system optima for the general multiclass QoS provision game.

Given the form of Theorem 3.10, one may wonder whether all assignments that are Nash- and Pareto-optimal are also system-optimal. The next result gives a counter-example, which shows that Theorem 3.10 is ‘‘tight’’ in the sense that, when conditioned with Nash equilibria, there are assignments that are both Nash- and Pareto- but not system-optimal.

## Proposition 3.11. There exist Nash equilibria that are Pareto-optimal but not system-optimal.

Next, we characterize those Nash equilibria that are Pareto-optimal. First, consider a modified game, parameterized by some assignment , defined as follows. The thresholds for the players remain the same as in the original game. However, for each player i, the mean arrival rates are taken to be $\gamma _ { i } \equiv \overline { { U } } _ { i } ( \varLambda )$ . Moreover, there is an additional player 0 whose thresholds $b _ { 0 j }$ are all 0, but whose traffic demand is $\gamma _ { 0 } = \Sigma _ { i } \gamma _ { i } { \stackrel { . } { - } } \Sigma _ { i } \gamma _ { i }$ . Note that the configurations  in the original game for which ; i: $\overline { { U } } _ { i } ( A ^ { \prime } )$ $\geq { \overline { { U } } } _ { i } ( A )$ Ž . correspond many-to-one to system-optimal configurations M for the modified game. Let $\begin{array} { r } { i _ { j } \colon = \operatorname* { m i n } _ { i \neq 0 } \{ \gamma _ { i j } > 0 \} } \end{array}$

Theorem 3.12 Ž . Nash-Pareto characterization . Let be a Nash equilibrium and let $i ^ { * }$ be the player such that $\forall i > i ^ { \bar { * } } , \overline { { { U } } } _ { i } ( \varLambda ) = \lambda _ { i } ; i . e . , i ^ { * } i s$ the largest player with incomplete utility. Then is a Pareto optimum if and only if the following hold: $( a ) \forall i \leq i ^ { * }$ $I _ { i } ^ { + } \subseteq \{ j \colon q _ { j } > b _ { i ^ { * } j } \} .$ ( )b ; j ${ l q } _ { i } \le b _ { i ^ { * } i } \Rightarrow \forall i \ j \notin { I } _ { i } ^ { + } I$ Notice since  is Nash, it follows from the hypothesis aboÕe and Theorem 3.4 that $q _ { j } = b _ { i ^ { * } j } .$ . c The ( ) two sets of players $S _ { I } \equiv \{ i > i ^ { * } : \ \exists j \ \stackrel { \prime } { \lambda } _ { i j } > \stackrel { } { 0 } , \ \exists i ^ { \prime } \leq i ^ { * }$ $j \in I _ { i ^ { \prime } } ^ { + } \dag$ and $S _ { 2 } \equiv \{ i > i ^ { * } \colon \exists j \lambda _ { i j } > 0 , \mathit { q } _ { j } \leq b _ { i ^ { * } j } \}$ are disjoint. d For any system optimum configuration ( ) M of the modified game, i.e., ${ \overline { { U } } } ( M ) \geq \Sigma _ { i = 1 } ^ { n } \gamma _ { i }$ , one of the following holds for each serÕice class j: d1( ) $\begin{array} { r } { \sum _ { i = o } ^ { n } \gamma _ { i j } = b _ { i _ { j } j } j } \end{array}$ when $i _ { j }$ is defined, d2 ( ) $\Sigma _ { i \neq 0 } \gamma _ { i j }$

$$
\begin{array}{l} \geq b _ {i ^ {*} j}, (d 3) \gamma_ {0} > b _ {i ^ {*} j} - \Sigma_ {i \neq 0} \gamma_ {i j} + \Sigma_ {j ^ {\prime} \neq j} b _ {i _ {j j}} - \\ \Sigma_ {i} \Sigma_ {j ^ {\prime} \neq j} \gamma_ {i j}. \end{array}
$$

Note that in part c of Theorem 3.12, an evenŽ . stronger statement is true: Consider the directed graph G whose vertices are the players $i > i ^ { * }$ and whose edges are defined as follows. An edge $( i _ { 1 } , i _ { 2 } )$ exists in G if and only if  j: $\lambda _ { i _ { 1 } j } > 0 , \lambda _ { i _ { 2 } j } > 0 \} \ne \emptyset$ or $\exists j _ { 1 } , j _ { 2 }$ with $\lambda _ { i \downarrow _ { 1 } } > 0 , \lambda _ { i _ { 2 j _ { 7 } } > 0 , }$ and $q _ { j _ { 2 } } \leq b _ { i _ { 1 } j _ { 2 } } .$ Then, there is no path from any vertex in $S _ { 2 }$ to any vertex in $S _ { 1 }$ in the graph G. In other words, for all players $i > i ^ { * }$ there is a path from $S _ { 2 }$ to i, or from i to $S _ { 1 }$ , or neither, but not both.

There are several interesting points to note in the above characterization. First, parts a and b de-Ž . Ž . pend on the combination of facts that is both Nash and Pareto. Parts c and d , however, depend only Ž . Ž . on the fact that  is Pareto. Second, removing the universal quantifier in d ‘‘ForŽ . Ž any configuration $M \ldots ^ { \prime \prime } )$ is impossible for reasons similar to removing the existential quantifier in the statement of Theorem 3.7. The problem of deciding whether a configuration is not Pareto is NP-complete as long as the thresholds of each player are allowed to vary arbitrarily across the classes. Third, the optimization problems that correspond to the above decision problems possess convex feasible regions but the objective functions are highly nonlinear and even discon tinuous. On the other hand, the feasible region can be naturally partitioned into convex subregions over each of which the objective function is, in fact, linear. In each such region, the traffic volume $q _ { j }$ of each class lies between an adjacent pair of threshold values $b _ { i _ { j } j }$ and $b _ { i _ { j } + 1 _ { j } }$ . The properties a to c in theŽ . Ž . above theorem, and, in fact, most of the structural results in this paper, rely on the behavior of objective functions whose level sets are convex within the subregions where they are linear. However, the level sets of these objective functions are nonconvex and consist of an intractably large number of disconnected components once we move outside the boundaries of these subregions. Therefore, searches for optima across boundaries of these subregions rapidly result in combinatorial explosion. The monotonicity properties of Proposition 3.1 do not seem to control this explosion. In general, a simple consequence of the above discussion is that many Nash equilibria exist, which are not Pareto-optimal. In fact, the normal form of a Nash assignment obtained from the construction in the proof of Lemma 3.9 is typically itself Nash, and can be used to exhibit assignments that are Nash- but not Pareto-optimal. Thus, in general, gaps exist in all the important relations between configurations that are Nash equilibria, Pareto-optimal, or system-optimal.

3.3. Resource-plentiful systems and dynamical behaÕior

In this section, we show that for certain ‘‘resource-plentiful’’ systems Nash equilibria always exist, and furthermore, they are always Pareto- and system-optimal. We also show that starting from any initial configuration robust convergence to a Nash equilibrium is achieved.

We define a dynamic game via the dynamic update process $\mathcal { P }$ as follows. We assume that the players move asynchronously, and at each step t, a single player $i _ { t }$ unilaterally and selfishly reassigns its $\lambda _ { i , }$ so that the new assignment $\varLambda _ { t }$ maximizes its individual utility $\overline { { U } } _ { i } ( A )$ . We further assume that no player moves unnecessarily — i.e., a player only makes changes to its assignment if it thereby strictly increases its individual utility. Moreover, for each user i there is an infinite sequence of time steps $t _ { 1 } ^ { i } < t _ { 2 } ^ { i } < . . .$ where i is allowed to perform an update including a ‘‘no move’’ update .Ž .

Theorem 3.13 Ž . Resource-plentiful system . For all $i \in { \cal I } I , n ] ,$ let

$$
\sum_ {j = 1} ^ {m} q _ {j} \leq \sum_ {j = 1} ^ {m} b _ {i j}.\tag{3.14}
$$

Then is a Nash equilibrium if and only if is a system optimum if and only if is a Pareto optimum. MoreoÕer, the optimum Õalue achieÕed is $\overline { { { U } } } ( A ) = \Sigma _ { j } q _ { j } = \Sigma _ { i } \lambda _ { i }$

First, note that $\lambda = \Sigma _ { i } q _ { i } ,$ . Resource plentifulness manifests itself via $\begin{array} { r } { \sum _ { j = 1 } ^ { \check { m } } \check { b } _ { i j } } \end{array}$ . Since $b _ { i j } = c _ { j } ^ { - 1 } ( \theta _ { i } )$ where $c _ { j }$ is the packet loss function and $\theta _ { i }$ is user $i \ ' \mathrm s$ utility threshold cf. Proposition 3.1 , the more Ž . resources there are available in the system $( \mathrm { e . g . }$ bandwidth , the less pronounced. $c _ { j }$ will be and the larger $b _ { i j }$ Žkeeping $\theta _ { i }$ . Ž . fixed . Condition 3.14 then states that there are sufficient resources available to potentially accommodate each user’s requirements, and Theorem 3.13 shows that this is indeed the case even when users are selfish. The next theorem shows that such desirable configurations can be realized in a noncooperative manner starting from any initial configuration.

Theorem 3.15 Ž . Convergence . Assume the supposition of Theorem 3.13 holds. Then, starting from any initial configuration $\varLambda _ { o }$ , the dynamic update process $\mathcal { P }$ conÕerges to a Nash equilibrium . MoreoÕer, is attained as soon as the sequence of players i.e.,( moÕes in the process ) $\mathcal { P }$ includes the subsequence n, $n - I , \ldots , I$

3.4. Extension of game-theoretic analysis to multi-dimensional QoS Õectors

In Section 2, we formulated a noncooperative QoS provision game based on singleton QoS vectors, $\mathbf { x } = \left( c \right)$ , where c was a bound on packet loss rate. Here, we will extend the model to multi-dimensional QoS vectors $\mathbf { x } \in \mathbb { R } ^ { s } , \ s \geq 1$ , and show that the singleton vector analysis carries over unchanged.

Let $\mathbf { x } = ( x _ { 1 } , x _ { 2 } , \ldots . . . , x _ { s } ) ^ { T } .$ and let $\mathbf { x } ^ { j } =$ $( x _ { 1 } ^ { j } , x _ { 2 } ^ { j } , \ldots , x _ { s } ^ { j } ) ^ { T }$ denote the quality of service rendered to service class $j \in [ 1 , m ] .$ . As before, we make the monotonicity assumption d $x _ { r } ^ { j } / \mathrm { d } q _ { j } \geq 0 , r \in [ 1 , s ] .$ $j \in [ 1$ <sup>x</sup> ,m which is satisfied by most packet scheduling policies of interest including weighted fair queueing. Each player’s utility function $U _ { i } ( \mathbf { x } ) , \ i \in$ <sup>w</sup> <sup>x</sup> 1, n , has the form

$$
U _ {i} (\mathbf {x}) = \left\{ \begin{array}{l l} 1, & \text { if } \forall r \in [ 1, s ], x _ {r} \leq \theta_ {r} ^ {i}, \\ 0, & \text { otherwise }, \end{array} \right.
$$

where $\theta ^ { i } = ( \theta _ { 1 } ^ { i } , \theta _ { 2 } ^ { i } , \ldots , \theta _ { s } ^ { i } ) ^ { T } = \ge 0$ is the multi-dimensional threshold vector that represents the ith application’s preference.

In order to deal with the multi-dimensional QoS vectors and thresholds uniformly, we henceforth make one of two uniformity assumptions: either assume that the thresholds ${ \theta } _ { r } ^ { i }$ can be ordered such that the ordering is uniform over r, i.e.,

$$
\forall r \in [ 1, s ], \forall i \in [ 1, n ]: \theta_ {r} ^ {i} \leq \theta_ {r} ^ {i + 1},\tag{3.16}
$$

or we assume that the functional forms $x _ { r } ^ { j }$ are uniform over r for each $j ,$ i.e.,

$$
\forall j \in [ 1, m ] \colon x _ {1} ^ {j} = x _ {2} ^ {j} = \dots = x _ {s} ^ {j}.\tag{3.17}
$$

By isolatedness, $x _ { r } ^ { j } = x _ { r } ^ { j } ( q _ { j } ) , r \in [ 1 , s ] , j \in [ 1 , m ] ,$ and just as in Proposition 3.1, the condition $x _ { r } ^ { j } ( q _ { j } )$ $\leq \theta _ { r } ^ { i }$ can now be stated as $q _ { j } \leq b _ { i j } ^ { r }$ using the definition

$$
b _ {i j} ^ {r} = \left(x _ {r} ^ {j}\right) ^ {- 1} \left(\theta_ {r} ^ {i}\right).
$$

Let $b _ { i j }$ be the minimum over r, i.e., $b _ { i j } =$ $\begin{array} { r } { \operatorname* { m i n } _ { r \in [ 1 , s ] } b _ { i j } ^ { r } . } \end{array}$

We can now rephrase $U _ { i } ( \mathbf { x } ^ { j } )$ as

$$
U _ {i} (\mathbf {x} ^ {j}) = \left\{ \begin{array}{l l} 1, & q _ {j} \leq b _ {i j}, \\ 0, & \text { otherwise }. \end{array} \right.
$$

Moreover, under the assumption that the functional forms $x _ { r } ^ { j }$ are uniform over r for each j where $x _ { * } ^ { j }$ satisfies $\begin{array} { r } { \dot { \forall } j \in [ 1 , m ] , \ \forall r \in [ 1 , s ] , x _ { r } ^ { j } = \dot { x } _ { * } ^ { j } } \end{array}$ , and using the monotonicity of $x _ { * } ^ { j }$ , it can be observed that the following identity holds:

$$
b _ {i j} = \min _ {r \in [ 1, s ]} \left(x _ {*} ^ {j}\right) ^ {- 1} \left(\theta_ {r} ^ {i}\right) = \left(x _ {*} ^ {j}\right) ^ {- 1} \left(\min _ {r \in [ 1, s ]} \theta_ {r} ^ {i}\right).\tag{3.18}
$$

That is, the min operator commutes with $( x _ { * } ^ { j } ) ^ { - 1 }$

Now we are ready to state a total ordering on $b _ { i j }$ for fixed j corresponding to its counterpart Proposition 3.1.

Proposition 3.19. For the multi-dimensional QoS Õector model with assumption 3.16( ) or $( 3 . I 7 ) ,$ there exists an ordering of the players $i \in I I , n J$ such that $\forall i \in I I , n - I J , \forall j \in I I , m J ,$

$$
b _ {i j} \leq b _ {i + 1 j}.
$$

Proposition 3.20. The game-theoretic results of Section 3 hold for the multi-dimensional QoS Õector model with assumption 3.16 or 3.17( ) ( ).

The proof structure of our game-theoretic results rely on Proposition 3.1 to order application QoS preferences. The QoS vectors $( \mathrm { i . e . }$ , scalar packet loss indicator and their functions affect the proof only. through Proposition 3.1. Thus, under either of the uniformity assumptions, and with Proposition 3.19 in hand, it is straightforward to check that the proofs carry over unchanged giving Proposition 3.20.

## 4. Conclusion

We have presented a study of the quality of service provision problem in noncooperative multiclass network environments where applications or users are assumed to be selfish. Users are endowed with heterogenous QoS preferences, and they are allowed to choose both where and how much of their traffic to send. Our framework and its conclusions are best suited — but not exclusively so — for best-effort traffic environments where the network is not required to provide stringent QoS guarantees which can only be accomplished, currently, by employing conservative resource reservations. Rather, service classes with differentiated QoS levels matching the needs of constituent applications are induced by the latter’s selfish interactions, providing reasonably stable and predictable QoS levels as a function of network state.

We have formulated a noncooperative multi-class QoS provision model and given a comprehensive analysis of its properties. We have shown that Nash equilibria — which correspond to stable fixed points in noncooperative games — need not be Pareto- nor system-optimal; in fact, Nash equilibria need not even exist. We have given a complete characterization of Nash equilibria and their existence conditions, and we have studied the game-theoretic structure relating Nash equilibria to Pareto optima and system optima. In general, gaps exist between the classes at all levels, producing a picture of the world that is nontrivial and complex. Much of this is due to the presence of applications with diÕerse QoS requirements, the fact that they are allowed to choose where to send their traffic, and the basic axioms underlying network systems. For ‘‘resource-plenti-$\mathrm { f u l } ^ { \flat }$ systems; however, we have shown that Nash, Pareto, and system optima all coincide, and moreover, convergence is monotone and fast if a form of asynchronous self-optimization is used. We have extended the analysis to systems with multi-dimensional QoS vectors containing both mean- and variance-related QoS measures. We have shown that the game-theoretic results carry over if a uniformity assumption is placed either on application preference thresholds or on QoS vector functions.

Many interesting and challenging problems remain, some of a mostly technical nature, and others motivated by performance evaluation and practical issues arising out of implementation-related considerations. The current work is directed in two main avenues, one, in the extension of the game-theoretic analysis to arbitrary monotone utility functions and the incorporation of pricing which requires further development of analytical tools and techniques, and two, in the study of many-switch systems — a prime target being the realization of such QoS provision architectures in wide area network environments including the Internet. In the latter, the interaction among switches or routers introduces couplings that give rise to new complexities and a slew of challeng ing distributed control problems. An architecture for noncooperative multi-class QoS provision in manyswitch systems and its properties can be found in Refs. 4,5 .<sup>w</sup> <sup>x</sup>

## Appendix A. Proofs of Section 3.1

Proof of Proposition 3.1. Since $\theta _ { i } \leq \theta _ { i + 1 } , \ i \in [ 1 , n$ $- 1 ] ,$ by monotonicity of $c _ { j } , j \in \left[ 1 , m \right]$

$$
c _ {j} ^ {- 1} \left(\theta_ {i}\right) \leq c _ {j} ^ {- 1} \left(\theta_ {i + 1}\right).
$$

Noting that $b _ { i j } = c _ { j } ^ { - 1 } ( \theta _ { i } )$ completes the proof. B

Proof of Proposition 3.2. Since for all $j \in J _ { i } ^ { + }$ $U _ { i } ( c _ { i } ( A ^ { \prime } ) ) = 0$ , the upper bound $\upsilon _ { i }$ follows immediately. B

Proof of Proposition 3.3. First, $J _ { i } ^ { * } \neq \emptyset$ since $J _ { i } ^ { - } \neq$ $\varnothing .$ . Since $\lambda _ { i } > \upsilon _ { i }$ and $J _ { i } ^ { + } = \emptyset$ , for at least one $j \in J _ { i } ^ { - }$ $q _ { j } > b _ { i j }$ . This implies that $U _ { i } ( c _ { j } ( { \cal A } ^ { \prime } ) ) = 0$ . It is easily checked that

$$
\max _ {\Lambda^ {\prime} \in \mathscr {L} _ {i} (\Lambda)} \overline {{U}} _ {i} (\Lambda^ {\prime})
$$

is achieved by such that $\lambda _ { i \ell } ^ { \prime } = b _ { i \ell } - q _ { \ell } ^ { i } \mathrm { i f } \ell \neq j ^ { * }$ and $\lambda _ { i j ^ { * } } ^ { \prime } = \lambda _ { i } - \Sigma _ { \ell \neq j ^ { * } } \lambda _ { i \ell } ^ { \prime } ,$ where $j ^ { * }$ is some element in $J _ { i } ^ { * }$ . Hence, $\overline { { { U } } } _ { i } ( \varLambda ^ { \prime } ) = \Sigma _ { \ell \neq j ^ { \ast } } \ b _ { i \ell } - q _ { \ell } ^ { i } = \upsilon _ { i } -$ $( b _ { i j ^ { * } } - q _ { j ^ { * } } ^ { i } ) _ { \cdot }$

$$
I _ {i} ^ {+} = \emptyset
$$

Proof of Theorem 3.4. Ž . <sup>¥</sup> . Assume I<sup>qs</sup>œ0 part Ž Ž ..a . Since $\forall j , \lambda _ { i j } > 0 \Rightarrow q _ { j } \leq b _ { i j }$ , we have ${ \overline { { U } } } _ { i } ( A ) =$ $\lambda _ { i } ,$ trivial upper bound on $\overline { { U } } _ { i } .$ Assume b holds. By Proposition 3.2, Ž . $\overline { { U } } _ { i } ( A ) \leq \upsilon _ { i }$ where $\begin{array} { r } { { \pmb { \upsilon } } _ { i } = \sum _ { j \in J i ^ { - } } b _ { i j } - q _ { j } ^ { i } . ~ I _ { i } ^ { - } = \emptyset } \end{array}$ and $J _ { i } ^ { - } \subseteq I _ { i } ^ { 0 }$ imply $\overline { { U } } _ { i } ( A ) = ^ { \prime } v _ { i } .$ , thus achieving the upper bound which holds for any $A ^ { \prime } \in \mathcal { L } _ { i } ( A )$

Notice that $J _ { i } ^ { + } , \ J _ { i } ^ { - }$ do not depend on the actions of player i.

Ž . Assume part c . $I _ { i } ^ { - } = \emptyset$ and $\exists j ^ { * } \in J _ { i } ^ { * }$ such that $J _ { i } ^ { - } \setminus \{ j ^ { * } \} \subseteq I _ { i } ^ { 0 }$ imply that $\overline { { U } } _ { \mathrm { i } } ( \varLambda ) \geq \upsilon _ { i } - \dot { ( } b _ { i j ^ { * } } - q _ { i } ^ { i _ { * } } )$ If $J _ { i } ^ { * } = \boldsymbol { \emptyset }$ , which holds iff $J _ { i } ^ { - } = \emptyset$ , then we are done. Assume $J _ { i } ^ { * } \neq \emptyset$ . Notice that the case $J _ { i } ^ { - } \subseteq I _ { i } ^ { 0 }$ is covered by part b or a . Hence, we can assumeŽ . Ž . $j ^ { * } \in I _ { i } ^ { + } . \ I _ { i } ^ { - } = \varnothing$ and $j ^ { * } \in I _ { i } ^ { + }$ imply that $\upsilon _ { i } < \lambda _ { i }$ . Thus, we can apply Proposition 3.3, which, in conjunction with the lower bound on ${ \overline { { U } } } _ { i } ( { \varLambda } ) .$ , yields $\overline { { U } } _ { i } ( A ) = \pmb { \nu } _ { i } -$ $( b _ { i j ^ { * } } - q _ { i ^ { * } } ^ { i } )$

$( \Rightarrow )$ . We will prove the contrapositive. That is, assuming $\exists i \in [ 1 , n ]$ , given , such that

$$
\begin{array}{c} I _ {i} ^ {+} \neq \emptyset \wedge \left(I _ {i} ^ {-} \neq \emptyset \vee J _ {i} ^ {+} = \emptyset \vee J _ {i} ^ {-} \not \subseteq I _ {i} ^ {0}\right) \wedge \left(I _ {i} ^ {-} \neq \emptyset \right. \\ \left. \vee J _ {i} ^ {+} \neq \emptyset \vee \forall j ^ {*} \in J _ {i} ^ {*}: J _ {i} ^ {-} \setminus \{j ^ {*} \} \not \subseteq I _ {i} ^ {0}\right), \end{array}
$$

we will show that is not Nash. There are nine clauses to be considered which are grouped into five cases i – v .Ž . Ž .

Ž .i $( I _ { i } ^ { + } \ne \emptyset \land I _ { i } ^ { - } \ne \emptyset ) , ( I _ { i } ^ { + } \ne \emptyset \land I _ { i } ^ { - } \ne \emptyset \land J _ { i } ^ { + } = \emptyset )$ $( I _ { i } ^ { + } \ne \dot { \emptyset } \wedge I _ { i } ^ { - } \ne \dot { \emptyset } \wedge J _ { i } ^ { - } \notin I _ { i } ^ { \mathrm { 0 } } ) , ( I _ { i } ^ { + } \ne \dot { \emptyset } \wedge I _ { i } ^ { - } \ne \dot { \emptyset } \wedge J _ { i } ^ { + }$ $\ne \emptyset ) , ( I _ { i } ^ { + } \ne \emptyset \wedge I _ { i } ^ { - } \ne \emptyset \wedge \forall j ^ { * } \in J _ { i } ^ { * } \colon J _ { i } ^ { - } \setminus \{ j ^ { * } \} \subset I _ { i } ^ { 0 } )$ They all have in common the conjunction $I _ { i } ^ { + } \neq \emptyset \ \wedge$ $I _ { i } ^ { - } \neq \emptyset$ . The latter implies $\exists j , \ j ^ { \prime } , \ j \neq j ^ { \prime }$ , such that $\lambda _ { i j } > 0 , q _ { j } > b _ { i j } ,$ and $q _ { j ^ { \prime } } < b _ { i j ^ { \prime } }$

We can construct an assignment $A ^ { \prime } \in \mathcal { L } _ { i } ( A )$ such that $\lambda _ { i \ell } ^ { \prime } { = } \lambda _ { i \ell } , \ell { \in } [ 1 , m ] \backslash \{ j , j ^ { \prime } \}$ , and $\lambda _ { i j } ^ { \prime } = \lambda _ { i j } - \epsilon$ $\lambda _ { i j ^ { \prime } } ^ { \prime } = \lambda _ { i j ^ { \prime } } + \epsilon$ , where $\epsilon = \operatorname* { m i n } \{ \lambda _ { i j } , \ b _ { i j ^ { \prime } } - q _ { j ^ { \prime } } \}$ . This yields

$$
\overline {{{U}}} _ {i} (\Lambda^ {\prime}) - \overline {{{U}}} _ {i} (\Lambda) \geq \epsilon
$$

from which it follows that is not a Nash equilibrium. It can be easily checked that the argument applies to the other four clauses.

Ž .ii $\left( I _ { i } ^ { + } \neq \emptyset \land J _ { i } ^ { + } = \emptyset \land J _ { i } ^ { + } \neq \emptyset \right) = F$ . The implication reduces to a tautology. Ž .iii $( I _ { i } ^ { + } \ne \emptyset \land J _ { i } ^ { - } \notin I _ { i } ^ { 0 } \land J _ { i } ^ { + } \ne \emptyset )$ $J _ { i } ^ { - } \nsubseteq I _ { i } ^ { 0 }$ implies that $J _ { i } ^ { - } \neq \emptyset$ . For $j \in J _ { i } ^ { - } \setminus I _ { i } ^ { 0 }$ , either $q _ { j } < b _ { i j }$ or $q _ { j } >$ $b _ { i j } . \mathrm { ~ I f ~ } q _ { j } < b _ { i j }$ , then the argument from i can beŽ . applied. Assume $q _ { j } > b _ { i j } .$

This implies that $U _ { i } ( c _ { i } ( \varLambda ) ) = 0$ . Since $J _ { i } ^ { + } \neq \emptyset$ , for all $j ^ { \prime } \in J _ { i } ^ { + } , \ j ^ { \prime } \neq j$ and $\overset { \prime } { U } _ { i } ( c _ { i ^ { \prime } } ( \varLambda ) ) = 0$ We can construct $A ^ { \prime } \in \mathcal { L } _ { i } ( A )$ such that ${ \lambda } _ { i { \ell } } ^ { \prime } { = } { \lambda } _ { i { \ell } } ,$ $\ell \in [ 1 , m ] \setminus \{ j , j ^ { \prime } \}$ , and $\lambda _ { i j } ^ { \prime } = \lambda _ { i j } - \in , \lambda _ { i j ^ { \prime } } ^ { \prime } = \lambda _ { i j ^ { \prime } } + \epsilon ,$ where $\epsilon = q _ { j } - b _ { i j }$ . We still have $U _ { i } ( \check { c } _ { i ^ { \prime } } ( A ^ { \prime } ) ) = 0$ however,

$$
U _ {i} \left(c _ {j} \left(\Lambda^ {\prime}\right)\right) = b _ {i j} - q _ {j} ^ {i} > 0
$$

since $j \in J _ { i } ^ { - }$ and $q _ { j } ^ { \prime } = b _ { i j } .$ . Hence is not Nash. Ž .iv $\begin{array} { r } { ( I _ { i } ^ { + } \ne \mathsf { \dot { \boldsymbol { \wp } } } \wedge J _ { i } ^ { + } = \emptyset \wedge \mathsf { \dot { \boldsymbol { \wp } } } j ^ { * } \in J _ { i } ^ { * } \colon J _ { i } ^ { - } \setminus \{ j ^ { * } \} \subset I _ { i } ^ { 0 } ) } \end{array}$ $J _ { i } ^ { + } = \emptyset$ implies $J _ { i } ^ { - } \neq \emptyset , J _ { i } ^ { * } \neq \emptyset$ . In fact, $\vert J _ { i } ^ { - } \vert \ge 2$ This follows from $\forall j ^ { * } \in \dot { J } _ { i } ^ { * } \colon J _ { i } ^ { - } \setminus \left\{ j ^ { * } \right\} \not \subseteq I _ { i } ^ { 0 }$ since $J _ { i } ^ { * } \subseteq J _ { i } ^ { - }$ , and assuming $| J _ { i } ^ { - } | < 2$ would imply $J _ { i } ^ { - } \setminus \{ j ^ { * } \} = \emptyset$ which would violate $J _ { i } ^ { - } \setminus \{ j ^ { * } \} \not \subseteq I _ { i } ^ { 0 }$ Let $j \in J _ { i } ^ { - } , \ j ^ { \prime } \in J _ { i } ^ { * }$ , with $j \neq j ^ { \prime }$ . If $q _ { j } < b _ { i j } ,$ then the argument from i applies and we are done. SimilarlyŽ . for $j ^ { \prime } .$ . Let $q _ { j } > b _ { i j } .$ . If $\vert I _ { i } ^ { + } \vert \ge 2$ , then we can choose $j ^ { \prime \prime } \in I _ { i } ^ { + }$ with $j \neq j ^ { \prime \prime }$ and apply the argument in iii Ž . with $I _ { i } ^ { + }$ in place of $J _ { i } ^ { + }$ . Assume $\vert I _ { i } ^ { + } \vert = 1$ , i.e., $I _ { i } ^ { + } = \left\{ j \right\}$ . We only consider the case $q _ { i ^ { \prime } } = b _ { i j ^ { \prime } }$ . Notice that $J _ { i } ^ { - } \setminus J _ { i } ^ { * } \neq \emptyset$ since, if $J _ { i } ^ { - } = J _ { i } ^ { * }$ then $J _ { i } ^ { - } \setminus \{ j \} \subseteq I _ { i } ^ { 0 }$ by $\vert I _ { i } ^ { + } \vert = 1$ , which would contradict the assumption $\begin{array} { r } { \forall j ^ { * } \in J _ { i } ^ { * } \colon J _ { i } ^ { - } \setminus \{ j ^ { * } \} \not \subseteq I _ { i } ^ { 0 } } \end{array}$ Construct the assignment $A ^ { \prime } \in \mathcal { L } _ { i } ( A )$ such that $\lambda _ { i \ell } ^ { \prime }$ $= \lambda _ { i \ell } , \ell { \in } [ 1 , m ] \backslash \{ j , j ^ { \prime } \}$ , and $\lambda _ { i j } ^ { \prime } = \lambda _ { i j } - \epsilon , \lambda _ { i j ^ { \prime } } ^ { \prime } =$ $\lambda _ { i j ^ { \prime } } + \epsilon ,$ , where $\epsilon = q _ { j } - b _ { i j } .$ . Now, $\tilde { U _ { i } } ( c _ { i ^ { \prime } } ( A ^ { \prime } ) ) \tilde { = } 0$ but $U _ { i } ( c _ { j } ( A ^ { \prime } ) ) = b _ { i j } - \ ' q _ { j } ^ { i }$ . Since $j \in J _ { i } ^ { - } \setminus ^ { ^ { \prime } } J _ { i } ^ { * }$ and $j ^ { \prime }$ $\in J _ { i } ^ { * }$

$$
\left(b _ {i j} - q _ {j} ^ {i}\right) - \left(b _ {i j ^ {\prime}} - q _ {j ^ {\prime}} ^ {i}\right) > 0
$$

which implies $\overline { { \mathrm { U } } } _ { i } ( A ^ { \prime } ) - \overline { { \mathrm { U } } } _ { i } ( A ) > 0 .$

Ž .v $( I _ { i } ^ { + } \ne \emptyset \wedge j _ { i } ^ { - } \notin I _ { i } ^ { 0 } \wedge \mathsf { \dot { V } } j ^ { * } \in J _ { i } ^ { * } { : } J _ { i } ^ { - } \setminus \{ j ^ { * } \} \notin I _ { i } ^ { 0 } )$ In the proof of iv ,Ž . $J _ { i } ^ { + } = \emptyset$ was only needed to establish $J _ { i } ^ { - } \neq \emptyset$ which we can get from $J _ { i } ^ { - } \nsubseteq I _ { i } ^ { 0 }$ Hence the argument of iv carries over unchanged.Ž .

Proof of Lemma 3.5. To the contrary, assume is a Nash equilibrium for the example described in the proposition. Due to the first inequality satisfied by the $\lambda _ { i } ^ { \mathbf { \lambda } , } \mathbf { s }$ and the $b _ { i j } ^ { \phantom { } , } \mathbf { s } ,$ it follows that there is a service class $j _ { 1 }$ for which $\lambda _ { 2 j _ { 1 } } = q _ { j _ { 1 } } ^ { 1 } < b _ { 1 j _ { 1 } }$ . Using this observation and applying the Nash characterization from Theorem 3.4 to the player 1, we obtain Žwithout loss of generality, by the choice of $j _ { 1 } ) _ { \ l }$

$$
q _ {j _ {1}} \leq b _ {1 j _ {1}}.\tag{5.1}
$$

Now, due to the second inequality b in the proposi- Ž . tion, it follows that service class $j _ { 2 } \neq j _ { 1 }$ has assigned traffic volume

$$
q _ {j _ {2}} > b _ {2 j _ {2}}.\tag{5.2}
$$

Furthermore, using Eq. 5.1 and the third inequality Ž . in the proposition,

$$
\lambda_ {2 j _ {2}} \neq 0.\tag{5.3}
$$

Moreover, since $b _ { 1 j } < b _ { 2 j }$ , for all j, we know from Eq. 5.1 thatŽ . $\lambda _ { 1 j _ { 1 } } \leq q _ { j _ { 1 } } \leq b _ { 1 j _ { 1 } } < b _ { 2 j _ { 1 } }$ . Thus, we get

$$
\lambda_ {1 j _ {1}} = q _ {j _ {1}} ^ {2} <   b _ {2 j _ {1}}.\tag{5.4}
$$

Using Eqs. 5.2 – 5.4 , and applying the Nash char-Ž . Ž . acterization from Theorem 3.4 to player 2, we get $q _ { j _ { 1 } } \geq b _ { 2 j _ { 1 } }$ which contradicts Eq. 5.1Ž . $b _ { 1 j } < b _ { 2 j }$ , for all j. B

Proof of Theorem 3.7. Ž . Ž . <sup>¥</sup> . First notice that a implies the existence of a Nash equilibrium. This follows by observing that since each player is domitable — i.e., the n equations $\begin{array} { r } { \sum _ { i ^ { \prime } \neq i } \lambda _ { i ^ { \prime } } + \sum _ { j } b _ { i j } + } \end{array}$ $a _ { i } ;$ are satisfied theŽ $a _ { i }$ act as positive slack constants — one can always find a configuration. where each player is dominated in each class. In other words, there is a choice of the 2 nm assignment variables $\lambda _ { i j }$ and slack variables $s _ { i j }$ which will satisfy the nm constraints: $\forall i \forall j \Sigma _ { i ^ { \prime } \neq i } \bar { \lambda } _ { i ^ { \prime } j } = b _ { i j } + s _ { i j }$ Ž . which is straightforward , which in addition satisfy the 2 n constraints: $\forall i \Sigma _ { j } \lambda _ { i j } = \lambda _ { i }$ and $\forall i \Sigma _ { j } s _ { i j } = a _ { i }$ Next, notice that b implies the existence of a NashŽ . equilibrium because, if satisfies the conditions in Ž . b , then each of the players satisfies one of the three conditions of Theorem 3.4.

Ž . Ž . Ž .<sup>«</sup> . Now we show that the negations of a and b together imply that every configuration  is not Nash. The negation of a implies that for eachŽ . configuration , some player is not dominated in some class. This, together with the negation of bŽ . implies that for each configuration  there is a smallest player $i ^ { * }$ which is not dominated in some class, and either there is a player $i > i ^ { * }$ which does not have complete utility in or none of the three Nash conditions holds for the player $i ^ { * }$ . In the latter case, clearly is not Nash. In the former case Žassuming one of the three Nash conditions holds for the player $i ^ { * } )$ , it follows that there is some class $j ^ { * }$ where $q _ { j ^ { * } } \leq b _ { i ^ { * } j ^ { * } }$ . However, since some player $i > i ^ { * }$ does not have full utility in , in order for to be Nash, $q _ { j } \geq b _ { i j } > b _ { i ^ { * } j }$ must hold for every class j due to the strict ordering of thresholds imposed by the statement of the Theorem. Hence it follows that is not Nash. B

Proof of Theorem 3.8. Let m be the number of service classes. If $m = 1$ , then we are done. Assume $m \geq 2$ . Designate one of the service classes, say 1, as a special service class called the dumping ground. Consider the constructive process which starts out with the empty assignment and proceeds to assign the traffic of the n players in descending order $n , n - 1 , \ldots , \ 1$ 1 starting with player n. At step k $( k \in [ 1 , n ] )$ , we assign the traffic of player $n - k + 1$ $\lambda _ { n - k + 1 } ,$ , to some service class $j \in [ 2 , m ]$ if player $n - k + 1$ attains full utility in j. By Proposition 3.1 and the descending order of assignment, we are assured that a player already assigned to $j$ will continue to achieve full utility. If no such service class exists, player $n - k + 1$ is assigned to service class 1. By construction, it follows that the configu ration reached is Nash. B

## Appendix B. Proofs of Section 3.2

Proof of Lemma 3.9. Let $S _ { i _ { \lambda } } = \{ i \in [ 1 , n ] ; i < i _ { \Lambda } \colon$ $\overline { { U } } _ { i } ( A ) \neq 0 \}$ . By the definition of $i _ { A }$ , for all $i > i _ { \Lambda }$ $\overline { { U } } _ { i } ( A ) = \lambda _ { i }$ Ž . , which gives b . If $S _ { i _ { A } } = \emptyset$ , then we are done.

Assume $S _ { i _ { A } } \neq \emptyset$ . We will construct an assignment $\varLambda ^ { \prime }$ from  such that it satisfies property a while Ž . preserving b . Notice that by Theorem 3.4 and Ž . $\lambda _ { i _ { 1 } } > \overline { { U } } _ { i _ { 1 } } ( \varLambda ) , \ q _ { j } \geq b _ { i _ { 1 } }$ for all $j \in [ 1 , m ]$ . Also, by Proposition 3.1, $b _ { i _ { A } j } \geq b _ { i j }$ for all $i \in S _ { i _ { A } }$ . Let

$$
\nu = \lambda_ {i _ {\Lambda}} - \overline {{U}} _ {i _ {\Lambda}} (\Lambda), \quad \pi = \sum_ {i <   i _ {\Lambda}} \overline {{U}} _ {i} (\Lambda).
$$

To achieve a , we will distribute the excess utilityŽ . into service classes j with $q _ { j } > b _ { i _ { A } j }$ thus nullifying their contribution. To avoid otherwise disturbing the utility assignment, we will move a commensurate amount from $\nu ,$ exactly filling the gap left by $\pi .$

That is, $q _ { j } ^ { \prime } = q _ { j } , \ j \in [ 1 , m ]$ , in the modified assignment $\varLambda ^ { \prime }$ . If $\nu > \pi$ , the reassignment can be achieved in one round. If $\nu \leq \pi$ , a refined construction is used that iteratively shrinks the violating player set $S _ { i _ { A } }$ until it becomes empty. Following is a formal description of the construction.

Case i .( ) Assume $\nu > \pi$

Let $K ^ { - } = \{ j \in [ 1 , m ] \colon q _ { j } = b _ { i j } , \lambda _ { i j } > 0 , i \in S _ { i } \} , K ^ { + } =$  <sup>w</sup> <sup>x</sup> j <sup>g</sup> 1, m : $q _ { j } > b _ { i _ { \scriptscriptstyle \lambda } j } , \lambda _ { i _ { \scriptscriptstyle \lambda } j } > 0 \}$ . We construct $\varLambda ^ { \prime }$ as follows. For $i \in S _ { i _ { A } } , j \in K ^ { - }$

$$
\lambda_ {i j} ^ {\prime} = 0, \quad \lambda_ {i _ {\Lambda} j} ^ {\prime} = \lambda_ {i _ {\Lambda} j} + \sum_ {k \in S _ {i _ {\Lambda}}} \lambda_ {k j}.
$$

For $i \in S _ { i _ { \cal A } } , j \in K ^ { + }$

$$
\lambda_ {i j} ^ {\prime} = \lambda_ {i j} + \epsilon_ {i j}, \quad \lambda_ {i _ {\Lambda} j} ^ {\prime} = \lambda_ {i _ {\Lambda} j} - \sum_ {k \in S _ {i _ {\Lambda}}} \epsilon_ {k j},
$$

where $\begin{array} { r } { \epsilon _ { i j } \geq 0 , ~ \sum _ { k \in { S i _ { \lambda } } } ; \epsilon _ { k j } \leq \lambda _ { i _ { \lambda } } \mathbf { j } . } \end{array}$ and $\Sigma _ { i \in { S _ { i } } , \dot { 7 } } \in$ $K ^ { + } \epsilon _ { i j } = \pi$ . For all other i and $j , \lambda _ { i j } ^ { \prime } = \lambda _ { i j } ^ { \prime \prime } .$ By construction, $q _ { j } ^ { \prime } = q _ { j }$ for $j \in [ 1 , m ] ,$ , and since the excess utility $\pi$ has been transferred into service classes belonging to $K ^ { + }$ , we have $\overline { { U } } _ { i } ( A ^ { \prime } ) = 0$ for $i \in S _ { i _ { A } }$ . Hence, $i _ { A ^ { \prime } } = i _ { A }$ . Also, notice that

$$
\overline {{U}} _ {i _ {\Lambda}} (\Lambda^ {\prime}) = \overline {{U}} _ {i _ {\Lambda}} (\Lambda) + \pi
$$

since player $i _ { A } \mathbf { \ ' } _ { s }$ unutilized traffic volume has been tranferred to service classes in $K ^ { - }$ where, by Proposition 3.1, they now count.

Case ii .( ) Assume $\nu \leq \pi$ . We will perform a similar switch as in case i , however, over possibly sev-Ž . Ž . eral rounds each time monotonically shrinking $S _ { i _ { A } }$ and obtaining a new estimate for $i _ { A ^ { \prime } }$ by decrementing the previous estimate.

In the first round, we transfer a traffic volume of from players $i \in S _ { i _ { A } }$ with assignments in $K ^ { - }  { \mathrm { ~  ~ \omega ~ } } _ { 0 }$ service classes belonging to $K ^ { + }$ . To preserve, $q _ { j } ^ { \prime } = q _ { j } ,$ $j \in [ 1 , m ]$ , we transfer an equal amount from player $i _ { A } \mathbf { \ ' } _ { s }$ assignments in $K ^ { + }$ to $K ^ { - }$ . This is possible since $\nu \leq \pi$ . This yields

$$
\overline {{U}} _ {i _ {\Lambda}} (\Lambda^ {\prime}) = \overline {{U}} _ {i _ {\Lambda}} (\Lambda) + \nu = \lambda_ {i _ {\Lambda}}.
$$

Thus, $i _ { A ^ { \prime } } \leq i _ { A } - 1$

If $S _ { i _ { A } } = \emptyset$ then we are done. If $S _ { i _ { A } ^ { \prime } } \neq \emptyset$ , we recursively repeat the switching process with $i _ { A ^ { \prime } }$ in place of $i _ { A }$ until $S _ { i _ { \ A } ^ { \prime } } = \emptyset$ . Since the dividing player’s index monotonically decreases by at least one in each round, the process terminates in at most $i _ { A } - 1$ rounds. B

Proof of Theorem 3.10. Let be the normal form constructed in the proof of Lemma 3.9. We will prove the following statement from which the theorem follows immediately: is not system-optimal iff there is a $\varLambda ^ { \ast }$ with $\overline { { { U } } } ( A ^ { * } ) > \overline { { { U } } } ( A ^ { \prime } )$ Ž . such that a $\forall \mathrm { i } \in [ 1 , n ] , \overline { { U } } _ { i } ( \varLambda ^ { \ast } ) \geq _ { i } ( \varLambda ^ { \prime } )$ , and $( \mathbf { b } ) \ \exists \\\\\mathbf { i } \leq \mathbf { i } _ { A ^ { \prime } }$ , such that $\overline { { U } } _ { i } ( A ^ { * } ) > \overline { { U } } _ { i } ( A ^ { \prime } )$

That is,  is not Pareto-optimal. Note that $\overline { { U } } ( A ^ { \prime } ) =$ $\overline { { U } } ( A )$ by the definition of .

The $\bullet \Leftarrow$ direction of the statement above is trivial. To show the $^ { \star } \implies ^ { \star }$ <sub>direction, we start with a</sub> ˜ <sub>with</sub> $\overline { { U } } ( \tilde { \lambda } ) > \overline { { U } } ( \varLambda ^ { \prime } )$ , which exists since is not systemoptimal. For all $i > i _ { \Lambda ^ { \prime } } , \ \overline { { { U } } } _ { i } ( \Lambda ^ { \prime } ) = \lambda _ { i }$ , hence any increase in the utility $\overset { = } { U } ( \tilde { \Lambda } )$ over $\overline { { U } } ( A ^ { \prime } )$ must come from one or more $i \leq i _ { A ^ { \prime } }$ for which $\overline { { U } } _ { i } ( \tilde { A } ) > \mathbf { \Omega } _ { i } ( A ^ { \prime } )$ Indeed, $\overline { { U } } _ { i } ( A ^ { \prime } ) = 0$ for $i < i _ { A ^ { \prime } } ^ { } ,$ Ž .  hence b and part of condition a , i.e.,Ž . $\forall i < \boldsymbol { i } _ { \lambda ^ { \prime } } , \ \overset { \cdot \cdot } { U } _ { i } ( \tilde { \lambda } ) \geq \overline { { U } } _ { i } ( \lambda ^ { \prime } )$ , are already satisfied. We will construct $\varLambda ^ { * }$ <sub>from</sub> ˜ <sub>such</sub> that the remaining part of a , i.e., Ž . $\forall i \geq i _ { A ^ { \prime } } , \overline { { U } } _ { i } ( \tilde { A } ) \geq$ $\overline { { U } } _ { i } ( A ^ { \prime } )$ , is satisfied as well. Let

$$
L ^ {-} = \left\{i \leq i _ {\Lambda^ {\prime}}: \overline {{U}} _ {i} (\tilde {\Lambda}) > \overline {{U}} _ {i} (\Lambda^ {\prime}) \right\},
$$

$$
L ^ {+} = \left\{i \geq i _ {\Lambda^ {\prime}}: \overline {{U}} _ {i} (\tilde {\Lambda}) <   \overline {{U}} _ {i} (\Lambda^ {\prime}) \right\}.
$$

Clearly, $L ^ { - } \cap L ^ { + } = \emptyset$ . Moreover, $i _ { A ^ { \prime } }$ need not be an element of either $L ^ { - }$ or $L ^ { + }$ . Let

$$
\pi = \sum_ {i \in L ^ {-}} \overline {{U}} _ {i} (\tilde {\Lambda}) - \overline {{U}} _ {i} (\Lambda^ {\prime}),
$$

$$
\nu = \sum_ {i \in L ^ {+}} \overline {{U}} _ {i} (\Lambda^ {\prime}) - \overline {{U}} _ {i} (\tilde {\Lambda}).
$$

By $\overline { { U } } ( \tilde { \lambda } ) > \overline { { U } } ( \varLambda ^ { \prime } )$ , we have $\pi - \nu > 0$ . We can perform a switch in assignments between players in $L ^ { - }$ and $L ^ { + }$ , similar to the proof of Lemma 3.9, obtaining an assignment $\varLambda ^ { * }$ which preserves $q _ { i } ^ { * } =$ $\tilde { q } _ { i } , j \in [ 1 , m ]$ , and which satisfies $\forall i \in L ^ { + } , \ \overline { { U } } _ { i } ( \mathbf { \Sigma ^ { ' } } A ^ { * } )$ $\stackrel { \scriptscriptstyle - , } { = } \overline { { U } } _ { i } ( \varLambda ^ { \prime } ) , \forall i \in L ^ { - } , \overline { { U } } _ { i } ( \varLambda ^ { * } ) \geq \overline { { U } } _ { i } ( \varLambda ^ { \prime } )$ , and for at least one element $i \in L ^ { - } , \overline { { { U } } } _ { i } ( A ^ { * } ) > \overline { { { U } } } _ { i } ( A ^ { \prime } )$

Pick any two players $i _ { - } \in L ^ { - } , \ i _ { + } \in L ^ { + }$ <sub>y</sub>. Then, ' j , $j _ { + } ^ { \mathrm { ~ ~ } } \in [ 1 , m ] , \ j _ { - } ^ { \mathrm { ~ ~ } } \not = j _ { + }$ , such that

$\lambda _ { i _ { - } j _ { - } } > 0 , \quad b _ { i _ { - } j _ { - } } \geq q _ { j _ { - } }$ and $\lambda _ { i _ { + } j _ { + } } > 0 , \quad b _ { i _ { + } j _ { + } } < q _ { j _ { + } }$

The inequalities follow from Lemma 3.9. $j _ { - } \neq j _ { + }$ q follows from the inequalities and the fact that if $j _ { - } = j _ { + }$

$$
b _ {i _ {-} j _ {-}} \geq q _ {j _ {-}} = q _ {j _ {+}} > b _ {i _ {+} j _ {+}} = b _ {i _ {+} j _ {-}},
$$

which leads to a contradiction due to the threshold ordering implied by Proposition 3.1.

Let $\epsilon = \operatorname* { m i n } \{ \lambda _ { i _ { - } j _ { - } } , \lambda _ { i _ { + } j _ { + } } \}$ . We can move an amount of $i _ { - } \ ' _ { \mathrm { s } }$ assignment from $j _ { - } ^ { \mathrm { ~ ~ } } \tan \ j _ { + }$ , and an equal amount of $i _ { + } \gamma _ { s }$ assignment from $j _ { + } ^ { \mathrm { ~ ~ } } \stackrel { \mathrm { ~ t o ~ } } { J _ { - } }$ . By Proposition 3.1, player $i _ { + } \gamma _ { s }$ utility strictly increases by  whereas player $i \_ s$ utility strictly decreases by the same amount. The other players’ utilities remain undisturbed since the total volume assignment to each service class was held invariant.

Since $\pi - \nu > 0$ , this reassignment process can be repeated until a total traffic volume of has been shifted from players in $L ^ { - }$ to players in $L ^ { + }$ and vice versa. Since $\forall i > i _ { \varLambda ^ { \prime } } , \overline { { U } } _ { i } ( \varLambda ^ { \prime } ) = \lambda _ { i }$ , by the definition of , we have that $\forall i > i _ { A ^ { \prime } } , \overline { { U } } _ { i } ( A ^ { * } ) = \lambda _ { i }$ , and thus $\forall i > i _ { \Lambda ^ { \prime } } , \overline { { U } } _ { i } ( { \cal { A } } ^ { * } ) \ge \overline { { U } } _ { i } ( { \cal { A } } ^ { \prime } )$ . For players $i < i _ { A ^ { \prime } }$ $\overline { { U } } _ { i } ( A ^ { * } ) \geq \overline { { U } } _ { i } ( A ^ { \prime } )$ remains satisfied since $\overline { { U } } _ { i } ( A ^ { \prime } ) = \overset { \_ } { 0 }$ The only consideration left is player $i _ { \varLambda ^ { \prime } } . \mathrm { ~ I f ~ } i _ { \varLambda ^ { \prime } } \notin L _ { - }$ $\cup L _ { + }$ , then we are done. If $i _ { \varLambda ^ { \prime } } \in { \cal L } _ { - } ,$ then after the switch operation, either $\overline { { { U } } } _ { i A ^ { ' } } ( { \it A } ^ { * } ) \geq \overline { { { U } } } _ { i A ^ { ' } } ( A ^ { \prime } ) - \mathrm { i n }$ 1 which case we are done — or $\overline { { { U } } } _ { i _ { \wedge ^ { \prime } } } ( { \varLambda } ^ { \ast } ) < \overline { { { U } } } _ { i \varLambda ^ { \prime } } ( { \varLambda } ^ { \prime } )$ In the latter, we may perform a further switch between player $i _ { A ^ { \prime } }$ and players $i < i _ { A ^ { \prime } }$ until $i _ { A ^ { \prime } } \mathrm { ^ { { s } } }$ utility has been sufficiently increased vis-a-vis\` $\overline { { U } } _ { i , \prime } ( A ^ { \prime } )$ This is possible since $\pi - \nu > 0$ . If $i _ { \varLambda ^ { \prime } } \in L _ { + } .$ , and after the switch we still have $\overline { { { U } } } _ { i \lambda ^ { \prime } } ( A ^ { * } ) < \overline { { { U } } } _ { i \lambda ^ { \prime } } ( \varLambda ^ { \prime } )$ then the same process as with $i _ { \varLambda ^ { \prime } } { \in } L$ can be done yielding the desired ordering result. B

Proof of Proposition 3.11. The following describes a counter example consisting of a system of 3 players and 3 service classes and an assignment , which is Nash and Pareto but not system-optimal. As usual, using Proposition 3.1, for each service class j, we can assume that $b _ { 1 j } \leq b _ { 2 j } \leq b _ { 3 j }$ For service class 1, take $b _ { 1 1 } = b _ { 2 1 }$ , and $b _ { 3 1 } = b _ { 1 1 } + 1$ For service class 2, take $b _ { 1 2 } = b _ { 2 2 } = b _ { 3 2 } = e$ where e is a very small positive quantity. For service class 3, take $b _ { 2 3 } = b _ { 3 3 }$ and $b _ { 1 3 } = s _ { \mathrm { \scriptscriptstyle ~ \mathscr ~ } }$ . Also, let $b _ { 3 2 } < b _ { 3 1 } < b _ { 3 3 }$ The assignment is defined as follows. The assignments to service class 1 are: $q _ { 1 } = \lambda _ { 1 1 } = \lambda _ { 1 } = b _ { 1 1 }$ , and $\lambda _ { 2 1 } = \lambda _ { 3 1 } = 0$ . The assignments to service class 2 are: $\begin{array} { r } { { { q } } _ { 2 } = \lambda _ { 2 2 } = \lambda _ { 2 } = b _ { 2 2 } + E , } \end{array}$ where E is a very large quantity and $\lambda _ { 1 2 } = \lambda _ { 3 2 } = 0$ . The assignments to service class 3 are: $q _ { 3 } = \lambda _ { 3 3 } = b _ { 3 3 }$ and $\lambda _ { 1 3 } = \lambda _ { 2 3 } = 0$ This assignment is clearly a Nash equilibrium: $\lambda _ { 2 2 } = \lambda _ { 2 }$ is unutilized, but player 2 cannot unilaterally reassign its share to improve its utility. Players 1 and 3 have full utility. Hence the total utility for assignment is $\lambda _ { 3 } + \lambda _ { 1 }$

This assignment , however, is not system-optimal. The total utility can be increased using the following changes to the assignment: the quantity $\lambda _ { 1 }$ can be moved to service class 2 from service class 1 so that the new $\lambda _ { 1 1 }$ is now 0, but the new $\lambda _ { 2 1 }$ is now equal to $\lambda _ { 1 } . \Lambda$ part of $\lambda _ { 2 }$ equivalent to the quantity $\lambda _ { 1 } + 1$ is moved into service class 3 so that service class 2 now has total volume $q _ { 2 }$ that is one less than its previous value. Therefore $\lambda _ { 2 }$ is now partitioned into $\lambda _ { 2 3 } = \lambda _ { 1 } + 1$ , with the remainder of $\lambda _ { 2 }$ assigned to $\lambda _ { 2 3 }$ while $\lambda _ { 2 1 }$ remains 0. Finally, a part of $\lambda _ { 3 }$ equivalent to the quantity $\lambda _ { 1 } + 1$ is moved to service class 1 so the volume of service class 1 increases overall by 1 unit, and service class 3 retains the same volume as before. Now $\lambda _ { 3 }$ is partitioned into $\lambda _ { 3 1 } =$ $\lambda _ { 1 } + 1$ , with the remainder of $\lambda _ { 3 }$ assigned to $\lambda _ { 3 3 }$ while $\lambda _ { 3 2 }$ remains 0. The utility of player 3 remains the same as before, i.e., it has full utility $\lambda _ { 3 }$ . The utility of player 1 has decreased from $\lambda _ { 1 }$ to 0 and the utility of player 2 has increased from 0 to $\lambda _ { 1 } + 1$ . Hence, the total utility after completion of the above reassignment is $\lambda _ { 1 } + \lambda _ { 3 } + 1$ and hence it has increased by 1 overall which shows that the assignment is not system-optimal. It is not hard to see that is, in fact, Pareto-optimal; i.e., for any assignment that has higher total utility, there must be at least one player, in particular, player 1, whose individual utility in is less than that in . B

Proof of Theorem 3.12. Before we give the proof, we first define a concept that is used often. $\textbf { A } k { - } f l i p$ is a map from one configuration  to another , denoted by a sequence $( i _ { 1 } , j _ { 1 } , i _ { 2 } , j _ { 2 } , \dots , i _ { k } , j _ { k } )$ with min $\lambda _ { i _ { 1 } j _ { 1 } } , \dots , \lambda _ { i _ { k } j _ { k } } \} = \nu > 0$ called the flip Õalue. The map is defined as follows. The new assignments $\lambda _ { i j } ^ { \prime }$ remain the same as $\lambda _ { i j }$ except in the following cases: for each l with $1 \leq l \leq k$

$$
\lambda_ {i _ {l}, j _ {(l + 1) (\mathrm{mod} k)}} ^ {\prime} = \lambda_ {i _ {l}, j _ {(l + 1) (\mathrm{mod} k)}} + \nu , \lambda_ {i _ {l}, j _ {l}} ^ {\prime} = \lambda_ {i _ {l}, j _ {l}} - \nu .
$$

Notice that a flip leaves total volumes unchanged in all classes. Also, player $i _ { l } { ' } s$ utility does not decrease if it holds that:

$$
q _ {j _ {l}} \leq b _ {i _ {l} j _ {l}} \Rightarrow q _ {j _ {(l + 1) (\mathrm{mod} k)}} \leq b _ {i _ {l} j _ {(l + 1) (\mathrm{mod} k)}}.
$$

In fact, player $i _ { l } ^ { \mathrm { ~ ~ } } \mathrm { s }$ utility strictly increases if $q _ { j _ { 1 } } >$ $b _ { i _ { 1 } j _ { 1 } }$ , whereas $q _ { j _ { ( l + 1 ) \ ( \mathrm { m o d } \ k ) } } \leq b _ { i _ { 1 } j _ { ( l + 1 ) \ ( \mathrm { m o d } \ k ) } } .$ . Notice that 2-flips have already been used extensively in earlier proofs.

$( \Rightarrow )$ Ž . . To show a , assume to the contrary, i.e., $\exists i < i ^ { * } \exists j \in I _ { i } ^ { + } \setminus \{ j { : } q _ { i } > b _ { i ^ { * } i } \}$ , in particular, $j \in$ $I _ { i } ^ { + } \setminus I _ { i ^ { * } } ^ { + }$ . Since $i ^ { * }$ has incomplete utility, we know that $I _ { i ^ { * } } ^ { + } \neq \emptyset$ , and by Theorem 3.4, we know that $q _ { j } = b _ { i ^ { * } j }$ . Let $j ^ { * } \in I _ { i ^ { * } } ^ { + }$ . Now, we obtain from by performing the 2-flip $( i , j , i ^ { * } , j ^ { * } )$ , which ensures that the individual utilities of all players except $i ^ { * }$ remain unchanged and $i ^ { * } \ d s$ utility increases by the flip value. This contradicts that is Pareto.Now bŽ . follows from a and the fact thatŽ . Ž is Nash the conditions of Theorem 3.4 applied to $i ^ { * } )$ , and $i ^ { * } \Rightarrow$ $I _ { i } ^ { + } = \emptyset$

To show c , assume to the contrary that there is a Ž . path from $i _ { b } \in S _ { 2 }$ to $i _ { a } \in S _ { 1 }$ in G.

Case 1. $( i _ { a } = i _ { b } = i )$ . Consider a class ${ j _ { a } \in I _ { i ^ { \prime } } ^ { + } }$ for some $i ^ { \prime } \leq i ^ { * }$ , such that $\lambda _ { i , j _ { \mathrm { a } } } > 0$ . The class $j _ { a }$ causes i to be in $S _ { 1 }$ . Consider also a class $j _ { b }$ with $\lambda _ { i j _ { \mathrm { b } } } > 0$ and $q _ { j _ { \mathrm { b } } } \leq b _ { i ^ { * } j _ { \mathrm { b } } }$ which causes i to be in $S _ { 2 }$

( ) Case 1 i . $( i ^ { \prime } = i ^ { * } )$ . That is, ${ j _ { a } } \in I _ { i ^ { * } } ^ { + }$ . Now, we obtain from by performing the 2-flip $( i , j _ { b } , i ^ { * } , j _ { a } )$ which, using the definition of $j _ { a }$ and $j _ { b } ^ { \phantom { \dagger } } .$ , ensures that the individual utilities of all players except $i ^ { * }$ remain unchanged, and $i ^ { * } \ d s$ utility increases by the flip value. This contradicts that is Pareto.

( )Case 1 ii . $( i ^ { \prime } \neq i ^ { * } )$ . We have ${ j } _ { a } \notin I _ { i ^ { * } } ^ { + }$ . Pick a class ${ j _ { c } \in I _ { i ^ { * } } ^ { + } }$ . First obtain using the 2-flip $( i ^ { * } , j _ { c } , i ^ { \prime } , j _ { a } )$ Ž Ž .. which ensures using part a that all players in $\varLambda ^ { \prime \prime }$ have the same utility as in , and therefore, $\varLambda ^ { \prime \prime }$ is Pareto if is Pareto. Now, in fact, in $\varLambda ^ { \prime \prime }$ , it holds that ${ j _ { a } } \in I _ { i ^ { * } } ^ { + }$ , and thus the proof of Case 1 i can beŽ . directly employed to contradict the fact that $\varLambda ^ { \prime \prime }$ Pareto thereby contradicting the fact that is Pareto.

Case 2. $( i _ { a } \neq i _ { b } )$ . Consider the class $j _ { b }$ that causes $i _ { b }$ to be in $S _ { 2 }$ and the class $j _ { a }$ that causes $i _ { a }$ to be in $S _ { 1 }$

( )Case 2 i . $( i ^ { \prime } = i ^ { * } )$ . That is, ${ j _ { a } } \in I _ { i ^ { * } } ^ { + }$ . Since there is a path from $i _ { b } \mathrm { ~ t o ~ } i _ { a }$ in $G ,$ say $i _ { b } = i _ { 1 } , i _ { 2 } , \ldots , i _ { k } = i _ { a } ,$ we use the definition of the edges of $G$ to construct a flip sequence as follows. The existence of the edges $( i _ { l } , i _ { l + 1 } )$ for $1 \leq l < k$ implies the existence of classes $j _ { b } = j _ { 1 } , j _ { 2 } , . . . , j _ { k } = j _ { a }$ , such that the flip sequence $( i _ { b } = i _ { 1 } , j _ { b } = j _ { 1 } , j _ { 2 } , j _ { 2 } , \ldots , i _ { k } = i _ { a } , j _ { k } = j _ { a } )$ has non-zero flip value. Moreover, by the definition of the edges of $G ,$ , and using the definition of $j _ { a }$ and $j _ { b }$ we obtain  from  by performing this k-flip which ensures that the individual utilities of all players except $i ^ { * }$ remain unchanged, and $i ^ { * } \ d s$ utility increasesby flip value. This contradicts the fact that is Pareto.

( ) Case 2 ii . $( i ^ { \prime } \neq i ^ { * } )$ . A preprocessing is performed exactly like Case 1 ii , and thereafter, the proof ofŽ . Case 2 i is applied. Ž .

To show d , assume to the contrary that there is aŽ . system optimum configuration M of the modified game as well as a service class $j ^ { * }$ for which the negations of d1 , d2 , and d3 hold.Ž . Ž . Ž .

$\sum _ { i = 0 } ^ { n } \gamma _ { i j ^ { \ast } } \neq b _ { i _ { j ^ { \ast } j ^ { \ast } } }$ when $i _ { j ^ { \ast } } \geq 1$ is defined; this implies $\gamma _ { i j ^ { * } } < b _ { i _ { i } * j }$ ) since $\overline { { U } } _ { \mathrm { i } } ( M ) = \gamma _ { i }$ for $i \neq 0$ $\sum { \gamma _ { i j ^ { * } } } < b _ { i ^ { * } j ^ { * } }$ i<sup>/</sup>0

$$
\cdot \quad \gamma_ {0} \leq b _ {i ^ {*} j ^ {*}} - \sum_ {i \neq 0} \gamma_ {i j ^ {*}} + \sum_ {j ^ {\prime} \neq j ^ {*}} b _ {i _ {j ^ {\prime}} j} - \sum_ {i} \sum_ {j ^ {\prime} \neq^ {*}} \gamma_ {i j}.
$$

We can now create a configuration from Žin fact, from M . — where the utility of no player decreases and that of $i ^ { * }$ increases — as follows. Beginning with the service class $j ^ { * }$ and the player $i ^ { * }$ , we assign $\lambda _ { i ^ { * } j ^ { * } } ^ { \prime } \equiv \gamma _ { i ^ { * } j ^ { * } } + \operatorname* { m i n } \{ \lambda _ { i ^ { * } } - \gamma _ { i ^ { * } } , \ b _ { i ^ { * } j ^ { * } } -$ ${ \boldsymbol { \Sigma } } _ { i \neq 0 } { \boldsymbol { \gamma } } _ { i j ^ { * } } \}$ . The remaining unallocated volumes ofŽ all players are now allocated to the classes in any . manner that satisfies:

$$
\begin{array}{l} \text {(i)} \forall i \forall j \lambda_ {i j} ^ {\prime} \geq \gamma_ {i j}, \\ \text {(ii)} \forall j \neq j ^ {*} \Sigma_ {i} \lambda_ {i j} ^ {\prime} \leq b _ {i _ {j} j}, \\ \text {(iii)} \Sigma_ {i} \lambda_ {i ^ {*} j ^ {*}} ^ {\prime} \leq b _ {i ^ {*} j}. \end{array}
$$

It is clear that such an allocation is always possible since the $\gamma _ { i j }$ and $b _ { i _ { i } j }$ satisfy the negations of Ž . Ž . Ž . Ž . d1 , d2 and d3 listed above. Now, because of i , Ž . Ž . ii and iii , it follows that $\forall j \neq j ^ { * }$ , the amount that each player i contributes to its utility $\overline { { U } } _ { i } ( A ^ { \prime } )$ through the class j is at least $\gamma _ { i j } ,$ and in fact the player $i ^ { * }$ contributes strictly more than $\gamma _ { i ^ { * } j ^ { * } }$ through class $j ^ { * }$ Since M was chosen so that $\forall i \dag _ { \gamma _ { i } } = \overline { { U } } _ { i } ( \varLambda )$ , we have now exhibited $\mathrm { ~ \bf ~ { ~ a ~ } ~ } \Lambda ^ { \prime }$ which shows that is not Pareto.Ž . <sup>¥</sup> .

We assume is not Pareto and derive a contradiction to part d . IfŽ . is not Pareto, without loss of generality, there is a $\varLambda ^ { \prime }$ where the individual utilities of all players are at least as large as in , and in fact, the utility of the player $i ^ { * }$ strictly increases in going from to $\varLambda ^ { \prime } .$ . But each such configuration corresponds to a configuration $M ^ { \prime }$ of the modified Ž  game based on . with

$$
\overline {{U}} (M ^ {\prime}) = \sum_ {i = 1} ^ {n} \gamma_ {i} ^ {\prime} = \sum_ {i} \overline {{U}} _ {i} (\Lambda^ {\prime}).\tag{5.5}
$$

Clearly, each such configuration $M ^ { \prime }$ embeds a configuration M of the modified game Ž . based on with $\overline { { U } } ( \mathbf { M } ) = \gamma _ { i } = \Sigma _ { i } \overline { { U } } _ { i } ( \mathbf { \Sigma } A )$ . By ‘‘embed’’ we mean that

$$
\begin{array}{l} \forall j \colon \sum_ {i = 0} ^ {n} \gamma_ {i j} ^ {\prime} = \sum_ {i = 0} ^ {n} \gamma_ {i j}, \\ \forall i \forall j \colon \gamma_ {i j} \leq \gamma_ {i j} ^ {\prime}, \text { and } \exists j ^ {*}: \gamma_ {i ^ {*} j ^ {*}} <   \gamma_ {i ^ {*} j ^ {*}} ^ {\prime}. \end{array}
$$

Now consider the class $j ^ { * }$ where $\gamma _ { i ^ { * } j ^ { * } } < \gamma _ { i ^ { * } j ^ { * } } ^ { \prime }$ . For this $j ^ { * }$ Ž . , clearly d1 does not hold: otherwise, $\displaystyle { \dot { \Sigma } } _ { i = 0 } ^ { n } \gamma _ { i j } ^ { \prime }$ exceeds $b _ { i _ { i ^ { * } j } ^ { * } }$ which means that ${ \gamma _ { i _ { i ^ { * } } } } ^ { \prime } \geq \gamma _ { i _ { i ^ { * } } } > \bar { 0 }$ would not contribute to the utility of $M ^ { \prime } ,$ , contradicting Eq. 5.5 . Clearly, d2 does not hold either:Ž . Ž . otherwise, $\begin{array} { r l } { \sum _ { i \neq 0 } } & { { } \gamma _ { i j ^ { * } } ^ { \prime } > b _ { i ^ { * } j ^ { * } } } \end{array}$ , which means that $\gamma _ { i ^ { * } j ^ { * } } ^ { \prime } ( > \gamma _ { i ^ { * } j ^ { * } } \geq 0 )$ would not contribute to the utility of $' M ^ { \prime }$ , again contradicting Eq. 5.5 . Finally, d3Ž . Ž . does not hold: otherwise, since by the fact that d2Ž Ž . . does not hold $\Sigma _ { i \neq 0 } \gamma _ { i j } ^ { \prime } { * } \leq b _ { i ^ { * } j ^ { * } }$ , it would follow that for some class $j ^ { \prime } , \ { \Sigma _ { i = 0 } ^ { n } } ^ { \setminus } { \gamma _ { i j ^ { \prime } } ^ { \prime } } b _ { i _ { i } j j ^ { \prime } }$ . But this would result in $\gamma _ { i _ { j ^ { * } } } ^ { \prime } > 0$ not contributing to the utility of $M ^ { \prime }$ , again contradicting Eq. 5.5 .Ž . B

## Appendix C. Proofs of Section 3.3

Proof of Theorem 3.13. It is sufficient to show that every Nash equilibrium is system-optimal with utility ${ \overline { { U } } } ( A ) { \dot { = } } \Sigma _ { i } \lambda _ { i } .$ . The equivalence of Nash, Pareto, and system optima follows immediately.

Due to the inequality in Eq. 3.14 , for an assign-Ž . ment , each player can always unilaterally reassign its $\lambda _ { i j } \mathrm { ^ { \circ } s }$ and strictly increase its own utility unless the following holds:

$$
\forall i \forall j: \lambda_ {i j} \neq 0 \Rightarrow q _ {j} \leq b _ {i j}.\tag{5.6}
$$

Thus, is a Nash equilibrium i.e., such a reassign-Ž ment is impossible only if Eq. 5.6 holds. But Eq.. Ž . Ž . 5.6 is equivalent to

$$
\forall i \forall j: q _ {j} > b _ {i j} \Rightarrow \lambda_ {i j} = 0,
$$

which, in turn, implies that is system-optimal. Note that if Eq. 5.6 holds forŽ . , then clearly no player contributes to any service class where the contribution would be unutilized — i.e., every player has complete utility and thus $\overline { { U } } ( A ) = \Sigma _ { i } \lambda _ { i }$ Hence Nash, Pareto, and system optima are all equivalent.

## References

<sup>w</sup> <sup>x</sup> 1 T. Basar, G.J. Olsder, Dynamic Noncooperative Game Theory, 2nd edn., Academic Press, 1995.

<sup>w</sup> <sup>x</sup> 2 A. Bovopoulous, A. Lazar, Decentralized algorithms for optimal flow control, in: Proc. 25th Allerton Conference on Communication, Control and Computing, 1987.

<sup>w</sup> <sup>x</sup> 3 A. Campbell, C. Aurrecoechea, L. Hauw, A review of QoS architectures, ACM Multimedia Systems Journal 1996 inŽ . press.

<sup>w</sup> <sup>x</sup> 4 S. Chen, K. Park, A distributed protocol for multi-class QoS provision in noncooperative many-switch systems, in: Proc. IEEE International Conference on Network Protocols, 1998, pp. 98–107.

<sup>w</sup> <sup>x</sup> 5 S. Chen, K. Park, An architecture for noncooperative QoS provision in many-switch systems, in: Proc. IEEE INFO-COM ’99, 1999, in press.

<sup>w</sup> <sup>x</sup> 6 S. Clearwater Ed. , Market-Based Control: A Paradigm for Ž . Distributed Resource Allocation, Scott Clearwater, World Scientific, Hong Kong, 1996.

<sup>w</sup> <sup>x</sup> 7 R. Cocchi, S. Shenker, D. Estrin, L. Zhang, Pricing in computer networks: motivation, formulation, and example, IEEE<sup>r</sup>ACM Trans. Networking 1 6 1993 614–627.Ž . Ž .

<sup>w</sup> <sup>x</sup> 8 R.L. Cruz, A calculus for network delay, part I: network elements in isolation, IEEE Trans. Inform. Theory 37 1Ž . Ž .1991 114–131.

<sup>w</sup> <sup>x</sup> 9 R.L. Cruz, Quality of service guarantees in virtual circuit switched networks, IEEE J. Select. Areas Commun. 13 6Ž . Ž .1995 1048–1056.

<sup>w</sup> <sup>x</sup> 10 G. de Veciana, G. Kesidis, J. Walrand, Resource management in wide-area ATM networks using effective bandwidths, IEEE J. Select. Areas Commun. 13 6 1995 1081–Ž . Ž . 1090.

<sup>w</sup> <sup>x</sup> 11 A. Demers, S. Keshav, S. Shenker, Analysis and simulation of a fair queueing algorithm, Journal of Internetworking: Res. Exper. 1 1990 3–26.Ž .

<sup>w</sup> <sup>x</sup> 12 A. Elwalid, D. Mitra, Effective bandwidth of general Markovian traffic sources and admission control in high speed networks, IEEE<sup>r</sup>ACM Trans. Networking 1 3 1993 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 13 A. Elwalid, D. Mitra, Analysis, approximations and admission control of a multi-service multiplexing system with priorities, in: Proc. IEEE INFOCOM ’95, 1995, pp. 463–472.

<sup>w</sup> <sup>x</sup> 14 D. Ferguson, C. Nikolaou, J. Sairamesh, Y. Yemini, Economic models for allocating resources in computer systems, in: S. Clearwater Ed. , Market-Based Control: a ParadigmŽ . for Distributed Resource Allocation, Scott Clearwater, World Scientific, Hong Kong, 1996.

<sup>w</sup> <sup>x</sup> 15 D. Ferguson, C. Nikolaou, Y. Yemini, An economy for flow control in computer networks, in: Proc. IEEE INFOCOM ’89, 1989, pp. 110–118.

<sup>w</sup> <sup>x</sup> 16 D. Ferguson, Y. Yemini, C. Nikolaou, Microeconomic algorithms for load balancing in distributed computer systems, in: Proc. 8th International Conference on Distributed Computing Systems, 1988, pp. 491–499.

<sup>w</sup> <sup>x</sup> 17 J.W. Friedman, Game Theory with Applications to Economics, Oxford University Press, 1986.

<sup>w</sup> <sup>x</sup> 18 L. Georgiadis, R. Guerin, V. Peris, K. Sivarajan, Efficient´ network QoS provisioning based on per node traffic shaping, IEEE<sup>r</sup>ACM Transactions on Networking 4 4 1996 482–Ž . Ž . 501.

<sup>w</sup> <sup>x</sup> 19 A. Heddaya, K. Park, Parallel computing on high-speed wide-area networks: a pricing policy for its communication needs, in: Proc. 3rd IEEE Workshop on the Architecture and Implementation of High Performance Communication Subsystems, 1995, pp. 188–191.

<sup>w</sup> <sup>x</sup> 20 M.-T.T. Hsiao, A.A. Lazar, Optimal flow control of multiclass queueing networks with decentralized information, in: Proc. IEEE INFOCOM ’87, 1987, pp. 652–661.

<sup>w</sup> <sup>x</sup> 21 Y. Korilis, A. Lazar, Why is flow control hard: optimality, fairness, partial and delayed information, in: Proc. 2nd ORSA Telecommunications Conference, 1992.

<sup>w</sup> <sup>x</sup> 22 Y. Korilis, A. Lazar, On the existence of equilibria in noncooperative optimal flow control, Journal of the ACM 42 Ž . Ž .3 1995 584–613.

<sup>w</sup> <sup>x</sup> 23 Y. Korilis, A. Lazar, A. Orda, Architecting noncooperative networks, IEEE J. Select. Areas Commun. 13 7 1995Ž . Ž . 1241–1251.

<sup>w</sup> <sup>x</sup> 24 Y. Korilis, A. Lazar, A. Orda, Achieving network optima using Stackelberg routing strategies, IEEE<sup>r</sup>ACM Trans. Networking 5 1 1997 161–173.Ž . Ž .

<sup>w</sup> <sup>x</sup> 25 H.T. Kung, T. Blackwell, A. Chapman, Credit-based flow control for ATM networks: credit update protocol, adaptive credit allocation, and statistical multiplexing, in: Proc. SIG-COMM ’94, 1994, pp. 101–114.

<sup>w</sup> <sup>x</sup> 26 J. Kurose, R. Simha, A microeconomic approach to optimal resource allocation in distributed computer systems, IEEE Trans. on Computers 38 5 1989 705–717.Ž . Ž .

<sup>w</sup> <sup>x</sup> 27 J. Kurose, Open issues and challenges in providing quality of service guarantees in high-speed networks, Computer Communication Review 23 1 1993 6–15.Ž . Ž .

<sup>w</sup> <sup>x</sup> 28 A. Lazar, G. Pacifici, Control of resources in broadband networks with quality of service guarantees, IEEE Network Magazine 1991 66–73.Ž .

<sup>w</sup> <sup>x</sup> 29 W.E. Leland, M.S. Taqqu, W. Willinger, D.V. Wilson, On the self-similar nature of Ethernet traffic extended version ,Ž . IEEE<sup>r</sup>ACM Transactions on Networking 2 1994 1–15.Ž .

<sup>w</sup> <sup>x</sup> 30 S. Low, P. Varaiya, A new approach to service provisioning in ATM networks, IEEE<sup>r</sup>ACM Trans. Networking 1 5Ž . Ž .1993 547–553.

<sup>w</sup> <sup>x</sup> 31 S. Low, P. Varaiya, An algorithm for optimal service provisioning using resource pricing, in: Proc. IEEE INFOCOM ’94, 1994, pp. 368–373.

<sup>w</sup> <sup>x</sup> 32 J.-F. Mergen, Personal communication.

<sup>w</sup> <sup>x</sup> 33 R. Nagarajan, J. Kurose, On defining, computing and guaranteeing quality-of-service in high-speed networks, in: Proc. IEEE INFOCOM ’90, 1992, pp. 2016–2025.

<sup>w</sup> <sup>x</sup>34 A. Orda, R. Rom, N. Shimkin, Competitive routing in multiuser communication networks, IEEE<sup>r</sup>ACM Trans. Networking 1 5 1993 510–521.Ž . Ž .

<sup>w</sup> <sup>x</sup> 35 A. Parekh, R. Gallager, A generalized processor sharing approach to flow control in integrated services networks: the single-node case, IEEE<sup>r</sup>ACM Trans. Networking 1 3Ž . Ž .1993 344–357.

<sup>w</sup> <sup>x</sup> 36 A. Parekh, R. Gallager, A generalized processor sharing approach to flow control in integrated services networks: the multiple node case, IEEE<sup>r</sup>ACM Trans. Networking 2 2Ž . Ž . 1994 137–150.

<sup>w</sup> <sup>x</sup> 37 K. Park, G. Kim, M. Crovella, On the relationship between file sizes, transport protocols, and self-similar network traffic, in: Proc. IEEE International Conference on Network Protocols, 1996, pp. 171–180.

<sup>w</sup> <sup>x</sup> 38 K. Park, Self-organized multi-class QoS provision for ABR traffic in ATM networks, in: Proc. 15th IEEE International Phoenix Conference on Computers and Communications, 1996, pp. 446–453.

<sup>w</sup> <sup>x</sup> 39 V. Paxson, S. Floyd, Wide-area traffic: the failure of Poisson modeling, in: Proc. ACM SIGCOMM ’94, 1994, pp. 257– 268.

<sup>w</sup> <sup>x</sup> 40 J. Rosenmuller, The Theory of Games and Markets, North-¨ Holland, 1981.

<sup>w</sup> <sup>x</sup> 41 J. Sairamesh, D. Ferguson, Y. Yemini, An approach to pricing, optimal allocation and quality of service provisioning in high-speed networks, in: Proc. IEEE INFOCOM ’95, 1995, pp. 1111–1119.

<sup>w</sup> <sup>x</sup> 42 S. Shenker, Making greed work in networks: a game-theoretic analysis of switch service disciplines, in: Proc. ACM SIGCOMM ’94, 1994, pp. 47–57.

<sup>w</sup> <sup>x</sup> 44 N.N. Vorob’ev, Game Theory, Springer, 1977.

<sup>w</sup> <sup>x</sup> 43 H.R. Varian, Microeconomic Analysis, Norton Press, 1993.

<sup>w</sup> <sup>x</sup> 45 C. Waldspurger, T. Hogg, B. Huberman, J. Kephart, W. Stornetta, Spawn: a distributed computational economy, IEEE Trans. Software Engineering 18 2 1992 103–117. Ž . Ž .

<sup>w</sup> <sup>x</sup> 46 M.P. Wellman, A market-oriented programming environment and its application to distributed multicommodity flow problems, Journal of Artificial Intelligence Research 1 1993Ž . 1–23.

<sup>w</sup> <sup>x</sup> 47 M.P. Wellman, Market-oriented programming: some early lessons, in: S.H. Clearwater Ed. , Market-Based Control: aŽ . Paradigm for Distributed Resource Allocation, World Scientific, 1995, Chap. 4.

<sup>w</sup> <sup>x</sup> 48 W. Willinger, M. Taqqu, R. Sherman, D. Wilson, Self-similarity through high-variability: statistical analysis of Ethernet LAN traffic at the source level, in: Proc. ACM SIGCOMM ’95, 1995, pp. 100–113.

<sup>w</sup> <sup>x</sup> 49 Y. Yemini, Selfish optimization in computer networks, in: Proc. IEEE Conference on Decision and Control, 1981, pp. 281–285.

Kihong Park received his BA from Seoul National University, Korea, and his PhD in Computer Science from Boston University Ž . 1996 . Presently, he is an assistant professor of computer science at Purdue University. His research centers around design and control issues in high-speed multimedia networks including congestion control, quality of service provision, routing, and the facilitation of adaptive, fault-tolerant computing on large-scale distributed systems. He has over 40 technical publications and has served on several international program committees. He was a Presidential University Fellow at Boston University, is a recepient of the NSF CAREER Award, Fellow-at-Large of the Santa Fe Institute, and is a member of several professional societies including ACM and IEEE.

Meera Sitharam received a B. Tech. from the Indian Institute of Technology, Madras, India, in 1984 and a PhD in Computer Science in 1990 from the University of Wisconsin, Madison, in 1990. She joined the faculty of the Department of Mathematics and Computer Science at Kent State University in 1990, and served as a Humboldt Fellow at the University of Bonn in 1990–1991. She was a visiting associate professor at Purdue University in 1997–1998. Currently she is associate professor at the CISE department of University of Florida at Gainesville.

Shaogang Chen is a PhD student in Electrical and Computer Engineering at Purdue University. He received his B. Eng. in Electrical Engineering from Tsinghua University, China, in 1990, and a M.S. from Ohio State University in 1995. His research interests include quality of service provision architectures for wide area networks, microeconomic approaches to network resource allocation, and traffic control for bursty traffic.

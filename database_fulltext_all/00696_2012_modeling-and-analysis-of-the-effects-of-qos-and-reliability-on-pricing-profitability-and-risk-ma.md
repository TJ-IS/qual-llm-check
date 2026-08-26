---
otero_id: 696
otero_key: "F27BPD6H"
title: "Modeling and analysis of the effects of QoS and reliability on pricing, profitability, and risk management in multiperiod grid-computing networks"
authors: "Jose M. Cruz; Zugang Liu"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.10.012"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Modeling and analysis of the effects of QoS and reliability on pricing, pro<sup>fi</sup>tability, and risk management in multiperiod grid-computing networks

Jose M. Cruz <sup>a,</sup>⁎, Zugang Liu <sup>b</sup>

<sup>a</sup> Department of Operations and Information Management, School of Business, University of Connecticut, Storrs, CT 06269-2041, USA

<sup>b</sup> Department of Business and Economics, Pennsylvania State University, Hazleton, PA, 08071, USA

## a r t i c l e i n f o

Article history: Received 28 July 2010 Received in revised form 31 August 2011 Accepted 11 October 2011 Available online 19 October 2011

Keywords: Grid computing Market network equilibrium Pricing mechanism Quality of service System reliability Risk management Decision support systems

## a b s t r a c t

In this paper we develop a network equilibrium model for optimal pricing and resource allocation in Computational Grid Network. We consider a general network economy model with Grid Resource Providers, Grid Resource Brokers and Grid Users. The proposed framework allows for the modeling and theoretical analysis of Computational Grid Markets that considers a non-cooperative behavior of decision-makers in the same tier of the grid computing network (such as, for example, Grid Resource Providers) as well as cooperative behavior between tiers (between Resource Providers and Grid Brokers). We introduce risk management into the decisior making process by analyzing the decision-marker's reliability and quality of service (QoS) requirement. We analyze resource allocation patterns as well as equilibrium price based on demand, supply, and cost structure of the grid computing market network. We speci<sup>fi</sup>cally answer the following questions with several numerical examples: How do system reliability levels affect the QoS levels of the service providers and brokers under competition? How do system reliability levels affect the pro<sup>fi</sup>ts of resource providers and brokers in a competitive market? How do system reliability levels in<sup>fl</sup>uence the pricing of the services in a competitive environment? How do users' service request types, QoS requirements, and timing concerns affect users behaviors, costs and risks in equilibrium? How does the market mechanism allocate resources to satisfy the demands of users? We <sup>fi</sup>nd that for users who request same services certain timing <sup>fl</sup>exibility can not only reduce the costs but also lower the risks. The results indicated that the value of QoS can be ef<sup>fi</sup>ciently priced based on the heterogeneous service demands

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Grid computing is a form of distributed system wherein computing resources are shared across networks. These resources include CPU hours, storage, and applications and they are shared based upon their availability, capability, and cost, as well as the user's quality of service requirements. Consequently, grid technology can help organizations accelerate application performance, improve productivity and collaboration, and reduce total cost of IT infrastructure ownership. Grid computing has evolved from a niche technology associated with scienti<sup>fi</sup>c and technical computing into a businessinnovating technology that is driving increased commercial adoption. The growth of the grid computing market coupled with the increase in the number of market participants has generated many new challenges. In particular, since the grid-computing market is essentially a decentralized decision-making network, system reliability and quality of service (QoS) are among the major concerns of the market participants and users. In this paper, we study how the issues of quality of service, reliability, risk and standards can be resolved in this emerging market, and how these issues will affect the decision process and support systems as well as a company's bottom line. In particular, we investigate the following questions:

• How do system reliability levels affect the QoS levels of resource providers and brokers in a competitive market?

• How do system reliability levels affect the pro<sup>fi</sup>ts of resource providers and brokers in a competitive market?

• How do system reliability levels in<sup>fl</sup>uence the pricing of services in a competitive environment?

• How do users' service request types, QoS requirements, and timing concerns affect users' behaviors, costs and risks in a competitive market?

• How does the market mechanism allocate resources to satisfy the demands of users with different QoS requirements?

Recently grid computing market design and resource allocation have been a theme of many studies. A signi<sup>fi</sup>cant contribution to establish a market vocabulary and structure that can be associated with grid resource markets is from the work of Buyya [6], Wolski et al. [52], and Bapna et al. [3]. Wolski et al. [52] considers a multicommodity (CPU and storage) resource market and suggests that a tātonnement-based commodities exchange market structure is a better choice for controlling grid resources than auction strategies previously de<sup>fi</sup>ned in Regev and Nisan [41] and Waldspurger et al. [48], particularly with respect to price stability and resource utilization ef<sup>fi</sup>- ciency. Buyya [6], on the other hand, focuses on the implementation issues of scheduling and resource brokering and suggests a variety of market mechanisms, including models based on commodity markets, posted-prices, auctions and bargaining. Lin and Lin [34] examine the optimal service priority selection problem for a grid computing service user, who submits a multi-subtask job for the priced services in a grid computing network. Bapna et al. [3], however, were the <sup>fi</sup>rst to model grid resource allocation based on economic principles. They develop a decentralized market model using a combinatorial auction approach and consider only two classes of decision makers, buyers and sellers. Zhang et al. [57] use real option valuation technique and simulation to analyze economic decision criteria for a grid computing provider wishing to provide such a service to businesses. These studies, however, did not consider QoS, reliability, and risk management in a multiple criteria, multiple resource, multiple decision-makers and multiperiod grid computing network optimization framework.

We propose what we believe is a novel approach to the modeling and analysis of grid computing markets. We model the multicriteria decision-making behavior of various decision-makers, which includes: the maximization of net pro<sup>fi</sup>t and the minimization of risk. The proposed framework which is based on network equilibrium theory, allows for explicit modeling of decentralized decision-making behavior of the market participants. This approach differs from the recent models [3,6,48,51,52] in that, <sup>fi</sup>rst and foremost, we consider several different types of decision makers and model their behavior and interactions explicitly. Second, we introduce risk management into the decision making process by analyzing the decision-marker's reliability and QoS requirement. Finally, the proposed framework provides the tools for computing ef<sup>fi</sup>cient resource allocation patterns as well as equilibrium price patterns based on demand, supply, and cost structure of the grid computing network.

Many authors have previously addressed the issues of QoS, reliability, and risk in grids. In terms of QoS, Dogan and Ozguner [13] consider the problem of scheduling a set of independent tasks with multiple QoS requirements. Golconda and Ozguner [28] compare <sup>fi</sup>ve QoS-based scheduling heuristics. Ernemann [15] addresses the idea of applying economic models to the scheduling task. Chunlin and Layuan [10] consider scheduling <sup>fi</sup>nite resources to satisfy the QoS needs of various grid users with multiple dimensional QoS requirements. In this paper, however, we take a network market approach to QoS and assume that the user's transaction cost is a function of QoS requirement. Moreover, we assume that QoS is a function of the individual decision-maker's system reliability.

In terms of reliability, Hwang and Kesselman [22] present a failure handling system based on work <sup>fl</sup>ows. Jin et al. [27] propose a framework for the adaptive deployment of failure detectors and, based on it, a policy-based failure handling mechanism to choose the appropriate failure recovery method. Kola et al. [32] provide a classi<sup>fi</sup>cation of faults in large distributed systems (with the main focus on grids). Huedo et al. [21] evaluate the reliability of computational grids from the end user's point of view. The book of Xie et al. [55] present many models for measuring reliability of grid computing system. In this paper, in addition to modeling the reliability of individual decision nodes and links, we incorporate reliability into the decision making processes.

Most of the research concerned with grid computing risk have addressed some form of risk in computing jobs. Irwin et al. [24] and Popovici and Wilkes [40] minimize the risk of paying penalties to compensate users so as not to reduce the pro<sup>fi</sup>t of service providers. Kleban and Clearwater [30,31] determine the risk of completing jobs later than expected based on either the makespan (response time) or the expansion factor (slowdown). Yeo and Buyya [56], in contrast, provide a way to evaluate reliability and risk with respect to the required objectives, such as the deadline to complete the job, the budget and the penalty for any deadline violation. Nevertheless, these research consider the case of a single decision-maker and did not consider the grid network market competition and risk.

The grid computing network market equilibrium approach, developed in this paper, permits one to represent the interactions between decision-makers in the market in terms of network connections, reliability, QoS, risk, <sup>fl</sup>ows, and prices. We consider the relationships among QoS, reliability and risk. In addition, we consider noncooperative behavior of decision-makers in the same tier of the grid computing network (such as, for example, grid resource providers) as well as cooperative behavior between tiers.

The paper is organized as follows. In Section 2, we present the model setup. In Section 3, we model the various decision-makers and their behavior and analyze the equilibrium among the heterogenous decision makers. In particular, we develop a variational inequality formulation governing the entire grid computing network. In Section 4, we conduct computational studies to investigate the <sup>fi</sup>ve questions raised in the beginning of the paper. In Section 5, we discuss the managerial insights. In the concluding Section 6, we summarize our results and suggest directions for future research.

## 2. Grid computing network market model setup

In this Section, we develop an equilibrium model for a grid computing network market in which decision-makers operate in a decentralized manner. We develop an economic model of the computational grid market that provides an optimal pricing and resource allocation mechanism. Grid computing is exempli<sup>fi</sup>ed in the Globus project [19] and GrADS project [4]. We note that grid computing is closely related to the fasting emerging business model of “cloud computing”. In particular, Aymerich et al. [2] pointed out that “in computational terms cloud computing is described as a subset of grid computing concerned with the use of special shared computing resources”. In addition, Foster et al. [17] argued that “cloud computing relies on grid computing as its backbone and infrastructure support.” In this case, various services (e.g. <sup>fi</sup>nancial and accounting, database storage and analysis, scienti<sup>fi</sup>c computing, risk management, customer relationship management, etc.) are offered by the “software as a service”, to customers (users). The revenue of the SaaS industry in 2010 has grown by 15.7% worldwide and was forecasted to reach \$9.2 billion [18]. These SaaS providers may or may not own the resources necessary for the computations, and can purchase the resources from resource providers such as Amazon (Compute Cloud Ec2 and Data Could S3) and Sun Microsystems [3].

The structure of the grid presented in this paper generalizes those of Nimrod/G, World Wide Grid [9], Legion [33], NetSolve [43], and DISCWorld [11]. In these grids there are three sets of entities involved in the grid computing — job owners (users), resource owners (resource providers), and the scheduler (broker). Job owners specify their job requirements, the deadline, the budget available for their job, and the time at which the job will be ready to be processed [52]. The resource owners set the price for using their resources, and specify their capacities and availabilities. Examples of resource pricing can be found at Sun Grid [20,47] and the cluster of Tsunamic Technologies Inc. [23]. Note that our network is general enough and therefore a two-tiered network with providers and buyers is a special case of our network where the providers also manage resources.

The economic model presented in this paper re<sup>fl</sup>ects those of the Nimrod/G, World Wide Grid [9] and in Buyya et al. [8]. The World Wide Grid consists of computers in <sup>fi</sup>ve continents and has been used for drug design [5]. The economic model in World Wide Grid considers deadline, budget, and dollar cost of resources to decide the assignment of jobs to resources. Buyya et al. [8] proposed an economic approach for scheduling jobs in a grid. They considered budget, deadline, processing time of jobs and the cost of cpu time of resources to develop Nimrod/G scheduler as part of the Globus framework. In both of these systems, the jobs are submitted to a logically centralized scheduler with detailed descriptions, called GridLet [8], and the scheduler (broker) is responsible for allocating the jobs to the proper resource at the appropriate time so that a business objective is optimized. In this paper, however, in addition to consider cost structures, timing requirements, price sensitivity of demand, and resource requirements, we consider reliability, QoS and risk in order to maximize decision makers' pro<sup>fi</sup>ts and minimize their risks.

Note that the market mechanism in our paper is consistent with that of commodity market models which is the economic mechanism behind many grid computing networks, such as, Nimrod/G, World Wide Grid, Mungi, and MOSIX (see, e.g., [1]). Commodity market models have been discussed and used in a number of studies in the literature (see, e.g., [7,45,53,54]). In particular, in commodity market models, the same type of resources from different providers are substitutable which is the case for grid computing markets since CPU times, storage, and other resources can be considered as commodities.

In particular, in our model, we consider a grid computing network economy in which goods and services are multiple computing resources, such as CPU hours, storage, bandwidth and applications across networks. We divide the grid market participants into three categories according to their role: Grid Resource Providers (Providers), Grid Resource Brokers (Brokers), and Grid Users (Users) and assume that there is a time horizon under consideration and it is divided into T time intervals based on network system utilization (e.g. peak period, intermediate period, and off-peak period). The network structure of the computational grid market (economy) is depicted graphically in Fig. 1. Note that the ideal of grid computing market with providers, brokers and users can also be found in Buyya [6] and in Jiang and Xing [26]. The indexes and variables used throughout this model are summarized in Tables 1 and 2 respectively. All vectors throughout this paper are assumed to be column vectors unless otherwise noted.

Resource providers are those decision-makers who own the resources and can sell them to the service providers (brokers). The prices that providers charge for the resources are determined by the competitive market. At any time period t we assume that there is a total of S providers who may manage one or multiple resources. If a provider does not operate a particular resource in the model we let the provider's capacity of the resource be equal to zero. Brokers, in turn, bear the function of an intermediary. Some existing grid resource brokers are GRUBER [14], and NimRod/G [1,6], for example. Their main function is to provide services to the users. They provide security and current information about available resources and serve as a link to the diverse systems available in the grid. The Brokers who may or may not own the resources can purchase the resources from providers and use the resources to meet the users' service requests. A typical broker is denoted by b with a total of B Brokers (or service providers). We assume that a service provider can offer up to J types of services to the users. In any time period, brokers are represented by the middle tier of nodes in the grid computing network market in Fig. 1. Note that there is a link from each provider to each broker in the network in Fig. 1 which represents that a broker can buy the resource from any provider on the market (equivalently, a provider can sell to any/all the brokers). The decision to buy or sell from a given decision marker is driven by availability, price, transaction cost, etc.

![](/api/attachments/F27BPD6H/fulltext/images/a2d8658c407d39cca84fa30f0b442960000b96084e3dce787efef26db5e59862.jpg)  
Fig. 1. The network structure of the grid computing market.

Table 1  
Indexes used throughout the model.

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td> $t = 1,\dots,T$ </td><td>Time period</td></tr><tr><td> $s = 1,\dots,S$ </td><td>Grid Resource Provider</td></tr><tr><td> $b = 1,\dots,B$ </td><td>Grid Service Broker</td></tr><tr><td> $k = 1,\dots,K$ </td><td>Grid User Market</td></tr><tr><td> $i = 1,\dots,I$ </td><td>Grid Resources</td></tr><tr><td> $j = 1,\dots,J$ </td><td>Service types</td></tr></table>

Our model is general enough to allow service brokers to also own resources in which case the <sup>fi</sup>rm combines the roles of both service broker and resource provider. In addition, note that our model also allows for multiple brokers where a single centralized broker is a special case (B = 1).

The third tier of nodes consists of demand markets of users. We assume that the users are heterogeneous whose demands may have different characteristics. We group the users' demands with similar characteristics into K aggregate demand markets with a typical market denoted by k. In particular, we de<sup>fi</sup>ne the demand markets based on timing, cost sensitivity of demand, QoS requirements of the users. Note that in each market, users can purchase the J types of services offered by the brokers where each service type may require different quantities of various resources (CPU, Storage, etc.). The links on the network connecting brokers and user markets represent a possibility of transactions between brokers and users. We assume that users will try to minimize their total service costs which takes into consideration not only payouts to brokers but also other characteristics of their requests.

In the grid computing market each decision maker may have different goals. The resource providers make their pricing decisions based on demand and availability of the resource during various time periods in order to maximize their utility. The brokers, who also maximize their own utility, may charge different prices for different services based on the characteristics of the demands. On the other hand, the users try to minimize their total cost. Therefore each decision-maker tries to maximize its own good without concern for the global good. Such self interest naturally encourages negotiations and, therefore, cooperation among independent businesses or individuals [6].

Variables used throughout the model.

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td> $q_{sb}^{it}$ </td><td rowspan="2">Amount of flow of Resource  $i$  between Provider  $s$  and Broker  $b$  during time  $t$  SBIT-dimensional vector of  $q_{sb}^{it}$ </td></tr><tr><td> $Q^1$ </td></tr><tr><td> $q_{bk}^{it}$ </td><td rowspan="2">Task flow of service  $j$  between Broker  $b$  and User market  $k$  during time  $t$  BKJT-dimensional vector of  $q_{bk}^{lt}$ </td></tr><tr><td> $Q^2$ </td></tr><tr><td> $y_b^{it}$ </td><td rowspan="2">Amount of broker  $b$ &#x27;s own resource  $i$  used during time  $t$  BIT-dimensional vector of  $y_b^{lt}$ </td></tr><tr><td> $Y$ </td></tr><tr><td> $\rho_{1sb}^{it}$ </td><td>Price associated with the transaction of Recourse  $i$  between Provider  $s$  and Broker  $b$  during time  $t$ </td></tr><tr><td> $\rho_{2bk}^{it}$ </td><td>Price of Service  $j$  associated with transaction between Broker  $b$  and User Market  $k$  during time  $t$ </td></tr><tr><td> $\rho_{3k}^{j}$ </td><td>Total unit cost of the users using Service  $j$  in Market  $k$  are willing to pay</td></tr></table>

We now turn to the description of the cost functions given in Table 3. Each decision-maker is faced with certain transaction costs which are the costs of making an economic exchange. These costs may include costs of coordinating the exchange actions between decision-makers [44], costs of motivating decision-makers to align their interests, costs of cheating or costs of opportunistic behavior [49,50]. The transaction costs are affected/in<sup>fl</sup>uenced by the amount of the resource transacted.

In addition, each <sup>fi</sup>rm is also faced with what we term an operating cost (cf. Table 3), which may include, for example, the general cost of running the business. The operating cost of a <sup>fi</sup>rm is a function of its workload.

We assume that the transaction cost and operating cost are convex and continuously differentiable, and that the unit cost functions are positive and continuous.

## 3. The behavior of decision-makers and equilibrium analysis

We now turn to describing the behavior of the various economic decision-makers. We <sup>fi</sup>rst focus on the resource providers. We then turn to the brokers, and, subsequently, to the users. An equilibrium solution is denoted by “\*”.

## 3.1. The behavior of grid resource providers

Recall that providers are those decision-makers in the grid computing market, who own the resources and sell their resources to the brokers. Let $q _ { s b } ^ { i t }$ denote the nonnegative amount of resource i being transacted from provider s to broker b during time t. We group all the resource <sup>fl</sup>ows associated with all the providers to the brokers into the column vector $Q ^ { 1 } \in R _ { + } ^ { S B I T } . ~ \rho _ { 1 s b } ^ { i t }$ denote the price charged by provider s to broker b for a unit of resource i during time period t. $\rho _ { 1 s b } ^ { i t }$ is an endogenous variable and its equilibrium value $\rho _ { 1 s b } ^ { i t ^ { * } } ; s = 1 , . . . , S ; b = 1 , . . . , B ; i = 1 , . . . , I ; t = 1 , . . . , I$ is determined once the complete network model is solved.

We let $\theta _ { s } ^ { i t }$ denote the amount of the resource i available at provider s in period t, and therefore we have the following capacity constraint:

$$
\sum_ {b = 1} ^ {B} q _ {s b} ^ {i t} \leq \theta_ {s} ^ {i t} \quad \forall i, s, t\tag{1}
$$

that is, the total amount of resource transacted with brokers cannot exceed the amount available at provider s during time interval t and given by $\theta _ { s } ^ { i t } .$ . Note that if provider s does not operate certain type of resource we let the supplier's capacity of the resource, $\theta _ { s } ^ { i t } ,$ be equal to zero.

A provider s is faced with various costs of operating its resources. We refer collectively to such costs as an operating cost and denote it by $c _ { s } ( Q ^ { 1 } )$ . In addition, while the resources are being transacted from providers to brokers, there will be some transaction costs associated with each transaction process. The transaction costs are affected/ in<sup>fl</sup>uenced by the amount of the resource transacted. Therefore, in order to represent the most general case, we have that

Cost functions used throughout the model.

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td> $c_{sb}^{it}(q_{sb}^{it})$ </td><td>Transaction cost function of Recourse  $i$  of Provider  $s$  transacting with Broker  $b$  during time  $t$ </td></tr><tr><td> $c_s(Q^1)$ </td><td>Operating cost function of Provider  $s$ </td></tr><tr><td> $c_b(Q^1,Q^2,Y)$ </td><td>Operating cost function of Broker  $b$ </td></tr><tr><td> $\hat{c}_{sb}^{it}(q_{sb}^{it})$ </td><td>Transaction cost function of Recourse  $i$  of Broker  $b$  transacting with Provider  $s$  during time  $t$ </td></tr><tr><td> $c_{bk}^{it}(q_{bk}^{it})$ </td><td>Transaction cost function of Service  $j$  of Broker  $b$  transacting with User Market  $k$  during time  $t$ </td></tr><tr><td> $\hat{c}_{bk}^{jt}(Q^2)$ </td><td>Unit transaction function of Service  $j$  of User Market  $k$  transacting with Broker  $b$  during time  $t$ </td></tr></table>

$$
c _ {s b} ^ {i t} \left(q _ {s b} ^ {i t}\right), \quad \forall s, b, i, t.\tag{2}
$$

As noted in the introduction, we assume that each provider seeks to maximize his/her net revenue. The optimization problem faced by grid resource provider s can be expressed as:

$$
\text { Maximize } \sum_ {i = 1} ^ {I} \sum_ {t = 1} ^ {T} \sum_ {b = 1} ^ {B} \left(\rho_ {1 s b} ^ {i t *} \times q _ {s b} ^ {i t} - c _ {s b} ^ {i t} \left(q _ {s b} ^ {i t}\right)\right) - c _ {s} \left(Q ^ {1}\right).\tag{3}
$$

Objective function (3) represents the net revenue of provider s.

In addition to the criterion of pro<sup>fi</sup>t maximization, each provider also seeks to minimize the total risk associated with the transactions with the next tier of decision-makers, the brokers, over the planning horizon T. The risk is de<sup>fi</sup>ned as the expected penalty that the provider will have to pay due to system or network related failures. System related failures comprise hardware, base software, and grid middleware components that could unpredictably fail. The network related failures includes network disconnection and network saturation. Moreover, the network can also lose its QoS due to dynamic changes in resource load like the increase of network traf<sup>fi</sup>c.

The provider's risk function can be modeled as the expected penalty of the system. We can express it as:

$$
r _ {s} ^ {i t} \left(Q _ {s t} ^ {i}\right) = \omega^ {s} \int_ {0} ^ {Q _ {s t} ^ {i}} \left(Q _ {s t} ^ {i} - x\right) f _ {s} ^ {i t} (x) d x\tag{4}
$$

where $\begin{array} { r } { Q _ { s t } ^ { i } { = } \sum _ { b } ^ { B } { = } _ { 1 } q _ { s b } ^ { i t } , f _ { s } ^ { i t } ( x ) } \end{array}$ denotes the probability density function that the system fails when processing the $\dot { \boldsymbol { x } } ^ { t h }$ unit of workload, and $\omega ^ { s }$ denotes the unit penalty for tasks that are not completed in time.

Lemma 1. $r _ { s } ^ { i t } ( Q _ { s t } ^ { i } )$ is a convex function of $q _ { s b } ^ { i t }$

Proof.

$$
\begin{array}{l} \frac {\partial r _ {s} ^ {i t} \left(Q _ {s t} ^ {i}\right)}{\partial q _ {s b} ^ {i t}} = \frac {\partial r _ {s} ^ {i t} \left(Q _ {s t} ^ {i}\right)}{\partial Q _ {s t} ^ {i}} \\ = \omega^ {s} \frac {\partial \int_ {0} ^ {Q _ {s t} ^ {i}} Q _ {s t} ^ {i} f _ {s} ^ {i t} (x) d x}{\partial Q _ {s t} ^ {i}} - \omega^ {s} \frac {\partial \int_ {0} ^ {Q _ {s t} ^ {i}} x f _ {s} ^ {i t} (x) d x}{\partial Q _ {s t} ^ {i}} \\ = \omega^ {s} \left(Q _ {s t} ^ {i} f _ {s} ^ {i t} \left(Q _ {s t} ^ {i}\right) + \int_ {0} ^ {Q _ {s t} ^ {i}} f _ {s} ^ {i t} (x) d x - Q _ {s t} ^ {i} f _ {s} ^ {i t} (x)\right) \\ = \omega^ {s} \int_ {0} ^ {Q _ {s t} ^ {i}} f _ {s} ^ {i t} (x) d x \end{array}
$$

The second derivative of $r _ { s } ^ { i t } ( Q _ { s t } ^ { i } )$ is simply $\omega ^ { s }  { f _ { s } } ^ { i t } (  { Q _ { s t } } ^ { i } )$ ), which is nonnegative. So, the expected penalty function $r _ { s } ^ { i t } ( Q _ { s t } ^ { i } )$ is convex. □

Note that our model does not need any assumptions regarding the type of probability distribution. In Section 4, in order to conduct computational studies, following Xie et al. [55], we use the Poisson distribution to model the system failures. Therefore, in the simulation in Section 4 the risk function takes the following form:

$$
r _ {s} ^ {i t} \left(Q _ {s t} ^ {i}\right) = \omega^ {s} \int_ {0} ^ {Q _ {s t} ^ {i}} \left(Q _ {s t} ^ {i} - x\right) \eta_ {s t} ^ {i} e ^ {- \eta_ {s t} ^ {i} \frac {x}{\mu_ {s t} ^ {i}}} d x,\tag{5}
$$

where $\eta _ { s t } ^ { i }$ is resource provider s's system failure frequency in time period t, and $\mu _ { s t } ^ { i }$ is the processing rate of resource i at the resource provider s in time period t.

Hence, the second criterion of each provider can be expressed mathematically as:

$$
\text { Minimize } \sum_ {i = 1} ^ {I} \sum_ {t = 1} ^ {T} r _ {s} ^ {i t} \left(Q _ {s t} ^ {i}\right).\tag{6}
$$

The decision-making objective function of provider s is denoted by U<sup>s</sup>. We can now construct a value function for each provider based on the pro<sup>fi</sup>t and the expected penalty. Therefore, the decision-making problem of provider s can be expressed as:

$$
U ^ {s} = \sum_ {t = 1} ^ {T} \sum_ {b = 1} ^ {B} \sum_ {i = 1} ^ {I} \left(\rho_ {1 s b} ^ {i t *} \times q _ {s b} ^ {i t} - c _ {s b} ^ {i t} \left(q _ {s b} ^ {i t}\right)\right) - c _ {s} \left(Q ^ {1}\right) - \sum_ {i = 1} ^ {I} \sum_ {t = 1} ^ {T} r _ {s} ^ {i t} \left(Q _ {s t} ^ {i}\right)\tag{7}
$$

subject to Eq. (1) and

$$
q _ {s b} ^ {i t} \geq 0, \quad \forall b, i, t.\tag{8}
$$

## 3.2. The behavior of grid service brokers

The brokers play a fundamental role in our model since they are responsible for acquiring resources from providers and delivering services to the users. Therefore, the brokers are involved in transactions with both providers, as well as with users. Let $q _ { b k } ^ { j t }$ denote the quantity of type j service being transacted between broker b and user market k during time period t. We group all transactions associated with broker b and user market k into a column vector $Q ^ { 2 } \in R _ { + } ^ { B K J T }$ In addition, let y<sup>it</sup> denote the amount of broker b's own resource i used during time t. We group all $y _ { b } ^ { i t } s$ into a column vector $Y { \in } R _ { + } ^ { B I I }$

A broker b is faced with certain expenses, which may include, for example, the cost of licensing, the costs of maintenance as well as the cost of using its own resources. We refer collectively to such costs as an operating cost and denote it by $c _ { b } ( Q ^ { 1 } , Q ^ { 2 } , Y )$ . We also assume that there is another type of cost that a broker may face, namely, transaction costs. As mentioned earlier, each broker is involved in transacting with both providers and with users. Therefore, there will be costs associated with each such transaction. In order to capture all possible scenarios, we will use a transaction cost function of a general form. Let $\hat { c } _ { s b } ^ { i t }$ denote the transaction cost associated with broker b transacting with provider s for resource i during time t where we assume that

$$
\hat {c} _ {s b} ^ {i t} = \hat {c} _ {s b} ^ {i t} \left(q _ {s b} ^ {i t}\right), \quad \forall s, b, i, t.\tag{9}
$$

Similarly, let $c _ { b k } ^ { j t }$ denote the transaction cost associated with broker b selling service j to user market k during time t where:

$$
c _ {b k} ^ {j t} = c _ {b k} ^ {j t} \left(q _ {b k} ^ {j t}\right), \quad \forall b, k, j, t.\tag{10}
$$

Note that in both Eqs. (9) and (10) the cost functions are the functions of transaction <sup>fl</sup>ows between the associated tiers of nodes since the links in our model do not represent distinct physical lines, but, rather, they represent the economic transactions from one decisionmaker to another.

Let $\rho _ { 2 b k } ^ { j t }$ denote the price of service j associated with broker b transacting with user market k during time t and let $\rho _ { 2 b k } ^ { j t * }$ denote the price charged in equilibrium. As in the case of providers, we have that each broker b tries to maximize pro<sup>fi</sup>ts, with the objective expressed as:

$$
\begin{array}{l} \text { Maximize } \sum_ {t = 1} ^ {T} \left[ \sum_ {k = 1} ^ {K} \sum_ {j = 1} ^ {J} \rho_ {2 b k} ^ {j t *} \times q _ {b k} ^ {j t} - \sum_ {i = 1} ^ {I} \sum_ {s = 1} ^ {S} \dot {c} _ {s b} ^ {i t} \left(q _ {s b} ^ {i t}\right) - \sum_ {i = 1} ^ {I} \sum_ {s = 1} ^ {S} \rho_ {1 s b} ^ {i t *} \times q _ {s b} ^ {i t} - \sum_ {k = 1} ^ {K} \sum_ {j = 1} ^ {J} c _ {b k} ^ {j t} \left(q _ {b k} ^ {j t}\right) \right] \\ - c _ {b} \left(Q ^ {1}, Q ^ {2}, Y\right) \end{array} \tag {11}
$$

In addition to the criterion of pro<sup>fi</sup>t maximization, we assume that each broker also seeks to minimize the total risk associated with the transactions over the planning horizon T. As in the case of the providers, the broker's risk is de<sup>fi</sup>ned as the expected penalty that the broker will have to pay due to system or network related failures. We can express it as:

$$
r _ {b} ^ {t} (Q _ {b t}) = \omega^ {b} \int_ {0} ^ {Q _ {b t}} (Q _ {b t} - x) f _ {b} ^ {t} (x) d x\tag{12}
$$

where $\begin{array} { r } { Q _ { b t } = \sum _ { k = 1 } ^ { K } \sum _ { j = 1 } ^ { I } q _ { b k } ^ { j t } , \omega ^ { b } } \end{array}$ denotes the unit penalty for tasks that are not completed in time, and $f _ { b } ^ { t } ( x )$ denotes the probability density function that the system fails when processing the $x ^ { t h }$ unit of workload.

## Lemma 2. $\boldsymbol { r } _ { b } ^ { t } ( Q _ { b t } )$ is a convex function of $q _ { b k } ^ { j t }$ .

Proof. The proof is an analog of the proof of Lemma 1. □

Note that our model does not need any assumptions regarding the type of probability distribution. In Section 4, in order to conduct computational studies, following Xie et al. [55], we use the Poisson distribution to model the system failures. Therefore, in the computational studies in Section 4 the risk function takes the following form:

$$
r _ {b} ^ {t} (Q _ {b t}) = \omega^ {b} \int_ {0} ^ {Q _ {b t}} (Q _ {b t} - x) \eta_ {b t} e ^ {- \eta_ {b t} \frac {x}{\mu_ {b t}}} d x\tag{13}
$$

where $\eta _ { b t }$ is node $b ^ { \prime } s$ failure rate in time period t; and $\mu _ { b t }$ is the processing rate of the broker b in time period t.

Hence, the second criterion of each broker can be expressed math ematically as:

$$
\text { Minimize } \sum_ {t = 1} ^ {T} r _ {b} ^ {t} (Q _ {b t}).\tag{14}
$$

In addition, we use $R _ { b } ^ { t } ( Q _ { b t } )$ to denote the probability that broker's b's jobs are completed without any system failure or interruption, which can be expressed mathematically as:

$$
R _ {b} ^ {t} (Q _ {b t}) = \int_ {Q _ {b t}} ^ {\infty} f _ {b} ^ {t} (x) d x = 1 - \int_ {0} ^ {Q _ {b t}} f _ {b} ^ {t} (x) d x\tag{15}
$$

In the case of Poisson distribution, we can rewrite Eq. (15) as follows:

$$
R _ {b} ^ {t} (Q _ {b t}) = e ^ {- \eta_ {b t} \frac {Q _ {b t}}{\mu_ {b t}}}.\tag{16}
$$

Broker b′s decision-making objective function is denoted by $U ^ { b } ,$ and can be expressed as:

$$
\begin{array}{l} \text { Maximize } U ^ {b} = \sum_ {t = 1} ^ {T} \left[ \sum_ {k = 1} ^ {K} \sum_ {j = 1} ^ {J} \rho_ {2 b k} ^ {j t ^ {*}} \times q _ {b k} ^ {j t} - \sum_ {s = 1} ^ {S} \sum_ {i = 1} ^ {I} \hat {c} _ {s b} ^ {i t} \left(q _ {s b} ^ {i t}\right) - \sum_ {s = 1} ^ {S} \sum_ {i = 1} ^ {I} \rho_ {1 s b} ^ {j t *} \times q _ {s b} ^ {j t} - \sum_ {k = 1} ^ {K} \sum_ {j = 1} ^ {J} c _ {b k} ^ {j t} \left(q _ {b k} ^ {j t}\right) \right] \\ - c _ {b} \left(Q ^ {1}, Q ^ {2}, Y\right) - \sum_ {t = 1} ^ {T} r _ {b} ^ {t} (Q _ {b t}) \end{array}
$$

subject to

17

$$
\sum_ {k = 1} ^ {K} \sum_ {j = 1} ^ {J} q _ {b k} ^ {j t} \leq \theta_ {b} ^ {t}, \quad \forall t,\tag{18}
$$

$$
\sum_ {k = 1} ^ {K} \sum_ {j = 1} ^ {J} \kappa_ {i j} q _ {b k} ^ {j t} \leq \sum_ {s = 1} ^ {S} q _ {s b} ^ {i t} + y _ {b} ^ {i t}, \quad \forall i, t,\tag{19}
$$

$$
y _ {b} ^ {i t} \leq \theta_ {b} ^ {i t}, \quad \forall i, t,\tag{20}
$$

$$
y _ {s} ^ {i t} \geq 0, \quad q _ {s b} ^ {i t} \geq 0, \quad q _ {b k} ^ {t} \geq 0, \quad \forall s, k, i, t.\tag{21}
$$

Constraints (18) represent the processing capacity limit. Following the reasoning in Bapna et al. [3], we assume that every type of user service has a known requirement for resources (for example, number of CPU hours and storage units). Constraint (19) guarantees that a broker cannot use more resources than the quantity of resources it has available where $\kappa _ { i j }$ represents the quantity of resource i required by a unit of service type j. Note that our model allows a broker to own and operate resources in which case the <sup>fi</sup>rm combines the roles of broker and resource provider and can directly trade with users. Constraint (20) is the resource capacity constraint where $y _ { s } ^ { i t }$ is the usage of the broker's own resource i in period t and $\theta _ { b } ^ { i t }$ represents the capacity of resource i owned by the broker itself in period t. If a broker does not own resource i we simply let θ<sup>it</sup> be equal to zero.

## 3.3. The behavior of grid market user

We consider K aggregate user markets which can be de<sup>fi</sup>ned based on the users' demand patterns, cost sensitivity of demand, QoS requirements, and timing concerns.

In each market, users can purchase the J types of services offered by the brokers. The users consider not only the prices of the services but also the quality of service (QoS) [29], and the timing of the execution. Moreover, we assume that users are willing to pay more for a service if the broker has superior QoS. In particular, we measure the broker QoS based on its probability to complete a job without disruption. Therefore, the broker's QoS in time period t, is $\pi _ { b } ^ { t } { = } R _ { b } ^ { t } ( Q _ { b t } )$ . We also de<sup>fi</sup>ne, $\beta _ { b } ^ { t } ,$ , the broker's risk perceived by the users as the probability that jobs are not completed in time without disruption, that is, $\beta _ { b } ^ { t } ( Q _ { b t } ) = 1 - R _ { b } ^ { t } ( Q _ { b t } )$

Lemma 3. $\beta _ { b } ^ { t }$ is an increasing function of $q _ { b k } ^ { j t }$

Proof. Based on Eq. (15), we can calculate the <sup>fi</sup>rst derivative of $\beta _ { b } ^ { t } \mathrm { : }$

$$
\frac {\partial \beta_ {b} ^ {t}}{\partial q _ {b k} ^ {j t}} = f _ {b} ^ {t} (Q _ {b t}) > 0. \square
$$

The users can decide how much, in which period, and from which broker they purchase the services in order to minimize their actual cost of services. We denote the total unit cost of service type j the users in market k are willing to pay by $\rho _ { 3 k } ^ { j * }$ . The total demand function of user market k for service j over all periods is $d _ { k } ^ { j } ( \rho _ { 3 k } ^ { j * } )$ .

While making their consumption decisions the users take into account not only the price charged but also the transaction costs associated with obtaining the grid resource as well the penalty cost caused by the risk of service and the penalty cost caused by timing inconvenience. Using Wardrop's <sup>fi</sup>rst principle [25] we can formulate user's cost optimization problem as the following equilibrium condition (cf. [42,46]): for all brokers $b ; b = 1 , . . . , B ;$

$$
\rho_ {2 b k} ^ {j t *} + \hat {c} _ {b k} ^ {j t} \Big (Q ^ {2 *} \Big) + h _ {k} ^ {t} + v _ {k} ^ {t} \Big (\beta_ {b} ^ {t} \big (Q _ {b t} ^ {*} \big) \Big) \left\{ \begin{array}{l l} = \rho_ {3 k} ^ {j *}, & \text {if} \quad q _ {b k} ^ {j t *} > 0 \\ \geq \rho_ {3 k} ^ {j *}, & \text {if} \quad q _ {b k} ^ {j t *} = 0, \end{array} \right.\tag{22}
$$

$$
\sum_ {t = 1} ^ {T} \sum_ {b = 1} ^ {B} q _ {b k} ^ {t} \left\{ \begin{array}{l l} = d _ {k} ^ {j} \Big (\rho_ {3 k} ^ {j *} \Big), & \text {if} \quad \rho_ {3 k} ^ {j *} > 0 \\ \geq d _ {k} ^ {j} \Big (\rho_ {3 k} ^ {j *} \Big), & \text {if} \quad \rho_ {3 k} ^ {j *} = 0, \end{array} \right.\tag{23}
$$

where $\nu _ { k } ^ { t } ( \beta _ { b } ^ { t } ( Q _ { b t } ^ { * } ) )$ represents the unit cost related to the risk of service that incurs to the users, and is an increasing function of $\beta _ { b } ^ { t . }$ and $h _ { k } ^ { t }$ is the unit penalty cost incurred to users in market k in period t due to timing inconvenience.

Conditions (22) state that, in equilibrium, if users at market k purchase service j from broker b in period t, then the price charged by the broker for the service at that time period plus the unit transaction cost and users' costs due to risk and timing inconvenience is equal to the total unit cost of service j that the users are willing to pay. If the price plus the unit transaction cost and the costs due to risk and timing inconvenience is higher than the total unit cost of service the users are willing to pay then there will be no transaction of service j between the broker and market pair at that time period. Conditions (23), in turn, state that for each service type and in each market if the total supply is equal to the total demand then the price the users are willing to pay is positive while if the total supply is greater than the total demand the price is zero.

This form of equilibrium conditions was derived from the cost minimization of the users, and has been widely used in network studies (see, e.g., [12,36,37]). Note that <sup>fi</sup>xed user demand is simply a special case of Eq. (23) where $d \dot { \phi } ( \rho \dot { \bar { \phi } } _ { \ast } )$ is equal to a predetermined demand level, $d \dot { \not | } _ { k 0 } .$ In addition, if users in market k does not need service type j then $\begin{array} { r } { \mathbb { H } _ { k } ^ { j } ( \rho _ { 3 k } ^ { j } ) \equiv 0 } \end{array}$

## 3.4. Equilibrium analysis of the grid computing network

In this section we analyze the equilibrium state of the entire grid computing network market. In particular, we develop a variational inequality formulation governing the grid computing network equilibrium. First, we start with the optimality condition for all resource providers given that they all have similar objectives, see Eq. (7).

We assume that the cost functions are continuously differentiable and convex, and that the resource providers compete in a noncooperative manner in the sense of Nash [38,39]. The optimality conditions for all decision-makers providing the grid resources simultaneously coincide with the solution of the following variational inequality: determine $\left( Q ^ { 1 * } , \bar { \gamma } ^ { * } \right) \in R _ { + } ^ { S B I T + I T S }$ , such that

$$
\begin{array}{l} \sum_ {s = 1} ^ {S} \sum_ {t = 1} ^ {T} \sum_ {b = 1} ^ {B} \sum_ {i = 1} ^ {I} \left[ \bar {\gamma} _ {s} ^ {i t *} + \frac {\partial c _ {s} (Q ^ {1 *})}{\partial q _ {s b} ^ {i t}} + \frac {\partial c _ {s b} ^ {i t} (q _ {s b} ^ {i t *})}{\partial q _ {s b} ^ {i t}} + \frac {\partial r _ {s} ^ {i t} (Q _ {s t} ^ {i *})}{\partial q _ {s b} ^ {i t}} - \rho_ {1 s b} ^ {i t *} \right] \times \left[ q _ {s b} ^ {i t} - q _ {s b} ^ {i t *} \right] \\ \sum_ {s = 1} ^ {S} \sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {I} \left[ \theta_ {s} ^ {i t} - \sum_ {b = 1} ^ {B} q _ {s b} ^ {i t *} \right] \times \left[ \bar {\gamma} _ {s} ^ {i t} - \bar {\gamma} _ {s} ^ {i t *} \right] \geq 0, \forall (Q ^ {1}, \bar {\gamma}) \in R _ {+} ^ {S B I T + I T S}, \end{array}\tag{24}
$$

where $\bar { \gamma } _ { s } ^ { i t } \mathfrak { s }$ are the KKT multipliers for constraint (1), and γ- is the column vector of all $\bar { \gamma } _ { s } ^ { i t } \mathfrak { s }$ .

The inequality (24), which is a variational inequality [16,35] has a meaningful (interesting) economic interpretation. We can see that in equilibrium, if there is a positive amount of the resource transacted from a resource provider to a broker, then the marginal operation and transaction costs plus the marginal risk and the shadow price of the capacity must be equal to the price that the broker is willing to pay for the resource. If the price, in turn, exceeds the marginal costs and risk plus the shadow price then there will be no transaction.

We can rewrite Eq. (24) as the following equivalent from: determine ${ Q } ^ { 1 * } { \in } { \mathcal { K } } ^ { 1 }$ , such that

$$
\begin{array}{l} \sum_ {s = 1} ^ {S} \sum_ {t = 1} ^ {T} \sum_ {b = 1} ^ {B} \sum_ {i = 1} ^ {I} \left[ \frac {\partial c _ {s} (Q ^ {1 *})}{\partial q _ {s b} ^ {i t}} + \frac {\partial c _ {s b} ^ {i t} (q _ {s b} ^ {i t *})}{\partial q _ {s b} ^ {i t}} + \frac {\partial r _ {s} ^ {i t} (Q _ {s t} ^ {*})}{\partial q _ {s b} ^ {i t}} - \rho_ {1 s b} ^ {i t *} \right] \times \left[ q _ {s b} ^ {i t} - q _ {s b} ^ {i t *} \right] \geq 0,   \forall Q ^ {1} \in \mathcal {K} ^ {1}, \\ \text {where} \mathcal {K} ^ {1} \equiv \Bigl \{Q ^ {1}   | q _ {s b} ^ {i t} \geq 0 \quad \forall s, t, i, b \text {and(1)is satisfied} \Bigr \}. \end{array}\tag{25}
$$

As for the case of the providers, all the brokers will try to solve their optimization problem (17). Let γ<sup>t</sup>, λ<sup>it</sup>, and $\tilde { \gamma } _ { b } ^ { i t }$ be the KKT multipliers associated with constraint (18), (19) and (20), respectively. We group $\gamma _ { b } ^ { t } s$ into the column vector γ, group λ<sup>it</sup>s into the column vector λ, and group $\tilde { \gamma } _ { b } ^ { i t } s$ into the column vector $\tilde { \gamma } .$ . We assume that the cost functions are continuously differentiable and convex, and that the brokers compete in a noncooperative manner. Hence, the optimality conditions for all brokers simultaneously can be expressed as the following variational inequality: determine $\left( \dot { Q ^ { 1 * } } , Q ^ { 2 * } , \Lambda ^ { * } , \gamma ^ { * } , \tilde { \gamma } ^ { * } \right) \in \mathcal { K } ^ { 2 }$ satisfying:

$$
\begin{array}{l} \sum_ {s = 1} ^ {S} \sum_ {t = 1} ^ {T} \sum_ {b = 1} ^ {B} \sum_ {i = 1} ^ {I} \left[ \frac {\partial \hat {c} _ {s b} ^ {i t} \left(q _ {s b} ^ {i t *}\right)}{\partial q _ {s b} ^ {i t}} + \frac {\partial c _ {b} \left(Q ^ {1 *} , Q ^ {2 *} , Y ^ {*}\right)}{\partial q _ {s b} ^ {i t}} + \rho_ {1 s b} ^ {i t *} - \lambda_ {b} ^ {i t *} \right] \times \left[ q _ {s b} ^ {i t} - q _ {s b} ^ {i t *} \right] \\ + \sum_ {b = 1} ^ {B} \sum_ {t = 1} ^ {T} \sum_ {k = 1} ^ {K} \sum_ {j = 1} ^ {J} \left[ \frac {\partial c _ {b k} ^ {i t} \left(q _ {b k} ^ {i t *}\right)}{\partial q _ {b k} ^ {i t}} + \frac {\partial c _ {b} \left(Q ^ {1 *} , Q ^ {2 *} , Y ^ {*}\right)}{\partial q _ {b k} ^ {i t}} + \frac {\partial r _ {b} ^ {t} (Q _ {b t} ^ {*})}{\partial q _ {b k} ^ {i t}} - \rho_ {2 b k} ^ {j t *} + \sum_ {i = 1} ^ {I} \kappa_ {i j} \lambda_ {b} ^ {i t *} + \gamma_ {b} ^ {j t *} \right] \\ \times \left[ q _ {b k} ^ {j t} - q _ {b k} ^ {j t *} \right] + \left[ \frac {\partial c _ {b} \left(Q ^ {1 *} , Q ^ {2 *} , Y ^ {*}\right)}{\partial y _ {b} ^ {i t}} + \tilde {\gamma} _ {b} ^ {i t} - \lambda_ {b} ^ {i t *} \right] \times \left[ y _ {b} ^ {i t} - y _ {b} ^ {i t *} \right] \\ + \sum_ {t = 1} ^ {T} \sum_ {b = 1} ^ {B} \sum_ {i = 1} ^ {I} \left[ y _ {b} ^ {i t *} + \sum_ {s = 1} ^ {S} q _ {s b} ^ {i t *} - \sum_ {k = 1} ^ {K} \sum_ {j = 1} ^ {J} \kappa_ {i j} q _ {b k} ^ {j t *} \right] \times \left[ \lambda_ {b} ^ {i t} - \lambda_ {b} ^ {i t *} \right] \\ + \sum_ {t = 1} ^ {T} \sum_ {b = 1} ^ {B} \sum_ {i = 1} ^ {I} \left[ \theta_ {b} ^ {i t} - y _ {b} ^ {i t *} \right] \times \left[ \tilde {\gamma} _ {b} ^ {i t} - \tilde {\gamma} _ {b} ^ {i t *} \right] + \sum_ {t = 1} ^ {T} \sum_ {b = 1} ^ {B} \left[ \theta_ {b} ^ {\mathrm{t}} - \sum_ {k = 1} ^ {K} \sum_ {j = 1} ^ {J} q _ {b k} ^ {j t *} \right] \times \left[ \gamma_ {b} ^ {\mathrm{t}} - \gamma_ {b} ^ {\mathrm{t}} * \right] \geq 0, \\ \forall (Q ^ {1}, Q ^ {2}, \lambda , \gamma , \tilde {\gamma}) \in \mathcal K ^ {- 2}, \\ \mathcal K ^ {- 2} \equiv \Bigl \{\bigl (Q ^ {1}, Q ^ {2}, \lambda , \gamma , \tilde {\gamma} \bigr) | q _ {s b} ^ {i t} \geq 0, q _ {b k} ^ {\mathrm{it}} \geq 0, \lambda_ {b} ^ {\mathrm{it}} \geq 0, \gamma_ {\mathrm{t}} ^ {\mathrm{t}} \geq 0, \tilde {\gamma} _ {\mathrm{t}} ^ {\mathrm{it}} \geq 0,   \forall s, b, k, i, j, t \Bigr \}. \end{array}\tag{26}
$$

The economic interpretation of the broker's optimality conditions is very interesting. The <sup>fi</sup>rst term in Eq. (26) states that if there is a positive amount of resource i transacted between a provider/broker pair at any time period t, that is, $q _ { s b } ^ { i t ^ { * } } > 0 ,$ , then the shadow price of resource i at the broker, $\lambda _ { b } ^ { i t ^ { * } }$ , is equal to the price charged for the service plus the various marginal costs. In addition, the second term in Eq. (27) states that, if users at market k purchase service j from a particular broker $b ,$ that is, $q _ { b k } ^ { i t ^ { * } } > 0 ,$ , then the price charged by broker $b ,$ is equal to the weighted sum of the shadow prices of resources, $\sum { _ { i } ^ { I } } _ { = 1 } ^ { I } \kappa _ { i j } \lambda _ { b } ^ { i t ^ { * } }$ <sup>\*</sup>, plus marginal risks and the shadow price of the capacity as well as the marginal transaction costs in dealing with the users at market k.

We now rewrite Eq. (26) as the following equivalent form: Determine $\left( Q ^ { 1 * } , Q ^ { 2 * } , Y ^ { * } \right) \in \dot { K } ^ { 3 }$ such that

$$
\begin{array}{l} \sum_ {s = 1} ^ {S} \sum_ {t = 1} ^ {T} \sum_ {b = 1} ^ {B} \sum_ {i = 1} ^ {I} \left[ \frac {\partial c _ {s b} ^ {i t} \left(q _ {s b} ^ {i t ^ {*}}\right)}{\partial q _ {s b} ^ {i t}} + \frac {\partial c _ {b} \left(Q ^ {1 *} , Q ^ {2 *} , Y ^ {*}\right)}{\partial q _ {s b} ^ {i t}} + \rho_ {1 s b} ^ {i t ^ {*}} \right] \times \left[ q _ {s b} ^ {i t} - q _ {s b} ^ {i t ^ {*}} \right] \\ + \sum_ {b = 1} ^ {B} \sum_ {t = 1} ^ {T} \sum_ {k = 1} ^ {K} \sum_ {j = 1} ^ {J} \left[ \frac {\partial c _ {b k} ^ {j t} \left(q _ {b k} ^ {j t ^ {*}}\right)}{\partial q _ {b k} ^ {j t}} + \frac {\partial c _ {b} \left(Q ^ {1 *} , Q ^ {2 *} , Y ^ {*}\right)}{\partial q _ {b k} ^ {j t}} + \frac {\partial r _ {b} ^ {t} (Q _ {b t} ^ {*})}{\partial q _ {b k} ^ {j t}} - \rho_ {2 b k} ^ {j t ^ {*}} \right] \times \left[ q _ {b k} ^ {i t} - q _ {b k} ^ {i t ^ {*}} \right] \\ + \sum_ {b = 1} ^ {B} \sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {I} \frac {\partial c _ {b} \left(Q ^ {1 *} , Q ^ {2 *} , Y ^ {*}\right)}{\partial y _ {b} ^ {i t}} \times \left[ y _ {b} ^ {i t} - y _ {b} ^ {i t ^ {*}} \right] \geq 0 \\ \forall (Q ^ {1}, Q ^ {2}, Y) \in \mathcal {K} ^ {3}, \\ \mathcal {K} ^ {3} \equiv \left\{(Q ^ {1}, Q ^ {2}, Y) | q _ {s b} ^ {i t} \geq 0, q _ {b k} ^ {j t} \geq 0, y _ {b} ^ {i t} \geq 0 \forall s, b, k, i, j, t, a n d (1 8), (1 9), a n d (2 0) h o l d \right\} \end{array}\tag{27}
$$

Finally, in equilibrium, conditions (22) and (23) will have to hold for all grid users, which, in turn, can be expressed also as an inequality analogous to those in (25) and (27), and given by: determine $\left( Q ^ { 2 * } , \rho _ { 3 } ^ { * } \right) \in \mathcal { K } ^ { 4 }$ , such that

$$
\begin{array}{l} \sum_ {b = 1} ^ {B} \sum_ {k = 1} ^ {K} \sum_ {j = 1} ^ {J} \sum_ {t = 1} ^ {T} \left[ \rho_ {2 b k} ^ {j t *} + \hat {c} _ {k b} ^ {j t} \left(Q ^ {2 *}\right) + h _ {k} ^ {t} + v _ {k} ^ {t} \left(\beta_ {b} ^ {t} (Q _ {b t} ^ {*})\right) - \rho_ {3 k} ^ {j *} \right] \times \left[ q _ {b k} ^ {j t} - q _ {b k} ^ {j t *} \right] \\ + \sum_ {k = 1} ^ {K} \sum_ {j = 1} ^ {J} \left[ \sum_ {t = 1} ^ {T} \sum_ {b = 1} ^ {B} q _ {b k} ^ {j t} - d _ {k} ^ {j} \left(\rho_ {3 k} ^ {j *}\right) \right] \times \left[ \rho_ {3 k} ^ {j} - \rho_ {3 k} ^ {j *} \right] \geq 0 \forall \left(Q ^ {2}, \rho_ {3}\right) \in \mathcal {K} ^ {4}, \\ \mathcal {K} ^ {4} \equiv \Bigl \{\left(Q ^ {2}, \rho_ {3}\right) \big | q _ {b k} ^ {j t} \geq 0, \rho_ {3 k} ^ {j} \geq 0, \forall b, k, t, j \Bigr \} \end{array}\tag{28}
$$

In equilibrium, the resource <sup>fl</sup>ows that the resource providers transact with the service brokers (intermediaries) must be equal to those that the brokers accept from the resource providers. In addition, the service amounts that are obtained by the users must be equal to the volume that the brokers transact with the users. Hence, the equilibrium <sup>fl</sup>ow and price pattern must satisfy the sum of the optimality conditions (25), (27), and (28), in order to formalize the agreements between tiers of the computational gird network. We now state this formally:

De<sup>fi</sup>nition 1. Grid Network Equilibrium The equilibrium state of the computational grid market network is one where the resource and service <sup>fl</sup>ows between tiers coincide and the <sup>fl</sup>ows and prices satisfy the sum of conditions (25), (27), and (28).

We now establish the following:

Theorem 1. Variational Inequality Formulation The equilibrium conditions governing the computational grid market network are equivalent to the solution of the variational inequality given by: determine $\left( Q ^ { 1 * } , Q ^ { 2 * } , Y ^ { * } , \rho _ { 3 } ^ { * } \right) \dot { \in } { \cal K } ,$ such that

$$
\begin{array}{l} \sum_ {s = 1} ^ {S} \sum_ {b = 1} ^ {B} \sum_ {i = 1} ^ {I} \sum_ {t = 1} ^ {T} \left[ \frac {\partial c _ {s} \left(Q ^ {1 *}\right)}{\partial q _ {s b} ^ {i t}} + \frac {\partial c _ {s b} ^ {i t} \left(q _ {s b} ^ {i t *}\right)}{\partial q _ {s b} ^ {i t}} + \frac {\partial c _ {b} \left(Q ^ {1 *} , Q ^ {2 *} , Y ^ {*}\right)}{\partial q _ {s b} ^ {i t}} + \frac {\partial c _ {s b} ^ {i t} \left(q _ {s b} ^ {i t *}\right)}{\partial q _ {s b} ^ {i t}} + \frac {\partial r _ {s} ^ {i t} \left(Q _ {s t} ^ {i *}\right)}{\partial q _ {s b} ^ {i t}} \right] \times \left[ q _ {s b} ^ {i t} - q _ {s b} ^ {i t *} \right] \\ + \sum_ {b = 1} ^ {B} \sum_ {k = 1} ^ {K} \sum_ {j = 1} ^ {J} \sum_ {t = 1} ^ {T} \left[ \frac {\partial c _ {b k} ^ {i t} \left(q _ {b k} ^ {i t *}\right)}{\partial q _ {b k} ^ {i t}} + \frac {\partial c _ {b} \left(Q ^ {1 *} , Q ^ {2 *} , Y ^ {*}\right)}{\partial q _ {b k} ^ {i t}} + \hat {c} _ {k b} ^ {i t} \left(Q ^ {2 *}\right) + \frac {\partial r _ {b} ^ {t} (Q _ {b t} ^ {*})}{\partial q _ {b k} ^ {i t}} + h _ {k} ^ {t} + v _ {k} ^ {t} (\beta_ {b} ^ {t} (Q _ {b t} ^ {*})) - \rho_ {3 k} ^ {i *} \right] \\ \times \left[ q _ {b k} ^ {i t} - q _ {b k} ^ {i t *} \right] + \sum_ {b = 1} ^ {B} \sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {I} \frac {\partial c _ {b} \left(Q ^ {1 *} , Q ^ {2 *} , Y ^ {*}\right)}{\partial y _ {b} ^ {i t}} \times \left[ y _ {b} ^ {i t} - y _ {b} ^ {i t *} \right] \\ + \sum_ {k = 1} ^ {K} \sum_ {j = 1} ^ {J} \left[ \sum_ {t = 1} ^ {T} \sum_ {b = 1} ^ {B} q _ {b k} ^ {i t} - d _ {k} ^ {i} (\rho_ {3 k} ^ {i *}) \right] \times \left[ \rho_ {3 k} ^ {j}, - \rho_ {3 k} ^ {j *} \right] \geq 0 \forall (Q ^ {1}, Q ^ {2}, Y, \rho_ {3}) \in \mathcal {K}, \\ \end{array}\tag{29}
$$

where

$$
\begin{array}{l} \mathcal {K} \equiv \left\{\left(Q ^ {1}, Q ^ {2}, Y, \rho_ {3}\right) \mid q _ {s b} ^ {i t} \geq 0, q _ {b k} ^ {j t} \geq 0, y _ {b} ^ {i t} \geq 0, \rho_ {3 k} ^ {j} \geq 0 \right. \\ \forall s, b, k, i, j, t a n d (1), (1 8), (1 9), a n d (2 0) a r e s a t i s f i e d \Big \} \end{array}
$$

Proof. Summation of inequalities (25), (27), and (28), yields, after algebraic simpli<sup>fi</sup>cation, the variational inequality (29).

Variational inequality (29) can be written in standard form:

$$
\left\langle F \left(X ^ {*}\right), X - X ^ {*} \right\rangle \geq 0, \forall X \in \mathcal {K},\tag{30}
$$

where $X \equiv ( Q ^ { 1 } , Q ^ { 2 } , Y , \rho _ { 3 } )$ and $F ( X ) \equiv ( F _ { s b } ^ { i t } , F _ { b k } ^ { j t } , F _ { b } ^ { i t } , F _ { k } ^ { j } )$ with indices: $s = 1$ $. . . , S ; i = 1 , . . . , I ; b = 1 , . . . , B ; j = 1 , . . . , J ; k = 1 , . . . , K$ and the speci<sup>fi</sup>c com ponents of F given by the functional terms preceding the multiplication signs in Eq. (29), respectively. The term $\langle \cdot , \cdot \rangle$ denotes the inner product in N-dimensional Euclidean space.f The qualitative properties are provided in the Appendix A.

## 4. Computational studies

In this section we investigate the interactions between QoS/reliability and the decision-making of the players in the computational grid network. In particular, we will utilize a series of numerical examples to study the following questions:

• How do system reliability levels affect the QoS levels of resource providers and brokers under competition?

• How do system reliability levels affect the pro<sup>fi</sup>ts of resource providers and brokers in a competitive market?

• How do system reliability levels in<sup>fl</sup>uence the pricing of services in a competitive environment?

• How do users' service request types, QoS requirements, and timing concerns affect users' behaviors, costs and risks in equilibrium?

• How does the market mechanism allocate resources to satisfy the demands of users?

We use $\eta _ { s t } ^ { i }$ and $\eta _ { b t }$ as the proxies of system reliability levels of resource providers and brokers, respectively. Note that $\eta _ { s t } ^ { i }$ and $\eta _ { b t }$ only depend on the inherent characteristics of the systems of pro viders and brokers. The QoS level, on the other hand, is de<sup>fi</sup>ned as the probability that the tasks are completed in time without any disruptions, which depends not only on ηs but also on the actual workload.

We consider 2 types of resources, 20 resource providers where 10 providers only operate resource 1 and the other 10 providers only operate resource 2. We consider 10 brokers, and 5 user markets. We also consider three periods where periods 1 and 2 are peak periods and period 3 is off-peak period. Since the purpose of the paper is to study the impact of system reliability levels on major decisionmakers in a competitive environment, in the examples we assume that all resource providers have the same cost factors but different system reliability levels, $\eta _ { s t } ^ { i } s .$ We also assume all service brokers have the same cost factors but different system reliability levels, $\eta _ { b t } \mathsf { S } .$ The parameters are speci<sup>fi</sup>ed in Table 4.

Note that in Table 4 the providers are arranged in the decreasing order based on their system reliability levels, η<sup>i</sup> s, with provider 1 of each resource having the most reliable system and provider 10 of each resource having the least reliable system. The brokers are also arranged in the decreasing order based on their system reliability levels, $\eta _ { b t } S ,$ , where broker 1 has the most reliable system and resource provider 10 has the least reliable system.

We consider two types of service products where type 1 service requires 1 unit of resource 1 and one unit of resource 2; and type 2 service requires 1.5 units of recourse 1 and one unit of recourse 2. The aggregate demand markets are de<sup>fi</sup>ned based on the QoS requirements and timing concerns. In particular, we let $\nu _ { k } ^ { t } ( \beta _ { b } ^ { t } ( Q _ { b t } ^ { * } ) ) =$ $a _ { k } ^ { t } \beta _ { b } ^ { t } ( Q _ { b t } ^ { * } )$

The parameters of demand markets are speci<sup>fi</sup>ed in Table 5. The users in market 1 request type 1 service. The inconvenient timing penalties for the users in market 1 for the three periods are: 0, 1, and 100, respectively, which indicates that it is important to execute the jobs in a timely fashion in the <sup>fi</sup>rst two periods. Users in markets 2, 3, and 4, in turn, have identical timing penalty parameters (0, 1, 7) for the three periods, which indicates a moderate level of <sup>fl</sup>exibility. However, users in market 3 request type 2 service product while users in market 4 have higher risk penalty and, thus, is more risk averse. Finally, users in market 5 have no timing preference.

Note that the total capacity of the network over three periods is $3 \times 1 0 \times 1 0 = 3 0 0$ . In these examples, since we want to precisely control the demand levels we assume that the demands are insensitive to prices, and are varied as follows. We <sup>fi</sup>rst de<sup>fi</sup>ne the capacity factor of the network, z, as the ratio between the total demand and the total capacity. We assume that the demand of market 1 is equal to 200×z, and that the demands of markets 2 to 5 are all equal to

Parameter Speci<sup>fi</sup>cation for Resource Providers and Brokers.

<table><tr><td>Notation</td><td>Value</td></tr><tr><td> $c_s(Q^1)$ </td><td>=10 for all resource providers</td></tr><tr><td> $c_{sb}^{it}(q_{sb}^{it})$ </td><td> $=q_{sb}^{it}$  for all provider/broker pairs</td></tr><tr><td> $c_b(Q^1,Q^2,Y)$ </td><td> $=\sum_{t=1}^T\sum_{i=1}^I\sum_{s=1}^S q_{sb}^{lt}+10$  for all brokers</td></tr><tr><td> $\hat{c}_{sb}^{it}(q_{sb}^{it})$ </td><td>=0 for all provider/broker pairs</td></tr><tr><td> $\hat{c}_{bk}^{it}(q_{bk}^{it})$ </td><td> $=q_{bk}^t$  for all broker/market pairs</td></tr><tr><td> $\hat{c}_{bk}^t(Q^2)$ </td><td>=0 for all broker/market pairs</td></tr><tr><td> $\theta_s^{it}$ </td><td>10 for all providers</td></tr><tr><td> $\theta_b^t$ </td><td>10 for all brokers</td></tr><tr><td> $\theta_b^{it}$ </td><td>0 for all brokers</td></tr><tr><td> $\omega_2^s$ </td><td>20 for all providers</td></tr><tr><td> $\omega_2^b$ </td><td>20 for all brokers</td></tr><tr><td> $\mu_{st}^i$ </td><td>0.8 for all providers</td></tr><tr><td> $\mu_{bt}$ </td><td>1 for all brokers</td></tr><tr><td> $\eta_{st}^i$ </td><td>From 0.01 to 0.1 with interval 0.01, e.g.,  $\eta_{1t}^i=0.01$ ,  $\eta_{2t}^i=0.02,...,\eta_{10t}^i=0.1$ </td></tr><tr><td> $\eta_{bt}$ </td><td>From 0.01 to 0.1 with interval 0.01, e.g.,  $\eta_{1t}=0.01$ ,  $\eta_{2t}=0.02,...,\eta_{10t}=0.1$ </td></tr></table>

Table 5  
Parameter speci<sup>fi</sup>cation for aggregate demand markets.

<table><tr><td rowspan="2">Market</td><td rowspan="2">Service type</td><td rowspan="2"> $\alpha_{k}^{t}$ </td><td colspan="3"> $h_{k}^{t}$ </td></tr><tr><td>t=1</td><td>t=2</td><td>t=3</td></tr><tr><td>1</td><td>1</td><td>10</td><td>0</td><td>1</td><td>100</td></tr><tr><td>2</td><td>1</td><td>10</td><td>0</td><td>1</td><td>7</td></tr><tr><td>3</td><td>2</td><td>10</td><td>0</td><td>1</td><td>7</td></tr><tr><td>4</td><td>1</td><td>20</td><td>0</td><td>1</td><td>7</td></tr><tr><td>5</td><td>1</td><td>10</td><td>0</td><td>0</td><td>0</td></tr></table>

25×z. We then vary the capacity factor of the network, z, from 0.6 to 0.9. Note that at each total demand level, the demands that are relatively <sup>fl</sup>exible (demands of markets 2–5) account for one third of the total demand.

The results at different demand levels are shown in Figs. 2 to 12. In order to keep the <sup>fi</sup>gures clean and to demonstrate the trends, we only present the results for brokers and resource providers 1, 3, 5, 8, and 10, respectively. The results for the other decision-makers are consistent with the trends exhibited in the <sup>fi</sup>gures.

## 4.1. Analysis of QoS levels

We now investigate the <sup>fi</sup>rst question raised in the beginning of this section: How do system reliability levels affect the QoS levels of the resource providers and brokers under competition? Fig. 2 shows the QoS levels of brokers with different reliability levels in the three periods. We can see that the QoS levels of brokers with higher system reliability levels (e.g. brokers 1 and 3) are always greater than or equal to those of brokers with lower reliability levels (e.g. brokers 8 and 10). Moreover, when the capacity factor is low the difference of QoS levels between different brokers is relatively small while as the capacity factor gets higher the gaps between the QoS levels become larger. For instance, when the capacity factor=0.6, the QoS level of broker 1 is 0.90; the QoS levels of broker 3 is 0.74; and the QoS levels of brokers 5, 8, and 10 are all equal to 0.71 in period 1. However, when the capacity factor=0.9 the QoS levels of brokers 1 and 2 remain the same while the QoS level of broker 5 decrease to 0.61; and the QoS levels of brokers 8 and 10 both drop to 0.47. In addition, for each broker the QoS level in the off-peak period (period 3) is higher than or equal to the that in the peak periods (periods 1 and 2).

In summary, the QoS levels of brokers at higher demand levels are always less than or equal to those at lower load levels. Moreover, as demand increases the brokers with lower system reliability levels tend to have greater decreases in QoS compared to the brokers with higher system reliability levels.

Figs. 3 and 4, in turn, demonstrate the QoSs of the suppliers for recourses 1 and 2 in the three periods at various load levels, respectively. The trends exhibited in Figs. 3 and 4 are similar to that in Fig. 2: the QoS levels of suppliers at higher demand levels are less than or equal to those at lower demand levels, and as demand increases the suppliers with lower system reliability levels tend to have greater decreases in QoS compared to supplier with higher system reliability levels. In addition, Fig. 3.A and 3.B are identical to 4.A and 4.B while in Fig. 3.C the QoS level of each supplier for resource 1 is less than or equal to that of the supplier for resource 2 with the same reliability factor in Fig. 4.C. The reason is that in our results, the users in market 3 choose to schedule all the demands in period 3. As a consequence, the demands for the two resources are the same in periods 1 and 2; and the demand for resource 1 is higher than that for resource 2 in period 3, which lowers the QoS levels for resource 1 suppliers. Figs. 2 and 3 answered the <sup>fi</sup>rst question raised at the beginning of this section.

![](/api/attachments/F27BPD6H/fulltext/images/b0bdfec2addbc87503f86525a79ddaed0080557488ee6aa25eb16899d09efb21.jpg)

![](/api/attachments/F27BPD6H/fulltext/images/bc1c135fe743e4e84f7c14fabf579f4bc7c6702fb878cb6e9bc3f93fb6af08ea.jpg)  
Fig. 2. QoS levels of brokers.

![](/api/attachments/F27BPD6H/fulltext/images/55beff75ce9126c5c0225985a395abb34056741645536442573067aae2bd464b.jpg)

## 4.2. Analysis of profits

We now investigate the second question raised in the beginning of this section: How do system reliability levels affect the pro<sup>fi</sup>ts of resource providers and brokers in a competitive market? Fig. 5 presents the expected pro<sup>fi</sup>ts of the brokers and the resource providers, respectively. In Fig. 5.A, we observe that the brokers with higher system reliability levels always have higher expected pro<sup>fi</sup>ts than the brokers with lower system reliability levels. In addition, the pro<sup>fi</sup>ts of the brokers also increase as the capacity factor increases. For example, when the capacity factor is equal to 0.6 the brokers' expected pro<sup>fi</sup>ts are equal to 195, 101, 59, 37, and 30, respectively; and when the capacity factor is 0.9 the expected pro<sup>fi</sup>ts of brokers 1, 3, 5, 8, and 10 are equal to 408, 297, 212, 129, and 104, respectively.

Moreover, when users' demands get lower which indicates more intense competition between the brokers, the brokers with lower system reliability levels will suffer a bigger percentage decrease in expected pro<sup>fi</sup>t compared to the brokers with higher reliability levels. For example, when the capacity factor decreases from 0.9 to 0.6, the expected pro<sup>fi</sup>t of broker 1 decreases from 408 to 195 which is a 52% drop while the expected pro<sup>fi</sup>t of broker 10 decreases from 103 to 30 which is a 68% decline.

In summary, the brokers with higher system reliability levels always have higher expected pro<sup>fi</sup>ts than the brokers with lower system reliability levels at all demand levels, and the demand variations have greater impacts on the expected pro<sup>fi</sup>ts of brokers with lower reliability levels than on those of brokers with higher reliability levels.

Fig. 5.B and 5.C, in turn, exhibit the expected pro<sup>fi</sup>ts of the resource providers with different system reliability levels. The trends in Fig. 5.B and 5.C are similar to that in Fig. 5.A: the resource providers with higher system reliability levels always have higher expected pro<sup>fi</sup>ts than those with lower system reliability levels, and the demand variations have bigger impact on the expected pro<sup>fi</sup>ts of providers with lower reliability levels than on those of providers with higher reliability levels. Fig. 5 answers the second questions raised at the beginning of this section.

![](/api/attachments/F27BPD6H/fulltext/images/dd76cfe237975ac8add7ca86f32268c9c57769e23c04575404a9052a0f11fcdd.jpg)

![](/api/attachments/F27BPD6H/fulltext/images/34a3493ce4da5ee5120fef77d7cfd3c827477bbb7f20053ab5db70b8ab2c780f.jpg)  
Fig. 3. QoS levels of resource providers for resource 1.

C) QoS Levels of Providers  
![](/api/attachments/F27BPD6H/fulltext/images/e3c22adfc4c2983ff4756257fd4ddc9aa281cd41d8202e720db6e8b57fce7a4f.jpg)

![](/api/attachments/F27BPD6H/fulltext/images/b6bdad057d6b8cf8efb862fe02e4141422db7db33b7e2ddbc93f4bda45d18d1b.jpg)

![](/api/attachments/F27BPD6H/fulltext/images/c8c26152cf482ca2f8a5276e77b64cb8a9dcd4a9988570b1223bda55f96b6877.jpg)

![](/api/attachments/F27BPD6H/fulltext/images/10ac349e83a9c0182cba73d12091e1e16574dd78ea8d8c5571d1f99d845fe5f9.jpg)  
Fig. 4. QoS levels of resource providers for resource 2.

## 4.3. Analysis of service prices

We now investigate the third question raised in the beginning of the section: How do system reliability levels in<sup>fl</sup>uence the pricing of services in a competitive environment? Figs. 6 and 7 answer the third question by showing the prices of service products 1 and 2 charged by different brokers in the three periods at different demand levels. We observe that in any period the prices of brokers with higher reliability levels are always greater than or equal to the prices of brokers with lower reliability levels. In addition, as the demand increases the price gaps between brokers with different reliability levels become larger. Moreover, we can see that in each period for each broker the price of product 1 is higher than that of product 2 since product 1 requires more resources than product 2 does.

## 4.4. Analysis of users' behaviors, costs, and risks

We now turn to the fourth question raised in the beginning of this section: How do users' service types, QoS requirements, and timing concerns affect users' behaviors, costs and risks in equilibrium? We <sup>fi</sup>rst de<sup>fi</sup>ne the average service cost of users in market $k , \psi _ { k } ,$ , and the average risk of users in market k, ϕ , as follows:

$$
\psi_ {k} = \frac {\sum_ {t = 1} ^ {T} \sum_ {b = 1} ^ {B} \sum_ {j = 1} ^ {J} q _ {b k} ^ {j t} \rho_ {3 k} ^ {j}}{\sum_ {t = 1} ^ {T} \sum_ {b = 1} ^ {B} \sum_ {j = 1} ^ {J} q _ {b k} ^ {j t}},\tag{31}
$$

$$
\phi_ {k} = \frac {\sum_ {t = 1} ^ {T} \sum_ {b = 1} ^ {B} \sum_ {j = 1} ^ {J} q _ {b k} ^ {j t} \beta_ {b} ^ {t}}{\sum_ {t = 1} ^ {T} \sum_ {b = 1} ^ {B} \sum_ {j = 1} ^ {J} q _ {b k} ^ {j t}}.\tag{32}
$$

Fig. 8 exhibits the average costs and risks of users in different markets, and Fig. 9 shows the percentages of demands of markets 1, 2, and 4 scheduled in each period. Note that in equilibrium users in markets 3 and 5 choose to schedule all their demands in the off-peak period (period 3).

![](/api/attachments/F27BPD6H/fulltext/images/3ff8fcaa79c6b7684f0f62ca9bb06372a276619e71b3c8649534f813606dbfe4.jpg)

![](/api/attachments/F27BPD6H/fulltext/images/a1b8b42a211262de907f9e52c3778d832e994f36bfecf1d4c215fb69d1770b89.jpg)  
Fig. 5. Expected pro<sup>fi</sup>ts of the suppliers and brokers.

![](/api/attachments/F27BPD6H/fulltext/images/612befde52b4e859809c0996a5b7db80aed6a115931c5d82c36b2e4928b538ea.jpg)

![](/api/attachments/F27BPD6H/fulltext/images/b5d2e163d1f1058c67cd1e48cc8459af8c2b2c7c2236363ea6aedec04d6bd021.jpg)

![](/api/attachments/F27BPD6H/fulltext/images/12146d3469b6bd224537c4d030e1ef709814700c4fa636c5b8c9c4d0b7a05648.jpg)

![](/api/attachments/F27BPD6H/fulltext/images/d7866e6cc072eab2e98ec44e0a356d2d59f049c0e256d1fe3813dbecf3f27ed0.jpg)  
Fig. 6. Brokers' service prices for product 1.

Fig. 8.A shows the weighted average service costs paid by users in different markets. We can see that the average cost in market 3 is always the highest at all capacity factor levels since users in market 3 purchase type 2 service product which requires more resources. The average cost paid by the users in market 4 is the second highest due to the fact that these users have higher reliability requirement than the other users so that they have to pay a premium to purchase the service with the highest QoS. The average costs paid by users in markets 1 and 2 are close since these users request same service product, and have identical QoS requirements. However, when capacity factor increases the average cost of market 2 becomes lower than that of market 1. The reason is that when the total demand (capacity factor) is high the users in market 2 are able to schedule most of the demand to period 3 (see Fig. 9.B) while the high off-peak period timing penalty of users in market 1 $( h _ { 1 } ^ { 3 } = 1 0 0 )$ prevents them from moving demands to period 3 (see Fig. 9.A). The average cost paid by users in market 5 is the lowest because they have the highest <sup>fl</sup>exibility $( h _ { 5 } ^ { t } = 0 , t = 1 , 2 , 3 )$ , and can always pay the lowest price.

Fig. 8.B, in turn, demonstrates the average risks of users at dif ferent markets. We can see that users in market 1 have the highest average risk since they can only schedule their demands in the peak-periods where the demands are higher and reliability levels are relatively low. The users in market 3 and 5 have the same risks because these users always schedule their demands in the off-peak period (period 3). The users in market 2 schedule a higher percentage of the demand to period 3 as the capacity factor increases (see Fig. 9.B). As a consequence, in Fig. 8.B the average risk of users in market 2 move closer and closer to the risks of users in markets 3 and 5. The average risk of users in market 4 is always the lowest due to the fact that these users have higher α<sup>t</sup> which indicates a higher level of risk aversion.

Fig. 9 exhibits the percentages of demands satis<sup>fi</sup>ed in each period. Fig. 9 only presents the results for markets 1, 2, and 4 since users in market 3 and 5 always schedule all the demands in the off-peak period (period 3). Fig. 9.A shows that users in market 1 schedule approximately half of the demands in each of the <sup>fi</sup>rst and second periods.

![](/api/attachments/F27BPD6H/fulltext/images/14b555ab12ccc480bece089d23241a430c59f96e53e58b8d6e1870bda5187124.jpg)

![](/api/attachments/F27BPD6H/fulltext/images/44de4b1dba20539229b2704e8cf7d344c8d042f32066c5ba7e9003fb7183eaf4.jpg)  
Fig. 7. Brokers' service prices for product 2.

C)Prices of Type 2 Service  
![](/api/attachments/F27BPD6H/fulltext/images/290b4ed3e3f23081395a6fbc5272fd545a0b792aeba4a21365804deb6f4f2513.jpg)

![](/api/attachments/F27BPD6H/fulltext/images/ec7db58def39daae95524a904335255419641e2c3be1033328fca18f2eef261a.jpg)

![](/api/attachments/F27BPD6H/fulltext/images/0080d07242e122c1cf71a7ac166c5660b0ab548225de7cdbe16e82ebba70b6c5.jpg)  
Fig. 8. Average service costs and risks of users at different markets.

The percentage of demand scheduled in period 2 is slightly lower because of the users' small timing penalty associated with period 2. Fig. 9.B shows that as the capacity factor increases users in market 2 schedule higher and higher percentage of the demand to the offpeak period to avoid higher cost and lower QoS in the peak periods.

From Fig. 9.C we can see that as the capacity factor increases the users in market 4 <sup>fi</sup>rst reduce the percentage of demand scheduled in period 3, and when the capacity factor approaches 0.9 they start to increase the percentage of demand executed in period 3. The reason is as follows. Since the users in market 4 are the most risk averse they tend to purchase services from the most reliable brokers. Indeed, they <sup>fi</sup>rst purchase the service from the most reliable broker (broker 1) in period 3 till broker 1 reaches its maximum capacity in period 3. Then the users in market 4 start to purchase services from broker 1 in periods 1 and 2. As the capacity factor (total demand) increases the users in market 4 acquire more and more services from broker 1 in periods 1 and 2 which reduces the percentage of the demand executed in period 3. However, as the demand factor approaches 0.9 the product prices of the most reliable broker (broker 1) in the peak periods become so high that the users in market 4 cannot afford to purchase a higher percentage from broker 1. As a consequence, these users start to acquire the service from the second most reliable broker in period 3 which, as we can see from Fig. 9.C, increases the percentage of their demands executed in period 3.

![](/api/attachments/F27BPD6H/fulltext/images/7b1ab4a934d8ef225a1c21e1011076f761f95d19c060bd52efc640bbba931904.jpg)

Figs. 8 and 9 answer the fourth question raised at the beginning of this section. Our results also show that heterogeneous users with different service types, timing concerns, and QoS requirements exhibit very different behaviors under competitive environments.

## 4.5. Analysis of network resource allocation

We now investigate the <sup>fi</sup>fth question raised in the beginning of this section: How does the market mechanism allocate resources to meet demands from users? Fig. 10 shows the workloads of brokers in each period at different demand levels. First, when user demands rise the workload of every broker increases until it reaches the broker's capacity. Moreover, we can see that the workloads of brokers with higher system reliability levels are always greater than or equal to those of brokers with lower reliability levels. This trend indicates that if costs are equal the market mechanism will make the brokers with higher system reliability levels take more demand in the network.

![](/api/attachments/F27BPD6H/fulltext/images/4009d4dd9c5639216a1faa2504419d56ffc9180dd84c4386874279100026e6cf.jpg)  
Fig. 9. Percentages of Demands Executed in Different Time Periods.

C)Percentages of the Demand  
![](/api/attachments/F27BPD6H/fulltext/images/2fc881aca378ff7260c240b12e6fe54163ba9efc4707afcbb08321652b636d89.jpg)

![](/api/attachments/F27BPD6H/fulltext/images/52bbef1913f29f86b6dd94b87e8f918cc71c8b9e081049b5c9cb7c96f2f7021e.jpg)

![](/api/attachments/F27BPD6H/fulltext/images/eae3118db337e7b081dba09e177a326565e394781788c1152f13144a9228f369.jpg)  
Fig. 10. Workloads of brokers.

![](/api/attachments/F27BPD6H/fulltext/images/714b022d12a8584cbe2a3d29a4af20ed4a7cb07e32748c517cb7ce9c68adf409.jpg)

Figs. 11 and 12, in turn, present the workloads of service providers in each period at different demand levels. The trends exhibited in Figs. 11 and 12 are similar to that in Fig. 10, which implies that if costs are equal the market mechanism will make the service suppliers with higher system reliability levels contribute more resources to the network. Figs. 11 and 12 answered the last question raised at the beginning of this section.

## 5. Managerial insights

Our results reveal important insights regarding reliability, QoS, pricing, and pro<sup>fi</sup>tability for policy makers, managers as well as users.

For policy makers, our analysis shows that in a healthy competitive market, decentralized decision-making can ef<sup>fi</sup>ciently allocate resources with consideration of system reliability. In particular, if suf<sup>fi</sup>cient information regarding <sup>fi</sup>rm's reliability is accessible to market participants and users, the market mechanism can <sup>fi</sup>rst automatically dispatches <sup>fi</sup>rms with more reliable systems. Moreover, multiple dimensions of service requests, such as, resource requirements, timing requirements, and QoS requirements can be ef<sup>fi</sup>ciently priced in the market equilibrium, which send right economic signals to the users. The heterogeneous users, who may exhibit very different behaviors, are able to optimally achieve their own goals under this market mechanism. We also <sup>fi</sup>nd that <sup>fl</sup>exibility has a value, that is, for users who request same services certain timing <sup>fl</sup>exibility can not only reduce the cost but also lower the risk. It is worth noting that since “cloud computing relies on Grid computing as its backbone and infrastructure support” Foster et al. [17], our results also shed light on the development of the rapidly emerging market for cloud computing.

For managers, reliability and QoS are critical for the success of business. Our research reveals several important insights regarding reliability, QoS, and pro<sup>fi</sup>tability. First, our results show that higher network demand tends to decrease QoS. However, the QoS levels of the <sup>fi</sup>rms with lower system reliability are more sensitive to the increase of the total demand. As load increases the gaps between the QoS levels of more reliable <sup>fi</sup>rms and less reliable <sup>fi</sup>rms become greater, which suggests that as the whole market grows bigger managers invest more to improve the <sup>fi</sup>rms' system reliability since the competitive advantage of higher system reliability will become more prominent.

![](/api/attachments/F27BPD6H/fulltext/images/57ad327945f5c1d0deeb4719454a722b9fa7a0da0f07cfd06d39e390eead1f4c.jpg)

![](/api/attachments/F27BPD6H/fulltext/images/b0e76b28c5820702225ce3d10c470ac19af451f8d5e3e4437bc96eb70163fa29.jpg)  
Fig. 11. Workloads of resource providers for resource 1.

C)Workloads of Providers  
![](/api/attachments/F27BPD6H/fulltext/images/06e2baa72a5a9beea97d6513aaa8d9ef14eb7ce6df4a135365d13e4bf57055f8.jpg)

![](/api/attachments/F27BPD6H/fulltext/images/effe185158d5d22c610db587896b18f4e9fcd3def8131b93aa43254539c800c9.jpg)

![](/api/attachments/F27BPD6H/fulltext/images/6a0e91b8d124c001c5ff2371d6a5e843ce06d3eb133cce469dfd0f5bf29c2b16.jpg)  
Fig. 12. Workloads of resource providers for resource 2.

![](/api/attachments/F27BPD6H/fulltext/images/fec07afcfa0c1b376b4fc65c430e9022708c8fdc0c117e841ea77a1873863f7c.jpg)

Second, the results also demonstrate that the higher the system reliability the higher the expected pro<sup>fi</sup>t for the <sup>fi</sup>rm. Moreover, the pro<sup>fi</sup>ts of <sup>fi</sup>rms with higher system reliability are less sensitive to the variations of demands compared to the systems with lower system reliability. Such results imply that if managers invest more in reliability the earnings will be higher and more stable.

Third, our analysis shows that, under competition, as the overall demand increases the price gaps between brokers with different reliability levels become larger, which is indicative that when the market grows bigger the users are more willing to pay a greater premium for higher QoS. The information helps manages decide the timing of upgrading the system reliability and changing the pricing strategy to differentiate the service in the competition.

## 6. Conclusions, insights, and future research

In this paper, we proposed a novel approach to the modeling and analysis of grid computing markets. In particular, we consider QoS, reliability, and risk management in a multiple criteria, multiple resource, multiple decision-maker and multiperiod grid computing network optimization framework. The proposed framework which is based on network equilibrium theory, allows for explicit modeling of decentralized decision-making behaviors, the maximization of net pro<sup>fi</sup>t, and the minimization of risk, of the market participants. This research differs from the recent models [3,6,48,51,52] in that, <sup>fi</sup>rst and foremost, we consider several different types of decision makers and model their behavior and interactions explicitly. Second, we introduce risk management into the decision making process by analyzing the decision-marker's reliability and QoS requirement. Finally, the proposed framework provides the tools for computing ef<sup>fi</sup>cient resource allocation patterns as well as equilibrium price patterns based on demand, supply, cost structure, QoS and reliability of the grid computing network.

In addition, we illustrated both the model and computational procedure through computational studies. The grid computing network market equilibrium approach, developed in this paper, allows us to investigate <sup>fi</sup>ve questions regarding reliability, QoS, pricing, user behaviors, resource allocation, and pro<sup>fi</sup>tability, which revealed important insights for managers, policy makers, as well as users.

In conclusion, the grid computing network market equilibrium approach, developed in this paper, permits one to investigate the interactions between heterogenous decision-makers in the network. It allows decision makers to consider not only the relationships among service price, QoS, reliability and risk, but also cooperative and/or non-cooperative behaviors of other decision-makers in the grid computing network market.

This research can be extended in several directions. For example, empirical analysis can be conducted based on our model to reveal more behavioral and managerial insights using real data. Additionally, our model can be extended to consider market power and to further study brokers' market differentiation strategies based on their QoS levels.

## Appendix A. Supplementary data

Supplementary data to this article can be found online at doi:10. 1016/j.dss.2011.10.012.

## References

[1] D. Abramson, R. Buyya, J. Giddy, A computational economy for grid computing and its implementation in the nimrod-g resource broker. Future Generatior Computer Systems 18 (2002) 1061–1074.

[2] F. Aymerich, G. Fenu, S. Surcis, An approach to a cloud computing network, Proceedings of IEEE Applications of Digital Information and Web Technologies, IEEE, Ostrava, Czech Republic, 2008, pp. 113–118.

[3] R. Bapna, S. Das, R. Gar<sup>fi</sup>nkel, J. Stallaert, A market design for grid computing, INFORMS Journal on Computing 20 (2008) 100–111.

[4] F. Berman, A. Chien, K. Cooper, J. Dongarra, I. Foster, D. Gannon, L. Johnson, K. Kennedy, C. Kesselman, J. Mellor-Crummey, D. Reed, L. Torczon, R. Wolski, The grads project: software support for high-level grid application development, International Journal of High-Performance Computing Applications 14 (2001) 327–344.

[5] R. Buyya, Biogrid. virtual lab tools for data intensive computing on grid: drug design case study, http://www.buyya.com/talks/biogrid.ppt 2001.

[6] R. Buyya, Economic-based Distributed Resource Management and Scheduling for Grid Computing, Ph.D. thesis, Monash University, Melbourne, Australia, 2002.

[7] R. Buyya, D. Abramson, J. Giddy, H. Stockinger, Economic models for resource management and scheduling in grid computing, Concurrency and Computation: Practice and Experience 14 (2002) 1507–1542.

[8] R. Buyya, M. Murshed, D. Abramson, S. Venugopal, Scheduling parameter sweep applications on global grids: a deadline and budget constrained cost-time optimization algorithm, Software-Practice and Experiences 35 (2005) 491–512.

[9] R. Buyya, D. Abramson, J. Giddy, Nimrod/g: An architecture for a resource management and scheduling system in a global computational grid, in: Proceedings of 4th International Conference on High Performance Computing, 2000.

[10] L. Chunlin, L. Layuan, Qos based resource scheduling by computational economy in computational grid Information Processing Letters 98 (2006) 119–126

[11] P. Coddington, Discworld, virtual data grids and grid applications, http://www. gridbus.org/ozgrid/DiscWorld.ppt/ 2002.

[12] J. Cruz, A. Nagurney, T. Wakolbinger, Financial engineering of the integration of global supply chain networks and social networks with risk management, Naval Research Logistics 53 (2006) 674–696.

[13] A. Dogan, F. Ozguner, Scheduling independent tasks with qos requirements in grid computing with time-varying resource prices, Lecture Notes in Computer Science, vol. 2536, Springer, Berlin, 2002, pp. 58–69.

[14] C.L. Dumitrescu, I. Foster, Gruber: a grid resource usage sla broker, Proceedings of the 11th International European Parallel Computing Conference, Springer, Berlin, 2005, pp. 465–474.

[15] C. Ernemann, Economic scheduling in grid computing, Proceedings of 8th International Workshop Job Scheduling Strategies for Parallel Processing, Lecture Notes in Computer Science, UK, 2002, pp. 128–152.

[16] F. Facchinei, J.S. Pang, Finite-Dimensional Variational Inequalities and Complementarity Problems, Springer-Verlag, New York, NY, 2003.

[17] I. Foster, Z. Yong, I. Raicu, S. Lu, Cloud computing and grid computing 360-degree compared, Grid Computing Environments Workshop, IEEE, Austin, Texas, USA, 2008, pp. 1–10.

[18] Gartner, Gartner says saas revenue within the enterprise application software market to total \$9.2 billion in 2010, http://www.gartner.com/it/page.jsp?id=1492814 2010.

[19] Globus.org, Globus alliance, http://www.globus.org 2011.

[20] S. Grid, Sun grid computing utility. sun microsystems, http://www.network.com 2006.

[21] E. Huedo, R.S. Montero, I.M. Llorente, Evaluating the reliability of computational grids from the end user's point of view, Journal of Systems Architecture 52 (2006) 727–736.

[22] S. Hwang, C. Kesselman, Grid work<sup>fl</sup>ow: a <sup>fl</sup>exible failure handling framework for the grid, Journal of Grid Computing 3 (2003) 251–272.

[23] I. Tsunamic Technologies, Cluster computing on demand, http://www.tsunamic technologies.com/services/services.htm 2006.

[24] D.E. Irwin, L.E. Grit, J.S. Chase, Balancing risk and reward in a market-based task service, Proceedings of the 13th International Symposium of High Performance Distributed Computing (HPDC13), Honolulu, HI, 2004.

[25] J.G. Wardrop, Some theoretical aspects of road traf<sup>fi</sup>c research, in: Proceedings of the Institute of Civil Engineers PART II, 1952.

[26] Y. Jiang, G. Xing, A grid model design of service-oriented, Proceedings of the 2008 International Symposium on Intelligent Information Technology Application Workshops, IEEE Computer Society, Washington, DC, USA, 2008, pp. 228–231.

[27] H. Jin, X. Shi, W. Qiang, D. Zou, Dric: dependable grid computing framework, IEICE Transactions on Information and Systems E89-D, 2006, pp. 612–622.

[28] K. Golconda, F. Ozguner, A comparison of static qos based scheduling heuristics for ameta-task with multiple qos dimensions in heterogeneous computing, in: Proceedings of the 18th International Parallel and Distributed Processing Symposium, 2004.

[29] K.H. Kim, R. Buyya, J. Kim, Imprecise computation grid application model for <sup>fl</sup>exible market-based resource allocation, in: Proceedings of the 6th IEEE International Symposium on Cluster Computing and the Grid (CCGrid 2006), vol. 1, 2006, p. 5.

[30] S.D. Kleban, S.H. Clearwater, Computation-at-risk: assessing job portfolio management risk on clusters, Proceedings of the 18th International Parallel and Distributed Processing Symposium JEEE Computer Society Press 2004 pp. 254–260

[31] S.D. Kleban. S.H. Clearwater. Computation-at-risk: emploving the grid for computational risk management, Proceedings of the 18th IEEE International Conference on Cluster Computing, IEEE Computer Society Press, 2004, pp. 347–352.

[32] G. Kola, T. Kosar, M. Livny, Fault in large distributed systems and what we can do about them, Proceedings of the Euro-Par 2005LNCS, vol. 3648, Springer-Verlag, 2005, pp. 442–453.

[33] Legion, A world wide virtual computer. university of virginia, http://legion.virginia. edu 2007.

[34] M. Lin, Z. Lin, A cost-effective critical path approach for service priority selections in grid computing economy, Decision Support Systems 42 (2006) 1628–1640.

[35] A. Nagurney, Network Economics: A Variational Inequality Approach, Kluwer Academic Publishers, Dordrecht, The Netherlands, 1999.

[36] A. Nagurney, K. Ke, Financial networks with intermediation: risk management with variable weights, European Journal of Operational Research 172 (2006) 40–63.

[37] A. Nagurney, L. Zhao, Variational inequalities and networks in the formulation and computation of market equilibria and disequilibria: The case of direct demand functions, Transportation Science 27 (1993) 4–15.

[38] J.F. Nash, Equilibrium points in n-person games, Proceedings of the National Academy of Sciences 36 (1950) 48–49.

[39] J.F. Nash, Noncooperative games, Annals of Mathematics 54 (1951) 286–298.

[40] F. Popovici, J. Wilkes, Pro<sup>fi</sup>table services in an uncertain world, Proceedings of the 2005 ACM/IEEE conference on Supercomputing, IEEE Computer Society, Washington, DC, USA, 2005, p. 36.

[41] O. Regev, N. Nisan, The popcorn market — an online market for computational resources, Proceedings of the First International Conference On Information and Computation Economies, ACM Press, Charleston, SC, 1998, pp. 148–157.

[42] P.A. Samuelson, Spatial price equilibrium and linear programming, American Economic Review 42 (1952) 293–303.

[43] K. Seymour, A. YarKhan, S. Agrawal, J. Dongarra, Grid computing and new frontiers of high performance processing, Grid Computing and New Frontiers of High Performance Processing, Elsevier, 2005, pp. 33–51.

[44] G.J. Stigler, The economics of information, Journal of Political Economy 69 (1961) 213–225.

[45] G. Stuer, K. Vanmechelen, J. Broeckhove, A commodity market algorithm for pricing substitutable grid resources, Future Generation Computer Systems 23 (2007) 688–701.

[46] T. Takayama, G.G. Judge, Spatial and Temporal Price and Allocation Models, North-Holland, Amsterdam, The Netherlands, 1971.

[47] U. Computing, Utility computing. sun microsystems, http://www.sun.com/service sungrid/overview.jsp 2006

[48] C.A. Waldspurger, T. Hogg, B. Huberman, J. Kephart, S. Stornetta, Spawn: a distributed computational economy, IEEE Transactions on Software Engineering 18 (1992) 103–117.

[49] O. Williamson, Markets and Hierarchies: Analysis and Antitrust Implications, Free Press, New York, NY, 1975.

[50] O. Williamson, The Economic Institutions of Capitalism: Firms, Markets, Relational Contracting, Free Press, New York, NY, 1985.

[51] R. Wolski, N. Spring, J. Hayes, The network weather service: A distributed resource performance forecasting service for metacomputing, Journal of Future Generation Computing Systems 15 (1999) 757–768.

[52] R. Wolski, J. Plank, J. Brevik, G-commerce. Building computational marketplaces for the computational Grid, Technical Report UT-CS-00-439, University of Tennessee, 2000.

[53] R. Wolski, J. Plank, J. Brevik, T. Bryan, Analysing market-based resource allocation strategies for the computational grid, International Journal of High-Performance Computing Applications 15 (2001) 258–281.

[54] R. Wolski, J. Brevik, J.S. Plank, T. Bryan, Grid resource allocation and control using computational economies, Grid Computing: Making the Global Infrastructure a Reality, John Wiley & Sons, 2003, pp. 747–772.

[55] M. Xie, K. Poh, Y. Dai, Computing Systems Reliability: Models and Analysis, Springer-Verlag, New York, NY, 2004.

[56] C.S. Yeo, R. Buyya, Managing risk of inaccurate runtime estimates for deadline constrained job admission control in clusters, ICPP'06: Proceedings of the 2006 International Conference on Parallel Processing, IEEE Computer Society, Washington, DC, USA, 2006, pp. 451–458

[57] J. Zhang, S. Bandyopadhyay, S. Piramuthu, Real option valuation on grid computing, Decision Support Systems 46 (2008) 333–343.

Jose M. Cruz is an Assistant Professor of Operations and Information Management in the School of Business. University of Connecticut. His current research interests include complex decision-making on network systems (international <sup>fi</sup>nancial networks, global supply chain networks, social and knowledge networks, and grid computing networks), corporate Social responsibility and risk management. His research has appeared in European Journal of Operational Research, Naval Research Logistics, Environment & Planning B, International Journal of Production Research, International Journal of Production Economics, Decision Support Systems, Mathematical and Computer Modelling, Computational Management Science, Quantitative Finance, and other journals and book chapters.

Zugang (Leo) Liu is an Assistant Professor of Business Administration in the Pennsylvania State University — Hazleton. His main research interest concerns decision making on complex network systems including global supply chain networks, energy and power networks, <sup>fi</sup>nancial networks, transportation networks, and grid computing networks. His research has appeared in Naval Research Logistics, Journal of Banking and Finance, Transportation Research D, Transportation Research E, Mathematical and Computer Modelling, Computational Management Science, and other journals and book chapters.

---
otero_id: 16280
otero_key: "2UE87NCT"
title: "The role of centrality in ambulance dispatching"
authors: "Seokcheon Lee"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.05.036"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The role of centrality in ambulance dispatching

Seokcheon Lee ⁎

School of Industrial Engineering, Purdue University, 315 N. Grant St., West Lafayette, IN, USA

## a r t i c l e i n f o

Article history: Received 12 September 2011 Received in revised form 10 May 2012 Accepted 20 May 2012 Available online 26 May 2012

Keywords: Ambulance dispatching Centrality Sensitivity analysis Weight on centrality Choice of centrality measure

## a b s t r a c t

An ambulance dispatching policy, Centrality policy, is proposed in an effort to reduce the response time in demanding emergency situations such as in natural disasters, based on the notion of centrality from the study on complex networks. The nearest neighbor (NN) policy prioritizes the emergency calls by closeness and it has been known effective in the literature. The NN policy is evolved into the Centrality policy by prioritizing the calls based on the centrality in addition to the closeness. The centrality enables to capture the ef<sup>fi</sup>ciency of a call site in reaching out other current and future calls thus secure the long-term performance beyond the immediate performance pursued by the NN policy. Two parameters are associated with the Centrality policy: weight on centrality and choice of centrality measure. An extensive simulation-based sensitivity analysis is conducted on the algorithmic parameters to examine the role of centrality in ambulance dispatching. The analysis evidences the potential of centrality consideration in reducing the response time beyond the NN policy, given that these parameters are appropriately chosen.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Emergency medical service (EMS) provides pre-hospital treatments to those in need of urgent medical care. The response time in EMS is the time taken to reach the patient after an emergency call is received, and it is of major concern since it might mean the difference between life and death of the patients. Ambulance dispatchers assign appropriate ambulances to the calls such that the response time is minimized. A dispatching decision can be either call-initiated or ambulanceinitiated. In call-initiated decisions, a newly arriving call <sup>fi</sup>nds idle units (ambulances) thus initiates the decision of selecting a unit among the idle units. On the other hand, if the calls cannot be immediately assigned, they start being queued, and a unit that has just got freed has to choose a call among those waiting thereby initiating the dispatching decision.

The relevance of the two types of dispatching decisions depends on the busyness of the system. Call-initiated decisions are more relevant in routine emergency scenarios where the system load is relatively low, while in high load conditions the ambulance-initiated decisions play the primary role. This research concerns the ambulance-initiated dispatching decisions, in an effort to help respond effectively to the catastrophic natural disasters that recent years have evidenced. According to the Centre for Research on the Epidemiology of Disasters (http://cred.be/), in 2010 alone, 373 natural disasters killed over 296,800 people and affected nearly 208 million others.

One distinct characteristic of the dispatching problem in EMS is that the hospitals serve as hubs of the service as the patients are transferred to hospital. It is also important to recognize the fact that it is not always necessary to transfer the patients to hospital. The actual percentage of essential emergency calls that require transferring to hospital is only 25% in the United States [6]. Therefore, it is highly possible that a unit continues serving multiple calls before heading for a hospital. Various factors would be associated with the probability of transferring to hospital, including the resource scarcity, information uncertainty, crew expertise, and nature of catastrophic event, which essentially differ in space and time.

The objective of this research is to provide an ambulance-initiated dispatching policy in an effort to help ambulance dispatchers to make effective decisions in demanding emergency situations. The dispatching problem under consideration has not been addressed in the literature to the best of the author's knowledge. However, the static version of the problem with a single unit and with the probability of transferring to hospital equal to zero, has been studied under the name of Travelling Repairman Problem (TRP) or Minimum Latency Problem (MLP). The objective of TRP is to <sup>fi</sup>nd a route that, for a given set of customer locations, minimizes the total response time of customers rather than the total traveling time that is usually pursued by the well-known Vehicle Routing Problems (VRPs). The TRP is known NP-Hard [24], and several researchers have proposed heuristic methods [2,13] or exact methods for special cases [1,12,19,26].

The D-TRP is the dynamic version of the TRP where the requests for service arrive stochastically in random locations. Bertsimas and van Ryzin [5] proposed several dispatching policies for the D-TRP: FCFS (First Come First Served), SQM (Stochastic Queue Median), PART (PARTitioning), TS (Traveling Salesman), SFC (Space Filling

Curve), and NN (Nearest Neighbor) (refer to [5] for the details of the policies). In their simulation study, the NN policy, which is to serve the closest customer, signi<sup>fi</sup>cantly outperforms other policies in all different low and high load conditions except that the SQM policy is slightly better in very-low load conditions.

Another special case of the dispatching problem under consideration is when there are one hospital and one unit, and the probability of transferring to hospital is one. This system mimics the classical M/ G/1 queue and the shortest processing time (SPT) <sup>fi</sup>rst rule, which can be translated into the NN policy, is known to be optimal for this queuing system [9]. From the survey so far, the NN policy, though it is computationally simple, can be deemed to be effective across all different scenarios under consideration thus it can potentially serve as a dispatching policy in the demanding emergency situations.

However, the NN policy, which prioritizes calls by closeness, only tries to minimize each current response time without taking into account longterm consequences. This study develops a novel ambulance-initiated dispatching policy, Centrality policy, which prioritizes calls based on the socalled centrality (i.e. give a higher priority to the call that is more centrally located with respect to other calls) in addition to the closeness. The centrality, adopted from the study on complex networks, represents the importance of a node in the operational ef<sup>fi</sup>ciency of the network [4], and there exist various measures of centrality. The centrality is used in this dynamic ambulance dispatching problem to compute the ef<sup>fi</sup>ciency of a call site in reaching out other calls, thus enabling to secure the long-term performance.

The Centrality policy has two algorithmic parameters, weight on centrality and choice of centrality measure, which enable the policy to be <sup>fl</sup>exibly applicable to various scenarios. An extensive simulationbased sensitivity analysis is conducted on the algorithmic parameters to examine the role of centrality in ambulance dispatching. The analysis evidences that the centrality consideration, upon the right selection of the parameters, can signi<sup>fi</sup>cantly reduce the average as well as the variation of response time beyond the NN policy which is presumable to be effective across all different scenarios as discussed above. Therefore, the Centrality policy, despite its simplicity, is capable of effectively supporting the decisions of ambulance dispatchers in various demanding emergency situations requiring real-time decision making.

The rest of this paper is organized as follows. Section 2 introduces the Centrality policy. The policy and its parameters are evaluated and analyzed in various scenarios in Sections 3 and 4. Finally Section 5 concludes this work and discusses future work.

## 2. The Centrality policy

An ambulance-initiated dispatching policy is devised in this section that is <sup>fl</sup>exibly applicable to various demanding emergency situations. The NN (Nearest Neighbor) policy, dispatching the freed unit to the closest call site, is a policy that can potentially be used in such situations. However, one problematic aspect of the NN policy is that it myopically pursues only the immediate performance without taking into account the long-term consequences. The Centrality policy designed here incorporates the principle of centrality from the study on complex networks, thereby securing the long-term performance.

## 2.1. The policy

The study of complex networks is an active area of scienti<sup>fi</sup>c research on large-scale real-world networks. One principal thrust in this area has been the identi<sup>fi</sup>cation of the structural properties that are common to many real networks. Node centrality in a network indicates the importance of a node in the operational ef<sup>fi</sup>ciency of the network, and various measures of centrality have been de<sup>fi</sup>ned in an effort to identify the common properties in the distribution of node centrality (Several relevant measures of centrality will be detailed in Section 2.2). The node centrality is used as a decision principle for the dynamic ambulance dispatching problem at hand. When an ambulance gets freed, a network can be constructed where nodes represent waiting calls that have not been assigned to any unit and an edge between every pair of calls has a value of distance between the two call sites connected by the edge. The centrality of a call computed upon this call network can be interpreted as the ef<sup>fi</sup>ciency of the call in reaching other calls or the density of calls around the call with respect to the geographical call distribution over the service area. When calls are prioritized by the centrality and a unit is dispatched to the most central call, the unit will be given the opportunity, after the completion of the immediate service, to serve the other calls around it at the maximum rate of completion.

The centrality also contributes to the preparedness for future calls. The geographical distribution of current calls re<sup>fl</sup>ects the call arrival pattern over the service area. Therefore, when units are positioned according to the centrality (computed upon the network of current calls), they would occupy the regions with high call rates and consequently become able to quickly respond to the calls arriving in the future, thus being well-prepared. The centrality, therefore, implies the ef<sup>fi</sup>ciency of a call site in serving the current as well as future calls, and the centrality consideration in the dispatching decisions is expected to synergistically escalate the completion rate.

However, if calls are prioritized only by the centrality, the units would travel excessively just to reposition themselves in central nodes without enough exploitation of calls in vicinity. Therefore, it is undesirable to use the centrality alone for the dispatching decision and the centrality has to be combined with a measure that provides the capability of local exploitation. The closeness that is used in the NN policy is an appropriate measure as it enables to pursue minimizing each current response time. The NN policy is evolved into the Centrality policy by prioritizing calls based on the centrality in addition to the closeness, thereby being equipped with both global exploration capability and local exploitation capability. The Centrality policy is presented in four steps as follows.

## 2.1.1. The Centrality policy

i. When an ambulance gets freed, identify all unassigned calls U. ii. Compute centrality $c _ { u }$ of each call u∈U upon the network of calls U with the edge between every pair of calls having the value of distance between them (alternative centrality measures will be detailed in Section 2.2).

iii. Compute goodness $f _ { u }$ of each call u∈U based on two quantities: 1) expected (shortest) response time $t _ { u }$ to call u and 2) centrality $c _ { u }$ of call u weighted by w (≥0).

$$
f _ {u} = \frac {c _ {u} ^ {w}}{(1 + t _ {u})}
$$

iv. Dispatch the freed unit to the call $u ^ { * }$ that maximizes the goodness.

$$
u ^ {*} = \operatorname * {a r g   m a x} _ {u \in U} f _ {u}
$$

## 2.2. Algorithmic parameters

Two parameters are associated with the Centrality policy: weight on centrality w (numerical parameter) and centrality measure $c _ { u }$ (functional parameter). Note that the Centrality policy is exactly the same as the NN policy when w=0 because then the goodness $f _ { u }$ becomes a function of the closeness only; however, when the weight is positive the policy incorporates the centrality into the decision by the extent corresponding to the weight. As mentioned before, one crucial characteristic of the ambulance dispatching is the uncertainty involved in the need for transferring the patient to hospital. The choice of the weight value will be affected by the probability of transferring as it determines the relevance of the centrality consideration, i.e. the centrality will be more relevant in lower probability. Also, various factors would in some way affect the choice of the weight value, such as the size of service area, size of ambulance <sup>fl</sup>eet, call arrival pattern, etc. The effect of the weight in various operational scenarios will be evaluated and analyzed in Section 3.

![](/api/attachments/2UE87NCT/fulltext/images/1193df4ecf68148360494286d1d1d5dd88c7ac10df77cfad6a11cbaf5b1b7786.jpg)  
Fig. 1. Call arrival patterns.

The second parameter is the centrality measure $c _ { u } .$ It is computed upon the network of unassigned calls U with the edge between every pair i and j of calls having the value of distance $\tau _ { i j }$ between them. Among various centrality measures available in the literature, three popular centrality measures are chosen as they are appropriate to the call network. The measures are presented as follows and will be evaluated in Section 4.

## 2.2.1. Weighted degree (WD)

The degree of a node is the number of edges that the node has, and the weighed degree is an extension of the degree to the weighted network (where an edge has a weight representing capacity or strength). The weighted degree of a node is the sum of the weights of all edges connected to the node [3,20]. Note that this method is used when higher weight values are preferred (e.g. capacity and strength); however, the weight in the call network represents distance, thus lower weight values are preferred. The weighted degree in this case is computed by the sum of the reciprocals of weights.

$$
k _ {u} = \sum_ {i \in U, i \neq u} \frac {1}{(1 + \tau_ {u i})}
$$

## 2.2.2. Distance centrality (DC)

This measure represents the proximity of a node to the rest of nodes in the network [18,23]. It is de<sup>fi</sup>ned as the inverse of farness which is the sum of distances to all other nodes. This measure is also called closeness centrality.

$$
d _ {u} = \frac {1}{1 + \sum_ {i \in U , i \neq u} \tau_ {u i}}
$$

## 2.2.3. Betweenness centrality (BC)

This measure is used to estimate the in<sup>fl</sup>uence of a node over the <sup>fl</sup>ow in a network [4,11,14]. It is de<sup>fi</sup>ned as the sum of fractions of all the shortest paths between each pair of vertices in a network that traverse a given node.

$$
b _ {u} = \sum_ {i, j \in U, i \neq j \neq u} \frac {\sigma_ {i j} ^ {u}}{\sigma_ {i j}}
$$

$\sigma _ { i j } \mathbf { \cdot }$ the number of paths that have the same minimal length from i to j

σ<sub>ij</sub><sup>u</sup>: the number of paths that traverse u among those counted in $\sigma _ { i j } .$

## 3. Performance evaluation of Centrality policy

In this section, the performance of the Centrality policy is evaluated in various scenarios implemented in a discrete event simulator, by the performance enhancement over the NN policy as well as another local policy, the DNN policy, that is a more articulate version of the NN policy as will be detailed in Section 3.3. Since the NN policy is presumable to be effective across all different scenarios as discussed before, if the performance of the Centrality policy even outperforms the NN policy, the effectiveness of the Centrality policy will get supported to the large extent. In this evaluation, the effect of the weight on centrality is investigated while using weighted degree as centrality measure, and the effect of different centrality measures will be analyzed in Section 4.

## 3.1. Experimental design

The service area is represented in a 5∗5 square grid as shown in Fig. 1. Each vertex generates calls at a certain rate and ambulances move from vertex to vertex through edges each with 1 min of traveling time. Once dispatched to a call, the ambulance serves the patient with a service time that is exponentially distributed with average service time=0.5 min. The ambulance then, with a probability, transfers the patient to the hospital which is located at the center of the grid as depicted in the <sup>fi</sup>gure. The probability of transferring to hospital is denoted by hospital\_prob<sup>1</sup> throughout the rest of the paper. The purpose of this experiment is to evaluate various ambulance-initiated dispatching policies, and in cases when call-initiated decisions are needed, the policy of dispatching the closest unit is applied as this policy is the most commonly used in practice [8,10,15].

Three factors are taken into consideration in generating different test conditions: 1. call arrival pattern, 2. size of ambulance <sup>fl</sup>eet, 3. hospital\_prob. A total of 12,500 calls are generated at the rate of 1 call/min following an exponential distribution, and they are distributed to the vertices according to one of the four call patterns as shown in Fig. 3: a. uniform, b. centered, c. cornered and d. bipartite. A value in the <sup>fi</sup>gure of each call pattern represents the probability for an arriving call to be allocated to a corresponding vertex. For example, in the centered pattern, the vertex located in the center gets an arriving call

Weight on centrality (w) a2.1 unit-centered

with a probability of 0.4. The size of ambulance <sup>fl</sup>eet can be one, three, or <sup>fi</sup>ve, and the units are randomly located in the beginning of each simulation run. The hospital\_prob ranges from 0 to 1 with an increment of

![](/api/attachments/2UE87NCT/fulltext/images/d9fc0c8f806337a6040b163efbb4e044d7bc5ade398e9e75057de0bf78fc7d1d.jpg)  
Weight on centrality (w) a1.1 unit-uniform

![](/api/attachments/2UE87NCT/fulltext/images/34f6e60eb31c0e8b81a8930f0bd2f4ecb1ac9b2300c3dd2148caa1b1d134814b.jpg)

![](/api/attachments/2UE87NCT/fulltext/images/765fb1ba01f63a541d439ee559b88450135676b3a8a05313b00fc914ca068687.jpg)

![](/api/attachments/2UE87NCT/fulltext/images/7da7b7a513a136d4f30e328c259ff660a20b71a5279c6336840d8cd945f676c3.jpg)

0.1. As a result, 132 test conditions (4 call arrival patterns∗3 sizes of ambulance <sup>fl</sup>eet ∗11 hospital\_prob) are established. Fifty simulation runs are replicated for each test scenario.

![](/api/attachments/2UE87NCT/fulltext/images/029710340eda7e90c871f386194a87ecadb39244188267c7ecd5e075126fe74e.jpg)

![](/api/attachments/2UE87NCT/fulltext/images/b0fa14d35e98aaf7ad39fecafc3f1d80deef3c5c4b8fbd61c68aad98fe66fbfd.jpg)

![](/api/attachments/2UE87NCT/fulltext/images/3762131b70ebd082c851b7c8cbae718928e671c5bdc33ca0c41ef0bd8b9d4757.jpg)

![](/api/attachments/2UE87NCT/fulltext/images/d39183d8e7675d5d01bd9e7e867699027cebb6a1873cdfd5e7b2ca8b1a20bc7a.jpg)  
Fig. 2. Effect of weight on performance enhancement by Centrality policy.

c1. 5 units-uniform

c2. 5 units-centered

![](/api/attachments/2UE87NCT/fulltext/images/5b073615990ecb10076dd3468c276f52d25771bd847ec5da8dbf5e86cc54f2d5.jpg)

![](/api/attachments/2UE87NCT/fulltext/images/cca44156a839f0c98888c8112985405197f0d704adc5a38105e2cdf8bf7a2f04.jpg)

![](/api/attachments/2UE87NCT/fulltext/images/16c5e199d103055ee847a30e308212e77e4ce726b4b125fc7390f1695f0226d2.jpg)

Fig. 2 (continued).  
![](/api/attachments/2UE87NCT/fulltext/images/2818787234c6a1152b2586ca0cd330085a2e0f9d21bdc7985692e322f07ff7db.jpg)

## 3.2. Performance of Centrality policy over NN policy

For each test condition, the Centrality policy is applied with the centrality measure $c _ { u }$ <sup>fi</sup>xed to weighted degree (WD) and the weight on centrality w varying in {0.001, 0.2, 0.4, 0.6, 0.8, 1.0, 1.5, 2.0, 2.5, 3}. Fig. 2 shows the average reduction in response time by the Centrality policy over the NN policy, i.e. average reduction in response time = (average response time with NN policy average response time with Centrality policy) / (average response time with NN policy). The Centrality policy dominantly outperforms the NN policy in all different conditions with up to 86% reduction in response time, as long as the weight is not too large. The improvement is signi<sup>fi</sup>cant even with a small weight (w=0.001), and it thereafter tends to increase with higher weight values. Then, after reaching the peak, the improvement keeps going down towards negative improvement (i.e. increase in response time). As discussed before, if the units pursue too much the centrality they will travel excessively just to reposition themselves in central nodes without enough exploitation of calls in vicinity.

The nonlinear behavior with the weight on centrality gives rise to the need for carefully choosing the right value of weight according to the operating environment, in order to maximize the bene<sup>fi</sup>t of centrality consideration. In practice, when a disaster breaks out, the parameters of operating environment are initially unknown to a large extent, and it is recommended to start using a small weight value with the Centrality policy. As the parameters are becoming revealed over time, the optimal weight value can be searched by a simulation study.

Fig. 3 summarizes the results in Fig. 2 by taking the maximum improvement (from the best weight value) by the Centrality policy for each test condition (Please refer only to the curves indexed by the “Centrality” for now. The “DNN” will be discussed in Section 3.3.). As shown in Fig. 3, the enhancement by centrality exhibits the bellshaped nonlinearity with the hospital\_prob. It is because the increase of hospital\_prob ampli<sup>fi</sup>es the contribution of centrality consideration due to the high system load, but at the same time it diminishes the contribution as the chance for a unit to continue serving calls before heading for a hospital gets reduced. When the size of <sup>fl</sup>eet increases, the peak point tends to occur at higher hospital\_prob. This is because the increase in <sup>fl</sup>eet size reduces the frequency of ambulanceinitiated decisions and thus the contribution of centrality becomes eminent in higher load conditions.

The standard deviation of response times in each simulation run is computed to analyze the impact of the centrality consideration on the performance variation. Fig. 4 (please refer to those indexed by the “Centrality”) shows the average reduction in variation by the Centrality policy over the NN policy, i.e. average reduction in variation=(average standard deviation with NN policy−average standard deviation with Centrality policy)/(average standard deviation with NN policy). Note that the weight value used by the Centrality policy in each test condition is the one that produces the maximum improvement in the average response time in that condition, thus being consistent with the weight used in Fig. 3. The overall pattern is similar to the pattern obtained in Fig. 3; however, the reduction in variation is even larger than the reduction in response time. The Centrality policy reduces the variation up to 94%. The reduction in both average and variation implies that excessive tardy responses can be avoided with the centrality consideration.

## 3.3. Performance of Centrality policy over DNN policy

The NN policy dispatches a freed unit to the closest call site. However, there can be multiple such sites and the NN policy does not specify the action to be taken in that case. A more articulate policy can be formed by letting choose the call site that has the most number of calls. This policy, called DNN (Densest among Nearest Neighbors) policy, is more speci<sup>fi</sup>c than the NN policy but it still remains local. Fig. 3 shows the average reduction in response time of the DNN policy over the NN policy, in comparison with the one maximally achieved by the Centrality policy.<sup>2</sup> The DNN policy provides signi<sup>fi</sup>cant advantages against the NN policy with up to 62% reduction in response time. However, the Centrality policy again shows dominant performance even over the DNN policy in all different conditions with up to 30% more reductions, further demonstrating the signi<sup>fi</sup>cance of the centrality consideration in reducing the response time.

![](/api/attachments/2UE87NCT/fulltext/images/52973707e6fc4ac39781646f0beaaed98551e8ab90b8345d32a98c0a57499d09.jpg)  
a1. 1 unit-uniform

![](/api/attachments/2UE87NCT/fulltext/images/9b461a13f1a00b5e6802e5b1ef686b08212901caeafd332708cc5a658c4e773f.jpg)

![](/api/attachments/2UE87NCT/fulltext/images/6f259dd85b3dcaa5cbd149d5fce998774788c6d8000d2520d484d19fbfc0b030.jpg)  
b1.3 units-uniform

a2. 1 unit-centered  
![](/api/attachments/2UE87NCT/fulltext/images/cec1124976af8c215ec4117a7fed2ba4ea1e66ef46c82ba4b6ff21d6fc624331.jpg)  
b2. 3 units-centered

c1. 5 units-uniform  
![](/api/attachments/2UE87NCT/fulltext/images/96caf4532cd4cd10a48d0e8f3b336b5860bf43ff1cbf93edfbc76bf249940c71.jpg)

![](/api/attachments/2UE87NCT/fulltext/images/858159f0a19ef5212ed08ab80b1863090bdcb44b4a5ac3c795e29ae869c389ac.jpg)

![](/api/attachments/2UE87NCT/fulltext/images/cca7f56c216615995832d642a0e1035878bec647b214caea0c7056d887f1a0f6.jpg)

![](/api/attachments/2UE87NCT/fulltext/images/58b8c0776f0a5640bc6eb657feb7f2f25a6ebef07e1705cfde0d5ceab30a220c.jpg)  
a3. 1 unit-cornered  
b3. 3 units-cornered

c2. 5 units-centered  
![](/api/attachments/2UE87NCT/fulltext/images/f570ba5fc4b3564a22bd31ca0e56064f24da5f2f99dbf121826d2e4f10429e62.jpg)  
c3. 5 units-cornered

![](/api/attachments/2UE87NCT/fulltext/images/9e696ba174b6b9a0cb5abddd84ebcf23471669500a063e1677db7687398937c5.jpg)  
a4. 1 unit-bipartite

![](/api/attachments/2UE87NCT/fulltext/images/549c4f26ffc69075efe29cfee3e78dadab01125380e5e9f586c0b701830265d0.jpg)  
b4. 3 units-bipartite

![](/api/attachments/2UE87NCT/fulltext/images/1abc2b30de72d8eaa5d8d78a55f87baf365d0ebbac3457ac1c85b4af6b21e044.jpg)  
c4. 5 units-bipartite  
Fig. 3. Reduction in response time by Centrality policy in comparison with DNN policy.

Fig. 4 shows the average reduction in variation by the Centrality policy in comparison with the DNN policy, where the Centrality policy uses the same weight values used in Fig. 3. Though the DNN policy effectively reduces the variation up to 85%, the Centrality policy again exhibits dominant performance over the DNN policy with 55% more reductions in variation. From the observations so far, it is possible to argue that the centrality consideration can signi<sup>fi</sup>cantly reduce the average as well as the variation of response time, as a result of equipping with global exploration capability that is lacking in other local policies.

## 4. Effect of centrality measures

The Centrality policy has the centrality parameter $c _ { u }$ and this section analyzes the effect of different centrality measures. As mentioned before three centrality measures are taken into consideration, which are WD (weighted degree), DC (distance centrality), and BC (betweenness centrality). The experiment made in the previous section is repeated for each centrality measure, but only in the conditions where the Centrality policy produces the most outstanding improvements, i.e. hospital\_prob ∈ {0.0, 0.1, 0.2} when <sup>fl</sup>eet size=1, {0.3, 0.4, 0.5} when <sup>fl</sup>eet size=3, and {0.6, 0.7, 0.8} when <sup>fl</sup>eet size=5.

![](/api/attachments/2UE87NCT/fulltext/images/3e95ebe9a80d8d194784fcdc9c35baa65a8337fb1af9ec9db10794af07911525.jpg)  
a1. 1unit-uniform

![](/api/attachments/2UE87NCT/fulltext/images/d8f2312f8e2c420a100a90b1201e1ec3547ffa585e6235012a027b45d27b8104.jpg)  
b1. 3 units-uniform

![](/api/attachments/2UE87NCT/fulltext/images/e0257157f1de9e1200ebaf85fb6e3cfc32892b893b950e39021a6ec6ea938c89.jpg)  
c1. 5 units-uniform

![](/api/attachments/2UE87NCT/fulltext/images/e4aaf545b8bae100c609e15db9e90387fa6a06520819a7ab450fde12acf90d0c.jpg)  
a2. 1 unit-centered

![](/api/attachments/2UE87NCT/fulltext/images/b4c39e9236b4d99f761ef181d38c9820703e04e6a2149bb8b4c4beae8b05bccc.jpg)  
b2. 3 units-centered

![](/api/attachments/2UE87NCT/fulltext/images/152260ae7ceb005022b83a2fca51bbf91586f0a7a3c93a6515abe7dc64b48e61.jpg)

![](/api/attachments/2UE87NCT/fulltext/images/93513548e1221de7e0858831453fc8c478c176b46a932dea25a339461bc9a23a.jpg)  
a3. 1 unit-cornered

c2. 5 units-centered  
![](/api/attachments/2UE87NCT/fulltext/images/a560f1c25ee85860716ccc166e83555e018b78a0a3469980791394d254a633d1.jpg)  
b3. 3units-cornered

![](/api/attachments/2UE87NCT/fulltext/images/895743c4ea50af557982faf414539a470833cd2defe4f5934672f6313624d950.jpg)  
c3. 5 units-cornered

![](/api/attachments/2UE87NCT/fulltext/images/1988a4312c1743af4ccece801fbc958cfb8a014345d89fc98f6e4716f47cff77.jpg)  
a4. 1 unit-ipartite

![](/api/attachments/2UE87NCT/fulltext/images/2dabc8eab98dc725c896b6a03dc0502f49e8a5347ce7330d7e7574104bfd9aab.jpg)  
b4. 3 units-bipartite

![](/api/attachments/2UE87NCT/fulltext/images/b39e20930d3cd5e4ef05267e9cd81dde44e5f9e8297ba06eab29b9e3f51513cd.jpg)  
c4. 5 units-bipartite  
Fig. 4. Reduction in variation by Centrality policy in comparison with DNN policy.

Fig. 5 compares the reduction in response time of different centrality measures. The performance of a centrality measure is represented by the maximal improvement over the NN policy from applying different weights on centrality. All the centrality measures make signi<sup>fi</sup>cant improvements in response time, thus being capable of capturing the guidance information for the global exploration. However, note that the WD consistently produces high performance in all different conditions. The maximal improvement is achieved by the WD in 26 cases out of 36 (72%) with slight differences from the best when it is not the best, while the DC makes 6 best cases (17%) and the BC makes 4 best cases (11%). The strength of the weighted degree is also supported by the reduction in variation as shown in Fig. 6. The weighted degree consistently shows superior performance in variation in most cases. The maximal improvement is achieved by the WD in 22 cases out of 36 (61%), while the DC makes 6 best cases (17%) and the BC makes 8 best cases (22%).

Therefore, from these observations, the weighted degree can be considered most suitable as the centrality measure. The weighted degree is also simple to compute thus it is appropriate to the realtime applications. On the other hand, the BC is much more complex to compute since one has to search for all different shortest paths between every pair of nodes, taking a long time especially when the number of calls is very large.

## 5. Conclusions

A novel ambulance dispatching policy is proposed by the principle of centrality from the study of complex networks. The policy is applicable to various demanding emergency situations such as in disasters requiring real-time decision making. There are two parameters within the policy. One parameter is the weight on centrality. The weight value has to be carefully chosen according to the operating environment, in order to maximize the bene<sup>fi</sup>t of centrality consideration. Even a small weight value gives signi<sup>fi</sup>cant bene<sup>fi</sup>ts; however, the performance gets considerably degraded if the weight is too large. Another parameter is the centrality measure. The weighted degree among others is recommended as it consistently produces high performance and is computationally simple. The dispatching policy, upon the right selection of the parameters within the policy, can signi<sup>fi</sup>cantly reduce the average as well as the variation of response time, as a result of being equipped with global exploration capability driven by the centrality consideration that is lacking in other local policies.

![](/api/attachments/2UE87NCT/fulltext/images/e3399b917cbada08fa37bd41ad299e2a6aad0bfa9b5fe8e9c5c934c1be2103c9.jpg)  
a1. 1 unit-uniform

![](/api/attachments/2UE87NCT/fulltext/images/856d7044f2a0bc6e7d0cd78730fece35f9ef2b8dd778df0b9c57e8aee6f91d83.jpg)  
b1. 3 units-uniform

![](/api/attachments/2UE87NCT/fulltext/images/1d9e171d3e89a4de221dcda1a21f1837a340fed91731086fe549ffee06f0fca1.jpg)  
c1. 5 units-uniform

![](/api/attachments/2UE87NCT/fulltext/images/80edbc960795c65dbfe82847336826b935af5e71958657e919c9ecef7bcacfd8.jpg)  
a2.1 unit-centered

![](/api/attachments/2UE87NCT/fulltext/images/6252586f206688c15ddb424eba3b876007ffaf70acc8698806d4604717445ade.jpg)  
b2. 3 units-centered

![](/api/attachments/2UE87NCT/fulltext/images/26ad7071eaf94672ad559ec623b1be7a3d6407c8e530c13ae37536f201d21e4b.jpg)  
c2. 5 units-centered

![](/api/attachments/2UE87NCT/fulltext/images/fee403f5bd0a47f90ed6554a3fdd0a2e23ad4e7070284b80261c64f7f524eacd.jpg)  
a3. 1 unit-cornered

![](/api/attachments/2UE87NCT/fulltext/images/24c28624c5bafb012b9daecb2830492b75956deabeb1a9c4af20276d35ab84fa.jpg)  
b3. 3 units-cornered

![](/api/attachments/2UE87NCT/fulltext/images/29da256b394a63814b2f259ed840db367c0471b07dbe3585074ad375af77b7c4.jpg)  
c3. 5 units-cornered

![](/api/attachments/2UE87NCT/fulltext/images/3fe7345190c11b0d8463cec7deef340b58ea48b5a5bf02a99ee8417fde1dacbd.jpg)  
a4.1 unit-bipartite

![](/api/attachments/2UE87NCT/fulltext/images/eb990becb365978d9c69ceb2e27710d29b106f458d90c27db101ece0316b8efc.jpg)

![](/api/attachments/2UE87NCT/fulltext/images/dc6fe7c4a5da8365b55a64d7f8232ec61d430e7b1ca9e65ee43927991454ae22.jpg)  
c4. 5 units-bipartite  
Fig. 5. Reduction in response time of different centrality measures.

This work is aligned with recent endeavors that try to apply information technology and decision support systems in disaster management [7,16,17,22,25]. During emergencies, decision making is a challenging task that requires immediate and effective action despite the pressures of incomplete and erroneous information. The policy devised in this research is expected to effectively support the decisions of ambulance dispatchers, when it is implemented by the use of modern computation and communication capabilities available today.

The policy devised here takes into account only the idle unit that has just got freed, despite the possibility that a busy unit can respond more quickly, even after the completion of the currently assigned service, to the call that is otherwise assigned to the idle unit. To further improve the performance by avoiding this inef<sup>fi</sup>ciency, all the units need to be taken into account whether they are idle or busy, and it naturally forces to consider all unassigned calls at the same time, leading to an assignment problem that matches between calls and units.

Another important problem in disasters is the emergency commodity logistics problem that involves transporting relief commodities (e.g. food, water, medical aids, etc.) to the affected people. Though the details of the commodity logistics problem are different from the ambulance dispatching problem, they share several key characteristics. Both problems involve vehicle routing and especially aim to minimize response time [21,27,28]. Therefore, the lessons and principles obtained from the ambulance dispatching will provide the basis on which the solution policy for the commodity logistics problem can be established.

![](/api/attachments/2UE87NCT/fulltext/images/f3f519bffa34f05c9994fdb5b4f4ee33367e933690bdaa3342b59b50c76f40e3.jpg)  
a1. 1 unit-uniform

![](/api/attachments/2UE87NCT/fulltext/images/52d2d2ae211adeab861ddecaf925f7a22a80303115bef9a76173b8b2ad7ab225.jpg)  
b1. 3 units-uniform

![](/api/attachments/2UE87NCT/fulltext/images/66e4defa250aa393bce5fe6b28533c55c4dfcc42bfb5e480c3262f713eba5959.jpg)  
c1. 5 units-uniform

![](/api/attachments/2UE87NCT/fulltext/images/f7c1129a89e695edaf6c890cf37fea2ecda6177a8946faee534e4444db17a91f.jpg)  
Hospital\_prob a2.1 unit-centered

![](/api/attachments/2UE87NCT/fulltext/images/4170cd2902a220a05688ef2a45f5e6a784f62f95e0faaddebfdf57ce4bcc8a3d.jpg)  
Hospital\_prob b2. 3 units-centered

![](/api/attachments/2UE87NCT/fulltext/images/41546d944c795492617df56051b7c862dc752aa061d8382616a938691492c2e9.jpg)  
Hospital\_prob c2. 5 units-centered

![](/api/attachments/2UE87NCT/fulltext/images/33e2fe71a23102fcaef42bc5362b66e68eb896d8165dc185a9b751276b62bb27.jpg)  
a3. 1 unit-cornered

![](/api/attachments/2UE87NCT/fulltext/images/2c92c02314a60a01783efac166c730a9eed910df73ab3a053f427ae1b776199b.jpg)  
b3. 3 units-cornered

![](/api/attachments/2UE87NCT/fulltext/images/89d46c4b7d45721f88b0fddfbda7d430609f3f95c128d89a8c216f2ec04ae57d.jpg)  
c3. 5 units-cornered

![](/api/attachments/2UE87NCT/fulltext/images/7eb37713b3097472b254bcbecaaababc07a5018ba19bcd2e5403bb4567bba4e2.jpg)  
a4.1 unit-bipartite

![](/api/attachments/2UE87NCT/fulltext/images/6a72d5739521d89ad85bfa65d3b9dc1a3bfd95ab23988e40e3d4bbf97ae83a3a.jpg)  
Fig. 6. Reduction in variation of different centrality measures.

![](/api/attachments/2UE87NCT/fulltext/images/f87a4524faa25aea63eb37a4430a6587d1bb685d96be9bc65b3ef6ea00bdfa4b.jpg)  
c4. 5 units-bipartite

## References

[1] F. Afrati, S. Cosmadakis, C. Papadimitriou, G. Papageorgiou, N. Papakostantinou, The complexity of the traveling repairman problem, Theoretical Informatics and Applications 20 (1) (1986) 79–87

[2] S. Arora, G. Karakostas, Approximation schemes for minimum latency problems, SIAM Journal on Computing 32 (5) (2003) 1317–1337

[3] A. Barrat, M. Barthelemy, R. Pastor-Satorras, A. Vespignani, The architecture of complex weighted networks, Proceedings of the National Academy of Sciences of the United States of America 101 (11) (2004) 3747–3752.

[4] M. Barthelemy, Betweenness centrality in large complex networks, The European Physical Journal B 38 (2) (2004) 163-168

[5] D.J. Bertsimas, G. van Ryzin, A stochastic and dynamic vehicle routing problem in the Euclidean plane, Operations Research 39 (4) (1991) 601–615.

[6] E.A. Blackstone, A.J. Buck, S. Hakim, The economics of emergency response, Policy Sciences 40 (2007) 313–334.

[7] T.X. Bui, S.R. Sankaran, Design considerations for a virtual information center for humanitarian assistance/disaster relief using work<sup>fl</sup>ow modeling, Decision Support Systems 31 (2001) 165–179.

[8] J.M. Chaiken, R.C. Larson, Methods for allocating urban emergency units: a survey, Management Science 19 (3) (1972) 110–130.

[9] R.W. Conway, W.L. Maxwell, L.W. Miller, Theory of Scheduling, Addison-Wesley, Reading, Mass, 1967.

[10] S.F. Dean, Why the closest ambulance cannot be dispatched in an urban emergency medical services system, Prehospital and Disaster Medicine 23 (2) (2008) 161–165.

[11] L.C. Freeman, A set of measures of centrality based on betweenness, Sociometry 40 (1)(1977)35-41

[12] A. Garcia, P. Jodrá, J. Tejel, A note on the traveling repairmen problem, Networks 40 (1)(2002) 27-31.

[13] M. Goemans, J. Kleinberg, An improved approximation ratio for the minimum latency problem, Mathematical Programming 82 (1998) 114–124.

[14] K.-I. Goh, E. Oh, H. Jeong, B. Kahng, D. Kim, Classi<sup>fi</sup>cation of scale-free networks, Proceedings of the National Academy of Sciences of the United States of America 99 (20) (2002) 12583–12588.

[15] J. Hayes, A. Moore, G. Benwell, B. Wong, Ambulance dispatch complexity and dispatcher decision strategies: implications for interface design, Lecture Notes in Computer Science 3101 (2004) 589–593.

[16] J.K. Kim, R. Sharman, H.R. Rao, S. Upadhyaya, Ef<sup>fi</sup>ciency of critical incident management systems: instrument development and validation, Decision Support Systems 44 (2007) 235–250.

[17] J. Lee, N. Bharosa, J. Yang, M. Janssen, H.R. Rao, Group value and intention to use — a study of multi-agency disaster management information systems for public safety, Decision Support Systems 50 (2011) 404–414.

[18] L. López-Fernández, G. Robles, J.M. Gonzalez-Barahona, I. Herraiz, Applying social network analysis techniques to community-driven libre software projects, International Journal of Information Technology and Web Engineering 1 (3) (2006) 27–48.

[19] E. Minieka, The delivery man problem on a tree network, Annals of Operations Research 18 (1989) 261–266.

[20] M.E.J. Newman, Analysis of weighted networks, Physical Review E 70 (5) (2004) 056131.

[21] L. Özdamar, E. Ekinci, B. Küçükyazici, Emergency logistics planning in natural disasters, Annals of Operations Research 129 (2004) 217–245.

[22] Y. Peng, Y. Zhang, Y. Tang, S. Li, An incident information management framework based on data integration, data mining, and multi-criteria decision making, Decision Support Systems 51 (2011) 316–327.

[24] S. Sahni, T. Gonzalez, P-complete approximation problems, Journal of the ACM 23 (3) (1976) 555–565.

[23] G. Sabidussi, The centrality index of a graph, Psychometrika 31 (1996) 581–606.

[25] D.E. Snediker, A.T. Murray, T.C. Matisziw, Decision support for network disruption mitigation, Decision Support Systems 44 (2008) 954–969.

[26] B.Y. Wu, Polynomial time algorithms for some minimum latency problems, Infor mation Processing Letters 75 (5) (2000) 225–229.

[27] W. Yi, A. Kumar, Ant colony optimization for disaster relief operations, Transportation Research Part E 43 (2007) 660–672.

[28] W. Yi, L. Özdamar, A dynamic logistics coordination model for evacuation and support in disaster response activities, European Journal of Operational Research 179 (2007) 1177–1193.

Seokcheon Lee received the B.S. and M.S. degrees in Industrial Engineering from Seoul National University, South Korea, in 1991 and 1993 respectively, and the Ph.D. degree in Industrial Engineering from Pennsylvania State University, University Park, in 2005. Currently, he is an Assistant Professor in the School of Industrial Engineering at Purdue University. His research interests include decision making techniques from the principles in economics, swarm intelligence, learning, and complex network theory.

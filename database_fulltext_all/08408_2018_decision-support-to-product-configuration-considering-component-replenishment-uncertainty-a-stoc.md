---
otero_id: 8408
otero_key: "FFX9F84K"
title: "Decision support to product configuration considering component replenishment uncertainty: A stochastic programming approach"
authors: "Dong Yang; Xiaohong Li; Roger J. Jiao; Bill Wang"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.11.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Decision support to product configuration considering component replenishment uncertainty: A stochastic programming approach

Dong Yang, Xiaohong Li, Roger J. Jiao, Bill Wang

![](/api/attachments/FFX9F84K/fulltext/images/8db1e3bab149de91deec875edd756d0d4ccd49173c8ab39318bd805ad544506a.jpg)

<table><tr><td>PII:</td><td>S0167-9236(17)30216-6</td></tr><tr><td>DOI:</td><td>doi:10.1016/j.dss.2017.11.004</td></tr><tr><td>Reference:</td><td>DECSUP 12898</td></tr><tr><td>To appear in:</td><td>Decision Support Systems</td></tr><tr><td>Received date:</td><td>7 May 2017</td></tr><tr><td>Revised date:</td><td>20 November 2017</td></tr><tr><td>Accepted date:</td><td>21 November 2017</td></tr></table>

Please cite this article as: Dong Yang, Xiaohong Li, Roger J. Jiao, Bill Wang , Decision support to product configuration considering component replenishment uncertainty: A stochastic programming approach. The address for the corresponding author was captured as affiliation for all authors. Please check if appropriate. Decsup(2017), doi:10.1016/ j.dss.2017.11.004

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Decision Support to Product Configuration Considering Component Replenishment Uncertainty: A Stochastic Programming Approach

Dong Yang <sup>a,\*</sup>, Xiaohong Li <sup>a</sup>, Roger J. Jiao <sup>b</sup>, Bill Wang <sup>c</sup>

<sup>a</sup> School of Business and Management, Donghua University, 1882 Yan-an Road, Shanghai 200051, PR China

<sup>b</sup> The George W. Woodruff School of Mechanical Engineering, Georgia Institute of Technology, Atlanta,

GA30332-0405, USA

<sup>c</sup> School of Engineering and Advanced Technology, Massey University, New Zealand

Abstract: Product configuration is to make decisions on component selections and combination to constitute a customized product under mass customization production. However, the uncertainties (such as component supplies) in product configuration setting are not considered in the existing product configurators. To handle the uncertainty in component replenishment lead-time, a new stochastic decision model is proposed in this paper using two-stage stochastic programming approach. Further, a pre-procuring strategy for component supply is employed to reduce total configuration costs and shorten the delivery date of customized products. The stochastic decision model for product configuration is solved by using Lagrangian relaxation algorithm. The effectiveness of the stochastic decision model is demonstrated through case studies from both computer configuration and ranger drilling machine configuration. Computational comparisons with a commercial solver (CPLEX) indicate that the proposed stochastic decision model provides competitive solution results.

Key words: product configuration decisions; stochastic programming; mass customization; Lagrangian relaxation

## 1 Introduction

Stimulated by growing demand for quick response to customer requirements and providing individualized products, an increasing number of manufacturers are transforming from mass production to mass customization (MC) production [1, 2]. Modular product design in which a product consists of common modules and variant modules is widely accepted as an effective means to achieve MC [3-5]. As one of the key enabling technologies for mass customization [6, 7], product configuration (PC) is defined to select components (such as common and variant components) from the predefined component catalogue and assemble these components into a valid product with configuration rules and customer requirements simultaneously satisfied [8, 9].

A product configuration system, namely configurator, is a computer-supported decision support system (DSS) that assists a customer and engineers/salesmen in eliciting preference, capturing customer needs, representing product knowledge and rules, selecting alternative components and options, building mathematical models for deriving configurations, and recommending options to customers during the configuration process in a interactively or automatically way [10-13]. The general structure of a configurator, as illustrated in Fig. 1, mainly consists of information modeling and configuration engine functions. Product knowledge depicting the decomposable structures of a product (like modules and components) and configuration rules restricting the combination of configured elements (such as components) are represented by means of information modeling techniques. Typical information modeling used in product configuration includes objected-oriented technique like UML (Unified Modeling Language) [14], ontology-based knowledge representation such as OWL (Ontology Web Language) [51] for representing hierarchical structures and relationships between components, modules and products Configuration rules can be represented as first-order predicate logics or if-else-like formalism. The configuration engine with both product configuration knowledge and customer requirements as the inputs infers configuration results by using the problem-solving technologies like CSP (Constraint Satisfaction Problem) [18-20], rule-based reasoning [21], and case-based reasoning [22, 23]. Further, the optimization engine can be employed to derive the optimal configuration in the case of a numerous number of feasible configurations available [13]. Additionally, some configurators also consider an additional function, namely recommendation technologies, to recommend suitable components or modules to customers in the case of multiple alternatives valid in the configurations [16, 17]. With the proliferation of global supply chains, more and more enterprises begin to organize their productions or procure components from the chains. Therefore, researchers begin to integrate the supplier function into the product configurators [24, 25], as shown in the left part of Fig.1.

However, the existing product configurators only consider decision models for deterministic product configuration problem where configuration parameters (such as purchase costs, replenishment lead-time) are fixed and pre-determined. As a consequence, the effect of uncertainty in supply chains on product configuration is not taken into account in the existing configurators. In fact, supply chains operate in a highly uncertain environment like infrastructure breakdowns, traffic conditions, vehicle troubles, natural disasters, terrorist attacks, strikes [48]. The uncertainties in a supply chain will have a substantial effect on component replenishment lead-time, supply capacities of suppliers, purchase costs and customer demands. Current decision models adopted by the product configurator cannot handle well with the uncertainty since the optimal configuration will become invalid when the uncertainty is addressed. Therefore, it is a challenge to develop a new decision model in configurators to deal with the uncertainty in the configuration problem.

![](/api/attachments/FFX9F84K/fulltext/images/312fea6cb8ec00aab6eb0d2c75fabb7b741947996e5768e09d0b135dcba8687a.jpg)  
Fig.1. Structure of a product configurator.  
In this paper, we develop a new decision model for the product configurator to handle

# ACCEPTED MANUSCRIPT

the uncertainty in product configuration problem by using stochastic programing [26]. The configuration decision problem under uncertainty in component replenishment lead-time (i.e. the time required to purchase and ship a component from a supplier to a manufacturer) is formulated as a nonlinear mixed-integer programming model using discrete scenario-based modeling. Every possible random situation of the problem data is represented by a scenario with the associated probability [27, 28]. Then Lagrangian relaxation is applied to solve the stochastic model and obtain optimal product configuration. Finally, the proposed algorithm is compared with the commercial solver CPLEX through both the computer and ranger drilling machine cases. The results indicate that the suggested algorithm increases the efficiency of solving optimal configuration, which can be well used to solve product configuration decision problem under uncertainties.

The remainder of this paper is organized as follows. Section 2 reviews the related literature. Product configuration problem under uncertainty and corresponding stochastic decision model model using Lagrangian relaxation algorithm. Section 5 provides the case studies of product configuration decisions. Conclusions and future research directions are discussed in Section 6.

## 2 Literature review

The concept of mass customization (MC) was firstly proposed by Davis in the late 1980s [29]. It was popularized in the early 1990s and has been identified to provide individualized products and services to customers with a large scale at a relatively low cost [30]. Owing to its obvious advantage in delivering an increasing product variety while keeping mass production efficiency, MC has become a mainstream production mode of the 21st century. Considering that making a product can be easily customizable, Fogliatto et al. [8] and Berman [31] proposed that modular product design would be an enabler for successfully implementing MC. Because modular products are designed to consist of common and variant components, a customized product can be configured to quickly meet the diverse demands of

## ACCEPTED MANUSCRIPT

customers [3, 5]. Product configuration is defined to select components from a predefined component library to constitute a customized product with configuration rules and the individualized customer requirements simultaneously satisfied [18]. The first successful commercial application of product configuration is XCON configuration system in 1989 [32]. Since then, product configurators are widely used in various industrial settings to configure a variety of products, such as in the telecommunication, computer industry, building, and such as object-oriented methods are adopted to describe the conceptual models products. Alexander et al. [14] employed the Unified Modeling Language for modeling configuration knowledge base including components knowledge and function knowledge. Yang et al. [51] applied ontology-based modeling, namely OWL, to formally represent product configuration knowledge with the aim of reusing configuration knowledge. Furthermore, some researchers focus on the inference technology for configuration engines in product configurators. So far, the main inference methods include constraint satisfaction problem (CSP) [18, 33], case-based reasoning (CBR) [22, 23], and rule-based reasoning [21, 35]. For example, IBM used constraint satisfaction problem to build its configuration system Saturn to check the orders correctness and configure personal computers according to the customer requirements [34]. Chao and Chen [35] employed rule-based reasoning to establish the product’s assembly rules and then integrate the rules into a configuration model. However, almost all studies above are concentrated on generating feasible configuration solutions and do not consider obtaining the optimal configuration, namely the optimal solution in all feasible configurations. Thus, the exact algorithms like mixed-integer programming [13] and the heuristic methods such as genetic algorithm (GA) [36, 37] and particle swarm optimization algorithm (PSO) [38] are utilized to obtain a near-optimal or optimal configuration solution. Nevertheless, it can be seen that all the configuration problems occur within a single enterprise and the effects of supply chains on product configuration are not taken into account.

Nowadays, the globalization of supply chains enables many organizations to obtain

# ACCEPTED MANUSCRIPT

production resources conveniently. Thus, more and more enterprises are shifting from a closed environment to an open global supply chain, where the enterprises purchase modules or components from suppliers in the chain. The benefit of global procurement has prompted researchers to pay attention to joint research on product configuration with supply chains. For instance, Huang et al. [24] employed Nash game theory to optimize both product configuration and supplier selection problem. Further, Huang et al. [39] also proposed linear programming approach to minimizing the total cost of supply chains with respect to product module design. Similarly, Kumar and Chatterjee [40] applied a mixed-integer programming (MIP) model to jointly optimize product configuration and the corresponding supply chain. Cao et al. [41] utilized consumer choice theory to capture the probability of selecting the final products, and then the product configuration problems were combined with the supplier selection decisions. However, these studies only focus on the supplier selection decisions, and the vital parts such as the production and transportation decisions are not considered. The simultaneous optimization of product modules and supply chains was also proposed by Khalaf et al. [42], Gupta and Krishnan [43]. Luo et al. [44] developed a unified optimization model in which the outsourcing-related cost and supplier selection decisions were considered, and consumer choice theory and supplier availability were employed to choose a product family design. Further, Yang et al. [1] comprehensively studied the joint problem of product by formulating the joint optimization model as a leader-follower Stackelberg game. Nevertheless, the above studies only deal with deterministic supply chains and product configuration problems where configuration parameters such as purchase and shipping costs of components are fixed. As a consequence, the existing product configurator cannot handle well with the uncertainty in the configuration problem.

3 A stochastic decision model for product configuration under uncertainty

## 3.1 Product configuration decision problem

A computer manufacturer adopting ATO (Assemble-to-order) production strategy receives multiple customer orders for customized products which are configured by selecting common and variant components. Due to the fact that all the configured components are offered by suppliers in the supply chain, this manufacturer is just responsible for selecting and assembling the components into an end-item product such that all configuration rules and individualized customer requirements are satisfied. Now, it is assumed that its supply chain may suffer from the uncertainty due to traffic conditions and vehicle troubles and thus the replenishment lead-times for components provided by suppliers are uncertain and random. Before the mathematical model is formulated, essential concepts for product configuration and the developed pre-procuring strategy will be discussed below.

## 3.1.1 Information modeling for product configuration

An example from the literature [45] is given to illustrate the conceptual model for product configuration, as shown in Fig.2. The conceptual model for computer configuration, depicted with AND/OR graph, consists of common components and variant modules. For instance, common components include Shell and Memory whereas variant modules involve Hd-unit, Motherboard, CPU and Server-OS. Moreover, each variant module has its own alternative components. For example, Hd-unit variant module has three types of alternative components, i.e., SATA-disk, IDE-disk and SCSI-disk.

![](/api/attachments/FFX9F84K/fulltext/images/5b3e57eac69151588aa374f057341f8d2b3e53ca5e5f7b17fb0c4447c5dbd58e.jpg)  
Fig.2. Conceptual model for computer configuration

Table 1 Configuration rules for the computer configuration.

<table><tr><td>No.</td><td>Type of configuration rule</td><td>Explanation</td></tr><tr><td>R1</td><td>Selection rule</td><td>IDE-disk requires Motherboard-3 in the same configuration</td></tr><tr><td>R2</td><td>Selection rule</td><td>Motherboard-3 requires CPU-580 in the same configuration</td></tr><tr><td>R3</td><td>Incompatible rule</td><td>Motherboard-2 and CPU-530 are exclusive in a configuration</td></tr><tr><td>R4</td><td>Incompatible rule</td><td>Motherboard-1 and CPU-580 are exclusive in a configuration</td></tr><tr><td>R5</td><td>Selection rule</td><td>OS-2 requires Motherboard-1 in the same configuration</td></tr><tr><td>R6</td><td>Selection rule</td><td>OS-2 requires SCSI-disk in the same configuration</td></tr></table>

For a valid computer configuration, all the common components represented as AND structural restriction must be selected and only one alternative component of variant modules denoted as OR structural restriction could be configured. Besides the above two kinds of structural restrictions, configuration rules exist between components. Generally, there are mainly two types of rules, namely selection rule and incompatible rule. The former defines that the existence of one type of component requires the existence of another type of component in the same configuration, whereas the latter specifies that some types of components cannot be used together in the same final configuration because they are incompatible. The configuration rules for the computer configuration example are shown in Table 1. To take an example, OS-2 requires Motherboard-1 in the same configuration while

CPU-530 is incompatible with Motherboard-2. If we suppose that a customer needs CPU-530 and does not need SATA-disk, it can be easily verified that a valid configuration, which consists of {SCSI-disk, Motherboard-3, CPU-530, OS-2}, satisfies the customer requirements and all rules from R1 to R6 in Table 1.

## 3.1.2 Pre-procuring strategy

Within the context of uncertainty, the manufacture faces the challenge to ensure quick delivery of products even though the uncertainty is realized later in a future moment. At that time, the manufacturer would procure all needed components and assemble the components into an end-item product. Considering that long supply lead-times for components will lead to the late delay in delivering products, the profit of the manufacturer will be adversely affected. The reason is that the price of a product delivered generally depends on the delivery lead-time [49]. Especially, for computers and electronic goods, the pricing function of a product is decreasing in its lead-time due to severe price erosion over time. Therefore, a pre-procuring strategy is proposed in our study to shorten the delivery time of a customized product and avoid the late delivery of the product.

During the product configuration process, the manufacturer pre-procures some components in advance to hedge against the risk caused by the uncertain lead-time, with the aim of delivering customized products as soon as possible and minimizing the total cost. If the customer demands for some component are not satisfied by the pre-procuring strategy, the manufacturer has an opportunity to purchase additional components to meet the remaining demands. The product configuration process with this pre-procuring strategy is illustrated in Fig.3. The configuration steps are elaborated as follows.

![](/api/attachments/FFX9F84K/fulltext/images/d49ebb972becea9f4ae9351efe2499a435754410e5d20ff45c909222d27a9acf.jpg)  
Fig.3. The product configuration process.

Step 1. Configure a product according to customer requirements and select components and corresponding suppliers.

Step 2. Pre-procure components from the selected suppliers with the pre-procuring strategy.

Step 3. Receive the pre-procured components, and then assemble products (called pre-assembled products) and deliver the assembled products to customers.

Step 4. If the product demands for components cannot be met by the pre-procured strategy, the manufacturer purchases additional components from the corresponding suppliers.

Step 5. Receive the additional components and then assemble the remaining products (called additional assembled products) and deliver the final products to customers.

## 3.2 Stochastic model for product configuration decisions

Due to the fact that common components or modules must be selected in each product, decisions on common components are not consider in the objective. Further, some assumptions are made as follows.

Assumption 2. In order to avoid procuring too many components and incurring excessive inventory, the penalty costs for excessive inventory of components are considered.

Assumption 3. No shortage is allowed and the manufacturer must deliver all the required products within the delivery deadlines.

Assumption 4. It is reasonable to assume that the per-unit purchase price of a pre-purchased component is not greater than that of its additionally-purchased component, since there is ample time to prepare for the pre-procurement of components before the deadlines.

Assumption 5. The per-unit selling price of a pre-assembled product is higher than that of its additionally-assembled product. The reason is that the pre-assembled product can be delivered much earlier than the additional product, and the pricing of a product is decreasing function of lead-time.

Assumption 3 can be relaxed and thus the shortage costs for products can be added to the model. To avoid much complexity of the model, however, we choose not to consider shortage costs of products in this study.

The indices, sets, parameters and variables used in the product configuration optimization model are shown in Tables 2-5.

Table 2 Indices.

<table><tr><td>Notation</td><td>Description</td></tr><tr><td>i, h, l</td><td>Index of product, i, h, l ∈ I</td></tr><tr><td>j</td><td>Index of component, j ∈ J</td></tr><tr><td>n</td><td>Index of module, n ∈ N</td></tr><tr><td>k</td><td>Index of supplier, k ∈ K</td></tr><tr><td>ξ</td><td>Index of scenario, ξ ∈ Ξ</td></tr></table>

<table><tr><td colspan="2">Table 3 Sets.</td></tr><tr><td>Notation</td><td>Description</td></tr><tr><td> $I$ </td><td>Set of products</td></tr><tr><td> $J$ </td><td>Set of components</td></tr><tr><td> $N$ </td><td>Set of modules</td></tr><tr><td> $K$ </td><td>Set of suppliers</td></tr><tr><td> $\Xi$ </td><td>Set of scenarios</td></tr><tr><td> $SC_{n}$ </td><td>Set of components that belong to module  $n$ </td></tr><tr><td> $SEL$ </td><td>Set of selection pairs  $(h,l)$  which represents that selection of component  $h$  requires component  $l$  in the same configuration</td></tr><tr><td> $INC$ </td><td>Set of incompatible pairs  $(h,l)$  which represents that component  $h$  and component  $l$  cannot be used together in the same configuration</td></tr><tr><td> $REQI$ </td><td>Set of pair  $(i,j)$ , representing that a customer needs component  $j$  in product  $i$ .</td></tr><tr><td> $REQN$ </td><td>Set of pair  $(i,j)$ , representing that a customer does not need component  $j$  in product  $i$ .</td></tr></table>

<table><tr><td colspan="2">Table 4 Model parameters.</td></tr><tr><td>Notation</td><td>Description</td></tr><tr><td> $t_i$ </td><td>Assembly time for product i</td></tr><tr><td> $\overline{D}_i$ </td><td>Delivery deadline of product i</td></tr><tr><td> $d_i$ </td><td>Demand number of product i</td></tr><tr><td> $v_i$ </td><td>Per unit penalty cost for excess inventory of component j</td></tr><tr><td> $u_{ij}$ </td><td>Number of component j contained in product i if component j is selected</td></tr><tr><td> $f_{ij}$ </td><td>Selection cost of component j in product i</td></tr><tr><td> $w_j$ </td><td>Maximize storage capability for component j</td></tr><tr><td> $c_{jk}$ </td><td>Per unit procurement cost of component j from supplier k</td></tr><tr><td> $l_{jk}^{\xi}$ </td><td>Lead time for component j from supplier k under scenario ξ</td></tr><tr><td> $p_{i0}$ </td><td>Per unit selling price of pre-assembled product i</td></tr><tr><td> $p_{i1}$ </td><td>Per unit selling price of additionally-assembled product i</td></tr><tr><td> $Prob^{\xi}$ </td><td>Probability of scenario ξ</td></tr></table>

Table 5 Decision variables.

<table><tr><td>Notation</td><td>Description</td></tr><tr><td> $\phi_{jk}$ </td><td>Number of pre-procured component  $j$  that is purchased from supplier  $k$ </td></tr><tr><td> $\varphi_{jk}^{\xi}$ </td><td>Number of additional component  $j$  that is purchased from supplier  $k$  in under scenario  $\xi$ . The batch of the components is received at the time  $l_{jk}^{\xi}$ </td></tr><tr><td> $\psi_{i0}^{\xi}$ </td><td>Number of pre-assembled product  $i$  under scenario  $\xi$ </td></tr><tr><td> $\psi_{ijk}^{\xi}$ </td><td>Number of additionally-assembled product  $i$  under scenario  $\xi$  at the time  $l_{jk}^{\xi}$ </td></tr><tr><td> $x_{ij}$ </td><td>Binary decision variable,  $x_{ij} = 1$  indicating where component  $j$  exists in a configuration of product  $i$ ; otherwise  $x_{ij} = 0$ .</td></tr><tr><td> $\tau_{jk}^{\xi}$ </td><td>Binary decision variable,  $\tau_{jk}^{\xi} = 1$  indicating the additional component  $j$  purchased form supplier  $k$  under scenario  $\xi$ ; otherwise  $\tau_{jk}^{\xi} = 0$ .</td></tr></table>

The product configuration decisions with the pre-procurement strategy under the uncertain component replenishment lead-time can be modeled as a two-stage stochastic optimization model. In the first stage, we must decide component selections and the number of the pre-procured components, prior to the realization of stochastic replenishment lead-time. The first-stage decision variable is $x _ { i j }$ , which is a binary variable that takes the value 1 if component ?? is selected in product ??, and 0 otherwise; $\phi _ { j k }$ , which is the number of pre-procured component ?? from supplier ??. The second-stage decisions are the numbers of additionally purchased components, pre-assembled products, and additionally assembled products under some scenario. Let $\varphi _ { j k } ^ { \xi }$ denote the number of additionally purchased component ?? from supplier ?? under scenario ?? , $\psi _ { i 0 } ^ { \xi }$ be the number of pre-assembled product ?? under scenario ??, $\psi _ { i j k } ^ { \xi }$ the number of additionally assembled product ?? under scenario ??. Moreover, a binary decision variable $\tau _ { j k } ^ { \xi }$ is also contained in the second-stage, taking the value 1 if additional component ?? is purchased from supplier ?? under scenario $\xi ,$ and 0 otherwise.

Obviously, the values of the second-stage variables depend on the stochastic problem data, namely component replenishment lead-time. Each possible random value of the problem data is represented as a scenario, which is indexed by $\xi \in \Xi ,$ , with corresponding probability $P r o b ^ { \xi }$

The objective of the product configuration problem under uncertainty is to maximize the expected total profit, namely total revenue minus the total costs. The total revenue includes the revenue of delivering customized products whereas the total cost contains the configuration costs, procurement costs and penalty costs of the excessive components.

The stochastic decision model for product configuration under the uncertain component replenishment lead-time is thus formulated as follows.

[PC\_SP]:

$$
\begin{array}{r l} & {\max - \left(\sum_ {i \in I} \sum_ {j \in J} f _ {i j} u _ {i j} x _ {i j} + \sum_ {j \in J} \sum_ {k \in K} c _ {j k} \phi_ {j k}\right)} \\ & {\qquad - \sum_ {j \in J} v _ {j} \left(\sum_ {k \in K} \phi_ {j k} - \sum_ {i \in I} d _ {i} u _ {i j} x _ {i j}\right) ^ {+}} \\ & {+ \sum_ {\xi \in \Xi} P r o b ^ {\xi} \{\sum_ {i \in I} \Psi_ {i 0} ^ {\xi} p _ {i 0} + \sum_ {i \in I} \sum_ {j \in J} \sum_ {k \in K} \Psi_ {i j k} ^ {\xi} p _ {i 1} - \sum_ {j \in J} \sum_ {k \in K} c _ {j k} \varphi_ {j k} ^ {\xi} \}} \end{array}\tag{1}
$$

$$
s. t.
$$

$$
\sum_ {j \in S C _ {n}} x _ {i j} = 1
$$

$$
i \in I, n \in N\tag{2}
$$

$$
x _ {i h} \leq x _ {i l}
$$

$$
i \in I, (h, l) \in S E L\tag{3}
$$

$$
x _ {i h} + x _ {i l} \leq 1
$$

$$
i \in I, (h, l) \in I N C\tag{4}
$$

$$
x _ {i j} = 1
$$

$$
(i, j) \in R E Q I\tag{5}
$$

$$
x _ {i j} = 0
$$

$$
(i, j) \in R E Q N\tag{6}
$$

$$
\sum_ {k \in K} (\phi_ {j k} + \varphi_ {j k} ^ {\xi}) \geq \sum_ {i \in I} d _ {i} u _ {i j} x _ {i j}
$$

$$
j \in J, \xi \in \Xi\tag{7}
$$

$$
\sum_ {k \in K} (\phi_ {j k} + \varphi_ {j k} ^ {\xi}) \leq M \sum_ {i \in I} x _ {i j}
$$

$$
j \in J, \xi \in \Xi\tag{8}
$$

$$
\sum_ {i \in I} \Psi_ {i 0} ^ {\xi} u _ {i j} x _ {i j} \leq \sum_ {k \in K} \phi_ {j k}
$$

$$
j \in J, \xi \in \Xi\tag{9}
$$

$$
\sum_ {i \in I} \Psi_ {i 0} ^ {\xi} u _ {i j} x _ {i j}
$$

$$
+ \sum_ {j ^ {\prime} \in J} \sum_ {k ^ {\prime}: l _ {j ^ {\prime} k ^ {\prime}} ^ {\xi} \leq l _ {j ^ {\prime \prime} k ^ {\prime \prime}} ^ {\xi}} \sum_ {i \in I} \Psi_ {i j ^ {\prime} k ^ {\prime}} ^ {\xi} u _ {i j} x _ {i j}
$$

$$
j, j ^ {\prime \prime} \in J, k ^ {\prime \prime} \in K, \xi \in \Xi\tag{10}
$$

$$
\leq \sum_ {k \in K} \phi_ {j k} + \sum_ {k: l _ {j k} ^ {\xi} \leq l _ {j ^ {\prime \prime} k ^ {\prime \prime}} ^ {\xi}} \varphi_ {j k} ^ {\xi}
$$

$$
t _ {i} + m a x _ {\Psi_ {i j k} ^ {\xi} > 0} \left\{l _ {j k} ^ {\xi} \right\} \leq \overline {{D}} _ {i}
$$

$$
i \in I, j \in J, k \in K, \xi \in \Xi\tag{11}
$$

$$
\Psi_ {i 0} ^ {\xi} + \sum_ {j \in J} \sum_ {k \in K} \Psi_ {i j k} ^ {\xi} = d _ {i}
$$

$$
i \in I, \xi \in \Xi\tag{12}
$$

## ACCEPTED MANUSCRIPT

$$
\varphi_ {j k} ^ {\xi} \leq \sum_ {i \in I} d _ {i} u _ {i j} \tau_ {j k} ^ {\xi}
$$

$$
j \in J, k \in K, \xi \in \Xi\tag{13}
$$

$$
\varphi_ {j k} ^ {\xi} \geq \tau_ {j k} ^ {\xi}
$$

$$
j \in J, k \in K, \xi \in \Xi\tag{14}
$$

$$
\Psi_ {i j k} ^ {\xi} \leq d _ {i} \tau_ {j k} ^ {\xi}
$$

$$
i \in I, j \in J, k \in K, \xi \in \Xi\tag{15}
$$

$$
\sum_ {k \in K} \phi_ {j k} \leq w _ {j}
$$

$$
j \in J\tag{16}
$$

$$
\tau_ {j k} ^ {\xi} = \{0, 1 \}
$$

$$
j \in J, k \in K, \xi \in \Xi\tag{17}
$$

$$
x _ {i j} = \{0, 1 \}
$$

$$
i \in I, j \in J\tag{18}
$$

$$
\phi_ {j k}, \varphi_ {j k} ^ {\xi}, \Psi_ {i 0} ^ {\xi}, \Psi_ {i j k} ^ {\xi} \geq 0
$$

$$
i \in I, j \in J, k \in K, \xi \in \Xi\tag{19}
$$

The objective is to maximize the expected total profit. The first two terms of the objective function represent the configuration cost and pre-purchase costs for components, and the third term denotes the penalty costs for excessive components. The last term is the expected revenue from delivering customized products minus the expected costs for additional components. Constraints (2) specify that only one type of variant component can be selected from the alternative components of a variant module. C straints (3) represent the selection rule between components whereas constraints (4) are the incompatible rules. Constraints (5-6) $\mathrm { f o r }$ mized products. Constraints (7) ensure that both numbers of the pre-purchased and additional components satisfy the requirements of the orders. Constraints (8) enforce that a component can only be purchased if it is selected in any configuration of products. Note that in constraints (8) and the later constraints, M is a sufficiently large positive number. Constraints (9) state that the number of a component used for pre-assembled products does not exceed that of the component by pre-procuring. Similarly, Constraints (10) ensure that the number of the components required for assembling additional products is no more than that of the available components. In the formula, $l _ { j " k " } ^ { \xi }$ is the maximal lead-time of component ?? that satisfies the inequality, considering that the component may be provided by different suppliers with different delivery times. Constraints (11) guarantee that the delivery lead time of products is less than or equal to the delivery deadline required by customers. Constraints (12) ensure that the demands are satisfied by the sum of the pre-assembled products and the additional assembled products. Constraints (13-15)

specify that the number of additional assembled products depends on that of additional components and their corresponding suppliers. The capacity restrictions are enforced by constraints (16), which say that the number of pre-procured components should not exceed its maximum storage capacity. Constraints (17-19) restrict decision variables.

## 4 Solving method for stochastic decision models

The above decision model for product configuration under uncertain component lead-time is a nonlinear mixed-integer programming model, due to both the objective (1) and the constraints (9-11). Thus, it is crucial to transform the nonlinear model into a linear one in order to reduce the complexity of the model. Furthermore, Lagrangian relaxation algorithm [46-47] is adopted to improve the computation efficiency $\mathrm { o f }$ the linearized model where the constraints (12) are relaxed. Lagrangian relaxation algorithm has been widely applied as an effective solving method for the mixed-integer linear programming, quadratic programming and large-scale mathematical programming as well as stochastic programming.

## 4.1 Linearization methods

The following linearization technologies are applied to transform the nonlinear objective and nonlinear constrains into linear ones. Firstly, the formulation $\begin{array} { r } { { ' } \sum _ { j \in J } v _ { j } \left( \sum _ { k \in K } \phi _ { j k } - \right. } \end{array}$ $\textstyle \sum _ { i \in I } d _ { i } u _ { i j } x _ { i j } ) ^ { + ^ { \prime } }$ in the objective can be transferred to a normal mixed- integer programming formulation by defining a continuous variable $\theta _ { j }$ and a binary variable $\eta _ { j }$ . Constraints (20-24) are defined to remove the form $^ \prime ( . ) ^ { + \prime }$ from the objective.

$$
\theta_ {j} \geq \sum_ {k \in K} \phi_ {j k} - \sum_ {i \in I} d _ {i} u _ {i j} x _ {i j}
$$

$$
j \in J\tag{20}
$$

$$
\theta_ {j} \leq \sum_ {k \in K} \phi_ {j k} - \sum_ {i \in I} d _ {i} u _ {i j} x _ {i j} + M \eta_ {j}
$$

$$
j \in J\tag{21}
$$

$$
\theta_ {j} \leq M (1 - \eta_ {j})
$$

$$
j \in J\tag{22}
$$

$$
\theta_ {j} \geq 0
$$

$$
j \in J\tag{23}
$$

$$
\eta_ {j} = \{0, 1 \}
$$

$$
j \in J\tag{24}
$$

Secondly, constrains (9-10) are nonlinear constraints because the form $\mathbf { \nabla } ^ { \prime } \Psi _ { i 0 } ^ { \xi } u _ { i j } x _ { i j }$ ′and′ $\Psi _ { i j ^ { \prime } k ^ { \prime } } ^ { \xi } u _ { i j } x _ { i j }$ ′are involved. Here, we define $\Theta _ { i j 0 } ^ { \xi } = \Psi _ { i 0 } ^ { \xi } x _ { i j }$ , and constraints (25-29) are employed to linearize constraint (9) as below.

$$
\Theta_ {i j 0} ^ {\xi} \leq \Psi_ {i 0} ^ {\xi}
$$

$$
i \in I, j \in J, \xi \in \Xi\tag{25}
$$

$$
\Theta_ {i j 0} ^ {\xi} \leq M x _ {i j}
$$

$$
i \in I, j \in J, \xi \in \Xi\tag{26}
$$

$$
\Theta_ {i j 0} ^ {\xi} \geq \Psi_ {i 0} ^ {\xi} - M (1 - x _ {i j})
$$

$$
i \in I, j \in J, \xi \in \Xi\tag{27}
$$

$$
\Theta_ {i j 0} ^ {\xi} \geq 0
$$

$$
i \in I, j \in J, \xi \in \Xi\tag{28}
$$

$$
\sum_ {i \in I} \Theta_ {i j 0} ^ {\xi} u _ {i j} \leq \sum_ {k \in K} \phi_ {j k}
$$

$$
j \in J, \xi \in \Xi\tag{29}
$$

Likewise, we define $\Lambda _ { i j j ^ { \prime } k ^ { \prime } } ^ { \xi } = \Psi _ { i j ^ { \prime } k ^ { \prime } } ^ { \xi } x _ { i j }$ for constraint (10), and the linearized result is represented by the following constraints (30-34).

$$
\Lambda_ {i j j ^ {\prime} k ^ {\prime}} ^ {\xi} \leq \Psi_ {i j ^ {\prime} k ^ {\prime}} ^ {\xi}
$$

$$
i \in I, j \in J, k \in K, j ^ {\prime} \in J, k ^ {\prime} \in K, \xi \in \Xi\tag{30}
$$

$$
\Lambda_ {i j j ^ {\prime} k ^ {\prime}} ^ {\xi} \leq M x _ {i j}
$$

$$
i \in I, j \in J, k \in K, j ^ {\prime} \in J, k ^ {\prime} \in K, \xi \in \Xi\tag{31}
$$

$$
\Lambda_ {i j j ^ {\prime} k ^ {\prime}} ^ {\xi} \geq \Psi_ {i j ^ {\prime} k ^ {\prime}} ^ {\xi} - M (1 - x _ {i j})
$$

$$
i \in I, j \in J, k \in K, j ^ {\prime} \in J, k ^ {\prime} \in K, \xi \in \Xi\tag{32}
$$

$$
\Lambda_ {i j j ^ {\prime} k ^ {\prime}} ^ {\xi} \geq 0
$$

$$
i \in I, j \in J, k \in K, j ^ {\prime} \in J, k ^ {\prime} \in K, \xi \in \Xi\tag{33}
$$

$$
\sum_ {i \in I} \theta_ {i j 0} ^ {\xi} u _ {i j}
$$

$$
+ \sum_ {j ^ {\prime} \in J} \sum_ {k ^ {\prime}: l _ {j ^ {\prime} k ^ {\prime}} ^ {\xi} \leq l _ {j ^ {\prime \prime} k ^ {\prime \prime}} ^ {\xi}} \sum_ {i \in I} \Lambda_ {i j j ^ {\prime} k ^ {\prime}} ^ {\xi} u _ {i j}
$$

$$
i \in I, j \in J, k \in K, j ^ {\prime} \in J, k ^ {\prime} \in K, \xi \in \Xi\tag{34}
$$

$$
\leq \sum_ {k \in K} \phi_ {j k} + \sum_ {k: l _ {j k} ^ {\xi} \leq l _ {j ^ {\prime \prime} k ^ {\prime \prime}} ^ {\xi}} \varphi_ {j k} ^ {\xi}
$$

Similarly, the nonlinear constraint (11) is replaced by constraints (35-38).

$$
\Psi_ {i j k} ^ {\xi} \leq M \alpha_ {i j k} ^ {\xi}
$$

$$
i \in I, j \in J, k \in K, \xi \in \Xi\tag{35}
$$

$$
\Psi_ {i j k} ^ {\xi} \geq \alpha_ {i j k} ^ {\xi}
$$

$$
i \in I, j \in J, k \in K, \xi \in \Xi\tag{36}
$$

$$
t _ {i} + l _ {j k} ^ {\xi} \alpha_ {i j k} ^ {\xi} \leq \overline {{D}} _ {i}
$$

$$
i \in I, j \in J, k \in K, \xi \in \Xi\tag{37}
$$

$$
\alpha_ {i j k} ^ {\xi} = \{0, 1 \}
$$

$$
i \in I, j \in J, k \in K, \xi \in \Xi\tag{38}
$$

Then the nonlinear product configuration optimization stochastic model in Section 3.2 can be transferred to the following stochastic mixed-integer linear programming [PC\_SMILP]

model.

[PC\_SMILP]:

$$
\begin{array}{r l} & {\max - \left(\sum_ {i \in I} \sum_ {j \in J} f _ {i j} u _ {i j} x _ {i j} + \sum_ {j \in J} \sum_ {k \in K} c _ {j k} \phi_ {j k}\right) - \sum_ {j \in J} v _ {j} \theta_ {j}} \\ & {+ \sum_ {\xi \in \Xi} P r o b ^ {\xi} \{\sum_ {i \in I} \psi_ {i 0} ^ {\xi} p _ {i 0} + \sum_ {i \in I} \sum_ {j \in J} \sum_ {k \in K} \psi_ {i j k} ^ {\xi} p _ {i 1} - \sum_ {j \in J} \sum_ {k \in K} c _ {j k} \varphi_ {j k} ^ {\xi} \}} \end{array}\tag{39}
$$

s.t. Constraints (2-8), (12-38).

## 4.2 Model solution with Lagrangian relaxation algorithm

In this section, Lagrangian relaxation algorithm is applied to improve the computation efficiency of the above mixed-integer linear configuration problem. This algorithm is utilized to find lower bounds on the given configuration optimization problem. The fundamental theory of Lagrangian relaxation algorithm is to use lagrangian multiplier to move difficult constraints to the objective while keeping the objective function linear. In this way, the difficult original configuration problem has been reduced to an easy-solvable problem. Thus, computation for solving medium or large-scale configuration problem.

To solve the above mixed-integer linear configuration problem [PC\_SMILP], we relax constraints (12) by moving these constraints into the objective and associating them with lagrangian multipliers $\beta _ { i } ^ { \xi } ( i \in I , \xi \in \Xi )$ . The Lagrangian relaxation problem LR (??) for product configuration becomes as follows.

[PC\_LR]:

$$
\begin{array}{r l} & L R (\beta) \colon \min - (- \left(\sum_ {i \in I} \sum_ {j \in J} f _ {i j} u _ {i j} x _ {i j} + \sum_ {j \in J} \sum_ {k \in K} c _ {j k} \phi_ {j k}\right) - \sum_ {j \in J} v _ {j} \theta_ {j} \\ & \qquad + \sum_ {\xi \in \Xi} P r o b ^ {\xi} \{\sum_ {i \in I} \Psi_ {i 0} ^ {\xi} (p _ {i 0} - \beta_ {i} ^ {\xi}) \\ & \qquad \qquad + \sum_ {i \in I} \sum_ {j \in J} \sum_ {k \in K} \Psi_ {i j k} ^ {\xi} (p _ {i 1} - \beta_ {i} ^ {\xi}) - \sum_ {j \in J} \sum_ {k \in K} c _ {j k} \varphi_ {j k} ^ {\xi} + d _ {i} \beta_ {i} ^ {\xi} \}) \end{array}\tag{40}
$$

s.t. Constraints (2-8), (12-38).

The objective function value of Lagrangian relaxation problem is less than that of the original configuration optimization model. To obtain the best lagrangian lower bound of the original configuration model, a sub-gradient method is adopted to approximately solve the following lagrangian dual problem.

## LD: <sup>max</sup> <sup>(</sup> <sup>)LR</sup>

The sub-gradient method is an iterative process, which solves the Lagrangian-relaxed problem and updates the stochastic lagrangian multipliers for the next iteration using the current sub-gradient information. The process is terminated if the maximum number of iterations is reached or the lower bound value of the configuration problem has not been improved within a given number of successive iterations.

Let $( \Psi _ { i 0 } ^ { \xi ( \pi ) } , \Psi _ { i j k } ^ { \xi ( \pi ) } )$ be the optimal solution of ${ \cal L R } ( \beta _ { i } ^ { \xi ( \pi ) } )$ at iteration π. Then we define

$$
\rho_ {i} ^ {\xi (\pi)} = d _ {i} - \Psi_ {i 0} ^ {\xi (\pi)} - \sum \sum \sum \Psi_ {i j k} ^ {\xi (\pi)}
$$

$$
i \in I, \xi \in \Xi\tag{41}
$$

The multipliers for the next iteration are updated as

$$
\beta_ {i} ^ {\xi (\pi + 1)} = \beta_ {i} ^ {\xi (\pi)} + \gamma^ {(\pi)} \rho_ {i} ^ {\xi (\pi)}
$$

$$
i \in I, \xi \in \Xi\tag{42}
$$

Where

$$
\gamma^ {(\pi)} = \frac {\lambda (B U B - L R (\beta_ {i} ^ {\xi (\pi)})}{\sum_ {i \in I} \sum_ {\xi \in \Xi} (d _ {i} - \Psi_ {i 0} ^ {\xi (\pi)} - \sum_ {j \in J} \sum_ {k \in K} \Psi_ {i j k} ^ {\xi (\pi)}) ^ {2}}\tag{43}
$$

In the sub-gradient optimization procedure, BUB and BLB are the best upper bound and the best lower bound for the optimal value of the original configuration problem, respectively. BUB is one of the feasible configuration solutions corresponding objective function value. ?? is a parameter in the interval (0,2], which is halved if the best lower bound has not been improved for a given number of consecutive iterations. The sub-gradient optimization procedure of the uncertain configuration optimization problem is shown in Algorithm I.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm I. Sub-gradient Optimization Procedure for uncertain configuration problem.

Parameter setting: BLB := -∞, Π := 120, π := 0, λ := 2, ε := 0.1, N := 10, β$_{i}^{\xi(0)}$ := 0, i ∈ I, ξ ∈ Ξ.

While (π &lt; Π and λ &gt; ε)
    {
    Step1: Solve the Lagrangian relaxation configuration problem LR(β$_{i}^{\xi(\pi)}$) to optimality, get the
</div>

<table><tr><td></td><td>objective function value (LR), and the values of the variables  $\Psi_{i0}^{\xi(\pi)}$  and  $\Psi_{ijk}^{\xi(\pi)}$  are obtained at the same time.</td></tr><tr><td>Step2:</td><td>If  $Obj(LR) > BLB$  then set  $BLB := Obj(LR)$ . If no improvement of  $BLB$  can be detected in N successive iterations, then set  $\lambda := \lambda/2$ ; otherwise stop.</td></tr><tr><td>Step3:</td><td>Set  $\pi := \pi + 1$ , update  $\beta_i^{\xi(\pi)}$  for  $i \in I, \xi \in \Xi$  according to constraints (41-43).</td></tr></table>

## 5 Case studies of product configuration decisions

The case studies in industrial setting are performed to demonstrate the effectiveness of the presented stochastic decision model and the efficiency of the Lagrangian relaxation algorithm.

## 5.1 Configuration results for the computer case

For the computer configuration case in Fig.2, we suppose that a manufacturer has received three customer orders for three different individually customized computers, i.e., P1, P2 and P3. All variant components can be purchased from two suppliers (i.e., supplier A and supplier B). The lead-time for component replen hment is stochastic and obeys uniform distribution. The experiment settings are listed in Tables 6-8. These settings are on the basis of the data extracted from an actual computer assembly system. Meanwhile, some values are necessarily altered to protect the proprietary information.

Table 6 Parameters for test problems (baselines).

<table><tr><td rowspan="2" colspan="2">Component</td><td colspan="3">Hd-unit</td><td colspan="3">Motherboard</td><td colspan="2">CPU</td><td colspan="2">Server-OS</td></tr><tr><td>SATA-disk</td><td>IDE-disk</td><td>SCSI-disk</td><td>Mother-board-1</td><td>Mother-board-2</td><td>Mother-board-3</td><td>CPU-530</td><td>CPU-580</td><td>OS_1</td><td>OS_2</td></tr><tr><td rowspan="2">Lead-time (day)</td><td>Supplier A</td><td></td><td></td><td></td><td></td><td colspan="2"> $U (2,50)^a$ </td><td></td><td></td><td></td><td></td></tr><tr><td>Supplier B</td><td></td><td></td><td></td><td colspan="5">Supplier A lead time*U (0.2,0.8)</td><td></td><td></td></tr><tr><td rowspan="2">Unit cost ($)</td><td>Supplier A</td><td>49</td><td>40</td><td>58</td><td>149</td><td>164</td><td>209</td><td>115</td><td>157</td><td>60</td><td>90</td></tr><tr><td>Supplier B</td><td>73</td><td>50</td><td>76</td><td>169</td><td>192</td><td>247</td><td>150</td><td>205</td><td>93</td><td>125</td></tr><tr><td colspan="2">Configuration cost($)</td><td>17</td><td>10</td><td>21</td><td>53</td><td>62</td><td>82</td><td>30</td><td>53</td><td>22</td><td>28</td></tr><tr><td colspan="2">Salvage value($)</td><td>26</td><td>11</td><td>16</td><td>76</td><td>114</td><td>56</td><td>67</td><td>83</td><td>17</td><td>59</td></tr><tr><td colspan="2">Maximize storage capacity(number)</td><td>470</td><td>545</td><td>480</td><td>430</td><td>530</td><td>420</td><td>580</td><td>560</td><td>585</td><td>425</td></tr></table>

U (2, 50) <sup>a</sup>: Uniform distribution between 2 and 50.

Table 7 Scenario set and probability of occurrence under component replenishment lead-time uncertainty (baselines).

<table><tr><td>Scenario</td><td>Supplier</td><td>SATA-disk</td><td>IDE-disk</td><td>SCSI-disk</td><td>Mother-board-1</td><td>Mother-board-2</td><td>Mother-board-3</td><td>CPU-530</td><td>CPU-580</td><td>OS_1</td><td>OS_2</td><td>Probability</td></tr><tr><td rowspan="2">S=1</td><td>A</td><td>14.58</td><td>33.19</td><td>19.33</td><td>22.56</td><td>33.35</td><td>23.34</td><td>30.75</td><td>15.09</td><td>25.00</td><td>25.89</td><td rowspan="2">0.40</td></tr><tr><td>B</td><td>5.17</td><td>16.07</td><td>10.66</td><td>8.09</td><td>19.00</td><td>11.81</td><td>9.22</td><td>11.09</td><td>12.03</td><td>15.00</td></tr><tr><td rowspan="2">S=2</td><td>A</td><td>19.51</td><td>13.12</td><td>29.34</td><td>28.56</td><td>13.35</td><td>33.37</td><td>10.75</td><td>19.09</td><td>19.00</td><td>47.08</td><td rowspan="2">0.30</td></tr><tr><td>B</td><td>5.17</td><td>6.07</td><td>15.12</td><td>18.45</td><td>9.00</td><td>21.12</td><td>4.22</td><td>11.06</td><td>2.03</td><td>28.16</td></tr><tr><td rowspan="2">S=3</td><td>A</td><td>11.82</td><td>39.02</td><td>27.58</td><td>19.52</td><td>42.72</td><td>4.39</td><td>12.54</td><td>5.76</td><td>41.60</td><td>32.05</td><td rowspan="2">0.30</td></tr><tr><td>B</td><td>3.31</td><td>26.91</td><td>14.51</td><td>13.43</td><td>33.34</td><td>1.52</td><td>8.95</td><td>2.70</td><td>11.61</td><td>18.00</td></tr></table>

Table 8 Product requirements (baselines).

<table><tr><td rowspan="2">No.</td><td colspan="2">Unit price ($)</td><td rowspan="2">Demand (number)</td><td rowspan="2">Delivery deadline (day)</td><td rowspan="2">Assembly time (day)</td><td rowspan="2">Customer requirements</td></tr><tr><td>Pre-assembled products</td><td>Additional assembled products</td></tr><tr><td>P1</td><td>1112</td><td>1002</td><td>500</td><td>25</td><td>0.083</td><td>Q1:(P1, SCSI-disk)</td></tr><tr><td>P2</td><td>1076</td><td>960</td><td>655</td><td>40</td><td>0.104</td><td>Q2:(P2, CPU-530)</td></tr><tr><td>P3</td><td>1022</td><td>893</td><td>390</td><td>15</td><td>0.124</td><td>Q1:(P3, Motherboard-3)</td></tr></table>

Table 9 Configuration results based on the baselines.

<table><tr><td colspan="3">Components</td><td>SATA-</td><td>IDE-</td><td>SCSI-</td><td>MB-1</td><td>MB-2</td><td>MB-3</td><td>CPU-530</td><td>CPU-580</td><td>OS_1</td></tr><tr><td rowspan="3">Product</td><td colspan="2">P1</td><td></td><td></td><td>+</td><td>+</td><td></td><td></td><td>+</td><td></td><td>+</td></tr><tr><td colspan="2">P2</td><td>+</td><td></td><td></td><td></td><td>+</td><td></td><td></td><td>+</td><td>+</td></tr><tr><td colspan="2">P3</td><td></td><td>+</td><td></td><td></td><td></td><td>+</td><td></td><td>+</td><td>+</td></tr><tr><td rowspan="4">Number of components</td><td colspan="2">Pre-procuring</td><td>470(A)</td><td>390(A)</td><td>480(A)</td><td>430(A)</td><td>530(A)</td><td>390(A)</td><td>500(A)</td><td>560(A)</td><td>585(A)</td></tr><tr><td rowspan="3">Additional procuring</td><td>s=1</td><td>185(A)</td><td>-</td><td>20(A)</td><td>70(A)</td><td>125(A)</td><td>-</td><td>-</td><td>485(A)</td><td>655(A)</td></tr><tr><td>s=2</td><td>185(A)</td><td>-</td><td>20(B)</td><td>70(B)</td><td>125(A)</td><td>-</td><td>-</td><td>485(A)</td><td>960(A)</td></tr><tr><td>s=3</td><td>185(A)</td><td>-</td><td>20(B)</td><td>70(A)</td><td>125(B)</td><td>-</td><td>-</td><td>485(A)</td><td>960(B)</td></tr></table>

Total profit: \$880644

The stochastic decision model PC\_SMILP is implemented by programming with CPLEX12.4 on a PC with 2.5GHz quad-core processor and 4GB memory in the experiments. Table 9 lists optimal configuration solutions that are derived on the basis of above benchmark parameters settings. The symbol “+” in the table represents that a component is configured in a customized product. Row 5 displays the number of purchased components and the selected supplier in the pre-procuring stage, such as 390(A), while those in the additional procuring stage are given in rows 6-8.

## 5.2 Experiments on the Efficiency of the Lagrangian relaxation algorithm

To better evaluate the efficiency of Lagrangian relaxation algorithm in a real industrial configuration setting, a configurable ranger drilling machine with ten variant modules and thirty alternative components from the literature [50] is further adopted in this study. The corresponding sub-assembly, modules and components are depicted in Table 10. We set the random component replenishment lead-time to follow uniform distribution in this case. The configuration cost, salvage value, maximal storage capacity, the number of demand, the assembly time of each customized machine, and the sale prices are randomly generated. The problem instances with different scale sizes are tested with the presented algorithm. The sizes of instances are represented by the number of customer orders |I|, components |J|, suppliers |K|, modules |M|, scenarios |Ξ| and the suffix where the capital letters C and D represent the computer case and drilling machine case, respectively. The experimental results for both compute and drilling machine cases are compared with those directly solved by CPLEX, which are shown in Table 11. It can be seen that even for large instances, the presented Lagrangian relaxation is roughly 2.5 times faster than CPLEX.

Table 10 A configurable ranger drilling machine

<table><tr><td>Assembly</td><td>Module</td><td>Component</td></tr><tr><td rowspan="2">Fuel Tank</td><td rowspan="2">Extra fuel filling pump</td><td>Normal pump</td></tr><tr><td>High capacity pump</td></tr><tr><td rowspan="8">Power unit assembly</td><td rowspan="3">Engine</td><td>Engine R (108Kw)</td></tr><tr><td>Engine S (135Kw)</td></tr><tr><td>Engine T (119Kw)</td></tr><tr><td rowspan="3">PA tank</td><td>Tank USA</td></tr><tr><td>Tank AUS</td></tr><tr><td>Tank EURO</td></tr><tr><td rowspan="2">Air conditioning</td><td>AC5</td></tr><tr><td>AC6&amp;7</td></tr><tr><td rowspan="7">Drill boom assembly</td><td rowspan="2">Boom attachment</td><td>Light boom attachment (LBA)</td></tr><tr><td>High boom attachment (HBA)</td></tr><tr><td rowspan="2">Drill attachment</td><td>Light drill attachment(LDA)</td></tr><tr><td>High drill attachment(HDA)</td></tr><tr><td rowspan="3">Rock-drill</td><td>HL500 (LBA) 108Kw</td></tr><tr><td>HL600 (HBA) 108Kw</td></tr><tr><td>HL700 (HBA) 135Kw</td></tr></table>

## ACCEPTED MANUSCRIPT

<table><tr><td rowspan="6">Craw assembly</td><td rowspan="2">Tracks</td><td>Three edge track</td></tr><tr><td>Normal track</td></tr><tr><td rowspan="2">Winch</td><td>Winch1</td></tr><tr><td>Winch2</td></tr><tr><td rowspan="2">Jack</td><td>Rear jack A</td></tr><tr><td>Rear jack B</td></tr></table>

Table 11 Comparison with CPLEX

<table><tr><td rowspan="2">Case idI-J-K-Ξ-ID</td><td colspan="2">Lagrangian relaxation</td><td colspan="2">CPLEX</td><td rowspan="2">Gap (%)</td></tr><tr><td>Obj.</td><td>Time(s)</td><td>Obj.</td><td>Time(s)</td></tr><tr><td>3-10-2-3C-1</td><td>849434</td><td>0.09</td><td>849434</td><td>5</td><td>0</td></tr><tr><td>3-15-2-3C-2</td><td>552835</td><td>0.12</td><td>552393</td><td>11</td><td>0.08</td></tr><tr><td>5-10-2-3C-3</td><td>1562529</td><td>0.16</td><td>1561592</td><td>13</td><td>0.06</td></tr><tr><td>5-15-2-3C-4</td><td>1206461</td><td>2.13</td><td>1204413</td><td>189</td><td>0.17</td></tr><tr><td>7-10-2-3C-5</td><td>1764542</td><td>0.23</td><td>1758388</td><td>23</td><td>0.35</td></tr><tr><td>7-15-2-3C-6</td><td>1946764</td><td>3.12</td><td>1935345</td><td>256</td><td>0.59</td></tr><tr><td>12-20-2-3D-1</td><td>13926688</td><td>63</td><td>13834000</td><td>464</td><td>0.67</td></tr><tr><td>12-25-2-3D-2</td><td>11934434</td><td>175</td><td>11831500</td><td>697</td><td>0.87</td></tr><tr><td>12-30-3-5D-3</td><td>12455523</td><td>245</td><td>12343200</td><td>1294</td><td>0.91</td></tr><tr><td>12-35-3-5D-4</td><td>12070934</td><td>453</td><td>11927800</td><td>1982</td><td>1.20</td></tr><tr><td>12-40-3-5D-5</td><td>13586537</td><td>785</td><td>13409531</td><td>3180</td><td>1.32</td></tr><tr><td>12-45-3-5D-6</td><td>13161416</td><td>2472</td><td>12973303</td><td>5741</td><td>1.45</td></tr><tr><td>12-50-3-5D-7</td><td>13791910</td><td>7867</td><td>13582736</td><td>16286</td><td>1.54</td></tr><tr><td>15-20-2-3D-1</td><td>19792587</td><td>236</td><td>19639400</td><td>762</td><td>0.78</td></tr><tr><td>15-25-2-3D-2</td><td>17056060</td><td>321</td><td>16898900</td><td>1083</td><td>0.93</td></tr><tr><td>15-30-3-5D-3</td><td>16968982</td><td>563</td><td>16804300</td><td>2152</td><td>0.98</td></tr><tr><td>15-35-3-5D-4</td><td>17304946</td><td>843</td><td>17044170</td><td>3454</td><td>1.53</td></tr><tr><td>15-40-3-5D-5</td><td>17931822</td><td>3298</td><td>17621680</td><td>9366</td><td>1.76</td></tr><tr><td>15-45-3-5D-6</td><td>17961200</td><td>5527</td><td>17628030</td><td>11355</td><td>1.89</td></tr><tr><td>15-50-3-5D-7</td><td>18633942</td><td>10760</td><td>18282910</td><td>25455</td><td>1.92</td></tr></table>

Note: (1) In ‘??-??-??-??’, ??, ??, ??, ?? denote the numbers of customer orders, components, suppliers, lead-time scenarios, respectively. (2) $\begin{array} { r } { G a p ( \% ) = \frac { L R ( \beta ) - P C \_ S M I L P } { P C \ S M I L P } . } \end{array}$ ∗ 100%.

## 5.3 Comparisons between the pre-procuring strategy and the one-time procuring strategy

In the context of one-time purchasing strategy, a component can only be ordered one-time after the configured components are selected. The corresponding stochastic programming model [OT\_PCSP] can be formulated as follows.

[OT\_PCSP]:

$$
\max - \sum_ {i \in I} \sum_ {j \in J} f _ {i j} u _ {i j} x _ {i j} + \sum_ {\xi \in \Xi} P r o b ^ {\xi} \{\sum_ {i \in I} \sum_ {j \in J} \sum_ {k \in K} \Delta_ {i j k} ^ {\xi} p _ {i} - \sum_ {j \in J} \sum_ {k \in K} o _ {j k} \varrho_ {j k} ^ {\xi} \}\tag{44}
$$

s.t. Constraints (2) - (5), (17) - (18).

$$
\sum_ {k \in K} \varrho_ {j k} ^ {\xi} \geq \sum_ {i \in I} d _ {i} u _ {i j} x _ {i j}
$$

$$
j \in J, \xi \in \Xi\tag{45}
$$

$$
\sum_ {k \in K} \varrho_ {j k} ^ {\xi} \leq M \sum_ {i \in I} x _ {i j}
$$

$$
j \in J, \xi \in \Xi\tag{46}
$$

$$
\sum_ {j ^ {\prime} \in J} \sum_ {k ^ {\prime}: l _ {j ^ {\prime} k ^ {\prime}} ^ {\xi} \leq l _ {j ^ {\prime \prime} k ^ {\prime \prime}} ^ {\xi}} \sum_ {i \in I} \Delta_ {i j ^ {\prime} k ^ {\prime}} ^ {\xi} u _ {i j} x _ {i j} \leq \sum_ {k: l _ {j k} ^ {\xi} \leq l _ {j ^ {\prime \prime} k ^ {\prime \prime}} ^ {\xi}} \varrho_ {j k} ^ {\xi}
$$

$$
j, j ^ {\prime \prime} \in J, k ^ {\prime \prime} \in K, \xi \in \Xi\tag{47}
$$

$$
t _ {i} + m a x _ {\Delta_ {i j k} ^ {\xi} > 0} \left\{l _ {j k} ^ {\xi} \right\} \leq \overline {{D}} _ {i}
$$

$$
i \in I, j \in J, k \in K, \xi \in \Xi\tag{48}
$$

$$
\sum_ {j \in J} \sum_ {k \in K} \Delta_ {i j k} ^ {\xi} = d _ {i}
$$

$$
i \in I, \xi \in \Xi\tag{49}
$$

$$
\varrho_ {j k} ^ {\xi} \leq \sum_ {i \in I} d _ {i} u _ {i j} \tau_ {j k} ^ {\xi}
$$

$$
j \in J, k \in K, \xi \in \Xi\tag{50}
$$

$$
\varrho_ {j k} ^ {\xi} \geq \tau_ {j k} ^ {\xi}
$$

$$
j \in J, k \in K, \xi \in \Xi\tag{51}
$$

$$
\Delta_ {i j k} ^ {\xi} \leq d _ {i} \tau_ {j k} ^ {\xi}
$$

$$
i \in I, j \in J, k \in K, \xi \in \Xi\tag{52}
$$

$$
\varrho_ {j k} ^ {\xi}, \Delta_ {i j k} ^ {\xi} \geq 0
$$

$$
i \in I, j \in J, k \in K, \xi \in \Xi\tag{53}
$$

Here, $o _ { j k }$ indicates the per unit procurement cost of component ?? from supplier ??; $p _ { i }$ denotes the per unit selling price of product ?? ; $\varrho _ { j k } ^ { \xi }$ states the number of the component ?? that is purchased from the supplier ?? in the scenario ??; $\Delta _ { i j k } ^ { \xi }$ represents the number of assembled product ?? at the time $l _ { j k } ^ { \xi }$ under the scenario $\xi$

In above [OT\_PCSP] model, objective (44) is to maximize the total profit. Constraints (45-46) specify that the number of procured components should be larger than or equal to the number of the required components. Constraints (47) enforce that the number of a component assembled in products cannot exceed the available components. Constraints (48) and (49) guarantee the delivery time and the number of delivered customized products required by the customers, respectively. Constraints (50-51) indicate logical relations between the number of assembled products, selected components and corresponding suppliers. Constraints (53) restrict the decision variables.

To compare the proposed pre-procuring strategy with the one-time purchasing strategy, the configuration experiments are carried out under different scales. The comparison results are listed in Table 12. Columns 3, 5 and 6 display total configuration profit for the pre-purchase strategy, total configuration profit for the one-time purchase strategy and the profit gap between the two strategies, respectively. The Avg. delivery times under the two strategies, which represents the mean delivery times of products in each instance, are depicted in columns 2 and 4, respectively. Comparing the results, it is obvious that the pre-purchase strategy outperforms the one-time purchase in more profit and shorter delivery times.

Table 12 Performance of the proposed pre-purchase strategy.

<table><tr><td rowspan="2">Case idI-J-K-Ε-ID</td><td colspan="2">Pre-purchase strategy</td><td colspan="2">One-time purchase strategy</td><td rowspan="2">Profit-Gap</td></tr><tr><td>Avg. delivery time</td><td>Total profit</td><td>Avg. delivery time</td><td>Total profit</td></tr><tr><td>3-10-2-3C-1</td><td>14.17</td><td>970335</td><td>24.4</td><td>761888</td><td>208447</td></tr><tr><td>3-15-2-3C-2</td><td>15.09</td><td>963198</td><td>25.6</td><td>849516</td><td>113682</td></tr><tr><td>5-10-2-3C-3</td><td>16.78</td><td>1719155</td><td>25.96</td><td>1697269</td><td>21886</td></tr><tr><td>5-15-2-3C-4</td><td>16.24</td><td>1983600</td><td>26.31</td><td>1959827</td><td>23773</td></tr><tr><td>7-10-2-3C-5</td><td>13.23</td><td>2320732</td><td>27.97</td><td>2248261</td><td>72471</td></tr><tr><td>7-15-2-3C-6</td><td>14.89</td><td>2172708</td><td>26.37</td><td>2102875</td><td>69833</td></tr><tr><td>10-20-2-3D-1</td><td>28.23</td><td>9821340</td><td>40.76</td><td>9187262</td><td>634078</td></tr><tr><td>12-25-2-3D-2</td><td>31.43</td><td>9912760</td><td>40.05</td><td>9226197</td><td>686563</td></tr><tr><td>15-30-3-5D-3</td><td>34.26</td><td>13128710</td><td>42.18</td><td>12187163</td><td>941547</td></tr><tr><td>18-35-3-5D-4</td><td>37.12</td><td>17108371</td><td>46.23</td><td>15914254</td><td>1194117</td></tr><tr><td>20-40-3-5D-5</td><td>39.98</td><td>19729730</td><td>48.34</td><td>18372610</td><td>1357120</td></tr></table>

## 5.4 Evaluation on the effectiveness of product configuration stochastic model

For comparing the effectiveness of the formulated stochastic decision model with the pre-purchase strategy against determine product configuration models, VSS (the value of the stochastic solution) and EVPI (the expected value perfect information) [18] are adopted. For this configuration problem, VSS measures the cost of ignoring the uncertainty of the component replenishment lead-time when making configuration decisions, whereas EVPI measures the maximum cost that the decision maker would be ready to pay in return for accurate lead-time data before making configuration decisions.

In order to obtain VSS and EVPI, the three models and corresponding objectives are shown in Table 13.

Table 13 Models for VSS and EVPI.

<table><tr><td>Model (or method)</td><td>Objective value</td><td>Measure</td></tr><tr><td>stochastic product configuration model: PC_SP</td><td>RP</td><td></td></tr><tr><td>deterministic product configuration model: PC_DP1</td><td>WS</td><td>VSS=RP-WS</td></tr><tr><td>deterministic product configuration model: PC_DP2</td><td>EEV</td><td>EVPI=EEV-RP</td></tr></table>

The first model with the objective RP is the proposed stochastic product configuration optimization model, namely PC\_SP as formulated in Section 3.2. The similar test instances in Section 5.3 are used. PC\_SP is solved based on the randomly generated scenarios. The second model with the objective WS is a deterministic model and is solved based on the ‘average’ scenario, where the lead-time data is the average value of the previously generated scenarios. Thus, VSS is the gap between PR and WS. The last model with objective EEV is used to derive EVPI where this deterministic model is solved for each generated lead-time scenarios. EEV is the mean value of these models’ objective values. The gap between EEV and RP reflects EVPI. Experimental results for both computer cases and drilling machine cases are shown in Table 14.

Table 14 Analysis on the value of the perfect information (EVPI) and the value of the stochastic solution (VSS).

<table><tr><td>Case idI-J-K-Σ-ID</td><td>RP</td><td>WS</td><td>EEV</td><td>VSS</td><td>EVPI</td></tr><tr><td>3-10-2-3C-1</td><td>830084</td><td>787646</td><td>831053</td><td>42438</td><td>969</td></tr><tr><td>3-15-2-3C-2</td><td>898392</td><td>865136</td><td>901004</td><td>33256</td><td>2612</td></tr><tr><td>5-10-2-3C-3</td><td>1672720</td><td>1647730</td><td>1679590</td><td>24990</td><td>6870</td></tr><tr><td>5-15-2-3C-4</td><td>1432520</td><td>1387950</td><td>1437440</td><td>44570</td><td>4920</td></tr><tr><td>7-10-2-3C-5</td><td>1694988</td><td>1658726</td><td>1699870</td><td>36262</td><td>4882</td></tr><tr><td>7-15-2-3C-6</td><td>1944812</td><td>1890735</td><td>1949231</td><td>54077</td><td>4419</td></tr><tr><td>10-20-2-3D-1</td><td>11438820</td><td>11166600</td><td>11438900</td><td>272220</td><td>80</td></tr><tr><td>12-25-2-3D-2</td><td>15118540</td><td>15027400</td><td>15118800</td><td>91140</td><td>260</td></tr><tr><td>15-30-3-5D-3</td><td>16177210</td><td>15992000</td><td>16178100</td><td>185210</td><td>890</td></tr><tr><td>18-35-3-5D-4</td><td>16806530</td><td>16723000</td><td>16807000</td><td>83530</td><td>470</td></tr><tr><td>20-40-3-5D-5</td><td>20827070</td><td>20718900</td><td>20829000</td><td>108170</td><td>1930</td></tr></table>

The results of VSS indicate that in the case of uncertainty in component replenishment lead-time, stochastic product configuration models can achieve more cost saving in total configuration cost in comparison with the determine configuration model. The decisions obtained by the deterministic model according to the ‘average’ lead-time data may not be the best one when facing uncertainty. Consequently, the results validate the effectiveness of the proposed stochastic optimization model. In addition, it is obvious that the value of EVPI is always a non-negative one, which demonstrates that the profit obtained based on exact information will be greater than that obtained using stochastic programing. Therefore, EVPI can motivate the decision maker to make a more exact prediction of the component replenishment lead-time.

## 6 Conclusions

In this paper, we consider a stochastic decision model for product configuration under the uncertainty in component replenishment lead-time. A pre-purchasing strategy is proposed to shorten the delivery date of a customized product and reduce the total configuration cost. Stochastic programming based on discrete-scenario modeling is used to formulate the product configuration decision problem under both the uncertainty and pre-purchasing strategy. Considering that this model is difficult to handle due to its nonlinearity and complexity, linearization technologies are introduced to transform it into an equivalent linear mixed-integer model. Further, by relaxing complex constraints and moving them into the objective function, Lagrangian algorithm is employed to solve the model more efficiently. Numerical experiments were performed to validate the effectiveness and efficiency of the proposed stochastic decision model.

Nevertheless, there are still some limitations. For instance, a scenario-based discrete stochastic programming requires that decision makers know the probability distributions of stochastic problem data, i.e. component replenishment lead-time. However, it is impractical for decision makers to have the information in some industrial settings. Therefore, a possible extension for future work is to construct a model by taking advantage of the robust optimization approach where the decision makers just need to have the ranges of stochastic problem data, thereby relaxing the restrictions on probability distributions of the uncertain parameters. In addition, another future direction is to investigate the effect of carbon emissions regarding component purchase and transportation on product configuration. Further, decisions on common components under both uncertainty and pre-purchasing strategy should

be investigated in future research.

## Acknowledgments

This research is supported by National Natural Science Foundation of China [Grant No. 71371045].

## References

[1] D. Yang, J. Jiao, Y. Ji, G. Du, P. Helo, A. Valente, Joint optimization for coordinated configuration of product families and supply chains by a leader-follower Stackelberg game, European Journal of Operational Research, 246 (2015) 263-280.

[2] J. Jiao, L. Zhang, S. Pokharel, Z. He, Identifying generic routings for product families based on text mining and tree matching, models, Decision Support Systems, 43 (2007) 866-883.

[3] J. Jiao, M.M. Tseng, A methodology of developing product family architecture for mass customization, Journal of Intelligent Manufacturing, 10 (1999) 3-20.

[4] T.W. Simpson, Product platform design and customization: Status and promise, Artificial Intelligence for Engineering Design Analysis & Manufacturing, 18 (2004) 3-20.

[5] J. Jiao, T.W. Simpson, Z. Siddique, Product family design and platform-based product development: a state-of-the-art review, Journal of Intelligent Manufacturing, 18 (2007) 5-29.

[6] D. Yang, M. Dong, X.K. Chang, A dynamic constraint satisfaction approach for configuring structural products under mass customization, Engineering Applications of Artificial Intelligence, 25 (2012) 1723-1737.

[7] X.F. Shao, Integrated product and channel decision in mass customization, IEEE Transactions on Engineering Management, 60 (2013) 30-45.

[8] F.S. Fogliatto, G.D. Silveira, D. Borenstein, The mass customization decade: An updated review of the literature, International Journal of Production Economics, 138 (2012) 14-25.

[9] Y.X. Feng, B. Zheng, J.R. Tan, Z. Wei, An exploratory study of the general requirement representation model for product configuration in mass customization mode, The International Journal of Advanced Manufacturing Technology, 40 (2009) 785-796.

[10] A. Haag, S. Riemann, Product configuration as decision support: The declarative paradigm in practice, Artificial Intelligence for Engineering Design Analysis & Manufacturing, 25(2011) 131–142.

[11] Richard T. Grenci, An adaptable customer decision support system for custom configurations, Journal of Computer Information Systems, 45(2005) 56-62.

[12] A.F.Barco, E.Vareilles, P.Gaborit, M.Aldanondo, Building renovation adopts mass customization: Configuring insulating envelopes, Journal of Intelligent Information Systems, 49 (2017) 119-146.

[13] J.D. Frutos, E.R. Santos, D. Borenstein, Decision support system for product configuration in mass customization environments, Concurrent Engineering: Research

[14] A. Felfernig, G. Friedrich, D. Jannach, Conceptual modeling for configuration of mass-customizable products, Advanced Engineering Informatics, 15 (2001) 165-176.

[15] S. Shafiee, L. Hvam, A. Haug, M. Dam, K. Kristjansdottir, The documentation of product configuration systems: A framework and an IT solution, Advanced Engineering Informatics, 32 (2017) 163-175.

[16] J. Tiihonen, A. Felfernig. Towards recommending configurable ffferings, International Journal of Mass Customization, 3(2010) 389-406.

[17] A. Falkner, A. Felfernig, A. Haag. Recommendation technologies for configurable products, AI Magazine, AAAI, 32(2011) 99-108.

[18] S. Mittal, F. Frayman, Towards a generic model of configuration tasks, the 11th International Joint Conference on Artificial Intelligence, IJCAI’89, 1989, pp. 1395-1401.

[19] E.P.K. Tsang, Foundations of Constraint Satisfaction, Academic Press, London and San Diego, 1993.

[20] P. Pitiot, M. Aldanondo, E. Vareilles, Concurrent product configuration and process

planning: Some optimization experimental results, Computers in Industry, 65 (2014) 610-621.

[21] J. Mcdermott, A rule-based configurer of computer systems, Artificial Intelligence, 19 (1980) 39-88.

[22] H.E. Tseng, C.C. Chang, S.H. Chang, Applying case-based reasoning for product configuration in mass customization environments, Expert Systems with Applications, 29 (2005) 913-925.

[23] H.J. Lee, J.K. Lee, An effective customization procedure with configurable standard models, Decision Support Systems, 41 (2005) 262-278.

[24] G.Q. Huang, X.Y. Zhang, V.H.Y. Lo, Integrated configuration of platform products and supply chains for mass customization: a game-theoretic approach, IEEE Transactions on Engineering Management, 54 (2007) 156-171.

[25] R.E.H. Khalaf, B. Agard, B. Penz, Simultaneous design of a product family and its related supply chain using a Tabu Search algorithm, International Journal of Production Research, 49 (2011) 5637-5656.

[26] J.R. Birge, F. Louveaux, Introduction to Stochastic Programming, Springer, 1997.

[27] H. Soleimani, M. Seyyed-Esfahani, M.A. Shirazi, A new multi-criteria scenario-based solution approach for stochastic forward/reverse supply chain network design, Annals of Operations Research, 242 (2016) 1-23.

[28] W. Klibi, A. Martel, Scenario-based supply chain network risk modeling, European Journal of Operational Research, 223 (2012) 644-658.

[29] S.M. Davis, Future Perfect, Addison-Wesley, New York, 1987.

[30] B.J. Pine, Mass Customization: The New Frontier in Business Competition, Havard Business School Press, Boston, 1993.

[31] B. Berman, Should your firm adopt a mass customization strategy?, Business Horizons, 45 (2002) 51-60.

[32] V.E. Barker, D.E. O'Connor, J. Bachant, E. Soloway, Expert systems for configuration at Digital: XCON and beyond, Communications of the ACM, 32 (1989) 298-318.

[33] G. Fleishanderl, G.E. Friedrich, A. Haselbock, H. Schreiner, M. Stumptner, Configuring large systems using generative constraint satisfaction, IEEE Intelligent Systems, 13 (1998) 59-68.

[34] S.M. Fohn, J.S. Liau, A.R. Greef, R.E. Young, P.J. O'Grady, Configuring computer systems through constraint-based modeling and interactive constraint satisfaction, Computers in Industry, 27 (1995) 3-21.

[35] P.Y. Chao, T.T. Chen, Analysis of assembly through product configuration, Computers in Industry, 44 (2001) 189-203.

[36] J.Y. Yeh, T.H. Wu, J.M. Chang, Parallel genetic algorithms for product configuration management on PC cluster systems, The International Journal of Advanced Manufacturing Technology, 31 (2007) 1233-1242.

[37] Y.K. Juan, S.G. Shih, Y.H. Perng, Decision support for housing customization: A hybrid approach using case-based reasoning and genetic algorithm, Expert Systems with Applications, 31 (2006) 83-93.

[38] W.J. Yu, J.W. Wang, J. Zhao, X.P. Wei, A hybrid intelligent algorithm for product optimization configuration. International Conference on Machine Learning and Cybernetics, 2007, pp. 2547-2552.

[39] G.Q. Huang, X.Y. Zhang, L. Liang, Towards integrated optimal configuration of platform Management, 23 (2005) 267-290.

[40] S. Kumar, A.K. Chatterjee, A heuristic-based approach to integrate the product line selection decision to the supply chain configuration, International Journal of Production Research, 51 (2013) 2399-2413.

[41] Y. Cao, X.G. Luo, C.K. Kwong, J.F. Tang, W. Zhou, Joint optimization of product family design and supplier selection under multinomial logit consumer choice rule, Concurrent Engineering: Research and Applications, 20 (2012) 335-347.

[42] R.EI.H. Khalaf, B.Agard, B. Penz, An experimental study of a product and supply chain design problem for mass customization, Journal of Intelligent Manufacturing, 21 (2008),

703-716.

[43] S. Gupta, V. Krishnan, Integrated component and supplier selection for a product family, Production and Operations Management, 8 (2009) 163-182.

[44] X.G. Luo, C.K. Kwong, J.F. Tang, S.F. Deng, J. Gong, Integrating supplier selection in optimal product family design, International Journal of Production Research, 49 (2011) 4195-4222.

[45] D. Yang, M. Dong, A constraint satisfaction approach to resolving product configuration conflicts, Advanced Engineering Informatics, 26 (2012) 592–602.

[46] M.L. Fisher, An applications oriented guide to Lagrangian relaxation, Interfaces, 15 (1985) 10-21.

[47] M.L. Fisher, The Lagrangian relaxation method for solving integer programming problems, Management Science, 27(1981) 1–18.

[48] S. Chopra, M. S. Sodhi, Managing risk to avoid: supply-chain breakdown. MIT Sloan Management Review, 46 (2004).

[49] V. N. Hsu, C.Y. Lee, K. C. So, Optimal component stocking policy for assemble-to-order systems with lead-time-dependent component and product pricing, Management Science, 52(2006) 337-351.

[50] J. Tiihonen, T. Lehtonen, T., Soininen, A. Pulkkinen, R. Solunen, A. Riitahuhta, Modeling configurable product families, Proceedings of The 4th WDK Workshop on Product Structuring, Netherlands ,1998, pp. 29-50.

[51] D. Yang, R. Miao, H. Wu, Product configuration knowledge modeling using ontology web language, Expert Systems with Applications, 36(2009) 4399‐4411.

Dr. Dong Yang is a full professor with Department of Management Information System at Donghua University. His research interests include product configuration, operational research and ontology representation. His research has been published in European Journal of Operational Research, Engineering Applications of Artificial Intelligence and Advanced Engineering Informatics.

Xiaohong Li is a mater student with the Department of Management Information System at Donghua University. Her areas of research are product configuration, mass customization and stochastic programming.

Dr. Roger (Jianxin) Jiao is an associate professor with the George W. Woodruff School of Mechanical Engineering at Georgia Institute of Technology. His research interests include mass customization, design theory & methodology, reconfigurable manufacturing systems, engineering logistics, and intelligent systems. His publications appear in IIE Transactions, IEEE Transactions on Engineering Management, Decision Support Systems, Computer-Aided Design, CIRP Annals, Journal of Intelligent Manufacturing, Computers and Operations Research, International Journal of Production Research, etc. He is a member of IEEE, ASME, and IIE.

Bill Wang is a senior tutor with Department of Logistics and Supply Chain at Massey University. His research interests include supply chain management and integration. His research has been published in Industrial Management and Data Systems.

Highlights

Stochastic programming used to formulate product configuration decisions under uncertainty.

 A pre-purchasing strategy is proposed to shorten the delivery times of products.

 Lagrangian relaxation is developed to solve the stochastic model.

 The effectiveness of the stochastic model is demonstrated through case studies.

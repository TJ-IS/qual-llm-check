---
otero_id: 4926
otero_key: "9XZHCGET"
title: "A stochastic model for the implementation of postponement strategies in global distribution networks"
authors: "Stefan Guericke; Achim Koberstein; Frank Schwartz; Stefan Voß"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.01.010"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A stochastic model for the implementation of postponement strategies in global distribution networks

Stefan Guericke <sup>a</sup>, Achim Koberstein <sup>a</sup>, Frank Schwartz <sup>b</sup>, Stefan Voß <sup>b,</sup>⁎

<sup>a</sup> Decision Support and Operations Research Lab, University of Paderborn, Warburger Str. 100, D-33098 Paderborn, Germany <sup>b</sup> Institute of Information Systems, University of Hamburg, Von-Melle-Park 5, D-20146 Hamburg, Germany

## a r t i c l e i n f o

Available online 25 January 2012

Keywords: Postponement Network design Stochastic optimization Supply chain management

## a b s t r a c t

When designing global production and distribution systems an important aspect becoming more and more relevant is the question of how to deal with demand uncertainties. Due to the proliferation of product variants that have to be handled in production and distribution, long lead times due to overseas transportation and increasingly volatile, uncertain and market speci<sup>fi</sup>c demands, an appropriate concept to deal with these problems has to be established. One concept that has been proposed but not yet been fully explored in this context is postponement. In this concept the customization and <sup>fi</sup>nalization of a product is procrastinated. i.e., the final products are not completed in factories but in facilities of a distribution network that are located on the network from factories to customers. This may also entail a resequencing of manufacturing steps.

Until now, research has mainly focused on general statements regarding advantages and disadvantages of postponement strategies. In contrast, quantitative models that allow for decision making for speci<sup>fi</sup>c postponement implementations are rare, particularly models that explicitly take into account stochastic demands and long lead times. In order to allow for decision making for speci<sup>fi</sup>c postponement implementations in uncertain environments, we present a two-stage stochastic mixed integer linear programming model in this paper. We design a case study inspired by decision support issues in the apparel industry. By means of this case study we show that the presented model formulation can support managers to determine an appropriate production and distribution network in uncertain environments. Bene<sup>fi</sup>ts from the concept of postponement are exempli<sup>fi</sup>ed using (commercially) available mathematical programming software.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Modern production and distribution systems are increasingly faced with different requirements such as, e.g., shorter product life cycles, an escalating diversity of variants, or gradually less predictable customer demands. This triggers considerations to procrastinate certain manufacturing steps of a product towards the end of a supply chain. This approach is called postponement. Following this concept, a product is not necessarily <sup>fi</sup>nished at the production site. Instead different manufacturing steps that constitute customer and/or regional requirements may be executed while the product is shipped to the customer. Possible manufacturing steps allowing for procrastination are the assembly of site-speci<sup>fi</sup>c components, the site- and/or customer-speci<sup>fi</sup>c packaging or possibly, e.g., in the apparel industry, the dyeing of garments with a site-speci<sup>fi</sup>c color palette. This approach enables delayed adjustments of production in view of changed customer demands by transferring a generic product from the production site into the distribution network where it is clientspeci<sup>fi</sup>cally individualized at a later stage.

In this paper we consider the postponement approach in the context of a global multi-tier and multi-product distribution network, which is characterized by stochastic demands and long lead times in at least one of its tiers. Long lead times, e.g., caused by overseas transportation, can lead to a decreased validity of demand forecasts and can inhibit later adjustment of previously taken, potentially erroneous production and distribution decisions.

We develop a two-stage stochastic mixed integer linear programming (SMIP) model with the objective of expected pro<sup>fi</sup>t maximization under stochastic demands. Long lead times are considered by an appropriate assignment of decision variables to the stages of the stochastic model. Solutions to the model specify facility locations where different manufacturing steps or activities, respectively, are potentially set up in order to satisfy the given demands. Furthermore, solutions also indicate if postponement strategies should be implemented. Postponement strategies are established by relocating production activities from one tier in the production and distribution system to a subsequent tier as well as by resequencing activities in this system if necessary.

The modeling idea in this paper can be applied in various industries such as, e.g., computer and computer components manufacturing, apparel, food, and retail industries. In this paper we evaluate the proposed decision model in the context of decision support for the apparel industry. In an illustrative case study, which is derived from a similar case from the research literature, we examine in which way certain production steps – especially dyeing and knitting – can be relocated from the production sites to certain stages within the supply chain, and how the dyeing and knitting process may be arranged. Therefore, a distribution network which consists of production sites, central warehouses, regional warehouses and sales regions is examined. Furthermore, we suppose long lead times between the production and the distribution sites which is typically the case in the apparel industry (e.g., production in India and China, consumption in Europe).

Numerical results demonstrate that our model makes a valuable contribution to decision support in postponement and that different levels of uncertainty may lead to different network and process structures. The model has the advantage that decision-makers need not rely any longer on general qualitative statements regarding the effects of global evaluations of different types of postponement strategies. Therefore, the model renders decision-making for speci<sup>fi</sup>c problems possible despite the contradictory effects of implementing postponement strategies.

The remainder of the paper is organized as follows. In Section 2, a brief literature review on postponement and the design of distribution networks is given. In Section 3, postponement strategies and tradeoffs in general global distribution networks are discussed. Section 4 contains a mathematical formulation of the planning problem. Section 5 comprises a detailed description of a case study from the apparel industry including model parameters and an analysis of the numerical results. A summary and an outlook to further research are given in Section 6.

## 2. Literature review

Several researchers state that postponement is an approach that may result in superior supply chains (see, e.g., Cooper [13] or Jones and Riley [23]). Although it has been recognized as a growing trend in manufacturing and distribution (see Skipworth and Harrison [39]) and much has been written in the literature on the bene<sup>fi</sup>ts of postponement, little is known about its implementation (see Yang and Burns [48]).

Different types of postponement strategies and the discussion of the bene<sup>fi</sup>ts when establishing postponement strategies have been considered in the context of marketing and logistics as well as supply chain management. Alderson [2] and Bucklin [9] present two early papers in this context. Alderson appears to be the <sup>fi</sup>rst who coined this term, and an early extension of the concept is presented by Bucklin. Alderson regards postponement from the marketing point of view as promising for reactions towards demand uncertainties in order to reduce costs. Bucklin broadens this concept to the distribution channel and raises the question of where, when and how inventories can be stocked to trigger cost reductions.

In the seminal work of Zinn and Bowersox [50] a fundamental classi<sup>fi</sup>cation scheme for postponement strategies is developed. They introduce labeling, packaging, assembly and manufacturing postponement which are based on the type of the postponed manufacturing activities and can be characterized as form postponement. Time postponement occurs during transportation and means that the forward movement of inventories is delayed. Labeling postponement means that products which are technically identical but are, nonetheless, launched under different brand names leave the production site without labels. Hence, labeling takes place at a later stage in the supply chain, e.g., if respective customer orders have been received specifying which products are demanded in which quantity. During packaging postponement the goods are at <sup>fi</sup>rst bulk shipped to the warehouses and then packed customer-speci<sup>fi</sup>cally. Assembly postponement means that a generic product is sold in different variants. The different variants are only differentiated in a single detail, e.g., the color of component. The generic product is not differentiated ex works, but only later within the supply chain when the diversi<sup>fi</sup>ed part is installed. Manufacturing postponement can be distinguished from assembly postponement in its extent, as more than one installation is relocated from the production site to the warehouses. While assembly postponement contains only the execution of one production step on the goods, the extent of production steps is larger for manufacturing postponement. Additionally, different components of the products can be received from different sites and combined at the warehouses. Time postponement does not mean that goods are transported to the warehouses based on a forecast, but that products are shipped to customers only following order receipt which results in central inventories.

Besides the frameworks and classi<sup>fi</sup>cation mentioned above, many additional postponement strategies and conceptual investigations of bene<sup>fi</sup>ts of postponement are presented by Cooper [13], Dapiran [14], Feitzinger and Lee [17], Pagh and Cooper [32], van Hoek [43], [44] and Yang and Burns [48] as well as Mikkola and Skjøtt-Larsen [29]. Contrary to these primarily qualitative papers, some papers focus on quantifying the bene<sup>fi</sup>ts and criteria of various postponement strategies. In this context see, e.g., Appelqvist and Gubi [5], Ernst and Kamrad [15], Garg and Tang [18], Lee et al. [27], Ma et al. [28], Skipworth and Harrison [39], Swaminathan and Tayur [40], Wong et al. [47] or Yeh and Yang [49].

Since its earliest days, operations research deals with models and methods for distribution planning, in particular for warehouse location, but also for more comprehensive design problems regarding multiple products, limited capacities, single resource constraints or nonlinear transportation costs (see, e.g., the reviews of Aikens [1], Klose and Drexl [26] or Owen and Daskin [31]). Geoffrion and Graves [19] were among the <sup>fi</sup>rst to investigate the bene<sup>fi</sup>t of intermediate distribution. They present a model to solve the problem of designing a distribution system with optimally allocating intermediate distribution facilities between factories and customers. A MIP formulation with the objective of maximizing the total after-tax pro<sup>fi</sup>t for manufacturing facilities and distribution centers is presented by Cohen and Lee [11]. The model determines the optimal deployment of resources subject to a particular policy option. The product structure consists of three levels (major components, subassemblies, <sup>fi</sup>nished products). Extending the model of Cohen and Lee [11], Cohen and Moon [12] analyze effects of various parameters on supply chain costs and determine which manufacturing facilities and distribution centers should be established. Pooley [34] presents a MIP model that allows for deciding where to locate factories and depots, allocating the production and how to serve customers. A MIP global supply chain model developed by Arntzen et al. [6] determines the number and location of distribution centers, customer-distribution center assignments, the number of tiers, and the product-factory assignment. Camm et al. [10] developed an integer model for <sup>fi</sup>nding the location of distribution centers and to assign those selected to customer zones. Amiri [4] presents a model considering different capacity levels. A tri-echelon multi-commodity system incorporating production, transportation and distribution planning is considered by Pirkul and Jayaraman [33]. In a succeeding work, Jayaraman and Pirkul [22] present a model determining the location of potential production plants and distribution centers. Further models of distribution networks with several layers are also presented in, e.g., Ambrosino and Scutellà [3], Klincewicz [25], Tsiakis et al. [41] or Wilhelm et al. [46]. A distribution network model taking into account mode selection, lead times and capacitated vehicle distribution centers is proposed in Eskigun et al. [16]. Kalcsics et al. [24] developed a generic strategic planning and design model for global supply chains capturing essential elements of many industrial environments. Additional references on distribution networks can be found in comprehensive reviews of, e.g., Bilgen and Ozkarahan [7], Goetschalckx et al. [20] or Vidal and Goetschalckx [45].

None of the papers discussed above explicitly deals with the implementation of postponement strategies in the context of planning a distribution network, and only few papers, e.g., Arntzen et al. [6], Cohen and Lee [11] and Cohen and Moon [12] rudimentarily combine aspects of postponement and distribution network design. Two papers that comprehensively take into account the aspects of postponement and distribution network design are Schwartz and Voß [37], [36]. In these two papers deterministic demands are examined. Guericke et al. [21] present an upgrade of this model that additionally covers stochastic demands. However, while Alderson [2] initially devised the idea of postponement as a reaction to demand uncertainties, respective models considering stochastic demands still need to be developed and tested. The subsequent sections present such a model.

## 3. A production and distribution network with postponement and stochastic demands

The general structure of the production and distribution network considered in this paper is based on the structure presented in Schwartz and Voß [37]. It is depicted in Fig. 1. Additionally, analogous to Guericke et al. [21], demands in customer zones are assumed to be stochastic. The distribution network displayed in Fig. 1 consists of four tiers which comprise factories, central warehouses, regional warehouses and customer zones. The arrows represent potential <sup>fl</sup>ows of the products from factories up to the customer zones. Typically, the goods <sup>fl</sup>ow from factories to central warehouses, from central warehouses to regional warehouses and then to the customer zones. The locations of all facilities are known, but the production activities that should be set up at the facilities have to be determined. Furthermore, goods can also be shipped directly from factories to regional warehouses, from central warehouses to customer zones, and from factories up to customer zones (respective arcs are omitted in Fig. 1 for the sake of clarity). In this paper we assume long lead times of potentially several weeks or even months (e.g. due to overseas transportation) on all transportation arcs from factories associated with tier one to facilities of subsequent tiers.

The network considers different <sup>fi</sup>nished or un<sup>fi</sup>nished products that are shipped to central warehouses in order to be shipped from there together. Regional warehouses serve as destinations of shipments from factories or central warehouses, and as starting points for short distance deliveries to customer zones. Multiple units of different products can be bundled while shipping over long distances. However, they are then split into smaller quantities in order to meet customer orders. The customer zones comprise several customers within an enclosed area. Each customer zone has a stochastic demand for a certain product, which has to be met by the distribution system.

![](/api/attachments/9XZHCGET/fulltext/images/da66d435ebb0e0765bd1fe326d7698b795173ae1526fc946231b745cbd2bfb61.jpg)  
Fig. 1. Distribution network with four tiers [37].

Common models of distribution network planning assume that they comprise a <sup>fl</sup>ow of <sup>fi</sup>nished products from factories to customers. In this paper this assumption is relaxed to allow the <sup>fi</sup>nishing activities to be performed later. This may be initiated by simply postponing activities along the route from a factory up to the customers, or by resequencing activities with the result that some activities are delayed and other activities are potentially brought forward, respectively. Potential locations for postponed activities are both central and regional warehouses. The paper assumes that a single apparel manufacturer controls the entire manufacturing process from the factories to the customer zones. Therefore, the manufacturer is able to postpone or resequence the activities of the manufacturing process.

Schwartz and Voß [37] as well as Guericke et al. [21] focus on savings in the physical transportation of goods that can be achieved by appropriate postponement strategies both under certain and uncertain demands. In addition to these existing approaches, in this work, we explicitly take into account market mismatch costs and costs related to inferior quality of demand information due to long lead times. Furthermore, we model and analyze two types of postponement strategies, namely strategies, in which a resequencing of process activities is allowed, and those, in which it is forbidden.

Postponement with its delay of activities of the production process may result in considerable cost tradeoffs. Typically, variable process costs and <sup>fi</sup>xed process costs for implementing activities in selected locations increase if they are transferred from a factory to a subsequent tier. Increased per unit variable costs result from reduced economies of scale in the concerned warehouses in contrast to performing the activities in a central plant, and from the increased wage level in sites closer to customer zones. On the other hand, transportation costs typically decrease if production activities are transferred to a subsequent tier. This is due to the fact that the transport of <sup>fi</sup>nished or semi-<sup>fi</sup>nished products over short distances is less costly than the transport over longer distances. Furthermore, transportation costs for un<sup>fi</sup>nished products are often lower than for <sup>fi</sup>nished products. Un<sup>fi</sup>nished products typically have a better density ratio than, e.g., wrapped <sup>fi</sup>nished products due to bulk shipping of the un<sup>fi</sup>nished products, and often the wrapping of un<sup>fi</sup>nished products is cheaper than for <sup>fi</sup>nished products.

The consideration of stochastic demands may be more costintensive because capacities have to be installed that are only used if accidentally higher demands occur.

The decisions to be determined by the problem represent strategic decisions on where, i.e., in which factories, central warehouses and/or regional warehouses, and in which sequence production activities should be established in the production and distribution network. Furthermore, decisions regarding quantities of products shipped between facilities have to be made. The quantities that are shipped to the customer zones do not need to meet their demands because the model also permits decisions about the acceptance of lost sales. In this paper, we assume that quantity decisions on tier one, both regarding production and transportation, have to be made at the beginning of the planning horizon and cannot be altered, revised or corrected later on due to very long lead times. The objective is expected pro<sup>fi</sup>t maximization. The pro<sup>fi</sup>t is the weighted difference between the sales revenue and the combined total costs of the network for a set of scenarios of stochastic demand of several customers, taking into account both <sup>fi</sup>xed infrastructure costs and variable operating costs.

## 4. Model formulation

In this section we model the strategic planning task presented in the previous section as a two-stage stochastic programming model.

Stochastic programming is a well-established <sup>fi</sup>eld of mathematical programming where uncertainty of input parameters is represented by random variables (see, e.g., Birge and Louveaux [8]). Due to computational reasons virtually only random variables with discrete distributions are deployed in practical stochastic optimization models. In this context a speci<sup>fi</sup>c combination of discrete values of all the random variables in a model is called a scenario.

A stochastic optimization problem is then characterized by the situation that a subset of the decisions has to be taken without full information on some random events, represented by a set of scenarios Ω. These decisions are called first-stage decisions and have to be feasible for all scenarios $\omega \in \Omega .$ A <sup>fi</sup>rst-stage decision is taken only with the knowledge of the distribution (ω, p(ω)) of the random parameters. Later, full information is received on the realization of the random parameters, i.e., the outcome ω is observed, and the second-stage decisions are taken. The corrective actions of the second-stage decisions both compensate for and adapt to different scenarios ω.

In our stochastic model different scenarios are constituted by a variation of product demands. First-stage decisions are taken about the implementation of production activities in different locations and also about the determination of quantities that are produced on and are distributed from the <sup>fi</sup>rst tier of the distribution network, $\mathrm { i . e . , }$ the factories. Associating quantity decisions (and not only strategic investment decisions) with <sup>fi</sup>rst-stage variables of the stochastic model allows for taking long lead times between tier one and subsequent tiers in the distribution network into account without resorting to a computationally much more complex multi-period model. On the second stage decisions are made about the quantities that are produced on subsequent tiers under known demands, and that have to be shipped from one location to another one. For an illustration of the decisions in our two-stage stochastic model see also Fig. 2.

Before we present the model formulation in detail, we explain some relevant terms to ease comprehension. According to Fig. 1, Tier 1, Tier 2, Tier 3 and Tier 4 contain factories, central warehouses, regional warehouses and customer zones, respectively. Furthermore, the terms tier and stage must not be confused: tiers refer to the design of a supply chain, stages refer to different types of decisions, i.e., <sup>fi</sup>rststage and second-stage decisions. Products can be the <sup>fi</sup>nal products, e.g., colored garments, but also semi-<sup>fi</sup>nished products such as bleached yarn, colored yarn, or bleached garments. Production activities in our model represent transformation processes executed in the facilities, such as dyeing, knitting or simple handling activities. The index k is used to distinguish different types of transportation links: $k = 1$ denotes transportation links between consecutive tiers, $k = 2$ denotes transportation links that skip one tier, and k= 3 denotes transportation links that skip two tiers.

The notation used in the mathematical formulation is as follows: Index sets:

## S Number of tiers

$L O C _ { s }$ Index set of potential locations of facilities on tier $s \in \{ 1 . . S - 1 \}$ and customer zones on tier S

$S L _ { s } ^ { k }$ Index set of allowed transportation links at tiers $s { \in } \{ 1 . . S - 1 \}$ and $s + k , k = 1 , 2 , 3$

$P$ Index set of products

L Index set of different production activities

$T F _ { l p } \subseteq P$ Index set of product variants generated by applying activity $l \in L$ to product $p { \in } P$

$T L _ { p } \subseteq L$ Index set of activities which can be applied to productp∈P Ω Index set of scenarios

## Decision variables:

$y _ { s i l }$ 1, if activity $l \in L$ is established on $\mathrm { t i e r } s \in \{ 1 . . s - 1 \}$ in a facility at location $i \in L O C _ { s } { : } 0$ otherwise; <sup>fi</sup>rst-stage decision

$$
z _ {p s k i j \omega}
$$

$$
s \in \{1.. S - 1 \}
$$

$$
p \in P
$$

$$
i \in L O C _ {s}
$$

$$
k = 1, 2, 3
$$

$$
s + k,
$$

$$
j \in L O C _ {s + k}
$$

$$
\omega \in \Omega ;
$$

$$
\text { if } s = 1
$$

x<sub>pp ' silω</sub> Quantity of product $p { \in } P$ transformed into product $p ^ { \prime } { \in } P$ in scenario $\omega { \in } \Omega$ in a facility at location i at tier $s { \in } \{ 1 . . S \}$ by the implemented activity $l \in L ;$ <sup>fi</sup>rst-stage decision i $\mathrm { f } s = 1$ second-stage decision otherwise

v<sub>psiω</sub> Slack quantity in scenario ω∈Ω of product $p { \in } P$ which was delivered to a facility on tier $s { \in } \{ 1 . . S \}$ at location $i \in L O C _ { s }$ but not further processed; <sup>fi</sup>rst-stage decision ${ \mathrm { i f ~ } } s = 1 ,$ , secondstage decision otherwise

$u _ { p s i \omega }$ Slack quantity in scenario ω∈Ω of product $p { \in } P$ which was processed in a facility on tier $s { \in } \{ 1 . . S \}$ at location i∈LOC but not further delivered; <sup>fi</sup>rst-stage decision if $s = 1$ second-stage decision otherwise

## Parameters:

$e _ { p i }$ Sales price per unit of product $p { \in } P$ in customer region $i { \in } L O C _ { S }$ (on tier S)

$c _ { p s } ^ { S }$ Shipping cost per unit and per unit distance for product $p { \in } P$ on tier s∈{1..S}

$d _ { s k i j }$ Distances between facility i∈LOC on tier s∈{1..S} and facility $j { \in } L O C _ { s + k }$ on tier $s + k , k = 1 , 2 , 3$

$c _ { p s i l }$ Processing cost for product $p { \in } P$ of activity l ∈ L in a facility at location $i \in L O C _ { s }$ at tier $s { \in } \{ 1 . . S \}$

$c _ { s i l } ^ { F }$ Fixed cost of establishing activity l ∈L in a facility at location $i \in L O C _ { s }$ at tier $s { \in } \{ 1 . . S \}$

$U _ { p s i l }$ Maximum throughput quantity (handling and inventory) for product $p { \in } P$ at a facility in location $\pmb { i } \in L O C _ { s }$ at $\mathrm { t i e r } s { \in } \{ 1 . . S \}$ for the implemented activity l∈L

$U _ { p s k i j } ^ { S }$ Maximum shipping quantities for product p∈P from a facility in location $i { \in } L O C _ { s }$ on tier $s { \in } \{ 1 . . S - 1 \}$ to a facility in location $j { \in } L O C _ { s + k }$ on tier $s + k , k = 1 , 2 , 3$

$D e m _ { p i \omega }$ Demand of product $p { \in } P$ in customer zone $i { \in } L O C _ { S }$ in scenario ω Ω

$S u p _ { p i }$ Supply of product $p { \in } P$ in factory $i { \in } L O C _ { 1 }$

$\pi _ { \omega }$ Probability of scenario $\omega \in \Omega ,$ subject to $\begin{array} { r } { \sum _ { \omega \in \Omega } \pi _ { \omega } = 1 , 0 { } \leq \pi _ { \omega } \leq 1 \forall \omega \in \Omega } \end{array}$

![](/api/attachments/9XZHCGET/fulltext/images/8410f67c7ac898f8483b2cbc216554ff16ae557300a5354e17c2a2436347daa6.jpg)  
Fig. 2. Decisions in a two-stage stochastic model.

In terms of the above notation, the problem can be stated as follows: Problem P:

$$
\max \theta = \sum_ {\omega \in \Omega} \pi_ {\omega} \left(\sum_ {k = 1} ^ {S - 1} \sum_ {\begin{array}{c}p \in P\\(i, j) \in S L _ {S - k} ^ {k}\end{array}} e _ {p j} z _ {p (S - k) k i j \omega} - \sum_ {k = 1} ^ {S - 1} \sum_ {\begin{array}{c}p \in P\\s \in \{1, 2, \dots , S - k \}\\(i, j) \in S L _ {s} ^ {k}\end{array}} c _ {p s} ^ {S} d _ {s k i j} z _ {p s k i j \omega}\right) - \sum_ {\begin{array}{c}p \in P\\s \in \{1, 2, \dots , S - 1 \}\\i \in L O C _ {s}\\l \in T L _ {p}\\p ^ {\prime} \in T F _ {l p}\end{array}} c _ {z s i l} x _ {p p ^ {\prime} s i l \omega}\left. \right) - \sum_ {\begin{array}{c}s \in \{1, 2, \dots , S - 1 \}\\i \in L O C _ {s}\\l \in L\end{array}} c _ {s i l} ^ {F} y _ {s i l} (1)
$$

subject to:

Material balance constraints Flows entering a facility

$$
v _ {p s j \omega} + \sum_ {l \in T L _ {p}} \sum_ {p ^ {\prime} \in T F _ {l p}} x _ {p p ^ {\prime} s j l \omega} = \sum_ {k = 1} ^ {s - 1} \sum_ {(i, j) \in S L _ {s - k} ^ {k}} z _ {p (s - k) k i j \omega} \quad \forall p \in P, s = 2, 3, j \in L O C _ {s}, \omega \in \Omega\tag{2}
$$

Flows leaving a facility

$$
\sum_ {l \in L} \sum_ {\left\{p \in P, p ^ {\prime} \in T F _ {t p} \right\}} x _ {p p ^ {\prime} s i l \omega} = u _ {p ^ {\prime} s i \omega} + \sum_ {k = 1} ^ {S - s} \sum_ {(i, j) \in S L _ {s} ^ {k}} z _ {p ^ {\prime} s k i j \omega} \forall p ^ {\prime} \in P, s \in \{1, 2,..., S - 1 \}, i \in L O C _ {s}, \omega \in \Omega\tag{3}
$$

Demand

$$
D e m _ {p j \omega} \geq \sum_ {k = 1} ^ {S - 1} \sum_ {(i, j) \in S L _ {s - k} ^ {k}} z _ {p (s - k) k i j \omega} \forall p \in P, s = S, j \in L O C _ {s}, \omega \in \Omega\tag{4}
$$

Supply

$$
\operatorname{Sup} _ {p i} \geq \sum_ {l \in T L _ {p}} \sum_ {p ^ {\prime} \in T F _ {l p}} x _ {p p ^ {\prime} s i l \omega} \forall p \in P, s = 1, i \in L O C _ {s}, \omega \in \Omega\tag{5}
$$

Capacity constraints

Transport capacity

$$
z _ {p s k i j \omega} \leq U _ {p s k i j} ^ {S} \quad \forall p \in P, s \in \{1, 2,..., S - k \}, (i, j) \in S L _ {s} ^ {k}, k = 1, 2, 3, \omega \in \Omega\tag{6}
$$

Facility capacity

$$
\sum_ {p ^ {\prime} \in T F _ {l p}} x _ {p p ^ {\prime} s i l \omega} \leq U _ {p s i l} y _ {s i l} \quad \forall p \in P, s \in \{1, 2, \dots , S - 1 \}, i \in L O C _ {s}, l \in L, \omega \in \Omega\tag{7}
$$

Non-anticipativity

$$
x _ {p p ^ {\prime} 1 i l 1} = x _ {p p ^ {\prime} 1 i l \omega} \forall p \in P, i \in L O C _ {1}, l \in T L _ {p}, p ^ {\prime} \in T F _ {l p}, \omega \in \Omega \backslash \{1 \}\tag{8}
$$

$$
z _ {p 1 k i j 1} = z _ {p 1 k i j \omega} \forall p \in P, k = 1, 2, 3, (i, j) \in S L _ {1} ^ {k}, \omega \in \Omega \backslash \{1 \}\tag{9}
$$

$$
u _ {p 1 i 1} = u _ {p 1 i \omega} \forall p \in P, i \in L O C _ {1}, \omega \in \Omega \backslash \{1 \}\tag{10}
$$

Furthermore, there exist non-negativity constraints for all decision variables. The variables $y _ { s i l }$ are binary variables.

Objective function (1) consists of the sales revenue and three cost types which are all assumed to be linear. Besides the sales revenue, the objective function encompasses variable shipping costs between the facility locations, variable processing costs at the facility locations, and <sup>fi</sup>xed infrastructure costs for establishing the optimal production activities in the facilities.

Constraint set (2) represents material balances. The <sup>fl</sup>ow entering a facility must equal the quantity that is processed in this facility plus a slack quantity, i.e., not all of the incoming <sup>fl</sup>ow has to be further processed. Analogously, constraint set (3) declares material balances which ensure that the <sup>fl</sup>ow leaving a facility plus a slack quantity has to be as high as the quantity that is processed there, i.e., not all of the processed quantity has to be further transported. Constraint set (4) determines the demand that ought to be met. However, the model design also permits lost sales. Due to the fact that demand is uncertain, it represents the stochastic parameter in the developed model. Constraint set (5) observes the maximum supply or rather the outbound material <sup>fl</sup>ow from the factories. With constraint set (6), the maximum quantity of products that can be shipped from one location to another one is incorporated into the distribution network model. Constraint set (7) represents a similar approach regarding the maximum quantity that can be processed by an implemented activity within a facility. The binary variables in constraint set (7) indicate whether a speci<sup>fi</sup>c activity should be established in a facility. Constraint sets (8) to (10) assure that all production, transportation and slack variables associated with tier one coincide in all the different demand scenarios, i.e., these decisions are assigned to the <sup>fi</sup>rst stage of the stochastic model. In the stochastic programming literature such constraints are called non-anticipativity constraints. They express that different demand scenarios in the future cannot be anticipated at tier one. Therefore, <sup>fi</sup>rst-stage decisions have to coincide in all scenarios (in contrast to second-stage decisions which can be dif ferent in each scenario).

## 5. A case study from the apparel industry

In this section the above model will be veri<sup>fi</sup>ed and evaluated on the basis of a case study which is adopted from a company of the apparel industry (see Dapiran [14]) and amended to <sup>fi</sup>t our requirements.

## 5.1. Motivation and setting of the case study

In the production and distribution network, which is depicted in Fig. 3, the manufacturing of garments starts with the dyeing of the yarn, which is followed by the knitting of the garment. Dyeing can be executed on the intermediate products uncolored yarn and uncolored garment, knitting on the intermediate products uncolored yarn and colored yarn. Different products (one type of garment in two different colors) are delivered from the garment factory to satisfy the stochastic demands of several customer zones. Due to the fact that the knitting process is relatively slow, it is necessary to hold high levels of inventories of <sup>fi</sup>nished garments in order to meet the customer service expectations. This in turn results in the problem that some desired colors will be out of stock shortly while there remain excess inventories of garments with unpopular colors. Furthermore, we assume that the factories are situated overseas (e.g., in China or India) while warehouses and customer zones are located in Europe, which is a likely scenario in the apparel industry. Due to seasonality considerations and long transportation times, it is also necessary to take all the production and transportation decisions at the beginning of the planning horizon. It is typically impossible to revise or correct these decisions during the course of the year when the demands for the <sup>fi</sup>nal products can be provided with higher certainty.

![](/api/attachments/9XZHCGET/fulltext/images/086f9335b87f3a16f17d0ff9549411055981306ce6b3a589b4014da00429f12a.jpg)  
Fig. 3. Structure of the distribution network.

In a market that is characterized by very short product life cycles, this mismatch of inventory and customer demand cannot be handled by the traditional manufacturing approach. Compared to the traditional approach, Dapiran [14] reports on a solution of this problem which was to knit the garments from the bleached yarn and delay dyeing until information on the preferred colors became available, i.e., the activities of the manufacturing process were resequenced (for an analysis of alternative approaches for managing high levels of uncertainty in the apparel industry see also Vaagen and Wallace [42]). This approach coincides with Yang and Burns [48] who postulate that in an environment with extreme demand uncertainty manufacturers may derive signi<sup>fi</sup>cant economic bene<sup>fi</sup>t from locating production geographically closer to customers.

The presented delayed dyeing process illustrates the general principle of postponement. Due to the fact that the implementation of this postponement strategy requires a fundamental change in the production process, the resequencing of the production process represents a manufacturing postponement.

The right sub<sup>fi</sup>gure of Fig. 4 shows that the point where a standardized product is customized is postponed to tiers closer to the customer. Thus the intermediate products are standardized products, and they are customized not before better forecasts are available or customer orders come in. The transition point constitutes a point commonly known as customer decoupling point (DP). Products before the DP are standardized, products after the DP (within the supply chain) are customized (see van Hoek [44]).

Fig. 5 presents a general design of the two types of the manufacturing process. In the graph in Fig. 5 different paths represent possible manufacturing processes. According to the selected path in this graph a manufacturing process with the sequence dyeing and knitting may be speci<sup>fi</sup>ed, or by selecting another path a manufacturing process with the sequence knitting and dyeing. The activities dye and knit do not need to be implemented in the factory. Instead, these activities can be implemented at a subsequent tier, maybe a central warehouse or a regional warehouse, which constitutes a postponement strategy. Note, that the graph displayed in Fig. 5 can be directly represented in our model formulation by the index sets $T F _ { l p }$ and $T L _ { p } .$

## 5.2. Input data

In order to be able to investigate certain postponement strategies in the case study we have to make further assumptions about the underlying cost structure. Most of the following assumptions have been taken from the postponement literature.

In Figs. 6 and 7 some relations between different types of costs speci<sup>fi</sup>ed in monetary units [MU] are illustrated qualitatively. We list the important assumptions involving the cost structure below.

![](/api/attachments/9XZHCGET/fulltext/images/e0f2cb8dd99cd36a8073ed7e7e3283e49e974809b463a9320de40675984a67b2.jpg)  
Fig. 4. Structure of the traditional and the modi<sup>fi</sup>ed manufacturing process (see Shen [38]).

![](/api/attachments/9XZHCGET/fulltext/images/2c8c21607cc90e0b02423819462a364f2ee3eddf50d5b7e24bd00aaf55319713.jpg)  
Fig. 5. Possible manufacturing processes.

1. The costs for executing any task increase with augmented customer focus (see Lee et al. [27]), i.e., the variable costs for dyeing or knitting or simply handling are higher in a regional warehouse than in the factory. This also holds analogously for the <sup>fi</sup>xed costs for establishing the dyeing and knitting activities.

2. The variable costs for dyeing yarn and the costs for dyeing the garments made of bleached yarn are assumed to be identical. Analogously, the variable costs for knitting garments are identical for bleached yarn and dyed yarn.

3. It is supposed that executing several production steps at one site is more favorable than at different sites (see Yang and Burns [48]). This rests on the assumption that the variable costs for a combined dyeing and knitting process at one location are lower than the costs for separated dyeing and knitting in different locations. Furthermore, it is assumed that the variable costs for dyeing are higher than for simply handling the goods and that the variable costs of knitting are higher again than the variable costs for dyeing.

4. Due to shorter distances the transport costs from a regional warehouse to a customer zone are lower than the transport costs from the factory to a central warehouse, or even from the factory to a regional warehouse or a customer zone.

5. Transport costs for <sup>fi</sup>nal products that are dyed and knitted are assumed to be higher than the transport costs for undyed garments. Furthermore, the transport of yarn is priced lower than the transport of knitted garments, and the transport of undyed yarn is priced lower than the transport of dyed yarn.

6. Transport capacities are assumed to be in<sup>fi</sup>nite, i.e., the transport amounts are not limited.

7. Supply and throughput capacities are assumed to be in<sup>fi</sup>nite.

8. Shipping routes exist between all sites.

9. The demand follows a normal distribution.

The mean of demand is identical for each product in all scenarios. The variable costs for combined dyeing and knitting exceed the variable costs for separate dyeing or knitting.

![](/api/attachments/9XZHCGET/fulltext/images/10aa2f44662df6ad23ad5dc5ea29c142583cb63dc30ada02901067e0ccbdf956.jpg)  
Fig. 6. Relations between different types of variable costs.

![](/api/attachments/9XZHCGET/fulltext/images/21fad1f922515ee1f1f34dbecbe4861502fa8bc1d51b95a637226e567de39997.jpg)  
Fig. 7. Relations between different types of <sup>fi</sup>xed costs.

Diverse scenarios are generated for initial test-runs. Each scenario can be characterized by different normally distributed demands with mean μ and standard deviation σ. The generation of demands takes place on the basis of a discretized normal distribution. A normal distribution can be modeled by describing random variables that are independent from each other and that are grouped around an average. Due to different levels of discretization the quality of the approximation of the normal distribution is variable as sketched in Fig. 8. The number of generated scenarios corresponds to the number of discretized steps (for theoretical background see, e.g., Ross [35]).

Furthermore, the experimental design has to be worked out. The following parameters are varied:

− Problem instance: Three types of problem instances are compared. One problem instance represents a situation that inhibits any procrastination of production steps. Both the dyeing and knitting are carried out in the factory. This approach represents a classical make-to-stock production, thus we call it MTS instance. The second problem instance allows a procrastination of production activities, i.e., maybe the knitting and/or dyeing activities do not need to be implemented in the factory. However, in this second problem instance a resequencing of the production process is not allowed which results in a process structure of <sup>fi</sup>rst dyeing the yarn and afterwards knitting it. We call this problem instance fixed process sequence instance. A resequencing of activities is only permitted in the third problem instance which also accompanies with a procrastination of production activities. This third approach represents the problem instance with the highest degree of freedom regarding the design of the production process, and consequently, we call this problem instance flexible instance.

− Mean of the demand: The mean demand μ ranges from 800,000 to 10,000,000.

− The standard deviation σ of the demand's normal distribution in relation to the mean μ of demand represents a measure of the uncertainty. In case of $\sigma / \mu { = } 0 ,$ , a deterministic problem is considered. In case of $\sigma / \mu > 0 ,$ a stochastic problem is on hand that requires the generation of several scenarios ω. The number of generated scenarios ω in the test instances is set to 11, as it delivers a suf<sup>fi</sup>cient level of approximation.

## 5.3. Numerical result

In this section the solutions to the problem instances associated with the above postponement strategies are presented and analyzed. The model was implemented in the modeling language Mathematical Programming Language (MPL); data is saved in a Microsoft Access data base. Scenarios are created by a VBA script which saves them directly in the data base. Solutions are generated by the solver MOPS 10.7 (see MOPS [30]) on a Windows PC (i5 Core, 2.66 GHz, 1 GB RAM, Windows 7 Professional).

For comparative purposes, a deterministic problem instance without procrastination and resequencing the dyeing and knitting activities is solved. The solution of this problem instance is $\theta ^ { * } { = } 9 , 5 5 9 , 9 9 6 . 1 7 .$ . The model comprises 250 decision variables and 180 constraints. Only a small number of 72 decision variables are binary variables and, therefore, integer variables. The import time of the model amounts to 0.18 s, the solution time by MOPS to 0.07 s.

The numerical results of the problem instances speci<sup>fi</sup>ed in the experimental design are reported in Table 1. The table contains a presentation of the pro<sup>fi</sup>t Θ and an illustration of the allocation of the activities dyeing and knitting. For instance, the character string $D _ { - } x \lrcorner K ^ { * }$ means that on the <sup>fi</sup>rst tier the dyeing activity, on the second tier no action, and on the third tier the knitting activity are implemented. The asterisk indicates that the optimal solution suggests the implementation of a postponement strategy. Note that the table does not distinguish between implementing the activity “no action” and avoiding the tier completely since only the postponement of activities is of interest. In contrast, the character string DK\_x\_x means that both the dyeing and knitting activities take place in the factory with the result that no activities are postponed. For presentational reasons, only changed structures are recorded. In case no character string is provided and $\Theta ^ { * } > 0 ,$ the previous uncertainty's structure in the table's row with less uncertainty is implemented again. In case $\Theta ^ { * } = 0 ,$ , no structure is created. Furthermore, the objective values of the instances are rounded to integers.

Fig. 9 illustrates the objective values of Table 1. All sub<sup>fi</sup>gures have in common decreasing objective function values with increasing volatility, represented by σ/μ. One can further observe that the MTS instance's objective values are much lower compared to the other instances. This can be explained by the high transportation costs for <sup>fi</sup>nished goods. Due to a relatively small margin and large <sup>fi</sup>xed costs,

![](/api/attachments/9XZHCGET/fulltext/images/1dda0e19aed3fc6bb29fa48814537be0ead66c864a666e7e545b3c28e5a422b7.jpg)

![](/api/attachments/9XZHCGET/fulltext/images/26d9822d1acf84003ed640e751fc53a4fbfef8bd1daaed81ae3acd701cfe8338.jpg)  
Fig. 8. Discretized normal distribution with 11 and 101 scenarios.

Table 1  
Pro<sup>fi</sup>t Θ and allocation of dyeing (D) and knitting (K) activities.

<table><tr><td rowspan="2">Type of instance</td><td rowspan="2"> $\mu [10^6]$ </td><td colspan="3"></td><td colspan="4"> $\sigma/\mu [\%]$ </td></tr><tr><td>0.0</td><td>2.5</td><td>5.0</td><td>10.0</td><td>20.0</td><td>30.0</td><td>36.5</td></tr><tr><td rowspan="5">MTS</td><td>0.8</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1.0</td><td>279998 DK_x_x</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2.0</td><td>9559996 DK_x_x</td><td>8294539</td><td>7029090</td><td>4498175</td><td>0</td><td>0</td><td>0</td></tr><tr><td>4.0</td><td>281199923 DK_x_x</td><td>25589086</td><td>23058171</td><td>18195713</td><td>9771433</td><td>1375706</td><td>0</td></tr><tr><td>10.0</td><td>83799981 DK_x_x</td><td>77472711</td><td>71769633</td><td>61239281</td><td>40950754</td><td>21526142</td><td>8900140</td></tr><tr><td rowspan="5">Fixed process sequence</td><td>0.8</td><td>7083198 D_x_K*</td><td>6652119</td><td>6221037</td><td>5358876</td><td>4315210 x_DK_x*</td><td>3756822</td><td>3393861</td></tr><tr><td>1.0</td><td>13103998 D_x_K*</td><td>12565145</td><td>12026306</td><td>10948606</td><td>8793215 x_D_K*</td><td>8003671</td><td>7515661</td></tr><tr><td>2.0</td><td>43207995 D_x_K*</td><td>42130303</td><td>41052604</td><td>38897213</td><td>36008874 x_D_K*</td><td>34507336</td><td>33534541</td></tr><tr><td>4.0</td><td>103415991 D_x_K*</td><td>101260599</td><td>99105208</td><td>94794429 x_D_K*</td><td>90517748</td><td>87514617</td><td>85562645</td></tr><tr><td>10.0</td><td>284039976 D_x_K*</td><td>278651521</td><td>273263009</td><td>267443713 x_D_K*</td><td>257347427</td><td>247251203</td><td>241656624</td></tr><tr><td rowspan="5">Flexible</td><td>0.8</td><td>7083181 D_x_K*</td><td>6652119</td><td>6221037</td><td>5358876</td><td>4315210 x_DK_x*</td><td>3756822</td><td>3393861</td></tr><tr><td>1.0</td><td>13103998 D_x_K*</td><td>12565145</td><td>12026306</td><td>109 48606</td><td>9370425 x_K_D*</td><td>8615645</td><td>8125029</td></tr><tr><td>2.0</td><td>43207995 D_x_K*</td><td>42130303</td><td>41052604</td><td>38897213</td><td>37240840 x_K_D*</td><td>35731284</td><td>34750059</td></tr><tr><td>4.0</td><td>103415991 D_x_K*</td><td>101260599</td><td>99105208</td><td>96000835 x_K_D*</td><td>92981680</td><td>89962512</td><td>88000118</td></tr><tr><td>10.0</td><td>284039976 D_x_K*</td><td>278674483</td><td>273263009</td><td>267752134 x_K_D*</td><td>260204267</td><td>252656464</td><td>247750306</td></tr></table>

some MTS objective function values are equal to zero. Respective demands result in minor revenues that would lead to an overall loss. Thus, an optimal solution is to produce nothing at all. Furthermore, the MTS instance also suggests avoiding the production in case of large uncertainties (and small quantities). In these instances some revenues are not suf<sup>fi</sup>cient to cover the costs, either due to high transportation costs or low quantities. One can observe that this myopic network structure fails and more holistic structures are needed. The second and the third sub<sup>fi</sup>gure report a much larger pro<sup>fi</sup>t for different mean values. Furthermore, the loss caused by the increasing uncertainty is much lower in these network structures. The instance with the largest pro<sup>fi</sup>t, $\mu { = } 1 0 , 0 0 0 , 0 0 0$ , might result in a more robust network structure, robust against small changes in demand uncertainty. The instances with low $\mu , { \ e . g . \ } \mu { = } 8 0 0 , 0 0 0$ , where the production quantity is close to the point of even gaining no pro<sup>fi</sup>ts at all, the solution might be more sensitive to changes in demand. However, since the pro<sup>fi</sup>t differs in a wide range for different μ, comparing objective function values with each other makes it dif<sup>fi</sup>cult to see the pro<sup>fi</sup>ts' relative changes with increasing uncertainty.

![](/api/attachments/9XZHCGET/fulltext/images/f823dc5a2ca29fd479685b2dcac7dab8be15029dd3d34ec896305552b8cc285e.jpg)

For an improved loss analysis, Fig. 10 presents the pro<sup>fi</sup>t performance values. As indicator, objective function values are represented in relation to the objective function values without uncertainty, i.e., the deterministic case. Thus, 100% means that the value equals the instances' deterministic objective value, and, e.g., 90% means that the value is 10% lower compared to the instances' deterministic objective value. As Fig. 10 indicates again, a decreasing performance occurs with increasing uncertainty. The decreases in extremely uncertain environments are between 10% $( \mathrm { a t } \ \mu { = } 1 0 , 0 0 0 , 0 0 0 , \sigma / \mu { = } 3 6 . 5 \% )$ up to 100% (at $\mu { = } 1 , 0 0 0 , 0 0 0 , \ \sigma / \mu { \geq } 2 0 \% )$ , depending on the speci<sup>fi</sup>c instance.

![](/api/attachments/9XZHCGET/fulltext/images/494f604ccea8a31b625db867132c2626a53dad1049ab363ccb58d4ee5a5a2af3.jpg)

![](/api/attachments/9XZHCGET/fulltext/images/31c9800858a674c13e8dab55a816082aa6f7e8201280dd5d3672821b7576f17a.jpg)  
Fig. 9. Pro<sup>fi</sup>t subject to uncertainty measure σ/μ.

![](/api/attachments/9XZHCGET/fulltext/images/7503bb4112094420fd63670719ed44c5178f3473c2b56a5150adf47feb32950a.jpg)

![](/api/attachments/9XZHCGET/fulltext/images/c081da1bc8d87890685c6bee2572719ff9aaf26e384113dfba6eaa0cf55ee914.jpg)

![](/api/attachments/9XZHCGET/fulltext/images/ecfb0620568f509425640ee912518c906f111e12496c49ba5a26c862bba66352.jpg)  
Fig. 10. Performance of pro<sup>fi</sup>t subject to uncertainty measure σ/μ.

Furthermore, as one can observe in the <sup>fi</sup>xed process sequence and <sup>fl</sup>exible instance in Fig. 10, large quantities lead to nearly linear performance decreases, whereas especially the mid to low quantities are assumed to be prone to demand uncertainty. This leads to related gaps to optimal solutions, i.e., the solution of the <sup>fl</sup>exible instance.

As can be concluded from Fig. 11, the MTS instance sub<sup>fi</sup>gure shows a gap of at least 70% to the best possible solutions. This gap increases dramatically to almost 100% for all mean values at an uncertainty of $\sigma / \mu = 3 6 . 5 \% .$ To summarize Table 1 again, a change in the process structure usually takes place at around an uncertainty σ/μ of 10% to 20%. When the network adjusts to deal with the increased uncertainty in an optimal solution, the gap becomes larger in both instances shown above, since such an adjustment is prohibited in these instances. However, due to the same network structure for the <sup>fl</sup>exible and the <sup>fi</sup>xed process sequence instance for an uncertainty of at most $\sigma / \mu = 5 \% ,$ , a gap of 0% is indicated. For $\mu { = } 8 0 0 { , } 0 0 0$ the structures and objective function values are even equal along all uncertainties which also results in a gap of 0%. A low but still signi<sup>fi</sup>cant gap can be observed in case of larger uncertainties. From $\sigma / \mu = 2 0 \%$ and μ≥1,000,000 the process sequence is <sup>fl</sup>ipped and the customer decoupling point represented by the dyeing activity is moved from the factories to the regional warehouses. Since this swap is not allowed for any instances of Fig. 11, the gap increases signi<sup>fi</sup>cantly. A gap of up to 7% in the <sup>fi</sup>xed process sequence instance indicates the relevance of a shifted decoupling point towards the domestic market. The cheap bleached yarn should preferably be brought to a central warehouse, knitted to bleached garment and then dispersed to the regional warehouses where the garments are <sup>fi</sup>nally dyed

![](/api/attachments/9XZHCGET/fulltext/images/073fc5fec5531264e806ff62086e5f5406b62a01246bed40cc686ed7b43b7554.jpg)

![](/api/attachments/9XZHCGET/fulltext/images/3c3f7754a01656bbce8434550dffd4c35665e6642c6c51527494fab27a6bbcee.jpg)  
Fig. 11. Gap to optimal solution subject to uncertainty measure σ/μ.

Production costs subject to uncertainty  
![](/api/attachments/9XZHCGET/fulltext/images/713d4382f5132d6c6b5e72c887be89c477ab7b8ddba22a2113de3b5696c7e7f4.jpg)

![](/api/attachments/9XZHCGET/fulltext/images/93ece36043f459d951579fefbd3ef6c8fe0d7ca74899baf3653b884144c55333.jpg)

![](/api/attachments/9XZHCGET/fulltext/images/7e782c6c9c7896a754bc3583827ae6d69464258ccc80daa32165ec0d9eb19263.jpg)

Transportation cost ssubject to uncertainty  
![](/api/attachments/9XZHCGET/fulltext/images/47ab5de720a3105796a1ef2ed40e88396d1ef9e061de0aae6d2c82b995e18214.jpg)

![](/api/attachments/9XZHCGET/fulltext/images/7f603226f984e2022aaa54126d9d0f382fd867ac5ce6fd6625ddc8fbed3e9b65.jpg)  
Fig. 12. Pro<sup>fi</sup>t, revenue and costs subject to uncertainty measure σ/μ.

according to the customer zones' demands. Especially in environments of extreme demand uncertainty this network structure becomes advantageous.

![](/api/attachments/9XZHCGET/fulltext/images/4f8fbfa4327c5f602c43031e59b7e395e15d5b963814df883e9a9628ddb4041e.jpg)  
Fig. 13. Uncertainty measure σ/μ subject to the mean of demand.

Fig. 12 shows the components of the objective function values for the MTS, the <sup>fi</sup>xed process sequence and the <sup>fl</sup>exible instance. The <sup>fi</sup>rst sub<sup>fi</sup>gure of Fig. 12 reports the pro<sup>fi</sup>t for the different instances. As stated above, the <sup>fl</sup>exible and <sup>fi</sup>xed process sequence instances result in an equal pro<sup>fi</sup>t for relatively low demand uncertainty, whereas the MTS instance's pro<sup>fi</sup>t is signi<sup>fi</sup>cantly lower. At an uncertainty level of σ/μ=20%, the upper curves slightly differ from each other and the lower MTS instance results in an objective value of 0. The change in the objective function values can be explained using the successive sub<sup>fi</sup>gures. The revenue gained by the upper two series is equal and until σ/μb20% slightly decreasing whereas the revenue of the MTS instance decreases rapidly. The model has to cope with increasing inventories on the one hand and lost sales on the other hand. Due to larger inventory costs (that are modeled implicitly by produced products that could not be sold), the model decreases the quantity of raw materials (yarn). This leads to lower revenues and lower production costs. With σ/μ≥20% the revenue <sup>fi</sup>rst increases slightly due to the improved distribution network. While this leads to nearly the same production costs for the <sup>fl</sup>exible instance, the costs of the <sup>fi</sup>xed process sequence instance increase (at this uncertainty level, the MTS instance already decides for a zero quantity optimal solution). This can be explained by the larger costs for <sup>fi</sup>nalizing the garments close to the domestic market. The transportation cost sub<sup>fi</sup>gure shows the underlying high transportation costs for the <sup>fi</sup>nal products. Due to decreasing quantity with increasing σ/μ, decreasing transportation costs for the MTS instance can be observed. For σ/μ 20% increasing transportation costs for the bleached garment compared to the dyed yarn can be observed from the underlying cost structure. Furthermore, the last sub<sup>fi</sup>gure shows slightly increased <sup>fi</sup>xed costs from σ/μ≥20% for the (optimal) <sup>fl</sup>exible solution and the <sup>fi</sup>xed process sequence instance. Here, implementing a production activity closer to the domestic market is by assumption more expensive than in low-wage countries. Due to the cancellation of production in the MTS instance at uncertainty σ/μ≥20%, no <sup>fi</sup>xed costs occur.

![](/api/attachments/9XZHCGET/fulltext/images/cdba0966c1568c9e122b9dbe5c4d7b3b0e1b9f903959733d4be6ee7f11bd3b9c.jpg)  
Fig. 14. Solution time subject to instances and number of scenarios

The computational results above can be represented by means of a shifted customer decoupling point. Fig. 13 reports the postponed decoupling point subject to the mean of demand and the uncertainty measure σ/μ. The plotted uncertainty represents the level where activities are postponed from the factory to the central warehouse (μ=800,000) or to the regional warehouses (μ≥1,000,000). From this level, the decoupling point is not shifted back to the factory again and can be described as stable. We can conclude from Fig. 13, that with increasing quantity it is worth to shift the decoupling point to the regional warehouses, even when dealing with small uncertainties. Smaller quantities and thus lower revenues make the shifting worthwhile in high uncertainty environments. In this case, the increased <sup>fi</sup>xed costs for the central warehouse related postponement activities are worth the lost sales or the indirect inventory costs.

Finally, Fig. 14 states the different solution times for each of the model's instances. The solution times are clearly lower for the MTS and the <sup>fi</sup>xed process sequence instance across all scenario sets. However, all of the instances have to cope with the proportionally growing model size with increasing number of scenarios and a respective increase in the solution times. However, due to the limited number of integer variables in the model, the solution time is still acceptable. Since |Ω|=11 already leads to good approximations for the instances at hand, the use of more scenarios does not seem to be mandatory.

Our numerical results show that the postulation of Yang and Burns [48] on signi<sup>fi</sup>cant economic bene<sup>fi</sup>ts from locating production geographically closer to the customer in environments of extreme demand uncertainty can be veri<sup>fi</sup>ed. Furthermore, the resequencing strategy of the considered apparel manufacturer has been con<sup>fi</sup>rmed to lead to signi<sup>fi</sup>cant economic bene<sup>fi</sup>ts, too. Both strategies are optimal under high values of mean demand, even at moderate levels of uncertainties.

## 6. Conclusions

The paper deals with the problem of establishing postponement strategies in global distribution networks under uncertain demands. A stochastic two-stage mixed integer programming model is developed supporting decisions about where and in which sequence potentially postponed activities have to be implemented in a distribution network with factories, central warehouses and/or regional warehouses, and how much quantities should be shipped between respective facilities. Long lead times are modeled by an appropriate assignment of decision variables to the stages of the stochastic programming model. The model has been veri<sup>fi</sup>ed and evaluated by investigating an illustrative case study from the apparel industry.

The model enables decision-makers for the <sup>fi</sup>rst time to generate and evaluate postponement strategies in a global distribution network under uncertainty on a quantitative basis. The signi<sup>fi</sup>cant virtue of this approach is the possibility to perform calculation using data of real planning problems. Decision-makers are no longer dependent on trend statements about pro<sup>fi</sup>t and applicability of the corresponding concepts. This is highly important due to the large differences of solutions subject to the problem's cost structure.

The proposed stochastic model can be regarded as a basis for further research. Thus, several aspects should be taken into account in future work, e.g., nonlinearities of costs, alternative technologies for production activities in the facilities, an observation across several periods (dynamic model), capital commitment and insurance contributions or taxes. Other extension options concern deterioration, perishability and rework as well as different buyback policies motivated from practical situations not only in the apparel industry. Moreover, implications of incorporating our model for decision support into advanced planning systems need to be explored.

## References

[1] C.H. Aikens, Facility location models for distribution planning, European Journal of Operational Research 22 (1985) 263–279.

[2] W. Alderson, Market ef<sup>fi</sup>ciency and the principle of postponement, Cost and Pro<sup>fi</sup>t Outlook 3 (1950) 15–18 September.

[3] D. Ambrosino, M.G. Scutellà, Distribution network design: new problems and related models, European Journal of Operational Research 165 (2005) 610-624

[4] A. Amiri, Designing a distribution network in a supply chain system: formulation and ef<sup>fi</sup>cient solution procedure, European Journal of Operational Research 171 (2006) 567–576.

[5] P. Appelqvist, E. Gubi, Postponed variety creation: Case study in consumer electronics retail, International Journal of Retail & Distribution Management 33 (10) (2005) 734–748

[6] B.C. Arntzen, G.G. Brown, T.P. Harrison, L.L. Tafton, Global supply chain management at Digital Equipment Corporation, Interfaces 25 (1) (1995) 69–93.

[7] B. Bilgen, I. Ozkarahan, Distribution Planning Problem: A Survey, in: D. Ahr, R. Fahrion, M. Oswald, G. Reinelt (Eds.), Operations Research Proceedings 2003, Springer, Berlin, 2004, pp. 39–46.

[8] J.R. Birge, F. Louveaux, Introduction to Stochastic Programming, Springer, New York, 1997.

[9] L.P. Bucklin, Postponement, speculation and structure of distribution channels, Journal of Marketing Research 2 (1965) 26–32.

[10] J.D. Camm, T.E. Chorman, F.A. Dill, J.R. Evans, D.J. Sweeney, G.W. Wegryn, Blending OR/MS, judgment, and GIS: Restructuring P&G's supply chain, Interfaces 27 (1) (1997) 128–142.

[11] M. Cohen, H.L. Lee, Resource deployment analysis of global manufacturing and distribution networks, Journal of Manufacturing and Operations Management 2 (1989) 81–104.

[12] M.A. Cohen, S. Moon, Impact of production scale economies, manufacturing complexity, and transportation costs on supply chain facility networks, Journal of Manufacturing and Operations Management 3 (1990) 269–292

[13] J.C. Cooper, Logistics strategies for global business, International Journal of Physical Distribution and Logistics Management 23 (4) (1993) 12–23.

[14] P. Dapiran, Benetton – Global logistics in action, International Journal of Physical Distribution and Logistics Management 22 (6) (1992) 7-11

[15] R. Ernst, B. Kamrad, Evaluation of supply chain structures through modularization and postponement, European Journal of Operational Research 124 (2000) 495–510.

[16] E. Eskigun, R. Uzsoy, P.V. Preckel, G. Beaujon, S. Krishnan, J.D. Tew, Outbound supply chain network design with mode selection, lead times and capacitated vehicle distri bution centers European Journal of Operational Research 165 (2005) 182-206

[17] E. Feitzinger, H.L. Lee, Mass customization at Hewlett-Packard: The power of postponement, Harvard Business Review 75 (1) (1997) 116–121

[18] A. Garg, C.S. Tang, On postponement strategies for product families with multiple points of differentiation, IIE Transactions 29 (1997) 641–650.

[19] A.M. Geoffrion, G.W. Graves, Multicommodity distribution system design by Benders decomposition, Management Science 20 (5) (1974) 822–844.

[20] M. Goetschalckx, C.J. Vidal, K. Dogan, Modeling and design of global logistics systems: a review of integrated strategic and tactical models and design algorithms, European Journal of Operational Research 143 (2002) 1–18

[21] S. Guericke, A. Koberstein, F. Schwartz, S. Voß, A stochastic model for implementing postponement strategies in distribution networks, in Proceedings of the 44th Hawaii International Conference on System Sciences (HICSS), Kauai, HI, USA 2011.

[22] V. Jayaraman, H. Pirkul, Planning and coordination of production and distribution facilities for multiple commodities, European Journal of Operational Research 133 (2001) 394–408.

[23] T.C. Jones, D.W. Riley, Using inventory for competitive advantage through supply chain management, International Journal of Physical Distribution and Material Management 15 (1985) 16–26.

[24] J. Kalcsics, M.T. Melo, S. Nickel, Mathematical programming models for strategic supply chain planning and design, in: U. Leopold-Wildburger, F. Rendl, G. Wäscher (Eds.), Operations Research Proceedings 2002, Springer, Berlin, 2003, pp. 108–113.

[25] J.G. Klincewicz, A large-scale distribution and location model, AT&T Technical Journal 64 (7) (1985) 1705–1730.

[26] A. Klose, A. Drexl, Facility location models for distribution system design, European Journal of Operational Research 162 (2005) 4–29.

[27] H.L. Lee, C. Billington, B. Carter, Hewlett-Packard gains control of inventory and service through design for localization, Interfaces 23 (4) (1993) 1–11.

[28] S. Ma, W. Wang, L. Liu, Commonality and postponement in multistage assembly systems, European Journal of Operational Research 142 (2002) 523–538.

[29] J.H. Mikkola, T. Skjøtt-Larsen, Supply-chain integration: Implications for mass customization, modularization and postponement strategies, Production Planning & Control 15 (4) (2004) 352–361.

[30] MOPS Optimierungssysteme GmbH & Co. KG, www.mops-optimizer.com.

[31] S.H. Owen, M.S. Daskin, Strategic facility location: a review, European Journal of Operational Research 111 (1998) 423–447.

[32] J.D. Pagh, M.C. Cooper, Supply chain postponement and speculation strategies: How to choose the right strategy, Journal of Business Logistics 19 (2) (1998) 13–33

[33] H. Pirkul, V. Jayaraman, Production, transportation, and distribution planning in a multi-commodity tri-echelon system, Transportation Science 30 (4) (1996) 291–302.

[34] J. Pooley, Integrated production and distribution facility planning at Ault Foods, Interfaces 24 (4) (1994) 113–121.

[35] S.M. Ross, Introduction to probability and statistics for engineers and scientists, Elsevier, Amsterdam. 2009

[36] F. Schwartz, S. Voß, Designing distribution networks taking into account aspects of postponement, in: J.A. Ceroni (Ed.), The Development of Collaborative Production and Service Systems in Emergent Economies, Proceedings of the 19th International Conference on Production Research, Tu3.4-6, IFPR, Valparaiso, Chile, 2007, p. 6.

[37] F. Schwartz, S. Voß, Distribution network design with postponement, in: A. Oberweis, C. Weinhardt, H. Gimpel, A. Koschmider, V. Pankratius, B. Schnizler (Eds.), e-Organisation: Service-, Prozess-, Market-Engineering, Universitätsverlag Karlsruhe, Karlsruhe, 2007, pp. 373–390.

[38] T. Shen, A framework for developing postponement strategies, Postponement Project Working Paper, MIT Center for Transportation and Logistics, February 23 2005.

[39] H. Skipworth, A. Harrison, Implications of form postponement to manufacturing: a case study. International Journal of Production Research 42 (2004) 2063-2081.

[40] J.M. Swaminathan, S.R. Tayur, Managing design of assembly sequences for product lines that delay product differentiation, IIE Transactions 31 (1999) 1015–1026.

[41] P. Tsiakis, N. Shah, C.C. Pantelides, Design of multi-echelon supply chain networks under demand uncertainty, Industrial and Engineering Chemistry Research 40 (16) (2001) 3585–3604.

[42] H. Vaagen, S.W. Wallace, Product variety arising from hedging in the fashion supply chains, International Journal of Production Economics 114 (2008) 431–455.

[43] R.I. van Hoek, Recon<sup>fi</sup>guring the supply chain to implement postponed manufacturing, The International Journal of Logistics Management 9 (1) (1998) 95–110.

[44] R.I. van Hoek, The rediscovery of postponement: A literature review and directions for research, Journal of Operations Management 19 (2) (2001) 161–184.

[45] C.J. Vidal, M. Goetschalckx, Strategic production-distribution models: a critical review with emphasis on global supply chain models, European Journal of Operational Research 98 (1997) 1–18.

[46] W. Wilhelm, D. Liang, B. Rao, D. Warrier, X. Zhu, S. Bulusu, Design of international assembly systems and their supply chains under NAFTA, Transportation Research 41 (6) (2005) 467–493.

[47] H. Wong, J. Wikner, M. Naim, Analysis of form postponement based on optimal positioning of the differentiation point and stocking decisions, International Journa of Production Research 47 (2009) 1201–1224.

[48] B. Yang, N. Burns, Implications of postponement for the supply chain, International Journal of Production Research 41 (2003) 2075–2090.

[49] C. Yeh, H.-C. Yang, A cost model for determining dyeing postponement in garment supply chain, International Journal of Advanced Manufacturing Technology 22 (1–2) (2003) 134–140.

[50] W. Zinn, D.J. Bowersox, Planning physical distribution with the principle of postponement, Journal of Business Logistics 9 (2) (1988) 117–136.

![](/api/attachments/9XZHCGET/fulltext/images/b87b51d34e8f385b0acf28f7ffef6005dc33b14dc7372d1eaecc75b9f26e50a6.jpg)  
Stefan Guericke is a PhD candidate at the International Graduate School Dynamic Intelligent Systems at the University of Paderborn, Germany. He studied Business Information Systems at the University of Paderborn and the Beijing Institute of Technology. His research interests include optimization models for logistics planning as well as stochastic and robust optimization.

![](/api/attachments/9XZHCGET/fulltext/images/9ba1626abab502a4206b38f1267e239c06ffb65041d691d2c5799d7def546064.jpg)

Achim Koberstein is Junior Professor for Business Informatics and Optimization Systems at the University of Paderborn, Germany. He studied Computer Science at the University of Paderborn and the Georgia Institute of Technology, Atlanta, USA. In 2005 he received his doctorate from the University of Paderborn. His research interests include optimization models and systems for production and logistics planning, supply chain management and for the liberalized gas market as well as optimization algorithms and solver technology in linear and stochastic optimization.

![](/api/attachments/9XZHCGET/fulltext/images/a09b4df95794b2fff08564688ef64f1c87a6c923c4226847bd7506a279d48682.jpg)

Frank Schwartz is a lecturer at the Institute of Information Systems at the University of Hamburg, Germany. He studied Industrial Engineering at the University of Hamburg, the Technical University of Hamburg-Harburg and the University of Applied Sciences in Hamburg. In 2004 he received his Ph.D. from the University of Hamburg. His research interests are disruption management in production systems as well as quantitative approaches to supply chain management and logistics.

![](/api/attachments/9XZHCGET/fulltext/images/60fb64aa46556bb9a20e2b777d8d9e68123c214a98a6f5018ac4286637fcefa5.jpg)

Stefan Voß is professor and director of the Institute of Information Systems at the University of Hamburg, Germany. Previous positions include professor and head of the department of Business Administration, Information Systems and Information Management at the University of Technology Braunschweig (Germany) from 1995 up to 2002. He holds degrees in Mathematics (diploma) and Economics from the University of Hamburg and a Ph.D. and the habilitation from the University of Technology Darmstadt. His current research interests are in quantitative / information systems approaches to supply chain management and logistics including public mass transit and telecommunications. He is author and co-author of several books and numerous papers in various journals. Stefan Voß serves on the editorial board of some journals including being Editor of Netnomics, Editor of Public Transport, Associate Editor of INFORMS Journal on Computing and Area Editor of Journal of Heuristics. He is frequently organizing work shops and conferences. Furthermore, he is consulting with several companies.

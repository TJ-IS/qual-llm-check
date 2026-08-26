---
otero_id: 380
otero_key: "2CDMVNYX"
title: "A decision support system for integrating manufacturing and product design into the reconfiguration of the supply chain networks"
authors: "Yohanes Kristianto; Angappa Gunasekaran; Petri Helo; Maqsood Sandhu"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.11.014"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision support system for integrating manufacturing and product design into the recon<sup>fi</sup>guration of the supply chain networks

Yohanes Kristianto <sup>a,</sup>⁎, Angappa Gunasekaran <sup>b</sup>, Petri Helo <sup>a</sup>, Maqsood Sandhu <sup>c</sup>

<sup>a</sup> Department of Production, University of Vaasa, P.O. Box 700, FI-65101 Vaasa, Finland

<sup>b</sup> Department of Decision and Information Sciences, Charlton College of Business, University of Massachusetts – Dartmouth, 285 Old Westport Road, North Dartmouth, MA 02747-2300, USA <sup>c</sup> Faculty of Business and Economics, United Arab Emirates University, P.O. Box 17555, Al-Ain, United Arab Emirates

## a r t i c l e i n f o

Available online 23 November 2011

Keywords: Assembly Decision Support Systems Inventory allocation Product design Supply chain

## a b s t r a c t

A supply chain needs to meet its customers' requirements (CRs) in terms of delivery lead times, total costs and product quality. The objective of this article is to improve the level of integration in all aspects of supply chain recon<sup>fi</sup>guration, such as the inventory allocation and manufacturing process involved, by incorporating manufacturing and product design into logistic design. The effect of uncertain customer demand, production and supply lead times are studied. An optimum supply chain network is con<sup>fi</sup>gured by combining optimization at the strategic and tactical level. A system dynamic based computer simulation model is used to validate the operations of the supply chain. The performance of the system is measured in terms of backorders and inventory level. The results and analysis indicate that fewer stockholding points and a shorter review period of demand can improve performance in this respect. In addition, a proposal for improving the performance of supply chain in terms of lower safety stocks is presented. Finally, management decision-making is discussed, among other concluding remarks.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

This paper examines the optimal supply chain con<sup>fi</sup>guration for customized products. Our intent is to develop a Decision Support System (DSS) for integrating manufacturing and product design into the design of the logistic process, since the supply chain must be recon<sup>fi</sup>gured before determining the product design, manufacturing technologies and vendors. We use assembly to represent manufacturing, since it is inherently integrative and should be composed to meet the Functional Requirements (FRs) of the product. The result is that the supply chain can be recon<sup>fi</sup>gured with full knowledge of the way in which the product is supposed to work. Supply chain recon<sup>fi</sup>guration involves creating a suitable assembly sequence, identifying subassemblies, integrating inventory control, and designing supplier–buyer coordination so that the performance in terms of backorders and inventory levels is compatible with the assembly method [40].

The liaison between manufacturing and product design, and the logistic process design should make a tradeoff between a higher unit of manufacturing cost with a more responsive supply chain or a lower manufacturing cost with a less responsive supply chain. While the FRs on this point have already been determined, there are several manufacturing options available for manufacturing or assembling the product. The supply chain con<sup>fi</sup>guration chooses a manufacturing option in terms of make-to-stock (MTS), make-to-order (MTO) or assemble-to-order (ATO) for each stage of the supply chain, so as to achieve the product functionality at minimum manufacturing cost and with higher supply chain responsiveness.

The supply chain recon<sup>fi</sup>guration frameworks consider three areas which are relevant to choosing a manufacturing option for each stage of the supply chain: assembly planning, demand planning, and inventory allocation. A better quality of demand planning leads to optimum inventory allocation [15,17,19,28]. The optimum further assists the supply chain with decision methods for responding to demands and improving the supply chain delivery performance [7,8,11,33,36]. The optimum assembly planning provides knowledge to the supply chain so as to realize the product with minimum lead times without impairing its functioning.

The frameworks of supply chain recon<sup>fi</sup>guration change the expectations regarding the DSS associated with the liaison between manufacturing and product design and the logistic process design, with the following challenges.

(a) Assembly redundancy: Whitney [40] mentions that a welldesigned product is a predictable product. This implies that product FRs analysis helps a designer to manufacture a product with minimum manufacturing effort without impairing its functioning. Thus, the product designer must consider the Product Key Characteristics (P-KCs). P-KCs are the FRs of a product to satisfy the Customer Requirements (CRs). P-KCs need support from the lower level of FRs to deliver CRs, which are called the Assembly Key Characteristics (A-KCs). Optimizing the assembly sequence according to the P-KCs and A-KCs hierarchy avoids redundant coupled assembly [35]. The optimum assembly sequence reduces the content of information within the product such that it also minimizes the information content within the product so as to reduce iterative operations in manufacturing [23]. In other words, instead of reducing the interdependency of the parts, the supply chain has to explicate the functional relationship between parts to properly deliver functionality in a product and minimize product failures. Product failures are de<sup>fi</sup>ned as the non-conformity of a product to the desired FRs. A lower probability of product failure minimizes the requirement on safety stock and reduces backorders.

(b) The imprecision of demand information: safety stock costs and backorders can be minimized by providing credible demand information through the application of DSS. The quality of demand information affects the ordering process and controls the target inventory level of the buyer [3]. Some research articles [9,27,37] focus on DSS development to forecast customer demands. Yao et al. [42] suggest the application of a Vendor Managed Inventory (VMI) as a DSS to minimize the inventory costs by distributing inventory status and demand information evenly along the supply chain. While VMI does not share the inventory status, the way in which VMI responds to demand depends on variations in the manufacturing process. To deal with the imprecision of demand information and manufacturing process variation, it is necessary to understand the implications of manufacturing process variation and to characterize the way in which the variations are hedged effectively through VMI.

(c) Non optimum inventory allocation: The imprecision of demand information affects the planning of the logistic process in terms of <sup>fl</sup>exibility and adaptability under the limitations of the capacity to supply with respect to the system dynamics [5]. Most of VMI is used to generate production <sup>fl</sup>exibility so as to minimize the discrepancy between demand and order rate [38,39,42] without considering the production capacity and capability in terms of the variability of production lead times. In other words, instead of a decision on production and order, the DSS needs to optimize the composition of the stockholding points; it is possible to mix push and pull inventory systems to satisfy customer demand at various levels of production variability [41].

To this end, a DSS, called the two-level optimization of supply chain networks, is proposed, for the purpose of integrating the manufacturing and product design into the supply chain recon<sup>fi</sup>guration in order to improve demand planning, inventory allocation and assembly planning. To deal with integration effectively, the concept of the FRs analysis of a product is put forward. On the <sup>fi</sup>rst level, optimized assembly sequencing is developed to allocate the safety stocks and to choose the stockholding points. On the second level, optimized production and distribution control is developed to characterize the supply chain networks effectively. The merit of a two-level optimization of supply chain networks is detailed in terms of inventory levels throughout supply chains and backorders.

The rest of the paper proceeds as follows. Section 2 reviews the literature on inventory allocation in the supply chain. Section 3 highlights the scope and de<sup>fi</sup>nition of the problem. Section 4 focuses on the features of DSS modeling, mainly aiming at supply chain recon<sup>fi</sup>guration and safety stock allocation. Section 5 validates the supply chain model in the previous section and discusses the DSS implications for management decision-making. Section 6 concludes this article.

## 2. Background of the research

The integration of FR analysis into the recon<sup>fi</sup>guration of supply chain networks extends the supply chain decisions by adding ‘how to manufacture’ to ‘how much to deliver’ and ‘how much to produce’. The integration requires an interplay between quality management (QM) and supply chain management (SCM) to coordinate and integrate the manufacturing processes [32]; however, not much research has been reported on the topic. Balachandran and Radhakrishnan [2] model the effect of supply chain coordination in terms of warranty contract to minimize product failures. Whitney [40] suggests that supply chains have to meet the design intent (FRs) to obtain a well-designed assembly. Dong and Whitney [9] use an axiomatic design approach to meet FRs at a minimum degree of integrality and information content [35]. We are aware of prior research which attempts to analyze the FRs as a tactic for assembly planning in a supply chain.

The model which we develop falls within the literature on assembly planning in a supply chain, in particular for a strategic inventory allocation of supply chain recon<sup>fi</sup>guration. In this way, our work is related to that of Novak and Eppinger [30] and Graves and Willems [18,19]. The former authors [30] hypothesize that product complexity and vertical integration are complementary and suggest greater coordination between the product design engineer and the supply chain engineer. They use original empirical evidence from the auto industry and <sup>fi</sup>nd that simpler product architecture can be suggested for an autonomous supply chain. Graves and Willems [18,19] develop a model for positioning safety stock in a supply chain, subject to non-stationary demand. It is suggested that optimal safety stock allocation may entail changing the service times, and thus the locations of safety stocks, as demand evolves over time. The authors [18,19] assume the same demand process for a multi-echelon system consisting of some manufacturing sites. The sites operate with an independent base-stock policy.

Our work differs from that of Novak and Eppinger [30], however, in that we consider axiomatic design, for which product complexity is reduced by <sup>fi</sup>rst identifying the liaison between the parts of a product and then providing information about the interdependency of the parts [43]. Liaison identi<sup>fi</sup>cation helps a designer to convey a well-designed manufacturing method so as to put into action the logistic planning by minimizing the interdependency of parts and to meet FRs [9] by relating the axiomatic design to assembly sequencing [43]. Not being able to do this leads to capacity overload and yields only 80% of successful assemblies on the <sup>fi</sup>rst try [6,14,40]. In addition, part modularization helps a logistics manager to minimize the amount of uncertain information about supply and demand within supply chains [12,37] and thus to reduce the level of safety stock [22]. While liaison identi<sup>fi</sup>cation has an important role in supporting supply chain recon<sup>fi</sup>guration in terms of better assembly planning and production clustering, the implications for the supply chain inventory cost are ignored or at best poorly understood [25].

Our model differs from that of Graves and Willems [18,19] in that we provide an insight into the behavior of inventory allocation and bene<sup>fi</sup>t from information sharing to minimize uncertainty about supply and demand [4,19,29,31]; this being the case, we have structured the model to allow the greatest possible responsiveness of production– distribution and clarify where the inventory hedge should be set. Graves and Willems [18,19] allocate the safety stock by assuming that the processing times are deterministic and that no capacity constraints limit production at any stage. Furthermore, the previous contributions minimize the safety stock placement at optimum processing time by considering the service level of the vertically integrated supply chain. Conversely, we consider backorder costs rather than service level targets in order to re<sup>fl</sup>ect managers' commitment to providing a 100% service level. In addition, VMI is employed to an autonomous supply chain and the service level is adjustable so as to maximize the supply chain performance.

This literature review leads on to supply chain coordination in terms of manufacturing and logistics planning. The supply chain needs to simplify the manufacturing method and minimize the content of information among the processing facilities. From the manufacturing viewpoint, assembly sequencing should minimize interdependencies between parts. From the logistical viewpoint, VMI provides a promising solution. This article covers the integration of manufacturing and logistics planning to improve the supply chain performance in terms of backorders and inventory levels by studying the effect of a review period of demand and assembly sequencing after analyzing product FRs [13].

## 3. Problem scope and de<sup>fi</sup>nition

In this section, we present the assembly and distribution operations of a furniture product family for recon<sup>fi</sup>guring the supply chain and allocating the inventory at the lowest possible backorder and inventory levels. The processing facilities have limited capacity for manufacture. However, the processing facilities have storage facilities. Depending on customer orders, the production quantities at the processing facilities <sup>fl</sup>uctuate over time and are not necessarily pre-determined. In addition, a processing facility has the probability of failure during the production process. The suppliers have no additional information regarding the buyers' inventory level. Indeed, forecasting matrices about demand are distributed across the supply chain, which is used by the suppliers to decide on delivery and production rates.

In considering probability of failure, we formulate the problem as a queue model and propose a dynamic simulation method. The method uses a GI/G/1-based inventory control which considers supply and demand uncertainties. The production rate in the queue model is dynamic by allowing backorders. Distribution from suppliers to buyers is considered in our model by implementing VMI to maximize the economies of scale in transportation costs.

First, in order to illustrate the proposed DSS in supply chain recon-<sup>fi</sup>guration and inventory allocation, Fig. 1 presents below a description of the strategic and tactical level optimization model.

## 4. DSS for tactical and operations level optimization

Fig. 1 shows that the DSS is split into a two-stage optimization, a strategic and tactical level. The optimization covers:

## 4.1. Strategic level optimization

The supply chain recon<sup>fi</sup>guration considers delivery lead times $L _ { n }$ and service level $z _ { n }$ in the supply chain against demand uncertainty $\sigma _ { d ( n ) } .$ The sequence should reduce part interdependency. Since most of the literature on inventory allocation considers the <sup>fi</sup>rst two components [24,19,29], part interdependency is rarely discussed.

4.1.1. KC analysis and assembly sequencing for supply chain reconfiguration We use the generic product structure of an of<sup>fi</sup>ce chair as an example [10]. There are six part frames (Fig. 2) comprising back, upholstery and arm rest as standard parts, and a seat frame, stand and support as three distinctive modules. The FRs of the chair includes its capability for making 360° rotations (FR 1) and choosing the quality of frame (FR 2). Both of these FRs are supported by de<sup>fi</sup>ning P-KC. The seat frame and the seat deliver P-KC 1 by allowing the customer to choose the material of the seat frame. The support and stand of the of<sup>fi</sup>ce chair deliver P-KC 2 by allowing the customer to rotate the chair 360°. Each P-KC is supported by using A-KCs to meet the quality objective of the product.

In addition, A-KCs are presented in the form of a liaison diagram, as follows.

Fig. 3 shows mate joints between upholstery and seat, between back and under frame, and between arm rest and under frame. Mate joints (dotted lines) do not affect A-KCs deliverability, but contact joints (directed lines) do so directly. Joints between the support and under frame, between under frame and stand, between seat frame and under frame, and between seat and under frame are represented as A-KCs 1 to 4. A-KCs 1 and 2 support the deliverability of P-KC 1 and A-KCs 3 and 4 for P-KC 2. The assembly sequence planning in Fig. 3 guides the supply chain recon<sup>fi</sup>guration, where the arrows signify the direction of product assembly.

The assembly sequencing in Fig. 3 is used to recon<sup>fi</sup>gure the supply chain networks, which are represented by the design structured matrix (DSM). DSM is used for the clustering of dependencies in a matrix [43]. The goal of DSM is to cluster closely related activities as shown in Fig. 4b so as to minimize the coupling between activities. The DSM square matrix comprises rows for representing independent variables and columns representing dependent variables. The diagonal line is blank when it is expected that either dependent or independent variables are dependent upon themselves. For instance, in Fig. 4, activity number 3 is sequentially accomplished just after activity number 1 and is recognized as the second of two activities in a series. Finally, activities number 2 and number 3 have no relationship that would signify simultaneous activities. It is shown in Fig. 1a that activities 2 and 3 are overlapping before clustering.

![](/api/attachments/2CDMVNYX/fulltext/images/2e71235ef2002df557e3fdbb0ebd7aa5978b56249afc499be1ab74f63bdd0ed8.jpg)  
Fig. 1. A DSS for supply chain recon<sup>fi</sup>guration and inventory allocation.

![](/api/attachments/2CDMVNYX/fulltext/images/59ac85f0af6f8768a7f089ddf49c3a20edb3505101e31c922232e24b34446123.jpg)  
Fig. 2. General product structure of a chair.

The assembly sequencing can be used to answer technical challenge 1 by the following proposition 1.

Proposition 1. If the number of stages within the supply chain is reduced and there is no overlapping cluster in the assembly sequence planning, then the product quality of the supply chain will increase. Furthermore, higher product quality minimizes the requirement for safety stock.

Proof. Let $A _ { 1 }$ and $A _ { 2 }$ be the failure probability (e.g. lateness, inappropriate quality, etc.) for materials at stages (n−2) and (n−1) respectively, their occurrence not being mutually exclusive. Thus, the probability of creating delivery delay due to the failure of one of the two coupled materials is $p _ { f ( 2 ) } { = } A _ { 1 } { + } A _ { 2 } { - } \left( A _ { 1 } { \times } A _ { 2 } \right)$ for $A _ { n } = 1 - z _ { n }$ to represent the service level. Further, for N coupled materials we then have a failure probability as much as

$$
p _ {f (n)} = \sum_ {x = n - 1} ^ {1} A _ {(n - x)} - \left(A _ {(n - 1)} \cap A _ {(n - 2)} \cap .. \cap A _ {(1)}\right).\tag{1}
$$

The <sup>fi</sup>rst component of Eq. (1) represents the probability of failure due to one of N coupled materials. The second component represents the joint probability for two or more components to fail together. We use this formulation since in a non-mutually exclusive event, material failure can occur altogether so that the entire product manufacturing breaks down. Eq. (1) shows that the coupled operations should be decoupled or be localized and manufactured integrally in the same processing site of the supply chain. Thus, it simply informs us that the buyer will reject the material even if only one part of the material fails.

![](/api/attachments/2CDMVNYX/fulltext/images/2a02cc04f92a5c7864ce0d068d9e63f8f6f9605ef265c32d2d73f553227e1e9c.jpg)  
Fig. 3. Liaison diagram of of<sup>fi</sup>ce chair.

The localization can be accomplished by clustering the coupled operations and supplying them from the same stage to minimize ${ \cal p } _ { f ( n ) }$ Then Eq. (1) will be changed to the joint probability of failure for a non-mutually exclusive event, as follows:

$$
p _ {m f (n)} = \max \left(A _ {(n - 1)}, A _ {(n - 2)},.., A _ {(1)}\right).\tag{2}
$$

We can compare in Eq. (1) and Eq. (2) that the failure probability reduces from $p _ { f ( n ) } \ \mathrm { t o } \ p _ { m f ( n ) }$ by as much as

$$
p _ {f (n)} - p _ {m f (n)} = \sum_ {x = n - 1} ^ {1} A _ {(n - x)} - \max \left(A _ {(n - 1)}, A _ {(n - 2)},.., A _ {(1)}\right) - \left(A _ {(n - 1)} \cap A _ {(n - 2)} \cap .. \cap A _ {(1)}\right).\tag{3}
$$

Furthermore, reducing the value of $( A _ { ( n - 1 ) } \cap A _ { ( n - 2 ) } \cap . . \cap A _ { ( 1 ) } )$ supports the risk sharing effort by minimizing the number of interactions (i.e. sharing functionality, interfaces, etc) within the module. Reducing $p _ { f ( n ) }$ supports safety stock decoupling at stage (n). Finally, the safety stock reduction $\Delta S S _ { n }$ at stage n due to lower failure probability is represented as follows:

$$
\Delta S S _ {n} = z _ {n} \left(p _ {f (n)} - p _ {m f (n)}\right) \sqrt {L _ {n}}\tag{4}
$$

where $L _ { n }$ stands for delivery lead times at stage n. In the following, we describe in more detail the inventory allocation and risk sharing to minimize the total inventory costs (cycle and safety stocks) after recon<sup>fi</sup>guring the supply chain.

## 4.1.2. Inventory allocation

If one operates a supply chain while disregarding demand volatility and capacity constraints, one may encounter unexpected stock-outs, as deliveries are delayed at system bottlenecks. However, the safety stock follows a non-linear pattern and arbitrarily large for demand volatility which is only slightly greater than average demand. Therefore, by characterizing the necessary safety stock levels as probability for stock out, we can determine the optimal safety stock placement in supply chains with one or many capacity constraint(s).

![](/api/attachments/2CDMVNYX/fulltext/images/3eec7c8f05225f94b7ac345598639fd2f5f3c949948f4f9f053590b0543c0c7b.jpg)

![](/api/attachments/2CDMVNYX/fulltext/images/b9d2def458161da1eabac005e11901acdaecf1baa07e0b36bf87a7924b625089.jpg)  
Fig. 4. (a). An example of a DSM matrix. (b). An example of a clustered DSM matrix.

The inventory allocation is modeled as a GI/G/1 queue model by bearing in mind the following reasons. First, consider the demand process of the upstream stage, namely the order stream (i.e., stage n) from the downstream stage (i.e., stage n−1). Second, the model considers that the demand inter-arrival and processing rates are sometimes in heavy traf<sup>fi</sup>c $( 1 - \varepsilon ) { < } \rho _ { n }$ or sometimes not stationary and divergent at a certain demand level $V _ { i }$ at time i $( i . e . , \rho { \geq } 1 )$ for $\rho _ { n } = { \frac { \lambda _ { n } } { \mu _ { n } } } \left( \lambda _ { n } \right.$ and μ<sub>n</sub>represent demand rate and production capacity at stage n respective-$\operatorname { l y } ) .$ . As a result, the waiting time in a queue $W _ { q ( n ) }$ at stage n depends on the demand inter-arrival rate standard deviation $\sigma _ { A ( n ) }$ and service rate standard deviation $\sigma _ { n }$ [20]. Third, the model considers the lead time variability in some range $\begin{array} { r }  \mathfrak { ; - \frac { \ln \left( 1 - \rho _ { n } ^ { \ 2 } \right) } { \lambda _ { n } } { \le } W _ { q ( n ) } { \le } \frac { \lambda _ { n } \left( \sigma _ { A ( n ) } ^ { 2 } + \sigma _ { n } ^ { 2 } \right) } { 2 ( 1 - \rho _ { n } ) } } \end{array}$ . The variability of lead times $\sigma _ { A ( n ) }$ signi<sup>fi</sup>es that the supply chain allocates the inventory to cover the demand volatility $\sigma _ { V ( n ) }$ . Thus, within T time horizon with review period j from time $i = T - j$ to $\mathrm { T } , \sigma _ { A ( n ) }$ is stated as $\sigma _ { A ( n ) } =$

$$
\frac {1}{\lambda_ {n}} - \frac {1}{\lambda_ {n} + \sigma_ {V (n)}} \text {   for   } \sigma_ {V (n)} = \sqrt {\frac {\sum_ {i = T - j} ^ {T} V _ {i} - \lambda_ {n}}{j - 1}}.
$$

The longer review period of the demand j reduces the level of sensitivity about the demand changes. Lower sensitivity creates lower demand responsiveness at $\textstyle \sigma _ { n } = { \frac { 1 } { \sigma _ { V ( n ) } } } + { \frac { 1 } { \mu _ { n } } }$ since $\sigma _ { n }$ represents the stan-<sup>ð</sup> <sup>Þ</sup>dard deviation of production lead times, which is inappropriate for a non-stationary demand process. Lower demand responsiveness further suggests that the supply chain should invest in a higher level of safety stock. Thus, an analysis of demand responsiveness is required to allocate the inventory.

This article uses the order of Erlang distribution $k _ { n }$ and $h _ { n }$ to measure the operation uncertainty in non-stationary demand at stage n. The reason for using the Erlang distribution in this case is that it facilitates the calculations of a stock out that is stated by using a stock out probability formulation of Leven and Segerstedt [26] as

<sup>In</sup> h <sup>kn</sup> x<sup>kn−1</sup>e<sup>−hnx</sup> Probability for stock out p 1− J <sub>ð</sub> <sub>Þ</sub> h<sub>n</sub>−1 !

$$
d x = h _ {n} ^ {k _ {n}} e ^ {- h _ {n} I _ {n}} \sum_ {i = 0} ^ {k _ {n} - 1} I _ {n} ^ {i} \frac {1}{i ! h _ {n} ^ {k _ {n} - 1}}\tag{5}
$$

where $I _ { n }$ is the inventory on hand at stage n. For calculating the distri bution parameters the following formulas can be used:

$$
k _ {n} = \left(\frac {\lambda_ {n}}{\sigma_ {V (n)}}\right) ^ {2}\tag{6}
$$

$$
h _ {n} = \frac {\lambda_ {n}}{\sigma_ {V (n)} ^ {2}}.\tag{7}
$$

For calculating the on hand inventory at stage n, $I _ { n } ,$ the following formulas can be used:

$$
I _ {n} = \mu_ {n}. \lambda_ {n} \left(W _ {q (n)} + \frac {1}{\lambda_ {n}}\right).\tag{8}
$$

Eq. (8) signi<sup>fi</sup>es tha $I _ { n }$ is increased at the increasing value of the $\sigma _ { V ( n ) }$ and $W _ { q ( n ) } .$ . This trend signi<sup>fi</sup>es that either the lower $\bar { \sigma _ { n } ^ { 2 } }$ or the higher $\mu _ { n }$ can help the supply chain to minimize the amount of inventory allocation. This implies that safety stock can be allocated to nodes or stockholding points with higher $p _ { s o ( n ) } > S L$ [26] for SL stands for customer service level. The inventory allocation can be used to answer technical challenge 3 by the following proposition 2.

Proposition 2. If the level of $p _ { s o ( n ) }$ is higher than SL at stage n, the additional safety stock, $S S _ { n } ,$ , required by stage n is given by putting $p _ { s o ( n ) } - S L$ in the left hand side of $E q . \ ( 5 ) ,$ , and finding the demand standard deviation during delivery lead times ${ \mathcal { O } } _ { d ( n ) }$ <sub>)</sub>,by iterative calculation.

Proof. Consider a case where the level of demand variation is large and thus the probability of stock out more than the expected service level. In this situation, there are two possible outcomes for the realized demand process, i.e., the demand realization is equal to $\lambda _ { n }$ and a shortage does not occur or equal to $\lambda _ { n } + \sigma _ { V ( n ) }$ if a shortage occurs after considering SL. De<sup>fi</sup>ning $p _ { s o ( n ) } - S L$ to be the probability of having a shortage at the end of planned interval gives the safety stock of the realized order interval as an iterative calculation of $\operatorname { E q . } ( 5 ) \sqsubseteq \sqsubseteq .$

In addition to the inventory allocation problem, risk sharing is developed in Section 4.1.3 to eliminate the safety stocks in some stockholding points.

## 4.1.3. Risk sharing through safety stock allocation

Section 4.1.2 mentions that the choice of $k _ { n }$ also in<sup>fl</sup>uences the demand response across the supply chain. Lower $k _ { n }$ represents a sluggish response and, conversely, higher $k _ { n }$ represents a quicker response. Thus, in providing guaranteed lead times and anticipating the forecasting error, safety stock needs to be allocated to cover demand uncertainty by as many as

$$
S S _ {n} = Z _ {n}. \sigma_ {d (n)}. \sqrt {L _ {n}}\tag{9}
$$

we can see from Eq. (9) that $\sigma _ { d ( n ) }$ is the only factor for allocating safety stock across the supply chain at service level $z _ { n } .$ Thus we have Proposition 3, as follows.

Proposition 3. Safety stock allocation for stockholding points can be optimized by shifting the safety stock at downstream (stage n) to upstream (stage $n - 1 ) , i f \sigma _ { d ( n - 1 ) } < \sigma _ { d ( n ) }$ holds.

Proof. We can transfer safety stock at stage n to all other stages that have a direct link to stage n $\left( \phi _ { n ( n - 1 ) } = 1 \right)$ if the safety stock after risk sharing is lower than before risk sharing. Thus, we have the following relationship:

$$
\sum_ {k = n - 1} ^ {1} \Phi_ {n (n - 1)} \frac {h _ {n - 1}}{h _ {n}} \Omega_ {n (n - 1)} > 1\tag{10}
$$

$$
\Omega_ {n (n - 1)} = \frac {\left(z _ {k} . \sigma_ {d (n - 1)} . \sqrt {L _ {n} + L _ {(n - 1)}}\right)}{\left(z _ {n} . \sigma_ {d (n)} . \sqrt {L _ {n}}\right)}\tag{11}
$$

where $h _ { n }$ and $h _ { n - 1 } \mathsf { a r e }$ the safety stock costs at stages n and $n - 1$ respectively.

This article provides a graph to make the analysis in Eq. (11) faster. The decision can be taken simply by multiplying the holding cost ratio $\frac { h _ { n } } { h _ { n - 1 } }$ to $\Omega _ { n ( n - 1 ) }$ in Fig. 5. The calculation is applied to all direct links between stage n and stage k for $k = 1 \ \mathrm { t o } \ n - 1$ , such that $\phi _ { n ( n - 1 ) } = 1$ if there is a direct link, otherwise, $\begin{array} { r } { \phi _ { n ( n - 1 ) } = 0 . } \end{array}$

Fig. 5 shows that higher demand uncertainty at stage $( n - 1 )$ as compared to stage (n) encourages stage (n) to decouple safety stock to stage $( n - 1 )$ to minimize the total of safety inventory costs between the two stages. Conversely, lower demand uncertainty at stage (n) motivates both stages to keep their own safety stocks. The supply chain can extend this relationship to many stages.

![](/api/attachments/2CDMVNYX/fulltext/images/15e81208991315ea5987507900009cd2c896daacaad9c219b77cc783bf6962a5.jpg)  
Fig. 5. Holding cost ratio at different delivery lead time $\left( L _ { n } / L _ { \left( n - 1 \right) } \right)$ and demand standard deviation ratios.

## 4.2. Tactical level optimization

At the tactical level, we de<sup>fi</sup>ne a node as any activity point in the supply chain (material receiving and inspection, work in process (WIP) or intermediate product processing and <sup>fi</sup>nal product processing). Thus, in each location the supply chain has at least one activity point (i.e. material receiving and inspection for warehouse). Otherwise, the location has two activity points (i.e. material and <sup>fi</sup>nal product processing facilities), or at most three points (i.e. material, WIP and <sup>fi</sup>nal product processing facilities).

For stage n, the replenishment time, $L _ { R ( n ) } ,$ comprising production lead time, $L _ { p ( n ) }$ ,and delivery lead times, $L _ { n } ,$ is given as follows:

$$
L _ {R (n)} = L _ {p (n)} + L _ {n}.\tag{12}
$$

The delivery rate in all periods must be enough to cover the demand over the upcoming $L _ { n } .$

The optimization of tactical level comprises demand forecast, production and inventory control. Demand responsiveness in terms of inventory responses is optimized to minimize the backorders and inventory level.

## 4.2.1. Demand forecast method

We assume that in each period, t, the observed demand $D ( t )$ from period t is used to issue the demand forecast from period t to t+1 or $F ( t + 1 )$ . We assume that it is possible to set an initial inventory level $\mathrm { { I _ { n } } ( 0 ) }$ and that $F ( t ) = \lambda$ for $t { \le } 0$ and furthermore $F ( t ) { \geq } 0$

Exponential smoothing is used to estimate the future demand. The reason has its roots in the ARIMA-based demand process model, in which the forecast demand $F ( t )$ at time t and its mean value λ are de<sup>fi</sup>ned as follows [19]:

$$
F (1) = \lambda + \varepsilon (t),
$$

$$
F (t + 1) = \left(1 - \alpha_ {a}\right) F (t) + \alpha_ {a}. D (t) + \varepsilon (t),\tag{14}
$$

<sub>ð</sub><sup>13</sup><sub>Þ</sub>

$$
\varepsilon (t) = D (t) - F (t).\tag{13}
$$

Eq. (13) shows that the demand forecast, $F \left( 1 \right)$ , at time $t = 1$ depends on the mean value of customer demands, λ, and random noise term ε(t) of the time series random variable which represents the forecast error. Eq. (14) shows that the future demand forecast, F(t+1), depends on the current demand forecast, F(t) and $\varepsilon ( t )$ . The value of α stands for the smoothing constant that is obtained from time to adjust the demand response time $T _ { a }$ for $T _ { a } = 1 / \alpha _ { a }$ . When $0 < \alpha _ { a } < 1$ 1, the demand process is a non-stationary process. When $\alpha _ { a } = 1$ , Eq. (14) shows that the demand forecast is correlated to the previous demand and the demand process resembles a random walk.

## 4.2.2. Production and inventory control

Production and inventory control is accomplished by adjusting the production rates $\mu _ { n } ( t )$ at stage n to minimize <sup>fi</sup>nal product inventory $I _ { n } ( t )$ and the WIP inventory $I _ { W I P ( n ) }$ t at stage n and time t. The adjustment requires the supply chain to ful<sup>fi</sup>ll the demand from product inventory according to delivery order at stage n $, q _ { n } ( t )$ , and considers production capacity constraint $K _ { n }$ at stage n as follows:

$$
\mu_ {n} (t) = \min [ K, F (t + 1) + \Delta I _ {n} (t) + \Delta W I P _ {n} (t) ],\tag{15}
$$

$$
q _ {n} (t) = \min \left(I _ {(n)} (t), F (t + 1) + \frac {(D (t) - q _ {n} (t - L _ {n})) L _ {n}}{T _ {q (n)}}\right),\tag{16}
$$

$$
\Delta I _ {n} (t) = \frac {\left(\mu_ {n} (t) * L _ {p (n)}\right) - \left(q _ {n} (t) * L _ {n}\right)}{T _ {i (n)}},\tag{17}
$$

![](/api/attachments/2CDMVNYX/fulltext/images/dfe16203232e012f6e923b1780efcd26b32f1026ae957dff18c88325c414fd5b.jpg)  
Fig.6. Template for iteration of a genetic algorithm.

Table 1 GA parameters.

<table><tr><td>Population</td><td>100</td></tr><tr><td>Generation</td><td>200</td></tr><tr><td>Crossover %</td><td>0.7</td></tr><tr><td>Crossover method</td><td>Elitism (Recommended)</td></tr><tr><td>Mutation rate</td><td>0.000002</td></tr><tr><td>Fitness scaling</td><td>Linear normalize</td></tr></table>

$$
\Delta \mathrm{WIP} _ {(n)} (t) = \frac {I _ {\mathrm{WIP} (n)} (t) - \left(\mu_ {n} (t) * L _ {p (n)}\right)}{T _ {W (n)}}.\tag{18}
$$

In minimizing the backorders $B O _ { n } ( t )$ at stage n, the supply chain must meet the next day demand forecast $F ( \mathfrak { t } + 1 )$ by optimizing time to adjust $q _ { n } ( t )$ level $\mathrm { T } _ { q }$ and time to adjust product inventory $T _ { i }$ and WIP inventory $T _ { W } \left[ 8 , 3 6 , 4 0 \right]$ . The response parameters $( T _ { q } , T _ { i } , T _ { W } )$ represent the willing ness of the stockholding points to meet the demand changes.

## 4.2.3. Optimization of the response parameters

The response parameters are optimized to minimize $B O _ { n } ( t )$ for $B O _ { n } ( t ) = D _ { t } - \mu _ { n } ( t )$ , at minimum difference between $q _ { n } ( t )$ and $\mu _ { n } ( t )$ Since the forecast of the demand is centralized, the optimization model can be obtained by inserting Eq. (17) to Eq. (18) into Eq. (15).

However, $B O _ { n } ( t ) , \mathrm { I _ { W I P ( n ) } } ( t ) , F ( t )$ and $\varepsilon _ { n } ( t )$ are the four independent variables that are always changing. Here, the optimization should cover the worst scenario, for instance, highest standard deviation of demand $\sigma _ { d ( n ) }$ (to invest in material safety stock $\mathrm { I } _ { \mathrm { W I P } ( n ) \operatorname* { m a x } } = z _ { p } \sigma _ { d ( n ) } . \sqrt { L _ { p } }$ for $z _ { p }$ represents the maximum allowable backorders and $L _ { p }$ represents the lead time of the production process) and lowest $B O _ { n } ( t ) = D _ { t } - \mu _ { n } ( t )$ (in this article, 1% backorders is taken as the customer risk $\alpha { = } 0 . 0 1 ;$ ). Manipulating Eq. (15) to Eq. (18) to get $B O _ { n } ( t )$ we then have the following optimization problem:

$$
\min _ {T _ {a}, T _ {W (n)}, T _ {i (n)}, T _ {q (n)}} \sum_ {n = 1} ^ {N} \Delta B O _ {n} = \sum_ {n = 1} ^ {N} \frac {\frac {\sigma_ {d (n)}}{1 + T _ {a}} \left(1 - \frac {L _ {n}}{T _ {i (n)}}\right) - \frac {1}{T _ {i (n)}} \frac {B O _ {(n) \max} L _ {n} {} ^ {2}}{T _ {q (n)}} + \frac {I _ {W I P (n) \max}}{T _ {W (n)}}}{1 - L _ {p (n)} \left(\frac {T _ {W (n)} - T _ {i (n)}}{T _ {W (n)} T _ {i (n)}}\right)}\tag{19}
$$

$$
1 \leq T _ {a}, T _ {i (n)}, T _ {W (n)}, T _ {q (n)} \leq 5\tag{20}
$$

$$
T _ {q (n)} \leq T _ {i (n)}\tag{21}
$$

$$
\sum_ {n = 1} ^ {N} \Delta B O _ {n} \geq 0.\tag{22}
$$

Eq. (20) is used to constrain the limit of responsiveness. Eq. (21) signi<sup>fi</sup>es that the delivery response is quicker than the production response. This signi<sup>fi</sup>es that the supplier (upstream) commits to providing a 100% service level. Considering that the backorder is always a positive value, Eq. (22) limits the solution in Eq. (19) to be positive. Section 4.2.4 is then used to <sup>fi</sup>nd the optimum response parameters.

4.2.4. GA for parameter selection to give optimum value in the response parameters

The XLBit Genetic algorithms add-in of MS-Excel spreadsheet is used to solve the non-linear supply chain dynamics in terms of inventory, production and distribution decisions. This free general-purpose simulator combines system dynamics with some aspects of discreteevent simulation, and embeds a meta-heuristic optimization engine within a Monte Carlo simulation framework, which is well-suited for modeling time-dependent conditions or processes. The Excel spreadsheet also provides easy access for the user to edit the mathematical models in Section 4.2.3.

The solution to a problem is called a chromosome, which simply represents the parameters to be optimized. A GA creates an initial population (a collection of chromosomes), evaluates this population and then evolves the population through multiple generations in the search for a good solution to the problem in hand. GA will stop the iteration process whenever the regeneration process has reached a speci<sup>fi</sup>ed value [16,23]. Basically, GA has the structure described in Fig. 6.

Table 1 shows the GA parameters for optimizing the parameters T , $T _ { i ( n ) } , T _ { W ( n ) }$ and $T _ { q ( n ) } .$ Table 2 exhibits the input parameters which are used during the simulation. The different settings of lead times are used within the supply chain to observe the effect of lead times on the performance indicators.

## 4.3. Results and analysis

In analyzing the proposed inventory allocation model, we benchmark the original supply chain con<sup>fi</sup>guration before and after the assembly sequence planning. Part variants in Fig. 2 are used to produce eight product variants in the product family. The parts are coded into capital letters, back (A), Seat frame A (B), Seat frame B (C), Upholstery (D), Stand A (E), Stand B (F), Pad (G), Wheel (H), Armrest (I). In Table 2, proposition 2 is applied to the decision whether or not to allocate the parts and product safety stocks to the supply chain without assembly sequence planning. The parameters of $\mathbf { \dot { L } } _ { R \left( n \right) }$ and $L _ { n } , \lambda _ { n } ,$ and $\mu _ { n }$ are stated in advance. The volatility is set at 40% of $\lambda _ { n } .$ In Table 3, the same operations are applied to the supply chain con<sup>fi</sup>guration which follows assembly sequencing.

Analysis results for allocating the safety stock of the problem example (without assembly sequence planning).

<table><tr><td>Stage (n)</td><td>Component/ Product</td><td> ${\lambda }_{\mathrm{n}}$ </td><td> ${\mu }_{\mathrm{n}}$ </td><td> ${\rho }_{\mathrm{n}}$ </td><td> ${\sigma }_{\mathrm{d}\left( \mathrm{n}\right) }$ </td><td> ${\sigma }_{\mathrm{{An}})}^{2}$ </td><td> ${\sigma }_{\mathrm{n}}^{2}$ </td><td> ${\mathrm{L}}_{\mathrm{n}}$ </td><td> ${\mathrm{k}}_{\mathrm{n}}$ </td><td> ${\mathrm{h}}_{\mathrm{n}}$ </td><td> ${\sigma }_{\mathrm{{Vn}}}$ </td><td> ${\mathrm{I}}_{\mathrm{n}}$ </td><td> ${\mathrm{p}}_{\mathrm{{so}}}$ </td><td>Inventory allocation</td></tr><tr><td>3</td><td>Product ABDEGI</td><td>276</td><td>330</td><td>0.84</td><td>132</td><td>1E-06</td><td>1E-04</td><td>1</td><td>4.3</td><td>0.02</td><td>110</td><td>276</td><td>7.6E-07</td><td>No</td></tr><tr><td>3</td><td>Product ABDEHI</td><td>275</td><td>280</td><td>0.98</td><td>203</td><td>2E-06</td><td>2E-04</td><td>3</td><td>1.8</td><td>0.01</td><td>110</td><td>275</td><td>1.1E-02</td><td>Yes</td></tr><tr><td>3</td><td>Product ABDFGI</td><td>400</td><td>410</td><td>0.98</td><td>282</td><td>1E-06</td><td>8E-05</td><td>3</td><td>2.0</td><td>0.01</td><td>160</td><td>400</td><td>2.6E-03</td><td>No</td></tr><tr><td>3</td><td>Product ABDFHI</td><td>300</td><td>310</td><td>0.97</td><td>203</td><td>2E-06</td><td>1E-04</td><td>3</td><td>2.2</td><td>0.01</td><td>120</td><td>300</td><td>1.7E-03</td><td>No</td></tr><tr><td>3</td><td>Product ACDEGI</td><td>310</td><td>320</td><td>0.97</td><td>210</td><td>2E-06</td><td>1E-04</td><td>3</td><td>2.2</td><td>0.01</td><td>124</td><td>310</td><td>1.8E-03</td><td>No</td></tr><tr><td>3</td><td>Product ACDEHI</td><td>200</td><td>220</td><td>0.91</td><td>111</td><td>3E-06</td><td>3E-04</td><td>2</td><td>3.2</td><td>0.02</td><td>80</td><td>200</td><td>5.5E-05</td><td>No</td></tr><tr><td>3</td><td>Product ACDFGI</td><td>500</td><td>520</td><td>0.96</td><td>328</td><td>6E-07</td><td>5E-05</td><td>3</td><td>2.3</td><td>0.00</td><td>200</td><td>500</td><td>5.2E-04</td><td>No</td></tr><tr><td>3</td><td>Product ACDFHI</td><td>800</td><td>810</td><td>0.99</td><td>620</td><td>3E-07</td><td>2E-05</td><td>4</td><td>1.7</td><td>0.00</td><td>320</td><td>800</td><td>1.2E-02</td><td>Yes</td></tr><tr><td>2</td><td>Back</td><td>3060</td><td>4200</td><td>0.73</td><td>1247</td><td>9E-09</td><td>1E-06</td><td>1</td><td>6.0</td><td>0.00</td><td>1224</td><td>3060</td><td>1.2E-14</td><td>No</td></tr><tr><td>2</td><td>Seat</td><td>3060</td><td>4000</td><td>0.77</td><td>1313</td><td>1E-08</td><td>1E-06</td><td>1</td><td>5.4</td><td>0.00</td><td>1224</td><td>3060</td><td>6.0E-13</td><td>No</td></tr><tr><td>2</td><td>Under frame</td><td>3060</td><td>3300</td><td>0.93</td><td>1782</td><td>1E-08</td><td>1E-06</td><td>2</td><td>2.9</td><td>0.00</td><td>1224</td><td>3060</td><td>1.6E-06</td><td>No</td></tr><tr><td>1</td><td>Seat frame A</td><td>1250</td><td>2000</td><td>0.63</td><td>445</td><td>4E-08</td><td>6E-06</td><td>1</td><td>7.9</td><td>0.01</td><td>500</td><td>1250</td><td>1.6E-15</td><td>No</td></tr><tr><td>1</td><td>Seat frame B</td><td>1810</td><td>2000</td><td>0.91</td><td>995</td><td>4E-08</td><td>4E-06</td><td>2</td><td>3.3</td><td>0.00</td><td>724</td><td>1810</td><td>3.7E-07</td><td>No</td></tr><tr><td>2</td><td>Upholstery</td><td>3060</td><td>3100</td><td>0.987</td><td>2358</td><td>2E-08</td><td>1E-06</td><td>4</td><td>1.7</td><td>0.00</td><td>1224</td><td>3060</td><td>4.2E-03</td><td>No</td></tr><tr><td>1</td><td>Stand A</td><td>1060</td><td>1100</td><td>0.964</td><td>702</td><td>1E-07</td><td>3E-06</td><td>3</td><td>2.3</td><td>0.00</td><td>424</td><td>1060</td><td>2.4E-04</td><td>No</td></tr><tr><td>1</td><td>Stand B</td><td>2000</td><td>2010</td><td>0.995</td><td>1722</td><td>5E-08</td><td>3E-06</td><td>5</td><td>1.3</td><td>0.00</td><td>800</td><td>2000</td><td>5.3E-02</td><td>Yes</td></tr><tr><td>1</td><td>Pad</td><td>1485</td><td>1500</td><td>0.990</td><td>1182</td><td>9E-08</td><td>3E-06</td><td>4</td><td>1.6</td><td>0.00</td><td>594</td><td>1485</td><td>1.3E-02</td><td>Yes</td></tr><tr><td>1</td><td>Wheel</td><td>1575</td><td>1580</td><td>0.997</td><td>1420</td><td>9E-08</td><td>3E-06</td><td>5</td><td>1.2</td><td>0.00</td><td>630</td><td>1575</td><td>1.3E-01</td><td>Yes</td></tr><tr><td>1</td><td>Armrest</td><td>3060</td><td>3100</td><td>0.99</td><td>2358</td><td>2E-08</td><td>1E-06</td><td>4</td><td>1.7</td><td>0.00</td><td>1224</td><td>3060</td><td>4.2E-03</td><td>No</td></tr></table>

Analysis results for allocating the cycle inventory of the problem example (after assembly sequence planning).

<table><tr><td>Component/product</td><td> $\lambda_n$ </td><td> $μ_n$ </td><td> $ρ_n$ </td><td> $σ_{d(n)}$ </td><td> $σ_{An}^2$ </td><td> $σ_n^2$ </td><td> $L_n$ </td><td> $k_n$ </td><td> $h_n$ </td><td> $σ_{Vn}$ </td><td> $I_n$ </td><td> $p_{so}$ </td><td>Inventory allocation</td></tr><tr><td>Product ABDEGI</td><td>276</td><td>810</td><td>0.34</td><td>66</td><td>5E-07</td><td>1E-04</td><td>0</td><td>17.3</td><td>0.06</td><td>110.4</td><td>276</td><td>1.5E-20</td><td>No</td></tr><tr><td>Product ABDEHI</td><td>275</td><td>810</td><td>0.34</td><td>66</td><td>5E-07</td><td>1E-04</td><td>0</td><td>17.3</td><td>0.06</td><td>110</td><td>275</td><td>1.2E-20</td><td>No</td></tr><tr><td>Product ABDFGI</td><td>400</td><td>810</td><td>0.49</td><td>120</td><td>3E-07</td><td>6E-05</td><td>1</td><td>11.0</td><td>0.03</td><td>160</td><td>400</td><td>5.8E-17</td><td>No</td></tr><tr><td>Product ABDFHI</td><td>300</td><td>810</td><td>0.37</td><td>76</td><td>5E-07</td><td>9E-05</td><td>0</td><td>15.7</td><td>0.05</td><td>120</td><td>300</td><td>2.0E-19</td><td>No</td></tr><tr><td>Product ACDEGI</td><td>310</td><td>810</td><td>0.38</td><td>80</td><td>4E-07</td><td>9E-05</td><td>0</td><td>15.1</td><td>0.05</td><td>124</td><td>310</td><td>8.4E-20</td><td>No</td></tr><tr><td>Product ACDEHI</td><td>200</td><td>810</td><td>0.25</td><td>40</td><td>7E-07</td><td>2E-04</td><td>0</td><td>24.5</td><td>0.12</td><td>80</td><td>200</td><td>3.2E-22</td><td>No</td></tr><tr><td>Product ACDFGI</td><td>500</td><td>810</td><td>0.62</td><td>176</td><td>3E-07</td><td>4E-05</td><td>1</td><td>8.0</td><td>0.02</td><td>200</td><td>500</td><td>7.1E-14</td><td>No</td></tr><tr><td>Product ACDFHI</td><td>800</td><td>810</td><td>0.99</td><td>620</td><td>3E-07</td><td>2E-05</td><td>4</td><td>1.7</td><td>0.00</td><td>320</td><td>800</td><td>1.2E-02</td><td>Yes</td></tr><tr><td>Back</td><td>3060</td><td>4200</td><td>0.73</td><td>1247</td><td>9E-09</td><td>1E-06</td><td>1</td><td>6.0</td><td>0.00</td><td>1224</td><td>3060</td><td>1.2E-14</td><td>No</td></tr><tr><td>Seat</td><td>3060</td><td>4000</td><td>0.77</td><td>1313</td><td>1E-08</td><td>1E-06</td><td>1</td><td>5.4</td><td>0.00</td><td>1224</td><td>3060</td><td>6.0E-13</td><td>No</td></tr><tr><td>Under frame</td><td>3060</td><td>3300</td><td>0.93</td><td>1782</td><td>1E-08</td><td>1E-06</td><td>2</td><td>2.9</td><td>0.00</td><td>1224</td><td>3060</td><td>1.6E-06</td><td>No</td></tr><tr><td>Seat Frame A</td><td>1250</td><td>4000</td><td>0.31</td><td>536</td><td>6E-08</td><td>5E-06</td><td>1</td><td>5.4</td><td>0.00</td><td>500</td><td>1250</td><td>3.2E-11</td><td>No</td></tr><tr><td>Seat Frame B</td><td>1810</td><td>4000</td><td>0.45</td><td>515</td><td>1E-08</td><td>3E-06</td><td>1</td><td>12.3</td><td>0.01</td><td>724</td><td>1810</td><td>2.0E-25</td><td>No</td></tr><tr><td>Upholstery</td><td>3060</td><td>3100</td><td>0.987</td><td>2358</td><td>2E-08</td><td>1E-06</td><td>4</td><td>1.7</td><td>0.00</td><td>1224</td><td>3060</td><td>4.2E-03</td><td>No</td></tr><tr><td>Stand A</td><td>1060</td><td>3300</td><td>0.321</td><td>1860</td><td>4E-07</td><td>2E-06</td><td>1</td><td>1.0</td><td>0.00</td><td>424</td><td>1060</td><td>9.6E-01</td><td>Yes</td></tr><tr><td>Stand B</td><td>2000</td><td>3300</td><td>0.606</td><td>1860</td><td>6E-08</td><td>2E-06</td><td>1</td><td>1.2</td><td>0.00</td><td>800</td><td>2000</td><td>2.2E-01</td><td>Yes</td></tr><tr><td>Pad</td><td>1485</td><td>3300</td><td>0.450</td><td>594</td><td>4E-08</td><td>2E-06</td><td>1</td><td>6.3</td><td>0.00</td><td>594</td><td>1485</td><td>1.7E-13</td><td>No</td></tr><tr><td>Wheel</td><td>1575</td><td>3300</td><td>0.477</td><td>630</td><td>3E-08</td><td>2E-06</td><td>1</td><td>6.3</td><td>0.00</td><td>630</td><td>1575</td><td>1.2E-13</td><td>No</td></tr><tr><td>Armrest</td><td>3060</td><td>3100</td><td>0.99</td><td>2358</td><td>2E-08</td><td>1E-06</td><td>4</td><td>1.7</td><td>0.00</td><td>1224</td><td>3060</td><td>4.2E-03</td><td>No</td></tr></table>

## 4.3.1. Assembly sequencing and the supply chain reconfiguration

Each part in the product structure (Fig. 2) is represented as one stage in the supply chain. However, the two dashed line which link to the same upstream part share the same stage since those two lines are options for the customers. The DSM matrix (Fig. 7) shows that the seat and seat frame should be assembled together in one stage. Similarly, the stand and support should also be assembled together in the same stage. Two bene<sup>fi</sup>ts of the assembly sequencing re that they reduce the number of workstations from 11 stages to 6 stages and reduce the interdependencies between them.

## 4.3.2. Inventory allocation

Tables 2 and 3 show that the assembly sequence planning is capable of eliminating safety stocks in some of stockholding points at stage 3 (product ABDEHI) and stage 1 (wheel, pad, stand A), and furthermore minimizes the total safety stock costs for all the activity points within the supply chain. Tables 2 and 3 summarize $p _ { s o ( n ) }$ and if $p _ { s o ( n ) } > \left( 1 - \right.$ SL), an additional safety stock will be required (in our example SL= 0.99). Placing the safety stock iteratively according to Eq.(5) will increase the inventory position which is only slightly greater than average demand. In addition, Table 3 shows that except product ACDFHI, all the rest product variants are assigned as safety stock free locations. This implies that the supply chain can make a saving on those products and increase the agility and production capacities towards process standardization. Process standardization reduces the number of activity points within the supply chain by clustering the interdependence parts into one location.

<table><tr><td></td><td></td><td>Back</td><td>Underframe</td><td>Arm rest</td><td>Upholstery</td><td>Seat</td><td>Seat frame A</td><td>Seat Frame B</td><td>Stand A</td><td>Stand B</td><td>Pad</td><td>Wheel</td></tr><tr><td></td><td></td><td>1</td><td>3</td><td>4</td><td>5</td><td>2</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td></tr><tr><td>Back</td><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Underframe</td><td>3</td><td></td><td>3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Arm rest</td><td>4</td><td></td><td></td><td>4</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Upholstery</td><td>5</td><td></td><td></td><td></td><td>5</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Seat</td><td>2</td><td></td><td></td><td></td><td></td><td>2</td><td>1</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>Seat frame A</td><td>6</td><td></td><td>1</td><td></td><td></td><td>1</td><td>6</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Seat Frame B</td><td>7</td><td></td><td>1</td><td></td><td></td><td>1</td><td></td><td>7</td><td></td><td></td><td></td><td></td></tr><tr><td>Stand A</td><td>8</td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td>8</td><td></td><td>1</td><td>1</td></tr><tr><td>Stand B</td><td>9</td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td>9</td><td>1</td><td>1</td></tr><tr><td>Pad</td><td>10</td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td>10</td><td></td></tr><tr><td>Wheel</td><td>11</td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>1</td><td></td><td>11</td></tr></table>

Fig. 7. The assembly sequence planning for supply chain con<sup>fi</sup>guration.

## 4.3.3. Risk sharing in terms of safety stock allocation

Furthermore, Proposition 3 is used to share the risk within the supply chain. Risk sharing reduces the total inventory costs of the products and their supporting parts. Fig. 4 is used to decide on risk sharing by obtaining a lead time ratio between stage n and stage n−1, and a standard deviation ratio between stage n and stage n 1.

Table 4 shows the application of Fig. 5 and Eq. (5). Product ACDEHI is the only stage which can share its safety stock to its parts (back, seat, under frame, upholstery and armrest). It is shown by iteratively calculating Eq. (5) that the holding costs are the determining factor in deciding on risk sharing. In addition, $\sigma _ { V ( n ) }$ also affects the risk sharing decision. It is shown that the product or parts safety stocks are shared if the demand standard deviation at stage n is lower than stage k for k=1 to n 1.

Safety stock allocation for stockholding points.

<table><tr><td rowspan="2">Component/ Product</td><td rowspan="2"> $\lambda_n$ </td><td rowspan="2"> $σ_d$ (Eq. 5)</td><td rowspan="2"> $σ_d$ (Tables 2 and 3)</td><td rowspan="2"> $h_n$ </td><td>Safety stock costs Eq. (5)</td><td>Safety stock costs(Table 2 and 3)</td></tr><tr><td>Product ACDFHI</td><td>Product ACDFHI</td></tr><tr><td>Product ACDEHI</td><td>800</td><td>620</td><td>620</td><td>1</td><td>2030</td><td>2030</td></tr><tr><td>Back</td><td>3060</td><td>420</td><td>1247</td><td>0.25</td><td>181</td><td>537</td></tr><tr><td>Seat</td><td>3060</td><td>585</td><td>1313</td><td>0.25</td><td>265</td><td>595</td></tr><tr><td>Under frame</td><td>3060</td><td>700</td><td>1782</td><td>0.25</td><td>431</td><td>1096</td></tr><tr><td>Armrest</td><td>3060</td><td>1020</td><td>2358</td><td>0.25</td><td>830</td><td>1919</td></tr><tr><td></td><td colspan="3">Safety stock allocation</td><td></td><td>Share</td><td>Not share</td></tr></table>

Table 5  
Table 6  
Optimum value of $T _ { a } , T _ { i ( n ) } , T _ { W ( n ) }$ and $T _ { q ( n ) } .$

<table><tr><td>Stage</td><td>Ta</td><td>Ti</td><td>Tw</td><td>Tq</td></tr><tr><td>Product</td><td>4.9</td><td>3</td><td>2.1</td><td>1.3</td></tr><tr><td>Back</td><td>4.9</td><td>2.5</td><td>2</td><td>1.2</td></tr><tr><td>Underframe</td><td>4.9</td><td>2.5</td><td>2</td><td>1.2</td></tr><tr><td>Arm rest</td><td>4.9</td><td>2.5</td><td>2</td><td>1.1</td></tr><tr><td>Upholstery</td><td>4.9</td><td>2.5</td><td>2</td><td>1.2</td></tr><tr><td>Seat frame</td><td>4.9</td><td>3.2</td><td>1.6</td><td>0.6</td></tr><tr><td>Underframe</td><td>4.9</td><td>3.4</td><td>1.2</td><td>0.6</td></tr></table>

4.3.4. Optimum value of response parameters $T _ { i ( n ) } , T _ { W ( n ) }$ and $T _ { q ( n ) } .$

The optimum inventory response parameters to minimize the backorders and inventory level are presented in Table 5. The responses are applied to the new con<sup>fi</sup>guration of supply chain (Fig. 7) and we have six workstations.

## 5. Model validation and management decision-making

We chose products ABDEHI and ABDEGI in the simulation, since both products act as stockholding (before clustering) and non-stockholding points.

## 5.1. Model validation

The simulation validates the amount of safety stock of the two adjacent stages in the supply chain (the <sup>fi</sup>nal product at stage n and its direct upstream at stage n − 1). The safety stock is counted as the required safety stock for products ABDEHI and ABDEGI. In order to validate the proposed analytical model, GoldSim simulation software developed by the GoldSim Technology Group is used. This general purpose simulator combines system dynamics with some aspects of discrete-event simulation, and embeds a dynamic simulation engine within a Monte Carlo simulation framework, which is well-suited for modeling time-dependent conditions or processes. The analytical models and discrete event simulation are tested at different levels of demand volatility. All other parameters in the model follow Tables 2 to 5. Moreover, some failure rates in the assembly plants are introduced to accommodate the effect of process quality to the backorders.

The validation applies the ANOVA (Table 12). In Tables 6 and 7, the analytical models of safety stock are not statistically different from the simulation safety stocks at a signi<sup>fi</sup>cant 5% level, where average Pvalues are 0.843 in all stages. The results show that the analytical model is capable of hedging demand variations. However, the results also show that the product ABDEGI inventory allocation by simulation is slightly higher than the analytical model and the opposite feature applies to product ABDEHI safety stock allocation. This signi<sup>fi</sup>es that product ABDEHI has higher inventory variance than product ABDEGI because of a higher number of stockholding points.

In addition to safety stock analysis, Tables 8 and 9 make it clear that the simulation has a different order rate at different demand volatility levels. The results imply that in non-stationary demand, the dy namic lot sizing is important in providing 100% guarantee lead times (Tables 10 and 11). Furthermore, in non-stationary demand, a more frequent demand sampling period is suggested, either for the simulation or the analytical model.

## 5.2. Management decision-making

In addition to the DSS model validation, Tables 6 and 7 illustrate that either at lower demand volatility $( \sigma _ { \mathrm { V A } } = 0 . 2 )$ or higher demand volatility $( \sigma _ { \mathrm { { V A } } } = 0 . 4 )$ , the product ABDEHI inventory allocation for the downstream stage (n) is always higher than for the upstream stage (n−1). This implies that the proposed analytical and simulation models are capable of sharing the risk in terms of safety stock allocation and improving the quality of information about demand. Tables 8 and 9 summarize that the magni<sup>fi</sup>cation of the order is eliminated without creating excessive backorders (Tables 10 and 11). Thus, the proposed DSS model contributes to current DSS commercial software (i.e. SAP APO, I2 Rhythm) [1,21,34] by optimally designing supply chain networks, and at the same time allocating the inventory with the fewest possible backorders.

Inventory allocation between the analytical model and simulation for product ABDEHI.

<table><tr><td>Demand process</td><td>Product ABDEHI safety stock</td><td>Simulation</td><td>Analytical model</td><td>Difference</td><td>Demand process</td><td>Product ABDEHI safety stock</td><td>Simulation</td><td>Analytical model</td><td>Difference</td></tr><tr><td rowspan="2"> $\sigma_{VA}=0.4; \lambda_n=200$ </td><td>Stage-n</td><td>200</td><td>191</td><td>9</td><td> $\sigma_{VA}=0.2; \lambda_n=200$ </td><td>Stage-n</td><td>102</td><td>96</td><td>6</td></tr><tr><td>Stage k</td><td>190</td><td>235</td><td>-45</td><td></td><td>Stage k</td><td>95</td><td>118</td><td>-23</td></tr><tr><td rowspan="2"> $\sigma_{VA}=0.4; \lambda_n=250$ </td><td>Stage-n</td><td>240</td><td>239</td><td>1</td><td> $\sigma_{VA}=0.2; \lambda_n=250$ </td><td>Stage-n</td><td>166</td><td>120</td><td>46</td></tr><tr><td>Stage k</td><td>190</td><td>244</td><td>-54</td><td></td><td>Stage k</td><td>133</td><td>122</td><td>11</td></tr><tr><td rowspan="2"> $\sigma_{VA}=0.4; \lambda_n=275$ </td><td>Stage-n</td><td>259</td><td>263</td><td>-4</td><td> $\sigma_{VA}=0.2; \lambda_n=275$ </td><td>Stage-n</td><td>117</td><td>131</td><td>14</td></tr><tr><td>Stage k</td><td>235</td><td>248</td><td>-13</td><td></td><td>Stage k</td><td>128</td><td>124</td><td>4</td></tr><tr><td rowspan="2"> $\sigma_{VA}=0.4; \lambda_n=310$ </td><td>Stage-n</td><td>270</td><td>296</td><td>-26</td><td> $\sigma_{VA}=0.2; \lambda_n=310$ </td><td>Stage-n</td><td>106</td><td>105</td><td>1</td></tr><tr><td>Stage k</td><td>236</td><td>254</td><td>-18</td><td></td><td>Stage k</td><td>105</td><td>109</td><td>-4</td></tr><tr><td>Average difference</td><td></td><td></td><td></td><td>-18</td><td>Average difference</td><td></td><td></td><td></td><td>7</td></tr></table>

Inventory allocation between analytical model and simulation for product ABDEGI.

<table><tr><td>Demand process</td><td>Product ABDEGI safety stock</td><td>Simulation</td><td>Analytical model</td><td>Difference</td><td>Demand process</td><td>Product ABDEGI safety stock</td><td>Simulation</td><td>Analytical model</td><td>Difference</td></tr><tr><td rowspan="2"> $\sigma_{VA}=0.4; \lambda_n=200$ </td><td>Stage-n</td><td>0</td><td>0</td><td>0</td><td> $\sigma_{VA}=0.2; \lambda_n=200$ </td><td>Stage-n</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Stage k</td><td>265</td><td>263</td><td>2</td><td></td><td>Stage k</td><td>137</td><td>131</td><td>6</td></tr><tr><td rowspan="2"> $\sigma_{VA}=0.4; \lambda_n=250$ </td><td>Stage-n</td><td>0</td><td>0</td><td>0</td><td> $\sigma_{VA}=0.2; \lambda_n=250$ </td><td>Stage-n</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Stage k</td><td>280</td><td>272</td><td>8</td><td></td><td>Stage k</td><td>141</td><td>136</td><td>5</td></tr><tr><td rowspan="2"> $\sigma_{VA}=0.4; \lambda_n=275$ </td><td>Stage-n</td><td>0</td><td>0</td><td>0</td><td> $\sigma_{VA}=0.2; \lambda_n=275$ </td><td>Stage-n</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Stage k</td><td>270</td><td>277</td><td>-7</td><td></td><td>Stage k</td><td>151</td><td>138</td><td>13</td></tr><tr><td rowspan="2"> $\sigma_{VA}=0.4; \lambda_n=310$ </td><td>Stage-n</td><td>0</td><td>0</td><td>0</td><td> $\sigma_{VA}=0.2; \lambda_n=310$ </td><td>Stage-n</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Stage k</td><td>297</td><td>284</td><td>13</td><td></td><td>Stage k</td><td>153</td><td>142</td><td>11</td></tr><tr><td>Average difference</td><td></td><td></td><td></td><td>2</td><td>Average difference</td><td></td><td></td><td></td><td>4</td></tr></table>

Table 9  
Table 8  
Order rate between analytical model and simulation for product ABDEHI.

<table><tr><td>Demand process</td><td>Product ABDEHI order rate</td><td>Simulation</td><td>Analytical model</td><td>Difference</td><td>Demand process</td><td>Product ABDEHI safety stock</td><td>Simulation</td><td>Analytical model</td><td>Difference</td></tr><tr><td rowspan="2"> $\sigma_{VA}=0.4; \lambda_n=200$ </td><td>Stage-n</td><td>220</td><td>200</td><td>20</td><td rowspan="2"> $\sigma_{VA}=0.2; \lambda_n=200$ </td><td>Stage-n</td><td>185</td><td>200</td><td>-15</td></tr><tr><td>Stage k</td><td>198</td><td>200</td><td>-2</td><td>Stage k</td><td>185</td><td>200</td><td>-15</td></tr><tr><td rowspan="2"> $\sigma_{VA}=0.4; \lambda_n=250$ </td><td>Stage-n</td><td>218</td><td>250</td><td>-32</td><td rowspan="2"> $\sigma_{VA}=0.2; \lambda_n=250$ </td><td>Stage-n</td><td>238</td><td>250</td><td>-12</td></tr><tr><td>Stage k</td><td>248</td><td>250</td><td>-2</td><td>Stage k</td><td>242</td><td>250</td><td>-8</td></tr><tr><td rowspan="2"> $\sigma_{VA}=0.4; \lambda_n=275$ </td><td>Stage-n</td><td>264</td><td>275</td><td>-11</td><td rowspan="2"> $\sigma_{VA}=0.2; \lambda_n=275$ </td><td>Stage-n</td><td>265</td><td>275</td><td>-10</td></tr><tr><td>Stage k</td><td>269</td><td>275</td><td>-6</td><td>Stage k</td><td>271</td><td>275</td><td>-4</td></tr><tr><td rowspan="2"> $\sigma_{VA}=0.4; \lambda_n=310$ </td><td>Stage-n</td><td>302</td><td>310</td><td>-8</td><td rowspan="2"> $\sigma_{VA}=0.2; \lambda_n=310$ </td><td>Stage-n</td><td>299</td><td>310</td><td>-11</td></tr><tr><td>Stage k</td><td>305</td><td>310</td><td>-5</td><td>Stage k</td><td>285</td><td>310</td><td>-25</td></tr></table>

Order rate between analytical model and simulation for product ABDEGI

<table><tr><td>Demand process</td><td>Product ABDEGI order rate</td><td>Simulation</td><td>Analytical model</td><td>Difference</td><td>Demand process</td><td>Product ABDEGI order rate</td><td>Simulation</td><td>Analytical model</td><td>Difference</td></tr><tr><td rowspan="2"> $\sigma_{\text{VA}} = 0.4; \lambda_n = 200$ </td><td>Stage-n</td><td>203</td><td>200</td><td>3</td><td> $\sigma_{\text{VA}} = 0.2; \lambda_n = 200$ </td><td>Stage-n</td><td>203</td><td>200</td><td>3</td></tr><tr><td>Stage k</td><td>195</td><td>200</td><td>-5</td><td></td><td>Stage k</td><td>205</td><td>200</td><td>5</td></tr><tr><td rowspan="2"> $\sigma_{\text{VA}} = 0.4; \lambda_n = 250$ </td><td>Stage-n</td><td>251</td><td>250</td><td>1</td><td> $\sigma_{\text{VA}} = 0.2; \lambda_n = 250$ </td><td>Stage-n</td><td>271</td><td>250</td><td>-11</td></tr><tr><td>Stage k</td><td>243</td><td>250</td><td>-7</td><td></td><td>Stage k</td><td>227</td><td>250</td><td>-23</td></tr><tr><td rowspan="2"> $\sigma_{\text{VA}} = 0.4; \lambda_n = 275$ </td><td>Stage-n</td><td>273</td><td>275</td><td>-2</td><td> $\sigma_{\text{VA}} = 0.2; \lambda_n = 275$ </td><td>Stage-n</td><td>271</td><td>275</td><td>-4</td></tr><tr><td>Stage k</td><td>277</td><td>275</td><td>2</td><td></td><td>Stage k</td><td>217</td><td>245</td><td>-28</td></tr><tr><td rowspan="2"> $\sigma_{\text{VA}} = 0.4; \lambda_n = 310$ </td><td>Stage-n</td><td>315</td><td>310</td><td>5</td><td> $\sigma_{\text{VA}} = 0.2; \lambda_n = 310$ </td><td>Stage-n</td><td>311</td><td>310</td><td>1</td></tr><tr><td>Stage k</td><td>310</td><td>310</td><td>0</td><td></td><td>Stage k</td><td>317</td><td>310</td><td>7</td></tr></table>

We need to be cautious about the analytical model, since it assumes that increasing demand volatility should be responded to linearly by providing extra safety stock. However, the simulation shows that the trend is not linear. Furthermore, with higher demand volatility, the backorder level of the simulation is a little higher than that of the analytical model. We suggest a shorter sampling period of demand to reduce this difference, or using simulation to investigate the true pattern of the demand process. We can validate our suggestion by measuring order rates in the three stage supply chain (Tables 10 and 11). Furthermore, a shorter sampling period implies that a lower number of stockholding points in the supply chain make the supply chain more autonomous. The reason is that the length of the supply chain is reduced and the supply chain con<sup>fi</sup>guration becomes simpler than before. The simpler supply chain brings the opportunity to meet the production and distribution decisions in terms of economies of scale of transportation cost. Below, the contributions of the DSS to current commercial DSS are summarized (Table 13).

## 6. Concluding remarks

The proposed DSS model improves supply chain ef<sup>fi</sup>ciency through supply chain recon<sup>fi</sup>guration and inventory allocation [18,19]. Furthermore, risk sharing adds bene<sup>fi</sup>t to the supply chain by reducing the safety stock investment. Proposition 1 endorses the importance of product functional analysis and assembly sequencing to supply chain recon<sup>fi</sup>guration [22]. Proposition 2 suggests a condition for safety stock allocation, and Proposition 3 guides us to decide on the conditions in which the safety stock can be decoupled. The safety stock decoupling can minimize the effect of demand uncertainty and inventory cost [4,31]. The model validation benchmarks the proposed analytical model against the simulation model, at the same model parameters. The statistical analysis for stockholding and non-stockholding points shows that the analytical and simulation models are not statistically different in terms of safety stock levels, order rates and backorders.

The supply chain recon<sup>fi</sup>guration reduces safety stock distribution at a lower number of stockholding points. Furthermore, the new supply chain con<sup>fi</sup>guration makes the supply chain more autonomous. The level of autonomy is higher when the interdependencies among stages in the supply chain are minimized. In addition, autonomy encourages supplier and buyer coordination. Finally, the value of the demand forecast is higher at a higher level of supplier and buyer coordination [3].

However, our model has two drawbacks: <sup>fi</sup>rst, the smoothing constant of the demand forecast is not related to supply and demand uncertainty. However, this relation is important in deciding the level of responsiveness at which the safety stock can be eliminated. The second drawback is the limitation of the analytical model in being sensitive to backorders. It is shown in Tables 10 and 11 that the simulation yields a variety of results on backorders. In the future, the

Table 10  
Backorders between analytical model and simulation for product ABDEHI.

<table><tr><td>Demand process</td><td>Product ABDEHI order rate</td><td>Simulation</td><td>Analytical model</td><td>Difference</td><td>Demand process</td><td>Product ABDEHI safety stock</td><td>Simulation</td><td>Analytical model</td><td>Difference</td></tr><tr><td rowspan="2"> $\sigma_{\text{VA}} = 0.4; \lambda_n = 200$ </td><td>Stage-n</td><td>2</td><td>2</td><td>0</td><td rowspan="2"> $\sigma_{\text{VA}} = 0.2; \lambda_n = 200$ </td><td>Stage-n</td><td>0</td><td>1</td><td>1</td></tr><tr><td>Stage k</td><td>1</td><td>2</td><td>0</td><td>Stage k</td><td>1</td><td>1</td><td>0</td></tr><tr><td rowspan="2"> $\sigma_{\text{VA}} = 0.4; \lambda_n = 250$ </td><td>Stage-n</td><td>1</td><td>2</td><td>-1</td><td rowspan="2"> $\sigma_{\text{VA}} = 0.2; \lambda_n = 250$ </td><td>Stage-n</td><td>1</td><td>2</td><td>-1</td></tr><tr><td>Stage k</td><td>2</td><td>2</td><td>0</td><td>Stage k</td><td>1</td><td>2</td><td>-1</td></tr><tr><td rowspan="2"> $\sigma_{\text{VA}} = 0.4; \lambda_n = 275$ </td><td>Stage-n</td><td>3</td><td>4</td><td>-1</td><td rowspan="2"> $\sigma_{\text{VA}} = 0.2; \lambda_n = 275$ </td><td>Stage-n</td><td>0</td><td>2</td><td>-2</td></tr><tr><td>Stage k</td><td>4</td><td>4</td><td>0</td><td>Stage k</td><td>0</td><td>2</td><td>-2</td></tr><tr><td rowspan="2"> $\sigma_{\text{VA}} = 0.4; \lambda_n = 310$ </td><td>Stage-n</td><td>4</td><td>4</td><td>0</td><td rowspan="2"> $\sigma_{\text{VA}} = 0.2; \lambda_n = 310$ </td><td>Stage-n</td><td>2</td><td>2</td><td>0</td></tr><tr><td>Stage k</td><td>3</td><td>4</td><td>-1</td><td>Stage k</td><td>1</td><td>2</td><td>-1</td></tr></table>

Table 11  
Backorders between analytical model and simulation for product ABDEGI.

<table><tr><td>Demand process</td><td>Product ABDEGI order rate</td><td>Simulation</td><td>Analytical model</td><td>Difference</td><td>Demand process</td><td>Product ABDEGI order rate</td><td>Simulation</td><td>Analytical model</td><td>Difference</td></tr><tr><td rowspan="2"> $\sigma_{\text{VA}} = 0.4; \lambda_n = 200$ </td><td>Stage-n</td><td>2</td><td>2</td><td>0</td><td rowspan="2"> $\sigma_{\text{VA}} = 0.2; \lambda_n = 200$ </td><td>Stage-n</td><td>1</td><td>1</td><td>0</td></tr><tr><td>Stage k</td><td>2</td><td>2</td><td>0</td><td>Stage k</td><td>1</td><td>1</td><td>0</td></tr><tr><td rowspan="2"> $\sigma_{\text{VA}} = 0.4; \lambda_n = 250$ </td><td>Stage-n</td><td>3</td><td>2</td><td>1</td><td rowspan="2"> $\sigma_{\text{VA}} = 0.2; \lambda_n = 250$ </td><td>Stage-n</td><td>1</td><td>2</td><td>-1</td></tr><tr><td>Stage k</td><td>2</td><td>2</td><td>0</td><td>Stage k</td><td>1</td><td>2</td><td>-1</td></tr><tr><td rowspan="2"> $\sigma_{\text{VA}} = 0.4; \lambda_n = 275$ </td><td>Stage-n</td><td>3</td><td>4</td><td>-1</td><td rowspan="2"> $\sigma_{\text{VA}} = 0.2; \lambda_n = 275$ </td><td>Stage-n</td><td>2</td><td>2</td><td>0</td></tr><tr><td>Stage k</td><td>3</td><td>4</td><td>-1</td><td>Stage k</td><td>1</td><td>2</td><td>-1</td></tr><tr><td rowspan="2"> $\sigma_{\text{VA}} = 0.4; \lambda_n = 310$ </td><td>Stage-n</td><td>4</td><td>4</td><td>0</td><td rowspan="2"> $\sigma_{\text{VA}} = 0.2; \lambda_n = 310$ </td><td>Stage-n</td><td>3</td><td>2</td><td>1</td></tr><tr><td>Stage k</td><td>4</td><td>4</td><td>0</td><td>Stage k</td><td>2</td><td>2</td><td>0</td></tr></table>

Table 12  
ANOVA test of analytical model and simulation differences.

<table><tr><td rowspan="2">System parameter</td><td colspan="2">F</td><td colspan="2">P-value</td></tr><tr><td>Product ABDEHI</td><td>Product ABDEGI</td><td>Product ABDEHI</td><td>Product ABDEGI</td></tr><tr><td>Safety stock difference (analytical model and simulation model)</td><td>0.107</td><td>0.005</td><td>0.746</td><td>0.939</td></tr><tr><td>Order rate (analytical model and simulation model)</td><td>0.312</td><td>0.017</td><td>0.58</td><td>0.896</td></tr><tr><td>Backorders (analytical model and simulation model)</td><td>3.253</td><td>4.171</td><td>0.081</td><td>0.612</td></tr></table>

Table 13  
Comparison of other operational level Supply Chain Optimization software.

<table><tr><td></td><td>SAP APO [23]</td><td>I2 RHYTIM [23]</td><td>The proposed DSS</td></tr><tr><td>Demand Planning</td><td>1. Promotional planning, causal analysis2. life cycle concept3. Collaborative forecasting</td><td>Forecasting process through statistical methods and multiple inputs from different organization units</td><td>1. Centralized forecast2. Supply chain reconfiguration3. Aligning product and supply chain reconfiguration</td></tr><tr><td>Available to promise (ATP)</td><td>1. Rule-based ATP2. Multi-level multi site ATP.3. Capable to Promise (CTP) function</td><td>User friendly product catalog and product configuration</td><td>1. Inventory allocation2. Risk sharing3. Implement APIOBPCS</td></tr><tr><td>Distribution Planning</td><td>1. Transportation planning and vehicle scheduling to multi-site optimization by GA and additional heuristic components2. VMI Support3. Demand-supply synchronization</td><td>Use transportation modeler, optimizer and manager order by customer service and financial settlement</td><td>1. VMI application.2. The application of APIOBPCS3. Optimal response on demand and supply synchronization</td></tr></table>

effect of demand sampling frequency must be considered. Thus, the analytical model should optimize the demand forecast method in order to obtain the minimum backorders.

## Acknowledgments

The authors are most grateful to two anonymous reviewers for their constructive and helpful comments which helped to improve the presentation of the paper considerably.

This research is supported by FUDGE Project and Fimmec under contract agreement with the Department of Production, University of Vaasa, Finland.

## References

[1] S. Bagchi, S. Buckley, M. Ettl, G.Y. Lin, Experience using IBM supply chain simulator, in: D.J. Medeiros, E.F. Watson, J.S. Carson, M.S. Manivannan (Eds.), Proceedings of the 1998 Winter Simulation Conference, 1998, pp. 1387–1394.

[2] K.R. Balachandran, S. Radhakrishnan, Quality implications of warranties in a supply chain, Management Science 51 (8) (2005) 1266–1277.

[3] S. Balan, P. Vrat, P. Kumar, Information distortion in supply chain and its mitigation using a soft computing approach, Omega: The International Journal of Management Science 37 (2009) 282–299.

[4] G.P. Cachon, The allocation of inventory risk in a supply chain: push, pull, and advance-purchase discount contracts, Management Science 50 (2) (2004) 222–238.

[5] H.K. Chan, F.T.S. Chan, Comparative study of adaptability and <sup>fl</sup>exibility in distributed manufacturing supply chains, Decision Support Systems 48 (2010) 331–341.

[6] T.C.E. Cheng, C. Gao, H. Shen, Production planning and inventory allocation of a single-product assemble-to-order system with failure-prone machines International Journal of Production Economics 131 (2) (2011) 604–617.

[7] T.W. Chien, A. Balakrishnan, R.T. Wong, An integrated inventory allocation and vehicle routing problem, Transportation Science 23 (2) (1989) 67–76.

[8] J. Dejonckheere, S.M. Disney, M.R. Lambrecht, D.R. Towill, The impact of information enrichment on the Bullwhip effect in supply chains: a control engineering perspective European Journal of Operational Research 153 (2004) 727–750.

[9] Q. Dong, D. Whitney, Designing a requirement driven product development process, 13th International Conference on Design Theory and Methodology, ASME, Pittsburgh, 2001.

[10] X. Du, J. Jiao, M.M. Tseng, Architecture of product family for mass customization, ICMIT conference, 2000, pp. 437–443.

[11] A. Federgruen, P. Zipkin, A combined vehicle routing and inventory allocation problem, Operations Research 32 (5) (1984) 1019–1037.

[12] E. Feitzinger, H.L. Lee, Mass customization at Hewlett Packard: the power of postponement, Harvard Business Review, January–February 1997, pp. 116–121.

[13] G. Ferrer, Open architecture, inventory pooling and maintenance modules, International Journal of Production Economics 128 (1) (2010) 393–403.

[14] C. Gao, H. Shen, T.C.E. Cheng, Order-ful<sup>fi</sup>llment performance analysis of an assemble-to-order system with unreliable machines, International Journal of Production Economics 126 (2) (2010) 341–349.

[15] E. Gebennini, R. Gamberini, R. Manzzini, An integrated production–distribution model for the dynamic location and allocation problem with safety stock optimization, International Journal of Production Economics 122 (1) (2009) 286–304.

[16] M. Gen, R. Cheng, Genetic Algorithms and Engineering Design, John Wiley and Sons Inc, New York, 1997.

[17] S.C. Graves, B.T. Tomlin, Process <sup>fl</sup>exibility in supply chains, Management Science 49 (7) (2003) 907–919.

[18] S.C. Graves, S.P. Willems, Optimization the supply chain con<sup>fi</sup>guration for new products, Management Science 51 (8) (2005) 1165–1180.

[19] S.C. Graves, S.P. Willems, Strategic inventory placement in supply chains: nonstationary demand, Manufacturing and Service Operations Management 10 (2) (2008) 278–287.

[20] D. Gross, C.M. Harris, Fundamental of Queueing Theory, John Willey and Sons, New York, 1974.

[21] P. Helo, Y. Xiao, J.R. Jiao, A web based logistics management system for agile supply demand network design, Journal of Manufacturing Technology Management 17 (8) (2006) 1058–1077.

[22] M. Jin, Y. Luo, S.D. Eksioglu, Integration of production sequencing and outbound logistics in the automotive industry, International Journal of Production Economics 113 (2) (2008) 766–774.

[23] R. Klein, Genetic algorithm, in: H. Stadtler, C. Kilger (Eds.), Supply Chain Management and Advanced Planning: Concepts, Models, Software and Case Studies, Second Edition. Springer-Verlag, Berlin, 2002, pp. 404–410.

[24] H.L. Lee, Effective inventory and service management through product and process redesign, Operations Research 90 (3) (1996) 361–367.

[25] H.L. Lee, C. Billington, Managing supply chain inventories: pitfalls and opportunities Sloan Management Review 33 (3) (1992) 65–73.

[26] E. Leven, A. Segerstedt, Inventory control with a modi<sup>fi</sup>ed Croston procedure and Erlang distribution, International Journal of Production Economics 90 (2004) 361–367.

[27] S. Li, B. Lin, Accessing information sharing and information quality in supply chain management, Decision Support Systems 42 (2006) 1641–1656.

[28] H. Ma, R. Davidrajuh, An iterative approach for distribution chain design in agile virtual environment, Industrial Management and Data Systems 105 (6) (2005) 815–834.

[29] J.J. Neale, S.P. Willems, Managing inventory in supply chains with nonstationary demand, Interfaces 39 (5) (2009) 388–399.

[30] S. Novak, S.D. Eppinger, Sourcing by design: product complexity and the supply chain, Management Science 47 (1) (2001) 189–204.

[31] G. Pishchulov, K. Richter, Inventory rationing and sharing in pre-sell distribution with mobile communication technologies, International Journal of Production Economics 121 (2) (2009) 584–600.

[32] C.J. Robinson, M.J. Maholtra, De<sup>fi</sup>ning the concept of supply chain quality management and its relevance to academic and industrial practice, International Journal of Production Economics 96 (2005) 315–337.

[33] J. Shang, P.R. Tadikamalla, L.J. Kirsch, A decision support system for managing inventory at GlaxoSmithKline, Decision Support Systems 46 (2008) 1–13.

[34] H. Stadtler, Supply chain management — an overview, in: H. Stadtler, C. Kilger (Eds.), Supply Chain Management and Advanced Planning: Concepts, Models, Software and Case Studies, Second Edition, Springer, Verlag, Berlin, 2002, pp. 7–29.

[35] N.P. Suh, Axiomatic Design: Advanced and Application, Oxford University Press, New York, 2001.

[36] H. Topaloglu, S. Kunnumkal, Approximate dynamic programming methods for an inventory allocation under uncertainty, Naval Research Logistics (2006) 822–841 Doi:10.10027nav.20164.

[37] D.R. Towill, S.M. Disney, The effect of vendor managed inventory (VMI) dynamics on the Bullwhip Effect in supply chains, International Journal of Production Economics 85 (1) (2003) 199–215.

[38] P. van der Vlist, R. Kuik, B. Verheijen, Note on supply chain integration in vendormanaged inventory, Decision Support Systems 44 (2007) 360–365.

[39] W.T. Wang, H.M. Wee, H.S.J. Tsao, Revisiting the note on supply chain integration in vendor-managed inventory, Decision Support Systems 48 (2010) 419–420.

[40] D.E. Whitney, Manufacturing by design, Harvard Business Review, July–August 1988, pp. 83 –91.

[41] J. Wikner, M.M. Naim, M. Rudberg, Exploiting the order book for mass customized manufacturing control systems with capacity limitation, IEEE Transactions on Engineering Management 54 (1) (2007) 145–155.

[42] Y. Yao, P.T. Ever, M.E. Dresner, Supply chain integration in vendor managed inventory, Decision Support Systems 43 (2007) 663–674.

[43] A. Yassine, D. Falkenburg, K. Chelst, Engineering design management: an information structure approach, International Journal of Production Research 37 (1999) 2957-2975

Yohanes Kristianto is now a Project researcher in Industrial Management at University of Vaasa, Finland. He earned a PhD in Industrial Management from Department of Production, University of Vaasa, Finland. His research interests are in the area of supply-chain strategy/ management and production/operations management. He has 11 years of working experi ence in the areas of quality management, logistics and process engineering.

Angappa Gunasekaran, PhD, is a Professor of Operations Management and the Chairperson of the Department of Decision and Information Science at the Charlton College of Business, the University of Massachusetts-Dartmouth, USA. He has over 200 articles published in 40 different peer-reviewed journals. He is on the Editorial Board of over 20 journals and the Editor of several journals in the <sup>fi</sup>elds of operations management and information systems. He is currently interested in researching the decision support systems in logistics and supply chain management. He is also the Director of the Business Innovation Research Center at the University of Massachusetts-Dartmouth.

Petri Helo is a Research Professor and the head of Logistics Systems Research Group, Department of Production, University of Vaasa. He earned a PhD in Industrial Management from Department of Production, University of Vaasa, Finland. His research addresses the management of logistics processes in supply demand networks, which take place in electronics, machine building, and food industries. Dr. Helo is also partner at Wapice Ltd, a solution provider of sales con<sup>fi</sup>gurator systems and tailored mass customization solutions; and visiting professor at Kasetsart University in Thailand, and FH Kiel in Germany.

Dr. Maqsood Sandhu is working at the Department of Business Administration, Faculty of Business and Economics at United Arab Emirates University, Al Ain since August 2008. He earned a PhD from Swedish School of Economics and Business Administration in Management. Sandhu has been working over <sup>fi</sup>ve years in project-based industry. Dr Maqsood has over 15 years' experience in academia and industry. He has been very active in initiating collaborative partnerships amongst academia, industry and policy making bodies. He is Author or Co-author of over 25 international journals articles and has presented over 50 papers and published about 40 articles in international conference proceedings. Currently, he is interested in doing research in the areas of project management, supply chain management and international entrepreneurship.

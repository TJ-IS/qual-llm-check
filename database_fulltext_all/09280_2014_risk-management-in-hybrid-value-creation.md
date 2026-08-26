---
otero_id: 9280
otero_key: "A5KT6TXK"
title: "Risk management in hybrid value creation"
authors: "Holger Schrödl; Klaus Turowski"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.12.042"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Risk management in hybrid value creation

Holger Schrödl <sup>a,</sup>⁎, Klaus Turowski <sup>b</sup>

<sup>a</sup> Otto-von-Guericke University of Magdeburg, Chair of Business Informatics I, Magdeburg, German

<sup>b</sup> Otto-von-Guericke University of Magdeburg, MRCC Research Cluster VLBA, Magdeburg, Germany

## a r t i c l e i n f o

Article history: Received 1 August 2011 Accepted 31 December 2012 Available online xxxx

Keywords: Value networks Hybrid value bundles Supply chain management Risk management Supply network selection

## a b s t r a c t

In the market for tangible goods, there is an increasing shift from the production of single individual products towards individualized mass customization. In contrast to this, so-called hybrid value bundles are getting more and more importance in achieving market share and in allowing for differentiation from competitors. Hybrid value bundles are integrated solutions combined of tangible and intangible goods. For these complex solutions, subparts are delivered from different suppliers and are bundled by a focal supplier. These bundles are delivered as a single solution to the customer. Heterogeneous suppliers within the supplier network require a complex supplier relationship management. Classic supply chain management techniques fail because of the speci<sup>fi</sup>c requirements of hybrid value bundles, e.g. strong customer integration, different product lifecycles of the individual components or incompatible product speci<sup>fi</sup>cation. One key issue in supplier management is risk management. For this, the focal supplier has to evaluate its suppliers according to risk characteristics and then choose to take those that implicate the lowest risk. In hybrid value creation, one serious problem is the availability of guaranteed information. Especially for service components, relevant information is not available, not assured, or the supplier does not want to provide them. Therefore, a risk management model for hybrid value creation has to deal with incomplete, varying information. In this article, a risk management model is presented, which takes care of the speci<sup>fi</sup>c requirements of hybrid value bundles in complex supply networks. This risk management model serves as a risk assessment framework for a focal supplier to identify supply chains with the lowest risk for a speci<sup>fi</sup>c offering.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Gaining sustainable competitive advantage towards competitors is a challenging task for every company. One possible answer to this challenge is the offering of innovative, customer-focused products. Central to this strategy is the development and offering of so-called hybrid value bundles or product-service systems. Hybrid value bundles are a speci<sup>fi</sup>c kind of product bundle, which consist of synchronized, highlyintegrated products and services with the goal to solve a speci<sup>fi</sup>c customer problem [27]. This tight integration increases the customer value of hybrid value bundles which exceed the sum of the values of the individual sub-services [30]. With these integrated solutions in their product portfolio, companies are able to distinguish from their market competitors to generate higher margins and promote the development of long-term, strong customer loyalty [12]. In addition, product ef<sup>fi</sup>ciency can be increased by the individual adaptation to customer needs [4] and higher added-value is generated for both the producer and the customer [19].

Current research results show that the management of value bundles leads established commercial processes to new challenges in information systems. Thus, value bundles cannot be managed suf<sup>fi</sup>ciently in commercial processes like supply chain management for example. The research in the range of the hybrid added value concentrates upon models and methods of the construction of such solutions. From a procurement perspective, we note <sup>fi</sup>rst results in a reference model for the strategic procurement process of value bundles in supply networks [46]. The discussion about more speci<sup>fi</sup>c aspects of value bundles in value networks like risk management is still incomplete.

The development and provisioning of a hybrid value bundle do not usually only involve a single company, but often an entire network of independent companies that make a contribution to the hybrid value bundle. Reiss and Präuer showed in an empirical study that the most appropriate structure for the development and provisioning of value bundles is strategic value-added partnerships, networks and crosscompany project-oriented cooperations [40].

Regardless of the origin of the network, usually a large number of suppliers and subcontractors are involved. Each of these participants engenders a risk to the network, and it changes the risk assessment of individual supply chains. The larger and more branched the network is, the more complex the associated risk is. Classical risk management methods for supply chains are not suitable for the speci<sup>fi</sup>c requirements of value bundles [44]. But in industrial practice, the need exists for risk management adapted to the speci<sup>fi</sup>c characteristics of hybrid value creation. This article closes this gap in research and industrial practice by proposing a risk management model suitable for hybrid value creation. The proposed model is developed in three steps. First based on a literature study, we identify speci<sup>fi</sup>c requirements for hybrid value creation, which may be regarded for risk management. Second we make use of a scoring model as the foundation for the new model, since a scoring model might be the one of the best approximations for risk management in hybrid value creation [44]. In a third step we formulate the basic concepts of the model and the model itself in a formalized way.

The article has several objectives: In the <sup>fi</sup>rst part (Sections 2 and 3), we give an introduction to the current state of research of risk management for hybrid value creation, and we describe our research approach. This work makes use of a design science approach with the main goal of the construction of a risk management model. The second part (Section 4) describes the construction of the risk management model. The model consists of several de<sup>fi</sup>nitions for key concepts and the main de<sup>fi</sup>nition of the risk management model. The third part (Section 5) covers the evaluation of the proposed model. This evaluation consists of two parts: <sup>fi</sup>rst a formal evaluation to prove the validity and the consistency of the model. Second, a simulation is conducted by using a software artifact to study the behavior of the model in certain settings. The fourth part (Section 6) discusses the results from the evaluation. In this discussion, two main aspects are identi<sup>fi</sup>ed: calculation costs and risk control. The <sup>fi</sup>nal section concludes with a summary of the work and an outlook for further investigations on the topic of risk management for hybrid value bundles.

## 2. Research background

## 2.1. Hybrid value creation

With the decline in economic importance of pure products and services because of lacking differentiation, combinations of physical products and services being offered as bundles have become more and more in<sup>fl</sup>uential in the industry. These combinations are called value bundles and are a combination of physical products and services as well as additional intangible values like warranty extensions for example. These combinations are specially tailored to solve an individual customer problem [24,47]. Value bundles can be subdivided in standardized physical products and standardized services as well as customized products and customized services (see Fig. 1). The division into these four elements is not dichotomous, but the transitions between these elements are linear in the sense that there are several possibilities to combine these elements into a value bundle.

The main goal in the offering of value bundles is solving a customer problem [9,41]. Examples for service components which may be bundled with physical products are extended service level agreements, availability guarantees, the output of a machine, performance/full service contracts, performance guarantees, <sup>fi</sup>nancial offerings, consulting, licenses or rights include. However, services, rights, or service level agreements may be involved in a hybrid value bundle.

![](/api/attachments/A5KT6TXK/fulltext/images/cb50ba93ef6194a26cefd52ca3f52408a9c7ba05331524b41cec5215acc5f5b0.jpg)  
Fig. 1. Component types of hybrid value bundles.

Integration is a key concept in developing and providing value bundles. This integration means not only the bundling of products and services for the purpose of a combined solution, but also process integration on customer and supplier side [29]. The degree of integration between different services is variable [17] and has a direct impact on the services. On the one hand, there are standardized physical products combined with services directly related to the physical product (e.g. a mobile phone with a price plan). On the other hand, there is the business case of performance contracting where the offer of a value bundle consists of several service agreements, to the customer with no tangible asset at all (e.g. the guaranteed output of a laser printer, counted in printing pages per day) [13]. With a high level of integration between the two units, the provision of the service component is strongly dependent on the tangible good component. These highly integrated value bundles are often offered to customers as service agreements and from a customer perspective it is not possible to separate the tangible goods from the services (see Fig. 2).

The customer orientated creation of value bundles offers companies the possibility of diversi<sup>fi</sup>cation and leads them to signi<sup>fi</sup>cant market advantages. But it also presents new challenges for the subprocesses along the value chain. A key design feature of a hybrid value-added process is the foundation of network structures. Reiss and Präuer [40] showed in an empirical study that cooperative organizational forms, such as strategic value-added partnerships, networks and cross-company projectorientated cooperations are the most appropriate organization forms to provide value bundles. Because of the high dynamic customer orientated variations of value bundles, they cannot be produced as bulk goods, so the network must be created by the offering company at the beginning of the manufacturing process. This also means that a valueadded network might not be used for another value bundle. The cooperating companies have to join forces in dynamic networks that can be con<sup>fi</sup>gured according to requirements of a speci<sup>fi</sup>c value bundle at its added-value processes (see Fig. 3).

Hybrid value bundles require a speci<sup>fi</sup>c supply chain management adapted to the characteristics of hybrid value creation [7]. There is a need to adapt existing management methods, which are primarily focused on the supply chain management for tangible goods to ful<sup>fi</sup>ll the speci<sup>fi</sup>c requirements of hybrid value creation. Recent research on this issue has shown that hybrid value bundles create new issues in procurement environments like SCOR [5] or cloud computing [6].

## 2.2. Risk management for suppliers

For the de<sup>fi</sup>nition of risk, several de<sup>fi</sup>nitions appear in the literature. In general, risk can be considered as the possibility for danger, damage, loss, injury or other unwanted effects [23]. Following Warner, risk can be regarded as a possibility for a certain unfavorable incident during a given time period or as a result of a particular challenge [52]. A more formal de<sup>fi</sup>nition of risk can be obtained by Mitchell. He de<sup>fi</sup>nes risk as a combination of the probability of loss $P ( l o s s _ { n } )$ and the impact of the loss $I ( l o s s _ { n } )$ for the organization, whereas n denotes the number of different risks, losses or impacts [36]. This means that risk in general can be decomposed into several partial risks. Every partial risk is related to its own loss and its own impact. These partial risks may be combined to a global risk by applying formal probability theory [23].

In industrial practice, risk management of suppliers and supply chains has a long tradition and several established methods. Risk of a supply chain may be de<sup>fi</sup>ned as “...any threat of an event that might disrupt normal <sup>fl</sup>ows of materials or stop things happening as planned.” [2]. In the building industry, for example, the risk of a supply chain may be described as “...uncertainty as to the <sup>fi</sup>nal cost, duration and quality of the project.” [2]. In this research, we de<sup>fi</sup>ne the risk for a supply chain as the probability, that some delivery provisions might not be provisioned as expected. Reasons for this might be found in exogenous factors like a lightning strike or an illness or in endogenous factors like machine disruption or construction failures [22]. Through the increasing complexity of hybrid value bundles as well as the outsourcing of suppliers, the place of risk changes and the risk itself is increasing. There are several scienti<sup>fi</sup>c discussions on the topic of risk in procurement and delivery, but only a few discussions on risk management in complex supply networks [23].

H. Schrödl, K. Turowski / Decision Support Systems xxx (2013) xxx–xxx  
![](/api/attachments/A5KT6TXK/fulltext/images/66230e67a71ff787c1188fcf5fdf244d41cfc7dbecada4d5f6dd8df2afa05f34.jpg)  
Fig. 2. Integration ratio of hybrid value bundles.

There is a set of established methods for supplier selection like lexicographic rules [57], cluster analysis [28], data envelopment analysis (DEA) [33] or min–max methods [49]. To ensure quality standards in the supplier rating as the foundation for supplier selection, a reliable method is necessary to remove those suppliers who are not able to meet a certain threshold in the selection criteria [1]. Clearly dominant in the literature is the method of scoring [8]. For the special case of hybrid value bundles, a method based on an extended scoring method is proposed [45].

Essential for the appropriate method for supplier risk management is the de<sup>fi</sup>nition of the appropriate criteria catalog. Central concept of these criteria catalogs is to address multiple criteria which can be considered simultaneous. A broad scienti<sup>fi</sup>c basis is established on the development of criteria catalogs since the early 1960s [1]. In 1966, Dickson has proposed 23 criteria which are relevant for supplier selection [15]. In particular, prize, delivery and quality metrics are outstanding in these criteria listing. Moreover, criteria like production capacity, previous outcomes, guarantees, geographical region and technical expertise are criteria often mentioned in the existing literature [53,54]. Since the selection of criteria covers different activities like inventory management, production planning or total quality management, it is necessary that every organizational unit, that is involved in the risk management process is able to make the right decision. Therefore, the selected criteria have to meet different targets and have to represent different organizational units of a company [1]. Decision catalogs with different criteria may lead to con<sup>fl</sup>ict of objectives [20]. An example for this may be searching for the lowest price and simultaneously the highest quality.

Assessing risk through a criteria catalog highly depends on the procurement situation. With the work of Aissaoui et al. as a foundation, several speci<sup>fi</sup>c criteria catalogs for speci<sup>fi</sup>c procurement situations have been developed. An example for such a speci<sup>fi</sup>c criteria catalog can be found for the procurement in the just-in-time production environment [54]. This emphasizes the need to adapt the criteria catalog carefully to the related procurement situation to ensure the assessment of the relevant risks.

## 2.3. Risk management in supply networks for hybrid value creation

The need for risk management in supply chains with a large number of participants is highly accepted [10]. For the concept of risk in supply chain management, there are several de<sup>fi</sup>nitions [34,48]. For the following we adopt the de<sup>fi</sup>nition of risk as “risk of loss or damage [which] by the failure of services that can be attributed to not be in<sup>fl</sup>uenced or anticipated events [arises]” [21]. Risk can be seen as the probability that a particular adverse event occurs during a speci<sup>fi</sup>ed time or results from a matter of special importance.

In the case of supply networks, this includes a nonlimited amount of risk factors related to the supplying company. To assess this variety of criteria systematically, it requires an appropriate procedure. For the purpose of evaluating suppliers and supply chains, several criteria have to be identi<sup>fi</sup>ed which operationalize relevant risk elements and make a clearly de<sup>fi</sup>ned risk calculation procedure possible. The challenge of hybrid value bundles encompasses the identi<sup>fi</sup>cation of relevant risk elements and their speci<sup>fi</sup>c operationalization. In the business case of classic products or isolated services, the risk elements are clearly de-<sup>fi</sup>ned and split into both qualitative and quantitative factors [31,50,51]. In hybrid value creation, the characteristics of the hybrid value bundle are of central importance for identifying risk factors. Therefore, it is

![](/api/attachments/A5KT6TXK/fulltext/images/b711dce18a371de76aef06eea6b9bf28eb4097521877b576aa7b93deaedf8c40.jpg)  
Fig. 3. Recon<sup>fi</sup>guration of supply network for changing hybrid value bundles.

Please cite this article as: H. Schrödl, K. Turowski, Risk management in hybrid value creation, Decision Support Systems (2013), http:// dx.doi.org/10.1016/j.dss.2012.12.042

necessary to transfer the speci<sup>fi</sup>c characteristics of hybrid value bundles in risk factors and use them as the basis for a risk model calculation.

The classi<sup>fi</sup>cation of the outcome of hybrid value bundles is just the <sup>fi</sup>rst approach. The outcomes can be divided into three different classes of service provisioning: functional orientation (the supplier guarantees a speci<sup>fi</sup>c functionality), use orientation (the provider takes over any speci<sup>fi</sup>c availability and integrates customer process guarantees in the performance offered) and results (the provider guarantees a certain production results while taking over other risks, such as operating risks) [11]. Moreover, Burianek [11] identi<sup>fi</sup>ed seven criteria which are characteristic of hybrid value bundles and have an essential effect on the complexity of value provision: type of customer bene<sup>fi</sup>t, scope of services, amount and heterogeneity of partial services, degree of technical integration, degree of integration into the value chain of the customer, degree of individualization and temporal dynamics and variability of value provision. Which criteria in detail are the best to serve as a base for the calculation of risk is an individual decision of the focal supplier and cannot be de<sup>fi</sup>ned per se. Examples of such decision criteria can be found in Heyder et al. [26]. Coupled with possible effects [37], which can help to assess the criteria change with respect to individual suppliers, one can get a practical insight. Especially for hybrid value bundles, Pousttchi et al. gave another example for speci<sup>fi</sup>c characteristics [39]. This is a classi<sup>fi</sup>cation of features for hybrid value bundles, which distinguishes the corresponding characteristics in three groups of features: strategic classi<sup>fi</sup>cation, component composition and value creation. Deciding, which of these criteria are more or less relevant for the inclusion in a risk calculation model highly depends on the hybrid value bundle and the sourcing situation of the focal supplier. At this time there is no work known which allows a guaranteed listing of criteria for supplier selection in hybrid value creation. Therefore, the risk calculation model must be able to handle all known characteristics of hybrid value bundles to open the possibility for integration in a calculation scheme.

One additional key aspect in the scenario of hybrid value bundles is that information is not available in every case. Especially for servicebased components of the hybrid value bundle, the suppliers are often not able or not willing to provide certain information to the customer. Reasons for this might be the lack of knowledge to provide the relevant information, competition aspects or just the nonexistence of the required information. Therefore, an appropriate method for risk management for hybrid value bundles has to deal with the possibility of incomplete information. The incompleteness of information must not lead to inaccuracy in the calculation results or the unexpected termination of the calculation.

## 3. Research design

The main objective of this research is to develop a risk management model for the selection of a risk-optimized supply chain for hybrid value creation. The research uses a design science approach. Design science is a research method to solve organizational problems by creating and evaluating IT artifacts [25]. These IT artifacts are de<sup>fi</sup>ned as constructs, models, methods, or instantiations [35]. To ensure a rigorous execution of the research, a clear research methodology is required. March and Smith proposed a design science research methodology that consists of four steps: build, evaluate, theorize and justify [35]. They considered build and evaluate as the main research activities in design science. Build activities should demonstrate that a particular artifact can be constructed. Evaluate activities should develop criteria to measure the behavior of the artifact and assess the performance of the artifact against these criteria. Taking this as basis for a design science research methodology, several extensions of this methodology have been proposed to increase the applicability of the research method. One of these adapted design science research methodologies is developed by Peffers et al. (see for example [32,38]). The design science process according to Peffers et al. includes six steps: problem identi<sup>fi</sup>cation and motivation, de<sup>fi</sup>nition of the objectives for a solution, design and development, demonstration, evaluation, and communication [38]. Vaishnavi and Kuechler proposed a design science research methodology consisting of <sup>fi</sup>ve main process steps: awareness of the problem, suggestion, development, evaluation and conclusion [32]. For the present research, we have adapted the design science research methodology from Vaishnavi and Kuechler. Based on their <sup>fi</sup>vesteps-approach, we included additional aspects from March and Smith (whose focus is on build and evaluate) and Peffers et al. (who claimed demonstration as additional process element along with the evaluation) as displayed in Fig. 4.

The <sup>fi</sup>rst process step, awareness of the problem, has been addressed in the introduction. The problem relevance leads to the main research question: How to identify a supply chain with the lowest risk in a supply network in the context of hybrid value creation? In the second process step, we recommend the adaption of a scoring model for a multi-criteria comparison to the speci<sup>fi</sup>c needs of supply chain selection in hybrid value creation. In research step 3, development, we construct a new scoring model for the calculation of risk for a supply chain in hybrid value creation. For the evaluation of the proposed risk management method, we follow the guidelines for design science research according to Hevner et al. [25], where <sup>fi</sup>ve classes of methods for design artifact evaluation are provided. In this research, we <sup>fi</sup>rst conduct a sensitivity analysis of the scoring model to ensure proper stability of the risk calculation. Second, we developed a software prototype for simulating supply network establishment and supply chain selection by using the proposed risk scoring method. With this prototype, we conduct a simulation of different typical scenarios from practice. This evaluation is for testing of the feasibility of the scoring model for a practical implementation and the effectiveness of the usage of the method. In the conclusion section, we re<sup>fl</sup>ect on the proposed method and discuss re<sup>fi</sup>nements of the method for further application.

## 4. Construction of the risk management model

The construction of the model has two presumptions:

• for the start, all relevant supply chains in the supply network are identi<sup>fi</sup>ed

• the sequence of the suppliers in the single supply chain will not be considered.

## 4.1. Preparations

For the construction of the risk management model, we assume the following situation: The focal supplier has offered a solution to a single customer. The solution is an integrated solution of tangible and intangible goods and services which are customized to the speci<sup>fi</sup>c needs of the customer. The customer agreed to the solution. The focal supplier does not produce all of the solution components himself. Therefore, he has to purchase the missing components from his suppliers in his supply network. For the procurement of these components, the focal supplier wants to minimize the risk in selecting the wrong suppliers which may lead to problems in the integration process of the single components to the customer solution.

The foundation of the proposed model is a method for risk assessment for suppliers in supply networks for hybrid value creation, developed by Schrödl et al. [45]. This method consists of three steps: <sup>fi</sup>rst, the focal supplier provides a decision catalog consisting of decision relevant criteria which are valid for every supplier in the supply network. Each criterium is related to a weighting factor which re<sup>fl</sup>ects the relative relevance of the criterium for the decision. Second, the suppliers provide their information on the criteria of the decision catalog to the focal supplier. In the third step, a conversion is done on the retrieved information by the focal supplier. Information, that does not correspond to a numeric value has to be transformed into a numeric value. Furthermore, the focal supplier assumes incompleteness of information from the suppliers. To face this issue, the focal supplier determines a lower boundary for the amount of information which the suppliers have to provide. Otherwise, they will not be considered for the supply chain.

![](/api/attachments/A5KT6TXK/fulltext/images/fead95625ab52db7f54fd41c151afdbe66187e6cc9aa109a58b4daa38da6bca3.jpg)  
Fig. 4. Research design.

The method proposed in [45] is formulated in a mathematical model which shows the applicability of the method. For further investigation on the model, we propose a novel formulation in the following section.

## 4.2. Basic notations

Before we formulate the new risk management model, some basic notations will be introduced.

De<sup>fi</sup>nition 1. Assume that the decision catalog provided by the focal supplier is represented by n criteria $k _ { 1 } , . . . , k _ { n } , k _ { i } \in \mathbb { N }$ i. To each criterium $k _ { i } , i { = } 1 , { \ldots } ,$ n a weighting factor g , $i = 1 , . . . , n , g _ { i } { \in } [ 0 , 1 ]$ ] is related. We denote $k \colon = \langle k _ { 1 } , . . . , k _ { n } \rangle$ the criteria vector, $g \colon = \langle g _ { 1 } , \ldots , g _ { n } \rangle$ the weight vector and $\tilde { k } : = \langle k _ { 1 } * g _ { 1 } , . . . , k _ { n } * g _ { n } \rangle$ the weighted criteria vector.

The criteria vector k is now used for gathering the supplier information from the supply network. For this purpose, every supplier is asked to respond to the criteria in the criteria vector according to a given response framework. This response framework provides prede<sup>fi</sup>ned values for suppliers to respond to the decision criteria. For every criterium there is a set of prede<sup>fi</sup>ned values which are to be used by the suppliers. These prede<sup>fi</sup>ned values must not be of a numerical type, giving the possibility to re<sup>fl</sup>ect speci<sup>fi</sup>c issues from hybrid value creation in the values. To make these prede<sup>fi</sup>ned values usable for the risk calculation, these values have to be transformed into numerical values. This will be done by assigning a numerical value to every element of the prede<sup>fi</sup>ned answer for calculation. The assignment is speci<sup>fi</sup>c for every value and has to be formulated by the focal supplier.

De<sup>fi</sup>nition 2. Assume the given criteria vector k. Let $P { = } \{ P _ { 1 } , { \ldots } , P _ { n } \}$ be the given response framework with P as the possible answers to the criterium k and $V = \{ V _ { 1 } , . . . , V _ { n } \}$ be the transformation of the response framework P with V as the value transformation for $P _ { i } \forall i = 1 , . . . , n$ . We denote $s _ { j } : = \langle s _ { j _ { 1 } } , . . . , s _ { j _ { n } } \rangle$ as the answer from supplier j with $j = 1 , . . . , m$ m as the number of suppliers in the supply network. Furthermore, we denote $\tilde { s } _ { j _ { 1 } } : = \langle \tilde { s } _ { j _ { 1 } } , . . . , \tilde { s } _ { j _ { 1 } } \rangle$ as the weighted answer with

$$
\tilde {s} _ {j _ {n}} := \left\{ \begin{array}{l l} v _ {n, i n d e x (s _ {j _ {n}}, P _ {n})} & \text { for } s _ {j _ {n}} \neq 0 \\ - 1 & \text { else } \end{array} \right.\tag{1}
$$

with sitio $\begin{array} { r } { { \nu } _ { n , i n d e x } ( \mathfrak { s } _ { j _ { n } } , P _ { n } ) } \\ { \mathfrak { l a s } { \mathfrak { s } } _ { j _ { n } } \mathrm { i n } { \cal P } _ { n } . } \end{array}$ as the element of $V _ { i } ,$ which is on the same array po-

For the current model we assume that there exists a mapping from $P _ { i }$ to $V _ { i }$ ∀i in such a way that every element of $V _ { i } { \in } [ 0 , 1 ]$ ] and there is an inherent metric in the way that the natural order given in $V _ { i }$ re<sup>fl</sup>ects the preferences of the focal supplier. This means, that values near 0 are of low preference and values near 1 are of high preference.

## 4.3. Model definition

De<sup>fi</sup>nition 3. Assume g as given weight vector. We de<sup>fi</sup>ne RB as the relevance boundary for the supplier answer with $0 \leq R B \leq | | g | |$

The relevance boundary is the lower threshold for the supplier's answer. The focal supplier uses this boundary to exclude suppliers who do not provide enough information to calculate the risk reliably. Suppliers who provide information with less value than the relevance boundary will not be taken into account for the supply chain. The determination of the relevance boundary depends on the risk concept of the focal supplier. Setting the relevance boundary too low may include high-risk suppliers in the supply chain; setting the relevance boundary to high will reduce the number of potential supply chains. In an extreme case, there will be no supply chain left for selection. Finding the optimal relevance boundary for a given risk concept is part of the future work on the topic of risk management for hybrid value creation.

De<sup>fi</sup>nition 4. Assume the given weight vector g. Let $s _ { i }$ be the answer from supplier i, $i { = } 1 , { \ldots } , m$ , m as the number of suppliers in the supply network. Supplier s<sub>i</sub> is called a relevant supplier, if s<sub>i</sub> is able to ful<sup>fi</sup>ll the demand and ‖s ⊗g‖≥RB, RB is relevance boundary, with

$$
(s _ {i} \otimes g) _ {j} := \left\{ \begin{array}{l l} g _ {j} & \text { for } s _ {i _ {j}} \neq 0 \\ 0 & \text { else } \end{array} \right..\tag{2}
$$

De<sup>fi</sup>nition 5. We de<sup>fi</sup>ne the risk of a single supply chain $R _ { \varOmega _ { j } }$ with

$$
R _ {\Omega_ {j}} := \frac {\sum_ {s _ {j} \in \Omega_ {j}} \left\langle g , s _ {j} \right\rangle}{\sum_ {s _ {j} \in \Omega_ {j}} \left\langle g , \tilde {s} _ {j} \right\rangle}.\tag{3}
$$

The values of $R _ { \varOmega _ { i } }$ ranges in the interval [0,1], where 1 is the best value and indicates the supply chain with the lowest risk. This can be seen by the fact that the numerator contains maybe empty answers from the supplier (which means several entries with 0). These empty answers will be corrected in the denominator. Therefore, the denominator is always greater or equal as the numerator.

De<sup>fi</sup>nition 6. Given a set of supply chains Ω with their corresponding calculated risk $R _ { \varOmega _ { j } }$ for every supply chain $\Omega _ { j } ,$ , the best supply chain in the set of given supply chains is $\bar { \Omega } _ { m a x } : = m \bar { a } x \Big \{ R _ { \Omega _ { j } } \Big \}$

## 5. Model evaluation

The evaluation of the proposed risk management model consists of three building blocks. The <sup>fi</sup>rst building block describes a sensitivity analysis of the model. This analysis is enhanced with some re<sup>fl</sup>ections on the feasibility of the model. These re<sup>fl</sup>ections reinforce the theoretical foundation of the proposed model and serve as analytical design evaluation for a statistic analysis. Second, a software prototype was developed to demonstrate the potential instantiation of the risk management model. A <sup>fi</sup>rst implementation of the prototype has already been shown in Schrödl et al. [45]. Therefore, we do not extend this building block in this regard. The prototype was slightly adapted for the simulation in the third building block of the evaluation. The adaption stems from the advanced data management used for the simulation. To demonstrate the practical implications, we present a simulation in the third building block. A simulation may be used in design science to evaluate new artifacts [25]. It is an experimental design evaluation method where the artifact is executed with arti<sup>fi</sup>cial data.

## 5.1. Sensitivity analysis and analytical evaluation

The <sup>fi</sup>rst question towards the proposed model is the question of how reasonable the results are. Since the proposed risk management model is a linear model, a sensitivity analysis might be used to answer this question [14]. The set of supply chains Ω is given a ranking through the risk calculation. Therefore, the sensitivity analysis will be split in two parts: <sup>fi</sup>rst, how sensitive is the calculation of the risk for a single supply chain $\Omega _ { j }$ and second, how sensitive is the resulting order in the set of supply chains Ω.

Theorem 1. Assume a given supply chain $\Omega _ { j }$ and the associated risk $R _ { \varOmega _ { j } } .$ The risk $R _ { \varOmega _ { i } }$ is stable under variations of s . This means that the changes in the calculated risk are directly associated with the changes in the suppli er answers $s _ { j } .$

Proof. To prove Theorem 1 we have to consider two different cases.

Case 1. $S _ { j } / \tilde { S } _ { j } \mathrm { ~ W i t h ~ } \tilde { S } _ { j } { \geq } S _ { j }$ . Since the risk management model 3 is a linear model, it follows immediately, that $R _ { ☉ _ { i } \ge R _ { \varOmega _ { i } } }$ , whereas $R _ { ☉ _ { j } }$ denotes the supply chain with the changed supplier answer $\tilde { s } _ { j }$ .

Case 2. $s _ { j } { \setminus } \tilde { s } _ { j }$ with $\tilde { s } _ { j } { \le } s _ { j }$ . This case may be transferred to Case 1 with the same argument of the linearity of the risk management model. Therefore, $R _ { \tilde { \Omega } _ { i } } { \leq } R _ { \Omega _ { j } }$ , whereas $R _ { \tilde { \Omega } _ { i } }$ denotes the supply chain with the changed supplier answer ${ \bf \tilde { \Gamma } } _ { S _ { j } . }$

Every other change in the supplier answers, e.g. one answer increases and another answer decreases, may be reduced to the two discussed cases by splitting the whole change to a sequence of singular changes. This can be done due to the linearity of the risk management model. □

So far we have shown, that the proposed risk management model acts stable with regard to the risk calculation of a single supply chain. The calculation of risk for every suitable supply chain in the whole supply network leads to a set of risk calculations with a natural given order (risk calculation operates on $\mathbb { R } ^ { + }$ and therefore follows the order of ℝ<sup>+</sup>). The question now arises, if how stable is the calculated order under variations. Variations in the order may occur through two different variations: <sup>fi</sup>rst, variations of the supplier answers and second, variation of the relevance boundary RB.

Theorem 2. Assume a given set of supply chains Ω with their corresponding calculated risk $R _ { \varOmega _ { i } }$ for every supply chain $\Omega _ { j } .$ The order of Ω is stable under variations of $\dot { s } _ { j } .$ This means, that the order in the calculated risk changes in the same way as changes occur in the supplier answers s<sub>j</sub>.

Proof. Following Theorem 1 it is suf<sup>fi</sup>cient to consider the change of one single supplier answer in one direction. Let $s _ { j } \tilde { \gamma } _ { j }$ wit $\begin{array} { r } { \phantom { } _ { 1 } \tilde { s } _ { j } \{ 2 s _ { j } . } \end{array}$ . Following Theorem $1 , R _ { \tilde { \Omega } _ { i } } { \geq } R _ { \Omega _ { j } }$ , whereas $R _ { \tilde { \Omega } _ { i } }$ denotes the supply chain with the <sup>j</sup>changed supplier answer $\tilde { s } _ { j } .$ <sup>j</sup>. The question is whether this change in $R _ { \tilde { \Omega } _ { i } }$ that leads to a change in the order of Ω lies in the distance between $R _ { \varOmega _ { j - } }$ and $R _ { \tilde { \Omega } _ { i } }$ . If this distance is larger than the change in $R _ { \tilde { \Omega } _ { i } }$ , no change of the order will occur. If the distance is smaller than the change in $R _ { \tilde { \Omega } _ { i } }$ , then the order will change in a way that $\Omega _ { j }$ will surpass $\Omega _ { j - 1 } .$ Generally speaking the order rank of $\Omega _ { j }$ increases, which is in accordance to the increase of ${ \bf \dot { \boldsymbol { s } } } _ { j } .$ In summary, the order may change when a change occurs in the supplier answers, but when the order changes, the change is in the same direction as the change in the supplier answer. □

Theorem 3. Assume a given set of supply chains Ω with their corresponding calculated risk $R _ { \varOmega _ { j } }$ for every supply chain $\Omega _ { j } .$ Let RB be the relevance boundary for the supply network. The order of Ω is stable against variations in RB.

Proof. For the proof of the theorem, let's assume <sup>fi</sup>rst RB is increased to <sup>˜</sup>RB with RB<sup>˜</sup> ≥RB. Increasing RB means, that the amount of information suppliers has to provide will increase. According to this, some of

Please cite this article as: H. Schrödl, K. Turowski, Risk management in hybrid value creation, Decision Support Systems (2013), http:// dx.doi.org/10.1016/j.dss.2012.12.042

the members of Ω will no longer be a valid supply chain, since they do not provide enough information to be regarded as relevant. Therefore, these supply chains will be excluded from Ω<sup>˜</sup> , whereas Ω<sup>˜</sup> is the new set of relevant supply chains. The elimination of the irrelevant supply chains from Ω will not re-order the remaining set of supply chains Ω<sup>˜</sup> , therefore, the order of Ω and Ω<sup>˜</sup> is equivalent.

Second, let's assume RB is decreased to <sup>^</sup>RB with <sup>^</sup>RB≤RB. This means, that suppliers are asked to give less information than before to become a valid member of the supply chains Ω. This will lead to the identi<sup>fi</sup>cation of new supply chains, which are not yet member of Ω. We denote the new set of valid supply chains with Ω<sup>^</sup> with Ω Ω<sup>^</sup> . The new members of the set of relevant supply chains will be sorted in the existing order of Ω. They might be sorted at the end of the order, but they might also be sorted in between the existing order. But this insertion will not rearrange the former sorting of Ω. Therefore, the sorting of Ω and Ω<sup>^</sup> will remain equivalent for those elements being in both sets.

In summary, the order of the valid supply chains Ω is stable against variation of the relevance boundary RB. □

## 5.2. Model simulation

After this theoretical analysis has shown the appropriate functionality of the proposed model, we provide additional insight through a model simulation using the implemented prototype from Schrödl et al. [45]. This prototype has been slightly extended for automation of data input, the main functionality remained unchanged. We conducted several prede<sup>fi</sup>ned, typical scenarios and random scenarios with different supply network sizes. To gain further insights into the picture of a practical implementation, we decided to create simulations with different sizes. The prede<sup>fi</sup>ned scenarios are modeled according to existing hybrid value bundles in the market in combination with an assumed supplier network. As an example for the existing hybrid value bundle, we have taken an example from the IT industry. The example is a real case from a company providing ICT solutions and is typical for procurement problems with complex product-service bundles in value networks. Elements of this case have been discussed with experts from the providing company in the areas of product management, marketing, IT operations and senior management. The considered hybrid value bundle is the offer from a provider of information technology. This package is an enterprise IT workplace, which can be used as a standard workstation for genera of<sup>fi</sup>ce activities. The scope of this IT workplace includes hardware (PC, keyboard, mouse), various software packages and internet connection. Furthermore, a customer relationship management system (CRM) with connection to an online marketplace for the purchasing of of<sup>fi</sup>ce supplies is integrated. To ensure proper backup, an online-backup solution is added. In addition, the offer includes the workplace installation and the training of the employee as a service. Finally, there is a service level agreement (SLA). This allows the user with problems either to call a hotline or to request an on-site service. This example is already part of a preliminary work in Bensch et al. [6]. The con<sup>fi</sup>guration of the supplier network and risk model was based on practical experiences. The hybrid value bundles in these scenarios consist in average of <sup>fi</sup>ve modules, the size of the supply networks consists in average of 15 different suppliers. Findings in this part of the simulation should provide insights in the behavior of the model in a real practical setting.

The second part of the simulation was based on a randomized con-<sup>fi</sup>guration of all system components of the model. This part of the simulation should provide insights into new aspects that have yet to be practically experienced. These aspects might be related to certain unlikely situations. Therefore, the supply networks, the segmentation of the hybrid value bundle, and the corresponding suppliers have been calculated randomly. The algorithm of the random number calculation was based on the algorithm of Wichman and Hill [55]. The random scenarios were built on a network node base on 10, 100 and 1000 suppliers in the supply network. Network sizes have been aligned according to several documented real cases in the industry (see for example [3,18,56]).

The hybrid value bundles in these scenarios consist on average of 20 modules. The upper boundary for the 10-node scenario was 5 modules, 30 modules for the 100-node scenario and 400 modules for the 1000-node scenario. In all three scenarios, we did 50 instances of each experiment to achieve an average value. As the average value, the arithmetic average for all instances was calculated. The simulations have been conducted to gain insights into computation times and potential applications of the model for a practical implementation. Furthermore, we expected to gain some insights on problems occurring through the network complexity.

At <sup>fi</sup>rst, we took a look at the computation time. Due to the lack of alternative models, it was not possible to compare the computation time of the proposed model to other existing models. Therefore, this section gives <sup>fi</sup>rst insights on the expected runtime behavior of the risk management model. For the calculation of the ranking of all relevant supply chains, we have implemented three steps: in the <sup>fi</sup>rst step, we identify a relevant subgraph in the whole supply network according to the demand of the focal suppliers. The subgraph consists of those suppliers who are able to provide at least one module of the hybrid value bundles. To obtain this subgraph, we have to traverse the whole supply network. Secondly, in this subgraph relevant supply chains will be identi<sup>fi</sup>ed. To ful<sup>fi</sup>ll a speci<sup>fi</sup>c demand, it is possible that several supply chains of different suppliers exist. In this stage, we take the relevance boundary into account to remove suppliers who did not provide enough information. To achieve this, the whole subgraph has to be traversed again. Third, the risk management model is applied to the set of identi<sup>fi</sup>ed supply chains. This calculation is again done on the whole subgraph. In summary, when we denote n as the number of nodes in the whole supply network and m as the number of nodes in the relevant subgraph, we have to execute n+2×m calculations. In the investigated scenarios with a maximum of 1000 nodes, computation time could be regarded as a nonlimiting factor. All calculations in the investigated experiment have been done under 1 s computation time.

Second, we consider the practical side of the implementation. This means in particular: how well does the risk management models identify relevant suppliers and calculate their ranking. As we have seen from the theoretical discussion, this selection process depends in particular on the con<sup>fi</sup>guration of the relevance boundary RB. We have conducted the experiments with several different relevance boundaries to identify the most suitable for the results. The right selection of the relevance boundary is a challenging task and may be part of future work on this topic. For all experiments, the relevance boundary RB has been <sup>fi</sup>xed. To display the practical application of the risk management model, we calculated the number of identi<sup>fi</sup>ed suppliers n, the number of identi<sup>fi</sup>ed members of the relevant subgraph m and the number of identi<sup>fi</sup>ed supply chains sc. In addition, we provide the calculation time ct for the speci<sup>fi</sup>c scenario. For an overview of the results – both the computation time and the practical application – see Fig. 5.

The table below Fig. 5 contains the average results from the simulation the particular scenario. Regarding the third part of the experiment – problems through network complexity – we have not encountered any problems in the tested network size. We did some preliminary experiments with 10,000 nodes and 100,000 nodes. We recognized that the computation time increases in the relation to the expected network con-<sup>fi</sup>guration. Therefore, these scenarios are as well solvable with slightly longer computation times. The main problem was the setup of an appropriate network structure with 100,000 nodes with respect to the requirements for hybrid value bundle procurement. These experiments with the larger supply network sets have brought up some interesting questions, which will be discussed in the following section.

## 6. Discussion

The theoretical foundation of the model provides a profound base for the application in a practical scenario.

Please cite this article as: H. Schrödl, K. Turowski, Risk management in hybrid value creation, Decision Support Systems (2013), http:// dx.doi.org/10.1016/j.dss.2012.12.042

H. Schrödl, K. Turowski / Decision Support Systems xxx (2013) xxx–xxx  
![](/api/attachments/A5KT6TXK/fulltext/images/2b7ad0beea1be733ff405005cc304454fe7a14eb36c7e502073c6fc8f0e9569d.jpg)  
Fig. 5. Results of the conducted experiments.

## 6.1. Calculation costs

Our formalized experiments have shown that the proposed risk management model works with reasonable computation time on a network size with a maximum of 1000 nodes. For practical purposes, this seems to be a comprehensive size for most scenarios. The preliminary experiments with up to 100,000 nodes have shown that the computation times rise as expected, but the complexity of the supply network sets up some other limits. The main problem lies in the <sup>fi</sup>rst step of the risk calculation. To identify the relevant supply chains in the supply network, all members of the supply network have to be investigated whether they are able to ful<sup>fi</sup>ll parts of the demand. For this, a comparison has to be done. In our prototype, we are working with the product and service description in text form, and we have to match the descriptions. This is time consuming and not acceptable for larger networks. This observation means that for the extension of the risk management model for larger supply networks beyond 1000 nodes, the focus has to be drawn to an ef<sup>fi</sup>cient matching algorithm and to corresponding descriptions for the products and services.

## 6.2. Risk control

The experiments have shown that the relevance boundary RB is a highly sensitive parameter to control the behavior and the results of the risk management model. On one side, a low relevance boundary gives more suppliers the opportunity to take part in the selection process of the most appropriate supply chain. From the focal company's view, it is easier to identify new suppliers, which gives them new opportunities to improve the procurement process. For the suppliers, a low relevance boundary gives the opportunity to hide relevant information from the other participants of the supply network without losing the chance to take part in the selection process for the most appropriate supply chain. However, a low relevance boundary increases the risk for the focal supplier to select suppliers with “hidden risk” since they do not have to communicate it. On the other side, a high relevance boundary decreases the risk for the focal supplier to select a wrong supply chain. For outstanding suppliers, a high relevance boundary gives them a chance to position themselves very prominently in the supply network to outperform their competitors. But a high relevance boundary limits the possibility for the focal suppliers to identify relevant suppliers. It reduces the possible relevant subgraph up to the extreme of failure in <sup>fi</sup>nding any suitable supply chain (according to the risk calculation, not to the possible ful<sup>fi</sup>llment of the procurement demand). In summary, the experiments have shown that it is a challenging task to <sup>fi</sup>nd an appropriate relevance boundary RB for an ef<sup>fi</sup>cient selection process in the supply network. From an initial standpoint we believe this problem might be formulated as an optimization problem to <sup>fi</sup>nd a minimum relevance boundary for a given supply network. There has not been any further investigation on this, but it should be part of the future work on this topic.

A second observation from the experiment concerns the availability of information in the supply network. The risk management model assumes existing information in the whole supply network from all tiers of the supply network. In practice, this issue is challenging due to security and competitiveness restrictions. The idea of the introduction of the relevance boundary gives companies the opportunity to hide much information. But the information given in the supplier response s is avail able in the supply network. This might be regarded as a limitation for the proposed model, but there are already ideas to solve this issue. The <sup>fi</sup>rst proposal is to establish the information system infrastructure on a purely service-oriented architecture. This kind of architecture is shown to be the most suitable implementation form for establishing information systems support for the supply chain management of hybrid value bundles [43]. Building on this, a service bus might be implemented to ensure proper and secure communication, especially of con<sup>fi</sup>dential data in the supply network [42].

## 7. Conclusion

The objective of this article was the development of a risk management model that is aligned with the speci<sup>fi</sup>c needs of the procurement of hybrid value bundles in a supply network. Based on the evaluation of existing models on their applicability for hybrid value bundles, a new model was proposed. This model is based on a scoring model and introduces the new concept of a relevance boundary to face the problem of incomplete or useless information in the supply network. The proposed model has been thoroughly evaluated through a theoretical proof and a conducted experiment. While the theoretical proof states the reasonability of the model, the experiment gave further insights into the behavior and restrictions of the model.

From the authors' knowledge, there is no other model for risk management adapted to the speci<sup>fi</sup>c needs of the procurement of hybrid value bundles. With the proposed model, we extend the broad and relevant research area of risk management in supply chain management. In practice, we see several applications of the proposed model. In the emerging <sup>fi</sup>eld of hybrid value creation, this model may generally be used to reduce risks for the focal suppliers. By having an appropriate method to estimate risk in the supply chain, the focal supplier might be able to integrate more smaller and specialized suppliers in the supply chain to provide more innovation to the customers. Second, application of the risk management model in supply chain management (SCM) or enterprise resource planning (ERP) solutions may increase the automation of procurement processes by proposing a relevant supply chain to the buyer. The buyer can easily identify the most appropriate supply chain. The procurement system may be transformed to an automated procurement system based on the riskbased selection of the supply chains. Third, we see several applications in the area of e-procurement with the procurement of internetbased services and product-servicebundles. In an e-procurement scenario, the supply chain consists of numerous suppliers, many of them are hard to recognize. The proposed risk management model will increase the ecosphere of supplier relationships with more possibilities to identify relevant suppliers and integrate them seamless into existing supply chains for an innovative product.

Future research on the proposed model is related <sup>fi</sup>rst on the further investigation of the relevance boundary. This relevance boundary has a signi<sup>fi</sup>cant impact on the structure and applicability of the proposed method. It may be formulated as an optimization problem to identify the most appropriate relevance boundary for a given supply network. To elaborate on this, more experiments have to be conducted to gain a deeper understanding of the ties between the relevance boundary and the supply network structure to formulate a corresponding optimization problem. Secondly, more attention has to be drawn on the matching subprocess of the proposed model. When evaluating larger network structures, this matching process may limit the application of the model. Therefore, the integration of existing industry standards like the EPCGlobal framework [16] or ID@URL should be considered.

## References

[1] N. Aissaoui, M. Haouari, E. Hassini, Supplier selection and order lot sizing modeling: a review, Computers and Operations Research 34 (12) (2007) 3516–3540.

[2] A.S. Akintoye, M.J. MacLeod, Risk analysis and management in construction, International Journal of Project Management 15 (1) (1997) 31–38.

[3] M. Al-Mashari, M. Zairi, Supply-chain re-engineering using enterprise resource planning (ERP) systems: an analysis of a SAP R/3 implementation case, International Journal of Physical Distribution and Logistics Management 30 (3/4) (2000) 296–313

[4] J. Becker, D. Beverungen, R. Knackstedt, Wertschöpfungsnetzwerke von Produzenten und Dienstleistern als Option zur Organisation der Erstellung hybrider Leistungsbündel, Wertschöpfungsnetzwerke, Physica, 2008, pp. 3–31.

[5] S. Bensch, H. Schrödl, Purchasing product-service bundles in value networks — exploring the role of SCOR, in: V. Tuunainen, J. Nandhakumar, M. Rossi, W. Soliman (Eds.), Proceedings of the 19th European Conference on Information Systems, 2011, p. Paper 114, (Helsinki).

[6] S. Bensch, H. Schrödl, Purchasing Cloud-based Product-Service Bundlles in Value Networks — The Role of Manageable Workloads, ECIS 2012 Proceedings. Paper 204, 2012, http://aisel.aisnet.org/ecis2012/204.

[7] S. Bensch, H. Schrödl, K. Turowski, Beschaffungsmanagement für hybride leistungsbündel in wertschöpfungsnetzwerken - status quo und gestaltungsperspektiven, in: A. Bernstein (Ed.), Proceedings of the 10th International Conference on Wirtschaftsinformatik, 2011, pp. 231–240, (Zürich).

[8] S. Beucker, Ein Verfahren zur Bewertung von Lieferanten auf der Grundlage von Umweltwirkungen unter Berücksichtigung von Prozesskosten. Ph.D. thesis, Universitä Stuttgart, Stuttgart, 2005.

[9] T. Böhmann, H. Krcmar, Hybride Produkte: Merkmale und Herausforderungen, Wertschöpfungsprozesse bei Dienstleistungen, Gabler, 2007, pp. 239–255.

[10] A. Braithwaite, D. Hall, Risky business? Critical decisions in supply chain management (part 1), Supply Chain Practise 1 (1999) 40–57.

[11] F. Burianek, C. Ihl, S. Bonnemeier, R. Reichwald, Typologisierung hybrider Produkte: Ein Ansatz basierend auf der Komplexität der Leistungserbringung, 2007.

[12] W. Burr, Service-Engineering bei technischen Dienstleistungen: Eine ökonomische Analyse der Modularisierung, Leistungstiefengestaltung und Systembündelung, Ph.D. thesis, Universität Hohenheim, Wiesbaden, 28.01.2002.

[13] H. Corsten, R. Gössinger, Einführung in das Supply Chain Management, 2nd ed., Lehr- und Handbücher der BetriebswirtschaftslehreOldenbourg, München, 2008.

[14] A. Deif, Sensitivity Analysis in Linear Systems, Springer, Berlin, 1986.

[15] G.W. Dickson, An analysis of vendor selection systems and decisions, Journal of Purchasing 2 (1) (1966) 5–17.

[16] EPCglobal, www.epcglobalinc.com2009

[17] In: P. Fettke, P. Loos (Eds.), Reference modeling for business systems analysis, Idea Group Pub., Hershey and PA, 2007.

[18] S. Fosso Wamba, L.A. Lefebvre, Y. Bendavid, É. Lefebvre, Exploring the impact of RFID technology and the EPC network on mobile B2B ecommerce: a case study in the retail industry, International Journal of Production Economics 112 (2) (2008) 614–629.

[19] J.R. Galbraith, Organizing to deliver solutions, Organizational Dynamics 31 (2) (2002) 194–207.

[20] R.M. Garfamy, Supplier Selection and Business Process Improvement: an Exploratory Multiple-case Study, 2003.

[21] U. Götze, K. Henselmann, B. Mikus, Risikomanagement, Beiträge zur Unternehmensplanung, Physica-Verl, Heidelberg, 2001.

[22] A. Haindl, Risk-Management von Lieferrisiken, Passauer Reihe Risiko, Versicherung und Finanzierung, vol. 3, VVW, Karlsruhe and Passau, 1996.

[23] C. Harland, R. Brenchley, H. Walker, Risk in supply networks, Journal of Purchasing & Supply Management 9 (2) (2003) 51–62.

[24] D.H. Hartel, Auditierung und Erfolgsfaktoren industrieller Serviceleistungen, 1st ed., Wissenschaft und Praxis, vol. 16, TCW Transfer-Centrum, München, 2002

[25] A.R. Hevner, S.T. March, J. Park, S. Ram, Design science in information systems research, MIS Quarterly 28 (1) (2004) 75–105.

[26] M. Heyder, K. Fahrtmann, L. Theuvsen, Lieferantenbewertung in der Lebensmittelindustrie: Eine empirische Analyse, Jahrbuch der Österreichischen Gesellschaft für Agrarökonomie, vol. 18, 2009, pp. 61–70.

[27] R. Hirschheim, H.K. Klein, K. Lyytinen, Information Systems Development and Data Modeling: Conceptual and Philosophical Foundations, Cambridge Univ. Press, Cambridge, 1995.

[28] G.D. Holt, Which contractor selection methodology? International Journal of Project Management 16 (3) (1998) 153–164

[29] C. Janiesch, D. Pfeiffer, S. Seidel, J. Becker, Evolutionary method engineering: towards a method for the analysis and conception of management information systems, Proceedings of the 12th Americas Conference on Information Systems, 2006, pp. 3922–3933.

[30] J.E. Johansson, C. Krishnamurthy, H.E. Schlissberg, Solving the solutions problem, McKinsey Quarterly 3 (2003) 116–125.

[31] P. Kajüter, Instrumente zum Risikomanagement in der Supply Chain, in: W. Stölzle (Ed.), Supply Chain Controlling in Theorie und Praxis, Gabler, Wiesbaden, 2003, pp. 107–135.

[32] B. Kuechler, V. Vaishnavi, On theory development in design science research: anatomy of a research project, European Journal of Information Systems 17 (5) (2008) 489–504.

[33] J. Liu, F.-Y. Ding, V. Lall, Using data envelopment analysis to compare suppliers for supplier selection and performance improvement, Supply Chain Management: An International Journal 5 (3) (2000) 143–150.

[34] J. March, Z. Shapira, Managerial perspectives on risk and risk taking, Management Sience 11 (1987) 1404–1418.

[35] S.T. March, G.F. Smith, Design and natural science research on information technology Decision Support Systems 15 (4) (1995) 251–266.

[36] V.-W. Mitchell, Organizational risk perception and reduction: a literature review, British Journal of Management 6 (2) (1995) 115–133.

[37] N. Müssigmann, Evaluierung und Auswahl von strategischen Liefernetzen unter Berücksichtigung kritischer Knoten, Ph.D. thesis, Universität Augsburg, Augsburg, 2006.

[38] K. Peffers, T. Tuunanen, M.A. Rothenberger, S. Chatterjee, A design science research methodology for information systems research, Journal of Management Information Systems 24 (3) (2007) 45–77.

[39] K. Pousttchi, H. Schrödl, K. Turowski, Characteristics of value bundles in RFID-enabled supply networks, The Ninth International Conference on Electronic Business (ICEB 2009), 2009, pp. 886–893.

[40] M. Reiss, A. Präuer, Solutions Providing: Was ist Vision-was Wirklichkeit? Absatzwirtschaft 5 (44) (2001) 48–53.

[41] M. Sawhney, Going beyond the product: de<sup>fi</sup>ning, designing and delivering customer solutions, in: R.L. Lusch, S.L. Vargo, R. Bolton, R.F. Lusch, S.L. Vargo (Eds.), The service-dominant logic of marketing. The Service-Dominant Logic of Marketing: Dialog, Debate, and Directions, M.E. Sharpe, Armonk N.Y., 2006, pp. 365–380

[42] H. Schrödl, A conceptual approach to a service oriented architecture in supply chain management for value bundles, European, Mediterranean & Middle Eastern Conference on Information Systems 2010 (EMCIS), 2010, pp. 1–13.

[43] H. Schrödl, Service- und komponentenorientierte Informationssystemarchitekturen für die strategische Beschaffung von hybriden Produkten - ein Vergleichsrahmen, in: W. Esswein, K. Turowski (Eds.), Modellierung betrieblicher Informationssysteme, GI-Edition Lecture Notes in Informatics P, Proceedings, vol. 171, Ges. für Informatik, Bonn 2010 pp. 195–209

[44] H. Schrödl, L. Geier, Risikomanagement in der hybriden Wertschöpfung: ein Vergleichsrahmen zur Bewertung von Risikomodellen für die Lieferantenauswahl: Dienstleistungsmodellierung 2012. LNCS, 2012, (wird veröffentlicht).

[45] H. Schrödl, M. Geier, L. Latsch, K. Turowski, Risk management in supply networks for hybrid value bundles: a risk assessment framework Proceedings of the 13th International Conference on Enterprise Information Systems 2011, SciTePress - Science and Technology Publications. 2011 pp. 157-162

[46] H. Schrödl, P. Gugel, K. Turowski, Towards a reference model for the identi<sup>fi</sup>cation of strategic supply chains for value bundles, in: R.H. Sprague (Ed.), Proceedings of the 44th Annual Hawaii International Conference on System Sciences, IEEE, Piscataway and NJ, 2011, pp. 1–10.

[47] K. Sontow, Industrielle Dienstleistungen - Chancen und Barrieren im Maschinenund Anlagenbau, Sonderdruck, Aaachen, 1998.

[48] G. Svensson, A conceptual framework of vulnerability in <sup>fi</sup>rms' inbound and outbound logistics <sup>fl</sup>ows, International Journal of Physical Distribution and Logistics Management 32 (2002) 110–134.

[49] S. Talluri, R. Narasimhan, Vendor evaluation with performance variability: a max– min approach, European Journal of Operational Research 146 (3) (2003) 543–552.

[50] M. Thiell, Strategische Beschaffung von Dienstleistungen: Eine Grundlegung und Untersuchung der Implikationen dienstleistungsspezi<sup>fi</sup>scher Objektmerkmale auf Basis institutionenökonimischer ansätze, Ph.D. thesis, Friedrich-Alexander-Universität Erlangen-Nürnberg, 2006.

[51] K.-I. Voigt, M. Thiell, Beschaffung wissensintensiver Dienstleistungen - Net Sourcing als alternative Bezugsform, in: M. Bruhn, B. Stauss (Eds.), Dienstleistungsnetzwerke, Dienstleistungsmanagement, vol. 2003, Gabler, Wiesbaden, 2003, pp. 287–318.

[52] F.E. Warner, Risk: Analysis, Perception and Management, Royal Society, 1992.

[53] C.A. Weber, J.R. Current, W.C. Benton, Vendor selection criteria and methods, European Journal of Operational Research 50 (1) (1991) 2–18.

[54] C.A. Weber, J.R. Current, A. Desai, Vendor: a structured approach to vendor selection and negotiation. Journal of Business Logistics 21 (1) (2000) 135–167.

[55] B.A. Wichman, I.D. Hill, Building a random-number generator, Byte (March) (1987) 127–128.

[56] J. Wilke, Supply Chain Koordination durch Lieferverträge mit rollierender Mengen<sup>fl</sup>exibilität: Eine Simulationsstudie am Beispiel von Lieferketten der deutschen Automobilindustrie, Gabler Verlag, Wiesbaden, 2012.

[57] P. Wright, Consumer choice strategies: simplifying vs. optimizing, Journal of Marketing Research 12 (1) (1975) 60–67.

![](/api/attachments/A5KT6TXK/fulltext/images/9b1ffc4e0b631251e79b6b641c9f70ba8918c51f957f992aefd122cbdff6dc4e.jpg)

Holger Schrödl, born in 1969, received a diploma degree in Mathematics and a Dr. degree in Business Informatics at the University of Augsburg. He worked in several industry positions in the areas of software development, IT consulting and Business Intelligence. In 2009 he changed as research assistant to the chair of Business Informatics and Systems Engineering at the University of Augsburg. In this position he worked in the area of interorganizational information systems and hybrid value bundles. Since 2011 he is a research assistant at the Otto von Guericke University Magdeburg and works in the area of very large business applications and IT operations management.

of Augsburg, the Cooperative State University Baden Württemberg Mannheim, the University of Applied Sciences Aalen and the University of Applied Sciences Munich He (co-)organized a variety of national and international scienti<sup>fi</sup>c conference tracks and was a member of several program committees and review boards.

Holger Schrödl had teaching assignments at the University

![](/api/attachments/A5KT6TXK/fulltext/images/7443de1a495d5ec6be613ad8a70b6ec0e1efa54905af8285b0566807793f8396.jpg)

Klaus Turowski, born in 1966, received a diploma degree in Industrial Engineering and Management at the University of Karlsruhe, a Dr. degree in Business Informatics at the University of Münster, and habilitated in Business Informatics at the Computer Science faculty of the Otto von Guericke University Magdeburg. In 2000 he was a visiting professor at the University of the Federal Armed Forces Munich. From 2001 he held the chair of Business Informatics and Systems Engineering at the University of Augsburg. Since 2011 he is a professor at the Otto von Guericke University Magdeburg. There he holds a chair of Business Informatics (AG WI), heads a research lab for very large business application systems (VLBA Lab), and is the academic director of the world's largest SAP university competence center (SAP UCC Magdeburg).

He was a visiting professor at various universities abroad and had teaching assignments at the Universities of Darmstadt and Konstanz. He (co-)organized a variety of national and international scienti<sup>fi</sup>c conferences (>30) and was a member of numerous program committees (>130) and expert groups. Besides his theoretical background, he has been working in various consulting projects.

Please cite this article as: H. Schrödl, K. Turowski, Risk management in hybrid value creation, Decision Support Systems (2013), http:// dx.doi.org/10.1016/j.dss.2012.12.042

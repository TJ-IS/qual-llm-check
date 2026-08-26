---
otero_id: 10534
otero_key: "2UG5GNVE"
title: "Design support systems: A case study of modular design of the set-top box from design knowledge externalization perspective"
authors: "Tzu-Liang (Bill) Tseng; Chun-Che Huang"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.10.013"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# Design support systems: A case study of modular design of the set-top box from design knowledge externalization perspective

Tzu-Liang (Bill) Tseng <sup>a</sup>, Chun-Che Huang <sup>b,⁎</sup>

<sup>a</sup> Department of Mechanical and Industrial Engineering, The University of Texas at El Paso, El Paso, TX 79968, USA <sup>b</sup> Department of Information Management, National Chi Nan University, Pu-Li, Nan Tau 545, Taiwan

Received 20 June 2006; received in revised form 17 October 2007; accepted 17 October 2007 Available online 4 November 2007

## Abstract

In this paper, the knowledge externalization of modular product design is introduced, which discovers and shares the design rules to increase the effectiveness/efficiency of the design process. This solution approach involves modeling modular products, formulating their design knowledge, and discovering implicit knowledge into design rules based on the rough set theory. The design rules are generated for improving heat dissipation issues of the set-top box (STB), which is perhaps the most attractive device for the home. A web based knowledge management of product design (KMPD) system is also implemented to provide adapted design rules and share design knowledge in distributed environment. The methodology discussed in the paper departs from the previous developments in design knowledge externalization as well as rough set theory application, thus creating a variable approach for product design.

Keywords: Set-top box; Modular product design; Knowledge externalization; Rough set theory; Heat dissipation

## 1. Introduction

It is very crucial to externalize design knowledge precisely if designing products is required to be distributed to different locations. Externalization means to make an abstraction concrete or perceptible knowledge, often by representation in human form. Through the externalization process, design knowledge can be unified, explicated, and disseminated for product design.

Design of modular products and reconfigurable processes are crucial to agile manufacturing and are a way to produce a variety of products to satisfy various customer requirements on time [17]. Modular product design is an important form of strategic flexibility [34], i.e., flexible product designs that allow a company to respond to the changing markets and technologies by rapidly and inexpensively creating product variants that are derived from different combinations of the existing or new modular components. The use of the core product concept and modular design process allows companies to quickly adapt to the changes in product and process technologies, as well as the change in consumer needs. By reducing the time and the amount of resources consumed in responding to these changes, the system flexibility is enhanced.

To externalize design knowledge of modular products, the solution approach involving modeling modular products, formulating their design knowledge, and discovering implicit knowledge are required. To complete design knowledge externalization process, one of the effective methodology is applying rule induction approach to generate design rules [21].

A rule induction approach is given the examples of a problem (called a training set) for which the outcome is known, e.g. previous design results. After the training set has been provided with sufficient examples, rules that fit the example cases can be created [39]. These rules are stored in rule-based knowledge management systems and mainly in the form of ‘if-then’ conditions. That is, the rules are triggered by conditions (facts) or problem events that match the if-part of the rule. The ifpart triggered rules result in a variable substitution that is applied to the then-part of the rule, instantiating a new fact. This process is executed until no more rules can be triggered [6] and the benefits module is ready for domain expertise in solving design problems. In addition, this kind of structured knowledge, e.g., design rules, benefits modularity of knowledge representation, independence of language between the representation of the design rules and the inference mechanism itself. It is a plausible model of human problem solving, being relatively easy for a human expert to represent his/her design knowledge in the form of rules [26].

The set-top box (STB) is the foundation of digital broadcast. All the critical subsystems, including the CPU, system chipset, memory, system I/O, expansion bus, and other critical components make up the STB modularly. The STB supports the consumers who wish to receive digital signals via their analog electronic devices. It is perhaps one of the most attractive devices for the home since it is used to improve video and audio quality. Since the STB is a widely used electronic device and its defective components require quick and easy replacement for repair, therefore the modular design approach is essential for the STB.

Chiang [3] analyzes the integration of major functions and the consolidation of separate memories, which integrate the decoder for the STB. Sohi and Gulak [37] try to implement a single reconfigurable hardware architecture that can satisfy the performance requirements while minimizing cost. An STB consists of a channeldecoding process and a source-decoding process. The channel-decoding process supports the transmission over the physical media. It delivers an error free signal to the source-decoding process. The error correction function is usually grouped in ‘forward error correction (FEC) as it provides error detection and correction to the received signal. The source-decoding process descrambles, de-multiplexes, and decodes the audio and video signal for reproduction.

The design goals of an STB should include costeffectiveness, expandability, compatibility, data independency, and so on [15]. The benefits of modular design [4,29] include economies of scale (cost-effectiveness), increased feasibility of product/component change expandability), increased product variety (compatibility), de-coupling tasks (independency), and so forth. Hence, the modular design can meet the design goals of STB effectively. Moreover, the modular design is supported with various knowledge domains, e.g., hardware involved knowledge, comprehension of various industrial standards, software programming (embedded system) capacity, and signal analysis skills.

This paper focuses on the knowledge externalization of modular product design for STB. Specifically the sharing and improvement of design knowledge, which refers to the formal management for facilitating creation, sharing, and re-use of the design knowledge with the use of Internet technology to increase the effectiveness/ efficiency of modular product design. The objectives of the paper are two-fold: First, modeling and discovering of the design knowledge. Second, proposing the typical design rules for improving heat dissipation issues of the STB.

The format of this paper is as follows: In Section 2, modeling knowledge of modular design is illustrated. This section includes modeling modular products and externalization of design knowledge. In Section 3, design rule induction is presented, followed by the new heuristic algorithm. A case study of modular STB design, which comprises overview of the STB system and design issues of the heat dissipation is explored in Section 4. In Section 5, sharing design knowledge in distributed environment is illustrated and implementation of the system is covered in this section. The suggestions of improving heat dissipation issues of the STB and research findings are discussed in the conclusion section.

## 2. Modeling modular design knowledge

Design process is often a conceptualization, which is not easy to share and seldom documented formally [29]. This section presents the modeling of modular product design, externalization of design knowledge, which includes module algebra, module operators and representation of design process and design knowledge storage.

## 2.1. Literature review of product design and modular products

In modern business, product design is defined as “the process of converting an idea into information from which a new product can be made” [33]. The process involves in the creation of synthesized solutions that satisfy perceived needs through mapping between functional requirements (FRs) in the functional domain and the design parameters (DPs) of the physical domain, through the proper selection of DPs that satisfy FRs [20]. Product design therefore is the activity in which ideas or market requirements are given, starting from the initial sketches or conceptual designs, through prototype development, to the detailed drawings and specifications needed actually to make the product. The problems involved in the product design [29,40] are often of such size and complexity that no single individual, organization, or design environment is capable of effectively addressing all aspects of the design and include “limited policies for recording experience” in acquiring and using system knowledge within companies.

Knowledge management in product design is a key challenge to increase business competitiveness. A great part of the product design knowledge in manufacturing enterprises is only available in forms of natural language documents, and is often type of tacit and not easy to share in public [32,36]. The know-how recorded in these documents is an essential resource of successful competition in the market. From the viewpoint of knowledge management, documents do not capture the wealth of knowledge contained in themselves, since the entire knowledge is not spelled out on the linguistic surface. Furthermore, what is also becoming clear is that further requirements of high variety and rapid product design are gradually being superimposed upon these older requirements. Therefore, the complex product markets of the twenty-first century will demand the ability to quickly and globally deliver a high variety of customized products. Earl Hall quoted in Davidow and Malone [5].

In such situations, the product design must be modularized [13,17] and addressed by a team of specialists or intelligent agents using the agent technology [16,44]. Modular products refer to products, assemblies and components that fulfill various functions through the combination of distinct building blocks (modules) [29]. The mixing and matching of modules in a modular product design can generate a potentially large number of different products in a modular product models consisting of distinct combinations of components that give each model distinctive functionalities, features, and/or performance levels [24,35,43]. Thus modular product design is an important form of strategic flexibility [34], i.e., flexible product designs that allow a company to respond to the changing markets and technologies by rapidly and inexpensively creating product variants derived from different combinations of the existing or new modular components. Potential benefits of modularity include economy of scale, increased feasibility of product/component change, increased product variety, reduced order lead-time, decoupled risks, easier product diagnosis, maintenance, repair, and disposal [4,27,29].

## 2.2. Modeling modular products

Modularity is viewed in [41] as depending on two characteristics of design:

(1) similarity between the physical and functional architecture of the design, and

(2) minimization of incidental interactions between physical components.

The characteristics above imply two types of relationships involved in the modularity concept:

(1) high degree of functional interactions of intermodules, and

(2) low degree of interactions among components of intra-modules.

Based on these two relationships, an interaction graph is used to represent modular products. An interaction graph (A, E, W) is a schematic graph with weights on the edges, where A is the node set representing product components, E is the edge set representing functional interactions, and W is the weight set of frequencies of the functional interactions among components. An example of interaction graph is shown in Fig. 1, where $A = \{ 1 , m , n , . . . \} . E ^ { = } \{ ( 1 m ) , ( m , n ) , . . . \}$ The weight $w _ { ( 1 , \ m ) } = 8$ indicates the function interaction from component l to m occurs in eight types of products.

The weight density of a sub-graph is defined as the ratio of the total weight of the edges included within the sub-graph over the number of edges included. The weight density determines the quality of clusters.

A cluster in the interaction graph is represented as a set of connected nodes N that satisfies [1,13]:

$$
w _ {d N} - w _ {i j} > \theta \text {   for   all   } i \in N \text {   and   } j \notin N, N \subseteq A
$$

where

$$
w _ {d N} \quad \text { weight   density   of   the   set } N \text { of   nodes   (components) }
$$

![](/api/attachments/2UG5GNVE/fulltext/images/8a37bceabeb594ee517d9c7aa484385e90422b06827da5e635e9f7caaf664557.jpg)  
Fig. 1. An example of interaction graph.

$w _ { i j }$ weight on the intra-edge from node $i \in N$ to $j \not \in N$

θ threshold index used to include a node in (or exclude from) a cluster.

For example, consider cluster (module) $3 = \{ k ,$ l, m, $n \}$ in Fig. 1. The weight density of cluster 3 is $w _ { d 3 } = 8 .$ If θ is set to $5 ,$ no additional nodes can be included in cluster 3. If θ is set to 4, then nodes $a , e , t ,$ and f would be included in cluster 3. The larger the value θ, the smaller size of a cluster. The value of the module threshold index θ is determined arbitrarily.

The components (nodes) that do not belong to a module (cluster) are referred to as independent components (nodes). The independent components (nodes) may be the basic components (nodes) that jointly with the modular components result in different types of modular products, e.g., basic components c and d in Fig. 1.

Based on the interactions within a product, three categories of modularity have been defined [41]:

(1) Component-swapping modularity occurs when two or more different basic components are paired within a module, thus creating different product variants that belong to the same product family.

(2) Component-sharing modularity is complementary to component-swapping modularity. Various modules sharing the same basic component create different product variants that belong to different product families.

(3) Bus modularity occurs when a module can be matched with any number of basic components.

Bus modularity allows for variation in the number and location of basic components within a product, while component-swapping and componentsharing modularity allows only for the types of basic components to vary.

Note that in the above three types of modularity, replacing a basic component with a module that interacts with other modules results in different types of moduleswapping, module-sharing, or global bus modularity. A customized product may be made up of numerous modules, e.g., the creation of a PC including a terminal, a motherboard, a keyboard modules, etc. Consequently, a customized product may consist of a base module and several customized auxiliary modules, adaptive modules, or basic components. With this approach, customized products can be produced quickly with lower manufacturing costs. The strategy of “modular products design” aims to reduce the design/manufacturing difficulties that are typically involved in manufacturing customized products.

Examples of modularity are presented in Huang and Kusiak [13].

## 2.3. Externalization of design knowledge

In general, externalization means to make an abstraction concrete, or perceptible, often by representation in human form. Therefore, it is very critical to externalize design knowledge properly when designing modules of products that are required for distribution to different places. Numerous literatures provide externalization of knowledge. For example, Nonaka et al. [28] proposed four modes of knowledge conversion: socialization, externalization, combination, and internalization (SECI model). The process of externalization converts tacit knowledge into explicit knowledge. Kwok et al. [23] proposed a study on knowledge externalization of Group Support Systems (GSS) [25]. Huang and Kuo [12] proposed a flow chart of externalization process of semi-structured knowledge. Huang [11] externalized the product design using star schema. However, there is limited information regarding externalization of design knowledge, specifically, the design knowledge for modular products. In this section, externalization of design knowledge includes module algebra, module operators, and representation of the design process. The details are as follows:

## 2.3.1. Module algebra

The main role of the module algebra is to define what is to be represented, and to specify the characteristics and properties of the aspects that are to be represented. This serves as a building block of the functional structure [29]. In this work, engineering design is viewed as a transformational incremental and evolutionary activity, e.g., adding a desired module to the artifact.

With the design requirement defined, the design with module (DwM) model [14] of the current design state $( P ^ { \prime } )$ is defined as follows:

In the DwM model, an artifact model consists of design functionality of modules and their relations (input/output interfaces).

$$
P ^ {\prime} = \sum_ {i j} \Phi_ {\mathrm{add}} i j M _ {i}\tag{1}
$$

The symbol $\textstyle \sum _ { i j }$ is taken to mean that a DwM model is an assembly of design modules, not just a collection of models. It includes not only design models but also the relations between them. The set of relations between the models, $\{ \varPhi _ { \mathrm { a d d } } \ i j \}$ , specifies the relations between $M _ { i }$ and other modules $j ^ { \circ } \mathbf { s }$ in $P ^ { \prime }$ . This regulates an instance of a design module such that the modules satisfy the intended sub-functional requirements and handle the validity of the model by controlling the interaction between the modules. Another property of the DwM model is the module index set $( \{ M _ { i } \} _ { P ^ { \prime } } )$ , which is defined as a set of modules constituting a DwM model, $P ^ { \prime }$

## 2.3.2. Module operators

A module operator is a mechanism for changing a DwM model. In order to formally define a module operator, a broader concept of design change, called design operation, is introduced. A design operation is any design activity that brings some change to an artifact model.

In order to apply a module operator, both the module to be manipulated and the model to which the operator is applied should be specified. An operator that brings change to the module indexed set of a model is termed a unit operator and any change in the DwM model $P ^ { \prime }$ can be obtained by applying a finite number of unit operators to $P ^ { \prime } .$ . The new outcome of DwM model is represented as P. Two basic module operators are defined as follows:

An add module operator on a model $P ^ { \prime }$ is a unit operator which adds exactly one module to the module index set $\left( \{ M _ { i } \} _ { P ^ { \prime } } \right)$

$$
\Phi_ {\mathrm{add}} (M _ {k}): P ^ {\prime} \rightarrow P \text {   where   } \{M _ {i} \} p = \{M _ {i} \} p ^ {\prime} - M _ {k}\tag{2}
$$

A delete module operator on a model $P ^ { \prime }$ is a unit operator which deletes exactly one module from the module index set $\left( \{ M _ { i } \} _ { P ^ { \prime } } \right)$

$$
\Phi_ {\text { delete }} (M _ {k}): P ^ {\prime} \rightarrow P \text {   where   } \{M _ {i} \} p = \{M _ {i} \} p ^ {\prime} - M _ {k}\tag{3}
$$

The module operator should also check the suitability of the constraints of the module interfaces, while the modules are selected. The constraints involved in the customer and concurrent engineering constraints can be referred in Huang and Kusiak [13].

As an illustration of the add module operator, Fig. 2 shows a design service to synthesize modules M1 and M2 into module M1+M2.

The module service is named $\mathbf { \ddot { M } } 1 + \mathbf { M } 2 \mathbf { \ddot { \Omega } }$ and has both of its inputs available: Input I1 from the client and input C2 from the server. The output field specifies the information produced by the service (in this case, module M1+ M2 and the output O2). In this illustrated example, the service consists of three sub-services (S1, S2, S3)= (Sub-service\_explore\_M1, Sub-service \_explore\_M2, and Sub-service\_add (M1, M2)) which must be executed in parallel (S1 and S2) and then sequenced (with S3). Associated with ok\_M1 + M2 is a completion expression, which specifies that each of the sub-services must successfully be completed if the entire service is to succeed.

## 2.3.3. Representation of the design process

In essence, the flow of design operations in the DwM is represented in terms of module operators. A combination of operators is an ordered set of module operators that are successively applied to the model. The order of elements in a combination represents the order in which the module operators are applied. The symbol ⊕ is used to represent the operators that are applied.

![](/api/attachments/2UG5GNVE/fulltext/images/57bbb063252ea55ffdbc3e914aaf51d5cdac2e67bc4b29553000bc1cca402eaa.jpg)  
Fig. 2. An illustrative of a template of design.

Three characteristics of the module operators are illustrated next [14]:

• Associative property

$$
\left(\Phi_ {i (M _ {i})} \oplus \Phi_ {j (M _ {j})}\right) (P ^ {\prime}) = \left(\Phi_ {j (M _ {j})} \left(\Phi_ {i (M _ {i})} (P ^ {\prime})\right)\right)\tag{4}
$$

The result of two modules combined together with any DwM model is equivalent to the result of the DwM model combining one module first, and then combining the other later.

• Recursive property

A combination can be defined recursively as follows:

$$
\begin{array}{l} \big (\Phi_ {1 (M _ {1})} \oplus \Phi_ {2 (M _ {2})} \oplus ... \oplus \Phi_ {n (M _ {n})} \big) (P ^ {\prime}) \\ = \big (\Phi_ {n (M _ {n})} \big (\ldots \big (\Phi_ {2 (M _ {2})} \big (\Phi_ {1 (M _ {1})} (P ^ {\prime}) \big)... \big) \big) \end{array}\tag{5}
$$

This property is the extension of the associative property.

• Non-exchangeable property

This states that the operator $\varPhi _ { j ( M _ { j } ) }$ is applied to the result of the operator $\varPhi _ { j ( M _ { i } ) }$ . Also, $( \ddot { \phi } _ { j ( M _ { i } ) } \oplus \bar { \phi } _ { j ( M _ { i } ) } ) ( P ^ { \prime } )$ is generally not equivalent to $( \bar { \phi } _ { j ( M _ { i } ) } \oplus \bar { \phi } _ { j ( M _ { i } ) } ) ( P ^ { \prime } )$ due to the validity preserving property included in module operators.

Modular products are modeled and generated in this way using the interaction graph, DwM model, and module operators. Through module algebra, module operators and representation of design process, the design knowledge can be externalized. Therefore, the graph, DwM models, and operators are able to store in the data repository with a systematic format. Once this transformation is completed, the data sets can be used to induct numerous design rules in order to explicit the DwM model.

## 2.4. Design knowledge storage

Design knowledge (record) is modeled in a similar approach to data warehouses using the dimensional modeling [8] approach that is one of the best approaches to model/store decision support knowledge for data warehouse [18]. Dimensional modeling is a logical design technique that seeks to present the data in a standard framework that is intuitive and allows for highperformance access. The production of dimensional modeling approach can be referred in Huang [11].

After modeling dimensional tables, which store the modules' information, the retrieved data from data warehouse is shown in Table 1, where each column is retrieved from the data warehouse by selecting modules of STB from any of the dimension tables. The information of each column (module) may be stored in different databases but combined together according to the selected objective. The columns of Table 1 are modules of STB, and the rows denote a set of combinations about STB design. The entries of each column denote types of modules. This information will be analyzed by the rough set approach to generate reduct rules. The design rule induction is introduced in the next section.

Table 1  
The structure and contents of modular design historical data

<table><tr><td>Code</td><td>A</td><td>B</td><td>C</td><td></td><td>M</td><td></td><td></td></tr><tr><td>Design records</td><td>Tuner</td><td>ADC</td><td>OFDM demodulation</td><td>......</td><td>Remote controller</td><td>......</td><td>Cost</td></tr><tr><td> $\Phi_1$ </td><td>TD1622</td><td>{AS1868A}</td><td>PDC5093</td><td>......</td><td>RM-1</td><td>......</td><td>$2400</td></tr><tr><td> $\Phi_2$ </td><td>TD1838</td><td>{AS1883}</td><td>PCD5122</td><td>......</td><td>RM-1</td><td>......</td><td>$4650</td></tr><tr><td> $\Phi_3$ </td><td>TD1838</td><td>{AS1888}</td><td>PCD5122</td><td>......</td><td>RM-1</td><td>......</td><td>$4000</td></tr><tr><td> $\Phi_4$ </td><td>PX6623</td><td>{FA7033}</td><td>SD-11A</td><td>......</td><td>RM-2</td><td>......</td><td>$5750</td></tr><tr><td> $\Phi_5$ </td><td>PX6623</td><td>{FA7066}</td><td>SD-11C</td><td>......</td><td>RM-2</td><td>......</td><td>$6100</td></tr><tr><td> $\Phi_6$ </td><td>PCD5127</td><td>{ZF6603}</td><td>A9346</td><td>......</td><td>RM-3</td><td>......</td><td>$2600</td></tr></table>

## 3. Design rule induction

In this section, design rules are inducted that are based on the production of the dimensional modeling and data repository. The rough set approach is proposed to induct design rule from the data repositories. The rough set approach for rule induction could improve the efficiency of the discovery and the quality of knowledge.

In product design, the design rules, constraints and knowledge that have impact on the design processes and results. They always exist in either structured or unstructured formats. The structured ones are obvious and are described in specifications, datasheets, and other digital reports, i.e. the working voltage of a component, frequency, temperature, and so on. The structured ones are easy to digitize and transform to a rule base. Unstructured ones are tacit and uncertain in the database, data warehouse and data mart. To induct the unstructured ones, data mining techniques are widely adopted. Data mining is an emerging area of computational intelligence that offers new theories, techniques, and tools for processing large volumes of data. It has gained considerable attention among practitioners and researchers. The growing volume of data that is available in a digital form has accelerated this interest [9,10,19].

To discover design knowledge, the design rule induction approach is proposed. Fig. 3 illustrates the functional architecture of the solution approach. Two sources compose a rule base. (i) Raw data is stored in distributed data repositories, i.e. manufacturing, marketing. These repositories imply a large amount of tacit knowledge that may support design decisions. The tacit knowledge needs to be inducted and turned into explicit knowledge. Thus, for this source, the rough set theory is adopted to derive rules, and an algorithm is developed to validate the derived rules based on the test set. (ii) Structured source, e.g., specifications, datasheets and other digital reports (the explicit knowledge) are digitalized and transformed directly to rule forms and stored in the rule base. In other words, this method is based on rough set theory for inducing “product design” rules that are developed from the data repository.

In data mining approach, according to Kusiak [19], the bootstrapping method suggests splitting the data set according to the following ratio, 0.632 for the training set and 0.368 for the test set. The rule-composing algorithm is developed to derive rules for the training set. The reduct generation procedure [22] to generate multiple feature sets (i.e. reducts) is adapted. These feature sets are used for predicting an object's outcome based on the proposed algorithms. Furthermore, the procedure to validate the derived rules, based on the test set, is also proposed. The rule-composing algorithm and rule-validation procedures are presented next.

## 3.1. The reduct generation procedure

According to rough set theory [30], $I { = \{ U , A \} }$ is an information system, where U is a finite set of objects and A is a finite set of attributes. In this paper, an attribute (feature) refers to a module while an object (record) refers to a product. With every attribute $a \in A ,$ , a set of its values Va is associated. Assume $A { = } C \cup D _ { \mathrm { : } }$ $B \subset C ,$ , where B is a subset of $C ;$ the positive region $\mathrm { P O S B } ( D ) = \{ x \in U ; [ x ] B \subset D \}$ can be defined. The positive region POSB(D) includes all objects in $U$ which can be with classified into classes of $D ,$ in the knowledge B. The degree of dependency between B and D can be defined as $K ( B , D ) { \frac { \operatorname { c a r d } ( \operatorname { P O S B } ( D ) ) } { \operatorname { c a r d } ( \operatorname { P O S C } ( D ) ) } }$ , where card yields the set cardinality. In general, if $K ( B , D ) = K ( C ,$ D), and $K ( B , \ D ) { \neq } K ( B - \{ a \} , \ D )$ , for any $a \in B$ are hold; then B is a reduct of C. Since a reduct (B) preserves the degree of dependency with respect to D and a reduct (B) is a minimal subset, any further removal of condition attributes will change the degree of dependency [38]. Note that the term “attribute” is normally substituted with “feature” based on a different application. For example, Kusiak [19] uses it to identify significant factors in semi-conductor manufacturing.

![](/api/attachments/2UG5GNVE/fulltext/images/13fa1d0166331932c83d44a3c7d93dfef10a7829e55359e0060c085e094ee020.jpg)  
Fig. 3. Functional Architecture of the solution approach.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
The Reduct Generation Procedure:
Input: A decision table I classified into C and D.
Output: The reducts.
Step 1. Initialization: List all objects in I
Step 2. Generate the reducts for each object
for i=1 to n do
    for j=1 to m
    if  $[V_{ij}]_{A_j} \subset [V_{ik}]_{O_{k|i}}$ 
    then the reducts for Xi is formed
    else for j=1 to m
    if  $\bigcap_{C-A_j}[V_{ij}]_{A_j} \subset [V_{ik}]_{O_{k|i}}$ 
    then the reducts for Xi is formed
    else the reducts for Xi is not formed
    endfor
    endfor
    endfor
Step 3. Termination: Stop and output the results.
</div>

Note that the Xi represents the objects where each $A _ { j }$ attribute contains $V _ { i j } ,$ while $[ V i k ] _ { O _ { k | i } }$ includes the objects with each $O _ { k | i }$ outcome (decision) attribute containing $V _ { i k } .$ . In order to find dispensable attributes, the examination of each attribute of the object is required by dropping one attribute at a time and rechecking to determine if the intersection of the remaining attributes is still included in the decision attribute.

## 3.2. The rule-composing algorithm

The proposed rule-composing algorithm that derives rules from the training data set consists of the following steps [38]:

Step 1. Define a proper feature set and a target file. This step is critical to obtain high-accuracy outcomes generated by the algorithm.

Step 2. Examine each object in the set for completeness. If the object is uncompleted, then delete the object from the file; repeat through all objects.

Step 3. Determine the final rules from the candidate decision rules generated by the reduct generation procedure. If all of candidate decision rules are satisfied then go to Step 6; otherwise go to Step 4.

Step 4. If candidate decision rules are satisfied, then transfer the rules to Step 5; otherwise, restore the objects associated with unsatisfied rule and go to Step 3.

Step 5. Collect all of the satisfied decision rules and go to Step $6 ;$ otherwise, go to Step 4.

Step 6. Stop and output the results (i.e., the potential rules for further validation).

## 3.3. The rule-validation procedure

The following steps are applied to the validation data set to validate the rules derived from the above algorithm [38]:

Step 1. Compare each decision rule that was derived from the rule-composing algorithm with each new object from the validation data set. Calculate the number of objects that are matched with the rule. Step 2. Repeat comparison of the decision rules with objects from the validation set until no decision rule is left.

Step 3. Calculate the accuracy of each rule by using total matched objects (for each rule) divided by summation of total correctly matched objects and total incorrectly matched objects. If accuracy of the rule is greater than a predefined threshold value (e.g., 60%), then go to Step 4; otherwise, remove the rules. Notably, an incorrectly matched object means that the object contains the identical known value of conditional features with the rule but different outcomes.

Step 4. Stop and output the results of validated rules.

Next, a numerical example is applied to illustrate the use of the algorithm and procedure.

## 4. A Case study of modular design of the set-top box

## 4.1. Overview of the STB system

Modular design is wildly adopted in STB industrial because of the complexity of STB design process. The modular design is supported with various knowledge domains, e.g., knowledge of the hardware involved, comprehension of various industrial standards, software programming (embedded system) capacity, and signal analysis skills. For example, a DVB (Digital Video Broadcasting) STB consists of 13 modules at the perspective of hardware. The basic building block, as shown in Fig. 4, serves as a platform for decoding electronic device programs in a standard definition. An STB consists of a channel-decoding process and a source-decoding process. The channeldecoding process supports the transmission over the physical media and it delivers an error free signal to the source-decoding process. The error correction function is usually grouped in ‘forward error correction’ (FEC) as it provides error detection and correction to the received signal. The source-decoding process descrambles, demultiplexers, and decodes the audio and video signal for reproduction.

In practice, the module is highly integrated with solutions from almost all electronic manufacturers, i.e. the channel-decoding process usually is highly integrated and it is usually offered as a single chip solution (module B to E); and is designed for variety of products, i.e. solution for DVD player. Table 2 briefly describes the functions and encode of each module.

![](/api/attachments/2UG5GNVE/fulltext/images/031bd3a9f65d93c67b32c445ce6bfe98bfd5f531e6ac69f76e610f61ec0a174e.jpg)  
Fig. 4. The hardware architecture of the DVB STB.

## 4.2. Design issues for the STB system

Due to complexity of the STB design process, and numerous design factors, most of the studies focus diversely on CPU operational performance [31], memory requirement [3], decoder integrating [7], and various industrial standards to be considered simultaneously [37]. However, one issue is crucial and is not considered in the previous studies: issue of heat dissipation in modular design of STB.

Heat dissipation: Heat dissipation influences performance and reliability significantly when the devices heat up too much. In any electronic design, as more components are squeezed into a smaller space, heat dissipation becomes an issue. The physical nature of electronics creates thermal management issues with a smaller, more functional design. This is complicated in a small consumer device because market forces prohibit the use of costly, large, and noisy heat management devices such as fans. When using semi-conductors, heat dissipation becomes an important issue because if the devices heat up too much, they lose performance, reliability, and lifespan [42].

## 4.3. A numerical illustration

In a set-top box, the major design consideration and challenges of functionality that includes heat dissipation, footprint, and routing/splitting of the signal. Additionally, each new service feature, such as picturein-picture, interactive television, high-speed Internet access, and personal video recording (PVR), requires its own dedicated tuner. Consequently, advanced STB designers need to consider the impact of combining multiple tuners in a single box. The wireless capability of providing streaming data and video throughout the house requires additional silicon technology — such as 802.11x, Bluetooth, or other solutions.

Table 2  
Description and encode of the STB modules

<table><tr><td>Module</td><td>Description</td><td>Code</td></tr><tr><td>1. Tuner</td><td>The tuner (sometimes known as the ‘front-end’), generally select one of the RF (Radio Frequency) channel and converts it into IF (Intermediate Frequency).</td><td>A</td></tr><tr><td>2. ADC (Analogue to Digital Converter)</td><td>The ADC receives the analogue signals and converts it into a digital signal for OFDM processing.</td><td>B</td></tr><tr><td>3. OFDM demodulation (Orthogonal Frequency Division Multiplexing)</td><td>This is the key element in the channel-decoding process: It performs digital demodulation and half-Nyquist filtering, and reformatting/demapping into an appropriate form for the FEC circuit. It also plays a part in the clock and carrier recovery loops, as well as generating the AGC (automatic gain control) for control of the IF and RF amplifiers at the front-end.</td><td>C</td></tr><tr><td>4. FFT (Fast Fourier Transform) processor</td><td>The FFT processor provides timing and frequency synchronization, channel estimation and equalization, generation of optimal soft decisions using the channel state information, symbol and bit de-interleaving.</td><td>D</td></tr><tr><td>5. Forward Error Correction (FEC)</td><td>The FEC block performs de-interleaving, Reed-Solomon decoding and energy dispersal de-randomizing. The output data are the 188 bytes transport packets in parallel form (8 bit data, clock and control signals).</td><td>E</td></tr><tr><td>6. CPU core</td><td>The whole system is controlled by a powerful 16/32-bit microprocessor, which controls all the circuitry, interprets user commands from the remote control, and manages the smart card reader(s) and the communication interfaces.</td><td>F</td></tr><tr><td>7. Descrambler</td><td>The descrambler receives the transport packets and communicates with the main processor by a parallel bus to allow quick data transfers. It selects and descrambles the packets of the required program under control of the conditional access device.</td><td>G</td></tr><tr><td>8. De-multiplexer</td><td>The de-multiplexer selects, by means of programmable ‘filters’, the PES packets corresponding to the program chosen by the user.</td><td>H</td></tr><tr><td>9. MPEG-2 decoder</td><td>The audio and video PES outputs from the de-multiplexer are applied to the input of the MPEG-2 decoder, which generally combines MPEG audio and video functions and the graphics controller functions required, among other things, for the electronic program guide (EPG). MPEG-2 decoding requires at least 16 Mbits (2MB) of DRAM [2].</td><td>I</td></tr><tr><td>10. Audio DAC</td><td>Decompressed digital audio signals in I2S format or similar are fed to a dual digital-to-analogue converter (DAC) with 16 bits or more resolution which delivers the analogue left and right signals.</td><td>J</td></tr><tr><td>11. Digital Video Encoder</td><td>Video signals reconstructed by the MPEG-2 decoder are then applied to a digital video encoder, which ensures their conversion into analogue RGB plus synchronization signals. For the best possible quality of display on a TV set via the SCART/PERITEL plus and PAL, NTSC or SECAM.</td><td>K</td></tr><tr><td>12. Smart Card Reader</td><td>The conditional access device generally includes one or two of these (one might be for a banking card, for instance). In the case of a detachable conditional access module using the DVB-CI common interface.</td><td>L</td></tr><tr><td>13. Remote Controller, Front Panel Control</td><td>Used for user channel selection or to capture any user choice. Also can be used for interactive TV feedback via modem.</td><td>M</td></tr></table>

The combination of selected features in an STB implies that they potentially impact the overall functionality. For example, the engineers believe only module F, G, H, I, J, K and M are relatively correlated to heat dissipation. Consider the example of 20 source-decoding solutions of the STB as shown in Table 3, the data set is divided into a training data set (the first fifteen objects) and the remaining as the validation data set. The input features of Table 3 are constituted from empirical data of modular design (e.g., Table 1) when heat dissipation is taken into consideration. The output feature is designated to display the status of the heat dissipation based on the threshold temperature. The value of “1” is corresponding to overheating while the value of “0” corresponds to normal temperatures. All modules, which are significantly related to heat dissipation, are selected as input features in Table 3. For example, a DVD STB includes thirteen modules (see Table 2) where only seven selected modules constitute the desired features and the entry of each feature (e.g., F1 to F7) denotes the type of module. These are the CPU core module (F1), descrambler module (F2), de-multiplexer module (F3), MPEG-2 decoder module (F4), audio DAC module (F5), digital video encoder module (F6), and remote controller module (F7). Note that these selected modules are retrieved from different databases and the letter “F” stands for feature here. Combining different modules (from F1 to F7) will result in different outcomes (see Table 3). Those initial data are used by the rough set approach to derive the quality rules. The reduct rules are generated by the rough set approach to support module design and stored in rule bases which can be used again in the future. Moreover, determination of threshold temperature is based on the range of standard operating temperature plus 15%. In order to maintain flexibility, performance, reliability, and lifespan of the set-top box, each product is required to avoid overheating. Therefore, identifying which modules and the specific type of the module has significant impact on heat dissipation is critical in STB production process.

Table 3  
Example of training and test data set

<table><tr><td>Object No.</td><td>F1 (F)</td><td>F2 (G)</td><td>F3 (H)</td><td>F4 (I)</td><td>F5 (J)</td><td>F6 (K)</td><td>F7 (M)</td><td>R</td></tr><tr><td>1</td><td>0</td><td>3</td><td>2</td><td>1</td><td>1</td><td>2</td><td>1</td><td>0</td></tr><tr><td>2</td><td>1</td><td>3</td><td>0</td><td>1</td><td>0</td><td>3</td><td>0</td><td>0</td></tr><tr><td>3</td><td>1</td><td>4</td><td>0</td><td>0</td><td>7</td><td>3</td><td>0</td><td>0</td></tr><tr><td>4</td><td>0</td><td>4</td><td>0</td><td>1</td><td>0</td><td>4</td><td>1</td><td>0</td></tr><tr><td>5</td><td>0</td><td>3</td><td>0</td><td>0</td><td>2</td><td>3</td><td>2</td><td>1</td></tr><tr><td>6</td><td>0</td><td>1</td><td>0</td><td>0</td><td>6</td><td>0</td><td>1</td><td>1</td></tr><tr><td>7</td><td>0</td><td>1</td><td>2</td><td>0</td><td>2</td><td>1</td><td>0</td><td>1</td></tr><tr><td>8</td><td>0</td><td>1</td><td>0</td><td>0</td><td>2</td><td>0</td><td>2</td><td>1</td></tr><tr><td>9</td><td>1</td><td>-</td><td>0</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>10</td><td>1</td><td>3</td><td>2</td><td>0</td><td>1</td><td>3</td><td>1</td><td>0</td></tr><tr><td>11</td><td>0</td><td>3</td><td>0</td><td>0</td><td>2</td><td>2</td><td>1</td><td>1</td></tr><tr><td>12</td><td>1</td><td>0</td><td>1</td><td>1</td><td>4</td><td>0</td><td>0</td><td>0</td></tr><tr><td>13</td><td>0</td><td>2</td><td>1</td><td>0</td><td>2</td><td>3</td><td>0</td><td>1</td></tr><tr><td>14</td><td>1</td><td>1</td><td>0</td><td>0</td><td>6</td><td>0</td><td>2</td><td>1</td></tr><tr><td>15</td><td>0</td><td>1</td><td>0</td><td>1</td><td>4</td><td>1</td><td>2</td><td>0</td></tr><tr><td>16</td><td>0</td><td>2</td><td>2</td><td>1</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>17</td><td>1</td><td>0</td><td>2</td><td>1</td><td>2</td><td>2</td><td>0</td><td>1</td></tr><tr><td>18</td><td>1</td><td>1</td><td>1</td><td>1</td><td>6</td><td>2</td><td>2</td><td>0</td></tr><tr><td>19</td><td>0</td><td>0</td><td>0</td><td>1</td><td>6</td><td>3</td><td>1</td><td>1</td></tr><tr><td>20</td><td>0</td><td>1</td><td>1</td><td>0</td><td>2</td><td>1</td><td>1</td><td>1</td></tr></table>

Note: F, G, H, I, J, K and M represent code of the STB modules.

## 4.4. The rule-composing algorithm

The proposed rule-composing algorithm is employed for the training data set to derive rules as follows:

Step 1. The feature set (F1 through F7) is defined. The target file consists of the first fifteen objects (i.e. Object 1 through Object 15).

Step 2. Object 9 contains five unknown values. Therefore, this object should be removed leaving only fourteen objects to form a training set.  
Step 3. Based on the reduct generation procedure, the candidate rules generated are as follows:

<table><tr><td>[1]</td><td>x</td><td>x</td><td>x</td><td>1</td><td>x</td><td>x</td><td>x</td><td>0</td><td>(5)</td><td>{1[1], 2[1], 4[1], 11[1], 14[1]}</td></tr><tr><td>[2]</td><td>x</td><td>4</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>0</td><td>(2)</td><td>{3[1], 4[1]}</td></tr><tr><td>[3]</td><td>x</td><td>x</td><td>x</td><td>x</td><td>2</td><td>x</td><td>x</td><td>1</td><td>(4)</td><td>{5[1], 7[1], 8[1], 10[1]}</td></tr><tr><td>[4]</td><td>x</td><td>x</td><td>x</td><td>x</td><td>6</td><td>x</td><td>x</td><td>1</td><td>(1)</td><td>{6[1]}</td></tr><tr><td>[5]</td><td>x</td><td>x</td><td>x</td><td>x</td><td>1</td><td>x</td><td>x</td><td>0</td><td>(1)</td><td>{9[1]}</td></tr><tr><td>[6]</td><td>x</td><td>2</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>1</td><td>(1)</td><td>{12[1]}</td></tr><tr><td>[7]</td><td>x</td><td>x</td><td>x</td><td>x</td><td>2</td><td>x</td><td>x</td><td>1</td><td>(1)</td><td>{12[1]}</td></tr><tr><td>[8]</td><td>x</td><td>x</td><td>x</td><td>x</td><td>6</td><td>x</td><td>x</td><td>1</td><td>(1)</td><td>{13[1]}</td></tr></table>

Since only the first and third rules are satisfied by the domain experts, so these two rules are selected. Remove Objects 1, 2, 4, 5, 7, 8, 10, 11 and 14 from the training set and go to Step 4.

Step 4. The first and third rules are selected, go to Step 5.

Step 5. Since not all of satisfied decision rules are determined, so go to Step 4.

Step 4. Objects 3, 6, 9, 12 and 13 are associated with unsatisfied rules and the remaining objects in the training set. Restore those objects and go to Step 3. Step 3. Based on the reduct generation procedure, the candidate rules from second iteration are as follows:

<table><tr><td>[1]</td><td>x</td><td>4</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>0</td><td>(1)</td><td>{3[1]}</td></tr><tr><td>[2]</td><td>x</td><td>x</td><td>x</td><td>x</td><td>6</td><td>x</td><td>x</td><td>1</td><td>(2)</td><td>{6[1], 13[1]}</td></tr><tr><td>[3]</td><td>x</td><td>1</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>1</td><td>(2)</td><td>{6[1], 13[1]}</td></tr><tr><td>[4]</td><td>0</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>1</td><td>(2)</td><td>{6[1], 12[1]}</td></tr><tr><td>[5]</td><td>x</td><td>3</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td><td>0</td><td>(1)</td><td>{9[1]}</td></tr></table>

Since only the second rule is satisfied by the domain experts, so this rules is selected. Remove Objects 6 and 13 from the training set and go to Step 4.

Step 4. The second rule is selected, go to Step 5. Step 5. Since all of satisfied decision rules are determined, so go to Step 6.

Step 6. Since three decision rules are determined so stop and output the results (see below).

<table><tr><td>[1]</td><td>x</td><td>x</td><td>x</td><td>1</td><td>x</td><td>x</td><td>x</td><td>0</td></tr><tr><td>[2]</td><td>x</td><td>x</td><td>x</td><td>x</td><td>2</td><td>x</td><td>x</td><td>1</td></tr><tr><td>[3]</td><td>x</td><td>x</td><td>x</td><td>x</td><td>6</td><td>x</td><td>x</td><td>1</td></tr></table>

Three rules have been derived for the training set by applying the rough set based algorithm. The derived rules are depicted in a “IF condition is satisfied THEN outcome is hold” format. For example, rule 1 is illustrated as “x x x 1 x x x 0.” This simply means if the value of the fourth feature is “1” then outcome is known as “0.” Note that those rules cannot be guaranteed to be useful since the accuracy of each rule is not fathomable. Each derived rule is required to be examined through the rule-validation procedure. The procedure is presented next.

## 4.5. The rule-validation procedure

Then, the rule-validation procedure is applied to the validation data set to validate the derived rules as follows:

Step 1. Compare the 1st decision rule to all objects (Objects 16 to 20). Objects 16 and 18 are matched with the rule and go to Step 2.

Step 2. Compare the 2nd decision rule to all objects. Objects 17 and 20 are matched with the rule and go to Step 2 again.

Step 2. Compare the 3rd decision rule to all objects. Object 19 is matched with the rule while Object 18 isn't matched; go to Step 3.

Step 3. After calculating accuracy of each rule, the results are as follows:

The accuracy of rule 1 is equal to 100%, since 2/ (2+0)=100%

The accuracy of rule 2 is equal to 100%, since 2/ (2+0)=100%

The accuracy of rule 3 is equal to 50%, since 1/(1 + 1)=50%

Since accuracy of rule 1 and rule 2 are 100%, which is greater than the threshold value (60%). Therefore, rule 1 and 2 are selected. Go to Step 4. Rule 3 is removed.

Step 4. Stop and output the results.

The results are as follows:

Rule 1: If the condition feature F4 = 1, Then the outcome feature O = 0. This rule validated with 100% accuracy.

Rule 2: If the condition feature F5 = 2, Then the outcome feature O = 1. This rule validated with 100% accuracy.

As shown above, only two rules are selected out of three original rules since the accuracy of the first two rules (rule 1 and rule 2) are higher than the threshold value. Note that the determination of the threshold value is dependant on the problem domain and decision maker's preference. Normally, the higher value is favored.

In this example, the defective module audio DAC is identified and the specific type of the audio DAC module (e.g., type 2) is recognized. It is also concluded that F4 is insignificant to heat dissipation, while F5 is significant to heat dissipation. The final derived rules reveal valuable design information and are able to support modular design of the STB.

## 5. Sharing design knowledge in a distributed environment

In this section, the conceptualized approach is carried out through the knowledge management of product design (KMPD) applets and package. The KMPD applets and package are constructed to discover and prune the rules in Web-based environments. Decision makers (clients) use their browsers to input the requirements, and then run the KMPD applets and package through the World Wide Web (WWW) regardless of what platforms are used (Fig. 5). The WWW is potentially useful for remote decision making since it allows the disparate functions that are involved with remote decision making in order to share data relatively easily.

Fig. 6 illustrates how the designer interacts with the Web server, by using a Web client (HTTP-based browser), to establish the DwM application. The connection between the client and server is through either over the Internet or a protected intranet to emphasize that the two architectures are interchangeable.

Referring to Fig. 6, the Steps 1 through 8 are followed to understand how a user session is handled. In Step 1, the designer, at the client browser, specifies the HTTPbased URL located on the remote Web server. Step 2 causes the synthesis job HTML page to be sent from the Web server to the client browser. The HTML page contains the references of the KMPD applets composed of JavaBeans. In Steps 3 and 4, the client browser downloads the KMPD applets and loads them into memory. The key new capability these KMPD applets have is that they can communicate directly with other software components, either elsewhere in the client browser or on the Web server because they do not need to launch a new HTTP request or open a new Web page. All of the various applets communicate directly via CORBA or DCOM. Thus in Step 5, the client software component calls the server software component — the KMPD package, executes the algorithm and prune procedure, and determines the desired modules. In Step 6, the KMPD package also makes further calls to the database machines in which design data warehouses are located, including database engines (warehouses). In Step 7, the database engine returns the design rules and module information to the KMPD package, and in Step 8, the information is transferred to the client browser.

![](/api/attachments/2UG5GNVE/fulltext/images/e4cf8b085d6791cad4bfc9c74fba378193017903739e4cb773ade808e34c62e7.jpg)  
Fig. 5. The implementation environment of the approach through the WWW.

These steps can be repeated at the request of the end user, for as many times and as long as the module synthesis job of the HTML page is satisfied. The user does not think of the screen as an HTML page, but rather as a single graphical user interface that is controlling a coherent session. This ability to have a single page act as a comprehensive user interface, with many possible responses to the user, and to have the single page mediate the complete user session is a huge leap forward in interactivity using the Web browser model.

The basic HTTP protocol remains as a stateless protocol. In other words, HTTP by itself does not provide support for a user session. To provide for a continuous coherent session, the Web server must rely on a session cookie that is provided by the client browser each time a request is made between machines. Each Web server application requires its own cookie to maintain a coherent session, and thus the Web server requires the client browser to assemble and keep this cookie so that it can be revealed every time the client and the server communicate.

![](/api/attachments/2UG5GNVE/fulltext/images/78c9bf4f1dbb0ac8e4ce4de5fe7ce08ed6453feabc951938ef189443049b8954.jpg)  
Fig. 6. The browser–server HTTP session.

![](/api/attachments/2UG5GNVE/fulltext/images/8323600d9d68fc1bee13d5b544f6334eb35797e5fac51ff5ca053f45d53493f5.jpg)  
Fig. 7. Selection of input features and a subject.

The system allows users to view the design operation records over a specific time period, or can be queried by a particular module in the design data warehouse. The design rules are inducted through the rough set based approach. Fig. 7 shows selection of input features and a subject.

Through the KMPD system, the users are able to model modular design knowledge, perform design rule induction, and share design knowledge in distributed environment effectively. The KMPD system is particularly beneficial for remote design teams since it allows the heterogeneous functions that are involved in the design process and it is regardless of what platforms are used. Moreover, the cost-effective ratio of using this system is consequentially lower than the conventional design approach according to company's empirical study in Taiwan and improvement of design operations and information technology.

User/Customer feedback of the KMPD system is also collected and measured with five indices in this case study: (1) customer's satisfaction, (2) customer's complaints, (3) effectiveness, (4) active usefulness, and (5) availability. The results indicate the significant fruits of this approach, where most percentages from reviewers are positive with the KMPD system. For example, 82% of reviewers are satisfied with KMPD system; 84% of them have no complaints; 89% of them perceive the KMPD system is effective and 92% of them respond usefulness of the KMS. Therefore, the proposed approaches are valid in a similar modular product design.

## 6. Conclusions

This paper focuses on a case study of modular design of the STB and knowledge externalization of modular product design, which creates and shares the design rules to increase the effectiveness/efficiency of design processes. The proposed solution approach modeled each synthesis job, which consisted of numerous design operations, as DwM by using module algebra. The formulation of the module algebra represented the design knowledge explicitly. Historically, design operations and the module dimensions, were stored in the design data warehouse, which was constructed based on dimensional modeling. The report and counts of a particular module were produced by dragging and dropping from the design data warehouse. The rough set based approach is adopted to derive rules and develop an algorithm to validate the rules from the data repository.

Design engineers are able to apply those elicited design rules in order to facilitate the modular design of the STB with consideration of heat dissipation. For example, highly accurate rules should be used to distinguish between superior and overheated STBs. Additional developments of the algorithms and largescale testing will be the ultimate proof of the prediction accuracy for modular design of the STB. Moreover, quality engineers should focus their efforts on the control of significant features. Specifically, conditions of the features (factors) need to be maintained, such as which ones produce the overheating, and become the primary focus. It is concluded that the RST is best suited for analysis of imprecise (noisy) data; this ability at the pre-processing stage could include removal of these data and methods of averaging for missing items of data, etc. RST also avoids the costly experimentation process involved in conducting STB heat dissipation analysis. With the objective of providing adapted design rules and shared design knowledge in a distributed environment, the KMPD system is implemented.

Externalizing and sharing design knowledge is definitely a fruitful area for further multidisciplinary work. Moreover, applying the agent technology to the product design is desirable and needs further investigation. For example, an intelligent mechanism is required to be developed for experts to perform robust configurations for confirmation of the inductive rules.

## Acknowledgements

This research has been partially supported by funds from the National Science Foundation (Grant No. DMI-0116515) and the Nation Science Council of Taiwan (NSC 94-2416-H-260-004).

## References

[1] Amit Basu, Robert W. Blanning, Metagraphs in workflow support systems, Journal of Decision Support Systems 4 (1) (1988) 17–25 March.

[2] H. Benoit, Digital Television MPEG-1, MPEG-2 and Principles of the DVB System, John Wiley & Sons, New York, NY, 1997.

[3] P. Chiang, A highly integrated decoder for the set top box, Consumer Electronics, ICCE, Digest of Technical Paper, 1997.

[4] J. Corbett, M. Dooner, J. Meleka, C. Pym, Design for Manufacturing: Strategies, Principles, and Techniques, ddison Wesley, New York, 1991.

[5] W. Davidow, M. Malone, The Virtual Corporation, Harper Collins, New York, 1992.

[6] M.A.F. De Souza, M.A.G.V. Ferreira, Designing reusable rulebased architectures with design patterns, Expert Systems with Applications 23 (4) (2002) 395–403.

[7] J. Fandrianto, Single chip MPEG2 decoder with integrated transport decoder for set-top box, Compcon '96, Technologies for the Information Superhighway Digest of Papers, Santa Clara, CA, USA, 1996, pp. 469–472.

[8] M.E. Jones, I.-Y. Song, Dimensional modeling: identification, classification, and evaluation of patterns, Decision Support Systems (in press).

[9] J. Han, M. Kamber, Data Mining: Concepts and Techniques, Morgan Kaufmann, San Francisco, 2000.

[10] D.J. Hand, H. Mannila, P. Smyth, Principles of Data Mining (Adaptive Computation and Machine Learning), MIT Press, Cambridge, MA, 2001.

[11] C.C. Huang, A multi-agent approach to collaborative design of modular products, Concurrent Engineering, Research and Applications 12 (1) (March 2004) 39–47 SCI (0.418).

[12] C.C. Huang, C.M. Kuo, Transformation and searching of semistructured knowledge in organizations, Journal of Knowledge Management 7 (4) (2003) 106–123.

[13] C.C. Huang, A. Kusiak, Modularity in Design of Products and Systems, IEEE Transactions on Systems, Man and Cybernetics. Part A. Systems and Humans 28 (1) (1998) 66–77.

[14] C.C. Huang, W.Y. Liang, A formalism for designing with modules, Journal of the Chinese Institute of Industrial Engineers 18 (3) (2000) 13–20.

[15] Y.H. Huang, Y.C. Chang, C.S. Wu, C.H. Wu, Design of an MPEGbased set-top box for video on demand services, Acoustics, Speech, and Signal Processing. ICASSP-95., 1995 International Conference on, vol. 4, Detroit, MI, USA, IEEE Press, Piscataway, NJ, USA, 1995, pp. 2655–2658.

[16] N.R. Jennings, J. Corera, I. Laresgoiti, E.H. Mamdani, F. Perriolat, P. Skarek, L.Z. Varga, Using ARCHON to develop real-word DAI applications for electricity transportation management and particle accelerator control, IEEE Expert 6 (5) (1996) 64–70.

[17] P.T. Kidd, Agile Manufacturing: Forging New Frontiers, Addison Wesley, New York, 1994.

[18] R. Kimball, L. Reeves, M. Ross, W. Thornthwaite, The Data Warehouse Lifecycle Toolkit, John Wily & Sons, New York, 1998, p. 139.

[19] A. Kusiak, Rough set theory: a data mining tool for semiconductor manufacturing, IEEE Transactions on Electronics Packaging Manufacturing 24 (1) (2001) 44–50.

[20] A. Kusiak, C.C. Haung, Development of modular products, IEEE Transactions on Components, Packaging, and Manufacturing Technology. Part A 19 (4) (1996) 523–538.

[21] A. Kusiak, T.L. (Bill) Tseng, Data mining in engineering design: a case study, Proceedings of the 2000 IEEE International Conference on Robotics & Automation, San Francisco, CA, 2000, (April 24–27 2000).

[22] A. Kusiak, J.A. Kern, K.H. Kernstine, T.L. (Bill) Tseng, Autonomous decision-making: a data mining approach, IEEE Transactions on Information Technology in Biomedicine 4 (4) (2000) 274–284.

[23] R.C.-W. Kwok, J.-N. Lee, M.Q. Huynh, S.-M. Pi, Role of GSS on collaborative problem-based learning: a study on knowledge externalization, European Journal of Information Systems 11 (2) (2002) 98–107.

[24] R.N. Langlois, P.L. Robertson, Networks and innovation in a modular system: lessons from the microcomputer and stereo component industries, Research Policy 21 (4) (1992) 297–313.

[25] J. Lim, X. Guoa, A study of group support systems and the intergroup setting, Decision Support Systems (in press).

[26] G.F. Luger, W.A. Stubblefield, Artificial intelligence: Structures and Strategies for Complex Problem Solving, Benjamin Cummings, CA, 1993.

[27] J.L. Nevins, D.E. Whitney, Concurrent Design of Products & Processes: A Strategy for the Next Generation in Manufacturing, McGraw-Hill, New York, 1989.

[28] Ikujiro Nonaka, Hirotaka Takeuchi, Katsuhiro Umemoto, A theory of organizational knowledge creation, International Journal of Technology Management 11 (7–8) (1996) 883–895.

[29] G. Pahl, W. Beitz, in: K. Wallace (Ed.), Engineering Design: A Systematic Approach, Springer-Verlag, The Design Council, London, UK, 1988.

[30] Z. Pawlak, Rough Sets, Dordrecht, Kluwer Academic Publishers, Netherlands, 1991.

[31] M.A.S. Poz, J.E. Aedo-Cobo, W.A.M. Van-Noije, M.K. Zuffo, A simple RISC microprocessor core designed for digital set-topbox applications, application-specific systems, architectures, and processors, 2000, Proceedings. IEEE International Conference on, 2000, Boston, MA, USA, IEEE Press, Piscataway, NJ, USA, 2000, pp. 35–44.

[32] D. Rösner, B. Grote, K. Hartman, B. Höfling, From natural language documents to sharable product knowledge: a knowledge engineering approach, in: U.M. Borghoff, R. Oareschi (Eds.), Information Technology for Knowledge Management, Springer, New York, 1998.

[33] R. Roy, Introduction: meaning of design and innovation, in: R. Roy, D. Wield (Eds.), Product Design and Technological Innovation, Open University Press, Bristol, PA, 1986.

[34] Ron. Sanchez, Strategic flexibility, firm organization, and managerial work in dynamic markets: a strategic options perspective, Advances in Strategic Management 9 (1993) 251–291.

[35] S.W. Sanderson, V. Uzumeri, Strategies for new product development and renewal: design-based incrementalism, Work ing Paper, Center for Science and Technology Policy, Rensselae Polytechnic Institute, Troy, New York, 1990.

[36] Peter C. Scott, Requirements analysis assisted by logic modelling, Journal of Decision Support Systems 4 (1) (March 1988) 17–25.

[37] N. Sohi, P.G. Gulak, A multi-standard set-top box channel decoder, Signal Processing Systems, 2000. SiPS 2000, 2000 IEEE Workshop on, Lafayette, LA, USA, 2000, pp. 295–304.

[38] T.L. (Bill) Tseng, Quantitative Approaches for Information Modeling, Ph.D. Dissertation, University of Iowa (1999).

[39] E. Turban, J.E. Aronson, Decision Support System and Intelligent System, Prentice-Hall, New Jersey, 1998.

[40] K.T. Ulrich, S.D. Eppinger, Product Design and Development, McGraw-Hill, New York, 1995.

[41] K. Ulrich, K. Tung, Fundamentals of product modularity, in: A. Sharon (Ed.), Issues in Design Manufacture/Integration 1991, vol. 39, ASME, New York, DE, 1991, pp. 73–79.

[42] N.V. Valkenburgh, Basic Electricity, Prompt Publication, New York, 2000.

[43] W. Ward, J.F. Liker, J.J. Cristiano, D.K. Sobek, The second Toyota paradox: delaying decisions can make better cars faster, Sloan Management Review 36 (3) (1995) 43–61.

[44] Dongming Xu, Huaiqing Wang, Intelligent agent supported personalization for virtual learning environments, Journal of Decision Support Systems 42 (2) (November 2006) 825–843.

![](/api/attachments/2UG5GNVE/fulltext/images/a45e4fb751341c10d51b383257166c6362d356f40a65f3c172ac6fa7d2d67ff9.jpg)

Tzu-Liang (Bill) Tseng received his M.S. degree in industrial engineering from the University of Wisconsin at Madison in 1995, and his Ph.D. degree in industrial engineering from the University of Iowa, Iowa City, in 1999. He is an Assistant Professor of the Department of Industrial Engineering, The University of Texas at El Paso. He has published papers in journals sponsored by various societies. His current research focuses on data mining, knowledge management, bio-infor-

matics, decision sciences and applications in manufacturing. Dr. Tseng is a Certified Manufacturing Engineer from the Society of Manufacturing Engineers (SME) since 2002. He is also a Member of IIE, SME, INFORMS, and SPIE and is actively involved in several consortia activities.

![](/api/attachments/2UG5GNVE/fulltext/images/79027c024b0951f07d67b69f97bc869b37277f6843593b7d36e157aa749eb75c.jpg)

Chun-Che Huang received his Ph.D. degree in Industrial Engineering from the University of Iowa, Iowa City, and his M.S. degree in Operations Research from Columbia University, New York, NY. He is a Professor and Chairman in the Department of Information Engineering, National Chi-Nan University, Taiwan and a director of the Laboratory of Intelligent Systems and Knowledge Management (ISKM Lab). He is interested in intelligent systems, development of products

and systems, knowledge management, and supply chain management. He has published research papers in journals sponsored by various societies.

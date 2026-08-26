---
otero_id: 17319
otero_key: "GB63MC9S"
title: "Modeling by analogy"
authors: "Ting-Peng Liang; Benn R. Konsynski"
year: "1993"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)90026-y"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Modeling by analogy Use of analogical reasoning in model management systems \*

Ting–Peng Liang

Purdue University, West Lafayette, IN 47907, USA

Benn R. Konsynski

Harvard University, Boston, MA 02163, USA and Emory University, Atlanta, GA30322, USA

Models in business and management processes often draw on analogs for explanation in formulation. The basic principles of modeling by analogy are discussed and issues related to the support of this modeling approach through the augmentation of functions provided by model management systems (MMS) are examined. The majority of recent research in MMS focuses on understanding and supporting model formulation from a 'blank sheet' approach. In reality, however, human modelers frequently use analogical thinking to overcome cognitive limitations. Other factors such as time pressure and limited opportunity for concentration drive decision makers to seek analogous situations to accelerate the model building process. Given that one goal of MMS is to improve modeling productivity, there is a significant opportunity to leverage analogical skills in an MMS that supports model building through a process of support for analogical reasoning.

Keywords: Analogical reasoning; Model management systems; Decision support systems.

## 1. Introduction

Recently, significant attention has focused on the development of a computer-based modeling environment, called model management systems (MMS) or integrated modeling environment [20]. For our purposes, a model is a set of mathematical equations representing a real world problem. Models are frequently used to support decision making by deriving the optimum solution or simulating various scenarios. The primary goal of MMS is to facilitate the development and utilization of these models [15,44]. Previous research has investigated important issues for developing MMS such

![](/api/attachments/GB63MC9S/fulltext/images/085fb6b835f56e9cdf48828423979a83e305bcfd661347e4ca58f7bfa5b6b080.jpg)

Ting-Peng Liang is an Associate Professor of Information Systems at the Krannert Graduate School of Management of Purdue University. He received his Ph.D. in Information Systems from the University of Pennsylvania and MBA from National Sun Yat-sen University in Taiwan, ROC. Prior to joining Purdue University, he was an Assistant Professor at the University of Illinois at Urbana-Champaign. Dr. Liang has published in journals such as Management Sci ence, Operations Research, MIS Quarterly, Decision Science, among others. His primary research interests include model management, machine learning, knowledge acquisition, and the integration of artificial intelligence, statistical, and operations research methods.

Benn R. Konsynski is the Robert Craft Professor of Business Administration and Area Coordinator for Decision and Information Analysis. He arrives at Emory University following six years on the faculty at the Harvard Business School. Prior to arriving at HBS, he was a professor at the University of Arizona, where he was the co-founder of the university's multimillion dollar group decision support laboratory. He holds a Ph.D. in Computer Science from Purdue University. Professor Konsynski specializes in issues of information technology in relationships across organizations. He has published in various journals such as Communications of the ACM, Harvard Business Review, MIS Quarterly, Decision Support Systems, and various IEEE Transactions. He also serves on the editorial boards for many research journals.

is model representation, model integration, model formulation, and the development of modeling languages. For example $^{1}$ , Blanning [4,6,7] studied how relational and entity-relationship models can be used to represent and manipulate models. Dolk and Konsynski [13] developed a frame-based model abstraction technique. Elam, Henderson and Miller [16] proposed a network-based model representation scheme. Klein [24] and Liang [32–34] studied mechanisms for constructing larger models by integrating smaller ones. Geoffrion [19] developed a structured modeling language for model specification. Krishnan [29] presented a language for production and inventory modeling. Muhanna and Pick [41] adapted the systems concept to model management. Murphy and Stohr [42] explored the formulation of linear models.

In addition to this existing line of work, the authors believe there is a fruitful opportunity for research focused on exploring the potential of modeling by analogy. Analogical thinking is a process that has proven useful in solving scientific and other problems for a long time. In fact, it is one of the fundamental capabilities human beings use to alleviate cognitive limitations such as limited short-term memory and bounded rationality $[22,45,46]$ . In a model construction process, analogical thinking plays a key role in helping model builders construct relationships between variables and in reducing the need of repetitive exhaustive rial. It has been widely used in practice. For example, a recent empirical study found that human modelers often tried to identify the type of problems before actually developing models. Once the problem type was recognized, modeling became easier and more productive $[43]$ .

The purpose of this paper is to highlight issues related to modeling by analogy and to explore how analogical reasoning can be supported by, and incorporated in, model management systems. There are two major motivations for incorporating this capability in MMS. First, because human modelers frequently use modeling by analogy to approach new problems, MMS must support it in order to improve productivity of model construction and modification. Second, the incorporation of modeling by analogy allows model storage to be more efficient (“space and search”). Under such an approach, the model base does not need to store all model instances. Only templates are stored. New model instances can be formulated from the templates analogically. In MMS, as in humans, the use of templates and analogues simplifies the ‘storage’ and ‘search’ costs involved in using models in the model base.

The remainder of the paper is organized as follows. First, concepts and definitions of model similarity and the process of modeling by analogy are introduced. Then, model management functions and a framework supporting analogical modeling are presented. Finally, issues for future research are identified and discussed.

## 2. Problem similarity and modeling by analogy

An analogy is “a problem of the form A is to B as C is to D (A:B::C:D), where, in most situations, the last term is omitted and must be filled in, selected from among answer options, or confirmed in a true-false situation” [46]. Analogical reasoning is a process by which D is determined by some known properties among A, B, and C. It is a core process of thinking [2] and has been studied extensively in artificial intelligence and cognitive science. Modeling by analogy (or called analogical modeling) is a process by which analogical reasoning is adopted for model construction. In other words, a model is constructed for a problem based on the similarity of the problem to previously solved problems. As illustrated in fig. 1, model B is developed based on a known model for problem A and the similarity between problems A and B. A combination of problem A and model A serves as a source for analogical modeling, whereas problem B and model B are the target.

![](/api/attachments/GB63MC9S/fulltext/images/3378f8a8143cfac27394b983f41463aa64eacf71c775f2cb1c632b6235213e72.jpg)  
Fig. 1. Modeling by analogy.

Models are representations of real situations. As such, model similarity exists in almost every problem situation, modeling by analogy is very useful in understanding the process of model construction and improving the productivity of model formulation. In physics, for example, the Newton's Law of Gravity and Coulomb's Law have the same functional form, $F = K(X_1X_2) / d^2$ , where $K$ is a constant, $F$ is the force between two objects, $d$ is the distance between two objects, and $X_{1}$ and $X_{2}$ are masses and charges of the two objects in Newton's Law and Coulomb's Law, respectively. In management science, process selection and transportation models are similar in many aspects, although they deal with two different problems. Therefore, exploring model similarity and examining how models can be built analogically are important areas for research in model formulation and management.

There are two alternative ways in which models can be constructed based on an analysis of similarity. First, a model may be an instance of a more general one. For example, a product-mix model of two products and three resources is an instance of the general product-mix model of m products and n resources, where m and n can be instantiated with certain values. In this case, both models have an identical structure and the latter is a template for the former. Modeling becomes a process of finding a proper template for instantiation. We call this modeling by template. Second, two models may be similar but not completely identical structurally. For example, a process selection model and a transportation model have certain common characteristics, but they are not identical. In this case, experience obtained from developing one model is useful in developing the other, but certain adaptation and modification are essential. We call this modeling by analogy or analogical modeling. In fact, modeling by template is a special case of modeling by analogy, because a template can be considered as a perfect analogue for the new model.

It is clear that in order to accomplish our objective, a key issue in modeling by analogy is to identify similarity. How do we know, before learning Coulomb's Law, that the problem of the attractive or repulsive force between two charged particles is similar to the problem of gravity? What is the similarity between the process selection and transportation problems? Although many different theories of analogical reasoning have been developed in cognitive science, they define similarity in two dimensions: Entity and structure [49]. In other words, problems may be similar in the entities they consist and/or the way those entities are related.

Problem entities are usually described by a set of attributed. For quantitative models, relationship between entities may be further divided into two levels: Qualitative structures and quantitative functions. For example, a transportation problem that a firm ships merchandise from plants to customers includes three entities: Plant, customer, and route. Each plant has a supply capacity. Each customer has a certain demand. Each route has an estimated shipping cost and flow quantity. The relationships among these entities and their attributes can be represented as graphical structures such as Geoffrion's elemental and generic structures [18]. In addition to rendering the links qualitatively in structures, a computer-executable model also requires the functional form such as summation or multiplication associated with a particular link to be specified. For the purpose of developing quantitative models analogically, therefore, problem similarity can be decomposed into entity, structural, and functional similarities [35].

Entity similarity indicates that two entities in different problems have similar properties. Because entities are the basic components of a problem, no analogy may exist unless entity mappings between problems can be established. In the analogy between the force of charged particles and the gravity, for instance, each charged particle matches an object, and the link between particles (a compound entity in the structured modeling terminology) matches the link between two objects. In the analogy between the process selection and transportation problems, products, processes, and their links in the former may match plants, customers, and routes in the latter (see the Appendix for representations of the problems).

A key to matching entities in different problems is to measure entity similarity. Because each entity is represented by its associated attributes, entity similarity can be measured by their attributes. For example, a metric adapted from Tversky's well-known Contrast Model [48] was developed for measuring entity similarity in Liang [36].

$$
\mathrm{S} (E _ {1}, E _ {2}) = \frac {1}{m} \sum_ {i} \partial_ {i}.
$$

This metric suggests that entity similarity be assessed based on attributes. Each common attribute receives one point and a different attribute receives zero for $\partial_{i}$ . The overall similarity score between $E_{1}$ and $E_{2}$ is the summation of $\partial_{i}$ divided by the total number of attributes compared (m). The higher is the overall score, the stronger are the entities similar. Figure 2 illustrates the entities and their attributes in the problem selection and transportation problems. In the Figure, ‘U’ stands for unspecified, the capital letters stand for specified but unknown, and lower-case letters stand for known values. The ROOT entity is a common parent for all entities. Because there are multiple possible matches, we have to calculate scores for all of them and choose one with the highest score. In this example, the optimum match is the following (which includes only one mismatched attribute—the production quantity of each process U versus the flow to each customer, $d_{i}$ ).

<table><tr><td>Process selection</td><td>Transportation</td></tr><tr><td>ROOT</td><td>ROOT</td></tr><tr><td>PRODUCT</td><td>PLANT</td></tr><tr><td>PROCESS</td><td>CUSTOMER</td></tr><tr><td>LINK(P, P)</td><td>ROUTE</td></tr></table>

Structural similarity indicates that two sets of matched entities have similar relationships. This can be measured by the isomorphism of two structures. Two structures are said to be isomorphic if there exists a one-to-one mapping function for all nodes and arcs in two structures. Two model structures are said to be structurally similar if they are isomorphic and matching entities are similar. In some situations, two structures may be partially similar. That is, parts of the structures are isomorphic. In this case, these two models have partially structural similarity.

When there are multiple partially similar models, a metric similar to the one for measuring entity similarity is necessary to determine the degree of structural similarity. Because structures can be represented as arcs linking nodes, given a set of entity mappings, similarity can be measured by the number of arcs properly matched, as follows

a) Process Selection Problem

<table><tr><td>ATTRIBUTES ENTITIES</td><td>TOTAL COST</td><td>UNIT COST</td><td>TOTAL CONSUMPTION</td><td>UNIT CONSUMPTION</td><td>PRODUCTION QUANTITY</td></tr><tr><td>ROOT</td><td>Z</td><td>U</td><td>U</td><td>U</td><td>U</td></tr><tr><td>PRODUCT</td><td>U</td><td>U</td><td>U</td><td>U</td><td>di</td></tr><tr><td>PROCESS</td><td>U</td><td>U</td><td>U</td><td>U</td><td>U</td></tr><tr><td>RESOURCE</td><td>U</td><td>U</td><td>bk</td><td>U</td><td>U</td></tr><tr><td>LINK (P,P)</td><td>U</td><td>cij</td><td>U</td><td>U</td><td>Xij</td></tr><tr><td>LINK (P,P,R)</td><td>U</td><td>U</td><td>U</td><td>aijk</td><td>U</td></tr></table>

b) Transportation Problem

<table><tr><td>ATTRIBUTES ENTITIES</td><td>TOTAL COST</td><td>UNIT COST</td><td>FLOW</td></tr><tr><td>ROOT</td><td>Z</td><td>U</td><td>U</td></tr><tr><td>PLANT</td><td>U</td><td>U</td><td> $s_i$ </td></tr><tr><td>CUSTOMER</td><td>U</td><td>U</td><td> $d_j$ </td></tr><tr><td>ROUTE</td><td>U</td><td> $c_{ij}$ </td><td>X</td></tr></table>

Fig. 2. Entities and attributes.

a) Process Selection Problem  
![](/api/attachments/GB63MC9S/fulltext/images/fa985d3c070ce2cd7a6426fd3244e74792b195b8ba138178d29910ac7e3c6db2.jpg)

b) Transportation Problem  
![](/api/attachments/GB63MC9S/fulltext/images/1c5e1ed3d6d7c29852ba54ed02a07db97bf61ff0f8cddfae1385009fc485953e.jpg)  
Fig. 3. Entity structure.

$$
\mathrm{S} \left(\mathrm{ST} _ {1}, \mathrm{ST} _ {2}\right) = \frac {1}{n} \sum_ {j} \partial_ {j},
$$

where, S (ST $_{1}$ , ST $_{2}$ ) is the overall similarity score of two structures, $n$ is the total number of arcs in the target structure, $\partial_{j}$ is the score for each arc mapping. $\partial_{i}$ is one if there exists a proper match and zero otherwise. For example, the entity graphs in figs. 3(a) and 3(b) have a substructure similarity score of 1.0, if the entity mappings are ROOT—ROOT, PRODUCT—PLANT, PROCESS—CUSTOMER, and LINK(P, P)—ROUTE. Graph 3(b) is isomorphic to a subset of graph 3(a). The similarity score is 0.75, if the entity mappings are ROOT—ROOT, LINK(P, P)—PLANT, RESOURCE—CUSTOMER, and LINK(P, P, R)—ROUTE (note that there is no arc between ROOT and LINK(P, P) in graph 3(a) to match the arc between ROOT and PLANT in graph 3(b)). Although the sample graphs consist of entities only, the metric is applicable to any kind of structures including the elemental and generic graphs in structured modeling because it only considers mappings rather than the nature of nodes. Two isomorphic structures indicate that similar causal relationships of nodes exist. Structural similarity, however, does not guarantee functional relationships such as summation or multiplication to be exactly the same. Another metric that is also useful for identifying structural similarity is the convergence-divergence (CD) measure described in [28] to be discussed in Section 3.

Functional similarity indicates that two models have similar functional forms. Two equations are said to be similar if they include the same set of functors. For example, $Y = \sum_{i=1}^{2} X_{i}$ is similar to $Z = \sum_{j=1}^{3} T_{j}$ because their function $\sum$ is the same. They are, however, dissimilar to $W = S_{1} \cdot S_{2}$ , whose functor is multiplication. Two isomorphic structures may be functionally different. For instance, two models, “total cost = shipping cost + purchasing cost” and “total cost = unit cost · quantity,” have an isomorphic structure, but are functionally dissimilar. Functional similarity can be used to determine whether two models are in the same model class. Therefore, it should be a binary measure, i.e., either true or false. If two models are functionally similar, then they are in the same class and can be formulated from the same template. They are dissimilar otherwise.

Since some models may include a combination of several equations (e.g., linear programs), it is possible that two models have a partial functional similarity, which means that a part of a model is similar to a part or the whole of the other one. When detecting functional similarity, algebraic rules such as the distributive law can be applied. If there exists an algebraic transformation that converts an equation to a form the same as the other, then we said these two equations are functionally similar.

In summary, two models may be similar in their entities, structures, or functions. A modeling process usually includes constructing complete structures and functions from entities, partial structures, and partial functions. Therefore, modeling by analogical can be further defined as a process by which the complete model structure and functions of a new problem are constructed from its entities, partial structures, and partial functions based on identified entity, structural, and functional similarities to existing models.

A typical analogical modeling process includes several steps. First, problem features necessary for comparing problem similarity need to be identified. These features serve as the basis for determining similarity. For example, the entities and attributes shown in fig. 2 can be used to compare problem similarity. Second, a similar problem whose model is known must be located and retrieved. This model serves as a source for analogical formulation. Unless such a model is found, no further analysis is possible. The degree of similarity can be measured by the metric previously presented. The one with the highest similarity score is considered the best analogue. Third, after a source is found, feature mappings between the source and target problems must be established. Fourth, once the mappings are determined, a new model can be formulated by replacing elements in the source with their corresponding elements in the target. This transfer process typically only involves substitution. Finally, the formulated model must be evaluated for consistency and completeness, and repaired if necessary [36]. A prototype system called ANALOGY that applies the above similarity measures to perform analogical modeling has been developed. The representation of the product-mix and process selection problems and a sample session showing the process by which similarity scores are calculated and the process selection model is formulated are illustrated in the Appendix.

## 3. Complexity-based similarity measures

A key issue in incorporating analogical reasoning capabilities in MMS is the complexity of the process. The identification of a proper analogue requires that a number of potential candidates be examined and the most proper one be selected. Complexity measured can be used to determine the complexity of the process. In addition, because similar problems may have similar structural complexity, problem complexity measures can also be used as a good index for screening unlikely candidate and finding for proper analogues.

In [28] problem complexity is divided into three types: volume, distribution, and location. Volume is a measure of the size of an entity (please note that the term “entity” here is equivalent to a problem and is different from our previous definition of entities in a problem). Distribution is a measure of the interrelatedness of components within an entity. It addresses the structural complexity of an entity. Location is a measure of the inter-entity interface complexity for a given entity. It deals with the relative functional/conceptual distance between entities. If we adapt these measures to our definitions of entities, structures, and functions, we can define three types of complexities in analogical modeling. First, volume complexity of a problem indicates the number of entities and attributes included in a problem. Second, distribution complexity of a problem indicates the number of connections existing among the entities. Finally, location complexity indicates how a particular problem is connected to other problems by different types of variables (e.g., how many parameters and how many unknown variables).

In order for these complexities to be useful, measurement metrics are necessary. Based on the metrics proposed in [28], we can develop an effort metric to measure volume complexity, a convergence-divergence (CD) metric to measure volume complexity, a convergence-divergence (CD) metric to measure distribution complexity, and a linear metric to measure location complexity.

Volume complexity reflects the number of entities and attributes in a problem. The more entities and attributes, the more effort is necessary to formulate a model for the problem. Based on a model proposed by Halstead (1977) the effort required for developing a software is $E = V^{2}/V^{*}$ , where V is the minimum number of bits necessary to represent a problem and $V^{*}$ is the minimum potential volume of the problem. For our purposes, V and $V^{*}$ are measured as follows $V = (N) \log_{2}(N)$ ,

where $N =$ total number of entities and attributes $V^{*} = (2 + M)\log_{2}(2 + M),$

where M = total number of input/output parameters.

Distribution (structural) complexity can be measured by the degree of connectivity of its elements, which include the arcs entering a node and the arcs leaving a node. We call the number of entering arcs of a node the convergence measure (C) and the number of outgoing arcs the divergence (D) measure. The first-order complexity of a node can then be measured as a product of these two measures (i.e., $C \cdot D$ ) and the structural complexity of a problem with i entities can be measured as $Z = \sum_{i} C \cdot D$ .

Location complexity shows the inter-problem communication behavior of a problem. This can be measured by the types of attributes included in a problem such as whether the values is known or unknown and what are the units associated with attributes. If we give each type of attributes k a weight $w_{k}$ , then the location similarity can be measured by

$$
\sum_ {k} w _ {k} \cdot e _ {k},
$$

where $e_{k}=1$ if there exists a k type attributes and 0 otherwise.

Given these three measures, we can assign to each of them a relative importance weight, $w_{p}$ , and calculate their weighted sum as a global complexity measure. This global complexity measure can then be used to compare problem similarity. If there is more than one existing problem that may be similar to the new problem, we can calculate their global complexity score and choose the one whose score is closest to the new problem as the best analogue and derive models for the new problem analogically. A prototype called DYCOM implements the complexity metrics described above.

## 4. Integrating analogical capabilities in MMS

Given that modeling by analogy is used by human modelers and can improve the productivity of model formulation, it is important to examine the means by which facilitate the analogical modeling capability through MMS. There are two ways in which the integration of modeling by analogy and MMS are beneficial. First, MMS can be augmented to support modeling by analogy and facilitate model formulation and use. Second, modeling by analogy can be used to make MMS more powerful beyond traditional model storage and retrieval.

## 4.1. Augmenting MMS to facilitate modeling by analogy

In order to support modeling by analogy in a computer-based environment, MMS must be augmented to provide additional capabilities to traditional MMS functions that include model representation, storage, retrieval, selection, evaluation, and execution. Figure 4 depicts possible matches between these functions and analogical modeling processes.

<table><tr><td>ANALOGICAL MODELING</td><td>MMS FUNCTIONS</td></tr><tr><td>Problem Feature Analysis</td><td>Model Representation Language</td></tr><tr><td>Identification of analogues</td><td>Model Retrieval from Model BaseModel StorageModel Decomposition</td></tr><tr><td>Analogical Mappings</td><td>Automation of Match ProcessModel Selection</td></tr><tr><td>Transfer</td><td>Automation of TransformationModel Integration</td></tr><tr><td>Evaluation</td><td>Model Consistency checkingModel Completeness Checking</td></tr><tr><td>Repair</td><td>Model Modification and EditingModel DecompositionModel Integration</td></tr></table>

Fig. 4. MMS functions facilitate modeling by analogy.

First, MMS can facilitate problem feature analysis by providing an analogical modeling language to represent and compare problem features. Because a problem description often contains some implicit relationships and functions to be identified analogically, this language may not be exactly the same as languages for model representation such as Geoffrion's structured modeling language or Krishnan's PDM. However, previous research in model representation and modeling languages should serve as a basis for the development of an analogical modeling languages $[13,19,29]$ .

Second, MMS can facilitate the identification of analogues by their model storage, retrieval, and decomposition capabilities. Because modeling by analogy requires that similar models be found before a new model can be formulated, a model base managed by MMS is critical. Without a well-indexed model base that supports the storage and retrieval of analogues, modeling by analogy would not be possible. In addition, because a new model may be partially similarity to existing ones, support of model decomposition may be necessary to identify this partial similarity.

Third, MMS can support analogical mappings between the target and source and, if more than one analogues exist, select an appropriate one based on predetermined criteria. Analogical mapping is a major step for modeling by analogy. Unless a set of proper mappings are found, the new model cannot be built. Since most problems include many entities, a number of possible mappings may exist between two problems. The determination of a set of proper mappings would require calculating similarity scores for all possible mappings and select the one with the highest score. This process can be done much more efficiently by computer-based MMS.

Fourth, once proper mappings are found, the new model can be formulated by replacing elements in the analogue with their counterparts in the new problem. This process is also tedious and error-prone if done manually. A computer-based MMS can significantly improve the efficiency and correctness of the transformation process. Furthermore, if the original problem was decomposed into several subproblems, an integration of submodels formulated separately is necessary to create the full model. The capability of model integration can facilitate the integration of separately formulated (analogically or not analogically) submodels.

Fifth, the new model formulated by analogy may be incomplete or inconsistent. An evaluation to examine the consistency and completeness of the model must be accommodated. Model consistency means that all functional relationships indicated in the model are consistent with those stated in the problem. Model completeness means that all entities and relationships stated in the problem are incorporated in the model. In other words, the model is a fair representation of the problem. An MMS can provide automated consistency and completeness checking capabilities by comparing the features included in the problem representation and the structure of the formulated model.

Finally, if errors are found in the evaluation stage, the primitive model must be repaired. The repair may range from minor changes, such as replacing an “=” relation with a “≤” relation, to major changes that need reformulation of partial models. MMS can facilitate model repair by providing model modification and editing capabilities to support minor changes. In the case of major changes, the repair process can be supported by model decomposition and integration capabilities. Model decomposition allows the problematic portion of the primitive model be separated from the remainder to form a subproblem. Then a correct model for the subproblem can be formulated and integrated with the remainder to formulate the correct model.

## 4.2. Applying modeling by Analogy to Support model management

In addition to providing support to modeling by analogy, MMS can also be enhanced by the application of the capabilities of analogical modeling. Figure 5 illustrates their possible integration from this aspect.

First, modeling by analogy adds a new dimension to model creation. Most existing literature on model formulation focuses on modeling from scratch (i.e., “whole cloth”); that is, formulating models directly from algebraic functions found in a problem description. Modeling by analogy suggests that, in addition to this straight forward approach, model formulation can take advantage of existing models and model templates. This would allow model formulation to be more efficient and more flexible. For instance, we can formulate a model analogically for a problem of which only a partial description is available.

Second, modeling by analogy adds new requirements for developing modeling languages. On the one hand, design of a modeling language must incorporate representation of problem features that allows similarity to be identified. On the other hand, because mappings and transformation are required in the process of modeling by analogy, parsimony of representation becomes a concern. A complicated representation scheme may significantly increase the computational cost of the matching process. Therefore, a representation scheme needs to focus on features that can be used to differentiate different models, rather than all details of the model.

<table><tr><td>MMS FUNCTIONS</td><td>ANALOGICAL CAPABILITIES</td></tr><tr><td>Model Creation</td><td>Analogical Formulation of Models</td></tr><tr><td>Model Representation</td><td>Problem Feature similarityParsimony of Representation</td></tr><tr><td>Model Storage</td><td>Templates and Analogical Rules</td></tr><tr><td>Model Retrieval</td><td>Analogical Retrieval</td></tr><tr><td>Model Decomposition</td><td>Templates</td></tr><tr><td>Model Integration</td><td>Templates</td></tr><tr><td>Model Modification</td><td>Repair RulesLearning</td></tr></table>

Fig. 5. Analogical capabilities facilitate MMS function.

Third, modeling by analogy allows model storage and retrieval to be more flexible. For example, instead of storing all individual models, MMS may maintain templates and higher level schemata in the model base, index those models to their proper templates, and rebuild them when necessary. Only those models that do not have a proper template need to be stored separately. This can save storage 'space' and reduce search costs for model management at the cost of rebuilding from templates. In addition, model retrieval can also be done analogically. In other words, model retrieval may allow the user to retrieve similar models if no exact match is found.

Fourth, modeling by analogy may support model decomposition and integration by providing templates and analogical guidelines. One role of model decomposition in MMS is to divide a large model into smaller modules shared with many models to reduce storage redundancy in the model base. These smaller modules can be integrated when the model is in use. Currently, the shared modules need to be exactly the same in different problems to be considered common. The capability of analogical modeling enables similar but not exactly the same modules to be decomposed and stored as long as there are analogical rules that can integrate these modules to reconstruct the model. This makes model decomposition and integration more flexible. In addition, when a new model is to be constructed from an integration of a set of existing ones, modeling by analogy can increase the efficiency of integration by identifying similar integrations previously done.

Finally, modeling by analogy can enhance the function of model modification. Little literature in MMS has discussed how an erroneous model can be repaired. Heuristics used for repairing a model formed analogically can also be used to fix incorrect models formulated from scratch. The repair process can also help the model builder learn error patterns and improve modeling productivity.

In summary, MMS can facilitate the implementation of modeling by analogy through its extensive model management functions, including modeling language, model storage and retrieval, model decomposition, model integration, and automated feature matching and transformation. Modeling by analogy can also enhance MMS by allowing more flexibility in model creation, model storage, model retrieval, model decomposition, model integration, and model modification.

## 4.3. Research issues

Although an integration of modeling by analogy and MMS can benefit both, there are several issues that need further research before real implementation can occur. Some of these issues are related to the process of modeling by analogy, whereas others are related to the management of analogues.

The first and foremost issue related to successful implementation of modeling by analogy in MMS is to define problem features and measure model similarity. We need to be able to know how alike and how different two models are and on what dimensions they are similar or different. In other words, we must know what are the problem features that govern problem similarity and how these features can be represented and compared with existing models. A language for modeling by analogy may be developed.

In Section 2, we presented a similarity metric adapted from Tversky's Contrast Model. We suggested that problem representation include entities, attributes, and their relationships. Entity and structural similarities can then be compared based on similarity scores calculated from the metric. In Section 3, we introduced another complexity-based metric that measures the volume, distribution, and location complexities of a problem. Although these metrics work fine with some models, no evidence indicates that it is applicable to all problems or whether there exist a universally applicable similarity metric. If a universally applicable similarity metric exists, how can it be discovered? If it does not exist, how can we know when and where a particular metric is better?

The second issue requiring further research is the computational efficiency for measuring similarity and selecting proper mappings. We defined in Section 2 that two structures must be isomorphic in order to be structurally similar. Identifying isomorphic structures itself is a computationally hard task. Therefore, how can an efficient method for matching entities and structures be developed may have an impact on the implementation of modeling by analogy. Part of this problem can be solved by using higher-level strucres. For example, instead of comparing element-l graphs, we may compare generic graphs when comparing the similarity between two structured models.

For large-scale problems, however, the generic structure may still be very complicated and a composition that breaks the structure into several substructures would be necessary. In this case, we must study the effect of model decomposition on model similarity. Are two structures having similar substructures also similar? How in the optimal decomposition be identified? If bstructure similarity exists, how can the submodels formed based on similarity at the submodel level be integrated to form an overall model?

The third major area in modeling by analogy at needs further research is the evaluation and pair of the formulated model. Unless a perfect match between two problems is found, the anagically formulated model usually contains errors at must be detected and repaired. These retire knowledge of error patterns, potential uses of a particular error, and the proper repair an error. Some of this knowledge can be obtained from human modelers. In an ideal situation, however, MMS must be able to classify error patterns, learn the causes of errors, and then ggest cures for them.

Concerning the application of MMS to support modeling by analogy, the first issue that needs other study is how to recognize the opportunity modeling by analogy and what are the basic ills of analogical thinking that need to be supported. Compared to modeling from scratch, modeling by analogy provides a short-cut for model builders to take advantage of previous experience. However, it may not be appropriate all kind of models. We need to know when modeling by analogy would be useful and when it not. This is especially important when the model base contains a large number of potential dialogues because an analogical modeling process may take a substantial amount of computational power. Therefore, a pre-processor for determining the opportunities of modeling by analogy may be necessary. The pre-processor must maintain a very-high-level schemata that can detect problem patterns and identify opportunities in analogical modeling efficiently.

A second issue is concerned with the indexing of models in the model base to support modeling by analogy. Each domain may have a relatively small number of useful analogues. It is important to note that in the majority of management situations there will only be a limit set of contexts, and hence, a limited set of highly useful analogues. The problems then are how to identify these essential models for analogical modeling? How to organize these analogues to best detect similarities? What would be the minimal set of model analogues that will serve the broadest class of modeling activities? How many candidate analogues must be considered in each modeling process?

A final issue that requires further study is the role of learning and adaptation in modeling by analogy. Most stages of the analogical modeling process require dynamic knowledge that changes over time. Learning of this knowledge such as rules for analogical mappings, improved similarity metric, and rules for evaluation and repair of models is also essential to the successful implementation of modeling by analogy.

## 5. Concluding remarks

Modeling by analogy is a technique frequently used by human modelers but virtually unexplored in existing model management literature. In this paper, we explored the concept of modeling by analogy and discussed its integration into MMS. We first described model similarity and the process of modeling by analogy. This was followed by discussions on the synergy between analogical reasoning and MMS. We suggested that, on the one hand, modeling by analogy can be supported by model management functions such as model representation, model storage and retrieval, model decomposition and integration, and model selection. On the other hand, modeling by analogy can also enhance MMS by providing analogical formulation and retrieval capabilities. We also identified many issues that need further research.

An implementation of modeling by analogy in a computer-based environment must have three characteristics. First, it must be interactive, that is, the system facilitates but does not replace the model builder in the process. The system focuses on searching the existing models and matching features, while the model builder verifies the appropriateness of the analogy. Second, it must be iterative. If an analogue is found to be inappropriate in any step of the process, it will be dropped and the next available one will be used as a substitute. This process continues until a satisfactory model structure is constructed or until all potential analogues are found inappropriate. Third, it must be flexible. In other words, it must allow submodel similarity to be identified or permit several analogues to work together to construct an integrated new model.

The implication of this work for further research is two-fold. First, it initiates research in an area that has been widely used in model construction practice but unexplored in existing modeling literature. Second, the discussion of model similarity and analogical modeling provides insights into further studies on model formulation, decomposition, integration, and other key issues. The knowledge obtained from studying analogical modeling can also be used to investigate model utilization and learning issues in problem solving.

## References

[1] L. Applegate, B.R. Konsynski and J. Nunamaker, Model Management Systems: Design for Decision Support, Decision Support Systems 2, pp. 81–91 (1986).

[2] M. Belth, The Process of Thinking (David McKay, New York, 1977).

[3] M. Binbasioglu and M. Jarke, Domain Specific DSS Tools for Knowledge-based Model Building, Decision Support Systems 2, 3, pp. 213–223 (1986).

[4] R.W. Blanning, Issues in the Design of Relational Model Management Systems, AFIPS Conference Proceedings, pp. 395–401 (1983).

[5] R.W. Blanning, Conversing with Management Information Systems in Natural Language, Communications of the ACM 27, 3, pp. 201–207 (1984).

[6] R.W. Blanning, A Relation Framework for Join Implementation in Model Management Systems, Decision Support Systems 1, 1, pp. 69–81 (1985).

[7] R.W. Blanning, An Entity-Relationship Approach to Model Management, Decision Support Systems 2, 1, pp. 65–72 (1986).

[8] R.H. Bonczek, C.W. Holsapple and A.B. Whinston (1980). The Evolving Roles of Models in Decision Support Systems, Decision Sciences 11, pp. 337–356 (1980).

[9] G.H. Bradley and R.D. Clemence, Model Integration with A Typed Executable Modeling Language, Proceedings of the 21st Hawaii International Conference on System Sciences, IEEE Computer Society Order Number 843, 3, pp. 403–410 (1988).

[10] M.L. Bu-Hulaiga and H.K. Jain, An Interactive Plan-

based Procedure for Model Integration in DSS, Proceedings of the 21st Hawaii International Conference on System Sciences, IEEE Computer Society Order Number 843, 3, pp. 428–434 (1988).

[11] D.R. Dolk, Data as Models: An Approach to Implementing Model Management, Decision Support Systems 2, 1, pp. 73–80.

[12] D.R. Dolk, Model Management and Structured Modeling: The Role of an Information Resource Dictionary Systems, Communications of the ACM 31, 6, pp. 704–718 (1988).

[13] D.R. Dolk and B.R. Konsynski, Knowledge Representation for Model Management Systems, IEEE Transactions on Software Engineering SE-10, 6, pp. 619–628 (1984).

[14] A. Dutta and A. Basu, An Artificial Intelligence Approach to Model Management in Decision Support Systems, IEEE Computer 17, 9, pp. 89–97.

[15] J.J. Elam and B.R. Konsynski, Using Artificial Intelligence Techniques to Enhance the Capabilities of Model Management Systems, Decision Sciences 18, 3, pp. 487-502 (1987).

[16] J.J. Elam, J.C. Henderson and L.W. Miller, Model Management Systems: An Approach to Decision Support in Complex Organizations, Proceedings of the First International Conference on Information System pp. 98–110 (1980).

[17] J. Fedorowicz and G.B. Williams, Representing Modeling Knowledge in an Intelligent Decision Support System, Decision Support Systems 2, 1, pp. 3–14.

[18] A.M. Geoffrion, Introduction to Structured Modeling, Management Science 33, 5, pp. 547–588.

[19] A.M. Geoffrion, SML: A Model Definition Language for Structured Modeling, Working Paper No. 360, UCLA (May 1988).

[20] A.M. Geoffrion (1989), Integrated Modeling Systems, Computer Science in Economics and Management 2, 1, pp. 3–15.

[21] H.J. Greenberg, A Natural Language Disclose Model to Explain Linear Programming Models and Solutions, Decision Support Systems 3, 4, pp. 333–342 (1987).

[22] M. Hesse, Models and Analogies in Science (Notre Dame University Press, 1966).

[23] S. Hwang, Automatic Model Building Systems: A Survey, DSS-85 Transactions, San Francisco, CA.. pp. 22–32 (1985).

[24] G. Klein, Developing Model String for Model Management, Journal of MIS 3, 2, pp. 94–110.

[25] G. Klein, B.R. Konsynski and P.O. Beck, A Linear Representation for Model Management in a DSS, Journal of MIS 2, 2, pp. 40–54.

[26] B.R. Konsynski and R.H. Sprague (1986), Future Research Directions in Model Management, Decision Support Systems 2, 1, pp. 89–91 (1986).

[27] J.E. Kottemann and D.E. Dolk, Process-oriented Model Integration, Proceedings of the 21st Hawaii International Conference on System Sciences, IEEE Computer Society Order Number 843, 3, pp. 396–402 (1988).

[28] J.E. Kottemann and B.R. Konsynski, Complexity Assessment: A Design and Management Tool for Information System Development, Information Systems 8, 3, pp. 195–206 (1983).

[29] R. Krishnan, PDM: A Knowledge-based Tool for Model Construction, Decision Support Systems, forthcoming.

[30] M.L. Lenard, Representing Models as Data, Journal of MIS 2, 4, pp. 36–48 (1986).

[31] T.P. Liang, Integrating Model Management with Data Management in Decision Support Systems, Decision Support Systems 1, 3, pp. 221–232.

[32] T.P. Liang, Toward the Development of a Knowledge-based Model Management Systems, Unpublished Ph.D. Dissertation, The Wharton School, University of Pennsylvania (1986).

[33] T.P. Liang, Reasoning in Model Management Systems, Proceedings of the 21st Hawaii International Conference on System Sciences, IEEE Computer Society Order Number 843, 3, pp. 461–470 (1988a).

[34] T.P. Liang, Development of a Knowledge-based Model Management System, Operations Research 36, 6, pp. 849–863 (1988b).

[35] T.P. Liang, Model Similarity and Modeling By Analogy, Working Paper, University of Illinois at Urbana-Champaign (1989).

[36] T.P. Liang, Modeling by Analogy: A Case-based Approach to Automated Formulation of Linear Programs, Proceedings of the Twenty-Four th HICSS Conference (1991).

[37] T.P. Liang and C.V. Jones (1988), Meta-design Considerations in Developing Model Management Systems, Decision Sciences 19, 1, pp. 72–92 (1988).

[38] P. Ma, F.H. Murphy and E.A. Stohr, Semantic Structures in Linear Programs, Proceedings of the Twenty-Second Hawaii International Conference on Systems Sciences III, pp. 459–466 (1989).

[39] M.V. Mannino, B.S. Greenberg and S.N. Hong, Knowledge Representation for Model Libraries, Proceedings of the 21st International Conference on System Sciences, IEEE Computer Society Order Number 843, 3, pp. 349-355 (1988).

[40] L.W. Miller and N. Katz, A Model Management System to Support Policy Analysis, Decision Support Systems 2, 1, pp. 55–63.

[41] W.A. Muhanna and R.A. Pick, Composite Models in SYMMS, Proceedings of the 21st Hawaii International Conference on Systems Sciences, IEEE Computer Society Order Number 843, 3, pp. 418–427 (1988).

[42] F.H. Murphy and E.A. Stohr, An Intelligent System for Formulating Linear Programs, Decision Support Systems 2, 1, pp. 39–47.

[43] M.M. Sklar, R.A. Pick and W.H. Sklar, An Automated Approach to LP Model Formulation, Working Paper, Department of QAIS, University of Cincinnati, (1989).

[44] R.H. Sprague Jr. and E.D. Carlson eds., Building Effective Decision Support System (Prentice-Hall, Englewood, 1982).

[45] R.J. Sternberg, Intelligence Information Processing and Analogical Reasoning (Lawrence Erlbaum Associates, Hillsdale, NJ, 1977).

[46] R.J. Sternberg, Reasoning, Problem Solving, and Human Intelligence (Cambridge University Press, Cambridge, 1982).

[47] E.A. Stohr and M.R. Tanniru, A Database for Operation

Research Models, International Journal of Policy Analysis and Information Systems 4, 1, pp. 105–121 (1980).

[48] A. Tversky, Features of Similarity, Psychological Review 84, 4, pp. 327–352.

[49] S. Vosniadou and A. Ortony, Similarity and Analogical Reasoning (Cambridge University Press, Cambridge, 1989).

## Appendix. Examples and sample sessions

## A. The process selection problem

<table><tr><td>&gt; Entity</td><td>&gt; Attribute</td><td>&gt; Feature</td></tr><tr><td>* root</td><td>* root</td><td>* root</td></tr><tr><td>* product</td><td>* tot_cost</td><td>% tot_cost</td></tr><tr><td>% root</td><td>% root</td><td>= = Z</td></tr><tr><td>* process</td><td>* unit_cost</td><td>* product</td></tr><tr><td>% root</td><td>% tot_cost</td><td>% quantity</td></tr><tr><td>* resource</td><td>* tconsump</td><td>&gt; = di</td></tr><tr><td>% root</td><td>% root</td><td>* resource</td></tr><tr><td>* link(p, p)</td><td>* uconsump</td><td>% tconsump</td></tr><tr><td>% product</td><td>% tconsump</td><td>&lt; = bk</td></tr><tr><td>% process</td><td>* quantity</td><td>* link(p, p)</td></tr><tr><td>* link(p, p, r)</td><td>% root</td><td>% unit_cost</td></tr><tr><td>% link(p, p) .end</td><td></td><td>= = cij</td></tr><tr><td>% resource</td><td></td><td>% quantity</td></tr><tr><td>end</td><td></td><td>= = Xij</td></tr><tr><td></td><td></td><td>* link(p, p, r)</td></tr><tr><td></td><td></td><td>% uconsump</td></tr><tr><td></td><td></td><td>= = aijk</td></tr><tr><td></td><td></td><td>.end</td></tr></table>

## B. The transportation problem

\* plant
% root

C. ANALOGY. Sample session

## SEARCH FOR ANALOG

Searching for similar problems ... Please wait for a moment

Current problem comparing = process selection problem

Score: $8 / 8 = 1.00$

Score: $11 / 12 = 0.92$

Similarity score of the problem = 0.92

The best analogy = process selection problem
Overall similarity score = 0.92

Transforming ... Please wait!

## <1> Attribute mappings:

<table><tr><td colspan="2">New Problem</td><td>Analogue</td></tr><tr><td>totalcost</td><td> $\langle --\rangle$ </td><td>tot_cost</td></tr><tr><td>unitcost</td><td> $\langle --\rangle$ </td><td>unit_cost</td></tr><tr><td>flow</td><td> $\langle --\rangle$ </td><td>quantity</td></tr></table>

## <2> Entity mappings:

<table><tr><td colspan="2">New Problem</td><td>Analogue</td></tr><tr><td>root</td><td></td><td>root</td></tr><tr><td>plant</td><td rowspan="3"><img src="/api/attachments/GB63MC9S/fulltext/images/f0c466fca2477abca25763a5aec424b7ab0c1899a9823024276420f6c2adc50a.jpg"/></td><td>product</td></tr><tr><td>customer</td><td>process</td></tr><tr><td>route</td><td>link(p, p)</td></tr></table>

## 〈3〉 Feature mappings;

<table><tr><td colspan="2">New Problem</td><td>Analogue</td></tr><tr><td>Z</td><td> $\langle - - - - - \rangle$ </td><td>Z</td></tr><tr><td>si</td><td> $\langle - - - - - \rangle$ </td><td>di</td></tr><tr><td>dj</td><td> $\langle - - - - - \rangle$ </td><td>U</td></tr><tr><td>cij</td><td> $\langle - - - - - \rangle$ </td><td>cij</td></tr><tr><td>Xij</td><td> $\langle - - - - - \rangle$ </td><td>Xij</td></tr></table>

... Generating an equation for dj by rule No. 2

$\mathrm{dj} = = \mathrm{sum(i)}\mathrm{Xij}$

... The following equation in the analogue is removed:

$\operatorname {sum}(\mathrm{ij})\mathrm{aij}^{*}\mathrm{Xij} <   = \mathrm{bk}$

Because $\langle aijk\rangle$ in the analogue does not match any feature in the problem

## MODELING OUTPUT

The resulting model formulated based on your problem description is as follows:

$$
Z = = \operatorname{sum} (i j) c i j ^ {*} X i j
$$

〈〈press RETURN to continue〉〉

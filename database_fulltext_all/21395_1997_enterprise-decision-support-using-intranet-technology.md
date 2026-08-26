---
otero_id: 21395
otero_key: "64AUZY2R"
title: "Enterprise decision support using Intranet technology"
authors: "Sulin Ba; Karl R Lang; Andrew B Whinston"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(96)00068-1"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Enterprise decision support using Intranet technology

Sulin Ba $^{a,*}$ , Karl R. Lang $^{b}$ , Andrew B. Whinston $^{c}$

$^{a}$ Marshall School of Business, University of Southern California, Los Angeles, CA 90089-1421, USA $^{b}$ Department of Information and Systems Management, Hong Kong University of Science and Technology, Hong Kong $^{c}$ Center for Information Systems Management, The University of Texas at Austin, Austin, TX, USA

## Abstract

We present a knowledge-based enterprise modeling framework that automatically builds and executes task-specific models in response to user queries. This framework bases its reasoning about a particular organization upon a library of knowledge representing significant organizational phenomena from different perspectives and at different levels of detail. The system is aimed at providing fast cycle responses to decrease organizational error and support strategic decision-making. The focus is on how to improve model building and how to extract the relevant knowledge to support specific analyses of corporate issues. An Intranet-based prototype implementation is presented to illustrate the ideas and concepts. © 1997 Elsevier Science B.V.

Keywords: Enterprise modeling; Decision support systems; Knowledge management; Automatic model building; Intranets

## 1. Introduction

In order to respond to new challenges in an increasingly complex and dynamic environment, modern management is using a vast amount of knowledge from various sources. Depending on the particular problem being investigated, managers switch between different perspectives and levels of detail when searching for the relevant pieces of knowledge required to provide an appropriate answer. However, lacking a centralized knowledge management facility, individual managers' access to knowledge is restricted to a relatively small subset of the collective organizational knowledge, depending on their status and function within the organization. This may inhibit the recognition of the interactions and interdependencies relevant to the problem under study. For better decision-making, managers need to look at problems in a non-myopic fashion and take on a global organizational view instead of individually biased perspectives.

Corporations routinely generate huge amounts of business data, spread across organizational divisions and departments, on a daily basis. While the concept of viewing information as a critical resource has now been widely accepted in theory and practice, it is still not fully understood how to explore the available masses of corporate data in order to enhance organizational effectiveness. However, it is clear that certain basic knowledge management principles ought to be followed to achieve the general goal of building an intra-organizational knowledge base that can be effectively used as the basis to deliver relevant and useful information to the right person at the right time. Those principles include (i) the usage of corporate data as building blocks to derive and create new, higher-level information and knowledge that describe the important enterprise operations; (ii) an organizational information integration to ensure that all departments and end-users (managers) have the ability to effectively access and utilize the intra-organizational knowledge base; and (iii) the provision of decision support systems (DSS) tools which transform scattered data into meaningful business information for supporting operational and strategic corporate decision-making.

Significant advances in organizational and network computing technologies and the recent development of corporate digital library and data warehousing technology $[34]$ help address these issues. However, current implementations of data warehouse systems are based only on the first two of the above principles, encompassing mainly the organization of dispersed, enterprise-wide data in form of data repositories and the provision of better transparency of the operational picture $[44]$ . Little is presently offered in terms of integrating data warehousing with DSS technology. Epstein, a Vice President of Sybase Inc. anticipates that the decision support technology incorporating data warehousing technology will become more and more crucial for productivity, and such an extended effort will make data warehousing and knowledge management the central components of future organizational information systems $[20]$ .

The research of DSS is concerned with the development and implementation of computer supported decision-making and problem-solving environments. Because many enterprise scenarios are too complex to be fully understood, models are developed to help decision-makers analyze specific situations, by choosing a particular view and by introducing assumptions, abstractions, and approximations. Despite some twenty years of progress in DSS research and technology, current systems still lack the generality and versatility needed to handle unstructured or semi-structured knowledge in order to supply managers with adequate DSS tools which support all phases of the enterprise modeling process.

On the other hand, organizations have become more and more distributed, with information sources dispersed in many locations, which makes it more difficult for a decision-making process to take a cross-functional, enterprise-wide perspective. Moreover, using online information for decision-making is made more challenging by the heterogeneity of the underlying knowledge representations, retrieval techniques, and end-user computing front ends. The big challenge for organizations today, particularly large global organizations, has become to find ways to integrate information across the enterprise. Fortunately, information integration, while a major research problem in the past, does seem to be less daunting in the presence of new technologies such as the World Wide Web (WWW) [7], or, more specifically, Intranets [48], and sophisticated browsers such as Netscape [28]. The transparency of the integration process is what makes the WWW technology so effective. It has become quite clear that enterprise computing is going to be an extremely important application of the Intranet technology that has not been widely recognized.

The need for effective knowledge management combined with the potential power provided by the Intranet technology prompted us to develop a knowledge centric enterprise-wide decision support system. Conceptually, we are looking for an enterprise modeling system (EMS) $^{1}$ which automatically builds and executes task-specific models as needed in response to queries posed by the user. EMS is especially aimed at providing fast cycle responses to decrease organizational error and support strategic decision-making such as predicting the effects of changes in business policies (“what if”-type of questions), analyzing possible reactions to internal and external threats (“what should we do”-type of questions), and exploring new business opportunities (“where should we go”-type of questions).

The management literature provides a strong motivation for building enterprise-wide modeling and decision support systems. For example, Refs. [35,36] argue that organizational systems exhibit a significant degree of interdependency across functional areas, that requires decision-makers to identify relevant relationships and knowledge that contribute to a given corporate goal across functional boundaries, and that senior managers need to consider all important operational measures to see whether improvement in one area may have been achieved at the expense of another. Ref. [30] points out that companies must be able to respond to threats quickly by identifying the important business processes and operations at stake. An EMS should not only tell managers “how we do things around here” and “why we do things this way” but also show managers “how we can change the way we do things” and “what we should change”.

In this paper, we discuss some major design issues for the next generation of knowledge-based enterprise modeling systems, and indicate the direction future research could take to support enterprise-wide problem formulation and problem solving with effective knowledge management. The focus of this paper is on how to improve model building and how to extract the relevant pieces of knowledge to support specific analyses of enterprise-wide corporate issues. We discuss and propose ideas which we see as promising steps towards accomplishing this difficult endeavor. There are two, essentially disjoint, research efforts, one based in the artificial intelligence community and the other in the decision support systems community, which study model building and reasoning with multiple models. This paper draws upon both of these efforts and develops a synergistic framework for knowledge centric enterprise modeling systems. We also propose to use the Intranet technology to implement our framework.

The several-fold purpose of this paper is (i) to introduce the readership to the literature on automated model building, which is largely unknown in the MIS community, and its connections to the DSS field; (ii) to propose a novel, conceptual enterprise modeling framework based on an automated question answering system which can be used to incorporate data warehousing and DSS into intra-organizational computing systems; (iii) to discuss model building issues that are of specific significance in the business and management domains; (iv) to present a partial, Intranet-based prototype implementation of our enterprise modeling system that demonstrates how query-specific answers can be derived from a repository of heterogeneous pieces of organizational knowledge; and (v) to suggest a research agenda by pointing out the current limitations of our approach and summarizing important open research problems that need to be resolved before off-the-shelf EMS software technology can be developed successfully.

The remainder of the paper is organized as follows. Section 2 puts forth the framework of our knowledge centric enterprise modeling system. In Section 3, we investigate major modeling approaches in both DSS and artificial intelligence fields. Then, in Section 4, we discuss in detail the knowledge representation issues and, in Section 5, the model composition process. Then we present, in Section 6, a partial implementation of an Intranet-based EMS prototype, and also summarize important open research questions and outline some suggestions for future research directions, and finally conclude with a summary of our paper in Section 7.

## 2. A conceptual framework for enterprise-wide modeling systems (EMS)

We see organizational-wide reasoning systems as decision tools for both strategic and operational management. In business related areas like organization science, management, business communication, and others, qualitative approaches are widely used in order to investigate problem scenarios and to develop theories $[45]$ . Especially when exploring strategic questions, it is essential to be able to include qualitative knowledge into the analysis. While traditional DSS research emphasizes quantitative modeling, work in the area of qualitative reasoning has focused attention on reasoning about qualitative knowledge. However, the importance and relevance of a more formal treatment of qualitative knowledge representations and qualitative inference methods has recently been recognized in the DSS literature as well $[31]$ . We envision a system whose reasoning about a particular organization is based upon a knowledge base consisting of model components (or fragments) representing significant organizational phenomena from different perspectives and at different levels of detail. Accomplishing this requires access to multiple sets of heterogeneous model fragments which differ in several dimensions, some of which might even be mutually inconsistent. We need to address the issue of model representation and model organization. That is, we need a language for expressing relationships of different kinds and for expressing underlying assumptions controlling and guiding their applicability. The task of organizing organizational knowledge into semi-independent, reusable model fragments is a crucial one for enabling an EMS to compose useful, problem-specific models by integrating relevant, existing model components under a variety of different modeling circumstances.

As a starting point of our framework for enterprise modeling systems we use the artificial intelligence (AI) vision of constructing large information repositories and developing automated question answering systems for explaining and predicting certain physical phenomena, as opposed to developing systems for merely indexing and reciting stored information. Although AI research has almost exclusively used fairly well understood problem domains from the physics and engineering fields as their application areas, it is evident that their vision applies as well to the business and management domains. However, while many physical processes can be represented by commonly agreed on descriptions of mechanical devices and their interactions based on accepted laws of the natural sciences, business processes, on the other hand, are influenced by human factors, incompletely known economic environments, competitive markets, and uncertain future events and developments entailing a higher degree of ambiguity. These differences in business related problem settings also impede a straightforward application of currently available AI systems. Nevertheless, and despite the fact that the above stated AI vision at this point is still far away from complete fulfillment, we believe that it is important for the MIS community to acknowledge automated question answering systems as a significant research topic that requires, in addition to applying AI-based concepts, studying fundamental business issues related to the understanding and formalization of business processes such as, for example, the epistemology of - organizational systems and the development of com-

'ensive business ontologies and taxonomies.

Clearly, this formidable research challenge cannot be met without breaking the traditionally rather rigid boundaries of individual research communities, but requires an interdisciplinary approach drawing input from the areas of IS/DSS, operations research/management science (OR/MS), organization science/management theory (OS/MT), AI and others.

The main challenge is how to build enterprise-wide models which are focused on the problem-specific issues. We propose a model building strategy which realizes that the construction of a holistic, monumental enterprise-wide model would be impractical. Hence, we need a flexible enterprise modeling system which builds models as needed in response to user queries. Given a query, the model formulation problem can be defined as selecting the relevant pieces of knowledge (model fragments) and generating a composite, task-specific model that is coherent and useful in answering it. Potential applications of enterprise modeling are diagnosing the performance of a firm, predicting the behavior of an organization over time, testing the implications of theories about organizations, supporting business re-engineering and strategic business decision-making.

Using different sets of assumptions and various kinds of knowledge ranging from general, qualitative knowledge to specific and precise numerical models, managers analyze organizational questions from different perspectives and at different levels of detail. Given a particular task, model building is guided by the selection of an appropriate perspective and level of detail, a modeling decision for which little support is found in current decision support system technology. When modeling a certain organizational phenomenon, it is crucial to focus on the relevant aspects of the situation under investigation, that is, to include all the relevant objects and constraints, but also to exclude irrelevant ones and ignore unnecessary details. For example, answering a question like “How do customers see our company?” does not require us to consider the production process at an operational level, or to consider individual pieces of machinery or product units. A recent study of enterprises in crisis situations $[55]$ shows that actors in complex organizational systems tend to neglect cross-functional interdependencies and make heedless decisions when under stress. All too often this leads to some local improvements at the cost of global organizational objectives of much higher importance. Organizations in a complex and turbulent environment could be managed better if a (computer supported) tool, specifically, an enterprise modeling system, were available which helps decision-makers to look at problems in a non-myopic fashion, identity all significant interactions, including cross-functional relationships, and recognize underlying modeling assumptions. We propose the conceptual framework depicted in Fig. 1 for designing such an EMS.

![](/api/attachments/64AUZY2R/fulltext/images/2543c9556fd5e5d19c702542bf9d3d6d63c39017edafba3c9a8a52819ac54526.jpg)  
Fig. 1. EMS software architecture.

This EMS framework is designed as a basis for the implementation of future interactive software tools which support decision-making and problem solving when exploring various business scenarios. It comprises five functional modules: the query manager, the model manager, the candidate evaluation module, the solver, and the report generator.

The query manager provides the interface between the EMS and the user, typically an organizational decision-maker or a technical assistant to one. It processes user's queries such as, "How does an increase in price affect net income?" and translates them into a set of executable statements which are submitted to the model manager.

The core of the EMS is the model manager which controls access to models and data in the organizational knowledge base that serves as organizational memory $[52]$ . The organizational knowledge base represents a computerized form of the organizational memory. Commercial systems that implement organizational memories by creating and maintaining repositories of corporate data and information are also known as data warehousing systems. The enterprise modeling framework requires first the building of a general-purpose organizational knowledge base that describes a variety of organizational objects, activities, and processes. The domain theory is represented as a library of model fragments, each describing an independent aspect from a particular viewpoint. It contains general organizational laws and rules as well as relationships that are very specific to a particular company. The organizational knowledge described in the domain theory could be obtained from research results in the organizational behavior field, which tries to formulate theories about organizations in general, that is, to find relationships that help understand the behavior of a wide variety of organizations. Since those relationships are supposed to hold for any particular organization of the class, they tend to be very qualitative in nature. Organization-specific information, on the other hand, is derived from historical data and experience accumulated within a particular company, and therefore, tends to be much more precise. This information is often encoded in a quantitative, management science/operations research (MS/OR) type of model like optimization, simulation, or forecasting models. The explicit representation of modeling assumptions in terms of abstraction level, approximation, perspective, level of detail, and granularity is another essential feature in enterprise modeling. Reasoning capabilities about those assumptions enables the EMS to identify a suitable collection of compatible model fragments and to build consistent, composite models in response to a query. Typically, there is no unique composite model and the model manager might find several feasible models, called candidate models, and passes each of them on to the next EMS module.

The candidate evaluation module then collects all candidate models and chooses the best candidate as the final scenario model. In this context, best means the simplest possible model that is coherent, comprehensive, and appropriate for the task. The solver module selects the adequate solution method and then solves or simulates the scenario model chosen by candidate evaluation. Finally, a report generator is employed as a post processor in order to translate the model solution into an intelligible answer which can be presented to the user in return to the original question.

We see our EMS concept as a refinement of Stein and Zwass' framework [52] for enterprise modeling systems which they call organizational memory information systems (OMIS) in their terminology. They argue, that in light of the advancement in information technologies, experiential organizational knowledge (or organizational memory) is an crucial key to competitiveness and that “... organizational memory information systems (enterprise modeling systems)... provide a means by which knowledge from the past is brought to bear on present activities, thus resulting in increased levels of effectiveness for the organization.” Their OMIS framework is founded on five basic functions called knowledge acquisition, retention, maintenance, search, and retrieval which basically resemble the structure of our EMS framework. However, while Stein and Zwass' work is at a strictly conceptual level and does not address how organizational memory would be represented in a formal way and how it would be used to generate task-specific models, we go a step further in this paper and discuss the technical issues of knowledge representation, knowledge management, and model composition.

In this section, we have presented a conceptual description of EMS and have raised in general terms the major EMS issues, several of them still being open research questions. We still need to operationalize the main concepts of EMS before a complete EMS can be successfully developed and implemented. After overviewing the relevant modeling literature in AI and DSS in the next section we will return to those issues again and discuss them in much more detail.

## 3. Reasoning with model in AI and DSS

Model management is an important area of DSS research. Model management systems constitute a class of software designed to support the construction, storage, retrieval, and use of models in the context of decision support systems [5]. The purpose of a model management system is to insulate the users of a DSS from the physical aspects of model base storage and processing. Research in model management has mainly focused on three topics: the structure of model bases, model base processing, and the organizational environment of model management systems [12]. In terms of model base structure, one effort is structured modeling which provides a framework, not only for model structuring, but also for model base documentation, the development of libraries of reusable model components, and object-oriented model management [26,21,41]. In this section, we overview some approaches to the model building processes based on which we develop our framework.

Researchers in the DSS and artificial intelligence (AI) communities have proposed several frameworks which provide partial solutions to this formidable problem. Similar to Ref. [23], we argue that cross-fertilizing ideas from both research fields will achieve significant progress in answering many of the open research questions impeding the development of complete, enterprise-wide decision support systems. While the DSS and AI paradigms diverge in their application domains, management and engineering, respectively, they face basically the same underlying model building issues. Work in the two areas also differ in other aspects. Model management in the DSS field can be seen as a natural extension of previous work in management science and operations research. It has advanced mathematical modeling from a state where modeling was an uncoordinated task, whose success depended mainly on the technical skills and expertise of the user, to a state where systems actually know about certain types of mathematical models and appropriate solvers. While restricted to mathematical programming models, statistical forecasting models, and perhaps discrete-event simulation models, DSS research has made considerable progress in solver and model integration. Most of that work is based on rather specific and well structured and well understood problem domains such as production, distribution and inventory models. The emphasis of AI research, on the other hand, has been put more on the issue of the explicit representation of modeling assumptions, and the usage and exploration of qualitative knowledge, and less on model integration and in particular on solver integration. The next two subsections summarize the work presented in the AI and DSS literature.

## 3.1. Reasoning with model building in artificial intelligence

De Kleer and Brown [19] propose component connection modeling as a tool for reasoning about loosely coupled, dynamic physical systems. De Kleer and Brown's framework rests on the no-function-in-structure principle which says that we can decompose a complex system into a structure of context-free components and interconnections. A domain dependent component library would supply the modeler with a standard set of independent building blocks from which a particular scenario model can be built. Model integration is achieved by connecting components with each other through terminal points which represent shared variables, a task which requires explicit specifications from the modeler. Components communicate by applying input signals to terminal points and propagating output signals from terminal points to connected components. The output signals produced by a component depend not only upon the input signals but also upon the active set of assumptions. The supporting context is described separately as a set of global, class-wide assumptions that determines the function of a component as a part of the system. The explicit representation of the underlying assumptions determines which devices are compatible and what kind of interactions are admissible. Another type of assumption concerns the treatment of the dynamics of the system. That is, it explicates if we are dealing with an equilibrium or non-equilibrium system. The quasi-static approximation assumption, the standard case in component connection modeling, states that the system is always in or near equilibrium, that is, the system returns quickly to equilibrium after a disturbance. This implicit assumption allows one to ignore intermediate non-equilibrium states which simplifies the simulation process, but excludes more general modeling situations. De Kleer and Brown do not discuss strategies of when and how to switch between different sets of assumptions. In order to apply the component connection approach to enterprise modeling we must develop a theory of business ontologies with coherent laws and assumptions, a task that needs further research.

Compositional modeling, proposed by Falkenhainer and Forbus (FF) [24], presents an automatic model building framework for reasoning with multiple models. The main characteristics of compositional modeling can be summarized as its capability of providing access to multiple models pertaining to a particular problem domain, forming an appropriate model for each specific analysis, and expressing explicit representations of underlying modeling assumptions. Given a model library that contains a collection of model fragments which represent the available domain knowledge and a description of a particular problem, the compositional modeling system generates, for each specific query, a scenario model which can be solved in order to give a satisfactory answer to the question raised by the query.

The idea of composing a scenario model as needed imposes a great challenge to model management. It is almost impossible to maintain a monolithic model that represents all facets of an entire system. Instead, the domain knowledge should be organized as a collection of heterogeneous model fragments and assumptions constraining their use. An important organization principle in building a model library is that the model fragments form a structural part-of-hierarchy which is used to identify related fragments. A model fragment contains not only a set of relationships describing objects and their interactions, it must also explicitly encode underlying assumptions which tell us under which conditions the model fragment is actually applicable. Model fragments should be designed as modular, semi-independent, reusable, and possibly mutually inconsistent building blocks. Additionally, sets of class-wide assumptions each describing commitments and conditions of a particular perspective of a scenario should be maintained. By matching the assumptions of the active set of class-wide assumptions with the assumptions explicated in the model fragments, it is possible to retrieve only those model fragments that are applicable and related to a given task. Which fragments should be considered for building a scenario model depends upon the active set of class-wide assumption. A crucial presupposition of compositional modeling is that the query posed provides enough clues to identify which objects and processes, and thereby which model fragments, need to be considered and what the appropriate set of assumptions should be.

While Falkenhainer and Forbus do provide a general framework for composing models from fragments and organizing alternative levels of detail around modeling assumptions and assumption classes, there are some severe limitations in their approach. First, the assumption that scenario objects can be decomposed into a single partonomic hierarchy of objects that can be analyzed independently rarely applies to business organizations. Organizational functions and processes are often times intertwined. Cross functional interactions are vital to the success of the whole organization. Second, the FF approach cannot determine how those given quantities in the scenario interact with quantities of interest.

Ref. [51] modifies FF's automatic modeling idea by exploiting knowledge of interaction paths relevant to the question. They define an interaction as a functional or differential relation between two quantities. The relations in a model fragment can be treated as a set of interactions. By including the interaction path to guide the modeling process, given quantities and quantities of interest are related. This knowledge helps to select an appropriate scope for the model and to choose time scale abstractions, which is another important aspect in choosing the right model fragments (see also Ref. [39]). Each model fragment in the domain knowledge can include a set of time scale conditions (e.g., daily, weekly, or monthly time scales) which delimit the time scales of analysis for which the model fragment can be used. They provide the criteria for selecting among alternative levels of detail in our representation. The notion of time scales is also very important in our business setting because in most real life situations there are many different processes working at different speeds. Furthermore, the points of view that users want their models to reflect may depend upon daily, monthly, quarterly, or annual changes and updates. In a complex organization, the type of model fragments would presumably include very different time scales. Thus there is not only the question of separating or interconnecting such fragments or components, but of designing the algorithm as well in such a way that it would take time scales into account.

Another notable AI approach to reasoning with multiple models is the graphs of models framework by Addanki et al. [1], which expresses physical domains as graphs where the nodes represent models and the edges represent the assumptions that have to be changed in order to switch between different models. Ref. [56] introduces a model management system which reasons about one dimension of modeling assumptions. Given a query it selects through refinement techniques a model with an appropriate level of detail, which might be qualitative or quantitative. Finally, Ref. [47] presents an approach for automatically generating (parsimonious) causal explanations of given physical phenomena. Causal ordering is used to build task-specific models from a set of model fragments consisting of causal relationships. A new concept called causal approximations is introduced in order to achieve tractability of the model selection method, at the expense of less accurate explanations.

## 3.2. Reasoning with multiple models in decision support systems

Model integration consists of identifying relevant models and properly combining them and other DSS components that are needed to respond to a specific query. The current stream of DSS literature argues for an approach in which model integration is achieved by relating existing models to each other, thus creating higher level structures. One of these approaches is that a model is viewed as a virtual relation, and model management is the organization and processing of virtual relations $[10–12]$ . When a change is made in a model, the entire virtual file is changed. The functional dependencies found in models (i.e., virtual relations) are causal dependencies. Because of this, sensitivity analysis is often performed on models. For example, in an order quantity model, changing a demand (an input) will change the corresponding order quantity (an output). One might perform sensitivity analysis to determine the effect of a change in demand has on order quantity. Model integration is accomplished by performing joins across the virtual relations. A join of two models occurs when the output of one model is the input to another model. One technique of doing the model integration, that is, the join, is AND/OR graphs [13], in which the AND operation is used to combine two dissimilar models and the OR operation is used to combine two similar models that have the same outputs but use different inputs or are based on different assumptions.

AND/OR graphs are also used in Ref. [42] to represent collections of related models and to drive model integration and selection. The author uses acyclic AND/OR graphs to capture all possible paths for producing the requested outputs. A path is a sequence of edges which connect some AND nodes and some OR nodes which implies an appropriate model. However, it does not guarantee that the model will generate a feasible solution.

Basu and Blanning [6] present another graph-based approach that exploits the structural and analytical properties of so called metagraphs to address some important questions in model integration. Meta-graphs allow more than two elements to participate in an edge while capturing the direction of the input-to-output relationship among the elements. An edge represents a model. If there exists a path between two elements $a$ and $b$ , then it is possible to compute a value for $b$ , starting with $a$ as input, by executing the models corresponding to the edges in the path in a strict sequence based upon their positions in the path. This path between $a$ and $b$ is called a simple path. The variables needed in addition to $a$ to compute $b$ are co-inputs and the values of other quantities we get besides $b$ are co-outputs. Another important concept is the metapath which represents non-sequential interactions between edges when the set of needed edges does not form a simple path. Model integration is achieved by searching the adjacency matrix of the graph to find the relevant metapaths. One of the limitations of this approach is that there is no explicit representation of modeling assumptions. Users do not know under what conditions the relationships between variables hold. Another issue is that there is not a notion of models in this approach. Though edges are called models, however, they are really only unspecified relationships between variables.

There is another stream of research which uses object-oriented approaches to model building. Ref. [22] proposes an object-oriented, integrated modeling environment based on the structured modeling language (SML) [26], where an overall task such as production and distribution planning is decomposed into several interacting subtasks where each subtask is modeled individually. They present a model control language which allows the user to specify a collection of predefined models as communicating processes. A cost accounting model, for example, could calculate product prices as its output which would be sent as an input to a forecasting model, which in turn would predict a demand which could be sent to a production planning model, and so forth.

Ref. [43] presents another object-oriented approach to modeling the level of details among models. They use three kinds of representation to represent models: model types that are classes of models defined by a collection of assumptions, model templates that add application knowledge to model types through decomposition and specialization of components, and model instances that are inputs to model templates. This knowledge representation approach uses inheritance to represent the level of generalization and instantiation to represent the level of details among models. Inexact search operators are used to support the content-based retrieval and model identification steps of the model life cycle.

Ref. [46] reports on a model management system called SYMMS that offers a model description and configuration language which enables the modeler to reuse and connect predefined models. For example, a production planning model which is formulated as a linear program could be coupled with a forecasting model which would provide demand figures as the right hand side parameters of the linear program. However, the matching of the shared variables, in this case the demand variables, which establishes the model-model linkage needs to be done explicitly by the user by writing a control module which pairs the output of the forecasting model with an input port of the production.

While all these approaches support model reuse and model integration, essential modeling decisions are still left up to the user, who is responsible for checking model compatibility and for sequencing and synchronizing the model solving process. These modeling decisions made by the user are based upon a set of assumptions which are often only implicitly expressed in the composite model. There is very little support for ensuring the sufficiency and consistency of the assumptions being used. We believe that these limitations can only be overcome by explicitly representing the underlying modeling assumptions which are necessary to compose a model. Ref. [13] first suggested the use of first-order predicate logic for stating the conditions which imply the application of certain model units, an idea which is also used in Ref. [24], and which we shall employ for organizing the domain knowledge in our model base.

## 4. The organizational knowledge base

In this section, we discuss the knowledge management principles of the organizational knowledge base (OKB) underlying our enterprise modeling framework. We view the OKB as a repository of organizational knowledge whose purpose is to provide a resource of sharable and reusable model pieces for helping to better understand, explain, and predict organizational phenomena in a variety of different situations. In order to achieve the necessary depth and versatility, the OKB needs to contain knowledge of different types: (i) relationships among organizational variables encoded as quantitative or qualitative constraints; (ii) their preconditions and associated modeling assumptions that define the presuppositions under which they hold; and (iii) knowledge about knowledge expressed as metarules which relate modeling assumptions to each other.

One of the main challenges in designing organizational knowledge bases is to decompose the vast body of knowledge available from different sources into semi-independent model building blocks in a manner that allows the EMS to assemble integrated, task-specific models under a wide range of scenarios. Merging several model components into an integrated, composite model requires not only a careful approach of grouping relationships into independently meaningful units, but also an explicit treatment of the modeling assumptions which describe when they apply.

The observation that a model consists of more than just a set of relationships, because a model always assumes a particular modeling context, leads us to a definition of an EMS model component where the modeling assumptions are explicitly and separately expressed from the actual relationships. Since these model components are intended to be used as building blocks to construct customized, higher level models, they are also called model fragments. We argue for different representation languages to represent the underlying assumptions of a model fragment and its constituting relationships, which we describe in the next two subsections. Each model fragment has two sections, one contains the specification of modeling assumptions (conditions section) and the other (relations section) contains the actual constraints and relationships that apply if the model assumptions hold. Before a model composition algorithm can actually search the model base and identify task-specific, relevant model fragments, it needs sufficient information to be able to evaluate the predicates in the model assumption section. This extra information needs to be either derived directly from the query or inferred from metaknowledge present in the OKB. Metaknowledge is to be specified separately from the model fragments as a set of rules. These metarules express integrity constraints which rule out incoherent and inconsistent combinations of modeling assumptions, and also imply additional conditions as a consequence of modeling assumptions that have been already established.

## 4.1. Representation of modeling assumptions

Conventional model building relies foremost on the modeling skills and the domain expertise of the human modelers. Normally, models are specified with a particular application in mind, thus establishing a problem context which allows one to tune models for the purpose of solving specific problems. However, when doing so, modelers make modeling assumptions which are used to justify model simplifications and specialization. While resulting models may be effective for the particular task, they are also highly context-dependent, and their reuse is limited to problems with the same scenario. Conventional modeling languages do not facilitate an explicit representation of assumptions, hence it is the modeler who is responsible for choosing an adequate set of modeling assumptions and for formulating a model accordingly. Automated model building, on the other hand, can be done successfully only if the modeling system has the capability to represent modeling assumptions and also to reason about them when constructing models. Therefore, we require that all EMS model fragments have to be qualified by explicitly stating the modeling assumptions under which they apply. As first suggested by Bonczek et al. [13], we use first-order predicate logic to represent modeling assumptions and specify each model fragment as a logical implication, where the set of the relationships would be the consequence, and the modeling assumptions which are expressed as a conjunction of predicates would be taken as the antecedent.

In order to enable the EMS to reason about assumptions effectively while engaged in a model building task, we must define a taxonomy of modeling assumptions for characterizing managerial decision problems in the realm of business and management. Modeling choices must be made along several dimensions. Hence, we group together those assumptions which represent alternative ways of modeling a certain aspect of a problem scenario. Such groupings of assumptions, each capturing one modeling dimension, called assumption classes, are defined for all modeling dimensions. Assumption classes are organized as sets of mutually exclusive modeling assumptions. Before the EMS begins searching the model space for task-relevant model fragments, it chooses a particular assumption from each assumption class. The EMS uses the resulting conjunction of modeling assumptions to guide model composition and to narrow the search scope of the OKB.

We distinguish between several categories of modeling assumptions.

(1) Ontological assumptions take a certain perspective on the enterprise and select an appropriate method of description. Should the organization be viewed as a collection of employees who are working towards a common, cooperate goal? Should the organization be described as a collection of interacting subunits such as functional departments where the interaction might be represented as information flows, influence flows, cash flows, or material flows? Ref. [35], for example, suggests a variety of perspectives including customer perspective, innovation and learning perspective, and several internal business perspectives. Ontological commitments shift focus to a particular perspective of the enterprise, and indicate if a cost analysis, a productivity analysis, or if some other kind of analysis is appropriate.

(2) Topological assumptions provide structural information on the organization considered. The entire enterprise should be organized as a system of linked subsystems such as branches, departments, or other functional business units. For example, the manufacturing department is part of the company, and plant X is part of manufacturing.

Next, we introduce simplifying assumptions which reduce model complexity and help focus the model-building process and the subsequent model-solving process by ignoring influences which are presumably insignificant for answering the posed query. We divide simplifying assumptions further into granularity assumptions, approximations, and abstractions.

(3) Granularity assumptions determine the level of detail for a given analysis. A production scheduling analysis may require the consideration of each worker and piece of machinery involved in the manufacturing process of the products. A strategic marketing study might need a more aggregated view, and suggest a study in terms of product groups without explicitly considering any details of the manufacturing process.

(4) Approximations are mainly used to simplify a model for computational benefits. Linearity assumptions and treatment of variables as constants, for example, abound in all modeling contexts.

(5) Abstractions are used to reduce the complexity of phenomena. Operative management problems, for example, may require a factual representation while strategic management problems usually suggest a more abstract representation. Choosing an abstraction assumption commits the EMS to a specific level of abstraction and thus determines if the scenario model uses a quantitative, a qualitative, or some hybrid form of representation.

(6) Time scale assumptions indicate under what time scale the fragment is applicable. Enterprise processes work on time scales of different orders of magnitude. For example, some manufacturing processes like jobs scheduling are best modeled at a time scale of hours or even minutes. Other models may be better represented in time units of days, like production planning models; weeks, like cash flow models; months, like sales predictions; or even quarters and years for strategic planning models. A question asking for the key factors which effect the future performance of the company should contain a hint that allows the system to infer if the question refers to short-term performance, or to long-term performance. A short-term analysis could penalize investments whose payoffs materialize only in the long run. Long-term analyses usually suggest less detail or a higher level of abstraction, because of their more strategic nature, and because uncertainties about future events and developments over time. (See Table 1).

Table 1  
Examples of business processes operating at different time scales

<table><tr><td>Time scale</td><td>Business process</td></tr><tr><td>Hour</td><td>Job scheduling</td></tr><tr><td>Day</td><td>Production planning</td></tr><tr><td>Week</td><td>Cash flow</td></tr><tr><td>Month</td><td>Sales prediction</td></tr><tr><td>Quarter or year</td><td>Strategic planning</td></tr></table>

(7) In order to help generating parsimonious answers and to ease model simulation, another class of modeling assumptions called operating assumptions is introduced. Operating assumptions narrow the scope of the model space search, and delimit different ranges of behavior. Operating assumptions help to focus model simulation by determining, for example, whether a static, quasi-static, or a dynamic analysis is appropriate.

We think that these seven different types of modeling assumptions cover most distinctions which are implicitly made when human modelers formulate traditional, monolithic models. However, our list of assumption categories is meant to be neither exhaustive nor indisputable. Quite on the contrary, we propose it as a rather prototypical assumption schema which serves not only to furnish our the compositional modeling strategy but also to stimulate further discussion. As a matter of fact, we believe that the development of comprehensive and commonly agreed on business ontologies and assumption taxonomies is one of the most important open research topics in enterprise modeling.

## 4.2. Representation of organizational relationships

In this section, we describe how organizational knowledge is represented in our EMS framework. A common pitfall of traditional DSS systems is their rigid representation of modeling information. Usually, modelers are forced to formulate the relationships of a model as a set of homogeneous constraints, typically quantitative constraints of one specific kind such as linear algebraic equations. To accommodate the inherent heterogeneity of organizational knowledge, different representational forms are considered to specify relationships. Monge [45] and Weick [54], for example, have observed that theoretical and especially empirical organization science/management (OS/MT) research has been impeded by the lack of appropriate conceptual and computational tools to model inexactly, vaguely, or qualitatively specified systems. This has lead to a dominance of linguistic analyses in most of the theoretical OS/MT research, and also to numerous ill-advised applications of statistical test methods and regression analyses in empirical work. Present qualitative OS/MT studies rely chiefly on verbal discourses or other informal approaches, but in order to formulate, test and verify theories more formalized methods are needed. Research in the still very young field of qualitative reasoning has produced several formal approaches of representing and computing with qualitative information. Therefore we argue that organizational computing systems must be able to process qualitative information. We propose the provision of at least one qualitative representation language and one quantitative modeling language for specifying algebraic and dynamic relationships as a minimal requirement in designing EMS systems. In the following, we discuss four different kinds of relationships which we want to include into our EMS framework, and suggest how to represent them in the OKB model fragments.

## 4.2.1. Purely qualitative relationships

Theories in management typically encompass general statements which apply to whole classes of organizations. Hence, management theories try to discover commonalities among all organizations (of a certain class) with general validity, which can sometimes only tenuously be described as certain trends, influences or tendencies. A widely used practice in research areas such as organization science, management, and behavioral information systems is to use qualitative descriptions in order to formulate causal and functional relationships as general propositions. The abundance of uncertainties and vagueness, which is actually very characteristic of organizational knowledge, often inhibit the specification of precise quantitative models. Qualitative statements are typically based on hypothesized monotonic relationships of the form if variable X is increased (or decreased) then variable Y will increase (or decrease). For example, (a) Ref. [16] states the qualitative proposition “Increasing the level of partnership among organizational units leads to an increase in the productivity of the entire organization”, and (b) Ref. [33] hypothesizes that “For a highly centralized organization, use of computer-assisted communication and decision support technologies (i.e., information technology (IT)) leads to more decentralization.” Each of these two propositions verbally expresses a monotonic relationship between two variables, which is very common in the OS/MT literature. Qualitative relationships of this kind can very well be represented in the QSIM $^{2}$ modeling language as M $^{+}$ /M $^{-}$ constraints, and then stored in the organizational knowledge base. Thus, we propose to use QSIM to represent qualitative knowledge in our EMS framework $^{3}$ , and specify relationship (a) as a QSIM constraint

## (a) PRODUCTIVITY = M $^{+}$ (PARTNERSHIP)

and relationship (b) similarly as

$$
\text {(b) DECENTRALIZATION} = \mathrm{M} ^ {+} (\mathrm{IT})
$$

However, while relationship (a) is formulated as a generally applicable statement, relationship (b) is conditioned on the assumption that we are operating in a highly centralized organization. This means that we additionally need a corresponding predicate in the modeling assumptions section of the model fragment, which may be done by specifying CENTRALIZED(ORGANIZATION\_XYZ) as an explicit modeling assumption.

## 4.2.2. Semi-qualitative relationships

Functional relationships are often partially known. In addition to knowing purely qualitative properties such as monotonicity, we may have some numerical information which, although insufficient to specify the precise form of the relationship, should not get lost in our modeling effort. An EMS should offer a designated representation language to capture those semi-qualitative descriptions. We suggest to use the RCR $^{4}$ modeling language which is suitable in cases where the relationship of interest can be bounded by envelope functions. Some purely qualitative relationships obtained from qualitative management theory can actually be refined with respect to particular companies under consideration. For example, Fig. 2a shows one possible depiction of the relationship “increasing promotional expenditure causes increasing sales volumes,” which would be specified in QSIM as

## (c) SALES = M $^{+}$ (PROMOTIONAL\_EXP)

In this formulation, (c) is a purely qualitative relationship which simply says that sales will monotonically increase with higher promotional expenditures. An $M^{+}$ relationship defines an entire class of monotonically increasing functions f. Let s denote SALES and p denote PROMOTIONAL\_EXP. Then we can say that the above relationship (c) defines a functional relationship $s = f(p)$ up to the qualitative property $f'(p) > 0$ , that is, it defines f as a member of a particular class of functions M, namely $f \in M = \{g | g' > 0\}^5$ , a class which includes, for example, exponential curves, lines, and arbitrary monotonic wiggles. Even when we propose such a qualitative relationship we realize that there exists a precise functional relationship between sales and promotional expenditure. However, the true relationship

![](/api/attachments/64AUZY2R/fulltext/images/a7c28c04959626d706035e05b245ac07dfc5e1d26959c2c46dc70d8a3adb10f0.jpg)

![](/api/attachments/64AUZY2R/fulltext/images/f76e472d8578208e93a65309879df6f16da5ab4c05cc6d9f82512817f857f253.jpg)  
(a) First Expert

![](/api/attachments/64AUZY2R/fulltext/images/16cb1ac7a0b9b61f4e48948edfadbfd391497af80e124cce6170fb6c9afa59b9.jpg)  
(b) Second Expert

![](/api/attachments/64AUZY2R/fulltext/images/819f6d0f7c810c79e242f4391728c7b1acaf078c9f31df4d27ffba05744ad106.jpg)  
Fig. 2. (a) Purely qualitative relationship. (b), (c) Divergent range specifications. (d) Compromise range specification.

remains hidden to us for various reasons such as (i) limited cognitive capabilities may prevent us from discovering it, (ii) complete knowledge discovery could be too expensive, (iii) perhaps we are only interested in qualitative properties anyway.

Relationship (c) could be specialized, if needed for better accuracy, to mirror the company's specific experiences and projections, and be restated more precisely by including specific ranges of the expected increase. Using the RCR language for representing such semi-qualitative constraints, we could restate the above relationship as

$$
\begin{array}{r l} \text {(c1) SALES =} & \left[ \mathrm {lb(PROMOTIONAL\_EXP)}, \right. \\ & \left. \mathrm {ub(PROMOTIONAL\_EXP)} \right] \end{array}
$$

where lb(PROMOTIONAL\_EXP) denotes a lower bounding function, and ub(PROMOTIONAL\_EXP) denotes an upper bounding function of the qualitative relationship between promotional expenditure and sales. More formally, we can say that relationship (c1) defines a class of functional relationships, $s = f(p)$ , where $f \in M' = \{g | lb(p) \leq g(p) \leq ub(p)\}$ . In order to get specific bounds on relationship (c1), competent experts could specify ranges for this relationship, as shown in Fig. 2b and Fig. 2c.

Using interval analysis it is straightforward to reconcile inconsistent range specifications by taking the union of intervals. In this case, we might get a compromise formulation, shown in Fig. 2d, which would then be added to the model base as a new fragment.

## 4.2.3. Definitional relationships

Definitional relationships are relations that hold by definition. They are usually valid in a quantitative sense as well as in a qualitative sense. For example, the fundamental accounting equation “total assets (TA) equals total liabilities (TL) plus stock owner’s equity (SE)” could be specified as

## TA = TL + SE

which could be used to build (1) a qualitative, QSIM-type constraint in which case the plus would be interpreted as qualitative addition; (2) a semiqualitative, interval-based RCR constraint; and (3) a quantitative model in which the definitional relationship would be instantiated as a conventional, algebraic equation, and incorporated into a model fragment.

## 4.2.4. Quantitative relationships

Finally, quantitative relationships could be, in principle, all kinds of equational constraints that are commonly used in MS/OR-type of models. Quantitative solution techniques, however, are often developed for a particular model type. Consequently, the issue of solver integration becomes especially important when integrating quantitative model fragments.

Quantitative model fragments can be isolated pieces of information, possibly just a single equation, or they could be larger model components which were derived from previous modeling efforts, like existing planning models, operative scheduling models, statistical forecasting models, or logistics models.

## 4.3. An illustrative example of an organizational knowledge base

In this section, we give an example that illustrates how the EMS principles discussed above apply to the development of an OKB model. The OKB is a pool of heterogeneous organizational knowledge, represented as model fragments, which encompasses both general domain and enterprise-specific knowledge. Constructing such an OKB is naturally an ongoing process and a tremendously time consuming and costly project in itself. For the purpose of this paper, showing just a small segment of an OKB shall be sufficient to demonstrate the essential features of an OKB. Recall that a model fragment consists of two major parts: one that contains the conditions under which the model fragment is applicable, the preconditions section, and another that encodes the actual relationships of the model fragment, the relations section. In exhibit 1, we show parts of the OKB of the hypothetical CORPX enterprise. The complete enterprise description would obviously be much more elaborate. For the sake of simplicity, we have left out some of the details in the relationships sections which would be necessary in order to render a composite scenario model solvable by any particular solution method selected such as QSIM or RCR. Model fragments are essentially of the form

## fragment $\langle NAME\rangle$ (input port) (output port)

{verbal description of the functionality of the model fragment}

## conditions

precondition specifications

## relations

relationship specifications

end

Here $\langle NAME\rangle$ is an identifier of a particular model fragment instance, input port is a list of the variables whose values need to be provided, either by computing them in other model fragments or by importing them as exogenous quantities, output port is a list of the variables which are computed by this model fragment, and which can be shared with other fragments. The conditions section contains precondition specifications, which define the modeling assumptions that an instantiation of a model fragment depends on. Lastly, the relations section contains relationship specifications, which would be constraints of a particular modeling language. We only assume that internally, that is, within a single model fragment, the relationships are of a homogeneous type. Across model fragments, heterogeneous relationship specifications are permitted by using several modeling languages.

Besides the definition of model fragments, the OKB also contains rules which further constrain the use of the model fragments, thus help to eliminate potential model candidates. For example, in the beginning of our enterprise modeling project at CORPX we may restrict our studies to using quasi-static models $^{6}$ . Hence, we have included this restriction as rule R-1 in our CORPX OKB in a separate rules section. Another rule, R-2, selects QSIM as the only solver for purely qualitative scenario models, and rule R-3 chooses RCR as the only solver for semi-qualitative models.

The organizational memory and intelligence of the EMS, however, resides mainly in the interaction graph, shown in Fig. 3, which represents knowledge about organizational knowledge. It is used in the OKB as a comprehensive model of the enterprise. More specifically, the interaction graph relates organizational variables, organizational relationships, modeling assumptions, and model fragments to each other. The nodes of the interaction graph represent organizational variables and arcs connecting two nodes indicate the existence of a relationship between the two corresponding variables. Notice, that unlike Forbus and Falkenhainer and other approaches in DSS, we do not assume that the variables and relationships are organized in a hierarchical manner. Arc labels identify model fragments containing such relationships. The specification of a relationship cannot be directly obtained from the interaction graph, but must be retrieved from the relations section of the containing model fragment. Likewise, modeling assumptions are to be found in the conditions section of the identified model fragment. Finally, self-loops, that is, arcs which leave from and return to the same node, indicate that the corresponding variable could be treated as being exogenous.

![](/api/attachments/64AUZY2R/fulltext/images/0441410e2496616fac5b9e895b56b61a186f53837b3680e3e247f9c4d39cde18.jpg)  
Fig. 3. Interaction graph of OKB CORPX.

In the lower left corner of Fig. 3, we can see, for example, that model fragment $f_{2}$ contains a relationship among the variables usage of Information Technology (IT) and Productivity (Prd). This means that if we want to build a model which predicts or explains the value of Productivity, we need to consider fragment $f_{2}$ as a potential building block. The actual specification of the relationship and its associated modeling assumptions represented by the arc $\langle IT-Prd\rangle$ can be looked up in the definition of fragment $f_{2}$ , which is shown below. In this case, we find the monotonic relationship Productivity = $M^{+}(IT)$ , which holds if the four modeling assumptions OntologyAssumption = influences, SimplifyingAssumption = qualitative, OperatingAssumption = quasi-static, and TimeScaleAssumption = medium are satisfied. Hence, if we are building a qualitative model describing, among other things, the impact (or influence) of IT usage on Productivity, we must consider the inclusion of fragment $f_{2}$ in the composite scenario model to be built.

In general, arcs emanating from a node x indicate the variables directly influenced by variable x. Thus, usage of IT has, in our enterprise model, a direct impact on Partnership, Productivity, and Customer Service. However, besides the direct influence of IT on Productivity, there is also an indirect influence of IT on Productivity, via Partnership. Indirect influences are represented in the interaction graph as a sequence of arcs called an interaction path. Here, the sequence $\langle IT-Pship\rangle-\langle Pship-Prd\rangle$ , or more compactly written as $\langle IT-Pship-Prd\rangle$ , expresses the indirect influence of IT on Productivity. Similarly, IT has many more indirect influences on other variables, for example, the interaction paths $\langle It-Prd-Perf-Gw\rangle$ and $\langle IT-CSrv-CSat-Gw\rangle$ represent alternative possibilities of modeling the indirect influence of IT on Goodwill. Incoming arcs of a node x represent the direct influences on variable x. Our example indicates that Productivity is directly influenced by IT usage and Partnership. However, IT has a self-loop as the only incoming arc. The arc going from node IT back to itself means that the only influence on variable IT is IT itself, in other words, IT cannot be explained within the enterprise model. IT has to be determined outside of the model, that is, IT is treated as an exogenous variable whose value needs to be imported from a separate database when IT is included in a scenario model. Exogenous variables are typically variables which are, at least to some extent, controllable. The level of IT, for example, is determined by the budget proposed and passed by the management.

An arc label actually consists of a list of fragment identifiers. Such a list may be empty, as in the case of arc $\langle IT-IT\rangle$ , indicating an exogenous variable; may contain one identifier, as in $\langle IT-Prd\rangle$ meaning that the OKB knows only about one relationship between IT and Prd; or it may contain several identifiers suggesting alternative relationships. Two examples of multiple relationships are, first, arc $\langle Price-Rev\rangle$ which lists two fragments, $f_{22}$ and $f_{23}$ , both using a relationship between price and revenue, and, second, arc $\langle Price-Sales\rangle$ which names three alternatives, fragments $f_{18}$ , $f_{19}$ and $f_{20}$ , of modeling price and sales. Relationships involving more than two variables are identified by any of the participating variables. For example, fragment $f_{28}$ , which specifies a relationship between three variables net income (NInc), cost (Cost) and revenue (Rev), must be instantiated when either of the two arcs $\langle Cost-NInc\rangle$ and $\langle Rev-NInc\rangle$ is considered.

Exhibit 1: OKB CORPX
ALIASES
/Partnership, Pship/
/Product\_Quality, PQual/
/Customer\_Satisfaction, CSat/
/Customer\_Service, CSrv/
/Marketing\_Position, MPos/
/Promotional\_Expenditure, PrmExp/
/Productivity, Prd/
/Information\_Technology, IT/
/Revenue, Rev/
/Net Income, NInc/
/Production Cost, PCost/
/Performance, Perf/
/Goodwill, Gw/
END
ASSUMPTION CLASSES
/Ontology Assumption, OntAss/ (influences, cash flow, material flow)
/Simplifying Assumption SimpAss/ (qual, semi-qual, quant)
/Operating Assumption, OpAss/ (static, quasi-static dynamic)
/Time Scale Assumption, TScAss/ (short, medium, long)
END

fragment f1 (IT) (Pship)
{qualitative model describing the relationship between IT and Partnership}
conditions
OntAss = influences, SimpAss = qual,
OpAss = quasi-static, TScale = medium
relations
Partnership = M $^{+}$ (IT)
end

fragment f2 (IT) (Prd)
{qualitative model describing the relationship between IT and Productivity}
conditions
OntAss = influences, SimpAss = qual,
OpAss = quasi-static, TScal = medium
relations
Productivity = M $^{+}$ (IT)
end

fragment f3 (Prd) (Pship)
{qualitative model describing the relationship between Productivity and Partnership}
conditions
OntAss = influences, SimpAss = qual,
OpAss = quasi-static, TScale-long

relations
Productivity = M $^{+}$ (Partnership)
end
....

fragment f18 (Price) (Sales)
{marketing model describing the qualitative relationship between Price and Sales volume}
conditions
OntAss = influences, SimpAss = qual,
OpAss = quasi-static, TScale = medium
relations
Sales = M $^{-}$ (Price)
end

fragment f19 (Price) (Sales)
{marketing model describing the semi-
quantitative relationship between Price and Sales
volume}
conditions
OntAss = cash\_flow, SimpAss = qual-quant,
OpAss = dynamic, TScale = short
relations
Sales(t) = [68000, 92000] + [40000, 48000] × Price(t)
end

fragment f20 (Price) (Sales)
{marketing model describing the quantitative relationship between Price and Sales volume}
conditions
OntAss = cash\_flow, SimpAss = quant,
OpAss = quasi-static, TScale = short
relations
Sales = 80000 - 44000 × Price
end

fragment f21 (Sales) (Rev)
{accounting model describing the qualitative relationship between Sales volume and Revenue}
conditions
OntAss = influences, SimpAss = qual,
OpAss = quasi-static, TScale = medium
relations
Revenue = M $^{+}$ (Sales)
end

## fragment f22 (Price) (Rev)

{accounting model describing the qualitative relationship between Price and Revenue}
conditions
OntAss = influences, SimpAss = qual,
OpAss = quasi-static, TScale = medium
relations
Revenue = M $^{+}$ (Price)
end

## fragment f23 (Price, Sales) (Rev)

{accounting model describing the quantitative relationship between Price, Sales volume, and Revenue}
conditions
OntAss = cash\_flow, SimpAss = quant,
OpAss = quasi-static, TScale = medium
relations
Revenue = Price × Sales
end

fragment f24 (Rev) (NInc)
{accounting model describing the qualitative relationship between Revenue and Net Income}
conditions
OntAss = influences, SimpAss = qual,
OpAss = quasi-static, TScale = medium
relations
NetIncome = M $^{+}$ (Revenue)
end

fragment f25 (Cost) (Price)
{financial model describing the qualitative relationship between Cost and Price}
conditions
OntAss = influences, SimpAss = qual,
OpAss = quasi-static, TScale = medium
relations
Price = M $^{+}$ (Cost)
end

fragment f26 (PCost) (Cost)
{financial model describing the qualitative relationship between Production Cost and Total Cost}
conditions
OntAss = influences, SimpAss = qual,
OpAss = quasi-static, TScale = medium
relations
Cost = M $^{+}$ (ProductionCost)
end

## fragment f27 (Cost) (NInc)

{financial model describing the qualitative relationship between Cost and Net Income} conditions
OntAss = influences, SimpAss = qual,
OpAss = quasi-static, TScale = medium relations
NetIncome = M $^{-}$ (Cost)
end

## fragment f28 (Cost, Rev) (NInc)

{accounting model describing the quantitative relationship between Cost, Revenue, and Net Income}
conditions
OntAss = cash\_flow, SimpAss = quant,
OpAss = quasi-static, TScale = medium
relations
NetIncome = Revenue - Cost
end

fragment f29 (Perf) (Gw)
{marketing model describing the qualitative relationship between Performance and Goodwill}
conditions
OntAss = influences, SimpAss = qual,
OpAss = quasi-static, TScale = medium
relations
Goodwill = M $^{+}$ (Performance)
end

R-1: OpAss(quasi-static)

R-2: SimpAss(qual) $\Rightarrow$ solver(QSIM)

R-3: SimpAss(qual-quant) $\Rightarrow$ solver(RCR)

R-4: ...

end

## 5. A model composition strategy

We refer to the real-world phenomenon under study as a scenario, and to the model representing it as a scenario model. Selecting the right model pieces to compose an appropriately integrated model for answering a given query requires modeling decisions along several dimensions. What is the best set of variables to be included in the model? What level of detail is appropriate? Which are the relevant organizational phenomena for studying the posed question? From what perspective should the problem be viewed? What kinds of approximations and abstractions should be allowed? Even the most carefully organized model fragment library would not provide enough information to find an answer to all of these questions. Therefore, we need to derive missing pieces of information from the query itself, that is, we need to look for clues provided in the query that could narrow the focus of the model composition process and reasonably constrain the set of plausible modeling assumptions. Further restrictions on the model space of a scenario can be imposed by defining a modeling environment, and specifically by setting modeling control parameters which select modeling options and heuristics that limit the search space and the scope of the scenario model $^{7}$ . The user may set and change these parameters at any time, or rely on the defaults provided by the EMS.

## 5.1. Model selection

As an example of composing a scenario model in response to a prediction question, let us consider, for example, the query “How does an increase in price affect net income?”. To interpret this, the query analyzer must figure out what the query is aiming at, and must recognize the objects and adhering manipulations addressed in the query. In this case, the user is asking for a prediction of the future behavior of the company’s net income. Hence, the query manager would declare the quantity net income as a goal variable. Moreover, it must find out what other quantities, called quantities of interest, the query refers to and how they relate to the goal variable(s). In our example, we would name price as another quantity of interest. The information hitherto defines the initial state of a scenario. Finally, we need to identify the manipulations mentioned in the scenario which the query describes, that is, we would hypothesize to increase the current value of price. Summarizing the analysis of this query, we would look for a model which computes net income and uses (at least) the quantity price. After interpreting a query, the query manager needs to supply the model management module with this information so that it can trigger the model building process properly. However, the model manager needs to receive statements in a format it can understand and execute. Typically, such a format would be much more primitive than the level at which the query manager operates. For example, it could be just a list of so called “ground expressions”, which are primitive modeling terms such as variables and operations. Therefore, the query manager is also responsible for translating a structured problem scenario description based upon natural language into a formal, lower level language understood by the model manager (see Fig. 4). To continue our example, the model manager would be furnished with the low level query {Increase(price), Quantity(net income)} as shown below.

![](/api/attachments/64AUZY2R/fulltext/images/92a681805405e04658d5d03aa9dccde8d41c67128970fcfef0b1e12198321aaf.jpg)  
Fig. 4. (a) Query language processing. (b) Example of a query.

Conceptually based on natural language processing, a query elaboration procedure would analyze the issued query and derive from it a set of ground expressions which would be passed on to the model manager module of the EMS for evaluation. Although we would very much like to employ a natural language processor in the design of an EMS user interface, we must concede natural language processing is beyond the scope of this paper and that implementing such an interface would certainly constitute a formidable task in itself. For some initial work in this direction see, for example, Crouch and Pulman [17] who have recently presented a restricted, natural language interface to a specialized planning system which allows a user to interactively build plans. In the absence of such a sophisticated, natural language based query analyzer, we could simply devise a primitive query language that basically lists a number of ground expressions permitting the system to identify objects, quantities and relations of interest. Hence, let us consider the simplified query {increase(Price), quantity(NetIncome)}, whose ground expressions increase(Price) and quantity(NetIncome) provide the input to the model manager.

The query indicates that we need a scenario model which computes net income. While the one ground expression quantity(NetIncome) of the query hints neither to a qualitative nor to a quantitative modeling approach, the other ground expression does provide a clear clue for a qualitative analysis. Since the increase operator indicates a desired direction of change without further specification, it suggests a qualitative model for investigating this effect on net income in the given scenario. Now, we could try to enumerate all possible combinations of model fragments, and to prune out those which either violate some of the modeling assumptions or prove to be irrelevant or insufficient regarding the query. However, this approach would be computationally too costly, considering the many combinations of model fragments, which would typically occur in an enterprise-wide environment. The number of modeling assumptions, on the other hand, tends to be much smaller, and therefore suggests a computationally better alternative by reasoning about combinations of modeling assumptions first, and then to select and integrate a suitable set of model fragments. We will come back to this computational issue below and discuss it in more detail.

Model composition begins with the derivation of an initial set of quantities of interest from the query. Quantities of interest correspond to variables which need to be included in the scenario model to be composed. In our example, we would take the query {increase(Price), quantity(NetIncome) and derive {Price, NetIncome} as the set of initial quantities of interest. The quantity operator in the second ground expression, {quantity(NetIncome)}, provides a hint that the value of the variable NetIncome is desired, which means that we are supposed to model a scenario wherein NetIncome is predicted. Variables to be predicted by a scenario model are called goal variables. The increase operator in the first ground expression, increase(Price), describes a manipulation to be performed on a variable. In this case we are supposed to (qualitatively) change the current value of price and then examine the effect of this change. Variables like Price which are to be changed initially in a way prescribed by manipulation operators in the query are called driving variables. Driving variables are used to drive the model building process by trying to establish a connection between them and the goal variables such that the values of the goal variables can be determined if an initial state description is given. In the example, we would try to build a model that computes NetIncome from Price. In order to accomplish this job, the EMS employs a compositional modeling approach which searches the OKB for relevant model fragments which then can be used to construct an appropriate model.

Before invoking the model composition process, we need to define a modeling environment that selects a set of modeling commitments that are appropriate for the given query. Most importantly, this includes the selection of query-consistent modeling assumptions. In general, this is an indeterminate task. Ideally, we would choose the most suitable option along each of the modeling dimensions that are defined as assumption classes in the OKB. However, we cannot expect that the query presented by the user conveys enough information to make indisputable decisions for all modeling assumption classes. For the sake of simplicity, let us suppose, in the example of this paper, that our query analyzer derives a uniquely determined modeling environment $^{8}$ . More specifically, we assume that

1. the encounter of the generic increase in the query implies a purely qualitative analysis

2. a qualitative analysis requires an ontological commitment to view the interactions in the enterprise as general influences between organizational variables

3. the organizational processes involving price and net income work at a medium time scale

4. we restrict the analysis to quasi-static models (at least for now)

Hence, we would select

(OntAss = influences, SimpAss = qual, OpAss

$= \text{quasi-static, TScale} = \text{medium}$

as the current set of modeling assumptions.

Unquestionably, many queries would lead to ambiguous decisions about those modeling assumptions. On the other hand, it actually would be desirable in such cases that the EMS would generate a scenario model for all plausible modeling environments, that is, for all combinations of modeling assumptions that could reasonably be derived from the query. Furthermore, in order to promote user interaction and extend user control with the EMS, the query language should allow the user to explicitly select some of the modeling assumptions anyway. And finally, one of the modeling control parameters could provide a confirmation option that forces the EMS to merely suggest important modeling decisions, and to seek user confirmation before proceeding. This would be especially useful in ambiguous situations in which the user could prevent the system from generating, and subsequently solving, unnecessary or unwanted models.

In an ideal setting one would certainly like to obtain a definite answer to a question asked. In a problem domain that abounds with incomplete and uncertain knowledge this is, however, rarely possible and even the best human experts in the field cannot accurately predict the outcome of organizational actions. A seemingly simple question such as our example on the effect of a price increase on net income has too many ramifications to allow one to formulate a model that is complete and correct in a sense that it includes exactly everything caused by a price increase, but nothing else, that influences net income. In an organizational environment we are dealing with numerous latent variables, that is, variables that relate to a given concept in some way but are not explicitly modeled because they are not yet identified or because their effect and level of impact is not fully understood. Even the most carefully designed organizational knowledge base will be incomplete in this sense. The mechanism that determines, for example, how the consumers will react to price changes of a product is simply too complex, and involves among other things the reaction of the competitors in the market, and the price elasticity of the product which in turn depends on many other factors and differs for each individual consumer. Nevertheless, using the experimental knowledge that is presently encoded in the organizational knowledge base, we can quickly derive important implications and possible consequences that should be accounted for in a decision-making process, and thus help to make better and faster decisions.

In the first step, the driving and goal variables are located in the interaction graph depicted in Fig. 3. Our example has only one of each, the driving variable price and the goal variable net income (NInc). Now, it needs to be checked whether initial values of the driving variables are provided. Initial values could be derived from the query, supplied by an external data base, or computed from other variables. The latter is computationally the most expensive possibility because it entails constructing a more complex scenario model, and is thus eschewed unless the former two fail. Our example query has no clue on the initial value of price. Fortunately, the second possibility applies, because the node representing price has a self-loop. This means that the variable price can be treated as an exogenous variable, that is, its current value can be obtained from an external source. Next, we try to connect the driving variables with the goal variables, that is, we search the interaction graph for interaction paths between driving and goal variables. Looking at Fig. 3, there are four interaction paths describing different ways of computing net income from price.

Each of the four generated interaction paths suggests to make use of a different collection of fragments for building a model that predicts how an increase of price would affect the net income of the CORPX enterprise. Potential scenario models, or model candidates, differ in their complexity measured in terms of number of variables and number of fragments involved in composing them. From Table 2 we can see that the first interaction path relates seven variables by six arcs identifying eight relationships represented in eight fragments. Since some of the arcs suggest a set of alternative relationships, we can choose from several different combinations of relationships and their associated fragments. As another example, the third interaction path in Table 2, Pricc–Rev–NInc, consists of three arcs $\langle Price-Sales\rangle$ , $\langle Sales-Rev\rangle$ , and $\langle Rev-NInc\rangle$ which suggest the sets $\{f_{18}, f_{19}, f_{20}\}$ , $\{f_{21}, f_{23}\}$ , and $\{f_{24}, f_{28}\}$ as possible fragments for modeling relationships between respectively price and sales, sales and revenue, and revenue and net income. Thus, any fragment triple

$$
\begin{array}{r l} & \langle F _ {1}, F _ {2}, F _ {3} \rangle \\ & \qquad \in \left\{f _ {1 8}, f _ {1 9}, f _ {2 0} \right\} \times \left\{f _ {2 1}, f _ {2 3} \right\} \times \left\{f _ {2 4}, f _ {2 8} \right\} \end{array}
$$

is an eligible candidate for a scenario model, resulting in $3 \times 2 \times 2 = 12$ combinations to choose from. Likewise, we can produce yet more candidate models, and represent them as fragment n-tuples where n denotes the number of participating fragments, from the other interaction paths. Specifically, the first interaction path generates four 6-tuples, the second four 6-tuples, and the last four pairs of fragments. All together, Table 3 lists a total of 24 candidates to consider when building a model of the scenario described in the given query “How does an increase in price affect net income?” Obviously, the number of model candidates varies with every query, and, in more intricate scenarios, can quickly reach an order of magnitude that is hard to manage.

In order to keep the model composition task tractable we would like to avoid a complete enumeration of possible model candidates. Since final scenario models have to be internally consistent, we must eliminate those candidates from further consideration whose constituting fragment's precondition sections contain contradictory modeling assumptions because this would indicate an incompatible set of model fragments. In our example above, we have hitherto ignored the modeling assumptions which the fragments are based upon. Prior to generating candidate models, we need to check the consistency of modeling assumptions. From the current modeling environment, we obtain the active set of modeling assumptions, (OntAss = influences, SimpAss = qual, OpAss = quasi-static, Tscale = medium) whereon the building of the scenario model rests.

Table 2  
Combinations of different interaction paths

<table><tr><td colspan="2">Interaction path</td><td># arcs</td><td># nodes</td><td># frags</td><td># models</td></tr><tr><td>1</td><td>Price-CSat-Gw-MPos-Sales-Rev-NInc</td><td>6</td><td>7</td><td>8</td><td>4</td></tr><tr><td>2</td><td>Price-CSat-MPos-Sales-Rev-NInc</td><td>5</td><td>6</td><td>7</td><td>4</td></tr><tr><td>3</td><td>Price-Sales-Rev-NInc</td><td>3</td><td>4</td><td>7</td><td>12</td></tr><tr><td>4</td><td>Price-Rev-NInc</td><td>2</td><td>3</td><td>4</td><td>4</td></tr><tr><td></td><td>Total</td><td></td><td></td><td></td><td>24</td></tr></table>

Model candidates generated from interaction paths (IP) using (OntAss = influences, SimpAss = qual, OpAss = quasi-static, TScale = medium) as the currently active set of modeling assumptions

<table><tr><td></td><td>IP</td><td>Model candidate</td><td>Model size</td></tr><tr><td>1</td><td>1</td><td> $(f_{12}, f_{8}, f_{9}, f_{14}, f_{21}, f_{24})$ </td><td>0</td></tr><tr><td>2</td><td>1</td><td> $(f_{12}, f_{8}, f_{9}, f_{14}, f_{21}, f_{28})$ </td><td> $(f_{28})$ </td></tr><tr><td>3</td><td>1</td><td> $(f_{12}, f_{8}, f_{9}, f_{14}, f_{23}, f_{24})$ </td><td> $(f_{23})$ </td></tr><tr><td>4</td><td>1</td><td> $(f_{12}, f_{8}, f_{9}, f_{14}, f_{23}, f_{28})$ </td><td> $(f_{23}, f_{28})$ </td></tr><tr><td>5</td><td>2</td><td> $(f_{12}, f_{10}, f_{14}, f_{21}, f_{24})$ </td><td>0</td></tr><tr><td>6</td><td>2</td><td> $(f_{12}, f_{10}, f_{14}, f_{21}, f_{28})$ </td><td> $(f_{28})$ </td></tr><tr><td>7</td><td>2</td><td> $(f_{12}, f_{10}, f_{14}, f_{23}, f_{24})$ </td><td> $(f_{23})$ </td></tr><tr><td>8</td><td>2</td><td> $(f_{12}, f_{10}, f_{14}, f_{23}, f_{28})$ </td><td> $(f_{23}, f_{28})$ </td></tr><tr><td>9</td><td>3</td><td> $(f_{18}, f_{21}, f_{24})$ </td><td>0</td></tr><tr><td>10</td><td>3</td><td> $(f_{18}, f_{21}, f_{28})$ </td><td> $(f_{28})$ </td></tr><tr><td>11</td><td>3</td><td> $(f_{18}, f_{23}, f_{24})$ </td><td> $(f_{23})$ </td></tr><tr><td>12</td><td>3</td><td> $(f_{18}, f_{23}, f_{28})$ </td><td> $(f_{23}, f_{28})$ </td></tr><tr><td>13</td><td>3</td><td> $(f_{19}, f_{21}, f_{24})$ </td><td> $(f_{19})$ </td></tr><tr><td>14</td><td>3</td><td> $(f_{19}, f_{21}, f_{28})$ </td><td> $(f_{19}, f_{28})$ </td></tr><tr><td>15</td><td>3</td><td> $(f_{19}, f_{23}, f_{24})$ </td><td> $(f_{19}, f_{23})$ </td></tr><tr><td>16</td><td>3</td><td> $(f_{19}, f_{23}, f_{28})$ </td><td> $(f_{19}, f_{23}, f_{28})$ </td></tr><tr><td>17</td><td>3</td><td> $(f_{20}, f_{21}, f_{24})$ </td><td> $(f_{20})$ </td></tr><tr><td>18</td><td>3</td><td> $(f_{20}, f_{21}, f_{28})$ </td><td> $(f_{20}, f_{28})$ </td></tr><tr><td>19</td><td>3</td><td> $(f_{20}, f_{23}, f_{24})$ </td><td> $(f_{20}, f_{23})$ </td></tr><tr><td>20</td><td>3</td><td> $(f_{20}, f_{23}, f_{28})$ </td><td> $(f_{20}, f_{23}, f_{28})$ </td></tr><tr><td>21</td><td>4</td><td> $(f_{22}, f_{24})$ </td><td>0</td></tr><tr><td>22</td><td>4</td><td> $(f_{22}, f_{28})$ </td><td> $(f_{28})$ </td></tr><tr><td>23</td><td>4</td><td> $(f_{23}, f_{24})$ </td><td> $(f_{23})$ </td></tr><tr><td>24</td><td>4</td><td> $(f_{23}, f_{28})$ </td><td> $(f_{23}, f_{28})$ </td></tr></table>

Table 3 shows for each model candidate those fragments that are incompatible because they violate some of the active modeling assumptions. Notice that only four (set in boldface) out of twenty-four model candidates are indeed internally consistent. Therefore, we devise a compositional modeling strategy which reasons first about the consistency of the modeling assumptions before it starts to assemble composite model candidates. This approach reduces quickly the search space of possible scenario models from 24 to just 4 candidates, namely $(f_{12}, f_{8}, f_{9}, f_{14}, f_{21}, f_{24})$ , $(f_{12}, f_{10}, f_{14}, f_{21}, f_{24})$ , $(f_{18}, f_{21}, f_{24})$ and $(f_{22}, f_{24})$ . Thus, our compositional modeling method concludes, for this example

{increase(Price), quantity(NetIncome)}

$$
\begin{array}{l} \Rightarrow \operatorname{or} \left(\left(f _ {1 2}, f _ {8}, f _ {9}, f _ {1 4}, f _ {2 1}, f _ {2 4}\right), \left(f _ {2 2}, f _ {2 4}\right) \right. \\ \times \left(f _ {1 2}, f _ {1 0}, f _ {1 4}, f _ {2 1}, f _ {2 4}\right), \left(f _ {1 8}, f _ {2 1}, f _ {2 4})\right) \end{array}
$$

All of these four possible models represent an alternative way of describing the effect of a price increase on net income. At present, our approach provides little information on how these model candidates relate to each other, besides that they are all consistent with the modeling environment derived from the user-specified query. Comparing the model candidates, all we can say is that they differ in complexity, measured in terms of number of variables and relationships. Which of the four possibilities is the best model in the given situation is in general an intractable problem $[47]$ and cannot be determined without making further assumptions.

## 5.2. Model evaluation

Since we have no explicit treatment of approximation or abstraction at the level of model candidates, we cannot derive a (partial) ordering such that we could select the most (least) approximate or abstract model as a final scenario model. However, using the observation that most analysts usually start with simple descriptions when studying a new problem and then move on to more complex and elaborate descriptions until they feel that they have gathered enough information to finally make a judgment or decision in a particular situation, we suggest the notion of appropriateness as a means of generating an order over model candidates. We assume that end-users are first interested in obtaining parsimonious problem descriptions before looking at more complicated ones, and we assume also that they are able to decide if and when a single model or a series of models is sufficiently appropriate to answer a question that is being investigated. Again, we would like to emphasize the role of enterprise modeling systems as a support tool for decision-making processes that bring to bear important implications of proposed managerial actions The decision-making function remains with the end-user who controls the amount of information collected and who makes the final judgments and assessments before arriving at a final decision.

Unfortunately, there is no single criteria that would alone by itself describe appropriateness in a satisfying way, which makes it difficult to provide a definition of it that is not arbitrary to some extent and, at the same time, operational. Ref. [24] defines the final scenario model as the model candidate which is coherent and most useful. The former criterion requires the scenario model to be consistent with the modeling assumptions to which the EMS committed when exploring the scenario set up by a query. The latter refers to the tradeoff between information cost and significance to the query in terms of sufficiency and minimality [4]. Sufficiency means that the answer to the query is firstly not only correct but also relevant to the question such that it provides her with the information sought, and secondly that the answer is also satisfactorily detailed and accurate. Minimality, on the other hand, calls for a parsimonious response and forbids elaborate details. In other words, we are looking for the scenario model which is minimal and (a) consistent, (b) valid, (c) relevant, (d) adequately detailed, and (e) adequately accurate.

The candidate evaluation module receives, from the model composition module as its input, a set of scenario model candidates, and produces as its output an order over the scenario models according to appropriateness. First, we need to ensure that the scenario model satisfies restrictions (a) to (e). Fortunately, our compositional modeling method was designed such that it generates only feasible model candidates, that is, candidates which do satisfy the above restrictions. Consistency is accomplished through the explicit reasoning about underlying modeling assumptions during the model building process. We can assume validity of the relationships used in building model candidates because model fragments are only applied if the assumptions stated in their preconditions section hold. We ensure relevance by assuming that our query analyzer identifies quantities of interest correctly, and that only such fragments are considered which the interaction graph relates to a driving variable or a goal variable. An adequate level of detail and accuracy is achieved by assuming that the query analyzer, in connection with user interaction, is able to derive and establish a proper set of modeling assumptions which include an appropriate description of level of detail and accuracy required in the given scenario.

Remaining models after eliminating incompatible models; model size measured in terms of the candidate evaluation function: $\text{eval}(m) = v + r$

<table><tr><td>Model candidate</td><td>Model size</td></tr><tr><td> $(f_{12}, f_8, f_9, f_{14}, f_{21}, f_{24})$ </td><td>13</td></tr><tr><td> $(f_{12}, f_{10}, f_{14}, f_{21}, f_{24})$ </td><td>11</td></tr><tr><td> $(f_{18}, f_{21}, f_{24})$ </td><td>7</td></tr><tr><td> $(f_{22}, f_{24})$ </td><td>5</td></tr></table>

Now that we are assured that all remaining candidate models are indeed feasible and appropriate in the sense that we can expect them to yield comparably satisfactory answers, we want to select the minimal or simplest one. Let us define simplicity of a model in terms of model size and define an evaluation function $eval(m)$ as a function of number of variables v and number of relationships r, for example as $eval(m)=v+r$ . From Table 4 we can see that candidate $(f_{22}, f_{24})$ is chosen as the first scenario model in our example and is passed on to the solver for model execution.

## 5.3. Model generation and integration

Using candidate model $M_{1}=(f_{22},f_{24})$ we obtain scenario model f22–f24 (Price) (NInc)

conditions

OntAss = influences, SimpAss = qual, OpAss = quasi-static, TScale = medium

relations

$$
\text { Revenue } = \mathrm{M} ^ {+} (\text { Price })
$$

$$
\text { NetIncome } = \mathrm{M} ^ {+} (\text { Revenue })
$$

end

as the scenario model that is first suggested to the end-user. This is not yet a completely specified model, one which could be solved as it is. However, it does show the complete specification of the model's constraints, the core part of the final scenario model.

Although it contains only valid relationships, a price increase leads, ceteris paribus, to higher revenues and higher revenues have a positive effect on net income, it may not be accurate enough for the user's current analysis. Model $M_{1}$ ignores, for example, the influence of price changes on sales which in turn also influence the goal variable net income. Hence, after inspecting the suggested scenario model, the user may opt for seeking a more accurate model and thus force the EMS to search for an alternative scenario model. In our example, the EMS would suggest model candidate $\mathbf{M}_{2} = (\mathbf{f}_{18}, \mathbf{f}_{21}, \mathbf{f}_{24})$ as its second scenario model.

scenario model f18-f21-f24 (Price) (NInc)

conditions

OntAss = influences, SimpAss = qual, OpAss =

relations

Sales = M $^{-}$ (Price)

Revenue = M $^{+}$ (Sales)

Netincome = M $^{+}$ (Revenue)

end

The new, more complex model $M_{2}$ does represent the indirect effect of price on net income by including sales as an additional variable and by adding another relationship. Depending on the user's intents, it may be beneficial to trade off some model cost (in terms of model complexity) for more accuracy. $M_{2}$ suggests that a price increase will lead to a drop in sales and revenues which in turn will diminish net income. Notice, that $M_{1}$ and $M_{2}$ predict opposite effects of a price increase. This may seem like a contradiction and one may argue that (at least) one of the two models must be ill-specified. However, recall that we view real-world enterprises as partially known systems that are too complex to enable us to discern a true model that would uniquely determine the future behavior of the enterprise system. It is this inherent ambiguity that is reflected in conflicting predictions. To the EMS both, an increase or a decrease in net income, may result from a price increase, and without additional information it cannot eliminate either possibility. In many situations, human experts are able to discard certain predictions on grounds of extra information and experience that is not encoded in thee organizational knowledge base or they are able to judge the likelihood of certain outcomes, and thus incorporate this experiential knowledge in their decision-making. Going back to our example, one would certainly agree that a price increase could lead to higher or lower revenues, and that it is impossible to determine which of the two will happen, unless more is known about the specific circumstances.

At this point the user may decide that the generated information is sufficiently appropriate or decide that more information is wanted before proceeding to the decision-making phase and hence terminating the session with the EMS system. In the latter case the EMS would continue by suggesting another more complex scenario model $M_{3}$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
scenario model f12-f10-f14-f21-f24 (Price)
(NInc)
conditions
OntAss = influences, SimpAss = qual, OpAss = quasi-static, TScale = medium
relations
CSat = M$^{-}$(Price)
MPos = M$^{+}$(CSat)
Sales = M$^{+}$(MPos)
Revenue = M$^{+}$(Sales)
NetIncome = M$^{+}$(Revenue)
end
</div>

Looking at model $M_{3}$ we can see that it implies the same prediction as $M_{2}$ , that is, a price increase results in a lower net income. $M_{3}$ , however, does also provide a basis for a more elaborate explanation than $M_{2}$ why this effect takes place. It gives more insight into the consumer choice process by explicitly including customer satisfaction and market position and their relationship to sales, and thus may help the decision-maker in better assessing and understanding the consequences of a price policy. A similar but slightly more intricate problem description can be obtained by choosing the last scenario model $M_{4}$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
scenario model f12-f10-f14-f21-f24 (Price)
(NInc)

conditions

OntAss = influences, SimpAss = qual, OpAss = quasi-static, TScale = medium

relations

CSat = M$^{-}$(Price)

Gw = M$^{+}$CSat)

MPos = M$^{+}$(Gw)

Sales = M$^{+}$(MPos)

Revenue = M$^{+}$(Sales)

NetIncome = M$^{+}$(Revenue)

end
</div>

which differs from $M_{3}$ by using another organizational variable, goodwill, for describing the relationship between customer satisfaction and market position.

To complete the model specification, we still need to provide an initial state of the system, that is, we need to specify that price is initially increasing, and we need to specify the current, qualitative values of the other involved variables. While the initial state value of price could be derived from the query, we would obtain the other values from an organizational database. Which details remain to complete the scenario model specification depends upon the solver selection. In our example, we have used a QSIM type of language to represent qualitative relationships. If we chose QSIM as the solver of the scenario model, we would already have a complete constraints specification for a QSIM model, although we would still need to include the initial state specification, as well as the appropriate quantity space definitions. All this extra information required for completing the specification of particular scenario models could be kept in the fragment definitions. However, conceptually we prefer a solution where this information is maintained separately because it is context independent and can be reused in different settings and scenarios. Thus, we suggest to create a database as a part of the model knowledge base where we store and maintain information like current values of system variables, possible quantity space definitions, and quiddity information, that is information about the intended interpretation of the variables. Bhargava et al. [9] suggest a representation of quiddity information, and also discuss the more practical yet very difficult problems of possible variable name violations along with the problems of dealing with variables expressed in different dimensions and measurement units.

The integration of the relationships in the above example scenario model was relatively straightforward. Because we have used only one qualitative representation language in our illustration, and the query indicated a qualitative scenario model, we could simply merge the relations sections of the involved model fragment. In a situation like this, all we have to worry about is checking the composite model for possible inconsistencies among the constraints and the possible removal of redundant constraints. Fortunately, both tasks could be left to the solver which, presumably, would not be affected (much) by redundant constraints and which would detect inconsistent constraints by failing to solve the model. Models that are over-constrained and have no solution can be interpreted as spurious model candidates that were not pruned out at an earlier stage, and can simply be removed from further consideration.

The greater the diversity of the modeling languages is, which we allow for specifying relationships, the more expressive the entire model knowledge base becomes. The task of integrating model fragments, on the other hand, gets more complicated as the heterogeneity of the model knowledge base increases. Since in our model integration approach we are favoring the merging of model components, like in compositional modeling, over communicating messages between model components, the issue of compatibility becomes more severe. We need to carefully check the compatibility of different model fragments before we actually attempt to convert and merge the relationships into a new, composite model. We suggest a model transformation mechanism based on qualitative abstraction. The basic idea of qualitative abstraction is that we can take two (or more) models, identify the one with the highest abstraction level, and then abstract the other one to this higher level. To illustrate this method, let us suppose that we need to integrate the two models

M1: SALES

$$
= [ 6 8 0 0 0, 9 2 0 0 0 ] + [ 4 0 0 0 0, 4 8 0 0 0 ] \times \text { PRICE }
$$

and

$$
\mathrm{M} 2: \text { PRICE } = 1. 1 + 3 3 4 0 6 5 3 / \text { SALES }
$$

Now, we see that model M2 is a precisely stated quantitative model and that model M1 is a semi-qualitative model formulation. Hence, we identify model M1 as the one with the highest abstraction level among the participating models and select its representation language as the target language of the composite model, say model M3. In this example, we would transform model M2 into an equivalent formulation, model M2', using the semi-qualitative target language, which, in this case, resembles the RCR language; cf. Ref. [32]. Thus, we get

M2': PRICE

$$
= [ 1. 1, 1. 1 ] + [ 3 3 4 0 6 5 3, 3 3 4 0 6 5 3 ] / \text { SALES }
$$

where PRICE and SALES are now treated as interval-valued variables. Model integration is achieved by merging models M1 and M2' into a new model

M3: SALES

$$
\begin{array}{r l} & = [ 6 8 0 0 0, 9 2 0 0 0 ] + [ 4 0 0 0 0, 4 8 0 0 0 ] ^ {*} \text {PRICE} \\ & \text {PRICE} = [ 1. 1, 1. 1 ] + [ 3 3 4 0 6 5 3, 3 3 4 0 6 5 3 ] / \text {SALES}. \end{array}
$$

The usage of interval representations as sort of a super language which can subsume quantitative and qualitative relationships bears some resemblance to an embedding language of the kind presented in Ref. [8]. Obviously, this technique has its limitations, and we cannot expect to merge any arbitrary combination of language representations, nor can we expect to retain all information when we perform the conversion through an abstraction mechanism. For example, it would be hard to integrate a SAS model with a linear program formulation in GAMS. A rule base which would determine an embedding language for a given model combination, and which would infer incompatible combinations of language representation could be used to prevent us from attempting to merge incompatible model fragments.

A related issue is the one of trying to combine a static and a dynamic model formulation. This could be ruled out by simply using the information that the two fragments are conditioned on different modeling assumptions, namely, the operating assumptions $OpAss = (\text{quasi-static})$ vs. $OpAss = (\text{dynamic})$ . Attempting to reformulate dynamic models as a static ones might be inappropriate in many cases, but, on the other hand, generalizing a static model into a dynamic model can be a reasonable thing to do. For example, model

$$
\begin{array}{r l} \text {M1: SALES} & \\ = [ 6 8 0 0 0, 9 2 0 0 0 ] + [ 4 0 0 0 0, 4 8 0 0 0 ] \times \text {PRICE} \end{array}
$$

which is a static one, that is one which applies at any time, could be generalized, and reformulated as

$$
\begin{array}{r l} \mathrm {M1^ {\prime} : SALES(t)} \\ & = [ 6 8 0 0 0, 9 2 0 0 0 ] + [ 4 0 0 0 0, 4 8 0 0 0 ] \times \mathrm{PRICE(t)} \end{array}
$$

In absence of a better, more accurate dynamic model in the model base, model M1' could serve as a valuable piece in a dynamic scenario model which needs to have sales included as a quantity of interest.

## 6. Open research and implementational issues

This section reports first on a prototype implementation of our enterprise modeling framework, and then highlights open research issues and outlines a research agenda.

## 6.1. Implementational issues

We have implemented a partial prototype system based on the architectural framework that we propose in this paper. The implementation is currently limited to those features of our framework that have primarily been discussed in this paper, namely the organizational knowledge base, and model management and model generation.

Acknowledging the fact that information generated in a company is dispersed, we have chosen a distributed environment, the World Wide Web, for our implementation. Note that using the Web as the implementation platform is fine for the illustrative purposes of this paper. However, in a real-world application one would move the system to an Intranet environment to ensure data security. The most important reason of using the Web as the implementation platform is its capability for seamless information sharing and information integration.

The idea of a centralized knowledge base that keeps every piece of information generated in the company in one place is simply not practical. Therefore, the organizational knowledge base is a decentralized one with each department maintaining their own department specific knowledge. For example, the accounting department maintains its own server containing information that is related to accounting, such as annual reports, balance sheets, cash flow statements, basic accounting models, etc. The manufacturing department, on the other hand, will keep on their server the inventory data, scheduling models, etc. Therefore, the implementation is based on a client-broker-server structure (see Fig. 5) wherein the broker assumes the role of the model manager and is also responsible for coordination tasks among Web clients. Each client, which could be a PC, a Mac, or a UNIX machine, is a Web client that has a Web browser (e.g., Mosaic, Netscape). The servers are Web servers that are maintained by different functional departments in a company.

![](/api/attachments/64AUZY2R/fulltext/images/1e9e89537f3ed8991c81c224c9dab764e44a3eafc1b541081a4b22f69a0b65de.jpg)  
Fig. 5. The client-broker-server architecture.

The broker serves as the intermediary between end-users and information that is scattered on different departmental servers. The broker is maintained by the MIS department in the company. Note that even though our knowledge base is decentralized, we still have a centralized broker maintaining the interaction graph, as a function of the MIS department [3]. The interaction graph plays the role of a metadirectory, it contains information on what is available in the knowledge base, how model fragments are related to each other, and where each model fragment resides. Each time a model fragment is added to the knowledge base, the interaction graph needs to be updated: The updating of the interaction graph takes place via the broker, which means that each time a model fragment is added to the knowledge base on a departmental server, the broker needs to be notified and the corresponding node needs to be added to the graph with the URL $^{9}$ address of the model fragment.

To be more specific, we use HTML forms (Fig. 6) to initiate queries and to enter information to the organizational knowledge base. The forms are processed by scripts written in Perl $^{10}$ , a scripting language. At this point, the query format is rather restrictive and only a certain query form is accepted from the user.

To enter model fragments to the knowledge base, each department uses the form as depicted in Fig. 7.

Then the form is processed by a Perl script and translated to an SGML $^{11}$ document. The SGML document would be stored on the departmental server as one entry in the knowledge base. The interaction graph is represented as one SGML document with nodes marked up. The form used by the broker to update the interaction graph takes the information as shown in Fig. 8.

The information entered into this form will be

![](/api/attachments/64AUZY2R/fulltext/images/8589315327e8a4f777ed5a436f008bbf5a89cca267391fb0c8c50308f10c56d2.jpg)  
Fig. 6. The query form.

processed by another Perl script and marked as one entry in the SGML document.

There are several kinds of scripts

1. a script running on each departmental server (remote servers) that takes the information in the fragment form and enters the information to the knowledge base

2. a script running on the broker that takes information in the interaction graph form and adds the information to the interaction graph

3. a script on the broker that analyzes the query from user, goes through the interaction graph, and collects all consistent paths

4. a script that analyzes the paths from (2), gets all

model fragments necessary from remote servers, computes the model size based on the evaluation scheme, and displays results to user In script 3 we have used the following traversal algorithm for searching the interaction graph.

```vhdl
Procedure Interaction_graph_search (START_NODE, END_NODE);
Begin
    COMPLETE_PATH := []; PATH := []; LASTPATH := null;
    END := FALSE; CURRENT_NODE := START_NODE; %initialize
    Recurse
    If CURRENT_NODE = END_NODE
    Then
    add PATH to COMPLETE_PATH;
    END := TRUE;
    Else
    push LASTPATH to PATH stack;
Loop:
    Begin
    If (there are more paths and END is FALSE)
    Then
    CURRENT_NODE := next node;
    call Recurse;
    Else
    END := FALSE;
    End;
    Remove last item from PATH stack;
End;
```

When a user initiates a query from a client machine, the query will be sent to the broker. Then the script running on the broker (script 3) searches the interaction graph and finds all the consistent paths, which are the consistent model candidates. Returned along with each model candidate is a ranking value (measuring model complexity) which is computed using the candidate evaluation function. A list, ordered according to the complexity of the model candidates, is presented to the end-user who can then choose which of the suggested models are to be executed (see Fig. 9). For a detailed discussion of the implementation and the client–broker–server structure on which the implementation is based, see Ref. [2].

## 6.2. Open research problems and possible future research directions

The success of compositional modeling depends heavily on a clear organization of the domain theory. We still need a better understanding of how to decompose an organizational environment into semi-independent components in a manner which really reflects how different parts of the organization work together to accomplish common corporate goals. More research needs to be done to develop comprehensive taxonomies and ontologies which are necessary as a basis for the formulation of organizational descriptions which can be truly considered as interpretable knowledge units that can be used to synthesize new, higher-level knowledge. A more finely grained representation of modeling assumptions is necessary if we want to improve the focus in searching the interaction graph for relevant model fragments and thereby reduce the level of ambiguity in the model building process. Recalling, from Section 5, our small example that yielded four model candidates, one may argue that it would be desirable to discriminate between the first two models which represent a more accounting-oriented view and the other two which represent a more organizational behavior kind of view on the effect of a price change to net income. Since our explicitly represented modeling assumptions prescribed to consider just qualitative influences we could not distinguish between more specific perspectives like an accounting-oriented or an organizational-behavior-oriented view in the model composition phase. This situation could be exacerbated when dealing with more complicated examples. Work in organizational behavior and management, such as Refs. [49,35], could help to structure organizational knowledge more systematically.

Another important and difficult issue is the reasoning with modeling assumptions and deriving internally consistent and coherent composite models when integrating model fragments from the organizational knowledge base. Merely using first-order logic statements to specify modeling assumptions, as we have done in this paper, presents a limitation to model coherency reasoning. More versatile approaches to manipulate sets of modeling assumptions could be based on the application of assumption-based truth maintenance systems $[18]$ or explanatory coherence networks $[53]$ .

In our enterprise modeling approach we have limited model integration to combining model fragments into candidate models, but do not attempt to integrate model candidates into higher-level hypermodels. Taking our example again, one may wish to combine scenario model $M_{1}$ and $M_{2}$ and construct a higher-level model $M_{12}$ that includes both effects of a price increase, $\text{Revenue} = \text{M}^{+}(\text{Price})$ and $\text{Revenue} = \text{M}^{+}(\text{Sales}(\text{M}^{-}(\text{Price}))$ . This approach would reduce the ambiguity at the level of generating the set

of model candidates by combining ambiguous descriptions into one model candidate, but would not necessarily reduce the level of ambiguity in the model prediction. Solving model $M_{12}$ would still yield the ambiguous prediction that a price increase could lead to either increased revenues or decreased revenues due to drop in sales. Furthermore, since we are using QSIM as the modeling language in $M_{1}$ and $M_{2}$ we would generate $M_{12}$ as a QSIM model also. Unfortunately, the QSIM solver treats conflicting relationships like the two revenue-price relationships above as contradictions, and would reject the $M_{12}$ as infeasible. However, our enterprise modeling approach could be extended to include this kind of

![](/api/attachments/64AUZY2R/fulltext/images/2901e651fa04219f3e2bea37e997196034f5914ea4605b9ba382a962a158ca4e.jpg)  
Fig. 7. The HTML form for entering document fragment to the knowledge base.

![](/api/attachments/64AUZY2R/fulltext/images/5f1d424027f223c7fa4f22223b7f33233e407cf3d6f3a030632f21e3ccf47904.jpg)  
Fig. 8. The HTML form for entering information to the interaction graph.

model integration across model candidates if we choose a different modeling language. QPT, a qualitative modeling language proposed in Ref. [25] is, for example, a language that does allow the formulation of models that contain relationships with opposite influences.

In this paper, we have used a rather small example of an organizational knowledge base to demonstrate how our enterprise modeling framework could be implemented. A natural question that arises is how does this approach scale up to real-world applications? A large-scale implementation would certainly require a lot more work and also reveal technical problems that could be neglected in this initial paper. Especially updating the organizational knowledge base could become a difficult problem. Modifying and adding model fragments and organizational variables to the interaction graph is a task that requires careful coordination. Data access and data security issues are also severe concerns in large-scale practical applications. Some other issues that need to be worked out carefully in distributed computing environments include solver integration, integration with existing data resources and semantic unification. For example, developing semantically consistent name spaces for named objects and providing conversion routines for integrating models that are expressed in different monetary units are topics that have not really been addressed in this paper. On the other hand, recent research suggests that it may not be necessary to develop large-scale organizational knowledge bases in order to make enterprise model-

## Results:

![](/api/attachments/64AUZY2R/fulltext/images/1caffe12b2a9f9adda320518d89caaa3dcf4ed632cedace55bbc42aecee1d599.jpg)  
Fig. 9. The candidate models.

ing a useful tool for decision support. Ref. [14] reports on a collaborative project with a company in the forest industry in which they have implemented a DSS for strategic management that is based on cognitive maps, a graph structure similar to our interaction graph. Their system does not build models from the cognitive map but only propagates qualitatively specified impacts and effects of organizational variables. The company was very impressed with their results, although only a few dozen organizational variables were used in the implementation. This indicates, that an enterprise modeling system may need only a moderately sized organizational knowledge base in order to work successfully in practice.

One issue that has not really been touched on in the DSS area is the pricing issue. As network computing grows, more and more information will be available on networks such as the Internet. Companies need to get information from many sources available on-line, such as World Wide Web (WWW) or commercial electronic on-line database services, such as Dialog, InvestText, or Lexis/Nexis. However, there are economic issues involved in organizational problem solving, that is, there is a tradeoff between the cost of the information and the value the organization gains from it. Ref. [29] presents some initial work on different pricing mechanisms associated with the Internet.

## 7. Conclusion

As organizations trim down and become leaner and meaner, they try to improve quality and productivity by giving people more decision-making responsibilities, which means that an effective enterprise-wide decision support system could become very important for distributing and assembling the information people need to make vital decisions. In this paper, we have outlined a comprehensive framework for future intra-organizational information systems that integrate data warehousing, enterprise modeling, and decision support systems with existing Intranet technologies, which are aimed at providing fast cycle responses to organizational decision-making situations.

Enterprise computing is a way to achieve ultimate organizational goals. We believe that future research in knowledge management for decision support requires more attention to organizational knowledge representation and to related model building and model reasoning research in artificial intelligence. One purpose of this paper is to bring to bear some of the stimulating results obtained from the AI community, and to indicate how they can be incorporated into the DSS research on model building. Among the new features we have proposed, we want to highlight those which, in our mind, map out the most promising future research directions. First, the possibility of both qualitative and quantitative model formulations, which introduces a new level of versatility to organizational model building, and which should widen the scope of computer supported decision tools considerably. Second, the explicit representation of modeling assumptions. Third, the application of a compositional modeling strategy to automatically build task specific scenario models, which liberates users from having to specify special modules for controlling the modeling integration process. And finally, the WWW-based implementation strategy, which provides a standard user interface with seamless information sharing and integration.

## References

[1] S. Addanki, R. Cremonini, J.S. Penberthy, Graphs of models, Artificial Intelligence 51 (1991) 145–178.

[2] S. Ba, R. Kalakota, A.B. Whinston, A client–broker–server architecture for Intranet decision support, Decision Support Systems 19(3) (1997) 171–192.

[3] S. Ba, A.B. Whinston, Preparing your MIS Organization for Electronic Commerce, Working Paper, Center for Information Systems Management, The University of Texas at Austin, 1996.

[4] A. Balakrishnan, A.B. Whinston, Information issues in model specification, Information Systems Research 2 (4) (1991) 263–286.

[5] P. Balasubramanian, T. Isakowitz, H. Johar, E. Stohr, Hyper model management systems, in: Proceedings of the 25th Hawaii International Conference on System Sciences, 1992, pp. 462–472.

[6] A. Basu, R. Blanning, Model integration using metagraphs, Information Systems Research 5 (3) (1994) 195–218.

[7] T. Berners-Lee, R. Cailliau, A. Luotonen, H.F. Nielsen, A. Secret, The World Wide Web, Communications of the ACM 37 (8) (1994).

[8] H.K. Bhargava, S.O. Kimbrough, Model management: an embedded languages approach, Decision Support Systems (1993), submitted.

[9] H.K. Bhargava, S.O. Kimbrough, R. Krishnan, Unique names

violations, a problem for model integration or you say Tomato, I say Tamahto, ORSA Journal on Computing 3 (2) (1991) 107–120.

[10] R.W. Blanning, A relational theory of model management, in: C.W. Holsapple, A.B. Whinston (eds.), Decision Support Systems: Theory and Application, Springer Verlag, 1987.

[11] R.W. Blanning, Model management systems, in: R.H. Sprague, Jr., H.J. Watson (Eds.), Decision Support Systems: Putting Theory into Practice, Prentice Hall, NJ, 1989.

[12] R.W. Blanning, Model management systems: an overview, Decision Support Systems 9 (1) (1993) 9–18.

[13] R.H. Bonczek, C.W. Holsapple, A.B. Whinston, Foundations of Decision Support Systems, Academic Press, 1981.

[14] C. Carlsson, P. Walden, Cognitive Maps and a Hyperknowledge Support System in Strategic Management, Research Report 5/94, Institute for Advanced Management Systems Research, Abo Akademi University, Data City, Finland, 1994.

[15] G.M. Carter, M.P. Murray, R.G. Walker, W.E. Walker, Building Organizational Decision Support Systems, Academic Press, San Diego, CA, 1992.

[16] J.G. Cooprider, Partnership Between Line and I/S Managers: A Management Model, PhD Thesis, MIT Sloan School of Management, Cambridge, MA, 1990.

[17] R.S. Crouch, S.G. Pulman, Time and modality in a natural language interface to a planning system, Artificial Intelligence 63 (1/2) (1993) 265–304.

[18] J. de Kleer, An assumptions-based TMS, Artificial Intelligence 28 (1986) 127–162.

[19] J. Kleer, J.S. Brown, A qualitative physics based on confluences, Artificial Intelligence 24 (1984) 7–83.

[20] K. Doler, Database maker sorting out info on warehousing, Investor's Business Weekly (1996).

[21] D.R. Dolk, Model management and structured modeling: the role of an information resource dictionary system, Communications of the ACM 31 (6) (1988) 704–718.

[22] D.R. Dolk, J.E. Kottemann, Model integration and a theory of models, Decision Support Systems 9 (1) (1993) 51–63.

[23] J. Elam, B. Konsynski, Using artificial intelligence techniques to enhance the capabilities of model management systems, Decision Sciences 18 (1987) 487–502.

[24] B. Falkenhainer, K.D. Forbus. Compositional modeling: finding the right model for the job. Artificial Intelligence 51 (1991) 95–144.

[25] K.D. Forbus, Qualitative process theory. Artificial Intelligence 24 (1984) 85–168.

[26] A.M. Geoffrion, An introduction to structured modeling, Management Science 33 (5) (1987) 547–588.

[27] C. Goldfarb, in: Y. Rubinsky (Ed.), The SGML Handbook, Oxford University Press, 1990.

[28] S. Greengard, Using internal web sites to automate HR user friendly, Personnel Journal 74 (6) (1995) 161.

[29] A. Gupta, D. Stahl, A.B. Whinston, Managing the Internet as an Economic System, Working Paper, Center for Information Systems Management, The University of Texas at Austin, 1990.

[30] S.H. Haeckel, R.L. Nolan, Managing by wire, Harvard Business Review (1993) 122–132.

[31] W. Hamscher, M.Y. Kiang, K.R. Lang, Qualitative reasoning in business, finance, and economics: introduction, in: Qualitative Reasoning (special issue), Decision Support Systems 15 (2) (1995) 99–104.

[32] A. Hinkkanen, K.R. Lang, A.B. Whinston, On the usage of qualitative reasoning as approach towards enterprise modeling, Annals of Operations Research (1995).

[33] G.P. Huber, A theory of the effects of advanced information technologies on organizational design, intelligence, and decision making, Academy of Management Review 15 (1) (1990) 47–71.

[34] R. Kalakota, A.B. Whinston, Readings in Electronic Commerce, Addison-Wesley, Reading, MA, 1996.

[35] R.S. Kaplan, D.P. Norton, The balanced scorecard—measures that drive performance, Harvard Business Review 70(1) (1992) 71–79.

[36] R.S. Kaplan, D.P. Norton, Putting the balanced scorecard to work, Harvard Business Review (1993) 134–147.

[37] M.Y. Kiang, A. Hinkkanen, A.B. Whinston. Reasoning in qualitatively defined systems using interval-based difference equations, IEEE Transactions on Systems, Man and Cybernetic (1994), in press.

[38] B. Kuipers, Qualitative simulation, Artificial Intelligence 29 (1986) 289–338.

[39] B. Kuipers, Qualitative simulation using time-scale abstraction, Artificial Intelligence in Engineering 3 (4) (1988) 185–191.

[40] B. Kuipers, D. Berleant, A Smooth Integration of Incomplete Quantitative Knowledge into Qualitative Simulation, Tech. Report AI90-122, AI Laboratory, The University of Texas at Austin, 1990.

[41] M.L. Lenard, An object-oriented approach to model management, in: Proceedings of the Twenty-Second Annual Hawaii International Conference on Systems Sciences I, 1989, pp. 507–515.

[42] T. Liang, Development of a knowledge-based model management system, Operations Research 36(6)(1988) 849–863.

[43] M. Mannino, B.S. Greenberg, S.N. Hong, Model libraries: knowledge representation and reasoning. ORSA Journal on Computing 2 (3) (1990) 288–301.

[44] B. McWilliams, Easy money, tough decisions. Computer World (1996).

[45] P.R. Monge, Theoretical and analytical issues in studying organizational processes, Organization Science 1 (1990) 406–430.

[46] W.A. Muhanna, R.A. Pick, Meta-modeling concepts and tools for model management: a systems approach, Management Science (1992), submitted.

[47] P.P. Nayak, Causal approximations, Artificial Intelligence 70 (1994) 277–334.

[48] Netscape, Intranets Redefine Corporate Information Systems, Netscape Whitepaper (1996).

[49] J.D. Orton, K.E. Weick, Loosely coupled systems: a recon-ceptualization, Academy of Management Review 15 (2) (1990) 203–23.

[50] C. Petrie (Ed.), Enterprise integration modeling, in: Proceedings of the First International Conference, MIT Press, 1992.

[51] J. Rickel, B. Porter, Automated modeling for answering prediction questions: exploiting interaction paths, in: Proceedings of the Sixth International Workshop on Qualitative Reasoning, Edinburgh, Scotland, 1992, pp. 82–95.

[52] E.W. Stein, V. Zwass, Actualizing organizational memory with information systems, Information Systems Research 6(2) (1995) 85–117.

[53] P. Thagard, Adversarial problem solving: modeling an opponent using explanatory coherence, Cognitive Science 16 (1) (1992) 123–150.

[54] K.E. Weick, Theory construction as disciplined imagination, Academy of Management Review 14 (4) (1989) 516–32.

[55] K.E. Weick, K.H. Roberts, Collective mind in organizations: heedful interrelating on flight decks, Administrative Science Quarterly 38 (1993) 357–381.

[56] D.S. Weld, Reasoning about model accuracy, Artificial Intelligence 56 (1992) 255–300.

[57] B.C. Williams, A theory of interactions: unifying qualitative and quantitative algebraic reasoning, Artificial Intelligence 51 (1991) 39–94.

![](/api/attachments/64AUZY2R/fulltext/images/4725d39abe265a38224f28a1252d44c935d1d1f2e49dee553a726f6acaad1a4b.jpg)

Sulin Ba is an assistant professor of information systems at the University of Southern California. She received her Master's degree in Library and Information Sciences and her PhD in Management Information Systems from the University of Texas at Austin. Her current research interests include electronic commerce, knowledge management, distributed decision support systems, and the design of information systems organizations to manage internal commerce.

![](/api/attachments/64AUZY2R/fulltext/images/4c5bb55a7ca94798f20a3281136084ebb29fee086c73f70b778884a862dc463e.jpg)

![](/api/attachments/64AUZY2R/fulltext/images/34508871d08292dce81eeae0ed0e89c39484e221bd66b8dabf395ceff544ae71.jpg)

Andrew B. Whinston is a professor of information systems, computer science, and economics at the University of Texas at Austin. He also holds the Hugh Roy Cullen Centennial Chair in Business Administration. He received his PhD in management from Carnegie Mellon University in 1962. An author or co-author of over 250 papers and 16 books, his current research is concerned with the potential of prices in engineering an improvement in the performance of Internet.

Karl Reiner Lang is an Assistant Professor in Information Systems at the Hong Kong University of Science & Technology. He received his MBA from the Free University of Berlin, Germany, and holds a PhD from The University of Texas at Austin. Before joining HKUST he had been on the faculty of the Business School at the Free University of Berlin. His research interests include Qualitative Modeling and Reasoning, Decision Support Systems and Work-

flow Management Technologies. Dr. Lang's recent papers have appeared in journals such as Annals of Operations Research, Computational Economics, and Decision Support Systems.

---
otero_id: 15192
otero_key: "2DRSACWE"
title: "A framework for model integration and holistic modelling of socio-technical systems"
authors: "Paul Pao-Yen Wu; Clinton Fookes; Jegar Pitchforth; Kerrie Mengersen"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.01.006"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A framework for model integration and holistic modelling of socio-technical systems

Paul Pao-Yen Wu ⁎, Clinton Fookes <sup>1</sup>, Jegar Pitchforth <sup>1</sup>, Kerrie Mengersen <sup>1</sup>

Queensland University of Technology, Mathematical Sciences School, 2 George Street, Brisbane, Australia

## a r t i c l e i n f o

Article history: Received 9 March 2014 Received in revised form 5 January 2015 Accepted 8 January 2015 Available online 21 January 2015

Keywords: Socio-technical systems (STS) Modelling Agent Based Model Bayesian Network Business Process Modelling Notation

## a b s t r a c t

This paper presents a lavered framework for the purposes of integrating different socio-technical systems (STS models and perspectives into a whole-of-systems model. Holistic modelling plays a critical role in the engineering of STS due to the interplay between social and technical elements within these systems and resulting emergent behaviour. The framework decomposes STS models into components, where each component is either a static obiect. dynamic object or behavioural object. Based on existing literature, a classi<sup>fi</sup>cation of the different elements that make up STS, whether it be a social, technical or a natural environment element, is developed; each object can in turn be classi<sup>fi</sup>ed according to the STS elements it represents. Using the proposed framework, it is possible to systematically decompose models to an extent such that points of interface can be identi<sup>fi</sup>ed and the contextual factors required in transforming the component of one model to interface into another are obtained Using an airport inbound passenger facilitation process as a case study socio-technical system, three different models are analysed: a Business Process Modelling Notation (BPMN) model, Hybrid Queue-based Bayesian Network (HQBN) model and an Agent Based Model (ABM). It is found that the framework enables the modeller to identify non-trivial interface points such as between the spatial interactions of an ABM and the causal reasoning of a HQBN, and between the process activity representation of a BPMN and simulated behavioural performance in a HQBN. Such a framework is a necessary enabler in order to integrate different modelling approaches in understanding and managing STS.

© 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

The task of modelling modern socio-technical systems (STS) such as transportation systems, organisational systems and energy infrastructure systems is challenging due to the complex nature of these systems. This complexity stems from the interactions and interdependencies between a diverse range of social, technical and contextual elements in and around the system [1,2]. However, modelling plays an essential role in STS engineering and providing decision support as part of the design, operation and evolution of STS [3]. Even though individual models of STS and specific STS elements are well developed, integration of the different perspectives in a holistic model is a signi<sup>fi</sup>cant research challenge [2,4–6]. Speci<sup>fi</sup>cally, an understanding of the relationships between different STS elements and how they can be captured by different modelling methodologies is essential to the development and application of holistic models that capture the different perspectives, interdependencies and ultimately the emergent behaviour of STS. Understanding emergent behaviour is integral for decision makers in the STS context.

One of the dif<sup>fi</sup>culties of STS modelling lies in the interdisciplinary nature of STS and the lack of consensus on issues such as the de<sup>fi</sup>nition of STS across the different <sup>fi</sup>elds [3,7]. First coined by Emery in 1960 [8], STS are characterised by a high degree of technical complexity, social intricacy, and elaborate processes, aimed at ful<sup>fi</sup>lling important functions in society [9]. The interaction and interdependency between social and technical systems on a large scale are a discerning feature of STS [9,1,10]. Also referred to in some <sup>fi</sup>elds as engineering systems [9] or Complex Largescale Integrated Open Systems (CLIOS) [11], STS need actors and some social/institutional infrastructure to be in place in order to perform their function [12]. Critical infrastructures, such as the national electricity grid, oil and gas systems, telecommunication and information networks, transportation networks, water, banking and <sup>fi</sup>nancial systems, agriculture and food systems, and public health networks, are examples of STS [2,12].

For many real world systems, it is necessary to adopt STS approaches rather than traditional systems engineering approaches due to the interplay between the social and technical elements. It is argued that due to the human dimension of STS, existing systems engineering approaches such as IEEE 1220/ISO 15,288 are inadequate for STS [12,13]. In traditional systems engineering, humans are represented exclusively as ful<sup>fi</sup>lling sub-functions and the social dimension (such as regulations, laws and procedures) is often ignored. A failure to incorporate social effects tends to result in unstable requirements, and poor systems design and user interfaces, thus incurring project delays and unmatched expectations [3,7]. It is argued that the human aspect is more expansive and complex than hard technologies and thus requires greater investment of time and resources in order to manage reliably (and have greater public trust) [10,14].

In addition, STS are not necessarily amenable to the reductionist approach of systems engineering due to the existence of complex relationships between system components and interdependencies [9]. Although the system can be viewed in terms of its constituent components, their interaction is non-linear, which undermines the ability to decompose the problem and specify requirements ahead of time as required in systems engineering [6]. Such non-linear interactions and dependencies lead to emergent behaviour, selforganisation, and adaptation (the system has memory) [6]. As a result, holistic modelling is necessary as modelling parts of the system in isolation is not only impractical, but often also irrational.

Modelling and simulation of STS, especially infrastructure systems, are essential to help enable stakeholders to: (i) <sup>fi</sup>nd downstream consequences of loss events and identify the risks and vulnerabilities, (ii) predict system behaviour for extreme and rare events, (iii) assist decision making and policy development, (iv) help develop, test and validate infrastructure protection strategies, (v) perform what-if analysis, and (vi) support training via modelling and simulation [15].

However, the task of modelling STS is challenging due to the complex nature of the problem domain. There are many different dimensions to STS such as economic, legal and regulatory, technical, security and social dimensions [2]. De Rosa [6] argues, based on Ashby's law of requisite variety [16] and Bar Yam's mathematical proof [17], that the complexity of the STS requires a corresponding level of complexity in the approach and hence in the model. Therefore, it is necessary to integrate different models to capture STS as a whole. Although existing models of individual elements of STS exist, integration of these models to obtain a whole-of-system perspective is in itself challenging as it is not possible to hook-together different models [2]. In order to meet the requirements for STS engineering, it is necessary to have a holistic model that captures whole-of-system effects, and especially system interdependencies [15]. Adapting and integrating one or more existing methods to develop a holistic model is a current research challenge [3].

This paper presents a framework that categorises the different elements of STS and provides a method for drawing relationships between them to enable holistic modelling. Using the framework, a case study is developed for an airport passenger terminal socio-technical system that evaluates and integrates three different models into a holistic model. The passenger facilitation process is particularly representative of STS due to the diversity of stakeholders involved in a process with regulatory, security, business economic and time based operational constraints and objectives [18]. Such a model is integral in understanding emergent airport behaviours and whole-of-system performance as part of the design, development and operation of the airport system.

## 2. Background: socio-technical systems

Despite the prevalence of STS in the real world, the application of STS methodologies such as STS design (STSD) or STS engineering (STSE) is rare; instead, systems engineering methods are still the predominant approach [3,6]. Part of this can be attributed to the fundamental paradigm shift required as the system cannot be centrally designed, made and controlled [10,9]. Instead, the development of STS and the implementation of changes are enacted by actors within the STS [7]. In addition, STS are inter-disciplinary by nature and there has been very little cross-fertilisation across research <sup>fi</sup>elds to date [3]. Furthermore, the tools for STSE are not well developed and there is little agreement on methods for STSE [6]. It can be seen that the development of models of STS is not only an integral part of STS engineering and decision making [3], but also in the study of such complex systems.

This section brie<sup>fl</sup>y reviews the STS literature with regard to current high-level approaches to modelling, and the need for a framework to enable holistic STS modelling and model integration.

## 2.1. Modelling approaches

There are two main approaches to STS modelling especially for infrastructure: an integrated model that covers every element in one framework, or a coupled model where a series of individual models are joined together [4]. Typically, integrated models tend to be high level models and coupled models tend to provide greater <sup>fi</sup>delity [4]. The challenge with the coupled approach, however, lies in the need to interface between different models which may have different assumptions, data requirements, and other characteristics (such as the scale of the model) [2]. A structured framework that identi<sup>fi</sup>es the different elements of STS and their relationships is essential to enable the integration of different modelling methods. Such a structure is also applicable to support the development of a single integrated model as it provides reference guidelines regarding the dimensions and elements of complex STS. The proposed framework helps to address this need.

In recent times, there has been a trend towards data-driven computational models of STS that enable the simulation of STS processes [19]. Examples of these approaches include discrete event simulation [20,21], Agent Based Modelling (ABM) [22,23] and network models [24,19]; however, de Weck et al. [9] argue that much more research is required in order to address the challenges of holistic STS behaviour [9]. In general, it is infeasible to obtain an analytic expression of dynamic STS behaviour, even for simple systems, hence the trend towards computational models [19].

Such dynamical models of STS have been applied in social sciences and infrastructure modelling to explore and predict the emergence of whole-of-system (macro level) collective behaviour as a function of processes at the individual (micro) level and especially of individual humans. There are two major approaches for modelling human agents [10]. One is to assign behavioural rules at an agent level and simulate system behaviour via scenarios, context, roles and the like as used in sociology and social psychology. The other approach, popular in economics, is to assume rational agents who always choose the action to maximise the expected outcome at every time step.

Rinaldi [15] classi<sup>fi</sup>es existing STS infrastructure interdependency models into six categories: (i) aggregate supply and demand tools, (ii) dynamic simulations (e.g. system dynamics), (iii) ABM, (iv) physics based models (e.g. power <sup>fl</sup>ow analysis on electricity), (v) population mobility models (movement of entities through urban regions), and (vi) Leontief Input–Output Models (economic <sup>fl</sup>ows). Pederson et al. [4] concur and add additional categories for models based on game theory, mathematical models, and models based on risk. A comprehensive review by [25] poses a simpler classi<sup>fi</sup>cation structure relating modelling methods with usage scenarios as shown in Fig. 1.

Another key thrust of research is the development of diagrammatic models to represent STS dependencies and processes. A dependency matrix or equivalent graph, where directed edges connect dependent subsystems, is a method that has been applied in the analysis of interdependencies of critical infrastructure [4]. Uni<sup>fi</sup>ed Modelling Language (UML) diagrams are another popular approach in the study of STS and especially organisational STS as they provide a graphical depiction of system relationships and processes with respect to function [3,9]. Herrmann et al. [5] present an approach based on UML for the study and optimisation of business processes.

Regardless of the approach adopted for modelling, it is necessary to capture the uncertainty inherent in the system. Herrmann and Loser [26] provide one approach to classifying uncertainty based on whether it is deliberately introduced by the modeller (e.g. through abstraction), through vagueness (potential inaccuracy and/or incompleteness), and omission (unrecognised unknowns). This uncertainty can be represented qualitatively on a diagram (see [26]), or quanti<sup>fi</sup>ed as part of an analytic or simulation model (see [19]).

![](/api/attachments/2DRSACWE/fulltext/images/87cbf68c55c24989bb6b97b2d8387db1eb9ad82d28a6fa666bb103f052c4e159.jpg)  
Fig. 1. Classi<sup>fi</sup>cation of existing infrastructure STS modelling approaches [25].

Even though existing approaches to modelling are well developed in themselves, there remain a number of challenges to holistic STS modelling; these are discussed in the next section.

## 2.2. Model integration and the need for a holistic STS framework

Existing forays into STS modelling in disciplines ranging from epidemiology through software design have identi<sup>fi</sup>ed a number of challenges to holistic modelling. It has been shown that existing models have limited ability to represent multiple attributes (or criteria), different perspectives and systematically represent meta-criteria [26,5]. The capture of multiple perspectives and especially the social dimension under uncertainty (‘vagueness’) and ‘free’ human decision making is a current research challenge [5]. Recent works, such as [27,28], recognise the unique needs of STS and study the application of multi-objective (or multi-criteria) models to support decision making for STS. Both [25] and [3] also corroborate this challenge of holistic modelling with multiple objectives.

One approach to addressing the challenges of modelling STS is to combine existing individual models of different parts and/or perspectives of STS into a holistic model [15,4]. The advantage of such an approach lies in the ability to exploit a dearth of existing modelling techniques with well-established theories and rich practical experience, and that are familiar to practitioners.

Even though models of individual perspectives may be well developed within each discipline, integrating them into a holistic STS model is non-trivial due to unique assumptions, data requirements and numerical requirements (e.g. time-step size, scaling limitations) of each model [2]. Additionally, there may be a non-negligible number of operational scenarios where emergence of unintended consequences challenge the underlying formulation of the model [9,2]. Unsurprisingly, an evaluation of how existing modelling techniques can be adapted to model STS is cited to be one of the key research challenges moving forward [3,4]. There is a strong need for an understanding of what is relevant and what is super<sup>fl</sup>uous in the description and analysis of STS [19]. A framework for developing the relationships between STS elements and perspectives, and modelling methods can serve as a crucial enabler towards holistic STS modelling and understanding.

Satumtira and Duenas-Osorio [25] propose a hierarchical ‘model’ (effectively a meta-model) of existing literature on critical infrastructure (a prime example of STS) interdependency modelling. This work can be viewed as a <sup>fi</sup>rst step towards the development of a STS modelling framework and informing model integration as described above. Although an extensive discussion is provided on the capabilities of reviewed models and the models are further categorised with respect to usage scenarios, this work [25] does not take the next required step in establishing links between how the methods relate to STS elements, and thus how different models can be integrated in a holistic, system of systems model like that described by [15,4].

It can be seen that, even at a high level, there are different modelling approaches that provide a means to capture different aspects of STS such as the structure, the relationships, processes and emergent behaviour. Integrating these approaches into a holistic model requires a structured framework for determining interface points. Although there is signi<sup>fi</sup>cant literature on model integration and meta-modelling in the <sup>fi</sup>eld of software systems as part of model driven engineering [29], these works are focused on language based models and do not cover the breadth of mathematical, simulation and other models found in STS. However, the seminal work of Dolk and Kottemann [30] provides valuable insights into model integration in general.

Dolk and Kottemann [30] af<sup>fi</sup>rm the need for holistic modelling and discuss two main aspects to model integration, de<sup>fi</sup>nitional and procedural. The former is concerned with linking similar model representations in building a uni<sup>fi</sup>ed model, and the latter is about linking processes to form operators on the integrated representation. They advocate the use of graph based representations of models as the basis for identifying commonalities for integration. However, when dealing with complex STS, decomposition of models into such a form is non-trivial; this is discussed further in Section 3.1. In addition, integration of heterogeneous models (e.g. business process and statistical models) is substantially more complex than for homogeneous models (e.g. process models of different parts of the system). Dolk and Kottemann suggest a process based approach for heterogeneous models where the integrated result is obtained through the scheduled execution of solvers for the constituent models. These concepts form the groundwork for the proposed STS framework.

Although general concepts for meta-modelling for model integration have been developed [25,30], the complexities of STS require STS speci<sup>fi</sup>c frameworks for model integration. Such frameworks need to systematically guide users in building representations of STS models from which links for integration can be made [30]. Note that the focus here is on STS modelling and not the overarching STS design [3] or STS engineering processes such as that described by [9] or the CLIOS process [11,31,32]. The requirements for a STS modelling framework are discussed in the following section.

## 3. The STS modelling framework

The development of holistic STS models requires a structured approach for capturing the different elements of STS and their relationships. This section reviews the literature to identify the key elements and dimensions (or perspectives) of STS, and develops from that the proposed framework.

## 3.1. STS elements

The task of identifying the major elements of STS is challenging due to the diversity in STS and their operation. By de<sup>fi</sup>nition, it is argued that there is both a human and technical element and that STS must be situated in the real world [1,9]. This implies that there is a physical world element; even the Internet, which is predicated on virtual interactions, is based on physical routers and cables. At this high level, Ottens, Franssen et al. [12] argue that there are three types of elements: (i) technical (hardware and software), actors (individual human beings, organisations), and social elements (e.g. <sup>fi</sup>nancial, organisational structure, policy, laws and regulations). Hughes [33] on the other hand suggests that STS are made up of: (i) physical artefacts, (ii) organisations, (iii) scienti<sup>fi</sup>c components (i.e. technical elements), (iv) legislative artefacts and (v) natural resources.

Already, it can be seen that not only are there differences in the approach, but also incongruity in the vocabulary re<sup>fl</sup>ecting the interdisciplinary nature of STS. For the purposes of this discussion, the term element is used to denote “a particular part of something (such as a situation or activity)” [34] where the something is the socio-technical system, as used by [2,12].

In light of the diversity of views on STS, the objective of this section is to identify and develop a uni<sup>fi</sup>ed structure of the main elements of STS from the literature. Such an approach leverages off of extensive studies on STS from a wide variety of STS <sup>fi</sup>elds including infrastructure systems (e.g. transport, <sup>fi</sup>nancial, energy, communications/Internet), organisational and business systems, and engineering systems. A hierarchical structure is proposed that combines the elements and structures (both hierarchical and categorical) in the literature [12,2,33,27]. Such a structure is intended as a means of bringing together the disparate views in the literature and to also enable the evaluation of models at different levels of detail. Although it is possible to propose arbitrary elements in arbitrary structures, the elements and structure of the proposed framework is built on existing literature as it re<sup>fl</sup>ects both theories and real world studies on STS.

At a high level, both Ottens, Franssen, et al. [12] and Hughes [33] share the same insights into STS — the difference primarily stems from the different hierarchical classi<sup>fi</sup>cation structures that are employed. Ottens, Franssen et al. [12] break down the social element into <sup>fi</sup>nancial, organisational structure and regulatory/legislative subelements, whereas Hughes [33] lists legislative as a stand-alone element. Rinaldi, Peerenboom et al. [2] offer an alternate description of STS elements for critical infrastructure based on: (i) economic and business opportunities and concerns, (ii) public policy (non-regulatory), (iii) government investment decisions, (iv) legal and regulatory concerns, (v) technical and security issues, and (vi) social and political concerns. Note that the structure provided by Rinaldi, Peerenboom et al. [2] is much more speci<sup>fi</sup>c, however, elements (i) through (iv) and (vi) are essentially an expansion of the social element of [12] with particular emphasis on policy, regulatory and even political elements.

Another source of insight into STS elements is the literature on critical infrastructure interdependencies. Rinaldi, Peerenboom et al. [2] de-<sup>fi</sup>ne four classes of interdependencies, corresponding to four different types of elements, namely: physical, cyber (or informational), geographic (or environmental) and logical (policy, legal or regulatory). Subsequent expansion of these four classes is provided in Ref. [15] to include the time and space elements, social/psychological elements, operational procedures, business policies, restoration and recovery procedures, government regulatory/legal/policy element, and stakeholder element. Dudenhoeffer and Permann [35] provide a similar decomposition with regard to physical, informational, geospatial, policy/ procedural and societal (including sub-elements such as public opinion, public con<sup>fi</sup>dence, fear and cultural issues).

The modelling of STS needs to account for not only sociological effects, but also communication patterns and technologies [36]. Communication can be affected by such sub-elements relating to interdependencies between persons as communication and cooperation structures, organisational structures, personal expectations, interests and quali<sup>fi</sup>cations [26]. Gregoriades and Sutcliffe [27] go further to develop <sup>fi</sup>ve categories of elements that in<sup>fl</sup>uence human performance, namely:

• technology (usability, reliability, functionality, maintenance and machine performance),

• environment (noise, lighting, comfort etc.)

• organisation (management practices, culture),

• task (complexity) and

• agent (inherent ability, training, experience).

One aspect that is rarely discussed explicitly in the literature is the environment. STS do not operate in isolation. There is a general recognition of the role of the regulatory and political environment [12], physical environment [15], resources [33] and even the built environment [27]. Unlike the case for systems engineering where it is possible to draw clear boundaries and assume a closed system, the interactions with a changing environment are an integral part of STS operations [6]. It is instructive to note the relatively scarce mention of the natural environment and associated events; natural disasters are discussed in the context of failures in [2] for instance. Despite comparatively little literature on this aspect, the environment is a crucial element that needs to be included within any STS modelling framework.

In light of the above <sup>fi</sup>ndings, a hierarchy of STS elements is synthesised and shown in Fig. 2. Based on the de<sup>fi</sup>nition of an element as ‘a part of something’, the hierarchy is de<sup>fi</sup>ned such that elements that are linked to an element at a higher level are all subsets of that element. For example, social, technical and natural environment elements are all subsets of the physical world element; similarly, human beings, regulatory and economic elements and so on are subsets of the social element. Note that this hierarchy is proposed as a guideline based on high impact literature relating to STS and is not intended to be de<sup>fi</sup>nitive due to the sheer breadth of STS modelling scenarios. Also, it should not be confused with STS architecture (for example, refer to [32]).

The proposed hierarchy uses the physical world element as the root node as all STS must have a physical presence in the real world [9]. Following on from this root, there are the social, technical and natural environment elements. Although the natural environment has not been explicitly listed as a key element in the existing work (unlike social and technical elements), the literature does explicate elements of the natural environment such as natural resources and geographic elements. Within the social element, there are human being, organisational, economic, policy, regulatory, social psychological and other elements. The technical sub-elements include hardware, information and software, security and the built environment. It is useful to explicitly represent the built environment sub-element especially for infrastructure STS given the implicit inclusion of this element in the literature (see e.g. [2]).

Note that tasks as de<sup>fi</sup>ned by Ref. [27] are an actualisation of operational policy and procedures in Fig. 2. Also, note that the government in Ref. [2] can itself be represented as an organisation; however, in terms of the effects of government, such effects are typically represented by policies, regulatory and political measures (in blue in Fig. 2). Additionally, the elements of noise, lighting and comfort as de<sup>fi</sup>ned by [27] refer to the built environment (e.g. of<sup>fi</sup>ce building) rather than the natural environment hence the addition of the built environment element (in red in Fig. 2). Note that location and navigation in the built environment has also been identi<sup>fi</sup>ed to be a challenge with complex built environments [37]. Finally, note that sub-elements in the hierarchy inherit the properties of parent elements. For example, a human beings element is in effect also a social element (immediate parent element), and also a physical world element (grandparent element).

![](/api/attachments/2DRSACWE/fulltext/images/d11f626c0d69e19b4479475849fcb9e50cad601e200a91dc9522edc58b1f2956.jpg)  
Fig. 2. Proposed STS element hierarchy, as developed from the literature. The physical socio-technical system is divided into three main elements — social (in blue), technical (in red) and the natural environment (in green). Each of these are in turn broken down into sub-elements. (For interpretation of the references to colour in this <sup>fi</sup>gure, the reader is referred to the web version of this article.

Such a proposed hierarchy provides a summary of STS elements as derived from the literature, and enables a concrete discussion about the relationships between STS elements and models. Note that the proposed hierarchy has a similar structure to many of the reviewed works (especially [12]). However, it is substantially different from the structure proposed by [9], which is made up of: living organisms (including humans), matter (including hardware and resources), energy (e.g. engines, generators i.e. technical hardware), information and money (i.e. <sup>fi</sup>nancial and economic). Nevertheless, all of the elements covered by Ref. [9] are also replicated in the proposed hierarchy.

## 3.2. Proposed framework

Using the STS elements as building blocks, it is possible to develop or characterise holistic STS models based on an abstraction layer concept which is illustrated in Fig. 3. Like the Open System Interconnect (OSI) model for network communications [39], the proposed framework is layered in that each higher layer logically wraps lower layers such that higher layers are abstracted from lower layers. The premise of the framework is that it provides a systematic method to represent the links between STS elements and modelling methods.

Consider the scenario where models M are to be integrated as per the proposed framework. Let the ith model M be made up of $n \geq 1$ unique components $c _ { i , j }$ such that $M _ { i } = c _ { i , 1 } \cup \ldots \cup c _ { i , n } .$ In this context, a model is de<sup>fi</sup>ned as ‘a simpli<sup>fi</sup>ed description, especially a mathematical one, of a system or process, to assist calculations and predictions’ [40] and a component is ‘one of the parts of something (such as a system) $\cdots ^ { \prime } \left[ 3 4 \right]$ where that something is the model. Note the difference between a component, used to refer to a part of a model, and element (as de<sup>fi</sup>ned in Section 3.1) which refers to a part of the actual socio-technical system.

Each component $c _ { i , j }$ is assigned to a layer in the proposed framework. In addition, each component can be classi<sup>fi</sup>ed as:

<table><tr><td rowspan="2">Layer 3</td><td rowspan="2">Behaviour Objects</td><td>Sub-layer 3.2</td><td>Performance</td></tr><tr><td>Sub-layer 3.1</td><td>Metrics</td></tr><tr><td rowspan="3">Layer 2</td><td rowspan="3">Dynamic Objects</td><td>Sub-layer 2.3</td><td>Processes</td></tr><tr><td>Sub-layer 2.2</td><td>Activities</td></tr><tr><td>Sub-layer 2.1</td><td>Events</td></tr><tr><td rowspan="2">Layer 1</td><td rowspan="2">Static Objects</td><td>Sub-layer 1.2</td><td>Object Relationships</td></tr><tr><td>Sub-layer 1.1</td><td>Object Definitions</td></tr></table>

Fig, 3. Three laver framework for viewing socio-technical systems where higher lavers logically wrap lower lavers (e,g, dynamic obiects describe the time-varving behaviour of static ob. jects). Each layer can be divided into sub-layers to more precisely classify a component; for instance, events are useful for characterising system state transitions whilst activities, which logically wrap events are useful for describing system evolution over time [38]

• a model input (I),

• output (O),

• internal component of the model (H).

Furthermore, each component can also be classi<sup>fi</sup>ed as being an: (i) inferred or represented element (X), or (ii) observed element (Y). For example, $c _ { i , j }$ may be a variable or a set of variables in an ABM, it may be an analytical expression in a system dynamics model, a series of coded observations as per an activity map, or a UML description of an activity or roles [19,5,41]. Note that there are often multiple ways to divide M into components $C _ { k } = c _ { i , j }$ for the kth decomposition due to the conceptual and scalable nature of the framework. Primarily, the purpose of this is to enable hierarchical decomposition to different levels of abstraction to support different levels of model integration as illustrated in the case study in Section 4.

Also note that due to the diversity of modelling approaches and STS element types, it is not necessarily feasible to decompose any two models M and $M _ { k }$ into components and <sup>fi</sup>nd component pairs $( c _ { i , j } , c _ { k , l } )$ for all relevant interface points such that $c _ { i , j } = c _ { k , l } .$ For example, two different simulation models may both use a parameter $\theta ,$ de<sup>fi</sup>ned in the same way in both models. In that case, $c _ { i , j } = \theta = c _ { k , l }$ and it is possible to link the two models via this parameter directly; $c _ { i , j }$ and $c _ { k , l }$ are interface points for the respective models. If $c _ { i , j }$ is an output and $c _ { k , l }$ is an input or internal component, then the link simply involves setting $c _ { k , l } \gets c _ { i , j }$ where ← is an assignment operator. This is similarly the case where $c _ { i , j }$ is an internal component and $c _ { k , l }$ is an input; set $c _ { k , l } \gets c _ { i , j } . \mathrm { I f } c _ { i , j }$ and $c _ { k , l }$ are both inputs, it is necessary to assign the same input to both components. However, if both are internal components or outputs, it is not logical to assign the value of one component to another. Nevertheless, since both models are of the same system and assuming $c _ { i , j } = c _ { k , l } ,$ this informs model builders that this aspect of both models needs to be consistent.

However, for heterogeneous models, it is often the case that there is an inexact match between $c _ { i , j }$ and $c _ { k , l }$ if one exists at all. For example, θ may be represented as a scalar $c _ { i , j } = \theta \mathrm { i n } \mathsf { a }$ simulation model, but is represented via probabilities in a statistical model $c _ { k , l } = p ( \theta )$ ; hence, $c _ { i , \ast }$ ${ \bf \zeta } _ { j } \neq c _ { k , l } .$ . In this case, a transformation function T is needed such that $c _ { i , \ast }$ ${ \bf \Phi } _ { j } = T ( c _ { k , l } )$ ; linking of the two components then follows as before for the different combinations of internal, input and output cases. Thus, the layered framework in Fig. 3 presents an intermediary, standardised interface to systematically link STS elements to how these elements are captured in different models.

The proposed framework shown in Fig. 3 comprises three main layers relating to static objects, dynamic objects and behaviour objects. In this context, an object is de<sup>fi</sup>ned to be a discrete, tangible or intangible “thing that forms an element of or constitutes the subject matter of an investigation or science” [34]. Static objects include everything from actors (human, organisational or otherwise) [12] to process artefacts [26] to physical infrastructure [2]. The de<sup>fi</sup>nition of these objects and their relationships provide a static picture of the system. Additionally, relationships can be established between different STS elements. For example, the roles of individual humans in an organisational context [26] show the relationship between the human beings element and the organisational element. Another example is the relationship between humans and artefacts such as where a technical hardware artefact (e.g. mobile phone) belongs to an individual human.

In the next layer, the dynamic aspect of STS is represented using dynamic objects. A common approach in many <sup>fi</sup>elds, such as arti<sup>fi</sup>cial intelligence and operations management is based on the concept of state space and events, activities and processes [38,42,43]. Events represent a change in state of one or more objects at an instance in time, whereas an activity comprises multiple events and a process describes a time-ordered sequence of events that may encompass several activities. The approach of Mumayiz [38] for characterising events, activities and processes has been adopted for this categorisation — events have zero time duration (i.e. are instantaneous) and activities and processes have non-zero time duration. An example of a model that captures the dynamic layer of STS is an organisational operating procedure like an acquisition and inventorying process [5].

Finally, a primary interest in the study of STS is the behaviour of the system such as with respect to the identi<sup>fi</sup>cation and analysis of emergent behaviour [2]. However, it is also often necessary to ascertain other aspects of behaviour (i.e. STS objectives) such as with respect to STS performance, namely, quality, safety/risk, usability and reliability [9]. Note that the ability to capture speci<sup>fi</sup>c objectives and/or multiple objectives (see Section 2.2) is entirely dependent on the constituent models being integrated.

The <sup>fi</sup>nal layer in the framework represents the behavioural element. The metrics sub-layer includes, by de<sup>fi</sup>nition, a speci<sup>fi</sup>cation of the part(s) of the system that contribute to the metric of interest. The actual performance of the said metric is captured in the performance sublayer. For example, timed surveys of the human beings element at the behavioural object layer can be linked, via metric de<sup>fi</sup>nitions, to organisational operating procedure elements describing the process at the dynamic object layer.

The proposed framework provides a systematic methodology for drawing the links between different model components and for visualising these links as illustrated in Fig. 4. Each component can be classi<sup>fi</sup>ed according to the layer (and sub-layer) in the framework that it belongs to, the type of STS element that it represents, whether it is an input/ output/internal component, and whether it is observed or inferred. Information <sup>fl</sup>ow between individual components is captured with arrows. Components are considered explicit when they are explicitly represented in the model (e.g. a speci<sup>fi</sup>c parameter or part in the model), and implicit when they are not (e.g. assumptions underlying the model). For example, assumptions about the space and spatial layout can be implicit components in a process model. This is similarly the case with links where solid arrows denote explicit information <sup>fl</sup>ow in the model, and dotted arrows denote inferred information <sup>fl</sup>ow in the model (often from assumptions). By explicitly categorising and identifying the relationships between model components internally and externally and the capabilities and shortcomings (e.g. which components are implicit or assumed), it is then possible to systematically identify points for interfacing and integrating different models to obtain a whole-of-system picture.

As discussed in Section 2.2, the proposed approach extends upon the early work of Dolk and Kottemann [30]. It derives a structured methodology for building uni<sup>fi</sup>ed component decomposition representations based on graphs like that shown in Fig. 4. It extends upon the general approach of Dolk and Kottemann [30] by providing STS speci<sup>fi</sup>c context via the three layered framework and STS element hierarchy. Additionally, the proposed framework supports the second aspect of uni<sup>fi</sup>ed model execution through the classi<sup>fi</sup>cation of components within each model as input, output or internal, and by drawing links denoting information <sup>fl</sup>ow between components as depicted in Fig. 4. Such links de<sup>fi</sup>ne the ‘order of operations’ when executing the integrated model.

It should be noted that the individual models to build and integrate are dependent on the speci<sup>fi</sup>c usage scenario(s) (i.e. decision support scenarios) envisaged for a given STS application. An application of the framework to a real world case study is provided in the ensuing section.

## 4. Discussion and airport STS case study

The proposed framework enables STS model integration by providing a structure for decomposing models into components in a systematic manner to best enable the construction of links between different STS elements. This is enabled via static, dynamic and behavioural object instantiations of STS elements (where an instance of a STS element is a component in the model). This section demonstrates the utility of proposed framework with a case study application in the Airports of the Future project, an Australian Research Council linkage project comprising

![](/api/attachments/2DRSACWE/fulltext/images/1f50c4a42e3b60fda3514168e00cd6b3bff010c3f3449e0e5a3e7513f36b9f70.jpg)  
Fig. 4. Illustration of the application of the proposed framework for linking models. Components for model 1 and model 2 are decomposed according to the layered framework, and can be classi<sup>fi</sup>ed as input/output/internal (abbreviated as I/O/H) and inferred/observed (abbreviated as X/Y). Arrows denote information <sup>fl</sup>ow between components, where dashed arrows indi cate an implicit link and solid lines an explicit link. Similarly, components with a solid border are explicit, components without a border are implicit. Finally, bold lines denote a connection between two models, this connection may require an intermediary transform function as illustrated.

29 government, industry and academic organisations [22,44,41,18]. The objective of the project is to improve the ef<sup>fi</sup>ciency, security and experience of the passenger facilitation process in airports.

For the purposes of this case study, the inbound passenger facilitation process in Australian international airports is chosen as an example of socio-technical system. This process comprises four main subsystems: the Arrival Concourse (AC), the Entry Control Point (ECP), the Baggage Hall (BH), and the Secondary Examination Area (SEA) [45]. There are multiple stakeholders in this process including: Customs and Border Protection, immigration, Biosecurity, the airport operator, airlines and baggage handlers, and the passenger. In addition, there are multiple operational objectives and key performance indicators such as with respect to facilitation rate (e.g. 92% of passengers need to be cleared within 30 min), wait times, passenger experience and border security. The passenger facilitation process is a complex socio-technical system that operates within the airport system, which itself is a form of critical infrastructure [15].

This case study considers the Customs component of the airport passenger facilitation process with respect to supporting decisions on the expansion of automated border processing (‘SmartGate’). Such a national policy decision has implications on infrastructure (putting in more kiosks and whether there is space to do so), on policy (extending SmartGate eligibility to other nationalities and implementing the procedures to support that), on Key Performance Indicators (KPIs), and local operations at individual airports. These correspond to changes in the operational policy, policy and hardware, and policy elements respectively. Policy and its actualisation in business processes are an aspect that can be explicitly captured via a diagrammatic business process model (refer to Section 4.1). However, assessing the impact on KPIs and policy details (e.g. eligible nationalities) requires a causal model such as the Bayesian Network in Section 4.2. Finally, as neither of the preceding models captures spatial constraints and effects in implementing new SmartGate infrastructure, this needs to be captured in an ABM simulation model as discussed in Section 4.3.

## 4.1. Business process model

The <sup>fi</sup>rst model is a Business Process Modelling Notation (BPMN) [46] model of the facilitation process [47]. This is a diagrammatic type of model that is composed of: (i) <sup>fl</sup>ow objects, which represent activities, events and gateways, (ii) connecting objects to show <sup>fl</sup>ow and association, (iii) swim lanes for illustrating roles, and (iv) artefacts [46]. An example extract showing the high level process at Customs from the inbound BPMN model is shown in Fig. 5 [47]. For this case study, the Customs component of the inbound facilitation BPMN model [47] is used. The model shows that upon entering this process, the passenger proceeds to either SmartGate (automated) border control or manual border control. It also shows, through sub-models and subprocesses, the detailed activities involved such as the exchange of artefacts (e.g. passport) and information as part of passenger processing. At the end of the process, the passenger moves onto the next area.

The BPMN model is a diagrammatic representation of the various activities undertaken by passengers on the inbound pathway, as elicited from expert airport operators. Thus, at a high level, it represents the organisational operating procedures element in Fig. 2. Note that this means, there are inherent assumptions regarding the constituent activities, events and objects making up the process. These assumptions as well as explicit model components can be decomposed using the proposed framework for the Customs component of the model shown in Fig. 6 and at a lower, more detailed level for the manual (border control) check activity as shown in Fig. 7.

![](/api/attachments/2DRSACWE/fulltext/images/aeeca54a1f7ddae2266fdae9c22189b7ab3bfb1d9d8a4363ad750fbeb43f7c7a.jpg)  
Fig. 5. Simple, high level BPMN model of Customs processing; note that a BPMN model is represented as a diagram.

![](/api/attachments/2DRSACWE/fulltext/images/84363c575c94ab742e792b9e1ab9c1b6a9e5fd480cc7e31e36e35df695e75417.jpg)  
Fig. 6. Decomposition of the Customs processing part of the BPMN model according to the proposed framework

Note that each component is represented as described in Section 3.2. For example, 2.2, H, X: Activities show that the activity is captured at layer 2.2 (Activities) in the framework, it is an internal component, and it is inferred/represented. Furthermore, as the component is explicitly represented, it has a solid border. Note that in the BPMN, the movement and wait time component is an input at the performance metrics layer (layer 3.1); hence, as there is no explicit information <sup>fl</sup>ow from the activities to the wait time component, that connection is shown as a dashed arrow.

In contrast to Fig. 6 for the Customs component of the model, the passenger and the Customs of<sup>fi</sup>cer in the manual check component (itself a sub-component of the Customs component) and their roles are explicitly represented in this sub-model (as shown in Fig. 7). The manual check component of the model focuses on the transactions between the passenger and Customs of<sup>fi</sup>cer. As a result, many components in Fig. 6 are not present in Fig. 7, such as decision points and movement activity (i.e. it assumes no passenger movement in the manual check component).

Additionally, note that the ownership component is located in the policy and procedures element in Fig. 7 as the model explicitly represents the requirements for passengers to present artefacts (e.g. passports) that they own. Although there is also the individual human perspective to ownership, an organisational procedure is not a representation of actual passenger activity in the terminal; it is a speci<sup>fi</sup>cation of how passengers should behave as designed by policy makers.

It can be seen that even a diagram of organisational processes such as a BPMN model can cover many different elements at different layers, re<sup>fl</sup>ecting the complexity of STS. The proposed framework enables the user to categorise model components in a structured manner, enabling integration across different models. Two other models are presented below for the purposes of this integration case study.

## 4.2. Hybrid Queue-based Bayesian Network model

The next model used in this case study is a Hybrid Queue-based Bayesian Network (HQBN) model of passenger facilitation performance [48]. This is a simulation model that integrates a Bayesian Network (BN)

model of the factors affecting facilitation performance with a stochastic queue model of passenger movement. A BN is represented in the form of a directed, acyclic graph where the nodes represent factors and the directed edges represent in<sup>fl</sup>uence or causal effect [49]. Each node is associated with a Conditional Probability Table (CPT) that quanti<sup>fi</sup>es the probabilistic relationship between nodes and their parent nodes. On the other hand, the queuing model is based on the Poisson process [50] where the rate (e.g. service rate) is determined by the BN. An illustration of the structure of the model, showing an excerpt from the Customs component, is shown in Fig. 8.

Unlike the previous model, the HQBN is a simulation and inference capable model. The model provides the capability to simulate and make inferences about performance and its relationship to underlying factors and vice versa. Performance metrics that are captured in this model include capacity, throughput and dwell time for each of the four subsystems. Fig. 9 shows an example output of predicted performance.

As shown in Fig. 10 (again, for the Customs component of the inbound process), the model captures the human beings element in greater detail to support the simulation of performance metrics related to queuing and processing. In general, components such as passengers and demographics in layer one, the checkpoint<sup>2</sup> and resource schedule in layer two and KPIs in layer three are derived directly from the factors (i.e. nodes in Fig. 9) and queue counters in the HQBN model.

The performance of the system is reported with respect to Key Performance Indicators (KPIs) relating to dwell time, cycle time, throughput and the number of passengers. As passengers are the entity being measured, this performance element is a re<sup>fl</sup>ection of both the human beings element and the normal procedures operational element (i.e. it relates to organisational KPIs), thus it spans both of those columns in Fig. 10.

Unlike the BPMN model, this model makes the direct links between objects such as passenger demographics, operator ef<sup>fi</sup>ciency and checkpoint choice (corresponding to the XOR decision point in the BPMN model previously), and performance. It enables learning, simulation and analysis of different factors and their effect on performance and vice versa. This means that some components, such as the checkpoint component in Fig. 10, can serve as an input (set passenger checkpoint distributions) or an output (simulate passenger choices based on factors such as demographics) or an internal component. Additionally, the model addresses the need to capture the effects of uncertainty in STS [5] by capturing the uncertainty distribution surrounding each of the objects as well as the predicted performance. However, the organisational processes and hence activities are represented implicitly in this model through the de<sup>fi</sup>nition of relationships between objects and performance metrics; hence, the activities component in Fig. 10 does not have a border. As a result, there is no direct mechanism to evaluate the effect on performance due to changes in processes or activities.

![](/api/attachments/2DRSACWE/fulltext/images/8b9ceb32d9f7f2baf08f0bb2eb1bd4c7efad1d5aca951a983559516eff3c0253.jpg)  
Fig. 7. Decomposition of the manual check activity within the Customs processing part of the BPMN model according to the proposed framework.

## 4.3. Agent Based Model

The <sup>fi</sup>nal model used in this case study is the ABM simulation approach [22,23]. Unlike the HQBN model, this model simulates individual passengers (the agents) according to speci<sup>fi</sup>ed agent behaviours via rules and a de<sup>fi</sup>ned environment and process. This approach is shown in Fig. 11.

An application of the proposed framework to the corresponding Customs component of the ABM is presented in Fig. 12. Like the HQBN, the components are derived from model parameters such as nationality and artefacts in layer one and the resource schedule in layer two, spatial parameters such as the layout in layer one, representation of agent activities in layer two, and outputs in the form of KPIs in layer three.

Both the ABM and the HQBN previously can be used to simulate the same KPIs, however, unlike the HQBN, no direct link is made between KPI performance and the factors that affect it such as demographic and operator ef<sup>fi</sup>ciency components (hence the dotted arrows). This arises because there is no direct link between the lower layers and performance; such behaviour emerges from the simulation of individual agents via their assigned rules (de<sup>fi</sup>ned activities) and ensuing interactions. This is evident in Fig. 12 as there are no direct connections between objects in layer 1 and layer 3; additionally, the link between activities (layer 2) and performance (layer 3) is dotted, indicating an implicit link.

Like the BPMN model, the ABM model also represents the organisational procedures that are conducted within the Customs area. However, unlike the BPMN model, the activities component spans both the human element as well as the policy and procedures element because the model simulates individual passenger movements and interactions as well as operational policies. Speci<sup>fi</sup>cally, the movement of human agents through the system is governed by the social force model [51], which represents an activity of moving towards goals and avoiding collisions with other agents and obstacles. This is only achievable with an ABM like approach because it simulates the movement and interactions of individual passengers in the (physical) built environment.

![](/api/attachments/2DRSACWE/fulltext/images/4ead402069971595afb9b9839b5c2873cf788e953de801625aba4c287470262d.jpg)  
Fig. 8. An example of a BN, showing an excerpt from the Customs component of the HQBN model.

Total #PAX in Area (On-time Arrivals Scenario)  
![](/api/attachments/2DRSACWE/fulltext/images/2a06944d88443d35938334ec5b8e377823b682f259a129fd28b99b30193032cf.jpg)  
Fig. 9. An example of just one of the outputs of the HQBN showing the number of passenger in each of the four main areas of the inbound facilitation process and their variation over time.

## 4.4. Integrated model

The choice of the above three models enables the user to reconcile organisational policy and procedure as described in a BPMN model with two different simulation models with different capabilities and limitations. Given the interactions and dependencies prevalent in complex STS (refer Section 1), integration of models to create a holistic picture of the different elements that are affected by the decision at hand is crucial. The component decomposition outcomes for the Customs process for each model are combined under the new proposed STS modelling framework as shown in Fig. 13.

In Fig. 13, the components that are similar are grouped together. For example, the performance outputs of both the HQBN and ABM are shown on top (labelled A in Fig. 13); note however, that the HQBN captures the uncertainty ‘distribution’ as indicated whereas the ABM only captures the expected performance. In addition, the ABM component is an output only whereas the HQBN component can be an input or an output.

Another example is the activities component, which is represented explicitly via discrete events in an ABM and diagrammatically in a BPMN model, but implicitly in the HQBN. Note that unlike the HQBN and BPMN models, the ABM activities component simulates the movement of individual passengers, thus it straddles both the human beings STS element as well as the normal procedures STS element. This is re<sup>fl</sup>ected in the layout component of the ABM which represents the built environment element. The BPMN model represents the average displacement, which is a simpli<sup>fi</sup>cation of the layout of the building.

Through this structured decomposition of components according to the elements and layers in the proposed framework, it is possible to start identifying areas (i.e. components) of similarity and difference, and potential interface points (i.e. links). Where direct interface points (direct match in model components) are not possible, links are developed through: (i) examination of components linked to potential interface point(s), and (ii) further decomposition

## 4.4.1. Integrating operational policy and procedure with performance

As shown in Fig. 13, a change in the operational policy and procedure can be easily represented in a BPMN model. However, as seen by the lack of BPMN components in layer 3, the BPMN model alone does not provide the decision maker with the capability to predict the impact on KPIs over a range of operational scenarios (such as different <sup>fl</sup>ight schedules and demographic make-up of passengers). The HQBN is shown in Fig. 13 to provide this capability by capturing the uncertainty distribution in the system and especially in the <sup>fi</sup>nal simulated performance output. Therefore, the framework can help support the <sup>fi</sup>rst step of determining which models and elements are relevant, and which models need to be integrated (if necessary).

![](/api/attachments/2DRSACWE/fulltext/images/2f4bd145193a57cd52929456275dee59bf79ca015be0eecd06e30ee7a226cdf8.jpg)  
Fig. 10. Decomposition of the Customs processing part of the HQBN model according to the proposed framework

![](/api/attachments/2DRSACWE/fulltext/images/e86e5f85481f270f66263c2bb5d3bc663c8ef8c5bda9d4cf2f989e15dd4264d1.jpg)  
Fig. 11. Example showing a ABM simulation of a queue and service process [44]; unlike the previous models, this one explicitly captures the spatial aspect of the problem

One approach to integration is to <sup>fi</sup>rstly examine the complete component decomposition map (Fig. 13) and identify what elements and components are needed. In this <sup>fi</sup>rst scenario, the HQBN covers virtually all necessary components from demographics to performance but the key missing element is the activities component (which captures the change in operational policy and procedure). Note further that the implicit activities component in the HQBN is linked to the passengers, checkpoint (choice of SmartGate or manual check), regulatory complexity, resource schedule components, KPIs and KPI performance distribution components.

Therefore, at a high level, integration of the BPMN and HQBN requires the development of an interface that transforms explicit activities in the BPMN model to implicit activities in the HQBN model as shown at the activities component (labelled B in Fig. 13). Doing so is non-trivial as the activities component of the HQBN is non-explicit.

However, it is possible to trace the components in the HQBN that are linked to activities, namely, KPI metrics, KPI performance distributions, passengers, checkpoint choice, regulatory complexity, resource schedule, demographics, operator ef<sup>fi</sup>ciency, location, correct paperwork and the Customs of<sup>fi</sup>cer. Therefore, the framework enables the user to identify the linked upstream and downstream HQBN components and thus the interface points when integrating a BPMN and HQBN model via transformation functions. Note that the integration of the ABM and the BPMN models at this point is comparatively straightforward as both represent activities explicitly, thus enabling a direct mapping from one model to another.

These transformations can be further characterised by decomposing individual activities and decision points within the BPMN model, such as that shown in Fig. 7 for the manual check activity. At this level, it is then possible to identify speci<sup>fi</sup>c artefacts (e.g. passports), speci<sup>fi</sup>c information entities (relating to questions and answers between the Customs of<sup>fi</sup>cer and the passenger) and even event transitions (e.g. passport scanned, database search completed and so on). The corresponding linked components in the HQBN can be similarly decomposed; for example, the KPIs performance distribution component can be decomposed into speci<sup>fi</sup>c KPIs (e.g. cycle time distribution at manual check). In this particular case, the cycle time is linked to the passenger/human element of Fig. 13 which itself can be further decomposed into nationality/passport and other information entities that match with those described in the BPMN model. Thus, through repeated systematic decomposition using the layered framework and STS elements classi<sup>fi</sup>cation, it is possible to develop the details to construct $T ( c _ { k , l } ) = c _ { i , j }$ and enable model integration.

![](/api/attachments/2DRSACWE/fulltext/images/151355448601adfcbf45f127793aeabc25aa6faa38d07559daec8f1e29cadcf2.jpg)  
Fig. 12. Decomposition of the Customs processing part of the ABM model according to the proposed framework.

![](/api/attachments/2DRSACWE/fulltext/images/c18942b96c81730ddc844f0edb843926bee448697b3ea945059a43ac43dbbae1.jpg)  
Fig. 13. Combined component decomposition diagram of the three separate models, BPMN model in red, BN model in yellow and ABM model in blue. Dashed green lines denote potential interface points between the three models. A, B and C as marked are candidate interface points discussed in the text. (For interpretation of the references to colour in this <sup>fi</sup>gure legend, the reader is referred to the web version of this article.)

## 4.4.2. Integrating the spatial element

The preceding discussion revolved around the operational policy and procedure and human beings elements as captured by the BPMN and HQBN. However, continuing the previous scenario of decision support for expansion of SmartGate infrastructure, the spatial positioning of the kiosks and resulting passengers could also impact performance. Therefore, it is necessary to integrate the spatial aspect through the use of ABM. It is still desirable to integrate with the HQBN because, as shown in Fig. 10, only the HQBN provides the capability to capture the direct links between KPI performance and factors such as paperwork and demographics. The ABM cannot do so explicitly as the link between activities and KPI performance is implicit (see Fig. 12).

Although it may be tempting to focus on the spatial layout component (labelled C in Fig. 13), it is not possible to interface between the ABM and HQBN here as the HQBN does not contain a similar component. It is not ef<sup>fi</sup>cient to directly transform the ABM spatial layout component into ‘average displacement’ in the BPMN model, because the ‘average displacement’ is linked to the activities component in the BPMN model, for which there is no direct counterpart in the HQBN.

From Fig. 13, it can be seen that both the ABM and HQBN share similar components at the performance layer (labelled A in Fig. 13), however, the HQBN component can be an input or output whereas the ABM component is an output only. Therefore, through further decomposition, one way to interface the two models is to simulate passenger movement activities given a spatial layout in the ABM and link the resultant KPI output as an input to the corresponding KPI in the HQBN model.

Taking it a step further, consider the design of the transformation functions necessarily to enable such an integration. Using Fig. 13, the KPI component in the ABM can be linked to activities, and from activities to components such as roster schedule, passengers, checkpoint and layout. Note that the checkpoint component in the ABM and HQBN both correspond to the decision point component in the BPMN (i.e. go to manual check or SmartGate).

Similarly, the KPI component in the HQBN is linked to passengers, checkpoint, resource schedule, regulatory complexity and paperwork — many of these components overlap with ABM components. By tracing through the linked components in Fig. 13, it is possible to identify the relevant context factors required, the gaps in each model, and thus assist the modeller in developing transformation functions for integration.

## 4.4.3. Discussion

In the context of the case study scenario for Customs in evaluating the expansion of SmartGate, the holistic model enables the reconciliation between policy and implementation of policy vis-à-vis day-to-day airport operations. This is achieved through the integration of models of policy as captured by the BPMN with their impact on the KPIs of the organisation via the HQBN whilst taking into account terminal space constraints via the ABM.

As presented in Section 3.2 and discussed in Section 4.4, there are two main types of links between model components in general. The <sup>fi</sup>rst is via components that are a direct match and thus can be directly linked as is the case for A in Fig. 13. The second type is via a transformation, to link to the corresponding component such as case C in Fig. 13, or to ‘downstream’ components that can reside in different layers as is the case for B. Links requiring transformations are to be expected when integrating heterogeneous models [30].

It is shown through the process of integrating the three different models that a comparatively simple policy of expanding SmartGate use has <sup>fl</sup>ow-on effects on KPIs such as dwell time and throughput and is itself affected by factors such as demographics and resourcing. The latter, along with spatial constraints, inform the viability of said policy. Hence, at the simplest level, the development of an integrated component decomposition like that shown in Fig. 13 already identi<sup>fi</sup>es to decision makers what aspects of the system are impacted by decisions. This also provides a platform for decision makers in different areas within the organisation (i.e. Customs) and other stakeholders such as airports and passengers to come together for discussion.

The integrated model developed from Fig. 13 can be used for different purposes given the same SmartGate expansion policy case study. At a national level, policy makers within Customs need to design policy and corresponding business processes (captured with BPMN modelling) to meet objectives. There is a need to estimate the potential bene-<sup>fi</sup>ts and impacts of such policy, especially with respect to KPIs such as waiting time and cost (captured with HQBN modelling and/or cost modelling). For example, it may be found that reductions in waiting time are insuf<sup>fi</sup>cient without opening SmartGate to other nationalities or without upgrading SmartGate hardware.

In addition to the national perspective, there is also the local operational perspective within individual airports. In some instances, there may be insuf<sup>fi</sup>cient space (captured with ABM) to implement new SmartGate infrastructure without requiring a costly expansion of the airport terminal itself. Furthermore, there is the design and day-to-day management of the actual Customs area according to the speci<sup>fi</sup>c <sup>fl</sup>ight schedules and passenger demographics of each airport.

Application of the proposed framework to this case study in effect produces a platform for discussion (the component decomposition like that shown in Fig. 13), and an integrated model that can be used in providing decision support. Such a holistic model can be used to support the assessment of policy impact and viability, in the design of the space for SmartGate at each airport, and in the management of SmartGate infrastructure given <sup>fl</sup>ight schedules. Note that it is conceivable that local design and management could be supported with a single model (e.g. the ABM or HQBN model). However, a holistic understanding as shown in Fig. 13 can still be useful for: (i) maintaining consistency of information across stakeholders and/or departments in an organisation, and (ii) providing a platform for feedback for future policy decisions.

This case study shows that, as is the case with STS in general, one component (national policy in this instance) can have far-reaching consequences on other components within the organisation (Customs) and stakeholders outside the organisation (airports and passengers). Therefore, a systematic framework for holistic modelling is critical in reconciling the multiple perspectives and objectives within STS, such as that of policy and practice in this case study.

In this case study, three existing models were integrated to address the needs of Customs decision makers. Generally speaking, selecting suitable models to integrate requires knowledge of the capabilities of candidate modelling methods and the decision context. Wu and Mengersen [52] present such an approach based on concept of operations usage scenarios to generate modelling requirements. They use this to assess and review a range of modelling methods and usage scenarios for modelling the airport system. Additionally, Satumtira and Duenas-Osorio [25] also review existing models and their applications (usage scenarios) for infrastructure STS. Both of these works can guide the selection of suitable models for integration to support a given decision scenario.

## 5. Conclusion

The task of modelling complex, socio-technical systems (STSs) is challenging due to the interactions and interdependencies between social and technical elements, resulting in dif<sup>fi</sup>cult to predict outcomes and emergent behaviour. Although individual models are well developed, a whole-of-system model is required in order to capture these emergent phenomena; however, such a model is dif<sup>fi</sup>cult to develop due to the diversity and complexity of STS.

This paper presented a framework for understanding and decomposing STS models into components where the components are classi<sup>fi</sup>ed according to a three-layer structure comprising static, dynamic and behavioural objects. Additionally, each component is classi<sup>fi</sup>ed according to the STS element it represents, using a framework synthesised through high impact works in the STS, critical infrastructure, information technology and organisational science literature. Ultimately, the proposed framework enables the integration of different modelling approaches to create a whole-ofsystem model to support decision making.

The resultant framework is demonstrated on an airport passenger facilitation case study, showing how a ABM [22], BPMN [47] and HQBN [48] can be integrated to provide whole-of-system decision support. It is found that decomposition and classi<sup>fi</sup>cation of model components as per the STS element hierarchy and three layered framework provides a systematic way to establish information <sup>fl</sup>ow both internally and between models via links/interface points. Additionally, when integrating heterogeneous models, the framework helps to identify the transforms required and the interface points (direct or indirect) in terms of linking inputs, outputs and internal components. Note that model components can be explicit, or implicit such as is the case for model assumptions.

Such an integrated model provides the capability to capture the mutual effects between spatial elements, human being elements, policy and procedural elements that is not possible with any single model. As a result, the case study demonstrates the ability to use a holistic model to evaluate national policy and its impact on local airports at an operational level and vice versa. In addition, the framework also helps the decision maker to identify the relevant STS elements to the problem at hand and in turn help select suitable modelling approaches.

Future work includes the application of the framework to different domains, development of interactive visualisation methods, and methods to transform from one modelling component to another. Although graph based component decomposition diagrams are easy to interpret, visual complexity increases with the number of components in the model such as when depicting multiple models for integration (see Fig. 13). Future work could investigate methods to reduce the cognitive burden for decision makers by creating a <sup>fi</sup>t between the characteristics of the task and the presentation format and/or by presenting subsets of the diagram(s). Researchers can investigate both approaches by using interactive formats supporting a trial and error approach or an aspiration based (i.e. based on desired KPIs and modelling outcomes for a given decision task) interactive search process over different models, parts of models, or STS element types [53]. In addition, the development of object-oriented formulations of the framework in conjunction with suitably structured software implementations of individual models (such as the BPMN, HQBN, ABM) could lead to automated whole-of-system integration solutions.

## References

[1] R.P. Bostrom, J.S. Heinen, Mis problems and failures: a socio-technical perspective. Part I: the causes, MIS Quarterly 1 (3) (1977) 17–32.

[2] S.M. Rinaldi, J.P. Peerenboom, T.K. Kelly, Identifying, understanding, and analyzing critical infrastructure interdependencies, IEEE Control Systems 21 (6) (2001) 11–25.

[3] G. Baxter, I. Sommerville, Socio-technical systems: from design methods to systems engineering Interacting with Computers 23 (1) (2011) 4–17

[4] P. Pederson, D. Dudenhoeffer, S. Hartley, M. Permann, Critical infrastructure interdependency modeling: a survey of U.S. and international research, Tech. Rep. INL/EXT-06-11464, Idaho National Laboratory, Aug 2006

[5] T. Herrmann, M. Hoffmann, G. Kunau, K.-U. Loser, A modelling method for the development of groupware applications as socio-technical systems. Behaviour and Information Technology 23 (2) (2004) 119–135.

[6] J.K DeRosa, A research agenda for the engineering of complex systems, in: IEEE Systems Conf, 2008 pp. 1–8.

[7] International Council on Systems Engineering, Systems engineering vision 2020 INCOSE-TP-2004-004-02 2007

[8] F. Emery, E. Trist, Socio-Technical Systems, vol. 2, Pergamon, Oxford, U.K., 1960

[9] O.L. de Weck, D. Roos, C.L. Magee, Engineering Systems: Meeting Human Needs in a Complex Technological World, The MIT Press, Cambridge, Massachusetts, 2011.

[10] P. Kroes, M. Franssen, I.v.d. Poel, M. Ottens, Treating socio-technical systems as engineering systems: some conceptual problems, Systems Research and Behavioral Science 23 (6) (2006) 803–814.

[11] R.S. Dodder, J.M. Sussman, J.B. McConnell, The concept of the clios process: Integrating the study of physical and policy systems using Mexico city as an example, MIT Engineering Systems Symposium, vol. 31, Cambridge, MA, 2004.

[12] M. Ottens, M. Franssen, P. Kroes, I. van de Poel, Modelling infrastructures as sociotechnical systems, International Journal of Critical Infrastructures 2 (2) (2006) 133.

[13] S. Jones, N. Maiden, An Integrated Method for Specifying Requirements for Complex Sociotechnical Systems. Information Science Publishing. 2005

[14] M.J. Egan, Anticipating future vulnerability: de<sup>fi</sup>ning characteristics of increasingly critical infrastructure-like systems, Journal of Contingencies and Crisis Management 15 (1) (2007) 4–17.

[15] S.M. Rinaldi, Modeling and simulating critical infrastructures and their interdependencies, System Sciences, 2004. Proceedings of the 37th Annual Hawaii International Conference on, 2004 (p. 8 pp.).

[16] W.R. Ashby, An Introduction to Cybernetics, Chapman and Hall, London, 1957.

[17] Y. Bar-Yam, Unifying Principles in Complex Systems, Kluwer, Dordrecht, 2003.

[18] P.P.-Y. Wu, K. Mengersen, A review of models and model usage scenarios for an airport complex system, Transportation Research Part A: Policy and Practice 47 (2013) 124–140.

[19] A. Vespignani, Modelling dynamical processes in complex socio-technical systems, Nature Physics 8 (1) (2012) 32–39.

[20] V. Ceric, Hierarchical abilities of diagrammatic representations of discrete event simulation models, Winter Simulation Conference (1994) 589–594.

[21] D.R. Pendergraft, C.V. Robertson, S. Shrader, Simulation of an airport passenger security system, Winter Simulation Conference vol. 1 (2004) p. 878.

[22] T. Kleinschmidt, X. Guo, W. Ma, P.K. Yarlagadda, Including Airport Duty-Free Shopping in Arriving Passenger Simulation and the Opportunities This Presents, 2011.

[23] W. Ma, C. Fookes, T. Kleinschmidt, P. Yarlagadda, Modelling Passenger Flow at Airport Terminals: Individual Agent Decision Model for Stochastic Passenger Behaviour, SIMULTECH2012.

[24] D.J. Watts, S.H. Strogatz, Collective dynamics of small-world networks, Nature 393 (6684) (1998) 440–442.

[25] G. Satumtira, L. Dueas-Osorio, Synthesis of Modeling and Simulation Methods on Critical Infrastructure Interdependencies Research, Springer Berlin Heidelberg, 2010. 1–51 (Ch. 1).

[26] T. Herrmann, K.-U. Loser, Vagueness in models of socio-technical systems, Behaviour and Information Technology 18 (5) (1999) 313–323.

[27] A. Gregoriades, A. Sutcliffe, A socio-technical approach to business process simulation, Decision Support Systems 45 (4) (2008) 1017–1030.

[28] D. Mackrell, D. Kerr, L. von Hellens, A qualitative case study of the adoption and use of an agricultural decision support system in the Australian cotton industry: the socio-technical view, Decision Support Systems 47 (2) (2009) 143-153

[29] S. Kent, Model driven engineering, Integrated formal methods, Springer, 2002. 286-298.

[30] D.R. Dolk, J.E. Kottemann, Model integration and a theory of models, Decision Support Systems 9 (1) (1993) 51–63.

[31] A. Mostashari, J.M. Sussman, A framework for analysis, design and management of complex large-scale interconnected open sociotechnological systems, International Journal of Decision Support System Technology 1 (2) (2009) 53–68.

[32] C.A. Osorio, D. Dori, J. Sussman, COIM: an object-process based method for analyzing architectures of complex, interconnected, large-scale socio-technical systems, Systems Engineering 14 (4) (2011) 364–382.

[33] T.P. Hughes, The evolution of large technological systems, The social construction of technological systems: New directions in the sociology and history of technology1987. 51–82.

[34] Merriam-Webster, Dictionary, http://www.merriam-webster.com/dictionary/ (Retrieved February 13 2014)

[35] D.D. Dudenhoeffer, M.R. Permann, M. Manic, CIMS: A framework for infrastructure interdependency modeling and analysis, In Proceedings of the 38th conference on Winter simulation (2006, December) 478–485 Winter Simulation Co.

[36] M. Tsvetovat, K.M. Carley, Modeling complex socio-technical systems using multiagent simulation methods, German Journal on Arti<sup>fi</sup>cial Intelligence 2/04 (2004) 23.

[37] A. Farr, T. Kleinschmidt, S. Johnson, P. Wu, K. Mengersen, Way<sup>fi</sup>nding in airports: A bayesian network approach, Australian Bayesian Network Modelling Society Annual Conference, ABNMS (2011).

[38] S.A. Mumayiz, Overview of airport terminal simulation models, Tech. Rep. Transportation Research Record No. 12731990

[39] H. Zimmermann, OSI reference model — the ISO model of architecture for open systems interconnection, IEEE Transactions on Communications 28 (4) (1980) 425–432.

[40] Oxford University Press, Oxford Dictionaries, http://www.oxforddictionaries.com/ (Retrieved February 13 2014).

[41] V. Popovic, B. Kraal, P. Kirk, Passenger Experience in an Airport: An Activity-Centred Approach, 2009.

[42] R.A. Brooks, Intelligence without representation, Arti<sup>fi</sup>cial Intelligence 47 (13) (1991) 139–159.

[43] A. Burns, I.J. Hayes, G. Baxter, C.J. Fidge, Modelling temporal behaviour in complex socio-technical systems, Tech. rep., University of York, 2005.

[44] L. Cheng, V. Reddy, C. Fookes, P.K.D.V. Yarlagadda, Analysis of passenger group behaviour and its impact on passenger <sup>fl</sup>ow using agent-based model, Int. Conf. on Mathematical Modeling in Physical Sciences (2013).

[45] Passenger Facilitation Taskforce, International Airport Operator's Guide, 1st edition Australian Customs and Border Protection Service, 2009

[46] S.A. White, Introduction to BPMN, IBM Cooperation, 2004. 2008–2029.

[47] S. Mazhar, Report for Melbourne airport — description, <sup>fi</sup>ndings and recommendations, Tech. rep., Queensland University of Technology, September 12 2011.

[48] J. Pitchforth, P. Wu, K. Mengersen, Performance framework trial: prototype inbound passenger facilitation model <sup>fi</sup>nal report, Tech. rep., Queensland University of Technology, ACBPS, 2013.

[49] J. Pearl, Probabilistic Reasoning in Intelligent Systems, Morgan Kaufmann, 1988

[50] S.M. Ross, Introduction to Probability Models, 10th edition Academic Press, Amsterdam, 2010

[51] D. Helbing, P. Molnar, Social force model for pedestrian dynamics, Physical Review E 51 (5) (1995) 4282–4286.

[52] P. Wu, J. Pitchforth, K. Mengersen, K. Dickson, S. Newick, S. Kirk, Performance framework trial: project management plan and high level requirements, Tech. Rep., 3, Queensland University of Technology, 2013.

[53] J. Gettinger, E. Kiesling, C. Stummer, R. Vetschera, A comparison of representations for discrete multi-criteria decision problems, Decision Support Systems 54 (2) (2013) 976–985.

## Paul Wu

Paul Wu is a research fellow in the Mathematical Sciences School in the Science & Engineering Faculty of the Queensland University of Technology in Brisbane, Australia. He holds a BEng (Electrical and Computer), MEngSc (Computer and Communications) and PhD in the <sup>fi</sup>eld of avionics and arti<sup>fi</sup>cial intelligence. He has worked with Bayesian Networks and complex systems modelling in a collaborative setting with airports and government, and also in risk modelling due to over<sup>fl</sup>ight of aircraft. His research interests include complex systems modelling, Bayesian statistics, multi-criteria decision making, and planning and arti<sup>fi</sup>cial intelligence.

## Clinton Fookes

Clinton Fookes is an Associate Professor in the School of Electrical Engineering & Computer Science in the Science & Engineering Faculty of the Queensland University of Technology in Brisbane, Australia. He holds a BEng (Aerospace/Avionics), an MBA and a PhD in the <sup>fi</sup>eld of computer vision. Clinton actively researches in the <sup>fi</sup>elds of computer vision and pattern recognition including biometrics, intelligent surveillance, airport operations, and complex systems. Clinton has attracted over \$12 M of cash funding for fundamental and applied research from external competitive sources and has published over 120 internationally peer-reviewed articles. He is a member of professional organisations including the IEEE. He is also an Australian Institute of Policy and Science Young Tall Poppy and an Australian Museum Eureka Prize winner.

## Jegar Pitchforth

Jegar Pitchforth is a PhD Candidate in Mathematical Sciences at the Science and Engineering Faculty of Queensland University of Technology. He received the Bachelors of Business Management and Bachelor of Arts in Psychology from the University of Queensland. He has been a Research Assistant with the Institute of Social Science Research at the University of Queensland and a consultant for Queensland Symphony Orchestra. His research interests cover Bayesian Network models for Decision Support, validation of expert-elicited models and visualisation of complex systems models

## Kerrie Mengersen

Kerrie Mengersen is Professor in the Mathematical Sciences School in the Science & Engineering Faculty of the Queensland University of Technology in Brisbane, Australia. She is a statistician with expertise in fundamental statistical research, applied statistics and statistical consulting. She currently holds a Chair in Statistics at Queensland University of Technology. Her interests are in modelling complex systems, Bayesian statistics, mixture models and meta-analysis, and the application of these and other modern statistical methods to challenging problems encountered in industry, environment and health.

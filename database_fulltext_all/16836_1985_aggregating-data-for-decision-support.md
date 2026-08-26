---
otero_id: 16836
otero_key: "F9DDX6TW"
title: "Aggregating data for decision support"
authors: "Henk G. Sol"
year: "1985"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(85)90062-4"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Aggregating Data for Decision Support

Henk G. SOL

Information Systems Group, Department of Computer Science, Delft University of Technology, Julianalaan 132, Delft, The Netherlands

Numerous strategic and tactical decisions in organisations are based on aggregated data. A simulation-based inquiry of a Multiple Store Company leads to the conclusion that aggregation of data on local decisions does not give insight for taking global decisions. This implies that one has to question the validity of management information produced through aggregation in numerous data processing systems. It also signifies that application of models based on definition and behavioural equations can be dangerous. Simulation-based inquiry systems are, however, capable of providing support even in these circumstances. With a simulation-based decision support system for global decision-making we may analyze through disaggregation the effects of these decisions at local levels. By using a problem-solving environment based on system description and simulation, effective decision support systems can be developed efficiently.

Keywords: Aggregation, DSS, Simulation

## Introduction

There is not yet a generally accepted definition of Decision Support Systems (DSS). The change in description of DSS from ‘concept’ through ‘movement’ to ‘bandwagon’ clearly illustrates the growing interest in the managerial as well as in the research field for decision support systems.

A useful framework for research on DSS is introduced in Sprague [1980]. He discusses the perspective of the end-user, the builder and the toolsmith from which a DSS can be viewed. In accordance with this distinction the concept of a DSS-generator is put forward to bridge the gap between general tools and specific DSS.

Sprague distinguishes as the main components of a DSS a data base, a model base, and an intermediate software system which interfaces the DSS with the user. Sprague and Carlson [1982] advocate an approach to systems analysis which is intended to identify requirements in each of the three major capability areas of DSS: The approach is based on a set of four user-oriented entities: Representations, Operations, Memory Aids and Control Mechanisms'. This so-called ROMC approach can be placed in the framework proposed by Bonczek et al. [1980]. They replace the components mentioned by the concepts of a language system (LS), a knowledge system (KS) and a problem processing system (PPS). The language system is the sum of all linguistic facilities made available to the decision-maker by a DSS. A knowledge system is a DSS's body of knowledge about a problem domain. The problem processing system is the mediating mechanism between expressions of knowledge in the knowledge system and expressions of problems in the language system.

In Sol [1982] we argued that much more attention has to be paid to the process of solving ill-structured problems. Problem-solving is an iterative modeling process, in which we identify the activities of conceptualization, problem specification, solution finding and implementation. We make a distinction between:

(a) Conceptual and empirical models;

(b) Descriptive and prescriptive models. We call a descriptive empirical model an ‘understanding model' or 'epistemological model'. A prescriptive empirical model is called a 'target solution' or 'design'.

The activity of CONCEPTUALIZATION comprises firstly the choice of a vehicle for communication and of a metatheory. The metatheory comprises a Weltanschauung and a construct paradigm. Thereafter, a conceptual model of the problem situation is formulated with the help of these. The conceptual model defines the variables that will be used to specify the nature of the problem in broad terms. It presents a ‘vision’ of the problem situation described in a specific application domain.

Once the conceptual model of the problem situation has been arrived at a descriptive empirical model has to be specified. By analysing the empirical model of the existing situation the PROBLEM SPECIFICATION has to become clear. The connection between this understanding model and the problem as perceived in reality reflects the degree of correspondence between these two. This can guide the problem owner in the selection and acceptance of courses of action.

Given the problem specification, the activity of SOLUTION FINDING starts off. Solution finding is an iterative process of questioning and answering, or of ANALYSIS and SYNTHESIS, where computers might be of great help. After a description of the problem situation in a descriptive model, the creation of prescriptive conceptual and empirical models starts off. The analysis of the understanding model may have generated some alternative solutions. Other solutions should be created from a design philosophy.

When a solution is found, a design or target solution is IMPLEMENTED, which influences the problem situation.

We define a problem as well-structured if the following conditions are met:

1. The set of alternative courses of actions is finite and limited;

2. The solutions are consistently derived from an empirical model that shows a good correspondence;

3. The effectiveness and efficiency of the courses of action can be numerically evaluated.

Problems that do not fulfill these requirements are defined as being ill-structured. Especially ill-structured problems demand specific emphasis on the activities of conceptualization and problem specification, leading to a good correspondence between the problem situation and the empirically supported model of it, see Sol [1982]. This understanding model is the only frame of reference for creating and evaluating alternative courses of action, leading to a design and a target solution.

In order to be able to describe the distinction between tools, specific DSS and DSS-generators, the logical components of a DSS, as well as the process of decision-making, we introduced in Sol [1983] Fig. 1, which integrates the framework of Sprague, Bonczek et al. and ours. The efficiency and effectiveness of the process of problem-solving are depending on:

\- A paradigm or Weltanschauung governing the conceptualization and the problem specification;

\- A construct paradigm or modelcycle, expressing in broad terms the order of activities;

\- A methodology, as an actual sequence of activities in view of a problem situation, telling what to do in which activity;

\- A theory, contributing to the actualization of the modelcycle and the methodology in terms of how the activity is to be performed.

It should be clear that a methodology cannot be discussed and evaluated apart from the Weltanschauung, the construct paradigm and the possible theories involved.

Placing recent literature on DSS in this framework we make the following observations:

1. As to the paradigm or Weltanschauung applied, we may conclude that the one of loosely-coupled systems or nearly decomposable systems is still prevailing. It is striking how little thought is given to the elicitation of assumptions governing the construction of DSS.

2. The model cycle behind most contributions can be characterized as a Singerian one, trying to integrate scientific, ethical and esthetic modes of thought in a synthetic, interdisciplinary way. However, most approaches start from the premise that more and better information will also lead to better decisions. Dickson [1983] identifies as required facilities for management support: writing, communicating, individual processing, managing data, problem finding, making decisions and conveying decisions. The availability of data and appropriateness of data for decision-making in organizations is not much questioned, which might be in contradiction with the Singerian point of departure.

![](/api/attachments/F9DDX6TW/fulltext/images/328cc5133b825a95c19404c269153febf54271a0f9d47b4bd714e4a2185dde2b.jpg)  
Fig. 1

3. As to a methodology for developing DSS, it is difficult to identify a generic framework. It is clear that an evolutionary or incremental approach is prevailing. Therefore, Keen [1980] applies the term DSS to situations where a final system can be developed only through an adaptive process of learning and evolution. We still need more insight in the process of actually developing DSS. We refer to Sol [1984] for an assessment of the prototyping strategy.

4. As to the possible theories for constructing DSS, we observe that co-ordination of decision-making processes is still a neglected topic. Bosman [1983] doubts whether the paradigm of loosely coupled systems or nearly decomposable systems as applied in many DSS-contributions can play the role of a generic mechanism for the construction of theories on organizational decision-making. He concludes that for the construction of DSS, not only a Weltanschauung, a construct paradigm and a methodology are to be considered, but that a development philosophy is at least as important.

We may summarize these remarks in the observation that a great many contributions start from the premise that decision support and coordination of decision-making processes can be achieved through aggregation of data. Keen [1980] presents a summary of major case studies, all using data on an aggregated level. The same applies to the case studies presented in Alter [1980] and Sol [1983]. The cases mostly deal with strategic and tactical problems, supported by corporate or financial models. It is striking that these models are mostly fed with aggregated data supporting functional relationships in terms of definition equations and of behavioural equations. These behavioural equations express effectiveness relationships between endogenous and exogenous variables. In a great many DSS a solution to a problem is strived at by applying what-if analysis, goal-seeking, Monte Carlo simulation or optimization to these functional relationships. However, the validity of the parameters in these equations, mostly technical coefficients in production functions or behavioural coefficients, is not much questioned.

In this contribution we address the question what use can be made of aggregated data fed into equation models in order to achieve co-ordination in organizations. In section 2 we deal with an appropriate research methodology to look into this question. In section 3 we apply simulation inquiry to a case, showing difficulties in using aggregated data to achieve co-ordination. Section 4 discusses a possible way out by applying a simulation based decision support as a prescriptive target solution. In section 5 we explore the generalizability of our findings, as well as of our approach to the development of information systems and of DSS. Section 6 presents our conclusions.

## 2. A Research Strategy: Simulation

In order to find an appropriate approach to look into the question formulated above, we have to get insight in the very nature of decision-making processes, whether or not they are described by models based on aggregated data. We therefore look again at fig. 1. The conceptual model controls the problem specification as it emerges during the analysis by the understanding model. The distinction between a conceptual model and an empirical model reflects the special character of conceptualization on the one hand, and problem specification and solution finding through experimentation on the other. Data are needed to construct an empirical model and to accept its degree of correspondence with the actual problem situation. However, in analyzing individual decision-making processes, it is often very difficult to analyze how data is used by individuals. As we have to give an empirical content to the conceptual model, we demand a methodology which may generate these data. Therefore, we do have to specify explicitly conceptual models and empirical models. Subsequently, we have to describe the way the models are placed in an empirical environment in the search for a solution.

In Sol [1982] we argue that the inductive–hypothetic model cycle is most appropriate in this case. We remark that this model cycle:

\- Emphasizes the activities of conceptualization and problem specification in its request for an expression of a conceptual model and an empirical model, thereby underlining the specification and testing of premises in an inductive way;

\- Tries to make a vision concrete and to provide a rapid feedback;

\- Opens up possibilities for a problem-specification using an interdisciplinary approach;

\- Enables the generation of various alternatives for the solution of the problem, starting if possible with an analysis of the existing situation;

\- Regards the phases of analysis and synthesis in the activity of solution finding as interdependent.

For the construction of conceptual models and empirical models we need a description form or language which does not restrict the capabilities of inquirers and decision-makers in making models and creating evidence. We make a distinction between on the one hand a description form using equations, and on the other hand process or rule-based models.

We encounter the equation models frequently in DSS, especially in corporate or financial models. Although the functional relationships in these models may be applied in a non-procedural way as in several DSS-generators, they still apply to the outside of a phenomenon seen as a black-box.

In the process or rule based models we do not try to summarize a process in equation form. Instead, one tries to describe the sequence of events in a system. We introduce the notion of an ENTITY as an identifiable set of associated ATTRIBUTES. An entity may portray behaviour by applying one or more transformation rules to change the values of some of its attributes and by interactions with other entities. We may define in a SCENARIO related to an entity the possible transformation rules and the possible interaction paths of an entity, as well as the conditions under which these can be actualized. The notions of an entity and a scenario enable us to 'open the black-box' of an individual decision-maker and to specify the concepts and rules applied. As to the construction of a conceptual model of an individual decision-maker, we have to describe how scenario's of entities with their attributes are actualized. We may specify various psychological types of a decision-maker in a multidisciplinary way by introducing entities with corresponding attributes and scenario's for processing data and making decisions. In a scenario for an individual we may even describe the changes in the data input mode and decision-making during the process of problem-solving. We observe that scenario's for portraying behaviour may bring about transformation rules not previously thought of, as well as attributes and interaction paths to other entities. He only observes a 'representative state' of an entity i.e., those attributes and that part of the scenario which give meaning to him. However, this representativeness may change dynamically during the problem-solving process.

The process of inquiry according to this modelcycle can be given a specific shape by using simulation as a methodology. The concept of simulation in the meaning of DOING AS IF is quite old. In the field of Operations Research simulation was, and still is, looked upon as a method of the LAST RESORT, when al else fails. In a scientific environment it is used as a methodology to perform EXPERIMENTS with models of complex systems.

More recently, simulation is put forward as a DISTINCTIVE methodology to solve problems. Simulation is then defined, following Shannon [1975], as the PROCESS of designing a MODEL SYSTEM of a concrete SYSTEM and conducting EXPERIMENTS with this model system in order to UNDERSTAND the BEHAVIOUR of a concrete system and/or to EVALUATE various

STRATEGIES for the OPERATION of the system. This definition of simulation is quite broad. However, the essential of simulation, and of prototyping, is that a conceptual model is reduced or formalized into a model system in view of the availability and accessibility of data. The process of model system construction comprises distinctive steps, related to the problem situation. These can be practical problems, problems to find an explanation for a phenomenon, or problems caused by objections against a proposed solution.

With simulation we achieve:

\- The possibility to emphasize the activity of conceptualization by presenting freedom for the construction of a conceptual model;

\- The possibility to construct a model in view of the availability and attainability of data, and to place it as model system in an experimental frame;

\- The possibility to generate alternative solutions and analyze these in comparison with the initial specifications;

\- The possibility to facilitate implementation.

Simulation based inquiry comprises a sequence of activities. The activity of CONCEPTUALIZATION consists of three distinct steps: The first step is the choice of a vehicle for communication and of a context for conceptualization, the description of the application domain. As our vehicle we often choose the programming language Simula, where the entity–attribute–action construct as embodied in the CLASS-concept is the cornerstone for possible application domain specifications. The second step comprises the identification of entity-categories in a given problem specification using the concepts in the application domain. In the third step, the specification or system description, the identified entity-categories are used to generate a conceptual model of the object system.

The activity of SIMULATION MODEL CONSTRUCTION comprises the transition of a conceptual model to a simulation model which has to be executed on a machine with a number of physical constraints. The conceptual model defines the scope for the specification of a simulation model without referring to available data. In the construction of a simulation model, reduction is an important step. Reduction can be achieved by:

\- Replacing one or more deterministically valued attributes by stochastic attributes, taking the availability of data into account;

\- Coarsening the range set of one or more attributes;

\- Simplification of entity-entity interaction by entity-categories, which define special associations, and by functions and procedures;

\- Aggregating entities together in instances of new entity-categories.

In order to place a simulation model as a system description in an experimental frame a simulation model system is constructed. The simulation model is then extended into an executable simulation model system entity by a specification of a treatment. An experimental frame is a set of possible treatments.

We make a distinction between a simulation model and a simulation model system, because we can now more clearly pay attention to the considerations to achieve model reduction and for exposing treatments to the model in an experimental frame. The EXPERIMENTATION or generation of evidence from the simulation model in an experimental frame is done in four phases, namely verification, validation, screening and investigation, see Sol [1982].

For an investigation of our research question we require an empirical situation. For such a case we require that:

\- It contains enough complexity;

\- It does not have an exceptional organizational structure;

\- Empirical data is available.

In order to reduce the time in dealing with a practical situation, we take a hypothetical case of a Multiple Store Company, see Sol [1982]. Of course, the drawback of a hypothetical situation is the impossibility of a replicative validation. Taking up a hypothetical case may on the other hand also show the strength of simulation for theory development.

## 3. A Case: Towards an Understanding Model

We introduce the hypothetical case of a Multiple Store Company (MSC):

The MSC consists of a central headquarters, one factory, two warehouses and ten stores. The stores are geographically spread. Six of them are served by the first warehouse, four by the second one. The product-mix of the Company comprises some 1100 articles, of which a 200 are made in its own factory. These articles are named own articles, whereas the others are referred to as commerce articles.

The store-managers have a decentralized responsibility as to the ordering of articles. They mainly order once or twice a week.

At the warehouse level, the ordering of commerce articles and of own articles as well as the routing is done centrally, once a week.

The factory manager performs the planning for the orders received from the warehouses and the purchase of required material.

At the headquarters a central computer system is in operation for financial and personnel administration, invoicing and central ordering of commerce and of own articles.

The problems envisaged by the Company can be summarized as follows:

1. At the corporate level managers are not sure that the centralization of decision-making in the factory and in the warehouses, and the decentralized responsibility of the store managers are the best solution for the Company.

2. Also some managers at headquarters have the idea that decentralized data processing could be cheaper, whereas others want to stimulate the use of computers for the support of decisions taken in the Company.

3. The Company does not know how to meet fast environmental changes.

4. From lower and middle management some problems with the budget control procedures can be heard.

5. Some lower managers feel that the introduction of small, personal computers could lighten their tasks.

An outside consultant is asked to react on the points raised and especially on the ill-structured problems that deal with:

\- High inventories;

\- Out of stock positions.

Possible explanations for these may be found in:

\- Fluctuations in demand;

\- Delivery times of commerce articles;

\- Changes in the environment.

Possibilities to control this situation may be sought in:

\- Other procedures for inventory control;

\- Changes in the product mix;

\- Introduction of an information system to speed up data processing and to provide possibly more and better information.

Taking up the role of the outside consultant we apply simulation to analyze the problem situation in the MSC. We start with the construction of a conceptual model.

We make a distinction between local decisions and global decisions. LOCAL decisions are defined through decision rules that are:

\- Of a relatively simple nature;

\- Specified by entities in physical quantities;

\- Used to direct and control the movements of parts and goods in the organization;

\- In most cases directly related to the transaction processing,

\- Efficiency oriented;

\- Not directly defined to solve co-ordination problems.

GLOBAL decisions have as their main purpose the solution of co-ordination problems, which can exist at different levels of the organization, according to different levels of aggregation of data.

Our approach comprises the following steps:

\- Choose appropriate building blocks tailored to this specific problem area or business class and make a system description of the existing situation;

\- Identify decision processes and describe decision rules;

\- Develop a simulation model and analyze the decision rules;

\- Present the simulation model system to the decision makers and analyze the process of decision-making in this context;

\- Look into the transformation of the prototype model system to a concrete decision support system or information system.

We look into local decision processes and the flow of material and data necessary to realize these. The obvious processes deal with inventories and ordering. Subsequently, we look into global decision-making. We assume that local decisions are co-ordinated through aggregation over article characteristics, e.g., for solving inventory problems and product mix problems.

We identify the entities of a store manager, store ordering, warehouse ordering, article, location, order, order line, delivery, delivery line.

It turns out that a system description in the programming language SIMULA along these lines is easy and natural.

For the analysis of the situation in the MSC we have to transform the conceptual model into a simulation model. Subsequently, we follow the phases of verification, validation, screening and investigation, respectively.

We consider what variables are appropriate to analyze local decisions regarding inventories and ways these are co-ordinated by aggregation. We identify for each article per location, registered per day, the following:

\- Demand;

\- Delivered quantity;

\- Technical quantity on hand;

\- Economical quantity on hand; and

\- Number of orders.

For these data we can calculate for each article per location per variable period the following:

\- Aggregates of the variables above;

\- Mean, standard deviation, minimum and maximum ordersize;

and for each location per variable period;

\- Number of order lines;

\- Number of delivery lines;

\- Number of orders;

\- Number of deliveries.

The simulation model is developed in several parts to facilitate verification. The daily output files as well as the aggregated output files are to be analyzed in the phases of verification, validation, screening and investigation. As we focus on the co-ordination of decision processes through aggregation of data, we have to provide facilities for aggregation over time as well as over article characteristics. In the screening and investigation phase, statistical analysis may be used to explore possible relations between exogenous and endogenous variables. In order to facilitate these investigations we develop a range of specific programs in Simula which may be applied in a recursive way.

We check the steady-state behaviour, determine the run-length and the number of replications. The replicative validation turns out to be acceptable.

In the screening we apply regression analysis to look into all possible relations between exogenous and endogenous variables. We assume that possible relations may exist between the exogenous variables, maximum stock (MAXSTOCK), contribution, mean demand (MDEM), mean delivered quantity (MDEL), standard deviation of demand (STDDEM), standard deviation of delivered quantity (STDDEL) and the endogenous ones mean economic quantity on hand (MEQOH), mean technical quantity on hand (MTQOH), mean number of orders (MORDERS), mean ordersize (MOS)

and mean out of stocks (MDEM–MDEL). In the actual situation the variables reorder period, warehouse period, factory period, initialization factor for tqoh, type of ordering system, ordering parameters and delivery time parameters are not subject to variation.

This statistical analysis leads to the following conclusions, see for more detailed figures, Sol [1982]:

1. At the factory level in none of the cases any equation can be accepted.

2. The variable MORDERS gives a bad explanation.

3. The variable MOS does not give a good explanation in any of the cases.

4. The variable MDEM–MDEL gives in all cases no acceptable equations.

5. Stepwise multiple regression does not change the simple linear regressions for more than several percent.

6. Multiplicative equations do not give any explanation.

7. For an individual store article several explanations can be found, although the rsquares are not too high. The variation in MTQOH is generally not well explained, only for MEQOH acceptable explanation is found.

8. For an individual warehouse article very few equations are accepted.

9. Pooling is only allowed over all articles per location or over own articles and commerce articles per location. Reasonable explanations with MAXSTOCK can be found, which are better than for individual articles.

10. Using time series on a weekly basis, only relationships can be identified for poolings over articles per store.

This analysis of the situation in the MSC does signify that the availability of more data on local decision processes does not lead necessarily to more insight, and thereby to more opportunities for decision making. In aggregating data of articles, not many relationships are accepted which can be used for decision making at a global level. This implies that it is difficult to support co-ordination on the basis of aggregated data. Analysis of time series suggests relationships which cannot found back in a more detailed examination. The currency of information is therefore of little importance.

## 4. A Case: Towards a Prescriptive Model

The results of the analysis of the situation in the MSC and a development theory lead to various alternatives for design. In a subsequent screening we analyze the variables which were kept constant in the existing situation. We look also into other possible ordering systems. After a screening of important variables an experimental design is made. Experiments are carried out after an inquiry into the feasibility of each treatment. Detailed analysis of the outcome leads to a few remaining alternatives. An alternative consisting of an ordering system with exponential smoothing rules turns out to give a satisfactory solution with low out of stocks and low inventories. We analyze for the latter alternative the effect of changes in instrumental variables. Again we find that it is difficult to analyze these effects using time series or cross-section data, even with various aggregations. We only find a relation between meqoh and maxstock and mtqoh and maxstock at location level and in aggregating one article over all stores.

Aggregation of data on local decisions has a limited contribution for taking global decisions with regard to co-ordination between articles at store and at warehouse level. If this data driven approach as followed in a great many DSS, does not work, what way out do we have?

Another way to achieve co-ordination at a global level is to apply disaggregation of article data. We then introduce a simulation model system as a decision support system to analyze what effects decisions proposed at a global level may have at local article level before implementing them. The simulation model system outlined so far can be used to explore possible alternatives by comparing these two by two. Such a simulation based inquiry system as DSS can be seen as a part of a concrete information system. The necessary inputs for a sample of articles, are:

\- MAXSTOCK;

\- Reorder period;

\- Ordering parameters;

\- Distribution of actual delivery times;

\- Actual TQOH, for verification and validation purposes;

\- Contribution to store turnover;

\- Distribution of order size;

\- Distribution of daily demand per store.

It is thus not necessary to keep track of all historical data per location. Instead, for disaggregation it is enough to build up some distribution statistics.

Developing information systems is a complex problem. This complexity is mostly addressed from a linear development paradigm. An appropriate phasing of the development process has to lead to manageable activities. However, we believe that it is more appropriate to tackle the complexity of developing information systems by distinguishing four sub-problems, see Sol [1982]:

\- Systelogical problem: The generation of one or more information system change facilitated object system alternatives and the selection of that alternative which is better or best in either an efficiency or effectiveness sense.

\- Infological problem: Given, by analysis, determination or assumption, a solution to the systological problem, determining and specifying the information requirements (both elements and properties) and their mode of presentation for those individuals associated with the object system;

\- Datalogical problem: Given by analysis, determination or assumption, a solution to the infological problems associated with the information system related object systems, to generate alternative data processing sequences and groupings necessary to satisfy these requirements, and to select from among those alternatives that which is better or best in an efficiency or effectiveness sense.

\- Technological problem: Given, by analysis, determination or assumption, a solution to the datalogical problem, to generate alternative technical implementations on a machine with hardware and software constraints.

Phasing and control of the project are of course to be directed towards the processes of solving these problems.

So far, we have dealt with the systological problem. The target system developed in this way is a well-defined starting point for the construction of a concrete information system. A possible way to proceed in the infological analysis is as follows.

As to the infological analysis:

1. Take the systelogical target system as a point of departure. The data model used so far is the entity–attribute–action description form. The target system reflects the modeller's awareness of the shortcomings, abstractions, interpretations and naming conventions. Then the target system has to be specified completely. For instance, administrative data processing and man-computer communications are to be specified as far as these are part of the concrete information system to be constructed.

2. Specify information and operational requirements by interviews and by simulation through prototype model systems. The simulations may bring out specific queries, which are not foreseen, and ergonomic requirements, like response time and screen-layouts. We may formulate hypotheses in this respect and construct new prototypes to check these. The result is a refined Conceptual Information Model and a specification of information and operational requirements.

3. Choose a data model for the mapping of a CIM to CDBM and a CPM. A conceptual Data Base Model presents a restricted snapshot of the Universe of Discourse. A Conceptual Programming Model defines a set of processes to manipulate and maintain a CDBM in accordance with the stated requirements. If we take the entity–attribute–action description form of SIMULA, we arrive at a mixture of CDBM and CPM with implied efficiency considerations. The binary relationship model is most flexible in this respect.

4. Map the model system to a CDBM and CPM in the data model chosen. If we take the binary relationship one as presented for instance by NIAM, this mapping may proceed in the following steps.

(1) Make for each entity-category a non-lexical object type. The identification of the entity-category becomes a bridge between the object type and a lexical object type.

(2) Each attribute of an entity-category becomes an idea type referring to the object type of the entity and the object type referenced by the attribute. The referenced object type may be a prespecified type as is the case for a data type such as integer, real, Boolean, text and character. If the referenced object type does not exist, it has to be identified and specified. Each attribute places a uniqueness constraint on both parts of the idea type.

(3) A data set within an entity represents an idea type, where the corresponding data items are specified in the second part of the idea type with a uniqueness constraint on the data item part.

(4) Prefixing of entity categories is translated into an idea type between the prefixed object and the prefixing object, with a uniqueness constraint on both parts.

(5) The action parts are translated either into exclusion, subset and transition constraints specified in the conceptual schema, or into procedural constraints specified through interpreted predicate logic in the CPM.

For the datalogical and technological design we may translate the target system, given in the entity–attribute–action form, to one or more external and internal schemata. If we choose a CODASYL-type data base, we map each data item one-to-one to a record, by reducing the prefix-structure, if any, to a flat record. Data sets are introduced in the same way by mapping a data set to a CODASYL set. The remaining processes are converted into program modules linked to the data bases. We may use specific utilities to test the generated prototype data bases on several query capabilities. In this way we create feasible solutions which are not necessarily most efficient. The prototype model systems mentioned can also be linked to the databases generated and used for tuning purposes later on.

## 5. Generalization

The case of the MSC teaches us an interesting lesson on the applicability of aggregation for coordination and of the possible solution by simulation-based inquiry. Can this conclusion be generalized? As to the contribution of aggregated data to co-ordination in organizations one might object that we used a hypothetical case. In several real life cases ranging from profit to non-profit organizations we reached similar conclusions (see, e.g., Sol [1984a,1984b]). Reuyl [1982] analyzed the German cigarette market and came out with similar conclusions.

When aggregated data are not appropriate to feed functional relationships used in models for decision support, a way out can be found by simulation-based inquiry using process models. The choice of a Weltanschauung and of a construct paradigm as points of departure for the activities of conceptualization and problem specification are closely related. The expression of a methodology and a theory, in view of a problem under consideration, follows these choices closely. We put forward the idea that it is possible to combine a Weltanschauung with a construct paradigm by giving the concepts of a DSS-generator, a language system, a knowledge system and a problem processing system a concrete form in the notion of an INQUIRY SYSTEM. We define an inquiry system as a structured set of instruments which can be used as a context or modelling environment in the problem-solving activities. It expresses a methodology in view of a problem area.

The inquiry system serves in the first instance as a ‘context for conceptualization’. It presents the building blocks for the creation of a system description. Subsequently, the inquiry system appears as a conceptual model for the problem specification, in a model system for the solution finding and in a target system for the implementation.

The notion of an inquiry system has two important contributions:

1. By a translation of a Weltanschauung and a construct paradigm into a context for conceptualization one can discuss the premises behind theory formulation. Through its application in the construction of a conceptual model and a model system, a theory comes about.

2. The products of the various activities in the process of problem-solving are building on each other as successive layers. This allows for an easy adjustment of individual theories and for an evolutionary development of the target system.

An inquiry system integrates what is called a language system (LS), a knowledge system (KS) and a problem processing system (PPS), see Bonczek [1981]. The inquiry system reflects an extensible LS with various contexts and data models. We are able to define various conceptual models as conceptual schemata reflecting the KS. Our inquiry system as a PPS, explicitly addresses the phases of verification, validation, screening and investigation.

For effective problem-solving a family of simulation-based inquiry systems can be implemented in the programming language SIMULA. This problem-solving environment comprises, the instruments of a conceptualizer, a modeller, an experimenter and an evaluator. Various classes of entity-categories form an application environment for a flexible conceptualization of the problem situation at hand. The specification of a conceptual model and the transition to a simulation model in an experimental frame is done in explicit transformation steps, subject to requirements of consistency and correspondence. The inter-relations between the various activities find form in successive models building on each other in layers. This is easily implemented in Simula by making the context, the conceptual model, the simulation model and the simulation model system 'prefixed' CLASSES, see Sol [1982]. The application of an experimentation data base is shown to be capable of avoiding confusion of evolutionary model building and experimentation. The lessons learned in applying the SIMULA-based inquiry systems are also applicable to prototyping, as is shown in Sol [1984b].

In the case of the Multiple Store Company we applied the inquiry system to a whole organization. A further step may be the development of 'personalized' inquiry systems, i.e., systems which can be tailored to individual decision-makers or groups by developing specific programming and modelling environments with specific instruments.

## 6. Conclusions

Aggregation of data on local decisions does not present insight for global decision-making. We may relate the latter to the local decisions by a simulation-based inquiry. Then, the simulation based inquiry system for the solution of the organizational problems may re-appear as a decision support system in the concrete information system.

Our inquiry system presents a problem processing system which is integrated with a knowledge system and a language system by the provision of a modelling environment and various models as successive layers. In this way the alternative space can easily be modified and explored.

With a simulation-based DSS for global decision-making we may analyze through disaggregations the effects of these decisions at local levels. We conclude that the DSS not only contributes to the generation of alternatives, but that it may also realize a better co-ordination.

Attention to the solution of the systelogical problem pays of in the solution of the infological, datalogical and technological problems. The transition from systelogical problem-solving to info-logical analysis, datalogical design, technological design and implementation is less difficult and time-consuming than expected. Firstly, this is realized by presenting the products of the various activities in the problem-solving process as successive layers. This facilitates communication, documentation and an evolutionary development. Secondly, a specification in an entity-attribute-action form, as arrived at in the target system, can easily be transformed into a conceptual data base model and a conceptual programming model, as well as into internal and external schemata and programs.

Ill-structured organizational problems, and thus the problem of developing information systems, can effectively be approached by inquiry systems. The simulation methodology contributes to a participative design and evolutionary development, where simulation models and prototypes form instances for refutation.

## References

[1] Bonczek, R.H., C.W. Holsapple, and A.B. Whinston, Foundations of Decision Support Systems, Academic Press, New York (1981).

[2] Bosman, A., Decision Support Systems: Problem Processing and Co-ordination in: Processes and Tools for Decision Support, Sol, H.G ed., North-Holland, Amsterdam, New York (1983).

[3] Dickson, G., Requisite Functions for a Management Support Facility in: Processes and Tools for Decision Support, Sol, H.G. ed., North-Holland, Amsterdam, New York, (1983)

[4] Keen, P.G.W., Adaptive Design for Decision Support Systems, Data Base 12 (1980).

[5] Olle, T.W., H.G. Sol and A.A. Verrijn-Stuart, (eds.), Information Systems Design Methodologies: A Comparative Review, North-Holland, Amsterdam, New York (1982).

[6] Reuyl, J.C., On the Determination of Advertising Effectiveness: An Empirical Study of the German Cigarette Market, PhD Thesis University of Groningen, Stenfert Kroese, (1982).

[7] Sol, H.G., Simulation in Information Systems Development, PhD Thesis, University of Groningen, (1982).

[8] Sol, H.G., Processes and Tools for Decision Support: Inferences for Future Developments, North-Holland, Amsterdam, New York (1983).

[9] Sol, H.G., The Emerging Role of Simulation Based Inquiry Systems for Decision Support, in: Beyond Productivity: Information Systems Development for Organizational Effectiveness, Bemelmans, Th.M.A., ed., North-Holland, Amsterdam, New York (1984a).

[10] Sol, H.G., Prototyping: A Methodological Assessment, in: Proceedings of the Working Conference on Prototyping, Budde, R. et al., eds., Springer, Berlin, New York (1984b).

[11] Sprague, R.H., A Framework for Research on Decision Support Systems, in: Fick, G. and R.H. Sprague (eds.), Decision Support Systems: Issues and Challenges, Pergamon Press, Oxford, (1980).

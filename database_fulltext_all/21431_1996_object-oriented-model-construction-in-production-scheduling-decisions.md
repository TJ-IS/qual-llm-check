---
otero_id: 21431
otero_key: "4Y2ECGJS"
title: "Object-oriented model construction in production scheduling decisions"
authors: "Sharma N. Pillutla; Barin N. Nag"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(96)80010-8"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Object-oriented model construction in production scheduling decisions

Sharma N. Pillutla, Barin N. Nag \*

Department of Management, School of Business and Economics, Towson State University, Towson, MD 21204-7197, USA

## Abstract

The importance of rapid and automated model development for decision support is recognized in production scheduling applications, where problem instances are often similar to some general model but not necessarily consistent with it, and yet there is little of either time or modeling expertise available. In the modeling literature, there are few, if any, constructs of model development from component parts. Model construction is closely associated with the structure and representation of model information and with the abstraction of problem information from the user. Proceeding from a taxonomy of general production scheduling models, we develop a schema to represent model information in an object-oriented framework that relies on the definitions of natural entities, rather than on a collection of models from past experience. We show the interactions of user information with the model objects in the construction of a model to support a decision in a problem instance.

Keywords: Model construction; Model management; Production scheduling; Object-oriented

## 1. Introduction

The decision problems that arise in the scheduling of production have been extensively studied in research literature and later applied successfully in industry practice. The economics of the decision problem is such as to encourage the development of optimal models. Even near-optimal (heuristic) models have proved effective where the optimal model does not exist or is difficult to apply. It this context, it may be seen that the nature of the problem is operational, and that the character of the decision is structured. In fact, the domain of production scheduling has been fertile in the development of structured decision models, which exist in a generalized form in the research literature.

The practical application of a generalized model is an instantiation of the model designed to fit the individual characteristics of a decision problem, and is constructed using the specific parameters of the individual problem. In view of the complexity of the model construction process, this task is often removed from the decision maker and left to the analyst to perform. Dynamic variations in the problem and the model further necessitate the actions of the analyst in model construction and development.

The consequent removal from the decision making end-user is hardly desirable.

Model Management Systems (MMS) provide a means of involving the decision making end-user in the modeling and problem-solving process. The objective of an MMS is to perform the functions of an analyst with a knowledge of the decision problem, and an expertise in the model-building and problem-solving process. The effect of an MMS is to support the decision making by translating problem characteristics to model characteristics, thus selecting model components to construct a model instance focused on a given problem.

Thus, the direction of much of the MMS research (the current piece included) is to extend enhanced support to the decision making process by making it simpler for the decision maker to use existing optimization models in an observed problem. The speed and simplicity of model generation implies the ability to “track” problems, i.e., to model dynamic variations in these problems. Business application scenarios and market dynamics often require a decision maker to derive model solutions in rapid succession, sometimes to answer a series of “what if” scenarios. A decision maker has neither the technical preparation on the model characteristics nor the time to develop models suited for individual scenarios. An MMS should aid the decision maker in (a) identifying the problem characteristics, (b) relating the problem characteristics to the model attributes, (c) selecting the model components of interest, (d) constructing the composite model from its respective components, and (e) solving the model to display the results. This study concentrates on parts (a) through (d), with the assumption that model solvers exist to take care of (e), an assumption that is valid for many widely-used models. Thus, in several respects, the issue is one of interfacing the knowledge and the knowledge representation as found in (a) to that of (b) and so on successively through (d) and even (e).

The issues of knowledge inherent to a problem, and the issues of knowledge representation of the problem and its modeling process have been extensively discussed in MMS literature, especially as it pertains to the development of a Decision Support System (DSS). It has been theorized that knowledge about an entity, in our case the problem to be solved, is a collection of truths about that entity. In theory, the organization of these truths can be such as to facilitate the classification and identification of a problem, which leads to its solving process and eventual solution. Organized knowledge representation and reasoning is discussed in Rich and Feldman [40], although not in a model management context. Knowledge representation and reasoning in another form, now directly applied to management of model libraries, is presented in Mannino et al. [35]. An introduction to knowledge representation concepts is found in Dolk and Konsynski [15]. These three papers are of special interest to this study. All three introduce and use the concept of frames to represent and store knowledge, a concept extensively used in the present study. A frame may be described as a pictorial equivalent of an entity, with slots assigned to attributes of the entity and containing attribute values. Reasoning suggests that attribute matching can be used effectively to identify the picture. Let us return later to the topic of frames.

In response to a problem input to the DSS, the MMS component is expected to generate a model to solve the problem. In this respect, Aggarwal et al. [1] discuss identification and classification for a special model category, and Lee [31] does the same for another category. Banerjee and Basu [3] discuss model type selection in a DSS. There are several other works that deal with the integrated modeling process. Some examples are Dhar and Jarke [13], and Dolk and Kottemann [16].

The similarities between data and models in the process of classification, identification, and retrieval, are used to advantage in Bhargava et al. [5], Gordon and Fry [22], Hong and Vogel [23], etc. In fact, although data and models belong to entirely different generic systems, the process similarities in identification and classification make it possible to use in model management techniques that are well-established in data management. The major extension over data management is that, while data has only one aspect, a model may have many facets of knowledge, and can perhaps be represented and classified in each of these facets. In fact, when any one facet is complete in itself, and also the knowledge characteristics form a good match with the facet, the model may be completely identified. Other facets then serve as a check or a cross-reference to confirm model identification.

Thus, model recognition and retrieval is critically dependent upon model representation. In the literature, much of the work in model representation and recognition has used stored and complete instantiated models and the identification of these models. Various schemes of model representation have been proposed in the literature. A graph-based representation scheme has been proposed by Liang [34]. Graph-based representation has been extended to graph-based modeling constructs by Jones [24,25]. Alternate representation schemes using an object-oriented approach have been proposed by Muhanna [36] and Lenard [33]. Lenard [33] uses a relational database to implement the object-oriented model management system.

It is a hypothesis of this study that a store of instantiated models is inadequate in response to variations caused by new problems. What is necessary here is the build-up of a new model from segments of existing models. Murphy et al. [37,38] have worked on building models from segments in the case of Linear Programming. Further, the approach is rule-based, a methodology directly suited to Linear Programming. A production scheduling problem is characterized by the presence of natural entities, e.g., production facilities, individual products, production periods, inventory, etc. Optimization techniques in production scheduling, i.e., model solvers, typically employ special techniques and special algorithms. Thus, if the selected problem-solving approach for a production scheduling problem is one of model construction, where model construction elements happen to be defined entities of the problem, an excellent choice for the mechanism is an object-oriented model representation used in conjunction with an object and class identification of the problem characteristics.

Object-oriented design concepts are established in software engineering. In the software engineering context, it has been suggested in research and practice literature that knowledge encapsulation present in a set of objects in an object-oriented system, where sub-classes show inheritance of the properties of the main class, is more compact and yet extensive compared to a logic-based system. Higher order logic is required to duplicate the performance of a simple object-oriented system. MMS literature does have much in the way of model construction.

Some examples are Lee et al. [28,30] in the construction of optimization models, Murphy et al. in the construction of linear programming models and Krishnan's [26] logic-based approach to model construction.

Finally, the process of model construction from an abstraction of the problem is an issue in MMS. The four stages in proceeding from an abstract problem description to the final instantiated model is described in Binbasioglu [6]. Associated with this process is the Structured Modeling (SM) concept of Geoffrion [19,20]. Structured Modeling decomposes a decision problem into genera and elements within the genera in a hierarchic way, a system that is at the same time sensitive to natural definitions of entities and objects in the problem, and dependent upon classes and inheritance of class properties as present in the problem description. We do not use the syntax or the semantics of SM in this study. However, the philosophy is closely related.

Lee and Kim [28,30] have proposed a comprehensive conceptual framework called UNIK (UNIfied Knowledge) which captures the optimization models at a semantic level. They also develop a prototype, UNIK-OPT, for knowledge assisted formulation of optimization models. An architecture of Unified Modeling modified from their paper to be appropriate for our work is shown in Fig. 1. This architecture traces all the steps needed to develop and solve a specific optimization model given the problem specification by the user. Lee and Kim [30] also develop a list of seventeen suggested design criteria for a knowledge-assisted modeling system. To reflect these criteria they propose four views of optimization models: Semantic View, Modeling Language View, Mathematical Notational View, and Tabular View.

No single software exists which encompasses the entire Unified Modeling framework nor do such systems satisfy all the design criteria listed in Lee and Kim [30]. In fact, UNIK-OPT adopts the three modeling views of semantic, mathematical notational and tabular view. In addition, other tools have been developed for developing integer programming models (UNIK-IP; Yeom and Lee [43]), constraint satisfaction problems (UNIK-CRSP; Lee and Kwon [29]), optimization and rule-based systems (UNIK-PMA; Lee and Hurst [27]) to encompass a variety of optimization problems. In this paper we propose a system which covers the semantic and modeling language views for the production scheduling domain. The output of this system would be a model formulation in the AMPL modeling language. Further transformation into a mathematical notational view (the traditional algebraic equation format) or a tabular view (an algorithm specific format like MPS or a simplex tableau format) can be done using this package. This paper has a focus on the specific domain of production scheduling. Thus the classification schema is restricted to one class of models. Focus on a specific domain also means that unlike domain independent modeling systems, the proposed system would not require the development of a separate front-end to present user-interfaced screens. The proposed system satisfies the primary design criteria specified in Lee and Kim [30] of representational adequacy, algorithm independence, data independence, knowledge independence. The domain-specific approach adopted in this paper can be looked at as a “building-block method”, i.e., methods can be derived for a series of specific domains and later integrated into a more generalized approach. A separate front-end which performs a primary classification can then be developed for such a generalized system.

![](/api/attachments/4Y2ECGJS/fulltext/images/427e9770e7abddffe6feb200caa8436f26f418a018ea433d4e612ae57f61cecd.jpg)  
Fig. 1. Architecture of unified modeling.

In the rest of the paper, the production problem is first described. The focus is on an Inventory Modeling variation of production scheduling, which is then described. Next, using the inventory model, we show how a problem may be identified as belonging to a certain class of problem, and further classified by attributes of a class to generate an instance. Frames are used to show the sets of attributes that describe an entity, and also how an entity can be described in a multitude of ways. The question is one of matching problem attributes to those of a model. We show how frames are used to effect the matching. The rest of the paper is described as follows. Section 2 gives a description of the characteristics of Scheduling decisions in the Production domains, together with models for lot sizing with inventory considerations. The object-oriented model construction process in the production-scheduling domain is described in Section 3. We discuss two approaches – the top-down and the more realistic bottom-up approach in detail. Templates are used to demonstrate the frames and their interactions in the class hierarchy. We finally conclude the paper and provide directions for further research.

## 2. Production lot-scheduling problems

The objective of automated model construction using defined protocols is based upon a recognition of the model characteristics derived from a mapping of the problem characteristics as described by the user. Thus, the method is most useful for problems having well-defined characteristics (i.e., attributes) and parameters, as well as a natural structure determined by interactions of environmental entities. Such problems lead to structured decision models, and the environmental entities have a substantial impact on the model classification. In the Production Scheduling area, there are a variety of lot-scheduling problems defined by the respective environmental parameters. Some idea of the decomposition and classification of production scheduling problems by their environmental characteristics is given in Fig. 2.

As an automated model construction from a recognition of the problem characteristics would lead to a problem formulation and a solution methodology, it is necessary to consider the types of formulation and solution methodology. In production lot-scheduling applications, there is a variety of both. The problem formulation as well as the solution methodology would vary from one type of problem to another. Thus, for example, the number of facilities, the presence or absence of set-ups, the time pattern, i.e., discrete or continuous, etc., are some factors playing a role in defining the type of the scheduling problem. Some frameworks have been developed based on these environmental parameters to better delineate the different lot-scheduling problems. Below we present a meta-model, i.e., a generalized model describing the knowledge, for the different lot sizing models. In this meta-model,

![](/api/attachments/4Y2ECGJS/fulltext/images/33f583dc88a0a3f0cffb64c33f4f643884e1c6219546adb5dce38e93d2f84ce9.jpg)  
Fig. 2. Taxonomy of production scheduling problems.

N = number of items,

$T =$ length of the planning horizon,

$K =$ number of production resources.

$x_{i}$ 's are production variables and the $I_{i}$ 's are the inventory variables

The first set of constraints in Eq. (1) represents the traditional inventory balance equations. The second set limits the amount of resources used and the third set represents the Bill of Materials relationships between various items.

$$
\begin{array}{l l} \text {Min} \int_ {0} ^ {T} V [ x _ {1} \dots x _ {n} ] (t) + h [ I _ {1} \dots I _ {N} ] (t) \\ \quad + o [ c _ {1} \dots c _ {k} ] (t) d t \\ \text {ST} \\ I _ {i} (t) = I _ {i} (o) + x _ {i} (t) - D _ {i} (t), & i = 1 \dots N, \\ g _ {k} [ x _ {1} \dots x _ {N} ] (t) \leq C _ {k} (t), & k = 1 \dots K, \\ x _ {i} = f _ {i} [ x _ {1} \dots x _ {N} ], & i = 1 \dots N. \end{array}\tag{1}
$$

This formulation encompasses a variety of problems each of whose formulation would be dependent on specific values of the problem parameters mentioned above. In fact, two critical environmental parameters which broadly divide the problems into various categories are:

1. capacitated problem or uncapacitated problem; and

2. “single” problem or “multi-echelon” problem.

Based on these two parameters, Bahl et al. [2] have proposed a framework which captures the essence of the lot-scheduling problem. The four categories of problems are labeled Single Level Unconstrained Resources (SLUR), Single Level Constrained Resources (SLCR) and the associated multiple level problems, viz. MLUR and MLCR. Another important factor which determines the solution methodology for these problems is the nature of demand, i.e., static and dynamic. This also implicitly determines the manner in which time is dealt with. A static demand pattern generally assumes a continuous time model, whereas dynamic demand implies that the time model chosen is discrete time intervals. For example, under the SLUR category, the venerable EOQ model is a static demand model.

A special case of inventory-based lot scheduling models is the Wagner–Whitin model, which is both a dynamic demand model and a discrete time model. The interesting features of Wagner–Whitin are respectively its easily identifiable entities, and its simple solution methodology based upon Network Model systems. A general formulation for the Wagner–Whitin model is presented below.

$$
\begin{array}{l l} \text {Min} \sum_ {t = 1} ^ {T} \big (V _ {t} (y _ {t}) + h _ {t} (I _ {t}) \big) \\ \text {ST} \\ I _ {t - 1} + x _ {t} - d _ {t} = I _ {t}, & \forall t, \\ y _ {t} \leq M \cdot x _ {t}, & \forall t, \\ I _ {0} = 0, \\ x _ {t} > 0, & \forall t, \end{array}\tag{2}
$$

where

$V_{t} =$ set up cost in period $t$

$$
h _ {t} = \text { inventory   holding   cost   in   period } t,
$$

$y_{t}=0/1$ integer variable to indicate a setup in period t.

The Wagner–Whitin model is simple in structure. In a practical application of model identification and model construction, one needs to recognize the logical relevance between demand, production, and inventory; and also to identify the entities of demand, production, and inventory, by periods.

## 3. Model construction process

classes of model types identified prior to setting up the model-base. In an alternate approach, if the objects are selected so as to be closer to the real-world scenario, then a bottom-up approach results. This latter approach is more flexible and extensible as it is characterized by definitions of objects as environmental entities and their class relationships. However, ensuring consistency in the bottom-up approach between various model pieces is an issue that needs to be addressed. We first discuss the top-down approach briefly and then elaborate on the bottom-up approach.

As mentioned earlier, the model building process is interwoven with issues of model representation. We hypothesize an object-oriented modeling system built around the natural entities present in the model. A frame-based representation is suggested to enhance the structure of entities and objects. In a frame-based representation, the knowledge of the model structure and model components are stored in the attribute-slots of the frames. A frame-based approach lends itself very well to defining various problem classes. Inheritance and encapsulation properties of this approach serve in clearly defining the properties of the classes and sub-classes. Distinguishing between problem classes is facilitated with this approach. The model construction process adopted here is similar to that illustrated in Binbasioglu [6].

In Binbasioglu [6], there are two distinct phases in the model building process, viz. the classification phase and the construction phase. The classification phase comprises the steps of abstraction and specialization while the construction phase consists of the aggregation and instantiation steps. Used in conjunction with our frame-based model representation approach, however, some of the steps coalesce into each other. Two approaches can be designated depending on how the objects are identified in setting up an object-oriented approach. If the classification of problem types is done first, and the objects correspond to these specific problem types, then a top-down approach results. A top-down approach is similar to a case-based reasoning approach. This approach is limited in its flexibility in that the types of problems that can be modeled are limited to the

## 3.1. The top-down approach

The model recognition and model construction process begins after the problem characteristics have been elucidated from the decision-making user. The acquisition of problem-related knowledge, i.e., the problem description, could be a narrative or obtained as answers to specific questions. To eliminate issues of language and semantics, let us consider a “multiple choice” format as a selection between predetermined alternate specifications. The next step is to derive an abstraction of the problem. For example, an abstract description for a production problem could be of the form shown below:

Minimize total production cost

subject to

$$
\text { amount   supplied   in   period } t
$$

$> =$ amount demanded in period $t$

resources used in period $t$

$< = \text{resources available in period } t.$

The abstract problem description is used to identify problem classes or model categories. The advantage of a frame-based representation is the ability it gives to directly map the problem description into model categories. In effect, identification of model categories also determines the various model components to be used, as the parameters, variables, and constraint types associated with the model are stored in the attribute-slots belonging to each class of problems. Following the identification of the type of model, the specialized model flows directly. The

objective is to solve the specialized model so generated for a decision. The AMPL system (see Fourier et al. [18]) has been used in this study as a viable modeling and solution mechanism. $^{1}$ As an example of the modeling paradigm, we show the specialized model for the Wagner–Whitin problem in the form of an AMPL program below:

```perl
set PERIODS;    # number of periods in the planning horizon
param demand {PERIODS} >= 0;    # demand in each period
param setup_cost {PERIODS} > 0;    # setup cost/setup
param holding_cost {PERIODS} > 0;    # holding cost/unit
param bigm > 0;
var production {j in PERIODS} >= 0;
var inventory {j in PERIODS} >= 0;
var setup {j in PERIODS} integer >= 0, <= 1;    # 0/1 integer variable to
    # indicate a setup in period .
minimize sum {j in PERIODS} setup_cost[j] * production[j] + sum {j in PERIODS} holding_cost[j] * inventory[j];
subject to inventory[j-1] + production[j] - inventory[j] = demand[j];
    subject to production[j] - bigm * setup[j] <= 0;
subject to inventory[0] = 0;
```

Thus, the top-down approach serves to identify gross problem categories, and possibly retrieve models that serve such category definitions. For example, if a given problem were to be identified as a an inventory-based production problem, and in particular, one that can be solved by the Wagner-Whitin algorithm, the top-down approach could directly retrieve the complete problem from the model-base, adjust the parameters to fit the input of problem characteristics, and arrive at the optimal solution through AMPL, in service to the decision maker. Below we expand on this approach.

Fig. 3 gives the hierarchical class structure for a top-down approach. It is seen that classes such as SLUR, SLCR, etc. result in a certain class of problems with attributes and properties. Thus the SLUR class encompasses all problems which have a single item and are uncapacitated. The information for these slots for the SLUR class is put in by the user. The SLUR class can then select the appropriate objects such as the EOQ model or the Wagner–Whitin model. Thus, for example, the Wagner–Whitin model object would inherit all of the properties of the SLUR class in addition to information about the type of demand – in this case a discrete or dynamic pattern of demand. In a similar fashion, one can have objects within the SLCR class including the ELSP (economic lot-scheduling problem) which includes problems with a static demand pattern, and a variety of problems with a discrete demand pattern, such as the CLSP (capacitated lot-scheduling problem), or CSLP (continuous setup lot-scheduling problem), the DLSP (discrete lot-scheduling problem), etc. These objects contain complete model information pertinent to the semantic view and, as such can output the specialized model in the modeling language of choice – in this case, an AMPL formulation as illustrated before. Specific model instances can also be stored as objects. However the utility of such instantiated models may be limited.

![](/api/attachments/4Y2ECGJS/fulltext/images/243fe321de60818f5dd784913a1ee99bf3319f63cc1b7aa31fb727d1ac536f93.jpg)  
Fig. 3. Model classes and instances - top-down approach.

Thus a top-down approach merely serves as a store of specialized models categorized according to the various classes. The “model-building” process essentially consists of selecting the appropriate specialized model according to the user specification which is stored in the slots for each class. In practice, the reliance of this approach is on past observations, and problems and models already observed and anticipated. The failure to recognize model entities not encountered in the past can be severe. In contrast a bottom-up approach is much more flexible, robust and extendible. The bottom-up approach to model recognition and construction, as presented below, is aimed at combining part-entities derived from natural characteristics of problems and models.

## 3.2. The bottom-up approach

As mentioned earlier, the bottom-up approach is one that relies on intuitive selection of objects from their respective real-world definitions for the purposes of object identification. Thus, in a production scheduling domain, conceptually defined entities such as machines, products, raw materials, etc. are easily identifiable objects. Figs. 4 and 5 show the objects and classes identified with respect to a model, and the relationships between them.

CLASSES AND OBJECTS 1.  
![](/api/attachments/4Y2ECGJS/fulltext/images/5bf4f3910014da2fc820a6f89a1ebd5934d8d45049163df75d98a96fe17ab591.jpg)  
Fig. 4. Representation of classes and objects in a generalization-specialization hierarchy.

In a bottom-up process, the object definition depends to a large extent on the nature of the relationship, and the identification of objects is closely associated with the hierarchy of relationships. Two kinds of relationships are clearly indicated. The first is a Part-Whole relationship, where an object is characterized as a is-a-part-of another object. The second type of relationship is a Generalization-Specialization, where successive objects and classes are specializations of a more general form. The $\cap$ connector in Fig. 4 signifies a generalization-specialization (i.e., is-a-kind-of) hierarchy whereas the connector $\wedge$ connecting the classes in Fig. 5, signifies a part-whole (i.e., is-a-part-of) relationship. For example a Warehouse\_Facility is a kind of Facility whereas an Objective\_Function is a part of a Formulation.

The hierarchic schema results in Class Templates for each object in the hierarchy. The Class Templates so formed indicate also the inheritance of attributes by sub-classes in a hierarchy. Further, the Class Template structure makes it possible to identify and retrieve the lowest level sub-classes by attribute matching in a systematic way from higher order classes. Noting the similarity between a Class Template for a model object, as is important in the present study, and a Data Dictionary entry for a data element which is a well-established mechanism), let us coin the term Model Dictionary for the set of Class Templates of the model.

Shown below are some Class Templates for the Production Scheduling problem (Schemes 1–8). We begin with the highest order object, i.e., a production facility, and proceed to lower order objects such as manufactured items, as well as associated items such as supplier and raw material. Note that the density of the template increases as we proceed down the order, where the attributes are more narrowly defined and the number of attributes increase.

Some comments about the templates help to explain their structure. The third element visibility indicates whether the class is exported, private or imported relative to its enclosing class category. The cardinality of the class captures how many instances are allowed; typically the values of this element are 0, 1, or n. The role that this class plays in the class hierarchy is expressed by the next two elements. A class may have zero, one, or more superclasses and a metaclass as well. The interface of a class provides its outside view and therefore emphasizes the abstraction while hiding its structure and the secrets of its behavior. This interface primarily consists of the declarations of all the operations applicable to instances of this class, but it may also include the declaration of other classes, constants, variables, and exceptions as needed to complete the abstraction. By contrast, the implementation of a class is its inside view, which encompasses the secrets of its behavior. An interface may be public, protected and private. A declaration that forms part of the interface of a class and is visible to all clients that are visible to it, is termed public. If this declaration is visible only to the subclasses, then it is termed protected and if it is visible to no other classes, it is termed private.

![](/api/attachments/4Y2ECGJS/fulltext/images/84dd625ff342e8fff4971a6c44d6e7780955a65e29d3930d0647e512fb90198c.jpg)  
Template 1: Class Template for Facility  
Scheme 1. Class Template for Facility.

The structure of the templates, their classification, and the hierarchy of their classes is designed to facilitate the extraction of problem information from the user and interface with the modeling operators. The semantics of information from the user, and the user's problem-solving motivation, are extremely difficult issues that border on the arena of processing Natural Language, and may well form the subject of future theses. To avoid such issues, and to make the model construction proposition feasible let us focus entirely on information extracted through a question-answer session in a multiple choice format.

On this basis, the result of a single query to the user would result in the selection of an object template. This template would have a number of slots that need to be filled. Further, once these slots are filled by the user information, the Class Template creates sub-classes appropriate to the attribute values entered by the user, a process known as calling the template. Sub-classes in turn create objects. The number of sub-classes is logically consistent with the hierarchic levels in the categorization of objects. Objects have a direct relationship to the algebraic model, which is built up from the parameter descriptions provided by the respective objects.

![](/api/attachments/4Y2ECGJS/fulltext/images/2ccccc158264ed6b7be6073c76577e9608f19156914a60a81854c7f0c9535461.jpg)  
Template 2: Class Template for Manufacturing Facility  
Scheme 2. Class Template for Manufacturing Facility.

As an example of this process, consider the case of a Production Scheduling problem with inventory variables, solved through the use of a Wagner-Whitin algorithm as discussed earlier. From the classification viewpoint, the Facility class has operations which interact with the user and obtain information like the Number and Type of Facilities. Based on the information collected, the Facility Class creates the sub-classes of Warehouse\_Facility, Manufacturing\_Facility, and Supplier\_Facility. The generic parameters like number of facilities are inherited by each of these sub-classes. Each sub-class then creates the appropriate number of objects. Thus, in the Wagner-Whitin example shown in Eq. (2), one would have the Facility class, only a Manufacturing\_Facility class and a single manufacturing facility object.

In a similar manner, the Item class has operations embedded in its implementation, which obtain from the user the number and type of various items including the attributes of End\_Item, Manufactured\_Item, and Raw\_Material\_Item. The Item class then creates the appropriate sub-classes. These sub-classes in turn create the appropriate number of objects for each sub-class. In the class-object hierarchy depicted in Fig. 4, we have assumed that there are various types of End-items. An additional level of detail could be included where the End\_Item class has a further sub-class called End\_Item Category which would correspond to the different product lines manufactured by the firm. Within each category one would finally have the end-item objects. For the Wagner–Whitin problem presented in Eq. (2), one would have an Item class, only an End\_Item class and a single End\_Item object. A similar form of logic would hold for the Resources hierarchy as well. We do not discuss this in detail as the Resources hierarchy does not play a major role in the creation of the model for Eq. (2).

The End\_Item object is the major role player in this example. It is this object that collects all the information pertaining to the item demand, holding and setup costs. At this stage, once all the information needed to create the formulation has been obtained through user queries, the End\_Item object invokes operations which will create the constraint objects corresponding to those in Eq. (2), viz. the inventory-balance and set-up constraints. The knowledge to create these constraints is embedded in the End\_Item class which is inherited by each End\_Item object. The End\_Item object also creates the objective function by asking the Formulation class to create the Objective\_Function object and providing the necessary information. It also creates the sets, parameters, and variables section of the AMPL formulation by creating appropriate objects in the Formulation hierarchy. The Formulation class then collects all the information to generate the completed problem formulation.

![](/api/attachments/4Y2ECGJS/fulltext/images/c599addb9637b08d3883f2225ac2086afdc4807be94a37066247aefb834d724c.jpg)  
Template 3: Class Template for Item  
Scheme 3. Class Template for Item.

The object-oriented approach thus offers a powerful and effective way of representing and manipulating domain knowledge. Features such as object operation and polymorphism can be taken advantage of to provide a flexible and facile way of constructing models.

## 3.2.1. Object operations and encapsulation

The features of encapsulation, inheritance and object operation were briefly illustrated in the foregoing explication. In the simple example discussed above, the End\_Item object was charged with the responsibility of setting up every aspect of the formulation. In more complex problems, other objects would have some role to play. For example, let us assume that there are multiple end-items and a single machine in a single manufacturing facility. The Machine\_Resource item shown in Scheme 8 would then send a message to every end-item object and fetch data on the run-time and set-up time (if existing). This “message” sending is accomplished through object-operations present in its interface. Scheme 8 again shows that operations Get\_Item\_Run\_Time and Get\_Item\_Setup\_Time would be the object operations that would come into play. Once the relevant timing information is obtained from each item, the Machine\_Resource object would create the relevant Constraint object. The object-operation Create\_Capacity\_Constraint would be responsible for creating the constraint as shown below:

![](/api/attachments/4Y2ECGJS/fulltext/images/a7b7c892434e7a2313f461c2ce15b78f1e3d5a328569beb6fb59056ab234620f.jpg)  
Template 4: Class Template for End-Item  
Scheme 4. Class Template for End-Item.

sum {i in PRODUCTS} production[i,j] \* runtime[i]
+ sum {i in PRODUCTS} setup[i,j] \*
settime[i] <= capacity[j].

As can be seen, there is another set here which is the number of end-items, labeled PRODUCTS, in addition to the set called PERIODS in Eq. (2). Note that the object-operation Create\_Capacity\_Constraint is part of the implementation of the Machine\_Resource object, i.e., it is not visible to other clients. On the other hand, both object-operations

Get\_Item\_Run\_Time and Get\_Item\_Setup\_Time are part of its interface. This example illustrates how encapsulation and object-operations work to effectively construct model components.

This example brings out another issue. Whereas in the Wagner–Whitin model, the variable production had a single index j, the same variable has two indices in the above examples of objects and calling sequences to account for a multiple end-item problem. This kind of anomaly can be effectively handled due to the polymorphism feature of object-oriented languages. Special mention is made below of the polymorphism feature and illustrated with an example.

## 3.2.2. Polymorphism

Polymorphism is a concept in Type Theory in which a name may denote objects of many different classes that are related by some common superclass. Thus, any object denoted by this name is able to respond to some common set of operations in differ-

![](/api/attachments/4Y2ECGJS/fulltext/images/b8b9f8ba905b55b16e8e36ad097fb96367ea21a529adbcc0ef4c6faddf4e98b1.jpg)  
Template 5: Class Template for Manufactured Item  
Scheme 5. Class Template for Manufactured Item.

![](/api/attachments/4Y2ECGJS/fulltext/images/4f8b9b86b33dc8baeedc33166a2e94414518884730eb0de35942b8f090695e76.jpg)  
Template 6: Class Template for Raw Material Item  
Scheme 6. Class Template for Raw Material Item.

ent ways. Thus, for example, an object Raw\_Material\_Item in Scheme 6 would respond to an operation, Create\_RM\_Requirement\_Constraint, in different ways depending on the problem characteristics. Without polymorphism, the developer has to develop programs consisting of large case or switch statements, i.e., with polymorphism, large case statements are unnecessary, because each object implicitly knows its own type.

Let's assume that the problem being tackled was a purchasing problem which ensures that each raw material procured from various sources should meet the requirement of such material. This constraint would appear as follows:

subject to
sum{m in SUPPLIERS} RM\_Item[k,m,j]
> = requirement[k,j].

This constraint would be created by the Raw\_Material\_Item object, where SUPPLIERS is a set, the quantity RM\_Item[k,m,j] is a variable indicating amount of raw-material k procured from supplier m in period j, and the requirement[k,j] is a parameter indicating the requirement of raw material k in period j.

Let us now assume that one would like to solve a joint scheduling and purchasing problem, i.e., there are multiple end-items which need to be scheduled on a single machine in a single manufacturing facility. $^{2}$ Each of these end-items require different kinds of raw materials. The above constraint, which assumes that requirement is a parameter, no longer holds true in this situation. The raw material requirement is a derived element depending on the number of units of various raw materials needed for each end item. Thus, the above constraint would morph to:

```prolog
subject to
sum {m in SUPPLIERS} RM_Item[k,m,j]
- sum {i in PRODUCTS} RM_Multiple[i,k] *
production[i,j] >= 0.
```

This constraint would also be created by the Raw\_Material\_Item object. In the above constraint, SUPPLIERS and PRODUCTS are sets, RM\_Item is a variable as above, RM\_Multiple[i,k] is the units of raw material k required per unit of end-item i and production[i,j] is the amount of end-item i produced in period j.

In working with objects and templates, the apparent anomaly that seemed to surface was the fact that the same object, e.g., Raw\_Material\_Item, would need to change the way it formulates constraints depending on problem characteristics. Thus, if the problem includes raw materials as well as end-items, as opposed to containing only raw materials, the Raw\_Material\_Item object would create different versions of the same constraint. As mentioned earlier, maintaining consistency among constraints becomes an issue when one uses a bottom-up approach to create the variables, constraints, and objective function as an integration of pieces or segments. It should be noted in this context, that the strength of the bottom-up approach lies in its capacity to create composite and complex models without being hampered to a great extent by previous knowledge of specific types of models. Thus the operations and/or methods which are invoked have to necessarily embody this flexibility. The polymorphism feature of most object-oriented programming languages can be exploited in this instance as was portrayed above.

![](/api/attachments/4Y2ECGJS/fulltext/images/3f0994a3c84c4c61d1323466b338839c280813c9ffa3bd6b7d58a609c2db4d2d.jpg)  
Template 7: Class Template for Supplier  
Scheme 7. Class Template for Supplier.

It was mentioned that the bottom-up model formulation approach is superior to the top-down approach. Nevertheless, the top-down approach does offer the advantage that, given a problem specification by the user, a complete model can be speedily selected from the store of existing models. Thus a system which integrates and includes elements of both the top-down and the bottom-up approach may be of increased value.

The primary user interface in such a system will still be controlled by the classes and objects defined in the bottom-up approach. Once the user input is complete however the Problem\_Definition class will query all the objects such as Item, Facility, Resources and obtain information about the problem characteristics in terms of problem attributes. Thus the Problem\_Definition class essentially acts a repository of all problem attributes. Based on these attributes the Problem\_Definition class would call the appropriate sub-class such as the SLUR class,

SLCR class, etc. The specific sub-class called will in turn, select the specialized model which satisfies the user-specifications provided such a model instance exists in the model library. The user will also be able to access a specific instantiated model if so desired. In the absence of such a model (specialized or instantiated), control reverts to the classes defined in the bottom-up approach which proceed with the piece-meal building of the model from scratch.

The integration of the two approaches results in a specialized model being either selected from the stored model library, or constructed from the model formulation knowledge residing in each of the classes. In addition such an integration will also permit updating and maintenance of the stored model-base. Thus, if a model has been constructed from the scratch using the bottom-up process, then this specialized model can be stored in the model-base under the appropriate class or under the Miscellaneous class if the constructed model does not fit into

![](/api/attachments/4Y2ECGJS/fulltext/images/f67574a6ef47d305520b37ccf70c059fd83bb08a41606e22ebeb1f945bf4249b.jpg)  
Template 8: Class Template for Machine Resource

Scheme 8. Class Template for Machine Resource.

![](/api/attachments/4Y2ECGJS/fulltext/images/14b277780c02f08b32db50dbba2ebb7bc102e765d6ab2eed3dc15adedf22b61a.jpg)  
Fig. 5. Representation of classes and objects in a part-whole hierarchy.

any of the pre-defined classes. This process obviates the need for building this model from ground-up if future usage is anticipated.

## 4. Conclusion and future directions

This study has been intended as a first step in the automated construction of models to solve problems that commonly arise in industry practice. Production Scheduling is a typical domain where structured models are found and used to advantage. Inventory-based models, such as the one used in this study, are even more typical of the problems found in practice. The importance of this problem is such that the algebraic model structure and its solution algorithms are well-established. Even the modeling structures have been incorporated in modeling software as used in this study, e.g., AMPL. The issue is no longer model solving once the model has been established, but rather, the construction of the model from the raw data concerning the problem.

Considering the end-user of the model, faced with a practical problem and a very large number of modeling choices, the difficulty in decision making arises from the aspects of model construction. From the perspective of the practical decision maker, the difficulty still exists in translating the problem characteristics of the given problem to the attributes of a model. This study specifically performs the task of developing mechanisms to extract problem knowledge, as elicited in a question-answer session, and convert the same to modeling constructs. The contribution to automated modeling lies also in the use of natural objects in the knowledge scenario. Systems design of the modeling process constructs a Model Dictionary, somewhat similar to the much used Data Dictionary, consisting of templates describing object attributes; object classes, and inheritance of class properties. The templates so formed become a part of the modeling system. Modeling a specific application problem consists of “calling” attributes through templates. Model characteristics are transparent to the user, who is free to concentrate on the problem and its model solution for decision making purposes.

Further, the emphasis is on constructing a model from its components, rather than on recognizing instances of models from past experience. Thus, a model for a specific application may be constructed automatically following an input of attributes by the user, through the mechanism of calling object templates. The result is a solvable model, dynamically constructed to suit a specific problem instance. The advantages are apparent in that the user is relieved from the need to acquire and employ technical modeling expertise, and secondly, that it becomes possible to apply problem-solving techniques to a wide variety of problems, often with characteristics that vary rapidly. The modeling system makes it feasible to solve varying problems in real time.

It should be pointed out that the present study addresses only the issue of the conceptual design of a problem-solving model construction system for some production scheduling problems. While conceptual design is the critical stage of the System Development Life Cycle (SDLC), the logical next stage of the SDLC is the actual system design and development, without which there is no implementation. Further, limitations of space restricts this paper to the consideration and explanation of only one model, viz. the Wagner–Whitin model. The modeling mechanism is generalizable to several classes of production scheduling problems. For completeness, the model construction techniques presented above can be, and should be, applied to a variety of other problem types and model types. Considering the building-block construct of model management, all such model construction techniques can then be integrated in a single model management mechanism with a classifier as a front-end, or interface to the user. The contribution to decision support would be enormous.

## References

[1] A.K. Aggarwal, E.R. Clayton, T.R. Rakes and J.R. Baker, A Problem Identification Taxonomy For Classification and Automated Formulation of Linear Programming Models, Annals of Operations Research 38, No. 1–4 (1992) 1–16.

[2] H.C. Bahl, L.P. Ritzman and J.N.D. Gupta, Determining Lot Sizes and Resource Requirements: A Review, Operations Research 35, No. 3 (1987) 329–345.

[3] S. Banerjee and A. Basu, Model Type Selection in an Integrated DSS Environment, Decision Support Systems 9, No. 1 (1993) 75–89.

[4] A. Bharadwaj, J. Choobineh, A. Lo and B. Shetty, Model Management Systems: A Survey, Annals of Operations Research 38, No. 1–4 (1992) 17–68.

[5] H.K. Bhargava, R. Krishnan and S. Mukherjee, On the Integration of Data and Mathematical Modeling Languages, Annals of Operations Research 38, No. 1–4 (1992) 69–97.

[6] M. Binbasioglu, Key Features for Model Building Decision Support Systems, European Journal of Operational Research 82 (1995) 422–437.

[7] M. Binbasioglu, Process-Based Reconstructive Approach to Model Building, Decision Support Systems 12, No. 2 (1994) 97–113.

[8] G. Booch, Object Oriented Design with Applications, (Benjamin/Cummings Publishing Co., Inc., Redwood City, California, 1991).

[9] A.K. Chakravarty and D. Sinha, Knowledge Modularization for Adaptive Decision Modeling, ORSA Journal on Computing 2, No. 4 (1990) 312–324.

[10] Ai-Mei Chang, C.W. Holsapple and A.B. Whinston, Model Management Issues and Directions, Decision Support Systems 9, No. 1 (1993) 19–37.

[11] Q.B. Chung and R.M. O'Keefe, A Formal Analysis of the Model Management Literature, Annals of Operations Research 38, No. 1-4 (1992) 137-176.

[12] P. D'Alessandro, M. Dalla Mora and E. De Santis, Issues in Design and Architecture of Advanced Dynamic Model Management for Decision Support Systems, Decision Support Systems 5, No. 4 (1989) 365–377.

[13] V. Dhar and M. Jarke, On Modeling Processes, Decision Support Systems 9, No. 1 (1993) 39–49.

[14] A. Di Nola, S. Sessa and W. Pedrycz, Fuzzy Information in Knowledge Representation and Processing for Frame-Based Structures, IEEE Transactions on Systems, Man, and Cybernetics 24, No. 6 (1994) 918–925.

[15] D. Dolk and B.R. Konsynski, Knowledge Representation for Model Management Systems, IEEE Transactions on Software Engineering SE-10, No. 6 (1984) 619–628.

[16] D. Dolk and J.E. Kottemann, Model Integration and a Theory of Models, Decision Support Systems 9, No. 1 (1993) 51–63.

[17] B.L. Dos Santos and M.L. Bariff, A Study of User Interface Aids for Model-Oriented Decision Support Systems, Management Science 34, No. 4 (1988) 461–468.

[18] R. Fourer, D.M. Gay and B.W. Kernighan, AMPL: A Modeling Language For Mathematical Programming (The Scientific Press, San Francisco, CA, 1993).

[19] A.M. Geoffrion, Introduction to Structured Modeling, Management Science 33, No. 5 (1987) 547–588.

[20] A.M. Geoffrion, The Formal Aspects of Structured Modeling, Operations Research 37, No. 1 (1989) 30–51.

[21] N. Ghiaseddin, K. Matta and D. Sinha, A Structured Expert System For Model Management in Inventory Control, ORSA Journal on Computing 6, No. 4 (1994) 409–422.

[22] M.D. Gordon and J.P. Fry, Novel Applications of Information Retrieval to the Storage and Management of Computer Models, Information Processing and Management 25, No. 6 (1989) 629–646.

[23] I.B. Hong and D.R. Vogel, Data and Model Management in a Generalized MCDM-DSS, Decision Sciences 22, No. 1 (1991) 1–25.

[24] C. Jones, Attributed Graphs, Graph-Grammars and Structured Modeling, Annals of Operations Research 38, No. 1–4 (1992) 281–324.

[25] C.V. Jones, An Introduction to Graph-Based Modeling Systems, Part I: Overview, ORSA Journal on Computing 2, No. 2 (1990) 136–151.

[26] R. Krishnan, Automated Model Construction: A Logic Based Approach, Annals of Operations Research 21 (1989) 195-226.

[27] J.K. Lee and E.G. Hurst, Jr., Multiple Criteria Decision Making including Qualitative Factors: The Post-Model Analysis Approach, Decision Sciences 19, No. 2 (1988) 334–352.

[28] J.K. Lee, C.C. Seok and M.Y. Kim, A Knowledge-Based Formulation of Linear Programming Models Using UNIT-OPT, Expert Systems in Economics, Banking and Management (Elsevier Science Publishers, North Holland, 1989) 447–455.

[29] J.K. Lee and S.B. Kwon, ES\*: An Expert Systems Development Planner Using a Constraint and Rule-Based Approach, Expert Systems with Applications 9, No. 1 (1995) 3–14.

[30] J.K. Lee and M.Y. Kim, Knowledge-Assisted Optimization Model Formulation: UNIK-OPT, Decision Support Systems 13 (1995) 111–132

[31] J.S. Lee, A Model Base for Identifying Mathematical Programming Structures, Decision Support Systems 7, No. 2 (1991) 99–105.

[32] J.S. Lee, M. Guignard and C.V. Jones, Variations in Model Formulations, Annals of Operations Research 38, No. 1–4 (1992) 325–358.

[33] M.L. Lenard, An Object-Oriented Approach to Model Management, Decision Support Systems 9, No. 1 (1993) 67–73.

[34] T.-P. Liang, Development of Knowledge-Based Model Management System, Operations Research 36, No. 6 (1988) 849–863.

[35] M.V. Mannino, B.S. Greenberg and S.N. Hong, Model Libraries: Knowledge Representation and Reasoning, ORSA Journal on Computing 2, No. 3 (1990) 287–301.

[36] W.A. Muhanna, An Object-Oriented Framework for Model Management and DSS Development, Decision Support Systems 9, No. 2 (1993) 217–229.

[37] F.H. Murphy, E.A. Stohr and A. Asthana, Representation Schemes for Linear Programming Models, Management Science 38, No. 7 (1992) 964–991.

[38] F.H. Murphy, E.A. Stohr and P.-C. Ma, Composition Rules for Building Linear Programming Models from Component Models, Management Science 38, No. 7 (1992) 948–963.

[39] W.D. Potter, T.A. Byrd, J.A. Miller and K.J. Kochut, Extending Decision Support Systems: The Integration of Data, Knowledge and Model Management, Annals of Operations Research 38, No. 1–4 (1992) 501–529.

[40] C. Rich and Y.A. Feldman, Seven Layers of Knowledge Representation and Reasoning in Support of Software Development, IEEE Transaction on Software Engineering 18, No. 2 (1992) 451–469.

[41] R. Santhanam and M.J. Schniederjans, A Model Formulation System for Information System Project Selection, Computers and Operations Research 20, No. 7 (1993) 755–767.

[42] M.J. Shaw, P.-L. Tu and P. De, Applying Machine Learning to Model Management in Decision Support Systems, Decision Support Systems 4 (1988) 285–305.

[43] K. Yeom and J.K. Lee, Knowledge-Assisted Optimization Modeling for Integer Programming Problem: UNIK-IP (forthcoming in Decision Support Systems, 1994).

![](/api/attachments/4Y2ECGJS/fulltext/images/4c1be2898d070da5e741a14ac6962c0faf053b69d98d1fa5762363a4a3fa1564.jpg)  
Sharma Pillutla teaches Information Systems and Operations Management Courses. His current research interest are in the areas of model management and production scheduling.

![](/api/attachments/4Y2ECGJS/fulltext/images/995824921d22902e259e83f029827af265af54e81db8da8eefe6bd2a0a7adfa7.jpg)

Barin N. Nag is an Associate Professor in the Management Department at Towson State University. He has a Ph.D. From the University of Maryland, and prior Electrical Engineering degrees. His research interests lie in Model Management, Idea Managemeny, Neural Networks, and AI methods in Decision Making and Scheduling. He has over 40 publications including European Journal of Operational Research, Decision Sciences, Annals of Operations Re

search, and Expert Systems with Applications. He is a member of INFORMS and IEEE, and has served as Chair of the AI Section of ORSA.

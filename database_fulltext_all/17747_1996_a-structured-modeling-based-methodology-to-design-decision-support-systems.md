---
otero_id: 17747
otero_key: "DY94VPTE"
title: "A structured modeling based methodology to design decision support systems"
authors: "S. Raghunathan"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(96)00006-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A structured modeling based methodology to design decision support systems

S. Raghunathan $^{1}$

Department of Accounting and MIS, Bowling Green State University, Bowling Green, OH 4340, USA

## Abstract

Many Decision Support Systems (DSS) support the decision making process through the use of mathematical models and data. DSS design involves modeling data as well as mathematical relationships in a domain. The process of model formulation and subsequent integration of model with data in a DSS is a complex and ill-structured process. This paper proposes a methodology based on Structured Modeling (SM), originally introduced by Geoffrion together with the modeling language SML, to model and design the DSS. The methodology includes rigorous and step by step procedures to design and integrate data and modelbases. The main contribution of our approach lies in the integration of research in database design, and mathematical model formulation within the structured modeling framework. The resultant procedures can be easily automated and taught to students in DSS courses. The motivation for our research stemmed from our constant frustrations in teaching DSS courses over the last five years. In the last two years, when we used our methodology, the performance of the students improved significantly. The average score in the DSS project went up to 85 from 60. Our positive experience in using our methodology in classes over the past two years suggests that the methodology imposes structure into the analysis of decision problems, and as a result students produce better DSS designs for classroom cases.

Keywords: DSS design; Modeling; Structured modeling; Systems development; Design methodologies

## 1. Introduction

Many Decision Support Systems (DSS) support the decision making process through the use of mathematical models and data. DSS design involves modeling data as well as mathematical relationships in a domain. The DSS design process is complex and ill-structured. Systems design methodologies, such as structured systems analysis and design, and tools, such as the Computer Aided Software Engineering (CASE) tools, are useful primarily in the design of Transaction Processing Systems (TPS) and Management Information Systems (MIS), whose function is to store and retrieve data efficiently. Even though some elements of these methodologies are used in DSS design, the DSS design process remains essentially ad hoc. The lack of a structured DSS design methodology inhibits the development and widespread use of well designed DSS. The complexity of the DSS design process is the result of the need to model not only the problem data and processes, which TPS and MIS design methodologies also include, but also the mathematical relationships, the integration of data and models, and the decision making style of the decision maker. It is well known that the risk-taking nature of the decision maker affects the model that will be used to support the decision making process [9,10]. This paper proposes the use of the Structured Modeling (SM) framework, originally introduced by Geoffrion [7] together with the modeling language SML [7], with enhancements, as an integrative methodology to design DSS.

Unlike other proposed DSS design approaches, such as prototyping $[1,11]$ and others $[3,16]$ , our approach includes rigorous and step by step procedures to design and integrate data and modelbases. The key benefits of such a detailed methodology are that the application of the methodology results in well designed DSS, and the methodology is amenable to automation. The drawback is that the use of the methodology is limited to certain classes of problems. Specifically, our methodology, in its present form, is capable of handling only situations where quantifiable goals exist, all the data are known with or without uncertainty, and the decision maker's preferences are known. In summary, the methodology can handle only situations where mathematical models can be used for decision support. Decision making situations that involve the use of qualitative analysis are beyond the scope of the methodology.

The methodology is a result of our continuing efforts in developing rigorous modeling and design methods that can be taught to students in a DSS course. Unlike databases, for which entity-relationship (ER) modeling [4] has become a standard teaching as well as practitioners' tool, DSS lack a methodology that can be reliably used as a design tool. We believe that our methodology fills that gap. Our experience in using the SM methodology in DSS courses over the past two years suggests that the methodology has the potential to become a successful teaching tool in DSS courses. We observed that the SM methodology imposes structure into the analysis of the problems, and hence students design "better" DSS for classroom cases.

The rest of the paper has the following structure. In Section 2, we summarize the basics of structured modeling including a simple example. We discuss the database design procedure in Section 3. In Section 4, we describe the modelbase design procedure. Then, in Section 5, we discuss the design of modelbase/database integration procedure. In Section 6, we discuss how DSS can be designed for specific problem situations using the database and modelbase. Then, in Section 7, we discuss some of the strengths and weaknesses of the methodology, and directions of future research in this area. Finally, we conclude with a summary in Section 8.

## 2. Structured modeling: Background

Our DSS design methodology consists of several phases, each phase supported by tools, specific procedures, and guidelines, as shown in Fig. 1. The DSS design process begins with an analysis and modeling of the problem domain. We model the domain rather than just a specific problem because the resultant design can then be used to implement DSS for a variety of specific problem situations that occur in the domain. Structured modeling is the tool used in this phase. Then, the structured model representation of the domain is transformed into a database and a modelbase design. Specific procedures enable this transformation process. The integration mechanism by which a model obtains the relevant data from the database is designed in the next phase. A specific procedure enables the design of this mechanism. The database, the modelbase, and the integration mechanism are then used, in conjunction with specific problem and decision maker characteristics, to identify the part of the database and modelbase needed to support decision making in those contexts. The model's type and solvers are also identified in this phase. Our methodology doesn't provide much insight into the identification of the specific model type and its solvers. The DSS design that integrates the identified model, its data, and the solver is then implemented using DSS generators, programming languages, and other tools. We begin our description of the methodology by reviewing structured models.

![](/api/attachments/DY94VPTE/fulltext/images/347f63de4bc2c39e5cbe7934a3403da5359fe7b3db93c95bfa64174a60cf3cb8.jpg)  
Fig. 1. DSS design methodology.

Our methodology uses Geoffrion's structured modeling language as a tool in one of the phases, viz., domain analysis and modeling. We use a diagrammatic representation of the model that is similar to the ER model, so that designers already familiar with ER modeling concepts can extend the same concepts to the structured modeling framework. We have also added some features of ER modeling, such as cardinalities of relationships, to the structured modeling framework so that existing database design procedures can be used in our methodology. Another difference between our representation and Geoffrion's representation of a structured model is that we allow uncertain data to be represented as probability distributions in the model. Hence, our methodology should be viewed as a collection of procedures that use Geoffrions's structured model adapted for our proposes.

Structured modeling methodology attempts to model data and relationships among data in a domain. It includes all the elements of the ER modeling methodology because DSS design includes the design of a database. However, SM has additional elements to model the modelbase, and to facilitate the integration of data and modelbases in a single system. We use the following example problem to illustrate our methodology.

XYZ manufacturing company operates several production plants. Each plant produces several items. An item is produced by many plants. The items are transported to warehouses near customer sites. The shipments to a warehouse can come from several plants and a plant can ship to several warehouses. Each plant has a production capacity to produce an item. Each warehouse has a specific demand for an item. The unit production cost for a product is the same in all plants. However, the unit shipping cost for a product varies depending on the plant and the warehouse. The manufacturer is interested in an appropriate shipping schedule that will minimize the total shipping cost.

The demand should be met; the entire production of an item is shipped out to warehouses. Also note that capacity refers to the maximum amount of an item that can be produced. The manufacturer cannot ship more than what is produced. The demand, production capacity, unit production cost, unit shipping cost are assumed to be known. The shipping schedule includes the amount of each item that needs to be produced in each of the plants, and the amount of each item that needs to be shipped to each warehouse.

Structured modeling views a model as being composed of discrete elements. Each element has a definition in which the element's existence is either postulated as a primitive of the model, or postulated in terms of other elements whose definitions have already been given. We represent each element by a symbol, and the entire model as a diagram, along with documentation, even though other representations, such as textual, are certainly possible. There are five types of elements.

(1) Entity: An entity element has no value and generally represents identifiable things or concepts postulated as primitives of the model. For instance, in the example problem, products may be modeled as entities. An entity has a name and a definition that describes what the entity represents. The definition serves as a documentation tool. An entity is represented by a rectangular box in the model. An entity can be viewed at two levels. An entity class represents a collection of similar entities whereas an entity instance represents a specific entity within the collection. For instance, product that models all the products manufactured is an entity class, and a 6-inch bolt is a product instance. We assume without loss of generality that only entity classes are represented in SM because an entity instance can be represented, if needed, as a class with one instance.

(2) Attribute: An attribute element has a single value and represents a characteristic or property of an entity $^{2}$ . An attribute has a name and a definition that describes what the attribute represents. For instance, a product is generally characterized by a product name. Hence, product-name can be modeled as an attribute of product. An attribute of an entity instance has a single value. For instance, assume that unit-price is modeled as an attribute of the entity product. It means that, a product instance, such as 6-inch bolt, has a single value, such as \$5.00 for unit-price. We distinguish known and unknown attributes by including the letter K or U, respectively, in parenthesis, beside the name of the attribute. Even though many attributes will have precise values, we allow probability distributions such as $N(0,1)$ which denotes a standard normal distribution of attribute values.

(3) Relationship: A relationship element (called compound entity by Geoffrion) represents an association among two or more entities. A relationship has a name and a definition that describes what the relationship represents. Relationship elements are defined in terms of entities. For instance, the manufacturing of products in production plants can be represented as a relationship between the entities product and plant. Here, the need for representing the manufacturing activity as a relationship stems from the fact that the manufacturing activity itself cannot be adequately described unless the activity relates to what is produced (product) and where it is produced (plant). Relationships may involve more than two entities. For instance, the transportation of a product from a plant to a warehouse may be modeled as a relationship among the entities product, warehouse, and plant. A relationship is represented as a diamond that connects all the entities that are part of the relationship. A relationship may also have attributes that characterize it. For instance, in the example, production capacity may be modeled as an attribute of the relationship between product and plant. Two aspects of relationships are useful in designing the DSS. The number of entities that are part of a relationship is called its degree. The degree can be any natural number greater than or equal to 1. A relationship of degree 1 is called a unary or a recursive relationship. A relationship of degree 2 is called a binary relationship, and so on. A relationship has a maximum and minimum cardinality. The maximum cardinality of a binary relationship refers to the maximum number of instances of an entity that can be related to one instance of another entity $^{3}$ . In a binary relationship, the maximum cardinality has two parts, each of which can be a 1 or M(any). For instance, in the case of manufacturing that relates product and plant, if a product instance is manufactured in only one plant instance, and a plant instance manufactures just one product instance, then the relationship has a maximum cardinality of 1–1. The maximum cardinality is indicated within the diamond. The minimum cardinality of a binary relationship refers to the minimum number of instances of an entity that should be related to one instance of another entity. Each part in the minimum cardinality can be a 0 or 1. The minimum cardinality is indicated on the lines that connect the relationship with the entities.

(4) Function: A function element has a value that is dependent according to a definite rule on the values of attributes that are part of the rule, and generally represents a calculable property and more complex aspects of models. A function has a name, a rule, and a definition that describes the function. For instance, assume that a modeler needs to represent the revenue generated by each of the products. Thus, a function called revenue = unit-price \* quantity-sold can be defined where unit-price and quantity-sold are attributes. However, note that the function revenue as defined above represents a calculable attribute of product. That is, each product instance has a value for revenue which is dependent upon the values of unit-price and quantity-sold of that instance.

In many cases, a function need not be an attribute of an entity/relationship even though the function has a value. For instance, consider total revenue which is defined as the total revenue generated by selling all the products. Here total-revenue can be defined as a function with the rule $\Sigma_{product}$ revenue where revenue is an attribute/function defined earlier. However, total-revenue is not an attribute of any entity.

(5) Constraint: Constraints represent restrictions on the values of attributes and functions (here we specialize Geoffrion's notion of a "test" element). A constraint may include constants, other elements of the model, relational operators such as $< , <=$ , and $=$ , logical operators such as AND, OR, and others. Unlike functions, constraints cannot be attributes of any entity. A constraint specifies the restriction, and a definition that describes the constraint. It is represented by a hexagon which is connected to all the model elements that are part of the restriction. For instance, a simple constraint such as the quantity sold of a product cannot exceed 1000 can be represented by a constraint with the restriction quantity-sold $< = 1000$ .

![](/api/attachments/DY94VPTE/fulltext/images/4d386ec40bbce93613265c37e0aa62880fa3f0c843d3ed13e689ef6da49b6f04.jpg)  
Fig. 2. A structured model for the example problem.

The model that consists of the above five elements $^{4}$ is called the structured model of the problem, which describes the problem domain in a detailed fashion. Depending on the need, there are ways of abstracting the detailed model into higher levels just like a data flow diagram which can be represented at different levels. A structured model (without the documentation) for the example problem is shown in Fig. 2.

Our structured modeling-based approach attempts to model the data associated with a problem domain. The decomposition of the data into the above five elements makes it easier for the DSS designer to analyze the individual elements without being overwhelmed by the details. The same domain can certainly be modeled in more than one way. As one would expect from any methodology that facilitates analysis, even the structured modeling approach cannot guarantee that the resultant model contains the complete, and relevant set of data needed to design the DSS. However, there are simple guidelines and heuristics that can be used to verify whether the structured model is ill-formed in some respects $[12]$ . Some of these guidelines are as follows:

(a) An element can be defined only if it is a primitive element, or it is defined in terms of other elements that are already defined. This means that an attribute cannot be defined unless the entity to which the attribute is associated is already defined. A relationship cannot be defined unless the entities that are part of the relationship are already defined. A function cannot be defined unless the attributes and other functions that are part of the function rule are already defined. A constraint cannot be defined unless the attributes and the entities that are part of the constraint are already defined.

(b) If an attribute is not part of any function rule or constraint, then the attribute doesn't play any role in the mathematical model that provides the decision support. The rationale underlying this guideline is that the modelbase includes functions and constraints defined in terms of variables, and an attribute that is not part of any function or constraint will not be part of the modelbase. This situation implies that either the model is incomplete, or that the attribute is used for storing data that is used for other types of decision support, such as data retrieval.

(c) The entity sets upon which the left hand side and the right hand side of a function depend should be identical. The rationale for this guideline is that when functions are used to calculate data, it is imperative that both sides refer to the same data. If the left hand side of the function is an attribute of product, and the function rule calculates the value of an attribute of resource, then the function is invalid. Additional guidelines based on dimensional information can also be used for the correct formulation of the structured model [2].

Once the structured model is developed, it can be transformed, using fairly simple procedures, into a database design and a mathematical modelbase to be used in a DSS. We will discuss these procedures in the next sections.

## 3. Database design using structured models

One of the benefits of using the structured modeling approach is that the database and modelbase to be used in a DSS can be designed and integrated using the same structured model. The procedures for transforming the structured model into database and modelbase designs are straightforward. If the structured model is correct, then the application of these procedures will result in well designed data and modelbases. The database design procedure is identical to the procedure for transforming an ER model into a database design. This procedure is discussed elaborately in database management texts such as $[8]$ .

A database design is usually expressed as a relational model. A relational model representation of the database structure consists of a set of relations. A relation has a name, and consists of a set of attributes, a subset of which is identified as its key. Relations are linked through the use of common attributes known as foreign keys.

The following procedure transforms a structured model into a database design. Given: A structured model consisting of entities, attributes, relationships, functions, and constraints Produce: A well designed relational model Method: Entity: Transform into a relation. The name of the entity becomes the name of the relation. Attribute of entity, whose value is known: Transform into attributes of the relation. If X is an attribute of entity E, then X becomes an attribute of relation E in the relational model. Relationship: The procedure depends on the type of relationship, whether it has attributes of its own, and the maximum cardinality.

Case 1: The relationship does not have any known attributes of its own.

Case 1.1: The relationship is a binary relationship

Case 1.1.1: The maximum cardinality is 1-1

Put the key of the relation corresponding to one of the entities as an attribute in the relation corresponding to the second entity in the relationship.

Case 1.1.2: The maximum cardinality is $1 - M$ (or $M - 1$ ) Put the key of the relation corresponding to the 1-part of the relationship as an attribute in the relation corresponding to the M-part of the relationship.

Case 1.1.3: The maximum cardinality is $M - N$ Create another relation that consists of the keys of the relations corresponding to the entities in the relationship as its attributes.

Case 1.2: The relationship is a recursive relationship

Case 1.2.1: The maximum cardinality is 1-1 or 1-M
Add the key of the relation corresponding to the entity as another attribute in the relation. Since a relation cannot have two attributes with the same name, change the name of the added attribute.

Case 1.2.2: The maximum cardinality is $M - N$

Create a relation that consists of the key, and the key with a different name as done in the previous case.

Case 1.3: All other types of relationships

Create a relation that consists of the keys of relations corresponding to the entities in the relationship.

Case 2: The relationship has its own known attributes.

Create a relation that consists of the keys of relations corresponding to the entities in the relationship, and the attributes of the relationship.

Applying the above procedure to the structured model shown in Fig. 1 results in the following database design (keys are underlined).

PLANT ( plant#, plant\_location)

ITEM (item#, unit\_production\_cost)

WAREHOUSE (warehouse#, war\_location)

PLANT\_ITEM (plant#, item#, prod\_capacity)

WAREHOUSE\_ITEM (warehouse#, item#, demand)

PLANT\_ITEM\_WARE (plant#, item#, warehouse#, unit\_shipping\_cost)

We include only the known attributes in the database design procedure because only they can be stored in the database. The procedure uses only the maximum cardinality of the relationships. The minimum cardinalities do not play any role in the database structure design. However, they are important in the design of database maintenance procedures $[8]$ . The discussion of these procedures are not directly relevant to this paper. We should note that the above database design can be implemented using a relational, network, or hierarchical database management system in a DSS.

## 4. Modelbase design using structured models

A mathematical model consists of elements such as variables, functions, and constraints. A mathematical model is often represented using subscripts, also referred to as indices. Each index has an associated index set. We use capital letters to indicate variables, and small letters to indicate indices.

The following procedure transforms a structured model into a mathematical model.

Given: A structured model consisting of entities, attributes, relationships, functions, and constraints.

Produce: A mathematical model consisting of variables, indices, index sets, functions, and constraints.

## Method:

1. Assign an index for each entity in the structured model. The index set for each index is the set of instances of the entity.

2. Assign a variable for each attribute and function in the structured model.

3. The index for a variable is

the index assigned for the entity, if the attribute corresponding to the variable is an attribute of an entity

the indices assigned for all the entities that are part of the relationship, if the attribute corresponding to the variable is an attribute of a relationship.

4. Transform each function in the structured model into a mathematical representation by substituting the corresponding variables (along with their indices) for attributes and functions mentioned in the right hand side of the function.

5. Transform each constraint using a procedure similar to step 4.

6. The collection of variables, their index sets, functions, and constraints is the mathematical model for the structured model.

The application of the modelbase design procedure to the structured model shown in Fig. 1 results in the following mathematical model.

INDICES

<table><tr><td>Index</td><td>Index set</td></tr><tr><td>i</td><td>PLANT</td></tr><tr><td>j</td><td>ITEM</td></tr><tr><td>k</td><td>WAREHOUSE</td></tr></table>

VARIABLES

<table><tr><td>Variable Name</td><td>Attribute/Function</td><td>Index</td></tr><tr><td>C</td><td>Prod_Capacity</td><td>ij</td></tr><tr><td>Q</td><td>Prod_Quantity</td><td>ij</td></tr><tr><td>U</td><td>Unit_Production_cost</td><td>j</td></tr><tr><td>S</td><td>Unit_Shipping_cost</td><td>ijk</td></tr><tr><td>D</td><td>Demand</td><td>jk</td></tr><tr><td>T</td><td>Amount_shipped</td><td>ijk</td></tr><tr><td>TPC</td><td>Total_Production_Cost</td><td></td></tr><tr><td>TSC</td><td>Total_Shipping_Cost</td><td></td></tr></table>

{Note: In addition to the above variables, there will be other variables for plant#, plant\_location, Item#, and so on. We have decided to omit these because they do not play any role in the mathematical model itself.}

FUNCTIONS

$$
\begin{array}{l} \mathrm{TPC} = \sum_ {i j} U _ {j} ^ {*} Q _ {i j} \\ \mathrm{TSC} = \sum_ {i j k} S _ {i j k} ^ {*} T _ {i j k} \\ \mathrm{TC} = \mathrm{TPC} + \mathrm{TSC} \end{array}
$$

CONSTRAINTS

$$
\begin{array}{l} {Q _ {i j} <   = C _ {i j}} \\ {\sum_ {k} T _ {i j k} = Q _ {i j}} \\ {\sum_ {i} T _ {i j k} = D _ {j k}} \end{array}
$$

Note that the mathematical model is developed for the entire structured model. Depending on the decision maker's objectives, preferences, and risk-taking nature, the entire model or a part of it may be used in the actual DSS design for specific problems.

A key advantage of using the above data and modelbase design procedures is that they separate the model structure, also called a template, from the data. A template model can be used with different sets of data to obtain different results. A template model also facilitates maintenance. Generally, model structure does not change as frequently as data. If data is separated and stored in a database, a DBMS can be used to take care of data maintenance and enforce data integrity. If models and data are integrated tightly, maintenance becomes difficult. However, when the model needs to be solved, it requires the data from the database. We discuss this data/modelbase integration next.

## 5. Integration of modelbase and database

Database and modelbase integration refers to the process by which a mathematical model obtains the correct data from the database. The modelbase and the database designs for the example problem, discussed in the previous section, may appear to be independent. However, a closer look will reveal that the components of the model, and the relations and attributes of the database are tightly integrated already. Let us illustrate this with the same example.

Consider the variable $C_{ij}$ . The variable name C is defined for the attribute Prod\_Capacity, which is stored in the relation PLANT-ITEM. The index of C includes i and j, which represent the entities PLANT and ITEM, respectively. Note that the index set of C is the cartesian product of the entity sets PLANT and ITEM. Thus, the values of C corresponding to all the combinations of values of i and j are stored in the attribute Prod\_Capacity of the relation PLANT-ITEM in the database. Hence, if the model needs the value of C for, say, plant TOL and item 6-inch-bolt, all it has to do is to obtain the value of the attribute Prod\_Capacity in the relation PLANT-ITEM for the key plant# = TOL and item# = 6-inch-bolt. If SQL is used as a database retrieval language, the model will use the command

SELECT Prod\_capacity

FROM PLANT-ITEM

WHERE Plant# = "TOL" AND Item# = "6-inch-bolt"

Obviously, the model can retrieve only those values that are stored in the database. The values of other variables are calculated by the model itself using the functions and constraints.

The following integration table provides all the necessary information to integrate the modelbase with the database in a DSS designed for the above problem. The DSS designer can implement the integration using any of the programming languages.

<table><tr><td>VARIABLE</td><td>INDEX</td><td>TABLE</td><td>COLUMN</td><td>SELECTION CRITERIA</td></tr><tr><td>C</td><td>ij</td><td>PLANT_ITEM</td><td>Prod_capacity</td><td>plant# = i and item# = j</td></tr><tr><td>U</td><td>j</td><td>ITEM</td><td>Unit_production_cost</td><td>item# = j</td></tr><tr><td>S</td><td>ijk</td><td>PLANT_ITEM_WARE</td><td>Unit_shipping_cost</td><td>plant# = i and item# = j and warehouse# = k</td></tr><tr><td>D</td><td>jk</td><td>WAREHOUSE_ITEM</td><td>demand</td><td>item# = j and warehouse# = k</td></tr></table>

When the integration table is complete, the DSS design specification will include three essential components, viz., database, modelbase, and the integration method, needed to implement the DSS. Since the design is for the entire domain rather than for specific problem situations, there is a need to identify which parts of the design are relevant for designing a DSS for a specific problem situation before it is implemented. Note that our design is independent of the implementation details.

## 6. Design of specific DSS

The modelbase and the database, which model the domain characteristics, represent all the data, variables, functions, and constraints associated with the domain. In addition to the domain characteristics, the decision making process is also guided by the decision maker specific characteristics in a specific problem situation. Some of these characteristics include the following.

(a) objective/goal of the decision maker.

We assume, as do many DSS, that the goal can be clearly stated and quantified. Typical goals include such statements as maximizing a quantity, calculating a quantity, and selecting an alternative that satisfies a specific condition.

(b) preference ordering rule used by the decision maker to evaluate the alternatives.

Sometimes the goal may include preference statements also. For instance, the maximization goal implicitly indicates that an alternative that yields a higher value of the goal is preferred over one that yields a lower value.

(c) risk taking nature of the decision maker.

The type of model to be used in a DSS varies depending on whether the decision maker is risk neutral, risk averse, or risk seeking. Many models, by taking expected or average values of quantities that are not known precisely, assume the risk neutral approach. However, there are studies that indicate that DSS design should match the characteristics of the individual decision making style $[10]$ .

Our methodology assumes that the above characteristics can be elicited from the decision maker. Depending on these characteristics, the entire model/database or a subset of it may be used to support decision making for specific problems. In general, all the data and model components that directly or indirectly influence the goal of the decision maker are possible candidates for inclusion in the DSS. [12] provides some results on identifying relevant/irrelevant data and model components. In the worst case, the entire database and the modelbase can be used in the DSS. After the model is selected, its type and a solver need to be determined. For instance, in some situations, the selected model might be a linear programming model which can be solved using a solver such as LINDO [15]. In other situations, the model might be a simulation model. The identification of model type is relatively straightforward once the model is identified. The selection of a good solver is more complex, and discussion of this process is beyond the scope of this paper. Further research is needed in formalizing the selection of a good solver for models. However, we do illustrate below how a specific DSS can be designed using our model/database for three different cases in our example domain.

Scenario I: The decision maker is interested in minimizing the total cost. All the data stored in the database are known accurately.

In this scenario, the goal is to determine that shipping schedule that minimizes the total cost. So, the preference rule used by the decision maker indicates that the lower the cost, better the schedule is. Since the decision maker has perfect knowledge about all the data about the problem, risk does not play any role in the decision making process.

The goal can be expressed as “minimize TPC + TSC”. The decision maker is interested in the values of unknown variables $Q_{ij}$ and $T_{ijk}$ representing production and shipping quantities respectively. In mathematical models, the factors that influence the goal are represented as functions and constraints that link the goal, the decisions, and other variables. The inclusion of the functions and constraints that link the decision variables and the goal function results in the following model.

$$
\text { minimize   TPC } + \text { TSC }\tag{1}
$$

Subject to

$$
\mathrm{TPC} = \sum_ {i j} U _ {j} ^ {*} Q _ {i j}\tag{2}
$$

$$
\mathrm{TSC} = \sum_ {i j k} S _ {i j k} ^ {*} T _ {i j k}\tag{3}
$$

$$
Q _ {i j} <   = C _ {i j}\tag{4}
$$

$$
\Sigma_ {k} T _ {i j k} = Q _ {i j}\tag{5}
$$

$$
\Sigma_ {i} T _ {i j k} = D _ {j k}\tag{6}
$$

The above model is a linear programming (LP) model. Once the DSS designer identifies it as an LP model, he/she can easily implement a DSS that selects the above model from the modelbase, links it with the database using the integration table discussed in Section 5, and solves it using a solver such as LINDO to determine the shipping schedule that achieves the goal of the decision maker, viz., minimizing the cost.

Scenario II: The decision maker is interested in evaluating a few alternatives (shipping schedules) by calculating the total cost for these alternatives. All the data stored in the database are known accurately.

In this scenario, the goal is to determine the value of the total cost of an alternative for which the values of the unknown variables $Q_{ij}$ and $T_{ijk}$ are specified. Since the decision maker is responsible for evaluating the alternatives, the DSS does not need to have knowledge of preference ordering. Alternately, if a DSS that chooses an alternative from a specified set is desired, then the DSS design can be modified easily to incorporate the preference ordering. Also, since the decision maker has perfect knowledge about all the data about the problem, risk doesn't play any role in the decision making process.

The goal can be expressed as “Calculate TPC + TSC” given the values of variables $Q_{ij}$ and $T_{ijk}$ . Again, the value of the goal function is dependent upon the decision variables and other variables whose values are stored in the database. The functions that relate the goal with these variables are:

$$
\text {   Calculate   TPC   +   TSC   }
$$

Where

(1)

$$
\mathrm{TPC} = \sum_ {i j} U _ {j} ^ {*} Q _ {i j}\tag{2}
$$

$$
\mathrm{TSC} = \sum_ {i j k} S _ {i j k} ^ {*} T _ {i j k}\tag{3}
$$

$$
\Sigma_ {k} T _ {i j k} = \dot {Q} _ {i j}\tag{4}
$$

$$
\sum_ {i} T _ {i j k} = D _ {j k}\tag{5}
$$

$$
Q _ {i j} <   = C _ {i j}\tag{6}
$$

In the above model, the value of $Q_{ij}$ can be calculated from (4), which can then be used to calculate TPC using (2). The value of TSC is given by (3). Then TSC and TPC can be added to determine the total cost.

It appears as if constraints (5) and (6) do not play any role in this context. Note that the values of all the variables in the constraints for an alternative are known. So, before applying the model to calculate the total cost, the DSS needs to check whether the constraints are satisfied by the assumed values of $Q_{ij}$ and $T_{ijk}$ for the alternative. The model is valid only if these are satisfied.

The above model can solved using a deterministic simulation modeling package such as a spreadsheet package. Again, a DSS that checks whether the model is valid and solves the model can be designed by incorporating the appropriate formulas in the spreadsheet.

Scenario III: The decision maker is interested in minimizing the total cost. However, assume that the decision maker is not sure of the value of demand $D_{jk}$ . However, the probability distribution of demand is known and stored in the database.

Similar to scenario I, the goal here is to determine the shipping schedule that minimizes the total cost. However, since the decision maker does not have perfect knowledge about all the problem data, risk plays an important role in the decision making process.

If the decision maker is risk neutral, then the average or expected value of demand can be calculated, which can then be used in the linear programming model discussed in scenario I. If the decision maker is risk averse, the lowest possible value for demand can be used in the model. If the decision maker is a risk seeker, the maximum value of demand can be used. If the decision maker would like to get insights into different possible total costs, then a stochastic simulation model can be used. Whatever be the model chosen, all the information needed to design the DSS is contained in the data/modelbase. For situations that involve uncertainty, DSS are usually designed so that the decision maker can perform what-if (sensitivity) analysis by altering data and models. A package such as IFPS [5] has the features to accommodate such explorations.

## 7. Discussion

The most important benefit of using the structured modeling methodology to design DSS is that the methodology imposes structure and discipline onto the otherwise unstructured exercise of designing a computer-based system to support decision making. The methodology allows the designer to focus on the data and relationships in the problem domain. In addition to providing detailed procedures for the design of the two important components of DSS, viz., database and modelbase, and their integration, our methodology has a number of other features that make it useful and desirable. First, the database and modelbase design procedures and the integration method can be automated by software. Even though currently no tool is available, efforts have already begun in this direction [6]. We believe that a design tool such as CASE for DSS will significantly enhance the use of DSS. Second, procedures that support the designer in developing a complete and consistent structured model exist [12]. Third, since the methodology is an extension of the ER modeling, in which many information systems professionals already have experience, the methodology can be learned and used with limited additional training.

A limitation of the structured modeling approach is that it assumes, in its current form, that the problem data, decision maker's goal, and other characteristics can be quantified. The focus on quantifiable data and relationships among data makes the methodology less suitable for situations that involve qualitative analysis. For instance, development of a DSS that uses models such as Analytic Hierarchy Process (AHP) [14], needs additional enhancements to the methodology.

There are other issues that are important to the design of DSS that we have not addressed in this paper. For instance, the user interface is an important component of a DSS. Our methodology does not address the interface issue at all. Design of a good interface to any computer based system is a complex issue which needs to be addressed separately. Another feature that DSS tend to have is the ability to perform exploration through what-if and sensitivity analysis. Many DSS generators including spreadsheets provide this capability. Thus the tools selected for implementation, rather than the design, will provide this capability in a DSS. There have also been attempts to provide model exploration capability in optimization based DSS [13].

We stated earlier that our original motivation for this research was to develop a good teaching methodology that can be used in DSS classes. Our experience suggests that our methodology does improve the DSS design skills of students. We have been teaching DSS courses for the last five years, with approximately 50 students each year, at the undergraduate level in a medium-sized mid-western university. The DSS course uses a case, similar to the one given in the appendix, to be done by individual students. The students are expected to analyze the case, identify the data and models needed to provide decision support, select an appropriate tool for implementation, and implement an actual DSS. The students were given 6 weeks to finish the project. When the students were exposed not to our methodology but to general high level DSS design approaches given in text books such as [17], the performance of the students in the project was well below expectations. Many did not complete the project; often they chose incorrect models and tools, and there was no clear separation of data and modelbases. The average score in the project was approximately 60 out of a possible 100. Even though most of our students in the DSS course (the students were primarily senior undergraduate business students specializing in MIS) had a fundamental understanding of models and databases, and knowledge of several software tools, they experienced severe difficulties in integrating all these pieces together to design DSS for specific problems. In the last two years, when we used our methodology, the performance of the students improved significantly. The average score in the project went up to 85. Most of the students completed the project. There was a clear separation of data and modelbases even though some did come up with incorrect database and modelbase designs. We hypothesize that the performance improvement was due, at least in part, to the integrative framework provided by the methodology to design a DSS. Our experience suggests that the structured modeling methodology facilitates the analysis and design phases of the DSS design process. Our classroom experience is admittedly not a rigidly controlled experiment, and thus the results will need to be confirmed. However, the experience does suggest the potential of this methodology as a teaching tool.

We believe that the methodology is a promising new development in the field of model based DSS design methodologies. The methodology opens up many new avenues for further research. First of all, even though our classroom experience has been positive, a formal evaluation of the methodology in controlled classroom as well as real life settings needs to be conducted. The evaluation is needed to not only show that the application of the structured modeling methodology results in better DSS designs but also collect data that can suggest further guidelines in developing better structured models. The results can be used to enhance the methodology. Second, structured modeling will flourish only if computer based tools similar to CASE tools are developed to support the methodology. The SM tool should automate all the procedures that can be automated, and let the designer concentrate on analysis and modeling, which, in our opinion, is more difficult to automate. Many of the procedures discussed in this paper can be automated easily. Additional procedures that check the “correctness” of a structured model can also be implemented in a software tool.

## 8. Conclusions

We have presented a methodology based on structured modeling to support the design of model based Decision Support Systems. The methodology integrates the design of database and modelbase, two important components of a DSS. The procedures that transform a structured model into a database and a modelbase are simple to use and amenable to automation. We also present a natural framework to integrate the data and modelbase. Preliminary experience with using the methodology in classroom settings is very encouraging. We have also proposed further research that will make the methodology attractive for practitioners in the DSS design process.

## Appendix A. Red and blue company (adapted from The Frazee Advertising Campaign [17])

The Red and Blue Company is a retailer of paint and wallpaper supplies. To a large degree Red and Blue purchases products in bulk at wholesale and provides retail store convenience such as trained personnel, color samples, and wallpaper catalogs to its clientele. Only a small portion of its business is involved in the actual manufacturing of paints.

The company has three major product areas: interior paints, exterior paints, and wall coverings. Interior paints are classified according to their brand name, type (such as acrylic), and color. The company has also developed a coding scheme for identification and control purposes. Similar classification exists for exterior paints also. Wallpapers are classified according to their brandname, color, and pattern style. Wallpapers are also identified by codes.

The problem faced by Red and Blue company is one of business planning. The company is interested in budgeting its advertising expenditure on each product for the next three years (1995, 1996, and 1997), and allocate the budget among various media. The sales of a product in a year depends on the advertising for that product in that year as well as the population surrounding the retail outlet. The sales manager believes, based on historical data, that the relationship between advertising, population, and sales is a linear one. The sales manager is confident that he/she can obtain the population figure from the local chamber of commerce.

The cost of producing each product in each year can be estimated fairly accurately. Since the company is interested in the bottom line profits, there is a need for data such as the profit from each product in the next three years, as well as the total profit in each of those years, for various levels of advertising expenditure.

The other problem faced by Red and Blue company is the allocation of advertising budget to different media. The company advertises on media such as newspaper, TV, direct mail etc. One of the important factors that affects this allocation process is the exposure of these media to the potential customers. The exposure is measured by audience points. Historical data on audience points per advertising spot (eg., a TV Commercial, a newspaper ad etc.) in a medium is available from marketing research companies. Each spot carries with it a cost. The company has to decide how many spots in each media to buy for its products so that it can maximize the total audience points. Obviously the total money spent on advertising for a product cannot exceed its budget for the product.

The following data and reports may be useful in your analysis.

The data below are sample for one paint and one wallcovering. The actual case will contain similar data for all paints and wallcoverings.

Historical data for population-advertising-sales relationship

<table><tr><td>Year</td><td>Interior paint advertising ($K)</td><td>Population (000)</td><td>Interior paint sales ($K)</td></tr><tr><td>1985</td><td>10</td><td>800</td><td>20465</td></tr><tr><td>1986</td><td>50</td><td>840</td><td>21468</td></tr><tr><td>1987</td><td>50</td><td>880</td><td>24321</td></tr><tr><td>1988</td><td>50</td><td>920</td><td>24798</td></tr><tr><td>1989</td><td>35</td><td>960</td><td>25432</td></tr><tr><td>Year</td><td>Exterior paint advertising ($K)</td><td>Population (000)</td><td>Exterior paint Sales ($K)</td></tr><tr><td>1985</td><td>15</td><td>800</td><td>10200</td></tr><tr><td>1986</td><td>40</td><td>840</td><td>12265</td></tr><tr><td>1987</td><td>40</td><td>880</td><td>14245</td></tr><tr><td>1988</td><td>55</td><td>920</td><td>17680</td></tr><tr><td>1989</td><td>25</td><td>960</td><td>14232</td></tr><tr><td>Year</td><td>Wallpaper advertising ($K)</td><td>population (000)</td><td>Wallpaper Sales ($K)</td></tr><tr><td>1985</td><td>15</td><td>800</td><td>20433</td></tr><tr><td>1986</td><td>100</td><td>840</td><td>26004</td></tr><tr><td>1987</td><td>85</td><td>880</td><td>23401</td></tr><tr><td>1988</td><td>70</td><td>920</td><td>27245</td></tr><tr><td>1989</td><td>55</td><td>960</td><td>24754</td></tr><tr><td colspan="4">Budget table needed by the manager</td></tr><tr><td></td><td>1995</td><td>1996</td><td>1997</td></tr><tr><td>Population (000)</td><td>800</td><td>840</td><td>880</td></tr><tr><td>Paint adv ($K)</td><td>75</td><td>288</td><td>360</td></tr><tr><td>Wallcov adv ($K)</td><td>75</td><td>288</td><td>360</td></tr><tr><td colspan="4">Paint dept</td></tr><tr><td colspan="4">Interior paint</td></tr><tr><td>Paint sales</td><td>XXX</td><td>XXX</td><td>XXX</td></tr><tr><td>Cost of goods sold</td><td>XXX</td><td>XXX</td><td>XXX</td></tr><tr><td>Profit</td><td>XXX</td><td>XXX</td><td>XXX</td></tr><tr><td>Exterior paint</td><td></td><td></td><td></td></tr><tr><td>Paint sales</td><td>XXX</td><td>XXX</td><td>XXX</td></tr><tr><td>Cost of goods sold</td><td>XXX</td><td>XXX</td><td>XXX</td></tr><tr><td>Profit</td><td>XXX</td><td>XXX</td><td>XXX</td></tr><tr><td>Wallcovering deptwsales</td><td>XXX</td><td>XXX</td><td>XXX</td></tr><tr><td>Cost of goods sold</td><td>XXX</td><td>XXX</td><td>XXX</td></tr><tr><td>Profit</td><td>XXX</td><td>XXX</td><td>XXX</td></tr><tr><td>Totals</td><td></td><td></td><td></td></tr><tr><td>Sales</td><td>XXX</td><td>XXX</td><td>XXX</td></tr><tr><td>Cost of goods sold</td><td>XXX</td><td>XXX</td><td>XXX</td></tr><tr><td>Profit</td><td>XXX</td><td>XXX</td><td>XXX</td></tr></table>

Budget Allocation table needed by the manager

<table><tr><td></td><td>Interior Paint</td><td>Exterior paint</td><td>Wallcovering</td></tr><tr><td>radio spots</td><td>XXX</td><td>XXX</td><td>XXX</td></tr><tr><td>newspaper spots</td><td>XXX</td><td>XXX</td><td>XXX</td></tr></table>

## References

[1] L. Bally, J. Brittan and K.H. Wayner, A Prototype Approach to Information System Design and Development, Information and Management 1 (1977) 21–26.

[2] H. Bhargava, S. Kimbrough and R. Krishnan, R. Unique Name Violations, a Problem for Model Integration or You Say Tomato, I Say Tomahto, ORSA Journal on Computing 3, No. 2 (1991) 107–120.

[3] C.H.P. Brooks, A Framework for DSS Development, in: P. Gray, Ed., Decision Support and Executive Support Systems (Prentice Hall, Englewood Cliffs, NJ, 1994) 27–45.

[4] P. Chen, The Entity-Relationship Model: Toward a Unified View of Data, ACM Transactions on Database Systems 1, No. 1 (1976).

[5] Execucom Systems Corporation IFPS/Plus User's Manual, Release 3.5, Austin, TX, 1987.

[6] C.K. Farm, An Integrated Information Systems Architecture Based on Structured Modeling, PhD Thesis (Graduate School of Management, The University of California at Los Angeles, 1985).

[7] A. Geoffrion, An Introduction to Structured Modeling, Management Science 33, No. 5 (1987) 547–588.

[8] D. Kroenke, Database Processing: Fundamentals, Design, Implementation (Macmillan, New York, NY, 1992).

[9] K.R. MacCrimmon and D.A. Wehrung, Taking Risks: The Management of Uncertainty (Free Press, New York, NY, 1986).

[10] J.L. McKenney and P.G.W. Keen, How Managers' Minds Work, Harvard Business Review 52, No. 3 (1974) 79–90.

[11] J.G. Nauman and M.A. Jenkins, Prototyping: The New Paradigm for Systems Development, MIS Quarterly (1982) 29–40.

[12] S. Raghunathan, KNAMS: A Knowledge Acquisition Tool for Modeling Systems, IEEE Transactions on Systems, Man, and Cybernetics 23, No. 5 (1993) 1316–1329.

[13] S. Raghunathan, R. Krishnan and J. May, On the Use of Belief Maintenance Systems to Assist Mathematical Modeling, IEEE Transactions on Systems, Man, and Cybernetics, Forthcoming (1994).

[14] T.L. Saaty, The Analytic Hierarchy Process (McGraw-Hill Publishers, New York, NY, 1980).

[15] L. Schrage, Linear, Integer, and Quadratic Programming with LINDO (Scientific Press, Palo Alto, CA, 1986).

[16] R.H. Sprague, Jr., A Framework for the Development of Decision Support Systems, MIS Quarterly (1980) 1–26.

[17] E. Turban, Decision Support and Expert Systems: Management Support Systems (Macmillan Publishers, New York, NY, 1990).

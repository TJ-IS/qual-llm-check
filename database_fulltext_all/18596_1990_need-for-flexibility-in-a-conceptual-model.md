---
otero_id: 18596
otero_key: "USZFEYCS"
title: "Need for “flexibility” in a conceptual model"
authors: "Kathi Hogshead Davis"
year: "1990"
journal: "Information & Management"
doi: "10.1016/0378-7206(90)90025-d"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Need for “Flexibility” in a Conceptual Model

Kathi Hogshead Davis

Northern Illinois University, Department of Computer Science, Dekalb, IL 60115, USA

The translation of one data model into another has become necessary. Database design methodologies stipulate that a conceptual model should be created prior to implementing a new database system. It is then, usually, the translation of this conceptual model into the physical model of a commercial database management system (DBMS) that is a necessity (e.g., The translation of the entity-relationship model into a relational DBMS). However, more and more we are seeing the translation of the data models in currently implemented conventional file and database systems into conceptual models (e.g., The translation of an ORACLE DBMS into an entity-relationship model). It is the conceptual model that is produced from the 'reverse' translation process that we address here; however, the ideas of flexibility can be applied to new database designs also. Since several different reverse translation algorithms have been developed, the questions that arise are: How do we know the resulting conceptual models are accurate? Does the resulting model contain enough information to be useful to database designers and which one is easier for the database designer to work with and to use as a communication tool with users or to develop new databases? The problem is that resulting conceptual data models from two different algorithms may differ even in the data objects obtained, and yet both be equivalent to the original model.

Keywords: Conceptual Data Model, Logical Data Model, Database Design, Relational Data Model, Entity-Relationship Model, Re-engineering, Data Model Translation, Behavior in Data Models, Software Reverse Engineering.

## 1. Introduction

Current data applications (either conventional files or database systems), especially those that have “grown up” over many years are unknown, uncharted territories – usually created by many different individuals and containing many different styles of design. A major difficulty in these data environments is that no one knows exactly what the data and the interrelationships really look like. This problem becomes severe when the current environment is to be improved or is needed for integration into other data environments. At these times, a more abstract, more conceptual understanding of the data is needed. That way, the database designer, armed with full comprehension of the existing system, can proceed in a knowledgeable manner. With a conceptual model of the current environment, he/she has the means, during new database development or database integration, of promoting better communication among the users, be they end-users, programmers, or analysts.

![](/api/attachments/USZFEYCS/fulltext/images/f01efb434b6ff6111e265f054cff7ddfc99df1d1801734c58270c60442059f0f.jpg)

Kathi Hogshead Davis has been a faculty member in the Department of Computer Science at Northern Illinois University for ten years. Prior to her teaching career she worked as an application programmer, systems analyst, and database designer for the Student Information System at Northern Illinois University. She received her B.S. and M.S. in Computer Science from Northern Illinois University and her Ph.D. in 1985 from the Department of Computer Science at Illinois Institute of Technology. Dr. Davis has a variety of research interests including Databases, Logical Data Modeling, Object-Oriented Data Modeling, Systems Analysis and Design, Software Engineering, and Re-Engineering. She has presented numerous papers at international and national meetings of different professional organizations. Dr. Davis is the co-author of a textbook entitled Structured Programming: PL/I with PL/C and is currently writing an introductory database textbook.

What is needed, then, is an algorithm that will translate a current environment into a conceptual model that provides the database designer with as much information as possible and that can be used as a communication tool. The goals of such a reverse translation algorithm are to produce a conceptual model that is

1. equivalent to the current environment;

2. clear in its representation of all the properties of the environment; and

3. easy to modify and use for future database designs.

In studying current reverse translation algorithms, we need to determine if these goals are being met. To prove that the first goal has been met, a definition of 'equivalence of translation algorithms' is needed. One that has been widely accepted is stated in [11]: A data model $DM_{j}$ which has been translated from data model $DM_{i}$ is equivalent if, and only if, there exists an inverse translation that when applied to $DM_{j}$ produces $DM_{i}$ . That is

## inverse-translation-algorithm

$$
\left(\text { translation - algorithm } \left(D M _ {i}\right)\right) = D M _ {i}.
$$

Therefore each reverse translation algorithm needs to have a corresponding inverse algorithm in order to show that it meets this equivalency test.

The second goal can be satisfied with the use of one of the semantic data models available for database design. Several of the Computer Aided Software Engineering (CASE) tools on the market today use some variation of the Entity-Relationship Model (ERM) for database design (Excelerator by Index Technology Corp., DesignAid from Nastec, and Consoi-ERM by SystemOID). For this and other reasons, we decided to use the ERM as the conceptual model in this study. The second goal can thus be met by using the Entity-Relationship Model [3] for the conceptual model. However, it is not, as defined, complete enough to show all the properties of a current environment. Here, we propose an addition in the form of the Update Protocol Model [1] to enhance the ERM as a conceptual model.

The third goal will give the database designer more control over the use of a conceptual model. This is where the flexibility of a conceptual model enters the picture. Flexibility can be determined by the impact modifications have on a conceptual model. For example, the addition (or deletion) of entities in the ERM has a greater impact on the model than the change in a role of an entity. (e.g. A roll change would occur if the DEPARTMENT entity was changed from representing only those departments involved in a certain project to all departments that could work on the project). The addition or deletion of objects in an ERM causes 'schema restructuring,' whereas a role change only requires modification of the restriction placed upon an entity. The more flexible the conceptual model, the less impact a modification has on the objects within the model. The database designer needs to be able to make the necessary modifications with as little impact on the schema as possible.

We begin our discussion of the flexibility of conceptual models with some definitions.

## 2. The Conceptual Data Model

Generally, data models have been defined as (1) the structure of the data and (2) the operators allowed to perform on the data. For example, it is the specification of the allowable operators that would change the data structure of a 'list of objects' into either a stack, COBOL record, or queue. Data models also include constraints placed upon the allowable operations. These constraints are restrictions on the permitted operations that prohibit the existence of certain data structures. The insertion and deletion processing constraints are called "behavior" of the data model. Here we propose an enrichment of these basic definitions that will be used to create a reverse translation algorithm that results in a conceptual model which meets the goals. We propose the following definitions:

1: Data Object

$= [Data Structure, Operators]$

2: Data Model

=[Data Object, Inherent Behavior]

3: Conceptual Model
= [Data Model, Explicit Behavior]

First, we combine the structure of the data with the allowable operators into a concept called a 'Data Object'. Data Objects and their 'Inherent Behavior' make up a Data Model. Inherent Behavior is the collection of all inherent constraints. This differs from the definition of data models in [11] only in that we have made the inherent constraints part of a Data Model rather than the idea that a data model can have inherent constraints associated with it. Conceptual models have been defined as representations of the information content of a database without regard to the physical storage of the data. We enhance this definition with the addition of 'Explicit Behavior' to a Data Model to produce the Conceptual Model. Therefore, a Flexible Conceptual Model not only includes the information content of a database but also the restrictions placed upon the information during insertion and deletion operations.

Next, the differences between the ‘static’ and ‘dynamic’ properties of a ‘schema’ must be presented. A Schema is traditionally defined as an instance (occurrence) of a data model. It contains a collection (instances) of data objects allowable within a data model. For example, a database designer at a company uses the ERM to design a database for the EMPLOYEE information that contains the EMPLOYEE, DEPARTMENT and PROJECT entities and their corresponding relationships as Data Objects. Here DM is used to refer to a type of Data Model (e.g., the ERM). Likewise, CM refers to the Conceptual Model. Schema refers to an instance of a DM or CM.

The static properties of a schema are those properties that are defined by the Data Definition Language (DDL) within a Data Model (e.g. the CREATE relation in a relational DM) and which must be true for all occurrences of the data within a schema. Not all static properties are modifiable. However, those that are require use of the DDL and may change the schema itself by adding or deleting instances of data objects.

In contrast, the dynamic properties of a schema are the set of allowable actions represented by the data manipulation language (DML). Thus operators such as INSERT A ROW, DELETE A ROW and the restrictions placed upon them are included as dynamic properties of a schema based upon the relational DM.

Inherent Behavior are the constraints directly associated with the Data Structures in a specific DM. These rules are applied to the Data Structures and all subsequent schemas must adhere to them. For Inherent Behavior to change the actual DM must change. For example, in the hierarchical data model the data are structured into a tree. The inherent behavior states that each parent node of the tree must have a one-to-many relationship with each of its children nodes. If this behavior were to change to allow a many-to-many relationship, we would no longer have a tree structure or an hierarchical DM.

Inherent Behavior is considered a static property of a Schema. However, Inherent Behavior cannot be changed via the DDL -- even though it is specified by the DDL. The DDL simply defines a Schema's Data Objects following the inherent constraints of a DM. Thus maintaining certain restrictions as Inherent Behavior in a DM makes it harder (and maybe impossible) to modify a Schema.

Explicit Behavior are constraints that are tangential to the data within a DM. In our case, these are insertion and deletion processing constraints (e.g., the salary of an employee cannot exceed \$50,000). Explicit constraints can be changed without changing the DM. And furthermore, they are frequently changed in conjunction with changes to the requirements of the data within a Schema. The modification of the Explicit Behavior does, however, change the Conceptual Model. That is when the restrictions placed upon the insertion and deletion of the information are altered, the CM is changed – but not the DM.

Explicit Behavior is included in the dynamic properties of a Schema. It, along with the operators, define the allowable actions that can be performed on a Schema.

By examining the distinction between a Data Model and a Conceptual Model an interesting phenomenon is revealed: currently there exists behavior that may be either inherent or explicit depending upon the user of a data model. This, we believe, is why one person's schema in a data model may differ substantially from another's in what is currently considered the same data model. In actuality they are using two different Data Models. For example, Codd [4] would argue that referential integrity constraints are part of the definition of the relational data model (RDM) and must be considered Inherent Behavior. However, we have all seen definitions of relational database systems where these constraints are considered Explicit Behavior (i.e., referential integrity is user defined). In our definitions, these two Data Models, even though both are very similar, are not exactly the same; their differences reside within the Inherent Behavior.

Similarly, Chen [3] imposed the constraint “no relationship can exist without corresponding entities” on the entity-relationship data model (ERDM). However, one can argue quite convincingly that this constraint should not be part of the DM itself since some organizations may want to be more liberal in their approach: they may allow the triggering of an entity’s existence once the appropriate relationship is known. What this user wants is a more dynamic use of relationships in the ERM.

Due to inconsistent use of these types of behavior within current data models, the appropriate place should be within the Explicit Behavior. This way, the database designer can determine, based upon data and its usage, whether or not to include referential integrity within a relational database. A more flexible Conceptual Model could be used with the same underlying DM either way.

## 3. Translation Algorithms

Currently, many algorithms to translate existing data environments into “conceptual models” have been presented $[2,5,7,9,10]$ . Essentially, there are two types of translation algorithms. The first translation algorithm translates a Source Data Model (SDM) into a Destination Data Model (DDM) obtaining only the Data Objects and the Inherent Behavior in the DDM. This is called “Data Model-to-Data Model” translation (DM-to-DM).

The second translation algorithm translates a SDM into a Destination Conceptual Model (DCM) using the DCM's Data Objects, Inherent Behavior, and Explicit Behavior. This type is called the "Data Model-to-Conceptual Models translation (DM-to-CM).

It might appear, at first glance, that the only difference between these two translation algorithms is the simple addition of explicit behavior to the data model in order to create a conceptual model. However, when the two translation algorithms are applied to an actual implementation of an SDM, the resulting DDM and DCM schemas do not have a one-to-one correspondence between the instances of Data Objects obtained (e.g., see Figures 1 and 2). The use of the Explicit

![](/api/attachments/USZFEYCS/fulltext/images/f8428afa3569b6b8c586aad13b90ba6e16a5d6e4a343c76426bcf7c3226a9418.jpg)  
Fig. 1. An Entity-Relationship Data Model Schema.

Behavior in the DCM, allows for a more flexible collection of Data Objects as we will show in the following sections by demonstrating each of the two types of translation algorithms using a relational data model to entity-relationship data model example.

## 4. Data Model-to-Data Model Translations

Casanova and de Sa [2] studied the problem of translation from the relational model to the entity-relationship model. The objects in their paper were presented as “conventional file records.” However, the restrictions placed upon these records make them third normal form relations. This algorithm carries over the inherent constraints of the Relational Data Model (RDM) and imposes them, as Inherent Behavior, on the resulting Entity-Relationship Data Model (ERDM). For example, applying their algorithm to the following relations of an RDM the resulting ERDM is shown in Figure 1.

Employee (E#, Name, Salary, Building#, Room#)

Employee-Project (E#, P#, Hours-spent)
Department-Project (D#, P#, Budget)
Job (J#, Description, Salary-Range)
Employee-Job (E#, J#)

Location (Building #, Room #, Description, Capacity)

![](/api/attachments/USZFEYCS/fulltext/images/c9b12f55b201f315fae940c1b4694b04a2682195e22f3c55140b0bd51ad416c9.jpg)  
Fig. 2. An Entity-Relationship Conceptual Model Schema.

This approach does not really yield a Conceptual Model for two reasons:

(1) no explicit behavior is included; and (2) the Inherent Behavior of the RDM is translated into the Inherent Behavior of the ERDM. Thus the resulting ERDM Schema is no more “conceptual” than the original RDM Schema. This defeats the purpose of the entity-relationship model, since it was defined to be a conceptual model. Therefore, by our terminology, this algorithm really converts an RDM into an ERDM.

## 5. Problems with DM-to-DM Translations

Since the ERM created with this methods is really an ERDM: there is no more flexibility in the ERDM than in the RDM. By using only the Inherent Behavior of both Data Models, we have taken the static properties of one DM and forced the Data Objects within the resulting DM to follow them. For example, an instance of Department cannot be added unless it is associated with some Project. Now if the designer decided that a Department should really be a separate object, not necessarily connected to a Project, the ERDM Schema would require modification. Since we are interested in obtaining a Conceptual Model of the informational content, it is not desirable that this type of behavioral change results in a major Schema restructuring.

Another difficulty highlighted by this example is that although there are common (partial) key attributes among the relations in the RDM, the algorithm completely ignores them. For example, no relationship is assumed to exist between Department-Project and Employee-Project entities, although they have a potentially independent object Project common between them. This is a clear case of imposing the static properties of the RDM onto the ERDM and again it would take a Schema restructuring to simply change the behavior of the data.

Fig. 2 (continued).  
```txt
Explicit Behavior:
INSERT emp IN Employee
    IMPLIES {INSERT emp-loc IN E-L | emp-loc [E#] = emp [E#]}
    DELETE emp FROM Employee
    IMPLIES {DELETE emp-proj FROM E-P | emp-proj [E#] = emp [E#]}
    IMPLIES {DELETE emp-job FROM E-J | emp-job [E#] = emp [E#]}
    IMPLIES {DELETE emp-loc FROM E-L | emp-loc [E#] = emp [E#]}
INSERT job IN Job No explicit behavior added.
DELETE job FROM Job
    IMPLIES {DELETE emp-job FROM E-J | emp-job [E#] = emp [E#]}
INSERT emp-job IN E-J
    PRECOND ∃ emp ∈ Employee ∃ job ∈ Job
    emp-job [E#] = emp [E#] AND
    emp-job [E#] = job [J#]
DELETE emp-job FROM E-J No explicit behavior added.
INSERT emp-proj IN E-P
    PRECOND ∃ emp ∈ Employee
    emp-proj [E#] = emp [E#]
    IMPLIES {INSERT project IN Project | project [P#] = emp [P#]}
DELETE emp-proj FROM E-P
    IMPLIES {DELETE project FROM Project | project [P#] = emp-proj [P#]}
INSERT project IN Project NOT ALLOWED
DELETE project FROM Project NOT ALLOWED
INSERT dept IN Department NOT ALLOWED
DELETE dept FROM Department NOT ALLOWED
INSERT dept-project IN D-P
    PRECOND ∃ project ∈ Project
    dept-project [P#] = project [P#]
    IMPLIES {INSERT department IN Department | department [D#] = project [D#]}
INSERT location IN Location No explicit behavior added.
DELETE location FROM Location
    IMPLIES { DELETE emp-loc FROM E-L | emp-loc [Building#, Room#] = location [Building#, Room#]}
INSERT emp-loc in E-L
    PRECOND ∃ location ∈ Location
    ∃ emp ∈ Employee
    emp-loc [Building#, Room#] = location [Building#, Room#]
    emp-loc [E#] = emp [E#]
DELETE emp-loc FROM E-L No explicit behavior added.
```

To summarize, it is true that the resulting ERDM schema achieved from the DM-to-DM translation algorithm is equivalent to the source RDM Schema, therefore the first goal of a translation algorithm is met. We can find an inverse translation [8] that, when applied to the ERM schema, gives the exact same Schema (relations) as in the original RDM. However, the second and third goals are not really achieved. We find the resulting ERDM Schema too closely tied to the RDM Schema, making the ERDM just a graphical means of representing an existing RDM. Our purpose, however, is to find a translation algorithm that will obtain an equivalent Conceptual Model tied only to the Inherent Behavior of its underlying DM, not the original DM. Thus, as a result of this type of translation, the destination Conceptual Model Schema should not reflect any of the physical nature of the data – even when being translated from currently implemented source Schemas. This is where the Explicit Behavior can be used.

## 6. Data Model-to-Conceptual Model Translations

This method of translation converts a DM into a CM - in our example, an RDM into an Entity-Relationship Conceptual Model (ERCM). The major purpose of the DM-to-CM translation is to obtain a resulting CM that uses its DM's Inherent Behavior. However, in order for a CM Schema to be equivalent to a source DM Schema, the Inherent Behavior of the SDM must be represented somewhere in the DCM. This is done by translating the Inherent Behavior of the SDM into the Explicit Behavior in the DCM. Thus we have translated the static properties of the SDM into dynamic properties of the DCM. Therefore, more control is given to the database designer by allowing easier modifications to the restrictions placed upon the insertion and deletion of the information. The database designer can modify these restrictions with the use of the DML.

At this point in time, we do not consider any of the Explicit Behavior of the SDM, since we are only looking at a source Data Model not at a source Conceptual Model.

Before we show an example of the DM-to-CM translation, it is necessary to introduce some technique for representing Explicit Behavior. In order to avoid translating one type of behavior representing technique into another, the method established must be able to be used with all DMs. Since our example translates an RDM into an ERCM, we are concerned here with a technique that can represent the processing constraints within both the RDM and the ERCM. We have selected the Update Protocol Model (UPM) which has been shown to successfully model behavior of most of the popular models $[1,6]$ including the two in our example.

The exact algorithms to translate an RDM into an ERCM and to test their equivalence were originally discussed in $[7]$ . The result is of applying this DM-to-CM translation to the source RDM listed above is shown in Figure 2. The UPM is used to represent all the Explicit Behavior of the ERCM Schema that has been translated from the Inherent Behavior of the RDM Schema. Thus, during the conversion process many of the inherent constraints of the RDM are made explicit in the resulting ERCM. By doing this, equivalent behavior of the instances of the data can be maintained within both the RDM and ERCM Schemas, and yet result in a more flexible CM.

The algorithm used in the DM-to-CM translation example chooses the Explicit Behavior of the destination ERCM to represent only the Inherent Behavior of the source RDM that, when imposed upon a Schema in the ERCM, would cause a Schema restructuring simply for a behavioral change. The inherent constraints chosen are ones that have a high probability of needing modification by the database designer.

## 7. Benefits of DM-to-CM Translations

The differences between the ERDM Schema of Figure 1 and the ERCM Schema of Figure 2 are that, in the ERCM Schema, there exists separate entity-sets Project and Department therefore additional Data Objects have been created. The Inherent Behavior of the Project and Department relations (in the RDM Schema) have become Explicit Behavior in the ERCM Schema. Note that due to the UPM protocols, a Department cannot, still, be inserted except through the D-P relationship. This is exactly as it is in the original RDM Schema. However, the ERCM Schema allows the designer to modify this behavior without a Schema restructuring. Thus the designer can change the DML to reflect the new behavior whereas in the ERDM Schema the DDL would be needed. The net result is that more of the changeable behavior of the data is in the control of the designer rather than in the control of the Data Model – which is the way a conceptual model should be.

To summarize, the DM-to-CM translation algorithm meets the goals stated earlier. To meet the first goal, an inverse translation algorithm is needed. For the second goal, the ERM, along with the UPM protocols making up the ERCM, represent all the properties of the current environment needed by the database designer in order to fully understand the RDM. And the flexibility of the ERCM achieved (the third goal) is shown by the ability to change the role of either the Department or Project entities by simply changing the Explicit Behavior (the UPM protocols).

## 8. A RDM-to-ERCM Translation Algorithm

We will use the following notation in the algorithm.

RDM - represents the relational data model, $\mathbf{r}_{\mathrm{i}}$ - represents a relation in R,

ERCM - represents the entity-relationship conceptual model,

$e_{j}$ – represents an entity-set in ERCM,

$s_{k}$ – represents a relationship in ERCM,

$a_{i}$ - represents an attribute of a relation $r_i$ or an entity-set $e_i$ ,

$K_{i}$ – represents the primary key of relation $r_{i}$ ,

$L_{j}$ – represents the primary key of entity-set $e_{i}$ ,

B[X] - represents the behavior of X and B[X] = I[X] U E[X] where I[X] are the inherent constraints, E[X] are the explicit constraints and $\mathbf{X} \in \{\mathrm{RDM}, \mathrm{ERCM}, \mathbf{e}_{\mathrm{j}}, \mathbf{s}_{\mathrm{k}}, \mathbf{x}_{\mathrm{i}}\}$ .

We note that some type of constraints are not considered by this algorithm, e.g., explicit constraints of $r_{i}$ . We also assume here that all the relations are in third normal form; a generalized algorithm is under construction.

Each step described in the algorithm has two parts: the translation of the structure of the data and the translation of the behavior of the data.

## 8.1. The Entity-Sets

The first thing we look for are the obvious entity-sets by examining the primary keys of the relations in RDM.

Step 0: B [ERCM] = empty

Step 1: (a) Any relation $r_i$ in RDM that has a single attribute $(K_i = \{a_i\})$ as its primary key is translated into an entity-set $e_j$ in the ERCM with the same attribute for a primary key $(L_j = K_i)$ .

(b) B [ERCM] = B [ERCM] U B $[r_{i}]$ No explicit behavior added.

In the relational model above, the Employee relation satisfies this requirement. Therefore, it becomes the Employee entity-set in the new ERCM.

The Job relation also meets this requirement and becomes the Job entity-set during the translation.

Step 2:

(a) Any relation $r_i$ in RDM that has a key containing multiple attributes ( $K_i = \{a_1, a_2, \ldots, a_n\}$ where $n > = 2$ ) is now considered. If the attributes are always used together as a set in primary keys of the other relations in RDM (never used separately within the primary keys of the other relations) or if the attributes are never used again, then $r_i$ is translated into an entity-set $e_j$ in the ERCM with the same set of attributes for the primary key ( $L_j = K_i$ )

(b) B [ERCM] = B [ERCM] U B $[r_{i}]$ No explicit behavior added.

The Location relation meets the criteria in Step 2, so it is translated into the Location entity-set in the ERCM. The Department-Project and Employee-Project relations do not meet this requirement because P# is used in combination with both D# and E# in two separate entity-sets.

## 8.2. The Dangling Keys

Now the “dangling keys” in RDM are sought. A dangling key attribute is an attribute that is “left over”; when the key of relation $r_{i}$ is compared to the key of an entity-set $e_{j}$ . That is, the dangling key attributes are the ones in $r_{i}$ not included in the key of $e_{j}$ . For example, the primary key of $r_{i}$ is $K_{i} = \{a_{1}, a_{2}\}$ and the primary key of $e_{j}$ is $L_{j} = \{a_{1}\}$ , then $a_{2}$ is the dangling key.

The dangling key is defined as an entity “discriminator” by Korth and Silberschatz in [8]. Also, the relation is which the dangling key resides could be considered a weak entity-set as defined by Chen [3]. The “weakness” of the dangling key entity-set will not be represented as a constraint of the data model but rather by the explicit behavior of the conceptual model.

Step 3:

(a) Repeat until there are no more dangling keys: If a relation $r_{i}$ has a dangling key attribute set $A = \{a_{1}, a_{2}, \ldots, a_{n}\}$ when compared to an entity-set $e_{p}$ in the ERCM, a weak entity-set $e_{j}$ is created for the dangling key attribute set. The only attribute of $e_{j}$ is the dangling key attribute set A which is the primary key of the new entity-set $e_{j}$ (e.g., $L_{j} = \{A\}$ ). A many-to-many relationship $s_{k}$ also created from $r_{i}$ between the new weak entity-set $e_{j}$ and the strong entity-set $e_{p}$ used in the comparison. The key of $s_{k}$ is $L_{k} = L_{n} U A$ .

(b) B [ERCM] = B [ERCM] U

{ INSERT e IN $e_{j}$ NOT ALLOWED
DELETE e FROM $e_{j}$ NOT ALLOWED
INSERT s IN $s_{k}$

PRECOND $\exists e_1\in e_p$

$$
\mathrm{s} \left[ \mathrm{L} _ {\mathrm{p}} \right] = \dot {\mathrm{e}} _ {1} \left[ \mathrm{L} _ {\mathrm{p}} \right]
$$

$$
\begin{array}{r l} \text { IMPLIES } & \{\text { INSERT } \quad \mathbf {e} _ {2} \text { IN } \mathbf {e} _ {j} | \\ & \quad \mathbf {e} _ {2} [ \mathrm{L} _ {j} ] = \mathbf {e} _ {1} [ \mathrm{L} _ {j} ] \} \end{array}
$$

DELETE s FROM $s_{k}$

$$
\begin{array}{l l} \text { IMPLIES   } \{\text { DELETE } & \mathrm{eFROM} \mathrm{e} _ {\mathrm{j}} | \\ & \mathrm{e} [ \mathrm{L} _ {\mathrm{j}} ] = \mathrm{s} [ \mathrm{L} _ {\mathrm{j}} ] \} \end{array}
$$

INSERT e IN $e_{p}$

No explicit behavior added.

$$
\begin{array}{l l} \text { DELETE   e   FROM   } e _ {p} \\ \text { IMPLIES   \{DELETE    s   FROM   } s _ {k} | \end{array}
$$

}

$$
\mathrm{s} \left[ \mathrm{L} _ {\mathrm{p}} \right] = \mathrm{e} \left[ \mathrm{L} _ {\mathrm{p}} \right] \}
$$

In the relational model above, the Employee-Project relation satisfies this requirement. Since the key of the Employee entity-set is E# and the key of the Employee-Project relation is E#, P#, the P# is the dangling key attribute. A new entity-set Project is created with its only attribute being the key attribute of P#. The Employee-Project relation is translated during this step. The entity-set Project has a many-to-many relationship (E-P) with the Employee entity. The constraints are added to the explicit behavior of the various objects.

Also now that a Project entity-set is created with key of P#, the D# of the Department-Project relation is a dangling key. Therefore, an entity-set called Department and a relationship called D-P are created and the appropriate explicit behavior is added.

## 8.3. The Many-to-Many Relationships

Now the search for the many-to-many relationships can begin by again examining the primary keys of the relations in R that have not yet been translated into entity-sets. The relations that are translated into many-to-many relationships have multiple attribute keys $(\mathbf{K}_{i}=(a_{1},\ldots,a_{n})$ where n>=2).

Step 4:

(a) If $\mathbf{e}_1, \mathbf{e}_2, \ldots, \mathbf{e}_n$ , $n > = 2$ , are some entity-sets and a relation $r_i$ exists whose key $K_i = L_1 U L_2 U \ldots U L_n$ (where $L_a \cap L_b = 0$ for $a \neq b$ and $l <= a$ , $b <= n$ ), then $r_i$ is translated into a many-to-many relationship $s_k$ (with key $L_k = K_i$ ) among the entity-sets $e_1, e_2, \ldots, e_n$ .

(b) B [ERCM] = B [ERCM] U

For $1 < = j < = n$

INSERT e IN $e_{j}$ No explicit behavior added.

For $1 < = j < = n$

DELETE e FROM $e_{i}$

$$
\text { IMPLIES } \{\text { DELETE   s   FROM   } s _ {k} \mid
$$

$$
\mathrm{s} _ {\mathrm{k}} \left[ \mathrm{L} _ {\mathrm{j}} \right] = \mathrm{e} \left[ \mathrm{L} _ {\mathrm{j}} \right]
$$

INSERT s IN $s_{k}$

$$
\begin{array}{c} \text { PRECOND } \exists e _ {n + 1} \in e _ {1} \\ \exists e _ {n + 2} \in e _ {2} \end{array}
$$

$$
\begin{array}{l} \exists \mathbf {e} _ {2 n} \in \mathbf {e} _ {n} \\ \text {s} [ \mathrm{L} _ {1} ] = \mathbf {e} _ {n + 1} [ \mathrm{L} _ {1} ] \\ \text {s} [ \mathrm{L} _ {2} ] = \mathbf {e} _ {n + 2} [ \mathrm{L} _ {2} ] \\ \cdot \\ \cdot \\ \cdot \\ \text {s} [ \mathrm{L} _ {n} ] = \mathbf {e} _ {2 n} [ \mathrm{L} _ {n} ] \end{array}
$$

DELETE s FROM, $s_{k}$ No explicit behavior added.

Our algorithm allows for many-to-many relationships greater than binary. An example of the binary case is

If $K_{1}=\{a_{1}, a_{2}\}$ is the key of $r_{1}$ and $e_{1}$ has as its key $L1=\{a_{1}\}$ and $e_{2}$ has as its key $L_{2}=\{a_{2}\}$ , then $r_{1}$ is translated into a many-to-many relationship $s_{1}$ between $e_{1}$ and $e_{2}$ in the ERCM.

In the relational model above, the Employee-Job relation meets this criteria. It is translated into a many-to-many relationship between the Employee and Job entity-sets. The corresponding constraints are added to the explicit behavior of the ERCM to maintain the referential integrity of the RDM.

## 8.4. The Many-to-One Relationships

The many-to-one relationships are translated next. If a set of attributes form a key of an entity-set in the ERCM and they also appear as non-key attributes in another entity-set of the ERCM, a many-to-one relationship is created.

Step 5:

(a) If the key of $\mathbf{e}_{\mathrm{j}}$ is $L_{j} = \{a_{1},\dots ,a_{n}\}$ , $n\geqslant = 1$ and $\{a_1,\ldots ,a_n\}$ are also nonkey attributes of $\mathbf{e}_k$ , then a many-to-one relationship $s_p$ created between $e_k$ and $e_j$ . The key of $s_p$ is $L_{p} = L_{k}$ .

(b) B [ERCM] = B [ERCM] U

$$
\begin{array}{l l} \{\text { INSERT   e   IN   e } _ {\mathrm{k}} \\ \text { IMPLIES   \{INSERT } & \text { s   IN   s } _ {\mathrm{p}} | \\ & \text { s } _ {\mathrm{p}} [ L _ {\mathrm{k}} ] = \text { e } [ L _ {\mathrm{k}} ] \} \end{array}
$$

DELETE e FROM $\mathbf{e}_{\mathbf{k}}$

IMPLIES {DELETE

$$
\begin{array}{l} \text { s   FROM } \mathrm{s} _ {\mathrm{p}} | \\ \mathrm{s} _ {\mathrm{p}} [ \mathrm{L} _ {\mathrm{k}} ] = e [ \mathrm{L} _ {\mathrm{k}} ] \end{array}
$$

INSERT e IN $e_{j}$ No explicit behavior added.
DELETE e FROM $e_{i}$

IMPLIES {DELETE s FROM $s_p$ }

$$
\begin{array}{l} \text {s FROM s_{p}} | \\ \text {s [L_{j} ] = e [L_{j} ]} \end{array}
$$

INSERT s IN $s_{p}$

PRECOND $\exists e_1 \in e_k$

$$
\begin{array}{l} \exists \mathbf {e} _ {1} \in \mathbf {e} _ {\mathrm{k}} \\ \exists \mathbf {e} _ {2} \in \mathbf {e} _ {\mathrm{j}} \\ \mathrm{s} [ \mathrm{L} _ {\mathrm{k}} ] = \mathbf {e} _ {1} [ \mathrm{L} _ {\mathrm{k}} ] \\ \mathrm{s} [ \mathrm{L} _ {\mathrm{j}} ] = \mathbf {e} _ {2} [ \mathrm{L} _ {\mathrm{j}} ] \end{array}
$$

DELETE s FROM $s_{p}$ No explicit behavior added.

In the example a many-to-one relationship is created between Employee and Location because Building#, Room# are attributes of the key of Location and non-key attributes of Employee.

## 8.5. The Inverse Translation of the Method Two Translation Algorithm

In order to meet the first goal of a translation algorithm and to show that the ERCM achieved via the translation algorithm we presented is equivalent to the original relational model given, we must show that there is an inverse translation algorithm which when applied to the ERCM will give us the same relational model back again. The inverse translation for the structure of the data is a modification of the inverse translation used in the discussion of the method one translation algorithm. If we were to directly, apply this algorithm to the ERCM, we would get the following relations:

Employee (E#, Name, Salary, Building#, Room#)

Employee-Project (E#, P#, Hours-spent)

Department-Project (D#, P#, Budget)

Job (J#, Description, Salary-Range)

Employee-Job (E#, J#)

Location (Building #, Room, Description, Capacity)

Project (P#)

Department (D#)

Notice that the only difference between this RDM and the original RDM are the two relations added for the dangling keys that were found. Therefore, we need to add a step to the inverse translation to handle the dangling key entity-sets created during the translation process. The following step will perform just such an inverse translation:

Inverse Step: If an entity-set $e_{j}$ was created from a dangling key, then do not translate it into a relation in the relational model. The $e_{j}$ is simply dropped during the inverse translation process.

The reason the inverse step will work and will not loose any information can be discovered by examining the explicit behavior of the ERCM. Notice that any weak entity-set $e_{j}$ created from a dangling key has constraints placed upon it that say that

\- No Inserts are allowed into the weak entity-set $e_j$ except for through the relationship with the strong entity-set.

\- Any inserts into the relationship $s_k$ has a precondition that the entry in the strong entity-set $e_n$ already exists and causes an insert into the weak entity-set $e_j$ .

\- A similar set of constraints is placed upon the deletion process of the relationship and the weak entity-set. (See the corresponding step for these constraints.)

Because of these constraints, if a value of the dangling key exists it has to exist in the relationship as well as in the weak entity-set. Exactly how the information is physically stored (i.e. not redundantly) is not a part of the ERCM.

The explicit behavior of the ERCM was translated from the inherent behavior of the RDM. Therefore, in the inverse translation process the explicit behavior of the ERCM will become inherent behavior in the relational model.

## 9. Conclusion

By translating the Inherent Behavior (static properties) of a SDM into Explicit Behavior (dynamic properties) of a DCM, we have shown that a wider flexibility can be provided to the database designers. Being more flexible becomes very important when modifying a Conceptual Model behavior. Being more flexible allows the behavior to be in the database designer's control and allows the behavior to be changed without the schema restructuring that would cause a change in the logical structure of the data. An added benefit of the CM is that it provides the database designer with more information about the current environment so that more knowledgeable decisions can be made during new database development process.

The ERCM is also provides an excellent communication tool between database designers, users, and programmers.

Although this paper is not about the qualities of various data models, some data models, such as the entity-relationship model are fairly easy to understand, since they do not insist upon many inherent constraints. This may be the reason for the popularity of these models since most of the constraints are within the Explicit Behavior and thus under direct control of the data designer and the administrator.

One point of note: We are not advocating that the explicit constraints be coded within application programs, as currently, but rather, that we expand our commercial database management systems to allow for the use of Explicit Behavior. This would be established at the time the database is designed. Moreover, these constraints could change without a major restructuring of the Schema.

We are continuing to study the CM-to-CM translation process. An algorithm needs to be developed to handle the translation of the source model's Explicit Behavior as well as its Inherent Behavior.

## Acknowledgements

We wish to thank Dr. Adarsh K. Arora for his guidance and suggestions in the writing of this paper.

## References

[1] Carlson, C.R. and Adarsh K. Arora, 'UPM: A Formal Tool for Expressing Database Update Semantics' Entity-Relationship Approach to Software Engineering, Proceedings of the Third International Conference on Entity-Relationship Approach, North Holland, NY, 1983, pp. 517–526.

[2] Casanova, Marco A. and Jose Eduardo Amarel de Sa, 'Designing Entity-Relationship Schema, for Conventional Information Systems', Entity-Relationship Approach to Software Engineering, Proceedings of the Third International Conference on Entity-Relationship Approach, North Holland, NY, 1983, pp. 265–278.

[3] Chen, P. The Entity-Relationship Approach to Logical Database Design, Q.E.D., Wellesley, MA, 1977.

[4] Codd, E.F. 'Extending the Database Relational Model to Capture More Meaning' ACM TODS Vol. 4:4, December 1979, pp. 397–434.

[5] Davis, Kathi Hogshead and Adarsh K. Arora, 'AUGUST: An Experimental Expert System to Translate a Conventional File System into a Commercial Database System' Proceedings of the IEEE COMPSAC, Chicago, IL, IEEE Computer Society, Los Angeles, CA, October 1985.

[6] Davis, Kathi Hogshead and Adarsh K. Arora, 'A Methodology for Translating a Conventional File System into an Entity-Relationship Model', Proceedings of the Fourth International Conference on Entity-Relationship Approach, IEEE Computer Society Press, Chicago, IL, October 1985, pp. 148–159.

[7] Davis, Kathi Hogshead and Adarsh K. Arora, 'Converting a Relational Database Model into an Entity-Relationship Model' Proceedings of the Sixth International Conference on Entity-Relationship Approach, November 1987, pp. 243–258.

[8] Korth, Henry F. and Abraham Silberschatz, Database System Concepts, McGraw Hill, 1986.

[9] Navathe, S.B. and A.M. Awong, “Abstracting Relational and Hierarchical Data with a Semantic Data Model”, Proceedings of the Sixth International Conference on Entity-Relationship Approach, November 1987, pp. 277–305.

[10] Nilsson, E.G., 'The Translation of a COBOL Data Structure to an Entity-Relationship Type Conceptual Schema', Proceedings of the Fourth International Conference on Entity-Relationship Approach, IEEE Computer Society Press, Chicago, IL, October 1985, pp. 170–181.

[11] Tsichritzis, Dionysios C. and Frederick H. Lochovsky, Data Models, Prentice-Hall, Englewood Cliffs, NJ, 1982.

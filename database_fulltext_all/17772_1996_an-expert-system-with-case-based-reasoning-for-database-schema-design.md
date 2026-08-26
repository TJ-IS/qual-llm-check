---
otero_id: 17772
otero_key: "RMNDSHX4"
title: "An expert system with case-based reasoning for database schema design"
authors: "Yong-Kee Paek; Jungyun Seo; Gil-Chang Kim"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(96)00020-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An expert system with case-based reasoning for database schema design

Yong-Kee Paek $^{*}$ , Jungyun Seo, Gil-Chang Kim

Department of Computer Science and Center for Artificial Intelligence Research, Korea Advanced Institute of Science and Technology, 373-1 Gusong-Dong, Yusong-Gu, Taejon, Korea

## Abstract

In this paper, we present a Design Expert System for Database Schema (DES-DS) based upon case-based reasoning. Instead of maintaining only domain cases for designing a target database schema, the proposed system relies on two case-bases that consist of a Domain Dependent Case-Base (DDCB) and a Domain Independent Case-Base (DICB). For this approach, we propose a Relational Conceptual Graph (RCG) to represent the users' design specification and each case in the case-bases. The details of the system architecture, organization of the case-bases, reasoning rules, and system flow are also described.

Keywords: Database schema design; Case-based reasoning; Expert system; Artificial intelligence

## 1. Introduction

Case-Based Reasoning (CBR) systems [12,17] solve problems by using knowledge gained from solving similar problems in the past. Major activities of such systems include retrieving relevant previous cases, adapting and combining them to solve new problems, and recording failures so that they can be avoided in the future. Applications of CBR techniques include story understanding, explanation-based reasoning, adaptive planning, learning and architectural design.

It has been demonstrated that artificial intelligence technology can play an important role in the implementation of design automation $[3,10,11,14,19]$ . The majority of present expert systems encode their knowledge as a large set of domain specific rules. However, there are many situations where the use of such rules does not accurately model the problem-solving strategies used. Generally, human designers appear to solve design problems not by reasoning from the primitive components available in the design domain, but by adapting the design cases of previously encountered artifacts. In some complex problem domains, such as the database schema design, the design tasks need human cognition and judgment in many cases. The solutions are fine-tuned through much experience and modeling techniques by experts.

Much of the design activity in the real-world seems to be case-based. Traditionally, database design has relied on human experience and judgment rather than mechanistic algorithms. For example, when a user designs a schema for one form at a time, the user finds a similar form schema and repairs it appropriately to meet the design requirements. Thus, it needs much experience and knowledge about design techniques.

There are several works in database schema design automation. None of them, however, use case-based reasoning techniques. Most research in the database design area is based on an E-R model or adapts a rule-based approach $[7,8,13,18]$ .

The most important steps during the early stages of the database schema design are conceptual design and logical schema design. At the conceptual design step, a database designer analyzes the requirements of the operation of an application (or organization) and then defines the logical structure of a database to satisfy those requirements at the logical schema design step. In defining the conceptual model, the designer should identify the entities that the database is to contain and the relationships among those entities [6]. Traditionally, it has been thought to be easy for the designer to describe the design requirements of a database through input/output forms by using natural language. From our experience, we came to conclude that specifying the design requirements using printed report forms, called form-oriented approach [7], is one of the most convenient methods for users. In designing a logical schema, all identified entities and relationships need to be transformed into relations for the relational database model [5].

With the form-oriented approach in conceptual design, we view the process of designing a logical schema as consisting of the following steps:

\- Design of each form schema: Takes the requirements for each form in natural language, extracts the information for data modeling, normalizes the form data model to guarantee the 3rd Normal Form (3NF), and produces the form schema as a form of the Data Structure Diagram (DSD).

\- Design of an application schema: Integrates each form schema into an application DSD as a conceptual schema.

\- Design of a relational schema: Transforms the application DSD into a relational schema as a logical model by using trivial rules.

Our approach for the use of case-based technology for designing a real-world database schema has made us aware of three important considerations. First, design requirements in real-world application tend to be changed dynamically because designers cannot completely formulate the design requirements at the beginning stage of schema design. Rather, they are evolving. Second, a database schema should be normalized to preserve data integrity and consistency. The normalization theory is based on the observation that a certain set of relations has better properties in an inserting, updating, and deleting environment than do other sets of relations containing the same data [2]. Third, an automatic database schema design method should be general enough for various application domains. To achieve such generality, it must have domain independent knowledge for database schema design and learning capability for more efficient ways of extending domain dependent knowledge (i.e., domain dependent cases).

The proposed Design Expert System for Database Schema (DES-DS) applies the two kinds of methods to the database design work. First, when there exists a similar design case in Domain Dependent CaseBase (DDCB), the target database schema is designed by using the similar case with a few modifications. Second, when there is no similar case, the target database schema is designed by using only domain independent, general normalization techniques.

In the next section, we describe the architecture and overall design flow of DES-DS. The Relational Conceptual Graph (RCG) which is an internal representation scheme to describe the dependency structure among related attributes; design using a DICB; design using a DDCB are described in Section 3, Section 4, and Section 5, respectively. In Section 6, we briefly review some related works. Section 7 concludes the paper and points out some important issues to future research.

## 2. Architecture and design flow of DES-DS

DES-DS consists of four major modules, and two kinds of case-bases. The modules are User Interface, RCG Translator, Case Retriever, and Schema Designer. The case-bases are DICB and DDCB. Fig. 1 shows the system architecture and the relationships among these system components.

![](/api/attachments/RMNDSHX4/fulltext/images/6b69452fc435741e08deb48f3a37efbf7157d44e88b6721aec9534c222475636.jpg)  
Fig. 1. DES-DS architecture.

The User Interface module provides interactive question-answering functions. It takes the users' requirements for database schema design, asks the user for specific information, accepts the answer, presents the schema description, and shows the designed logical schema. The interaction between the system and user is performed by using natural language sentences, form layout, and diagram.

The RCG Translator transforms natural language input sentences for the specifications of requirements into a RCG. Since natural language processing is beyond the scope of this paper, we will not discuss the details of the RCG translator in this paper.

The Case Retriever selects a similar case in DICB or DDCB. This module performs the following functions: searches for the relevant case by navigating a hierarchical case tree in DDCB through user interaction, calculates similarity to select the relevant cases, maintains a list of relevant cases, presents the best similar case to the schema designer module, and matches a RCG with the description of a case in DICB when there is no similar case in DDCB.

The Schema Designer takes a relevant case and performs design actions described in the case. In design using DDCB, this module presents the content of a selected form case to a user, such as form layout and form schema description in natural language. The user can request the modification of the form-case to the system. In design using DICB, it performs the normalization process through iterative case matching and user interaction.

The case-base consists of two case-bases: DICB and DDCB. DICB includes normalization cases for guaranteeing the 3NF. DDCB is a set of cases for an application database schema. DDCB is well organized as a hierarchical case tree.

![](/api/attachments/RMNDSHX4/fulltext/images/31b3be632349720c82b6575ac5cf443ea8cf55faca8e97baf8ee05880b7cf72f.jpg)  
Fig. 2. Database design flow of DES-DS.

A database design flow in DES-DS is illustrated in Fig. 2. At the beginning, DES-DS retrieves the similar design case by matching the design characteristics with the descriptions of cases in DDCB. If a similar case exists in DDCB, the system uses the case to design the application schema. If a similar case does not exist in DDCB, DES-DS designs the application schema by using DICB.

## 3. Relational conceptual graph

Traditionally, it has been thought to be easy for users to describe design requirements of database schema through input/output forms. From our experience, we came to conclude that specifying the requirement of printed report forms, called form-oriented approach [7], is one of the most convenient methods for naive users. For example, let us consider DES-DS's processing of a sample report form in a university administration (Fig. 3).

In this approach, a user explains the design requirements and the dependency among the attributes in a form by using natural language sentences. One possible explanation of the form in Fig. 3 is the following.

![](/api/attachments/RMNDSHX4/fulltext/images/cc663295dc7378156bd9a83b1ec0e57b35feb117f8954043a7108e004d41d524.jpg)  
Fig. 3. An example report form.

"In a given SEMESTER and for a given COURSE-NO (number of course) there is only one COURSE-TITLE, one NAME-INSTR (instructor teaching the course), one CAMPUS, one DAY-TIME, and one ROOM-NO where the COURSE-NO will be taught. But there may be a number of COURSE-NO with the same COURSE-TITLE. The same INSTR may be teaching a number of COURSE-NO in a SEMESTER, and a number of COURSE-NO may be taught on a specific CAMPUS in a specific SEMESTER at the same DAY-TIME and in the same ROOM-NO."

Design requirements described in natural language sentences should be transformed into internal structures to be processed by a computer system. Therefore, we need an internal representation scheme for describing the requirement sentences that mostly express the dependency among the attributes in a form.

A Relational Conceptual Graph (RCG) is an internal representation scheme to describe the structure of dependency among related attributes. A RCG consists of concept nodes and relation nodes. Concept nodes represent tentative-key attributes or non-key attributes, and relation nodes show how the attributes are inter-related. A concept node consists of the concept type either TENTATIVE-KEY or ATTRIBUTE and a referent that is a data element name. A concept node may have multiple referents using a set notation represented by curly brackets. We call such concept a set ATTRIBUTE or a set TENTATIVE-KEY according to the type of the concept. A relation node represents the relationship between TENTATIVE-KEY and non-key attributes. The types of relationship are $(1-1)$ for one-to-one relationship, $(1-M)$ for one-to-many, and $(M-1)$ for many-to-one. The many-to-many relationship can be represented as the combination of $(1-M)$ and $(M-1)$ . We call the relation and ATTRIBUTE concept a relationship subgraph. Normally, a RCG needs two relationship subgraphs. For example, Fig. 4 shows a RCG that has meaning for the requirement sentence “For a given STUDENT-NO there is only one STUDENT-NAME, STATUS. There can be many STUDENT-NO with the same STATUS.”

![](/api/attachments/RMNDSHX4/fulltext/images/1a919fda7c18cf5ac6a5b9e386f9500db572d34f3ebb4804615ff23d0e972d38.jpg)  
Fig. 4. An example RCG.

With the above requirement sentence, DES-DS identifies attributes' names shown as capital letters, and extracts the concept type and relations using objective clue words such as "for a given", "only one", "many", etc. By means of usual natural language understanding methods [1], requirement sentences can be translated into RCGs as a general form. To implement the RCG translator practically, it needs a more powerful natural language understanding system being able to recognize similarity among different data item names in realistic information models. Developing a powerful natural language processing system, however, is beyond the scope of this paper.

In designing the database schema, all RCGs for requirement sentences specified with a form are merged into Merged RCG (MCG) as follows [15]: unifying the RCGs that have the same TENTATIVE-KEY and ATTRIBUTE, merging the referents of ATTRIBUTE that has the same relation node within a RCG, and finally combining the RCGs that have partial key dependency into a RCG of COMPOSITE-KEY type that is composed by using the key words COMPOSITE-KEY and relation (PART).

For example, let us illustrate how the following four RCGs, (RCG-3-1), (RCG-3-2), (RCG-3-3), and (RCG-3-4), with corresponding requirement sentences can be merged into a merged RCG like the following:

"In a given SEMESTER and for a given COURSE-NO (number of course) there is only one COURSE-TITLE, one NAME-INSTR (instructor teaching the course), one CAMPUS, one DAY-TIME, and one ROOM-NO where the COURSE-NO will be taught."

(RCG-3-1):

[TENTATIVE-KEY: {SEMESTER, COURSE-NO}] -

```txt
(1-1) → [ATTRIBUTE: {COURSE-TITLE, NAME-INSTR, CAMPUS, DAY-TIME, ROOM-NO}]
```

"But there may be a number of COURSE-NO with the same COURSE-TITLE."

```snap
(RCG-3-2):
[ATTRIBUTE: COURSE-TITLE] -
(1-M)→ [ATTRIBUTE: COURSE-NO]
```

"The same NAME-INSTR may be teaching a number of COURSE-NO in a SEMESTER,"

```txt
(RCG-3-3):
[ATTRIBUTE: NAME-INSTR] -
(I-M)→ [ATTRIBUTE: {COURSE-NO, SEMESTER}]
```

"and a number of COURSE-NO may be taught on a specific CAMPUS in a specific SEMESTER at the same DAY-TIME and in the same ROOM-NO."

```txt
(RCG-3-4):
[ATTRIBUTE: {CAMPUS, DAY-TIME, ROOM-NO}] - (I-M) → [ATTRIBUTE: {COURSE-NO, SEMESTER}]
```

(RCG-3-3) and (RCG-3-4) can be easily merged into (RCG-3-[3 + 4]) by adding the attribute NAME-INSTR to set ATTRIBUTE in (RCG-3-4) because relationship subgraphs in two RCGs are identical.

```javascript
(RCG-3-[3+4]):
[ATTRIBUTE: {NAME-INSTR, CAMPUS, DAY-TIME, ROOM-NO}] - (1-M) → [ATTRIBUTE: {COURSE-NO, SEMESTER}]
```

(RCG-3-[3 + 4]) and (RCG-3-1) can be combined into (RCG-3-[1 + 3 + 4]) because attributes in concept nodes, [TENTATIVE-KEY: {SEMESTER, COURSE-NO}] and [ATTRIBUTE: {COURSE-NO, SEMESTER}], are identical.

```txt
(RCG-3-[1+3+4]):
[TENTATIVE-KEY: {SEMESTER, COURSE-NO}] - (1-1) → [ATTRIBUTE: {COURSE-TITLE, NAME-INSTR, CAMPUS, DAY-TIME, ROOM-NO}]
(M-1) ← [ATTRIBUTE: {NAME-INSTR, CAMPUS, DAY-TIME, ROOM-NO}]
```

Since the attribute COURSE-TITLE is partially dependent on an attribute COURSE-NO, the RCG (RCG-3-2) and (RCG-3-[1 + 3 + 4]) are combined as the MCG-3 in Fig. 5 with partial key dependency. The RCG with partial key dependency is composed by using the concept type COMPOSITE-KEY and relation (PART).

```txt
MICG-3.
[[COMPOSITE-KE1] -
(PART) → [TENTATIVE-KE1: SEMESTER]
(PART) → [TENTATIVE-KEY: COURSE-NO] -
(M-I) → [ATTRIBUTE: COURSE-TITLE]] -
(I-I) → [ATTRIBUTE: {COURSE-TITLE, NAME-INSTR,
CAMPUS, DAY-TIME, ROOM-NO}]
(M-I) → [ATTRIBUTE: {NAME-INSTR, CAMPUS,
DAY-TIME, ROOM-NO}]
```  
Fig. 5. An example of a Merged-RCG.

## 4. Design using a domain independent case-base

Human experts have the design knowledge about how a database schema should be normalized. Such design knowledge is domain independent and can be represented as a set of rules or cases. In this research, since the DDCB is organized as a set of cases for previous designed schemas, we also represent the normalization knowledge as a set of cases rather than rules to apply a same technique (i.e., case-based reasoning).

The DICB is a set of cases for normalizing the RCG set. Each case in the DICB consists of description, outcome, and actions. The description in a case is a RCG that violates the 1NF, 2NF, 3NF or guarantees the 3NF. The outcome is a relational model normalized as a logical schema. The actions consist of a sequence of the action rules for normalization, such as an inquiry for more information, confirmation for the 3NF, etc. A design case may contain several different types of description. In the DICB, currently there are only nine cases as follows:

DICB-1: Many-to-many mapping with partial key dependency.

DICB-2: Many-to-many mapping with transitive dependency.

DICB-3: Many-to-many mapping with full functional dependency.

DICB-4: One-to-one mapping with partial key dependency.

DICB-5: One-to-many mapping with partial key dependency.

DICB-6: One-to-one mapping with transitive dependency.

DICB-7: One-to-many mapping with transitive dependency.

DICB-8: One-to-one mapping with full functional dependency.

DICB-9: One-to-many mapping with full functional dependency.

The cases from DICB-1 to DICB-3 represent cases of violating the 1st Normal Form (1NF). If any RCG can be matched with those cases, the system is aware of the graph that violates the 1NF and takes actions specified in each case. The outcomes of the actions are revised graphs which guarantee, at least, the 1NF. Similarly, the cases DICB-4 and DICB-5 are cases for the graphs which may violate the 2nd Normal Form (2NF), and DICB-6 and DICB-7 are for the 3NF. DICB-8 and DICB-9 are the cases which guarantee the 3NF. Therefore if any graph can be matched to those cases, the graphs are guaranteed to satisfy the 3NF. For the normalization, each RCG is matched with each case in DICB, and the case retriever selects the similar cases by similarity order. When a RCG is normalized, the schema designer module transforms it into the RCGs of higher normal form by using the actions specified in each case. The transformed RCGs are appended to a RCG-set. The process does the same step with the RCGs in the set iteratively until they are exactly matched with DICB-8 or DICB-9.

The cases from DICB-1 through DICB-7 represent violating normal forms. These seven cases are based on the definition of the 1NF, 2NF, and 3NF. Therefore these seven cases are general enough to cover all RCGs which violate the 1NF, 2NF, or 3NF. The cases DICB-8 and DICB-9 are also based on the definition of the 3NF to confirm normalized cases. These two cases are the one and only cases which can confirm RCGs in the 3NF.

Let us illustrate the process with an example. The content of case DICB-5 is shown in Fig. 6. The DICB-5 consists of three parts: Description, Outcome, and Actions. The description of DICB-5 represents a case of a RCG that violates the 2NF. The description means that the attribute “attr-set-3” is partially dependent upon the partial key “key-set-1”. The constraints mean that they must satisfy the condition before processing the actions in the case. The actions are for transforming the violating RCG into the RCGs in the outcome to guarantee the 2NF. The relation node (ANY1) and (ANY2) are anonymous relation nodes that can be matched with any kind of relation node during case matching. When the outcome is produced, the relation node (ANY1) and (ANY2) are instantiated as the original relation node. After processing the actions, the schema designer module instantiates the original symbols and produces the outcome as decomposing the input RCG into two RCGs guaranteeing the 2NF.

![](/api/attachments/RMNDSHX4/fulltext/images/adb645233f0d9af196b189e3cddfe5e133dc7d7652677802f99eba12e4a504cc.jpg)  
Fig. 6. Content of DICB-5.

Actions in each case consist of a proper combination of the following steps.

\- Step-IIR (Inquiry for confirmation of Insufficient Requirement): When subgraphs lack some of the relationship, DES-DS asks the user to confirm the insufficient information.

\- Step-IER (Inquiry for confirmation of Excess Requirement): When more than two relationship subgraphs exist, DES-DS asks the user to confirm the exceeding information.

\- Step-IPD (Inquiry for confirmation of Partial key Dependency): To guarantee the 2NF, DES-DS asks the user to confirm whether the partial key dependency exists or not.

\- Step-ITD (Inquiry for confirmation of Transitive Dependency): To guarantee the 3NF, DES-DS asks the user to confirm whether the transitive dependency exists or not.

\- Step-IDA (Inquiry for confirmation of Different Attribute set): When two sets of ATTRIBUTES in one RCG are different, DES-DS asks the user to confirm whether some attributes are omitted or not.

\- Step-PIK (Process for finding the Inferred Key elements): When a RCG has a many-to-many relationship, it should be transformed into a RCG that has a one-to-many relationship because it violates the 1NF. It is possible to transform into the 1NF by appending the candidate tentative-keys in non-key attributes to the current tentative-key set. To find the candidate tentative-keys in non-key attributes, DES-DS uses some heuristics as follows. If some non-key attributes have been used as tentative-keys of another RCG, DES-DS selects the attributes as candidate tentative-keys for this RCG. If there are no such attributes, DES-DS selects the attributes that have been used in other RCGs. DES-DS asks the user to confirm whether it is possible to do that. When such heuristics cannot be applied, DES-DS should request the proper attributes of the user.

Case matching (i.e., selecting relevant cases) is done by graph matching algorithms. In case matching, our system calculates the similarity score to measure relevancy. The similarity score is a sum of weighted scores of matched subgraphs. These relevant cases are presented to the schema designer module in order of the score. In case of partial matching, the schema designer requests the user for more specific information. This information is appended to the RCG, and the RCG is matched with the DICB again. Upon exact matching, the schema designer generates outcomes in the 3NF. DES-DS maintains the matching history to identify what kinds of cases have ever been matched with the RCG. If the RCG is first matched with DICB-8 or DICB-9 without matching with any other cases, the system should ask the user to confirm whether the RCG guarantees the 1NF and 2NF with very easy natural language descriptions. After all RCGs are processed, DES-DS produces a normalized conceptual schema for each form of the form schema. DES-DS can also generate the schema for the target application as a merging normalized-RCG (NCG) set for all forms. The final NCG set, as an application schema, is indexed to a DDCB to be used to design similar databases later. For designing the logical schema, DES-DS translates each NCG of the conceptual schema into Data Description Language (DDL) of relational DBMS, such as ANSI/SQL.

For example, in MCG-3 of Fig. 5, case matching and reasoning processes are as follows:

At the first step, the case retriever selects relevant cases in order of similarity such as DICB-5, DICB-6, and DICB-7. These cases are not exactly matched, but partially matched. First, the case reasoner inquires of user for acquiring supplementary information by Step-IIR (“For a given COURSE-NO there is only one COURSE-TITLE, isn’t there?”). If the user’s answer is “Yes”, add following RCG to RCG set.

New-RCG:

[TENTATIVE-KEY: COURSE-NO] -

(1-1)→[ATTRIBUTE: COURSE-TITLE]

After the New-RCG is merged with the prior MCG-3, a new MCG-3 is generated. The system records the matching history “(DICB-5, IIR)”.

Second, after merging and combining again, the system asks the user to confirm whether partial key dependency exists, because it is known that the COURSE-TITLE exists in a dependent attribute set. With a “No” answer from the user, the system removes the partial key dependency relationship subgraph. Then, the case retriever presents the next case DICB-5 to the case reasoner.

Third, the system asks the user to confirm whether there are any omitted attributes (e.g., “Does the same COURSE-TITLE have different COURSE-NOs in a SEMESTER, or doesn’t it?”). With a “Yes” answer, the system merges and combines again, and inquires whether transitive dependency exists or not. If the user’s answer is “No”, the system saves the outcome into a NCG set after instantiating. Otherwise, the system accepts sentences for more supplementary information, and performs the case reasoning process again. This, NCG-3, is the final outcome saved into NCG set:

NCG-3:

$$
\begin{array}{l}\text {[ K E Y : \{\text { SEMESTER,   COURSE - NO } \} ] -}\\\quad (M - 1) \rightarrow [ \text { ATTRIBUTE:   \{\text { COURSE - TITLE,   NAME - INSTR, }}\\\quad \text { CAMPUS,   DAY - TIME,   ROOM - NO } ] ]\end{array}
$$

Each NCG can be considered as a table of the relational database model. The set of final NCGs can be considered as a final relational database schema. Briefly, design using DICB is iterative work which matches the RCG with cases and corrects the RCG until satisfying the 3NF.

## 5. Design using a domain dependent case-base

In DES-DS, the design task is performed by selecting the relevant previous cases, adapting it to users' requirements, repairing it for new solutions, and indexing the new solution into a DDCB. The DDCB, case memory, is well organized as a hierarchical case tree. The relevant cases are retrieved by calculating the similarity to measure the relevancy of domain and form features. Case adaptation is a process that builds a rough solution merging the relevant cases. The rough solution is modified by repairing the missing or incorrect part by using a DICB to guarantee the 3NF (3rd Normal Form). The new schema is added to the DDCB as a new case.

Specifying the design requirements is based on a report form. From our experience, we came to conclude that specifying the design requirements using printed report forms is one of the most convenient methods for users. The design requirements for a form are described by using pre-defined tabular forms [7]. From users' requirements, the system identifies two kinds of design features that consists of domain features and form features.

## 5.1. Memory organization of DDCB

DDCB is well organized as a hierarchical case tree as shown in Fig. 7. All cases are hierarchically organized to form a partially ordered graph to help the system to reduce its search space. Linking the cases into a well-defined hierarchy will facilitate modification of the case-base through addition of a new case and case abstraction.

![](/api/attachments/RMNDSHX4/fulltext/images/42e7b34616fea331530ebdbbdfef0b03c2ec30d1dbc991b86634f59a2acb4ae3.jpg)  
Fig. 7. Organization of DDCB.

![](/api/attachments/RMNDSHX4/fulltext/images/7459b614133461559dc0871d4a0d7a24de79f72c1a5d0e3ee032e5b0272761bd.jpg)  
Fig. 8. An example of a domain-case hierarchy.  
abstraction node. An example of a form-case node at the leaf level is illustrated in Fig. 9.

The upper part of the case hierarchy resembles a conceptual is-a hierarchy. We call each node in the upper hierarchy a domain-case. Each domain-case has its identifier, domain features, and a brief description of the domain it represents. Domain features are organization (e.g., university, bank, ...), management resource (e.g., student, money, ...), and use of the form (e.g., update, reporting, ...). Every domain-case node in memory will be an index for available designed form cases. Domain-case nodes with the same features are abstracted as a higher level abstraction node. Fig. 8 shows an example of a domain-case abstraction hierarchy. For example, in the university and company domain, there are several domain-nodes such as [University, Manpower,], [Company, Manpower,], etc. Since the domain-node [University, Manpower] has a similarity with the domain-node [Company, Manpower,], those two domain-nodes can be regarded as subdomains of the more general domain-node called [,Manpower,].

Below the hierarchy of domain-cases, there are form-case hierarchies. Since this system assumes a form-oriented approach to schema design, a well-organized form-case hierarchy is very important. Each domain-case can have many form-cases. Each form-case can have several sub-form-cases. Each form-case consists of form features, the description, and the layout of the form-case. Form features, which describe the structure of the form, are entities, attributes, the form type (e.g., table), utilization degree that represents the degree of references of the case, and the form name. Form-case nodes with the most similar features are grouped as a higher level

The lowest part of the DDCB hierarchy consists of form-DSDs (Data Structure Diagrams) as instances of the design case [16]. Each form-DSD represents a set of NCGs (Normalized RCGs) for the entities and attributes appearing in the form. An example of a form-DSD is shown in Fig. 10. The column “Level” indicates the hierarchical level of the relations. We regard the level 1 relations as entities and the subsequent level relations as relationships. The column “NCG-Description” indicates the description of the relation which is described as a NCG form. In the example of Fig. 10, the relation Student is an entity that has the many-to-one dependency key STUDENT-NO with non-key attributes STUDENT-NAME, STATUS, MAJOR, MINOR, and FACULTY-ADVISOR.

## 5.2. Case retrieval

The retrieval process tries to match the domain-case level first, and the form-case level afterwards. In traversing the domain-case hierarchy, the system selects the domain-case nodes with the most identi-

<table><tr><td>Feature</td><td>Value</td></tr><tr><td>Entity</td><td>Student. Semester. Course</td></tr><tr><td>Attribute</td><td>Student-No. Student-Name, Semester. Course-No</td></tr><tr><td>Form-Type</td><td>Table</td></tr><tr><td>Util-Degree</td><td>0.8</td></tr><tr><td>Form-Name</td><td>Student Schedule List/Semester</td></tr></table>

Fig. 9. An example of a form-case node.

cal domain features by using breadth-first search method. A purpose for selecting the most identical domain-case nodes is to reduce the search space for selecting the similar form-cases efficiently. After reducing its scope into the form-case level, the system searches the most similar form-case node (i.e., form-DSD). In searching the form-case hierarchy, since a form feature has many feature values, the system calculates the similarity of a form-case to select the most similar form-DSD. The similarity is calculated as the weighted sum of scores with matched form features as follows:

$$
\operatorname{Sim} = \sum_ {i = 1} ^ {n} \left(W \times S _ {i}\right),
$$

where:

$$
\begin{array}{l l} W \colon & \text { Weight   for   each   feature, } \\ S _ {i} \colon & \text { Score   for   matched   features. } \end{array}
$$

We set the weight for each feature intuitively. For example, feature “entity” has a larger weight value than feature “attribute”, since “entity” as a conceptual component is more important than “attribute” as an element of a form. We are still investigating for a more mechanical method to assign weight to each feature. We are planning to define weight after constructing a sufficiently large case-base. The system keeps form-DSDs in the order of similarity value. We call the most similar form-DSD the “Best-Form-DSD”. We ignore the form-DSDs of which similarity is less than some threshold value. In this case, DES-DS switches the design control to the design process using DICB.

## 5.3. Adapting cases

The selected cases may not exactly match with the user's requirements. Adaptation rules are needed to find the gaps and to fill the missing parts [19]. To generate a rough solution, the system processes the following two steps:

1. Merge the relevant form-DSDs selected by the case retriever.

2. Remove unnecessary components (entities, attributes) by comparing the design requirements.

First, the merging action is started by appending the necessary entities in partial matched form-DSDs to the Best-Form-DSD. For example, to design the schema for a form “Student Schedule List/Semester”, the system appends the entity “Course” in a partially matched form-DSD “Course Catalog” to the Best-Form-DSD “Course Registration List”. Next, the system removes the entities or attributes that have not been referenced in users’ requirements.

The generated rough solution has all entities and attributes that are included in previous cases. The system, however, does not have the entities and attributes that do not exist in the previous cases. Furthermore, it does not consider a correctness of the relationships among attributes, either. They will be considered in the solution refinement phase.

## 5.4. Explanation and solution refinement

The system briefly explains the overall design status to help the user to identify the design process, rough solution, design deficiency, and comments to aid the solution refinement.

<table><tr><td>Relations</td><td>Level</td><td>NCG-Description</td></tr><tr><td>Student</td><td>1</td><td>{KEY: STUDENT-NO} - (M-1) → [ATTRIBUTE: {STUDENT-NAME, STATUS, MAJOR, MINOR, FACULTY-ADVISOR}]</td></tr><tr><td>Semester</td><td>1</td><td>{KEY: SEMESTER} - (I-1) → [ATTRIBUTE: {DSTRTSEM, DENDSEM}]</td></tr><tr><td>Course</td><td>1</td><td>{KEY: COURSE-NO}</td></tr><tr><td>Course/Semester</td><td>2</td><td>{KEY: {SEMESTER, COURSE-NO}} - (M-1) → [ATTRIBUTE: {COURSE-TITLE, CAMPUS, NAME-INSTR, DAY-TIME, ROOM-NO}]</td></tr><tr><td>Grade</td><td>3</td><td>{KEY: {SEMESTER, COURSE-NO, STUDENT-NO}} - (M-1) → [ATTRIBUTE: CREDITS]</td></tr></table>

Fig. 10. An example of a form-DSD.

![](/api/attachments/RMNDSHX4/fulltext/images/f6bbe0dab1c88fbc4db63127e9ef5558ebf2607d49320458b7a1db4e1bafd2df.jpg)  
Fig. 11. An example of a design status report.

In explaining the rough solution, the system describes the solution as tabular representation, such as Fig. 10, that consists of relations and description. Each relation may be an entity or a relationship in the E-R model [6]. A description is a RCG that illustrates the relationships among attributes in that relation. An example of a design status report is shown in Fig. 11.

After generating a domain specific explanation for the missing parts of the requirements in a rough solution, the system interacts with the user for repairing the missing parts of the solution.

The system normalizes the modifications by using DICB and merges them into the rough solution. We have proposed an idea for the design using a DICB [15]. If the user confirms the correctness of the final solution that meet the users' requirements completely, the system accepts the attribute of each field in the relation, such as data-type, length, range, value-constraints, default-value, and null. The system generates a DDL (Data Definition Language) source for relational DBMS.

## 5.5. Case learning

Case learning in DDCB consists of two steps: adding a new case and reorganizing the case hierarchy by case abstraction. To add a new case into the DDCB, the system identifies the indexing terms for the added or modified domain features and form features. Then, it modifies the abstraction hierarchy for reflecting the identified indexing terms.

New abstractions are formed when a number of cases are discovered to share a common set of features. The common features are used as indices to the original cases. This is called similarity-based generalization [17]. A generalization is worth forming if there are enough instances with enough features in common, where “enough” was defined by thresholds. Forming new abstractions simply on the basis of shared features is not a very good technique. A good index for case-based reasoning is distinctive but not unique. The most useful features to use for indexing are the features shared by many instances in memory as a whole, but by only a few of the instances. We still did not set such threshold value for abstraction, since we need to build a sufficiently large case-base to experiment.

## 6. Related work

In this section, some related works for design application using case-based reasoning and for database design automation are briefly reviewed. Unfortunately, to the best of our knowledge, no attempts have been made to exploit case-based reasoning as methodology for database design automation.

Applications of case-based reasoning in design include weld-process design [14], conceptual design of office building [10], conceptual design of hydro-mechanical systems [19], menu design of a meal [11], and autoclave layout design [3]. These works, however, are only based on a domain specific case-base.

There are several works in database schema design automation. None of them, however, uses case-based reasoning techniques. Korczak [13] proposed a database schema design system using a rule-base; database design knowledge which is divided into a declarative part (containing a description of entities, relationships and attributes) and a procedural part (defining design operations). Ruoff [18] developed an expert system prototype that assists a database designer in defining a conceptual schema of a database using the IDEF1 modeling rules and heuristics. Dogac [8] developed a Generalized Expert System for Database Design (GESDD) that consists of an expert system for generating methodologies for database design, called ESGM, and an expert system for database design, called ESDD. GESDD assumes the Entity-Relationship (E-R) model [6] for modeling the conceptual schema. Thus, the designer should identify the entities and relationships in the application domain. Choobineh [7] proposed a form model and an Expert Database Design System (EDDS) that analyzes instances of the form model to derive a conceptual schema. The user paints the form on the screen, and the form definition system originates a conversation to capture the form-schema. This system derives an E-R diagram by analyzing a collection of forms.

A number of other researchers have reported works on the natural language inputs for database design. Bouzeghoub and Gardarin [4] report the implementation of an expert system which uses quasi natural language to drive a relational schema in the 3NF. Eick [9] reports a similar approach based on the natural language inputs from different user groups and the conversation with the designer.

Most of research in the database design area are based on an E-R model. However, for a naive designer, it is hard to identify the entities and relationships in his/her enterprise. The database design method based on a form model is more powerful and convenient than the E-R model for naive users, since the users do not need to define the conceptual schema for their enterprise. Our work extends these works by allowing users to describe design requirements in natural language, by normalizing the conceptual schema by using case knowledge, and especially by using the domain dependent case-base for similar database design.

## 7. Conclusion and future work

In this paper, we presented a case-based reasoning approach to develop an expert system for database schema design automation. We also defined RCG formalism to represent the entities appearing in user's design requirement and the relations among them.

The system uses a DDCB to find a case which is similar to the user's application. If there is a similar case, the system uses it to make a new schema for the application. During the operation, the user can interact with the system to change the case for his purpose. Whenever the system changes the schema in the case, it needs to use DICB to ensure that the newly changed schema should satisfy the 3NF. When the system fails to find a similar case, it designs a new one using the DICB. It may need lots of interactions with the user in this step to ensure a schema in the 3NF.

Currently, the RCG operation and the DICB are fully defined and implemented. We are working on developing a prototype of a DDCB in a small domain such as a university domain. We will concentrate on how the case hierarchy in DDCB can be reorganized dynamically when a new case is added. To implement a practical system, we need to develop a powerful natural language understanding system which recognizes requirement sentences.

The major contribution of this paper, we believe, is the modeling of an expert system with a case-based reasoning approach to database schema design automation. We present not only a domain specific case-base (i.e., DDCB) for designing a similar database schema, but also general normalization cases (i.e., DICB) for designing a novel schema or repairing a previously designed schema. To our best knowledge, this research is the first attempt to apply a case-based reasoning technique in database schema design automation. Since, we believe, many database schema design experts use their old experiences in various cases, this research can lead to a more realistic solution for such an expert system.

## References

[1] J. Allen, Natural Language Understanding (The Benjamin/Cummings Publishing Company, 1987).

[2] S. Atre, Data Base: Structured Techniques for Design, Performances, and Management (John Wiley and Sons, 1980).

[3] R. Barletta and D. Hennessey, Case Adaptation in Autoclave Layout Design, Proceedings of the Second DARPA Case-Based Reasoning Workshop (1989) 203–207.

[4] M. Bouzeghoub and G. Gardarin, The Design of an Expert System for Database Design, Proceedings of International Workshop New Applications of Databases (1983).

[5] H. Briand, H. Habrias, J.F. Hue and Y. Simon, Expert System for Translating an Entity-Relationship Diagram into Databases, Proceedings of the Fourth International Conference on ER-Approach (1985).

[6] P.P. Chen, The Entity-Relationship Model toward a Unified View of Data, ACM Transactions Database System 1, No. 1 (1976).

[7] J. Choobineh, M.V. Mannino, J.F. Nunamaker and B.R. Konsynski, An Expert Database Design System Based on Analysis of Forms, IEEE Transactions on Software Engineering 14, No. 2 (1988) 242–253.

[8] A. Dogac, B. Yuruten and S. Spaccapietra, A Generalized Expert System for Database Design, IEEE Transactions on Software Engineering 15, No. 2 (1989) 479–491.

[9] C.F. Eick, From Natural Requirements Language to Good Database Definition – A Database Design Methodology, Proceedings of the International Conference on Data Engineering (1984) 324–331.

[10] A. Goel, J. Kolodner, M. Pearce, R. Billington and C. Zimring, Towards a Case-Based Tool for Aiding Conceptual Design Problem Solving, Proceedings of Case-Based Reasoning Workshop (1991).

[11] T. Hinrichs, Some Criteria for Evaluating Designs, Proceedings of the Twelfth Conference of the Cognitive Science Society (1990) 900–907.

[12] J. Kolodner, Ed., Proceedings of the First Case-Based Reasoning Workshop (Morgan Kaufmann, 1988).

[13] J.J. Korczak, L.A. Maciaszek and G.L. Stafford, Knowledge Base for Database Design, Proceedings International Symposium on Database Systems for Advanced Applications (1989) 61–68.

[14] L.J. O'Connor, M.S. Lan, D.R. Partridge and J.M. Lee, A Case-Based Reasoning Approach to Automated Weld-Process Design, Applied Artificial Intelligence (1992) 315–330.

[15] Y.K. Paek, J. Seo and G.C. Kim, Domain Independent Case-Based Reasoning in an Expert System for Database Schema Design, Proceedings of '94 Japan/Korea Joint Conference on Expert Systems (March 1994).

[16] Y.K. Paek, J. Seo and G.C. Kim, A Case-Based Reasoning Approach to Relational Database Schema Design, Proceedings of EUROMICRO '94 Conference (September 1994).

[17] C.K. Riesbeck and R.C. Schank, Inside Case-Based Reasoning (Lawrence Erlbaum, 1989).

[18] K.L. Ruoff, CODES: A Database Design Expert System Prototype, Proceedings of the First Conference on AI Applications (1984).

[19] K. Sycara and D. Navinchandra, Influences: A Thematic Abstraction for Creative Use of Multiple Cases, Proceedings of Case-Based Reasoning Workshop (1991).

[20] D.C. Tsichritzis and F.H. Lochovsky, Data Models (Prentice-Hall, 1982).

![](/api/attachments/RMNDSHX4/fulltext/images/f0b040f352aa37cb5eb85f21ef80053914730ef944adb8a4ea5ba7d1adf4c537.jpg)

Yong-Kee Paek is a research fellow at the Korea Institute for Defense Analyses. He received his B.S. degree in Computer Science from Soongsil University, Seoul, Korea, in 1979, and M.S. and Ph.D. degrees in Computer Science from the Korea Advanced Institute of Science and Technology (KAIST), in 1986 and 1995, respectively. He has a national certificate of professional engineer for information processing systems. He was an invited researcher at the Uni-

versity of Connecticut in 1991. His research interests include applications of artificial intelligence, expert systems, database design, and software engineering.

![](/api/attachments/RMNDSHX4/fulltext/images/e45ff261d2bf03118f6e4b9ac7862d3604df0d6d7a376a3ed6dd2249beb44eed.jpg)

Jungyun Seo is an Assistant Professor in the Computer Science Department at the Sogang University in Seoul, Korea. Previously, he was a faculty member in the Computer Science Department at the Korea Advanced Institute of Science and Technology in Taejon, Korea, and a member of the technical staff at UniSQL, Inc., Austin, Texas. His research interests include natural language processing, artificial intelligence, and knowledge-based semantic analysis in distributed

query processing. Seo obtained a B.A. in Mathematics from Sogang University, Seoul, Korea, in 1981, and M.S. and Ph.D. degrees in Computer Science from the University of Texas, Austin, in 1985 and 1990, respectively.

![](/api/attachments/RMNDSHX4/fulltext/images/23088bbf8ed8d2dd8ca29d94258028e4f36f1e09482e629cfb76effe6330b7ce.jpg)

Gil-Chang Kim is a Professor in the Computer Science Department at the Korea Advanced Institute of Science and Technology in Taejon, Korea. He received his B.S. degree in Electrical Engineering from the University of Michigan in 1963, and M.S. and Ph.D. degrees in Mathematics from the University of Texas at Austin, in 1966 and 1969, respectively. He was a member of the research staff at the NASA from 1969 to 1970. Since 1971, he has been

working as a Professor at the Department of Computer Science at the Korea Advanced Institute of Science and Technology. In this period, he was an invited researcher at the IBM Watson Institute, New York, from 1972 to 1973, and the Nippon Electric Company, Japan, from 1986 to 1987. His research interests include operating systems, natural language processing, and machine translation.

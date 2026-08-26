---
otero_id: 17092
otero_key: "7Z9GHKHB"
title: "An expert modeling support system for modeling an object system to specify its information requirements"
authors: "Surya Bhan Yadav; Donald R. Chand"
year: "1989"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(89)90026-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An Expert Modeling Support System for Modeling an Object System to Specify Its Information Requirements

Surya Bhan YADAV

College of Business Administration, Texas Tech University, Lubbock, TX 79409, USA

Donald R. CHAND

Department of Computer Information Systems, Bentley College, Waltham, MA 02254, USA

This paper presents an analyst support system that partially automates the process of determining information requirements. The focus of this paper is upon the problems associated in developing a clear and consistent understanding of the object system by the analysis team, where the object system is essentially the larger system that an information system serves. It describes the design of a computer aided tool which is based upon an extension of SADT and it incorporates the use of problem domain knowledge-base and decision concepts of Simon. The emphasis is on the rationale for the structure and components of this tool and how it may be used for modeling the object system and performing both component and precedence analysis. The problem of generating information system requirements is reduced to traversing the conceptual model.

Keywords: Information Requirement Determination, System Analysis, Analyst Support System, Requirement Analysis.

![](/api/attachments/7Z9GHKHB/fulltext/images/4e2f116627ebfc9e12ec2bd109fc633234db25e28847d35aef99fcf02c16e820.jpg)

Surya B. Yadav received his B.S. degree in Electrical Engineering from Banaras University in 1972, his M. Tech. degree in Computer Science from I.I.T. Kanpur, India in 1974, and his Ph.D. degree in Business Information Systems from Georgia State University in 1981. He is an associate professor at Texas Tech University, Lubbock, Texas. He has worked as a consultant for developing system and application software. His research interests include expert systems for in-

formation system requirement determination and adaptive knowledge-based systems. He has published in several journals including Communications of the ACM, and Information Systems.

## 1. Introduction

Any methodology dealing with requirement specification must address three basic questions:

(1) What should requirements be?

(2) How should requirements be derived?

(3) How should requirements be stated?

The first question deals with the content, the second question deals with the process of determining the content and the third question deals with the form for stating the content. Very few researchers have addressed the first question. What are all the traits of a system which should be included in the requirement specification to make it a complete specification? For managers a verbal statement of requirements seems to be sufficient; technicians often include functional architecture, system context, performance specification, measurement, and test conditions as part of the total requirement specification.

Most software engineering research has focused on how to state requirements formally and completely. Generally, the statement of requirements has taken the form of:

(1) inputs, outputs and processes.

(2) data definition,

(3) processing requirements.

However, the process of determining requirements has received very little attention from re-

![](/api/attachments/7Z9GHKHB/fulltext/images/8718b7bf08e63d315d4e8e4521f9411ec9efee2c01e2f1a70ceb17cf67b05884.jpg)

Donald R. Chand is the Chair of the Department of Computer Information Systems at Bentley College. His teaching and research interests are in applications development technologies. He has published articles in the Communications of the ACM, the Journal of ACM, and IEEE Software. He has conducted ACM and IEEE tutorials in Design Methodologies and Fourth Generation Languages. He is an ACM lecturer and associate editor of the Journal of Information Resources

Management Systems. He also taught at Georgia State University and at Boston University. He received his Ph.D. degree from Boston University.

searchers. One of the main reasons for this lack is that the process spans over two ‘territories’ – the manager’s and the technicians’s [25]. This process starts with the understanding of an organization and ends with a formal specification of information requirements. In the early days of the development of computer based information systems, the emphasis was upon building transaction-based application systems that were designed to automate the clerical and operational tasks. For such relatively simple systems, the process of determining correct requirements was not critical. The problem of incorrect requirements [4] was not even considered to be an issue.

Thus, earlier research works on the development of computer based information systems emphasized mainly the problem of unclear and inconsistent [4] requirements. They started with a given set of user's need statements and tried to restate them in a formal manner to make them more clear and consistent. As a result, several documentation techniques were developed [7,17,18,45]. The problem of incorrect requirements got very little attention. However, during the era of multifunctional systems [3] the problems of both inconsistency and incorrectness became acute. Because it became very difficult to perform manual consistency checks for large systems, efforts were made to automate documentation techniques [1,38] in order to perform computer assisted checks. Efforts were also directed toward finding ways to tackle the problem of incorrectness. By the end of the era of multifunctional systems, work had started on modeling an object system to get a better understanding of the object system in order to reduce incorrectness. Methods like BSP [19], BIAIT [6] can be mentioned here. The arrival of the era of the multi-level management systems necessitated the broadening of the scope and the context of an object system: understanding organizational issues became critical to modeling the system.

It is obvious that the concept of multi-level management systems, henceforth called organization support system (OSS) [41], has changed the role of an analyst. An Organization Support System is an information system whose goal is to improve the effectiveness of an organization rather than just the efficiency of individual operations. If one is interested in the content of an information system that supports an organization in improving its effectiveness then one has to be concerned with the structure, processes, goal orientations and strategies of the organization besides the basic problem of how to manage well [42]. Thus, the concept of OSS complicates the task of an analyst. The analyst needs different skills and more sophisticated tools to understand the integration of the organizational structure and processes. Furthermore, the analyst has to work closely with the prospective users belonging to different parts of an organization. Each user has a different mental framework [44] of the problem and generally each framework differs from that of the analyst. Clearly an analyst needs a common framework to consolidate all these views as much as possible. We assert that a successful analyst needs a support system for playing the roles of different users and for communicating the progress of analysis to his team members. One of the author's Ph.D. research [43] is an attempt to develop such a support system.

Our experience has shown that an analyst support system should provide:

(1) a framework to study an organization in a systematic manner and characterize it with implications to its information requirements,

(2) an automated tool which includes:

(a) a formal notation to facilitate the modeling of organizational function,

(b) a knowledge base to help the an analyst in describing the model of functions,

(c) facilities for formal analysis of the described model for correctness and completeness,

(d) facilities to generate various analysis reports,

(e) a specification language to specify information requirements formally.

We have developed a conceptual design for such a support system. In this paper we concentrate on the automated tool portion of the analyst support system. It is important to note that the process of specifying the information requirements of an organization differs from the process of specifying the design requirements of information system. Obviously, the former process precedes the latter. Recently, there are several notable attempts being made to provide automated support for developing information systems [14,35,39]. However, most of these works emphasize automated support during the design process and not during the requirements analysis process. The tool described here helps an analyst in the former process. We call it the Expert Modeling Support System (EMSS). It provides a formal notation to describe and build a model of organizational functions. It includes a knowledge base to help the analyst build the model. It also supports a set of query-like language commands to generate interactively various reports about the description of the model.

Others have recognized the need for modeling in order to determine information systems requirements. It appears that Langefors [21] was the first. He emphasized that when designing an Information System, the designer has to distinguish between that part of the real world which is reflected in the system and that which is not. That part of the real world which is reflected in the system is said to be the object system. Langefors published a systematic and formalized approach to information systems design. He formulated a fundamental principle of systems work and sketched a basic theory of systems analysis. The theory is based on the concept of an imperceivable system. A large object system, in Langefors terminology, is an imperceivable system. A system is imperceivable if the number of its parts and their interrelations are so high that all of its structure cannot be safely perceived or observed at the same time. His theory states that for imperceivable systems a subsystem structure can be obtained recursively by perceivable steps of systems analysis. This subsystem structure can be checked for workability, which means that the system properties as a whole can be deduced from the set of properties of subsystems together with their interactions.

Langefors systems principle is essentially a top-down design approach where the system is partitioned into a set of subsystems at each step of the recursive procedure. Unfortunately, the lack of definite principles for selecting the subsystems at each level makes the process iterative. The choice of subsystems is, in some sense, an agreement between the user's mental model and the analyst's mental model of the problem. Another significant weakness of the approach is that it fails to specify when to terminate. However, the methodology that evolved based on Langefors theory at the

Royal Institute in Sweden, consists of a graphical notation for recording each step of this top-down systems approach. The object system model so constructed captures the information sets explicitly, and the interconnection between information sets defines the functional architecture of the desired information system. In ISAC [22] approach, tools are available to record the precedence relationship between information sets, and thus one can perform precedence analysis to identify inconsistencies and incompatibility in requirements.

In recent years, Structured Analysis & Design Technique (SADT) [32] has surfaced as a methodology for developing system. It also uses a graphical notation, but the approach is based on a fundamental model consisting of four elements, namely input, control, output, and function. Thus, SADT provides a framework for developing the conceptual model. When used in the system analysis phase, it produces a model of the system to be constructed and, when used during the design phase, it provides a model of a system to be implemented. The SADT model is again applied recursively. Instead of calling this process top-down, the term 'step wise refinement' is used. The reason for this term is that at each stage of recursive process both the input and the functions are decomposed or refined simultaneously. This joint decomposition strongly increases the correctness of a system and the use of the same abstract model at each step makes the process of validation systematic, orderly, and teachable.

The SADT, however, suffers from the following maladies:

(1) It does not provide any method to study an organizational set up in order to get an overall perspective of its managerial functions. Thus it is difficult to use SADT in determining requirements for Organization Support Systems.

(2) For large and complex systems, the lack of automation makes SADT vulnerable to inconsistency and incompatibility.

(3) No formal technique for model verification exists.

(4) No criteria for terminating the recursive process exists.

Systematic Activity Modeling Methods (SAMM) has been developed by Stephen & Tripp [36] to support the description of an activity model. This model appears similar to the SADT model. This work presents a good attempt to automate the conceptual modeling in a top-down fashion. However, it does not provide any definite criteria for terminating the top-down decomposition. It ignores the description of attributes of data. It does not provide any aid in identifying major activities. Precedence analysis seems to be limited to activities only. Precedence among inputs and outputs is not checked.

In this paper we describe the design of EMSS that helps in tackling the problems 2, 3, and 4 associated with SADT. A great deal of work has been done on problem 1 [42]. Section 2 describes a basic building block for constructing a conceptual model of an object system. Section 3 discusses the design of EMSS. It also describes the knowledge-base useful for an analyst in constructing the conceptual model. Section 4 discusses formal analyses which can be performed on the model. Section 5 elaborates on various reports which can be generated from the description of the model. The paper concludes with section 6, which briefly summarizes the paper, and section 7, which includes references.

## 2. The IFDC Block and Its Use in Building the Conceptual Model

This section describes the INPUT, FUNCTION, DECISION, and CONTROL (IFDC) block and its use in building the conceptual model.

To tackle the complexity of imperceivability of an object system, one needs to partition the object system into a set of manageable subsystems in a recursive manner. This partitioning cannot be arbitrary but must be done according to the workability concept described earlier. Following the SADT approach, we propose the following basic building block for partitioning an object system (fig. 1).

![](/api/attachments/7Z9GHKHB/fulltext/images/9b85b8ccf962f0cfe7f742720ee21888b9b1b7d77fa575ac002452e87799100e.jpg)  
Fig. 1. IFDC block.

We will see later, this block facilitates the checking for workability at each level of the recursive process. The name 'INPUT' refers to the information needed for the managerial FUNCTION to arrive at a DECISION. INPUT and DECISION may be viewed as the 'before' and 'after' state of an activity. The CONTROL element interacts with and constrains the functional transformation to ensure that it applies only under the appropriate circumstances. Note that the name 'CONTROL' has nothing to do with its general meaning in Cybernetics. It is synonymous with the constraint with influences a managerial function. The information in the control element is generally not modified by the functional transformation. It should be emphasized that INPUT, CONTROL, and DECISION are very general terms used for one or more inputs, controls and decisions respectively. Each of them can be thought of as a pipeline carrying many components of the same class. The arrows in the diagram define interfaces among the FUNCTIONS and they must not be considered as control flows, such as in a flowchart.

The IFDC block, shown in fig. 1, is an incomplete model for determining information systems requirements because it fails to incorporate the characteristics of a managerial function. Although it is well known that the kind of information needed for solving a problem varies, there exists no practical and useful characterization which aids the analyst in identifying the kind of information needed for a specific type of managerial problem. Keen and ScottMorton's [20] characterization of information based upon Anthony's model of managerial functions and Simon's [33,34] notion of structured and unstructured problems remains the most comprehensive framework for understanding the relationship between the nature of information and the managerial task. We propose an alternative characterization of information based upon the observation that one needs the following three entities for any decision:

(1) data,

(2) report form,

(3) decision process.

If we know all three entities then we label this case as structured decision case. If we know 1 and 2, and possess an incomplete understanding of the decision process so that human judgement is ininvolved to arrive at the final decision, then we define this as a semistructured case. If we know only 1 and possess partial or no knowledge of 2 and 3, then we classify the decision as an illstructured case. In problems like lot scheduling, we generally know all the three elements, whereas in capacity planning the decision process may be poorly defined, although we know data in a database form and in regular reports to assist managers in their planning. In problems like long range production planning, we might know data but we rarely know in advance their use. In this environment we need ad hoc reports from a database. Specially tailored programs are written from time to time to provide such ad hoc reports. It is pertinent to ask: how significant and useful it is to make this distinction among decisions? A recent study by Lyles and Mitroff [23] indicates that 90 percent of the problems reported by managers fell within the illstructured category. Mintzberg [26,27] has also emphasized the existence of illstructured decisions faced by managers. Therefore our model must deal with ill- and semistructured decisions along with the well structured decisions before it can be accepted as a general tool for developing MIS. To describe each kind of decision, we modify the IFDC block as shown in fig. 2.

The nature of the decision would be indicated by labeling the building block as such. This is an important aspect of the model. It allows one to state constraints and assumptions about any component of the IFDC block that might be missing, unknown, or explorable at the time of defining the object system. This information would be very helpful for the designer in developing an adaptive and flexible system. It is contended that assumptions and constraints about most of the problems currently perceived as illstructured change over time, and thus make an information system obsolete sooner than it should.

![](/api/attachments/7Z9GHKHB/fulltext/images/57244ff3ae3d823e986a991b00d3a45cd6c4a78894ac12f2b34fe51950dd29ad.jpg)  
Fig. 2. Modified IFDC block.

![](/api/attachments/7Z9GHKHB/fulltext/images/a9ccc129685428a4c6d10f9740e733cd97402d22d2bc55de23ca788fa3aa03c6.jpg)  
Fig. 3. A broad overview of a conceptual model.

## 2.1. Construction of the Conceptual Model

The IFDC block is the basic building block for a conceptual model. The conceptual model is developed using the stepwise refinement approach. Abstraction plays a major role in stepwise refinement. Abstraction is used in naming functions, inputs and decisions at each level of refinement. Abstraction also helps in reducing the demand to enumerating all the functions at the same time. The analyst creates names according to naming conventions described in the next section. The interactive tool supports the iterative process of building the conceptual model. This means that the analyst can come back to any level of refinement at any time to modify or alter the description of the model.

A broad overview of a typical conceptual model is shown in fig. 3. It shows a hierarchical model divided into levels. Following SADT terminology, we call each outer box a diagram. A diagram represents a set of partitioned subsystems corresponding to an IFDC block at a higher level. For example, the diagram $A_{01}$ contains a set of subsystems which has been derived by expanding the block $F_{01}$ at level 0. Each block represents a function along with its associated inputs, outputs, and controls. A block at level i is refined into a diagram at level $i+1$ . To understand the structural relationship among $F_{01}$ and $F_{11}$ , $F_{12}$ , and $F_{13}$ , let us look at the general representation of an

![](/api/attachments/7Z9GHKHB/fulltext/images/fd1fcb43d461e903c115715a4a77f8bdbf45712fda4b435e48ba553de0f3a2d2.jpg)  
Fig. 4. A general form of an IFDC block.

IFDC block in fig. 4. The symbols are defined as follows:

$F_{mn}$ is the nth function on the current diagram related to the mth function on the parent diagram

$I_{mnr}$ is the rth input related to mth input arrow on the parent block and this input is at the nth box on the current diagram

$O_{mns}$ is the sth output (decision) related to the mth output (decision) on the parent diagram and this output is at the nth box on the current diagram

$C_{mnl}$ is the lth constraint related to mth control (constraint) on the parent diagram and this constraint is at the nth box on the current diagram.

The letter S, H and U stand for structured, semi-structured and illstructured respectively. Indices of symbols show the relationships between two consecutive levels.

## 2.2. Termination of the Stepwise Refinement Process

‘Where to stop’ has always been a vague and unknown point in the description of a hierarchical model. This problem is cited as a major disadvantage of a stepwise refinement technique. Another important contribution of our approach is that a definite criteria is available to terminate the refinement process while generating a description of an object system. The refinement process terminates when all the ‘abstract type’ entities - inputs, outputs, and controls have been broken down into ‘primitive type’ entities and each of the primitive type entities has been described in terms of a given set of properties. We use the terms ‘a-type’ and ‘p-type’ to refer to ‘abstract type’ and ‘primitive type’ entities. These entities are defined in detail in the next section. Note that the analyst can stop at any point in describing the model as long as he or she is in a position to define a-type data sets in terms of a set of p-type datum.

## 2.3. A Formal Description of the IFDC Block

One of the major contributions of this research is the formal notation for describing an IFDC block. This formalism provides the means for automating the process of developing the conceptual model.

Essentially the problem is to describe formally the following four entities of the basic block:

(1) OUTPUT or DECISIONS

(2) MANAGERIAL FUNCTION

(3) INPUTS

(4) CONTROLS.

We emphasize that terms INPUTS and CONTROLS carry information to be used by a managerial function which produces a decision and/or an output. Output also carries information which can be used as a input or as a constraint for subsequent managerial functions in the hierarchy. To represent this information one has to first decide what kind of information is needed by the manager to perform a specific managerial function. Existing literature provides several different classification schemes for information. For example, Dearden and McFarlan [11] classify business information as based on its nature. Dermer [12] provides a classification based on the object or an activity about which information is needed Keen and ScottMorton [20] classify information based on data attributes, such as accuracy, level of detail, time horizon, frequency of use, source, scope of information, type of information, and age of information. Glaser [15] classifies information by its 'complexity'. White [40] classifies information into two levels depending upon whether the information describes a 'state' of the affair in some context or it specifies some connection between states. These two levels are:

(1) State type.

(2) Relation type.

It is easy to see that these classifications are not mutually exclusive. For example, the terms 'internal' and 'external' used by Dearden and McFarlan refer to the 'source' attribute of the information described by Keen and ScottMorton. 'Recurring' and nonrecurring' can be covered by the 'frequency of use' attribute. 'Historical' and 'future' information is measured by the 'time horizon' attribute of the information. 'Handbook' information can be thought of as the 'documentary' information. 'Environmental' information can be categorized as external information and so on. White's classification is a more abstract classification of information. For example, a state type information can be about the past, present, or future state of an affair. It can represent an external state or an internal state.

the relevant attributes of inputs, outputs, managerial functions and controls is described in fig. 5 using BNF [28] notation. We will briefly explain the terms used in fig. 5. The symbols a-type refers to a group of data elements treated as a unit which carries information for managers. The symbol p-type refers to a single data element. An a-type data set can carry either a state type information or a relation type information. A state type information can have various attributes such as 'frequency of use', 'sources', and 'standard-ad hoc-type' as defined in the fig. 5. A relation type information is derived from state type information with the help of a model supported by the information system.

A comprehensive framework for describing all

P-type datum is defined in terms of its various

```txt
<output>:: OUTPUT<a-type>| DECISION<decision-name>
    OUTPUT<function-name>

<managerial-function>:: FUNCTION<function-name>

<input>:: INPUT<a-type>| INPUT<p-type>

<constraint>:: CONTROL<a-type>| CONTROL<p-type>

<a-type>:: <iodentifier><state-relation-type><p-type>1
n

<decision-name>:: <identifier>

<function-name>:: <identifier><function-type><managerial-activity>

<p-type>:: <pdentifier><qualification-attribute><relationship-attribute>
<usage-user-attribute><source-attribute><measure-of-scale>
<stochastic-attribute>

<iodentifier>:: <input-identifier>| <output-identifier>
<control-identifier>

<state-relation-type>:: <state-type>| <relation-type>

<state-type>:: <state><form><standard-ad hoc-type><system-attribute>
<frequency-of-use><source>| <p-type>

<relation-type>:: If<p-type> THEN<p-type| BEST OF ALL IS<p-type>

<identifier>:: <alphabet><alphanumeric>0
60

<function-type>:: STRUCTURED| SEMISTRICTURED| UNSTRUCTURED

<managerial-activity>:: <activity-name><activity-attributes>

<activity-name>:: ALLOCATING| CONTROLLING| DIRECTING| EVALUATING|
MAXIMIZING MINIMIZING| OBJECTIVE SEEKING|
SEARCHING| VALIDATING| ADVISING| AUTHORIZING|
<other-activity>

<activity-attributes>:: <activity-objective><techniques-to-carry-
out-activity><reports-needed><children-
subactivities><time-horizons><others>

<other-activity>:: <string>

Fig. 5. A formal notation to describe various entities.
```

attributes. These attributes are qualification-at-tribute, relation-attribute, usage-users-attribute, source-attribute, measure-of-scale, and stochastic-attribute. Qualification-attribute refers to the exact circumstances under which the data element is intended for general use. This attribute is defined by characteristics such as accuracy, time dependency, and update-frequency. Relationship-attribute specifies the relationship between an entity and the p-type(s) that belong to it. Usage-users-attribute specifies status, security, and internal or external use of the p-type datum. Status indicates whether data elements are available for use or whether they are simply proposed for possible future use. Other attributes are self-evident in fig. 5. Ultimately each a-type data set is described in terms of p-type data.

A managerial FUNCTION is defined in terms of its type and the managerial activity to which it belongs. Our interactive system maintains, in a knowledge base, various kinds of managerial activities to aid the analyst during the description of a model. This knowledge base contains the description of managerial activities in the form of a

```txt
<pidentifier>:: <identifier>
<qualification-attribute>:: <accuracy> <update-frequency> <logical-unit-of-retrieval>
<relationship-attribute>:: BELONGS TO<iodentifier>1
<n
<usage-user-attribute>:: <status> <security> <internal-external>
<status>:: PROPOSED| APPROVED
<internal-external>:: INTERNAL| EXTERNAL
<source-attribute>:: <source-documentant>| <generated>
<measure-of-scale>:: <quantitative>| <qualitative>
<stochastic-attribute>:: <DETERMINISTIC| <stochastic>
<stochastic>:: <known-function>| <unknown-function>
<input-identifier>:: <identifier>
<output-identifier>:: <identifier>
<control-identifier>:: <identifier>
<state>:: PRESENT| PAST| FUTURE
<form>:: activity-report| analysis-report| logistics-report| variance-report| comparative-report| unknown
<standard-ad hoc-type>:: STANDARD| AD HOC
<system-attribute>:: PART<iodentifier>1| SUBPARTS<iodentifier>1
n n
<frequency-of-use>:: RANDOM| <periodic>
<periodic>:: MONTHLY| WEEKLY| DAILY| YEARLY| BIWEEKLY| <others>
<source>:: EXTERNAL| INTERNAL| MIXED
<string>:: <alphabet><alphanumeric>0
n
<alphanumeric>:: <alphabet> <digit>
<quantitative>:: <nominal-scale> <interval-scale> <ordinal-scale>
<ratio-scale>
Fig. 5. (continued).
```

```txt
<activity-objective>:: <text>
<techniques-to-carry-out-activity>:: <text>
<reports-needed>:: <text> <text>, <text>0
    n
<children-subactivities>:: INCLUDES <activity-name>0
1
<time-horizon>:: <text>
<qualitative>:: <string>
<text>:: <string> <string> <string>0
    n
<known-function>:: (function-name, parameters)
<others>:: <string>
<unknown-function>:: (probability-distribution)
<alphabet>:: A|B| --- Z
<digit>:: 0|1|2 --- 9
Fig. 5. (continued).
```

semantic-inheritance network (SI-net) [13]. SI-net is basically a network of various types of nodes and arcs to represent different traits of a 'concept'. In our case the 'concept' is a managerial activity. The description of a managerial activity consists of the following:

(1) What is needed to carry out an activity.

(2) How the activity is performed.

In the first case, we describe a managerial activity in terms of

(a) objectives of an activity,

(b) technique(s) used to carry out an activity, (c) kinds of reports needed to perform the activity,

(d) possible subactivities belonging to the activity,

(e) various other attributes such as time horizon, etc. for the activity.

These attributes vary from activity to activity.

In the second case, the activity is treated as a process and it is described in terms of a procedure. In order to specify an activity completely, one should describe an activity in terms of resources needed and the procedure. The knowledge base contains a description of all resources (information) that are needed to carry out the activity. The analyst may use this information in describing a managerial function in a procedural form which is unique to a particular organization.

The SI-net used here has three types of nodes and three types of arcs. An oval shaped node is used to represent the name of an object. A rectangular node is used to represent attributes of an oval node. A diamond-shaped node is used to indicate conditional relationships among objects. An arc labelled DATTR connects an attribute to its object. An arc labelled CAS ('contains as a subconcept') connects one object to its subcomponents. An arc labelled STRUCTURE connects various attributes to show the overall concept of an activity under a certain condition. Fig. 6 shows an example of SI-net to describe an activity called 'Planning'. Each attribute is defined in terms of: (1) attribute-name; (2) values which can fill in the attribute-name (shown by V/R (Values/Restriction) link); and, (3) modality, which indicates whether that particular attribute is required or optional. The STRUCTURE link is not shown in fig. 6. The subconcepts like 'production planning' can be defined further in terms of their specific attributes.

![](/api/attachments/7Z9GHKHB/fulltext/images/7eea89d77bb5eb27e20fe0d5a7a72ec3faba08bebfabffa55fb7a8bf0a1c636d.jpg)  
Fig. 6. SI-Net concept of planning.

## 3. Design of EMSS

Fig. 7 shows a simplified architecture of EMSS. EMSS has three subsystems:

(1) user-interface,

(2) model handling,

(3) knowledge handling.

All the user-interaction during the description of models or knowledge is managed by the user-interface sub-system. The model handling subsystem is responsible for maintaining the model base; the knowledge handling subsystem is responsible for maintaining the knowledge base.

## 3.1. Functional Components of EMSS

Figs. 8–10 show the functional components of EMSS. These functional components are shown using SADT (also called IDEF $_{0}$ ) diagrams. Fig. 8 shows the overall context in which EMSS interacts with an analyst. The major inputs to EMSS are the definitions of models and of knowledge. The major outputs are the various reports related to the model base and the knowledge base. The knowledge base is defined under the constraints of the application (or problem) domain. Fig. 9 shows the major functional components of EMSS. Fig. 10 shows a detailed description of the 'maintain-model-base' function shown in fig. 9.

![](/api/attachments/7Z9GHKHB/fulltext/images/b1be3ef89d29149b162521910e9cf8fa8993ac209c70d51902a2fad904b34c05.jpg)  
Fig. 7. A simplified architecture of EMSS (Expert Modeling Support System).

![](/api/attachments/7Z9GHKHB/fulltext/images/c246b337e97b46ff3c49376418c64f080306b3b533825a1e087944d956c27758.jpg)  
Fig. 8. An overall view of EMSS.

The system is interactive and prompts the user for the appropriate response while describing a model or asking for reports. The analyst has the option of quitting in the middle of the description of a model and saving the incomplete description. The analyst can type 'HELP' in any of the system's 'terminal states' to get help as to what possible alternatives are available to him or her at that terminal state. Thus the analyst does not have to remember the terminal state during a session with the system. Part of the user interface to the system is shown by a transition diagram [29] in figs. 11–12. A transition diagram consists of nodes and arcs. Nodes represent terminal states. (The system may go through various internal states in switching from one terminal state to another but these internal states are not shown on the transition diagram.) Arcs are labelled as 'user-response/system-response'. For example in the initial state of fig. 11 when user types 'FUNCTION' the system respond by asking the function-name. Then the user responds by typing in an identifier for the name. Then the system asks if this function belongs to (is part of) any other function. This interaction continues until the user stops. If the user does not understand any response from the system, explanation is available by typing in 'HELP'. The user can take as many sessions as needed to describe a model completely. Several models can be described. A model can be made as part of another model. The user can request reports on the described model at any point even during the description of the model. Various kinds of reports provided by the system are described in the next section.

![](/api/attachments/7Z9GHKHB/fulltext/images/2c2be3eae3942d35c3362daf4c330bae80e01424ac1d23bfc53d25f7cfee705a.jpg)  
Fig. 9. Major functional components of EMSS.

## 3.2. Internal Representation of the Model

By internal representation we mean the representation of all the components of a model inside a computer system. This representation should be such that it captures all the information about the described model and facilitates formal analysis to be performed on the model.

A close examination of structures shown in fig. 3 and fig 4 reveals that one has to keep the following information at each level:

(1) information about the diagram,

(2) information about the basic blocks inside a diagram,

(3) a pointer from the basic block to its current diagram and the successor diagram at the next level,

(4) a backward pointer from the diagram to its parent block.

![](/api/attachments/7Z9GHKHB/fulltext/images/454bc725a60b9617b5fc4397f2bb2ab6c60ba0d3daa4220b3270cc372374322c.jpg)  
Fig. 10. A detailed description of 'maintain model base'.

![](/api/attachments/7Z9GHKHB/fulltext/images/1a771b5e4d1f40b1e7ee01e13df856ce6ee9928a7e55827c5ef99d60bc6a581f.jpg)  
Fig. 11. A partial transition diagram to describe a 'function'.

![](/api/attachments/7Z9GHKHB/fulltext/images/d56879b397bcaaef6c60efbc41eba32da9cbd411339d34d1ed2f093000327791.jpg)  
Fig. 12. A partial transition diagram to describe an 'output'.

![](/api/attachments/7Z9GHKHB/fulltext/images/2b78739ccd7b6be7f456134ec9a3553ad585f9269edbed32a4584a54165e9f7d.jpg)  
Fig. 13. Part of an internal representation of a conceptual model.

This list suggests a doubly-linked structure to store the description of a conceptual model. We use the record concept to store the information at each level. Fig. 13 shows a detailed description of the internal structure. A record is used to represent a block inside the diagram. This record, in turn, points to various other records containing information about the managerial function, various inputs, and constraints belonging to that block. The model is stored in a model base which is a database containing the description of previously developed conceptual models.

## 4. Automated Means for Formal Analysis

The first part of this section describes the types of analysis that can be performed automatically during the construction of a conceptual model. The second part describes various types of reports that can be provided by the system. The system allows component analysis as well as precedence analysis.

Component analysis refers to identification of the structural relationship among components of the model from one level to another. Precedence analysis, on the other hand, identifies precedence relationships among components of the model within one level.

The purpose of component analysis is to identify:

(a) structural relationship among functions,

(b) structural relationship among inputs,

(c) structural relationship among outputs,

(d) structural relationship among controls.

Precedence analysis is performed at each level to identify:

(e) precedence relationship among functions, (f) precedence relationship among inputs & outputs,

(g) precedence relationship among inputs and functions.

These relationships are discussed below in detail.

## 4.1. Structural Relationship among Functions

Structural relationship refers to the interconnection between managerial functions of one level and the refinement of the functions down the hierarchy. This relationship can be tested for consistency as follows:

Suppose a managerial function fi at level i is divided into subfunctions fj1, fj2, ..., fjn at the immediate next level i + 1 which, for convenience, we will call j and

(i) if fi is structured, then fj1, fj2, ..., fjn must be structured functions,

(ii) if fi is semistructured then fj1, fj2, ..., fjn are either structured or semistructured,

(iii) if fi is illstructured then fj1, fj2,..., fjn can be structured, semistructured or illstructured functions as long as at least one of the functions is illstructured.

Consistency of structural relationship among diagrams means that the properties of fj1, fj2,..., fjn of a diagram must permit the determination of the properties of fi. In other words, each level of expansion correctly echoes the intentions of the immediately superior level. To achieve this echoing one has to look at all the components of a block at level i and at the block's corresponding diagram at level j. This relationship is illustrated in fig. 14. Let us assume that the expansion of function $F_{-1}, F_{-2}$ at level i is $F_{11}, F_{12}$ and $F_{21}, F_{22}, F_{23}$ respectively at level i + 1. Let us further assume that $I_{111}, I_{121}$ are refinements of $I_{-11}$ and $Odl_{11}$ and $O_{121}$ are components of $I_{-11}; O_{111}$ and $O_{121}$ reflect $O_{-11};$ and $C_{111}$ and $C_{121}$ are components of $C_{-11}$ . We notice $F_{11}$ and $F_{12}$ are structural components of $F_{-1}$ and they are related to each other and to $F_{-1}$ through their inputs, outputs, and constraints.

This consistency is checked during the description of the model and it fulfills the workability principle described earlier. In case an analyst introduces new entities while describing the expansion of $F_{-1}$ , the system interrogates the analyst to double check the relations among inputs and outputs of $F_{-1}$ and the inputs and outputs of the diagram at level $i + 1$ , according to the following rules:

![](/api/attachments/7Z9GHKHB/fulltext/images/f9bbdeb8e0c0e3fa4c1721e7d101b2ee6f1d68bd5a58d7ca6be81f94e64e686d.jpg)  
Fig. 14. Expansion of $F_{-1}$ and $F_{-2}$ .

$$
\begin{array}{c c} \mathrm{k-1,2...s} & \mathrm {p - 1,2...q} \\ \mathrm {I_ {mnk}} & \mathrm {I_ {-mp}} \\ \mathrm {n = 1,2,...,1} \\ \mathrm {k = 1,2...s} & \mathrm {p = 1,2...q} \\ \mathrm {C_ {mnk}} & \mathrm {C_ {-mp}} \\ \mathrm {n = 1,2,...,1} \\ \mathrm {k = 1,2...s} & \mathrm {p = 1,2...q} \\ \mathrm {O_ {mnk}} & \mathrm {O_ {-mp}} \end{array}\tag{i}
$$

(ii)

(iii)

where U indicates the set union and indicates a subset or a proper subset.

If new inputs, outputs, or constraints are introduced at level i + 1, they should be reflected in the block at level i. Note that an intermediate input, output, or constraint (within a diagram) is new but it does not have to be reflected in the corresponding block at the higher level. The above rules apply only to those entities which are carried from one diagram to another.

## 4.2. Structural Relationship among Inputs

The structural relationship among inputs describes connection among inputs at different levels. An input $I_{k}$ at level k is refined into $I_{11}, I_{12}, \ldots, I_{1n}$ at the next level. To be consistent, the attributes of $I_{11}, I_{12}, \ldots, I_{1n}$ , should be the same as that of $I_{k}$ and the set union of $I_{11}, \ldots, I_{1n}$ should account for $I_{k}$ .

![](/api/attachments/7Z9GHKHB/fulltext/images/f9099f6f941a67499e7c73803d7f13ec58043e237416d74ef8468b5aaea3442b.jpg)  
Fig. 15. Precedence relationship matrix for functions.

## 4.3. Structural Relationship among Outputs

The structural relationship among outputs describes the connection among outputs at different levels. An output $O_{k}$ may be refined into $O_{11}, O_{12}, \ldots, O_{1n}$ at the next level. To be consistent, the attributes of $O1_{1}, O_{12}, \ldots, O_{1n}$ should be the same as the $O_{k}$ and the set union of $O_{12}, \ldots, O_{1n}$ should be the same as $O_{k}$ .

## 4.4. Structural Relationship among Constraints

Constraints at level i + 1 must be derived from level i just like in the case of inputs. Refinement of constraints must also obey the same consistency laws as in the case of inputs and outputs discussed above.

## 4.5. Precedence Relationships among Functions

This relationship essentially identifies which functions are precedent to a given function on one level of the hierarchy. The precedence relationship enables a designer to identify which functions can be implemented independently.

![](/api/attachments/7Z9GHKHB/fulltext/images/4fb6996627a378cbef0843d9c65d33b0b60a722ce3da7f19bbdfc03d62517b53.jpg)  
Fig. 16. Precedence matrix for inputs and functions.

![](/api/attachments/7Z9GHKHB/fulltext/images/b10e749d91587416ec57ece30ad8585641696ee1d79e9126431fac4b3d7b6f05.jpg)  
Fig. 17. Precedence matrix for inputs and outputs.

The model is developed in a stepwise manner. Because of the complexity of a system, it is very hard to extract these precedence relationships manually from the model description. The EMSS scans the structure of the model and presents this relationship in a matrix form as shown in fig. 15.

A '1' entry indicates that the function corresponding to the row is precedent to the function corresponding to the column. A '0' entry indicates no precedence. For example $F_{1}$ precedes $F_{2}$ in fig. 15.

## 4.6. Precedence Relationship among Inputs and Functions

The precedence relationship among inputs and functions shows what inputs are required for what functions within a particular level. The information is recorded in a matrix form as shown in fig. 16. These precedence matrices are checked for consistency by the system. A matrix is consistent if and only if every principal submatrix contains at least one or more zero column [24]. Reachability computation [16] is performed after the consistency check to get further insight about the structure of the object system.

## 4.7. Precedence Relationship among Inputs and Outputs

The precedence relationship among inputs and outputs describes what inputs are needed to produce a specific output. The relationship is again recorded in a matrix form as shown in fig. 17. The matrix also lends itself to reachability analysis that aids in design and implementation of the system.

## 5. Generation of Reports

Reports are used to retrieve and present information stored in the object system model base and the knowledge base with the intent to help an analyst in

(1) identifying syntactic and semantic error in describing the model,

(2) modifying existing models stored in model base,

(3) presenting system specification to the designer,

(4) evaluating the status of the described model in terms of its completeness.

The following forms of reports are supported by the system to present data stored in model base and knowledge base:

(a) descriptive form (narrative and/or outline),

(b) list form,

(c) table form,

(d) matrix form,

(e) linear responsibility chart (LRC) form [2],

(f) graph form.

For a more detailed discussion of these report forms, reader is referred to Yadav [43].

## 6. Conclusion

We have described an automated process of determining information requirements. Specifically, we have introduced the formalism necessary for automating the process of developing a conceptual model, which is a prerequisite for deriving information systems requirements.

## References

[1] Alford, M.W., "Requirements Engineering Methodology for Real Time Processing Requirements." IEEE Trans. On Software Engineering, SE-3 (1977).

[2] Banes, D.W., "Linear Responsibility Charting." Industrial Engineering (1972) pp. 17–19.

[3] Benjamin, Robert I., "A Generational Perspective of Information System Development." Communications of the ACM, Vol. 15, 1972, pp. 640–643.

[4] Boehm, Barry W., "Software and Its Impact: A Quantitative Assessment." Datamation 19 (1973) pp. 48–60.

[5] Boehm, Barry W., "Some Steps Toward Formal and Automated Aids to Software Requirements Analysis and Design." IFIPS 74 (1974) pp. 192–197.

[6] Carlson, Walter M., "Business Information Analysis and Integration Technique (BIAIT) - The New Horizon." Data Base (Spring 1979).

[7] CODASYL Development Committee, "An Information Algebra Phase 1 Report." Communication of the ACM, Vol. 5, No. 4 (1962) pp. 190–204.

[8] Couger, J.D. and R.W. Knapp (ed.), System Analysis Techniques. New York: John Wiley and Sons, Inc., 1974, pp. 234–258.

[9] Couger, J.D., Mel A. Colter and Robert W. Knapp, Advance System Development/Feasibility Techniques, New York: John Wiley and Sons, Inc. 1982.

[10] Davis, Carl G and Charles R. Vick, "The Software Development System." IEEE Trans. on Software Engineering. Vol. SE-3, No. 1, 1977, pp. 69–83.

[11] Dearden, J. and F.W. McFarlen, Management Information System, Texts and Cases. Homewood, Illinois: Richard D. Darwin, Inc. 1966.

[12] Dermer, Jerry, Management Planning and Control Systems, Texts, and Cases. Homewood, Illinois: Richard D. Darwin, Inc. 1966.

[13] Elam, J.J., J.C. Henderson and L.W. Miller, “Model Management Systems: An Approach to Decision Support in Complex Organizations.” Conference on Information Systems Proceedings, 1980, pp. 98–110.

[14] Estrin, G., R.S. Fenchel, R.R. Rajouk and M.K. Vernon, "SARA (System Architects Apprentice): Modeling, Analysis and Simulation Support for Design of Concurrent Systems." IEEE Trans. on Software Engineering, Vol. SE-12, No. 2, 1986, pp. 293–311.

[15] Glasser, E., "Information Technology: Relationship to Management Decision Models." Management Information System and the Information Specialists – Proceedings of a Symposium held at Purdue University, July 12–13, 1965, pp. 26–35.

[16] Hansen, J.V., L.J. McKell and 'L.E. Heitger, "ISMS: Computer-Aided Analysis for Design of Decision Support System." Management Science, Vol. 25, No. 11, (1979) pp. 1069–1081.

[17] IBM (no author), The Time Automated Grid System: Sales and System Guide, Publication No. GY20-0358-1. 2nd ed. (1971).

[18] IBM, Study Organization Plan Documentation Techniques, Manual 620-8075 (1961) pp. 1–26; Manual F20-8136 (1963): pp. 2, 7–11.

[19] IBM, “Business Systems Planning—Information Systems.” Planning Guide, Manual GE 20-0527-2, 2nd ed. (1978).

[20] Keen, P.G.W. and M.S. Scott Morton, Decision Support System: An Organizational Perspective. Philippines: Addison Wesley Publishing Co., 1978.

[21] Langefores, B., "Some Approaches to the Theory of Information Systems." BIT 3 (1963) pp. 229-254.

[22] Lundberg, Mats, “Utilization of new Information System Development Methods in Practice-Perspectives and Prospects.” Information Processing. North-Holland, IFIP, 1977.

[23] Lyles, M.A. and I.I. Mitroff, “Organization Problem Formulation: An Empirical Study.” ASQ 25 (1980) pp. 102–119.

[24] Mairmont, R.B., "A New Method of Checking the Consistency of Precedence Matrices." Journal of the ACM 6 (1959) pp. 164–171.

[25] Miller, J.C., "Conceptual Models for Determining Information Requirements." Proceedings - Spring Joint Computer Conference, pp. 690-620.

[26] Mintzberg, H., “Managerial Work: Analysis from Observation.” Management Science, Vol. 19, No. 2 (1971) pp. B97–B110.

[27] Mintzberg, H., “The Structure of ‘Unstructured’ Decision Process.” ASQ 21: pp. 246–275.

[28] Naur, Peter, "Revised Report on the Algorithmic Language ALGOL 60." Communications of the ACM 6 (1963) pp. 1-17.

[29] Parnas, D.L., "On the Use of Transition Diagrams in the Design of a User Interface for an Interactive Computer System." Proceedings of the Twenty-Fourth National ACM Conference, 1969, pp. 379-384.

[30] Reitman, W.R., "Heuristic Decision Procedures, Open Constraints and the Structure of Ill Defined Problems." Human Judgments and Optimality, Edited by M.W. Shelly and G.L. Bryan. New York: 1964, pp. 282–315.

[31] Reitman, W.R., Cognition and Thought. New York: John Wiley and Sons, Inc., 1966.

[32] Ross, D.T. and K.E. Schoman, Jr., "Structured Analysis for Requirements Definition." IEEE Trans. in Software Engineering Vol. SE-3, No. 1 (1977).

[33] Simon, H.A., The New Science of Management Decision. Englewood Cliffs, New Jersey: Prentice-Hall, Inc., 1977.

[34] Simon, H.A., "The Structure of Illstructured Problems." Artificial Intelligence 4 (1973) pp. 181–201.

[35] Smith, D.R., G.R. Kotik and S.J. Westfold, "Research on Knowledge-Based Software Environments at Kestrel Institute," IEEE Trans. on Software Engineering, Vol. SE-11, No. 11, 1985, pp. 1278–1295.

[36] Stephens, Sharon, A. and L.L. Tripp, "Requirement Expression and Verification Aid." Proceedings-Third International Conference on Software Engineering, Atlanta: (1978) pp. 101–108.

[37] Stonebraker, Michael, E. Wong, et al., "The Design and Implementation of INGRES." ACM Transaction on Database System, Vol. 1, No. 3 (1976) pp. 189–222.

[38] Teichroew, D. and E.A. Hershey, "PSS/PSA: A Computer Aided Technique for Structured Documentation and Analysis of Information Processing System." IEEE Trans. on Software Engineering SE-3 (1977).

[39] Washerman, Anthony I., Peter A. Pircher, D.T. Shewmake and M.L. Kersten, "Developing Interactive Information System with the User Software Engineering Methodology." IEEE Trans. on Software Engineering, Vol. SE-12, No. 2, 1986, pp. 326–347.

[40] White, D.J., Decision Theory. London: John Wiley and Sons, 1965.

[41] Yadav, Surya B., “Determining an Organization’s Information Requirements: A State of the Art Survey.”, DATA BASE, Vol. 14, No. 3, 1983, pp. 3–20.

[42] Yadav, Surya, B., “Classifying An Organization to Identify Its Information Requirements: A Comprehensive Framework”, Journal of Management Information Systems, Vol. II, No. 1, 1985, pp. 39–60.

[43] Yadav, Surya, B., A Methodology for Modeling an Organization to Determine and Derive Information Systems Requirements. Ph.D. Dissertation, Georgia State University, 1981. Available from University Microfilm International., Ann Arbor, Michigan, U.S.A.

[44] Yeh, R.T. and A. Araya et al., "Software Requirements Engineering - A Perspective." Structured Software Development. State of the Art Report, Infotech, Intl., Ltd., 2 (1979).

[45] Young, J.W. and H. Kent, "Abstract Formulation of Data Processing Problems." Journal of Industrial Engineering (1958) pp. 471–479.

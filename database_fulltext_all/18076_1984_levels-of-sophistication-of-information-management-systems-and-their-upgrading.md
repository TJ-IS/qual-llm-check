---
otero_id: 18076
otero_key: "7YN4A9EB"
title: "Levels of sophistication of information management systems and their upgrading"
authors: "Victor L. Pérez"
year: "1984"
journal: "Information & Management"
doi: "10.1016/0378-7206(84)90005-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Levels of Sophistication of Information Management Systems and Their Upgrading

Víctor L. Pérez

Departamento de Ingeniería Industrial, Universidad de Chile, Casilla 2777, Santiago, Chile

The organizational Information Management System is identified, analyzed and evaluated. In order to identify it, the objectives and functional components of such a system are described; then, the different levels of sophistication of the alternatives implementing each one of the system components are presented. A proposed “upgrading approach” is applied to analyze the information management activities within the organization.

Keywords: Information management systems, information systems, logical information management, physical information management, information administrator, data base administrator.

![](/api/attachments/7YN4A9EB/fulltext/images/0a218a23c45c72caedbd8a9de338d66dfb379a70bf4a5410526e50da1d9d7e9b.jpg)  
Victor L. Pérez is Chairman and Professor of Management Information Systems of the Departamento de Ingeniería Industrial at the Universidad de Chile, Chile. He has published in several international journals on MIS, and he is the co-author of seven books on Information Systems. He has served as consultant to several governmental, business and international (PAHO, UNESCO) organizations.

## 1. Introduction

The allocation and management of informatics resources (i.e., information, administrative procedures, files content, application software, software products, documentation) are critical factors in organizations. As the organizational structures become more complex and the volume of and the relationships among data transactions continuously grows, the process of determining the real costs and benefits of an Information System (IS) during its development and operation becomes more difficult. This problem has lead administrators to look for better methods of allocation and management of informatics resources, while systems analysts and programmers have been trying to utilize more efficient tools to manage the allocated resources.

The interest in improving the efficiency and effectiveness of the IS has resulted in an increasingly rapid development of conceptual methodologies and technical tools; e.g., [2,3,7]. On the other hand, the tools have been directed towards the analysis, specification, selection and operation of alternative ways of implementing the activities of the IS life cycle in the most efficient manner; e.g., [1,6,9,10].

Such methodologies and techniques when dealing with the activities involved in the management and usage of the information have, however, failed to provide the proper relationship between the logical (what) and the physical (how) aspects of such activities; the logical aspects deal with the identification of the organizational processes that those activities are to support, whereas the physical ones consider how such activities are to be implemented.

Up to now, the design criteria has generally focussed on the optimization of the computerbased aspects of the information management and its usage.

The organizational aspects have not received the same attention. We observe an increasing interest in the cost reduction of all activities in software development, system physical design and computer-based activities, whereas the organizational decision-making structures and processes generally have been ignored, even though they ought to determine the required implementing features and facilities [5].

The reasons behind this bias, we believe, are to be found in the general lack of knowledge and/or misconceptions of the organizational Information Management System. We shall use our experience in system design to present a generalization of the information management field within the organization. From this experience, we conclude that we can apply a systems approach that considers both the logical and physical aspects of the Information Management System. At the same time, we suggest a way to avoid a biased perspective in evaluating and selecting a given set of data manipulation activities and facilities through an upgrading approach.

## 2. The Information Management System

Organizations depend heavily on the way the information was historically used and managed. Several authors have identified the different stages in this evolutionary process; e.g., [4]. Today the development of an IS is carried-out, in most firms, in an independent manner, with little or no cross-referencing, documentation, and coordination of objectives, priorities and resources. Furthermore, this has triggered a “non-integrated” mode of managing and using the information within the organization, with origins in the growing but overlapping and “rearranging” of computer-based administrative processes and procedures.

We are not suggesting that all IS are always developed in a non-integrated way, but that even when integrated approach to the IS design is used, each IS is considered as an independent and isolated system. Furthermore, if we consider that a set of data usage-manipulation activities has to be designed as an interrelated element of one Information System, we must also consider that set as an interrelated element of another system that includes all the other organizational data manipulation activities: the Information Management System. There must be consistency between the objectives of both systems if we wish to optimize with respect to the objectives of the organization.

The following are some requirements to be accomplished by the Information Management System:

\- Information must be considered a resource and, as such, analyzed with respect to its effectiveness and methods of allocation.

A tactical decision-making level should therefore administer the management and control of the information resources.

\- If possible, organizational information as well as its interrelationships should be stored only once to avoid redundancy and ambiguity; if it is necessary to duplicate (e.g., for reasons of efficiency), duplication should be controlled carefully in order to reduce errors.

\- It is necessary to provide adequate methods for defining this single, standard informatic resource.

\- Different types and levels of users require different interfaces, data manipulation tools and user oriented communication facilities.

\- In order to share information among different applications, privacy and integrity must be considered.

\- There must be an administration unit in charge of the physical design and implementation of the Information Management System.

We therefore present the functional components of the IM system, figure 1(a). But before describing them, we make a clear distinction between two types of attributes of data elements: logical attributes (those in the user's interest; e.g., data-type names, synonyms, or definitions), and physical attributes (of interest to the implementers who choose methods of storing, manipulating and retrieving the data values; e.g., size, format, access type, storage media).

The logical attributes are the responsibility of Logical Information Management and the physical attributes of Physical Information Management.

The IM System can thus be decomposed into the following functions:

a) Demand (DE). The DE function has to generate the users' information requirements that are characterized and specified by the Logical Information

![](/api/attachments/7YN4A9EB/fulltext/images/bdd2c83c35e826047ccd35596df4fcfdfcc39ac4339cd3c95932eef014724df0.jpg)  
Fig. 1b. Functional Diagram of the Information Management System.

Management function and that are satisfied through the Data Storage/Data Manipulation Management function.

The users will interact with data and logical attributes values in the manner of figure 1(b).

b) Logical Information Management (LIM). The objectives of the LIM function are (from the users' point of view) the data identification, characterization, control, and standardization. To define LIM needs, we state the different logical attributes describing each of the data-types.

Among the general activities (or sub-functions) carried out by the LIM function, we have: (1) users' information requirements determination; (2) design of the administrative procedures for the definition and control of data usage and manipulation; and (3) specification of the users' data usage and manipulation requirements.

Within the first general activity there are the following tasks: (1) identification of the relationships between the decisions taken and the information that should support them; (2) specification of users' information requirements; (3) search for and identification of data required for future applications; (4) data inventory and analysis; (5) determination of data usage parameters; (6) identification of cost and benefit parameters. Though the cost of the information is relatively well known, it is difficult to assess the benefits of that information. Here, we must introduce the user's subjective considerations on the need to use that information to support decision-making activities. This problem becomes increasingly complex when decisions are less structured and users allocate different relative weights to data within their personal management scheme.

Among the tasks of the second activity, we have to distinguish the administrative procedures designed as part of the IS from those designed as a way of communicating and implementing organizational-wide data definition and manipulation activities. Our concern is the latter, even though we recognize the necessary coordination that must exist among those two types of procedures; furthermore, that coordination is a LIM task.

The third activity requires a method of documenting, for different decision-making levels, all attributes and administrative procedures defining and governing the data usage and manipulation activities within the organization.

c) Physical Information Management (PIM). The objective of this function is to translate the Logical Information Management specifications into a physical design: here we design, specify, and control the particular way the organization chooses to implement its information requirements.

Among the activities of this function are:

i) Identification, characterization, design, control, and evaluation of all the data manipulation processes required to produce the information outputs from the input and stored data.

ii) Identification, characterization, design, specification, implementation and evaluation of all the facilities to be used in order to implement the objectives of the Data Storage/Data Manipulation Management function.

iii) Definition of all the physical data attributes.

iv) Design of the particular way the organization chooses to implement its data definition, data manipulation, and data security activities; this must be constrained by the other activities.

v) Definition of the data and storage structures to be manipulated (not necessarily in an automated mode) by the Data Storage/Data Manipulation Management function and to be implemented through the Data Storage function.

vi) Design, control, and evaluation of the necessary monitoring facilities and processes that determine the nature and frequency of data usage for the Data Storage/Data Manipulation Management function.

vii) Specification of the administrative procedures by which the organization implements the Physical Information Management, the Data Storage, and the Data Storage/Data Manipulation Management functions.

d) Data Storage and Data Manipulation Management (DS/DM). The objective of this function is to provide the necessary facilities to describe, create, store, access, manipulate, retrieve and protect the data and its attributes. It also provides procedures to control the performance of these facilities.

e) Data Storage (DS). The DS function materialize the storage of all the data in the IM System: the physical storage of data values, as well as their logical and physical attributes. We can extend these functional objectives to include the storage of the attributes describing all other informatics resources.

## 4. Functional Components Analysis

## 4.1. Implementation Alternatives

The means and resources allocated by the organization to fulfill the needs to manipulate and use data may vary from one IS application to another, but the objectives of the IM system components remain the same. The variations would depend, among others, on: (1) the structure of its financial decision making process, (2) the degree of technological sophistication introduced into and available to the organization, and (3) the informatic maturity of the organization.

In Table 1, for each function or component we have a number of steps, each representing an alternative way of implementing the objectives and activities of that function. Each column was built so that each step or method in the column represents an increasingly difficult approach (methodological and/or technically speaking) in the way it could be implemented.

Furthermore, if we analyze IS applications we find that they implement their data usage-manipulation activities according to approaches peculiar to either the application or the organization; in practice, the implementation of any given approach is nothing more than selecting, for each IM component, one specific step in each column. Thus, it would be possible that the development and operation of one IS is implemented with one set, whereas for another the chosen set could be different.

Note that if it is said that the component DE is implemented through one of the steps in the column, there is at least one organizational effort that uses this level of sophistication to carry-out the objectives of the component; it does not imply necessarily that all IS developments use the same way of implementing their DE function. In order to distinguish the column elements, an alphabetic subscript is used (e.g., LIM(b) for the second LIM).

## 4.2. Relationships between Steps

In order to formalize the relationships to be found among the steps shown in Table 1, several cases of IS applications are presented:

\- Case A: All Information Systems (IS) within the organization are manually-operated and informally defined. The components are not very well recognized and they are implemented most of the time following the data users' own cleverness. One possible approach implementing this type of IS could be the set of DE(a) through DS(a) of the first item in each column.

\- Case B: The introduction of computer-based applications allows IS to be implemented in a more formalized way. At first, IS tend to be developed in an independent manner, with almost no documentation; the IS development techniques are based either on the systems analysts' own experiences or on the users' requests. Examples of applications of this type are found in small and medium size firms entering Nolan's second stage (i.e., "contagion" [4]). In Case B, each IS implements its own data usage and manipulation activities according to its assigned resources and goals. Then, within each IS, the components are implemented following the set: DE(a), LIM(a), PIM(b), DS/DM(c), DS(b); or: DE(b), LIM(b), PIM(b), DS/DM(c), DS(b). It is not uncommon, though, to find organizations that then change by advancing the sophistication of the technological components (i.e., DS/DM and DS); e.g., as DE(b), LIM(b), PIM(c), DS/DM(d), DS(c).

\- Case C: After some experience with computer-based IS, organizations introduce the use of methodologies and techniques integrating (or, at least, coordinating) the design and implementation of either the logical-oriented components (i.e., DE and LIM) or the physical-oriented components (i.e., PIM, DS/DM and DS) for all their IS applications. In the first case the components could be implemented according to the set of steps: DE (c or d), LIM (c or d), PIM(c), DS/DM(c), DS(b). In the second case the implementation set could be: DE(b), LIM(b), PIM(d), DS/DM (d or e), DS (c or d).

\- Case D: A variation of Case C is produced when the simultaneous but mutually independent integration of both the logical-oriented and the physical-oriented components occurred. Generally the logical aspects of all the IS applications are materialized through the Industrial Engineering Department while the physical ones are the Computing Center and/or the Systems Department responsibilities. One implementation alternative is the set: De(d), LIM(d), PIM(e), DS/DM(e), DS(d).  
- Case E: Mature organizations entering Nolan's fifth stage (i.e., "Data Administration" [4]) consider that all the elements pursuing the implementation of their information management objectives conform to a system (i.e., that of the overall organization). Logical data usage and manipulation activities are identified after organization-wide analysis of the data required to support decision making. The implementation of those activities attempts to optimize two objectives: (1) the physical design objectives of each one of the information systems, and (2), those of the organizational IM system as a whole; in both cases the constraints are, among others: the available resources, the level of informatic maturity reached by the organization through its current information systems, and the IS development policies. One way the organization may implement the IM functional components is, in this case, through the set: DE(e), LIM(e), PIM(f), DS/DM(f), DS(e).

TABLE 1
Implementation Alternatives for Each Functional Component of the Information Management System

<table><tr><td>DE</td><td>LIM</td><td>PIM</td><td>DS/DM</td><td>DS</td></tr><tr><td rowspan="2">a) User defines own information requirements, mainly in independent and arbitrary manner.</td><td rowspan="3">a) There is neither formal knowledge nor a set of supervisory procedures over the specification of user information requirements; lack of awareness of redundancy, ambiguity and inconsistency in the data, and in corresponding manipulation procedures.</td><td rowspan="2">a) User defines, either explicitly or implicitly, manually-operated data storage-manipulation procedures; unaware of alternative procedures.</td><td>a) User carries-out own data storage-manipulation procedures manually and independently.</td><td rowspan="3">a) User stores data in arbitrary, dispersed, unordered, unspecified and independent manner; manually-implemented data storage medias with poor cross-referencing and updating.</td></tr><tr><td rowspan="2">b) User follows given manually-operated set of cross-referencing indexes to perform data storage-manipulation activities.</td></tr><tr><td rowspan="2">b) Identification of users&#x27; information requirements is joint work between each application user and systems analysts.</td><td rowspan="2">b) Application programmer defines, in each program, the data storage-manipulation scheme and procedures; no considerations of interrelationships and/or overlapping.</td></tr><tr><td rowspan="2">b) Formal specification of computer-based data manipulations activities; manual activities either ignored or not documented.</td><td rowspan="2">c) Computer-based procedures (inserted within each application program) defining and performing data storage and manipulation operations.</td><td rowspan="3">b) Computer-based data storage; each IS application stores data; improvements in manually-implemented data storage operations and facilities.</td></tr><tr><td rowspan="2">c) Users relate the identification of information requirements with decision-making processes to be supported.</td><td rowspan="2">c) Design of all data storage-manipulation scheme and procedures is responsibility of systems analysts; design process supported through the use of standard techniques (e.g., access methods).</td></tr><tr><td rowspan="2">c) User information requirements (mainly physical aspects) specified through formal languages; responsibilities of information analysts recognized and implemented.</td><td>d) Data storage and manipulation activities carried-out by powerful software products (e.g., file management systems).</td></tr><tr><td rowspan="2">d) Coordinated formulation of users&#x27; information requirements; first attempts relating activities with design of functional decision-making processes.</td><td rowspan="2">d) IS physical design process considers interrelationships among several applications; general purpose data manipulation software utilized; awareness of need to identify data physical attributes.</td><td rowspan="2">e) Use of generalized data storage and manipulation software (e.g., DBMS package); emphasis on data protection and management of very large data volumes; availability of data communication and user interface facilities.</td><td rowspan="2">c) Implementation of data storage integrates several applications through better cross-referencing techniques.</td></tr><tr><td rowspan="2">d) Some techniques used to implement and control identification and standardization of data physical attributes (e.g., Data Dictionaries); formal procedures specifying logical aspects of user information requirements.</td></tr><tr><td rowspan="2">e) Identification of user information requirements as a result of organization-wide Informatics Plan.</td><td>e) Responsibilities for a Data Base Administrator defined and implemented.</td><td rowspan="2">f) Implementation of software supporting data communication networks and distributed processing; availability of mini-computers and personal computers; introduction of office automation concepts.</td><td>d) Introduction and implementation of data base concepts for storage of data and descriptions.</td></tr><tr><td>c) Responsibilities of an Information Administrator defined and implemented; identification and characterization of logical attributes for the data and other informatics resources.</td><td>f) Design of data storage-manipulation-protection scheme and procedures supported through generalized software (e.g., DBMS packages); responsibilities for communications or network management defined and implemented.</td><td>e) Introduction and implementation of distributed data base concepts.</td></tr></table>

## 5. IM System Components Evaluation

The organization must therefore decide how to select a proper set of ways to implement its IM System; we see that the design objectives would tend to balance the ways of implementing the system activities as a whole, as well as each function. No matter how elementary and unsophisticated the methodologies and techniques chosen, there must be adequate consideration of both the logical and physical aspects. The search for that balance is the objective of our upgrading approach.

The way we attack this problem is by considering Table 1 as a “profile table” of IM activities. With such a table, we identify approaches (i.e., steps in each of the functions) actually used in the organization.

There are certain cases where relationships exist between the implementation of two or more functions. As an example, the use of a DBMS package in the DS/DM function implies the use of a data base in the DS function, (an induced relationship); as another example, the use of a DBMS package suggests the use of a Data Base Administrator in the PIM function (a complementary relationship); finally, the use of a data base in the DS function does not provide full benefit unless there is an Information Administrator in the LIM function, (an advisory relationship).

Also, we see that if a function is implemented according to a given step, that may imply that a set of techniques-procedures-methodologies-equipment-and informatic resources must also be used to implement another function according to a more advanced step. Thus, the way of implementing one step may force the upgrading of another.

There are, however, some cases where the upgrading in a function is seen by administrators as independent of the upgrading of another; furthermore, they usually see the need for entering the upgrading process only as a way of getting technological sophistication, affecting only the DS/DM and the DS functions with no considerations of the costs and benefits and the effect on the overall management activities. This shows another use of Table 1 – as a means for selecting or planning upgrades; we face two questions:

(1) Which functions should be upgraded to better the IM activities?, and

(2) what is the effect of upgrading one function on all the other functions?

The first question was presented as if there is a real interest in identifying and analyzing the reasons behind a possibly poorly managed activity. In this case, Table 1 allows the naming of the functional steps in the upgrading process, as well as the sequence order and priorities that should be followed. Suppose that an analysis shows that, within an organization, IM functions are implemented following the set DE(b), LIM(b), PIM(c), DS/DM(c), DS(b). If the latest decision is to introduce a DBMS package in order to develop a financial-oriented data base, the organization must upgrade at least two components: DS/DM and DS. Therefore the resulting implementation set for the IM system would be DE(b), LIM(b), PIM(c), DS/DM(e), DS(d); but this is an unbalanced set. One approach should be: (1) upgrade DE(b) to at least DE(d), (2) upgrade functions to LIM(d) and PIM(e), (3) only after this has provided a specification of the data usage and manipulation requirements should the organization upgrade to DS/DM(e) and to DS(d). The same suggested approach could be applied if our analysis shows that the set actually implemented is DE(b), LIM(b), PIM(c), DS/DM(e), DS(d); it is not uncommon that the DBMS package is bought first and that the decisions about what to do with it are made later!

The second question was presented positively. However, generally we tend to upgrade one function without consideration of the others, except when forced to do so (e.g., with a DBMS package implementing a database). From time to time, questions arise about the quality and costs of existing IS (or about the costs involved in the development of new IS or the resources being spent for data processing activities, etc.); the solutions being proposed for such problems almost always have a common factor: the search for more sophistication in the data processing software and hardware. There is a tacit assumption that we solve IM problems through technological solutions while organizational and functional factors receive little or no consideration. Moreover, IM problems are only seen as technological.

Today the “common” technical solution of the IM field is DBMS (probably with data communication facilities also). This results in dissatisfied users, expensive IS applications, utilization of larger computers, etc. [8]. In contradistinction our upgrading approach states that we first identify the current IM situation and then use Table 1 to state future data usage and manipulation requirements, alternative solutions and final implementation; following this approach, a DBMS package will get its proper place as a solution of proper problems, whereas other IM deficiencies will be identified and solved. We believe that with this approach, major problems will not be experienced. So, DBMS becomes just one way of implementing the DS/DM function; its usefulness, however, will be achieved only with a balanced approach.

A sketch of this upgrading process is given in Figure 2. In order to use it, the following steps should be considered:

a) There must be reasonable knowledge of the decision-making structure and those processes upon which the structure is supported (by functions, objectives, resources and administrative procedures); there must also be an understanding of the relationships among those processes and the existing IS within the organization. These produce either an organization-wide Informatics Plan or a Global Design Analysis, i.e., the framework within which individual applications are specified.

b) It is necessary to consider all the parameters related to the IS policy (short/medium/long range), for example: (1) the degree of saturation of the current computer system, (2) technological obsolescence of the supporting software, (3) degree of saturation of the administrative procedures, (4) user satisfaction with the existing IS, (5) degree of relationship among the existing IS, (6) existing data redundancy, (7) decision-making levels and organizational functions being supported.

c) Knowledge of the criteria and priorities guiding the degree of implementation of the IM System (including knowledge of functional components, types of activities achieving functional objectives, types of administrative units involved, types of schedules directing the implementation process, etc.).

d) Existence of feasibility studies of the different data usage and data manipulation processes, including: (1) characterization of the attributes of the data manipulated by existing and planned IS, (2) characterization of the logical and physical data manipulation activities (with corresponding efficiency and effectiveness measures), (3) job-descriptions and the corresponding administrative procedures for the Logical and Physical Information Management functions, (4) recommended logical and physical implementation features of the DS/DM and DS functions.

e) An approach carrying-out these steps would allow an integrated analysis of current and required informatics resources. Results from this analysis are the input data to an organization-wide Informatics Plan producing a definition of policies for the formulation and implementation of information management activities.

f) A preliminary result from previous step (e) is the identification of unbalanced approaches of implementing different components. Directives stating how to cope with such inbalances are the main goal of this identification process (e.g., redesigning the IS, or upgrading some of the IM components either as a system or as each IS application).

g) Identification of the needs for an administrative implementation of the approach chosen for the different information management activities (i.e., which components are to be upgraded, the opportunity and sequence in which the upgrading process is to be accomplished, the highest level to which each IM component is to be upgraded).

h) The sequence in moving an organization from Case A to Case E (section 4) is an alternative way of implementing an upgrading approach.

## 6. Final Comments

At the start of this paper, we presented some of the deficiencies that we see in the IM activities within organizations. In an effort to identify the logical as well as the physical considerations governing those activities, we defined an Information Management System. Then, as a way of characterizing that system, we presented its objectives and functional components; we also identified the interrelationships between those functions and the alternatives for implementing them.

![](/api/attachments/7YN4A9EB/fulltext/images/115c57fb5a66f6819f62042cd351ccbe1b5a4c4857ba9a58bb8e5eab904e1fe9.jpg)  
Fig. 2. Implementation Activities for an Upgrading Approach.

As a result of this way of understanding and implementing the usage, manipulation, and management of the organizational information, we proposed an upgrading approach to information management. This approach is balanced: the full benefits of either a technological or a methodological improvement to information management activities will only be achieved if organizations are able to identify their real information requirements, as well as match requirements with the implementation of the appropriate data usage-manipulation tools and techniques.

Applying such an upgrading approach, the administrators have the opportunity not only to concentrate on how the organization influences the selection and evaluation of a package, but also to question their own management processes (in so far as they are related to the formulation of management and information systems development policies). Our approach has been used as an evolutionary guide, indicating a logically sequenced set of activities to be used in changing a poorly managed situation into an effective and balanced approach to information management.

## References

[1] F.W. Allen, M.E.S. Loomis, and M.V. Mannino, The integrated dictionary/directory systems, Computing Surveys, Vol. 14, No 2, June 1982, pp. 245–286.

[2] O. Barros, V.L. Pérez, and A. Holgado, Structured logical design of information systems: a methodology, documentation and experience, Information Systems, Vol. 4, No 1, 1979.

[3] B. Langefors, Theoretical analysis of information systems, Studentlitterature, Lund, 1968.

[4] R.L. Nolan, Managing the crises in data processing, Harvard Business Review, Vol. 57, March-April, 1979, pp. 115–126.

[5] V.L. Pérez, Factors challenging information technology applications in developing countries, Information and Management, Vol. 3, No 4, 1980.

[6] V.L. Pérez, R. Schüler, The Delphi method as a tool for information requirements specifications, Information and Management, Vol. 5, No 3, 1982, pp. 157–167.

[7] H.J. Schneider (ed), Formal models and practical tools for information systems design, North-Holland Publishing Co., 1979 (ISBN: 0-444-85394-4).

[8] E.H. Sibley, The impact of database technology on business systems, Information Processing 77, North-Holland Publishing Co., 1977.

[9] W.M. Taggart, M.O. Tharp, A survey of information requirements analysis techniques, Computing Surveys, Vol. 9, No 4, Dec. 1977, pp. 273–290.

[10] D. Teichreow, E. Hershey, PSL/PSA: a computer aided technique for structured documentation and analysis of computer-based information systems, IEEE Trans. of Software Engineering, Vol. 3, No 1, Jan. 1977, pp. 41-48

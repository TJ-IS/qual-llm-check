---
otero_id: 18632
otero_key: "CAKUBK57"
title: "Work flow methodology"
authors: "Faten F. Mahmoud; Sherif A. Mazen"
year: "1990"
journal: "Information & Management"
doi: "10.1016/0378-7206(90)90047-l"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Work flow methodology

# A proposed approach for analysis and conceptual design of large scale computer based information systems

Faten F. Mahmoud and Sherif A. Mazen
Department of Statistics and Information Systems, Kuwait University, Safat 13055, Kuwait

The objective of this paper is to explain our approach called “Work Flow Methodology for Analysis and Conceptual Data Base Design of Large Scale Computer Based Information System”. The user fills in, through the different steps of the methodology and in the light of the definition of dynamic adaptive system, a number of forms which relate the topological dimension to the time dimension for each application of a given system. In addition, we obtain the “Unit Subschema” which defines the responsibilities of issuing and authorization of receiving information at the proper time. Finally, we apply our methodology to the Registration System in Kuwait University.

Keywords: Work flow methodology, Work flow diagram, Event form, Data pool, Matrix of units versus data stores, Matrix of units versus data elements, Unit subschema, Conceptual design.

## 1. Introduction

According to Grindley [1], reality can be formulated as a dynamic system. Furthermore, such systems can be represented as a closed loop feedback system, such that the originating signals, which represent plans or courses of action, are used as a stimulus to the structure of the reality which reacts to produce actions. Meanwhile, the behaviour produces feedback signals as a reaction to the inputs and, mostly, modify the characteristics of the system ingredients. The reality is composed of two basic components, firstly, the control component, which receives originating signals from the environment and issues instructions to the behavioural component; this, in turn, is responsible for producing actions and responses. Due to this output, feedback signals (external ones) may be received by the control component and it must then issue new instructions and corrections. Internal feedback signals, received by the two components of reality, modify their structure or attributes. The system would be adaptive if internal feedback exists.

Figure 1 shows the idealization of reality as a

![](/api/attachments/CAKUBK57/fulltext/images/f0f9e96281cf7f9caea452dd98e2d06776f5e5cd5e282d0ba5c8473720ca440d.jpg)

Faten F. Mahmoud is a professor of computer based information systems at Kuwait University. He is on leave from Zagazig University, Egypt. He received a Ph.D in computer aided design from Acronautical Engineering Department, Cairo University in 1973. He was the project leader for many national information systems in Egypt, Morocco, Tunisia and Kuwait. He has published many articles in Int. Jour. of Applied Mathematical Modelling, Computers and Structures, Int. Jour. of

Numerical Methods for Engineering, Engineering Fracture Mechanics, Wear, and Jour. of Applied Mechanics. Prof. Mahmoud is a member of ASME, IACM and Egyptian Society of Scientific Computations.

![](/api/attachments/CAKUBK57/fulltext/images/775b63ca0d9e793c74347366d0da9e4891af4782cc0bb3fc696bb0aa92bdb6b5.jpg)

Shed A. Mazen is an assistant professor of computer based information systems at Faculty of Commerce, Kuwait University. He is on leave from Cairo University, Egypt. He received his B.Sc. degree in Accounting from Faculty of Commerce, Cairo University. He holds an M.Sc. in Management and Ph.D. in Applied Informatics in Management from University of Toulouse I, Toulouse, France. His research interest focuses on analysis and design of large scale computer based information systems.

![](/api/attachments/CAKUBK57/fulltext/images/1f6bbbe893b2f5ad9c238bdb580e00f2ef7c88ea83859f6f862c5d022dfb9bb1.jpg)  
Fig. 1. The Reality as a Closed Loop Adaptive System.

closed loop adaptive system. Figure 2 illustrates the steps in transmission and transforming input signals to output actions. Accordingly, if we consider the information system as an equivalent model for reality, we must identify and differentiate between the different types of data elements. Data elements, which describe components of reality, are called entity attributes. Both input signals and output actions represent the development of the system states across time. Data elements corresponding to states are called “Operational Data”. Internal and external feedback signals are represented by control and follow-up data elements. Figure 3 shows the relations between information system and the components of reality, control, and behaviour, in conjunction with relationships between information system, organization system, and motivation system.

Most of the available methodologies take into consideration either time dimension or topological dimension to represent the reality of the organization. The proposed work flow methodology adopts both dimensions to represent the organization as an adaptive dynamic system.

## 2. Highlights on Some Available Methodologies

In the literature of structured systems analysis and design $[2,3,4,5,6]$ , we find a wide variety of methodologies and techniques that differ in scope; each has its own strengths and weaknesses. Our comparison will cover the following methodologies:

\- Structured Analysis and Design Technique (SADT).

\- Information Engineering (IE).

\- Structured Requirements Definition (SRD).

\- Jackson System Development (JSD).

![](/api/attachments/CAKUBK57/fulltext/images/cadd663fef5335df3213d880cdfb983a43b15a80486f5ac72d04508b09405e36.jpg)  
Fig. 2. Transmission of Input Signals to Output Actions.

![](/api/attachments/CAKUBK57/fulltext/images/a0a724ba7e6adf02ba20527b0a985c5ef9b17436cfec1c2b038fced07ef2f143.jpg)  
Fig. 3. Relations Between Information Systems and Reality.

\- Higher-Order Software (HOS).

\- Prototyping.

## 2.1. Structured Analysis and Design (SADT)

SADT [7,8,9,10] concentrates on the data flows through the different functions of the system under study. The structured tools used in this methodology are “Data Flow Diagrams (DFDs)” and “Structure Charts”. DFDs, which are supported by a Data Dictionary and Minispecifications, are used to develop logical and functional module hierarchies (Structures Charts), but not physical attributes. The focus is on the graphical representation of the system with its external entities, processes, data stores and data flows. One important feature of SADT is that the definition begins with the present physical system; it is converted into the present logical system. During the process, a normalized data structure eliminating all duplicate and unnecessary data is developed. This is converted into a logical system and thus to the proposed logical system satisfying the new system requirements. At this stage it is possible to provide the new physical design of the proposed system; this is crucial for the testing and implementation phases.

## 2.2. Information Engineering (IE)

IE [11,12] covers logical and physical data base design and interfaces with management techniques (corporate, strategic requirements and organizational planning). Systems designed according to this methodology are not based on flow of data but on normalized and related data. IE does not take into consideration the time dimension; the data model emphasizes data storage and data update.

## 2.3. Structured Requirements Definition

Structured systems development was defined by Kenneth Orr [13] as “output oriented design”, and he states that “it is not always possible to elicit the required outputs from the user”. So we must have “a requirements definition process that works from a definition of the problem to the definition of the outputs”. The tools used in structured requirements definition are the Warnier/Orr diagram, which is a series of brackets that can represent system, program, and data hierarchies, and the entity diagram, which charts information flows (outputs) between entities. The main disadvantage of this methodology is that the emphasis is on the outputs and their contents, which implies considerable duplication of data.

## 2.4. Jackson System Development (JSD)

JSD is defined by Michael Jackson [14,15,16] as “a method for specifying and implementing computer systems. These activities include requirements specification, functional specification, logical system design, program specification and design, program implementation, and system and program maintenance.” The effective use of JSD needs a very competent person and can consume large amounts of development time.

## 2.5. Higher-Order Software

The important concept of HOS is mathematical correctness of the program code without programmer participation.

## 2.6. Prototyping

In system design, a prototype $[17,18]$ can be either a model for further development or a full-scale functional system. By using software tools such as fourth-generation languages and application generators, it is easier to build the prototype. We note that the combination of certain techniques and methodologies can improve their value.

From these brief presentations of the main aspects of each methodology, we can note that none covers time and topological dimensions.

![](/api/attachments/CAKUBK57/fulltext/images/ccea843467a9aab938fbf85a58e3251174dd81d8c2b08e642c7187e78f2b6be0.jpg)  
Fig. 4a.

## 3. Work Flow Methodology

The steps of the proposed methodology are described on the light of the definition of dynamic adaptive system.

## 3.1. Work Flow Diagram

At any specific instant, a given system can be defined by a state vector, composed of different operational data items used in different activities and operations. The dynamic level of the system can be determined by tracing the system state vector across time.

The system may also be described by identifying the of organizational units involved and responsible for processing data at each instant. In other words, the system can be realized by action flow diagrams; therefore the flow is concerned mainly with organizational units.

The idea of representing the flow of activities or data in a system of charts is not new. Diagrams enable us to describe an existing system or a proposed new one logically without considering the physical environment of data or process. Several structured methodologies as SADT, Warnier/Orr, Data Flow and Jackson System Development methodology are based primarily on types of diagrams used to formulate the information concerning systems of a given reality.

Nevertheless, most of the methodologies, classical or structured, use diagrams to represent systems but consider only one of the two dimensions: time or organizational unit. The proposed work

![](/api/attachments/CAKUBK57/fulltext/images/c9bd98bf4ae7e71ec2ebf387c6d10ec7ebedfdd52f9dd0c1ebb70fe56d437b44.jpg)  
Fig. 4b. Work Flow Diagram.

Name of System: Registration Application Code:

App.(1)

Event Code: E1

<table><tr><td>Input</td><td>Details of Process CodeProcess Code or narrative</td><td>Output</td></tr><tr><td>1.InputCode:S1Source:Event:Unit:</td><td>1.The student receives the schedule course and registration sheet from the advising and guidance division.</td><td>1.OutputCode:S2Destination:Event:E2Unit:U2</td></tr><tr><td>2.InputCode: S2Source:Event:Unit:</td><td>2.The guide helps the students in filling the registration sheet.</td><td>2.OutputCode:Destination:Event:Unit:</td></tr><tr><td>3.InputCode: S3Source:Optional:Event:Unit: U5Optional:</td><td>3.The student registers his courses in Scientific Departments.Requirements:Duration:Start:End:</td><td></td></tr><tr><td>4.InputCode: S4Source:Event:Unit: U5</td><td></td><td></td></tr></table>

Fig. 5. Details of Event Form For E1.

flow methodology takes into consideration both dimensions; it represents the flow of data and actions of information system and is limited to the analysis and conceptual design phases.

The procedure adopts the convention of activity networks in developing the time scale as an ordered set of instances called “Events”. At each timed event “E” the interactions between the organizational units and data stores, whether input or output, are diagramed on the time scale by a work flow diagram (WFD). Several units may undertake the data processing activities at the same time (event). To draw a work flow diagram, some symbols and conventions are shown in Figure 4a, where the connectivity between events and units use special connector symbol to reveal their source or destination unit and event. Figure 4b illustrates part of a (WFD). For the sake of clarity and comprehension, the details of each event is placed in a special form as shown in Figure 5.

## 3.2. Data Pool

From the analysis of the existing data stores (forms) which are manipulated in all applications of the system, a list contained all data elements will exist in various forms, and consequently, in the total system, as shown in Figure 6. If only one application is being analysed, its application sub-schema will be obtained. But if we consider all applications of the system, a crude data schema representing the total system will result. Using a canonical data structure technique, the crude schema is transformed to a well structured one.

## 3.3. Matrix of Units Versus Data Stores

The contents of (WFD) is transformed into a matrix form which gives relationships between the unit of organization and different data stores used in different activities of each application. This matrix is constructed by scanning the (WFD) events and determine the unit responsible for data processing, the triggered data store inputs, and the output data stores or transactions. Each unit involved in one application is assigned to a corresponding row of the matrix, where each data store is assigned to a specific column. The entries of the matrix represent the interaction between data stores and units. The interaction is described by a set of attributes, such as: event number, type of interaction (input/output), the frequency of data store use, the volume of data store, and the media of the data store. If we focus our attention on a specific column, we see that the column represents the flow of the corresponding data store across different units of organization, while each row summarizes all input/output data stores that interact with the corresponding unit of organization.

<table><tr><td rowspan="2">Data Elements</td><td colspan="11">Data Stores</td></tr><tr><td>S1</td><td>S2</td><td>S3</td><td>S4</td><td>S5</td><td>S6</td><td>S7</td><td>S8</td><td>S9</td><td>S10</td><td>S11</td></tr><tr><td>D1</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td></tr><tr><td>D2</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td></td></tr><tr><td>D3</td><td>X</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>D4</td><td>X</td><td>X</td><td>X</td><td></td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td></tr><tr><td>D5</td><td>X</td><td>X</td><td>X</td><td></td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td></tr><tr><td>D6</td><td>X</td><td></td><td>X</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>D7</td><td>X</td><td></td><td>X</td><td></td><td>X</td><td>X</td><td></td><td></td><td></td><td>X</td><td>X</td></tr><tr><td>D8</td><td></td><td></td><td>X</td><td></td><td>X</td><td>X</td><td>X</td><td></td><td></td><td>X</td><td>X</td></tr><tr><td>D9</td><td>X</td><td></td><td>X</td><td></td><td>X</td><td>X</td><td>X</td><td></td><td>X</td><td>X</td><td>X</td></tr><tr><td>D10</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td>X</td><td>X</td><td>X</td></tr><tr><td>D11</td><td></td><td></td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td></td><td>X</td><td>X</td></tr><tr><td>D12</td><td></td><td></td><td></td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td></td><td>X</td><td>X</td></tr><tr><td>D13</td><td></td><td></td><td>X</td><td>X</td><td></td><td>X</td><td>X</td><td></td><td>X</td><td>X</td><td>X</td></tr><tr><td>D14</td><td></td><td></td><td>X</td><td>X</td><td></td><td>X</td><td>X</td><td></td><td>X</td><td>X</td><td>X</td></tr><tr><td>D15</td><td></td><td></td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td></td><td>X</td><td>X</td></tr><tr><td>D16</td><td>X</td><td></td><td>X</td><td></td><td></td><td>X</td><td>X</td><td></td><td></td><td>X</td><td></td></tr><tr><td>D17</td><td>X</td><td></td><td>X</td><td></td><td></td><td>X</td><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td>D18</td><td>X</td><td></td><td>X</td><td></td><td></td><td>X</td><td>X</td><td></td><td></td><td>X</td><td>X</td></tr></table>

<table><tr><td rowspan="2">Data Elements</td><td colspan="11">Data Stores</td></tr><tr><td>S1</td><td>S2</td><td>S3</td><td>S4</td><td>S5</td><td>S6</td><td>S7</td><td>S8</td><td>S9</td><td>S10</td><td>S11</td></tr><tr><td>D19</td><td>X</td><td></td><td>X</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>D20</td><td>X</td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>D21</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>D22</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>D23</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>D24</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>D25</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td></tr><tr><td>D26</td><td>X</td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td></td><td>X</td><td></td></tr><tr><td>D27</td><td>X</td><td></td><td></td><td></td><td></td><td>X</td><td>X</td><td></td><td></td><td>X</td><td>X</td></tr><tr><td>D28</td><td>X</td><td></td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td>X</td><td>X</td><td>X</td></tr><tr><td>D29</td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td>X</td></tr><tr><td>D30</td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td>X</td><td>X</td></tr><tr><td>D31</td><td></td><td></td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td></td><td>X</td><td>X</td></tr><tr><td>D32</td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>D33</td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>D34</td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>D35</td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>D36</td><td></td><td></td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td></td><td>X</td><td>X</td></tr><tr><td>D37</td><td>X</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>D38</td><td>X</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Fig. 6. Data Pool.

<table><tr><td>Code of Data Stores</td><td colspan="4">Code of Departments</td></tr><tr><td></td><td>U1</td><td>U2</td><td>U3</td><td>U4</td></tr><tr><td>S1</td><td>I/TE1</td><td></td><td></td><td></td></tr><tr><td>S2</td><td>I/TE1</td><td></td><td></td><td></td></tr><tr><td>S3</td><td>I/S(-.5)O/D(2,5)E1</td><td>I/S(1,1)O/D(3,3)E2</td><td>I/S(2,2)O/D(4,4)E3</td><td>I/S(3,3)E4</td></tr><tr><td>S4</td><td>I/S(-.5)E1</td><td></td><td></td><td></td></tr><tr><td>S5</td><td></td><td></td><td></td><td>O/D(5,2)E4</td></tr><tr><td>S11</td><td></td><td></td><td></td><td>O/D(5,5)E4</td></tr></table>

Fig. 7. Matrix of Department/Data Stores For Application (1).

As a matter of fact, the conceptual matrix formulates the map of all system data store flows and actions across the units of the organization responsible for data processing activities. The attributes of the matrix entries can be extended to include type of processing (operational/control/decision making), the level of privacy or security, and the number of copies to be issued or received by the unit. The matrix of units versus data stores is shown in Figure 7.

## 3.4. Matrix of Units Versus Data Elements

By substituting each data store given in the previous matrix by its equivalent data elements in the data pool, we obtain a matrix describes the relationships between different units of organization and the data elements manipulated and processed in different operations. We consider the information system of an organization as a structure consists of three basic constructs: organization chart, conceptual data base and the relationships between the organization and its data base. According to that abstraction, we rely on the matrix of units versus data elements to formulate the information system. By using a canonical data structure technique, we can normalize the data pool to get a conceptual data base. Moreover, if we define the type of data according to its use as operational, control or entity description data, we can illustrate the map of the data pool and its evolution in terms of time, since the operational data (whether input, intermediate, qualified, or output) define the state of the system and this

<table><tr><td></td><td>U1</td><td>U2</td><td>U3</td></tr><tr><td>D1</td><td>I,U5O,U2E1</td><td></td><td>I,U2O,U4E3</td></tr><tr><td>D2</td><td>I,U5O,U2E1</td><td></td><td>I,U2O,U4E3</td></tr><tr><td>D3</td><td>I,TE1</td><td></td><td></td></tr><tr><td>D4</td><td>I,U5O,U2E1</td><td>I,U1O,U3E2</td><td>I,U2O,U4E3</td></tr><tr><td>D5</td><td>I,U5O,U2E1</td><td>I,U1O,U3E2</td><td>I,U2O,U4E3</td></tr><tr><td>D6</td><td></td><td></td><td></td></tr><tr><td>D7</td><td>I,U5O,U2E1</td><td></td><td>I,U2O,U4E3</td></tr><tr><td>D8</td><td></td><td></td><td>I,U2O,U4E3</td></tr><tr><td>D9</td><td>I,U5O,U2E1</td><td>I,U1O,U3E2</td><td>I,U2O,U4E3</td></tr><tr><td>D10</td><td>I,U5O,U2E1</td><td></td><td></td></tr><tr><td>D11</td><td>I,TO,U2E1</td><td></td><td></td></tr></table>

<table><tr><td></td><td>U1</td><td>U2</td><td>U3</td></tr><tr><td>D13</td><td>I,U5O,U2E1</td><td></td><td></td></tr><tr><td>D14</td><td>I,U5O,U2E1</td><td></td><td></td></tr><tr><td>D15</td><td>I,TO,U2E1</td><td></td><td>I,U2O,U4E3</td></tr><tr><td>D16</td><td>I,U5O,U2E1</td><td></td><td></td></tr><tr><td>D23</td><td>I,TE1</td><td></td><td>I,TE3</td></tr><tr><td>D27</td><td>I,U1O,U2E1</td><td></td><td>I,U2O,U4E3</td></tr><tr><td>D31</td><td>I,TO,U2E1</td><td></td><td>I,U2O,U4E3</td></tr><tr><td>D36</td><td>I,TO,U2E1</td><td></td><td>I,U2O,U4E3</td></tr></table>

(I,U) = (Input,Source)

(0,U) = (Output,Destination)

E = Event Code

<table><tr><td>Data Element</td><td>Data Structure /Data Group /Data Set /Relation</td><td>App. Code</td><td>Event No.</td><td>I/O</td><td>Code of Source /Destination</td></tr><tr><td>D(1,2)</td><td>G1</td><td>App.(1)</td><td>E1</td><td>I/O</td><td>U5/U2</td></tr><tr><td>D(2,23)</td><td>G1</td><td>App.(1)</td><td>E1</td><td>I/O</td><td>T</td></tr><tr><td>D(4,5,7,9,16,27)</td><td>G2</td><td>App.(1)</td><td>E1</td><td>I/O</td><td>U5/U2</td></tr><tr><td>D(13,14)</td><td>G3</td><td>App.(1)</td><td>E1</td><td>I/O</td><td>U5/U2</td></tr><tr><td>D(11,31,36)</td><td>G1</td><td>App.(1)</td><td>E1</td><td>I/O</td><td>T/U2</td></tr><tr><td>D(15)</td><td>G3</td><td>App.(1)</td><td>E1</td><td>I/O</td><td>T/U2</td></tr></table>

Fig. 9. Unit Subschema Form For Application (1). Code of Department: U1.

represents the time change of reality. Meanwhile, by determining the control or feedback data for each event, we can define all the feedback signals (internal or external).

If the attribute data are changed across events, the characteristics themselves are changed in time, which consequently means that reality is adaptive. Figure 8 shows the details of this matrix. As its side product, we can deduce a new subschema for the specific organizational unit. By considering a row as corresponding to a specific unit in the matrix, we can find all data elements used by that unit. Alternatively, we can differentiate between input or output data elements and specify what unit is responsible for issuing or authorized to receive data. The time of issuing or receiving it can also be determined.

Figure 9 shows the details of the unit sub-schema. The advantage of deducing it is in defining the responsibilities of issuing and authorization of receiving data at the proper time. We can determine the shareability of data between different units and consequently identify the level of complexity of the data base type, whether it should be centralized or distributed.

## 4. Case Study

The case study of a registration system for Kuwait University is shown to highlight the different features of the Work Flow Methodology. We have already elaborated the case study, through all the steps for application (1). The appendix illustrates the Dictionary of the Registration System which lists the organizational units, the applications, the data stores, the data elements, and the data groups. The different forms for this in the Registration System are shown in Figures 4b to 9. Also, Figure 5 illustrates the details of Event (1) in application (1).

## 5. Conclusion

The paper has addressed a proposed methodology for developing a conceptual data base design. The steps consider the operational aspects and relationships between different organizational units and data elements contained in its data base. By applying the proposed methodology we obtain not only the conceptual data base but also the abstract model of the information system which consists, in addition to conceptual data base, of the organization chart and the interrelationships between them. The methodology gives a dynamic map for the structured data pool, since time is taken as a basic dimension in representing the reality of the organization.

## References

[1] K. Grindly, Semantics, A New Approach to System Analysis, McGraw Hill, 1975.

[2] "Information Systems Design Methodologies: A Feature Analysis," Proceedings of the IFIP WG8.1 Working Conference on Feature Analysis of Information Systems Design Methodologies. York, U.K., 5–7 July, 1983. Elsevier Science Publishers B.V.

[3] Wilton Chung, "Structured Approach to Systems Devel-

opment-CIS Experience", Computer Science & Informatics Journal, Vol. 13, No. 1, 1983, pp. 31–35.

[4] Denis Connor, Information System Specification & Design Road Map, Prentice-Hall International Editions, Englewood Cliffs, N.J. 07632, 1985.

[5] Yash P. Gupta, “Directions of Structured Approaches in System Development”, Industrial Management & Data Systems Journal, July/August 1988, pp. 11–18.

[6] Dr. Robert S. Tripp, "Blueprints: Adopting a Construction Trade Approach in Designing Large Scale Management Information Systems", Information & Management Journal, Vol. 13, 1987, pp.55–70.

[7] Chris Gane and Trish Sarson, Structured System Analysis: Tools and Techniques, Prentice-Hall Inc., Englewood Cliffs, New Jersey 07632, 1979.

[8] M. Gopikrishna and V. Rajaraman, “Data Flow Oriented Software Tools for Business Data Processing”, Computer Science & Informatics Journal, Vol. 15, No. 2, 1986, pp. 9–22.

[9] D.T. Ross, M.E. Dickover and C. McGowan, "Software design using SADT", Auerbach Inc., Portfolio No: 53-05-03.

[10] W.P. Stevens, “How Data Flow Can Improve Application Development Productivity”, IBM Systems Journal, Vol. 21, No. 2, 1982.

[11] James Martin and Clive Finkelstein, “Information Engineering”, Savant Research Studies, Lancashire, LAS 9BX, England, 1981.

[12] Clive Finkelstein, 6 articles on Inf. Engineering in Computerworld, May 11–15 June, 1981.

[13] Kenneth T. Orr, “Structured Requirements Definition”, Kenn Orr and Associates Inc., Topeka, KS, 1981.

[14] Michael A. Jackson, System Development, Prentice-Hall International, London, 1983.

[15] David King, Creating Effective Software – Computer Program Design Using the Jackson Methodology, Yourdon Press, Prentice-Hall, Englewood Cliffs, N.J. 07632, 1988.

[16] James Martin, “Program Design which Is Provably Correct”, Savant Research Studies, Lancashire, LAS 9BX, England, 1982.

[17] Marius Janson, “Applying a Pilot System and Prototyping Approach to System Development and Implementation”, Information & Management Journal, Vol. 10, 1986, pp. 209–234.

[18] Juhain Livari and Mikko Karjalainen, “Impact of Prototyping on User Information Satisfaction During the IS Specification Phase”, Information & Management Journal, Vol. 17, 1989.

[19] Peretz Shoval and Nava Pliskin, “Structured Prototyping: Integrating Prototyping into Structured System Development”, Information & Management Journal, Vol. 14, 1988, pp. 19–30.

## Appendix

Dictionary of the Registration System

List of Organizational Units
U1: Guide

U2: Secretary of scientific department  
U3: Registration division  
U4: Computer  
U5: Advising and guidance division  
U6: Student

List of Applications in the Registration System
App. (1): Advising and Guidance
App. (2): Addition and Fees Payment
App. (3): Withdrawal and Addition
App. (4): Withdrawal

List of Data Stores
S1: Student file
S2: Major sheet
S3: Registration sheet
S4: Schedule course
S5: List of students names
S6: Addition and withdrawal schedule
S7: Schedule after addition and withdrawal
S8: List of errors
S9: Empty withdrawal sheet
S10: Schedule after withdrawal
S11: Addition schedule

List of Data Elements

<table><tr><td>Data Element</td><td>Data Element</td></tr><tr><td>Code</td><td>Name</td></tr><tr><td>D1</td><td>Course Number</td></tr><tr><td>D2</td><td>Course Name</td></tr><tr><td>D3</td><td>Course Type</td></tr><tr><td>D4</td><td>D5Student Name</td></tr><tr><td>D6</td><td>Student Address</td></tr><tr><td>D7</td><td>Year</td></tr><tr><td>D8</td><td>Faculty Name</td></tr><tr><td>D9</td><td>Speciality</td></tr><tr><td>D10</td><td>Number of Credits</td></tr><tr><td>D11</td><td>Room Number</td></tr><tr><td>D12</td><td>Instructor Name</td></tr><tr><td>D13</td><td>Faculty Code</td></tr><tr><td>D14</td><td>Department Code</td></tr><tr><td>D15</td><td>Building</td></tr><tr><td>D16</td><td>Numb.of Credit H</td></tr><tr><td>D17</td><td>Numb. Of Probation</td></tr><tr><td>D18</td><td>GPA</td></tr><tr><td>D19</td><td>Major GPA</td></tr><tr><td>D20</td><td>Nationality</td></tr><tr><td>D21</td><td>Social Status</td></tr><tr><td>D22</td><td>Birth Date</td></tr><tr><td>D23</td><td>Prerequisites</td></tr><tr><td>D24</td><td>No. of Students</td></tr></table>

<table><tr><td>D25</td><td>Remained Credits</td><td>D35</td><td>Sex</td></tr><tr><td>D26</td><td>Academic Year</td><td>D36</td><td>Time</td></tr><tr><td>D27</td><td>Registered Credits</td><td>D37</td><td>Grade</td></tr><tr><td>D28</td><td>Semester</td><td>D38</td><td>Tot. No. of</td></tr><tr><td>D29</td><td>Telephone</td><td></td><td>Required Credit</td></tr><tr><td>D30</td><td>Department</td><td></td><td>Hours</td></tr><tr><td>D31</td><td>Days</td><td rowspan="2" colspan="2">List of Data Groups</td></tr><tr><td>D32</td><td>ID</td></tr><tr><td>D33</td><td>Schoolarship</td><td>G1: Course</td><td>G2: Student G3: Building</td></tr><tr><td>D34</td><td>Total Points</td><td>G4: Staff Member</td><td>G5: Academic Year</td></tr></table>

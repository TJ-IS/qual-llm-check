---
otero_id: 17992
otero_key: "PRT6R4SB"
title: "An effective architecture for Decision Support Systems"
authors: "Takeshi Kosaka; Tetsuo Hirouchi"
year: "1982"
journal: "Information & Management"
doi: "10.1016/0378-7206(82)90014-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An Effective Architecture for Decision Support Systems

Takeshi Kosaka

Nippon Univar Kaisha, Ltd., Applications Software Dept., 17-51, 2-chome, Akasaka, Minaroku, Tokyo, 107 Japan

and

Tetsuo Hirouchi

Bunkyo University, Faculty of Informatics, 3337 Minami-orgishima, Koshigayashi, Saitamaken, 343 Japan

Decision Support Systems (DSS) are, by nature, general-purpose systems, because they must support a variety of managers who have different decision styles and different problems. However, it seems that no effective general-purpose DSS have yet come into existence, although the components of DSS such as data base technology, modeling techniques, inexpensive graphic display etc., have progressed to the point where we should now be able to build effective DSS.

This shortcoming seems to result from the following fact: Research on decision support has focused on data enlargement and model refinement, however, little attention has been paid to DSS architecture which integrates these components of DSS. It has not been well appreciated that DSS architecture itself facilitates learning about unstructured-problem solving and enables system evolution.

In this paper, we propose a DSS architecture based on the study of unstructured-problem solving and considerations of the needs of managers as non-computer specialists. We illustrate this with a system realized using this architecture.

Keywords: Data base, Decision, Decision making, Decision support system, DSS, Ease of used, End user, Evolution, Learning, Management support software, Model, Problem solving, Software architecture, Unstructured problem..

## 1. Introduction

Design of Decision Support Systems (DSS) is considered a very difficult task for two reasons. One is the difficulty encountered by builders in understanding managers' needs, because of an incomplete presentation of their needs. The other is that DSS designed by a conventional system development approach is too large-scaled to function, and is inappropriate for

![](/api/attachments/PRT6R4SB/fulltext/images/9ad2bbb83276f210fb943f0b6303cee115c77d7f730dcd2fd4f2be0af69198c8.jpg)

Takeshi Kosaka is a systems analyst at Nippon Univac Kaisha, Ltd., in Tokyo. He received his B.S. in electronics engineering from Sophia University. With his industrial experience in systems consultation and systems design, he has presented numerous papers on Decision Support Systems, database design, systems implementation, scheduling techniques and office automation. His research interests include information analysis, managerial accounting and in formation systems implementation. Also in the DSS working group of the Operations Research Society of Japan Mr. Kosaka is currently active in working out the characteristics of information systems essential to Japanese Management.

![](/api/attachments/PRT6R4SB/fulltext/images/d68b7ebcaa7214a47668e7ef2e31f44ce5d2e58488a7492c7ba9b08c6bd5b8c6.jpg)

Tetsuo Hirouchi is a researcher in the Faculty of Informatics at Bunkyo University (Japan). He received a M.S. in molecular science majoring in theoretical studies from Tokyo University of Education. His research interests focus on the fields of Management Information Systems (systems analysis, systems design, systems implementation, database systems, and Decision Support Systems). He is the author of more than 10 technical papers in these subjects. Prior to joining Bunkyo University, Mr. Hirouchi worked for Nippon Univac Kaisha as a chief System Designer. His working effort was mainly in the areas of Decision Support Systems. He is a member of Information Processing Society, Office Automation Society, Operations Research Society, and Simulation Society in Japan.

![](/api/attachments/PRT6R4SB/fulltext/images/c3d4fe920cce286765fcee885b2e986756b7b7d6a72703bb5bc90af6f57ac428.jpg)  
Fig. 1. Elements for DSS.

effective support of management decision making.

These difficulties essentially arise from the element of human learning in the process of unstructured-problem solving. Managers usually gain understanding of problems as they use DSS, so that they can think out more reasonable solutions. Accordingly, they begin to ask for new functions from DSS. These facts suggest that DSS should either facilitate the user learning and evolve system capabilities by incorporating new functions required by users.

Elements integral to DSS are data, model and, finally, architecture which provides users with the first two elements and supports problem solving (Fig. 1). We note the similarities among means and methods which are used in problem solving and find that it is possible to build an architecture independent of specific problems. The architecture assumes the responsibility for promoting user learning and system evolution. This architecture is hereafter called 'DSS architecture'.

Most systems usually called DSS are intended for computer specialists. Efforts have been focussed on the preparation of data and the development of models for specific problems. In order to make DSS effective for users, we believe that DSS architecture must be established in advance of data and models.

From the software viewpoint, learning and evolution are reduced to the following two issues:

(1) DSS must be designed so that users can flexibly develop solution procedures for unstructured problems using DSS in a manner in proportion to their learning level in each situation, by invoking their experience, intuition and insight. Furthermore, it must be possible to incorporate into DSS new functions for ad-hoc requests. (Issue of flexibility).

(2) In order to increase the effectiveness of user learning, ease of use is required so that users can operate DSS by themselves as much as possible. Thus, DSS must be fully controllable in proportion to the user's experience, abilities and skill. (Issue of ease of use).

From the above mentioned standpoints, this paper shows how DSS should be designed so that data and models can be flexibly and easily used by managers. We discuss flexibility and ease of use in sections two and three, introduce DSS architecture, created from this discussion, in sections four and five, and describe DSS1100, which is based on the DSS architecture, in section six.

## 2. Flexibility

## 2.1. Study of Problem Solving

Simon studied human problem solving and found that the process for solving unstructured problems comprises three phases: intelligence, design and choice [1]. In the actual problem-solving process these phases overlap. At the same time, when these three phases are recognized, each becomes an independent problem. In the problem solving process, man employs the method of resolving a problem by breaking it into several sub-problems. He or she repeats such resolutions until the problem is finally broken down into structured sub-problems which can be directly solved. When a solution for each subproblem is obtained, he or she synthesizes the solutions in order to approach the solution of the initial problem.

We believe that such resolution and synthesis in the problem solving process can be interpreted from a data handling standpoint. When dealing with the process of problem resolution and synthesis, a manager uses representations such as graphs and lists. The manager identifies which aspect requires more detailed investigation by looking at the representations which illustrate general situations (Resolution). In contrast with this, the manager successively draws results from more than one representation to approach the solution of the initial problem (Synthesis).

If the problems are simple, managers can often solve them completely by only preparing representations directly from the data concerned. These cases correspond to situations where managers, to facilitate comparisons and grasp general trends, collect and transform separate data into graphs or make use of reports in which data concerning several entities are listed. Data base query, graphs or lists are the tools to be used in these cases. This will be termed 'physical transformation' here.

In case problems are more complicated or the quantity of data concerned is too large, competent managers first transform the data into manageable quantities or extract underlying facts from the data before they make representations, since they cannot solve these problems only by physical transformation. Classical management science models or simple calculations are the methods to be used in such cases. For instance, attempting 'what if ... questions' through the analysis of the relation between more than two variables, or by the preparation of accounting models corresponds to those cases. This task of data handling, to produce material to be shown in representations, is termed 'logical transformation'.

From the viewpoint of data processing which converts data that on its own are insignificant into useful information, means such as graphs, lists and data base query in physical transformation can be considered on the same level as methods such as management science models and simple calculations in logical transformation.

These means and methods are meaningful also from a communication viewpoint. For a sub-problem, managers picture a problem-solving procedure using specific means and methods and then leave the solution to assistants who have information on the type of means or methods they desire to employ. For example, a manager can easily define a specific problem-solving procedure, such as retrieving sales data for each product, calculating, forecasting and then plotting totals. Here, key words such as RETRIEVE, CALCULATE, FORECAST and PLOT used in the statement make it easy to communicate with their assistants.

These key words can be given spontaneously by managers without any assistance and can be used as terms for communication between DSS and the managers, if they use DSS for the problem solving. The idea of key words is also suggested by Keen as the potential use of verbs for communication with a DSS [2].

Noting that managers build decision support models for particular problems using these key words, that is, means and methods, we recognized that these means and methods can be considered universal components of any decision support models. Therefore, this component is called a 'model unit'. Such key words correspond to the names of the model units.

With the key words, all users can share the same ideas about model units. Therefore, the key words can also be of help in communicating between users.

The model units named with key words each have a single function, which is structured and is independent of specific problems. The following can be considered model units: data base queries, analytic methods, forecasting methods, simple calculations (data manipulation), graphs and tabulations (l:s's).

## 2.2. Idea of Modeling

We intend to promote the work of resolution and synthesis in the problem solving process by the concerted combination of several model units, each having a single function.

In order for managers to solve unstructured problems using model units, a systematic environment must be provided (Fig. 2).

Model units must be stored in an open model storage area easily accessible to managers so that they may become well aware of the existence and varieties of model units. This area is termed a 'model base'. If managers intend to use model units as tool for problem solving, they should be acquainted with their existence.

Managers take out a model unit they consider to be helpful from the model base and use it. They subsequently employ another model unit, recognizing the results obtained from the previous one. Thus, they are always in a process in which they think over the result from previous model units and then choose the next process by exerting their judgement. The significance of such a process is very important, because a manager's direct intervention in the process of modeling leads to correct evaluations (by the managers themselves) of the significance of decision support models built from a combination of model units.

![](/api/attachments/PRT6R4SB/fulltext/images/a9f4770c14d397ad14e8024d4b6deb40be4750df4a815018d89b146f3425f364.jpg)  
Fig. 2. Systematic Environment for Effective DSS.

To make this process work smoothly, a reusable data area (where users can store results of model units) is indispensable. This area is called a 'workspace'. This workspace should make it easy for users to see the contents of the data from outside the system. In addition, the workspace must have a capability for accepting external data, and assimulating it in the internal data.

Data exchange amongst model units, through the intermediation of the workspace, will result in the interconnection of model units, and, in turn, lead to the development of a decision support model.

Given a situation where it is possible to establish a systematic environment made up of these model units, model base, and workspace, managers have the means to build an appropriate decision support model with the aid of their experience, intuition and insight.

## 3. Ease of Use

## 3.1. Needs for Ease of Use

It is usually thought that the ease of use of a system has little influence on the essential requirement, that is, to solve a problem. However, it is a point to be emphasized, being fundamental in effectively aiding the manager. Existing systems which are designed for computer specialists usually compel them to refer to specially prepared operation manuals, but such forced use cannot be ideal for managers who are unfamiliar with computers. Managers are interested in information obtained from data retrieval and/or data manipulation and not information about system operation.

As pointed out above, the managerial decision making process takes very complicated forms, making it impossible to establish a common problem-solving procedure. Therefore, preparation of a single uniform method of system operation cannot effectively facilitate problem solving. It is important that DSS provide managers with functions which they can manipulate in proportion to their progress in the problem solving process and their styles of use. One of the major factors determining the effectiveness of DSS is the ease of use which allows personal use depending on the managers ability level.

We shall discuss ease of use in terms of (1) skillfulness/familiarization and (2) structuring of a problem-solving procedure, and make some suggestions for realizing ease of use.

## 3.2. Skillfulness/Familiarization

The first issue concerning ease of use is in improving the controllability of the system. Usually managers are not computer experts. Therefore, even if they are aware of the existence of a certain model unit, they may not always be able to operate it. Most managers know no more than the basic concept of a model unit. However, man is generally capable of acquiring a skill and familiarizing himself with a system, once he is taught how and then gains experience. Managers will eventually establish their own styles of use according to their abilities.

One of the characteristics of DSS is that they must accept a variety of potential users, from beginners to experts. DSS must have the following two forms of interaction in order to deal with varying levels of users:

(1) a system-driven interaction mode for beginners. This leads users, by showing them how and what input the model unit requires. Trial-and-error should be effective in this interaction form.

(2) a user-driven interaction mode for experts. In this, users who know what input is required provide it without any assistance.

In order to make allowance for the learning process, it is essential that DSS allows the combined use of the above two modes of interaction. With this available, users can gradually shift from system-driven interaction to user-driven interaction as they progress in their learning.

## 3.3. Structuring of the Problem-Solving Procedure

The second issue concerning ease of use deals with the ability to cope with developments in the structuring of problem solving. A problem which is originally unstructured is gradually transformed until it becomes structured and hence solvable by some structured method [3]. If DSS fails to cope with this problem structuring process, it becomes troublesome to use, because it requires frequent inputs from its users. It is therefore necessary that users can gradually transfer operations performed by them to the system.

The structuring of a problem-solving procedure begins with the input process of individual model units and gradually spreads to the process of combining model units. Therefore, it is necessary to be able to catalogue (either partially or entirely) "conversational" input for each model unit, as well as for combination of model units, so that users only have to refer back to the catalogued input when they deal with similar problems. Inclusion of these functions will enable users to handle structuring problems with simplified operations.

## 4. Realization of Flexibility

## 4.1. System Structure

In our design approach, a model unit (MU) is composed of a single problem-solving function. All information processing functions common to the various MU's are extracted, and are then independently implemented in the DSS architecture. The information processing functions of existing models include such essential functions as: conversation control, display management, file manipulation, data base interface, etc.

This approach has the following advantages:

(1) An MU can be composed using only its original problem-solving algorithm: other information processing functions do not have to be included in the MU.

(2) It is possible to provide a common data basis for all MU's.

(3) An interaction mode can be defined between users and the system that is common to all MU's.

We adopted a system structure as shown in Fig. 3 to realize the DSS architecture. Fundamental elements for the DSS architecture are: six functional modules, system files, a model base and a workspace. The DSS architecture makes each MU run, and works as if it plays the role of an operating system (OS) to MU's. An outline of the four fundamental elements is given below.

The six functional modules include the following software modules:

(1) A model unit connection module, which invokes a MU and makes it run according to a user's direction.

(2) A workspace manipulation module, which provides all MU's with a common basis for data interchange by allowing them to input data from and output data to the workspace using data names given by users.

(3) A conversation control module, which releases anything regarding conversation from MU's by conversing on behalf of them with a user according to the conversation control information stored in the system file discussed later.

![](/api/attachments/PRT6R4SB/fulltext/images/bcd3786443a6ca961dbcc8f1bc6b0281cdcda460bc7a2501b101a30d16016a27.jpg)  
←CONTROL INFORMATION FLOW □ DATA FLOW ◀ MODEL UNIT FLOW  
Fig. 3. System Structure for DSS.

(4) An output control module, which releases any function regarding output from MU's, including display and hard copy management.

(5) A system file handling module, which releases input and output operations of system files from MU's.

(6) A data management module, which separates MU's from data by providing interface with a CODASYL type DBMS (data base management system). This module also keeps track of the start time, periodicity of time series data and units of measurement, thus supplementing capabilities inherent in the DBMS.

A log module is also part of the functional modules. This monitors users' operational performance and collects information for performance improvement and system evolution.

The system files are prepared to hold, on behalf of MU's, information such as that needed to make the development of MU's easy, information necessary to make each MU run, and any volatile information. There are five system files for:

(1) the definition of conversation needed for MU's;

(2) the definition of information with regard to data base structure, access path, and time-series data;

(3) security information;

(4) the registration of conversational input images and problem-solving procedures; and finally,

(5) decoded information.

The model base is a file for holding MU's, and is designed to draw users attention to the existence of each MU and to facilitate the use, addition, renewal, or deletion of any MU.

The workspace is set up to circulate information among MU's. This provides input for and also stores output from all MU's. Data processed by a certain MU becomes input data for the next MU, which is then connected with the previous one by way of the workspace.

Data in the workspace is handled by the workspace manipulation module in vector form, which is part of the matrix form. Each vector carries data and its associated attribute information. The attribute information consists of entity names, item names, dates, data type, unit of measurement, etc.

Output data are assigned names given by users or generated according to an algorithm in the workspace manipulation module (from capital letters given by the users). The users only have to designate the data name – they do not need to know the storage structure of the relevant data. Because of the data transparency realized by the module, the workspace functions as a simple relational data base.

In addition, all or part of this workspace can be catalogued in the course of processing for later use, and can serve as a personal data base.

## 4.2. System Behavior

All the functions explained above enable a user to build a decision support model. The behavior of a system based on the DSS architecture can be described as follows.

When the system is started by a user, the model unit connection module, via the conversation control module, asks the user which MU is to be used. When the user gives the name of a specific MU, the relevant MU is called from the model base by the model unit connection module and is set at the MU position shown in Fig. 3. Then, the model unit execution starts.

The source of input to the MU is the workspace, and the MU processes data according to its inherent algorithm, entrusting basic processing to the capabilities of the workspace manipulation, conversation control, output control, system file handling, and data management modules.

The functional modules referring to data recorded in the system files undertake processing on behalf of the MU, while the MU outputs the processing results to the workspace.

Upon completion of the execution of the MU, the model unit connection module (via the conversation control module) again asks the user which MU to use next. This pattern is repeated until the user requests termination of the system.

All the above is an outline of system behavior. By repeating the above pattern, a decision support model is gradually built, and data is transformed into useful information as it is circulated among various MU's through the mediation of the workspace.

## 4.3. Types of Model Units

As the DSS architecture is constructed to be capable of incorporating any type of MU, a general-purpose DSS can be created by previously including various MU's in the model base of the DSS architecture.

We arranged for many standard MU's. These are considered necessary for supporting management control:

(1) Data base query MU; this is the fundamental MU in the intelligence phase of problem solving. It is used to retrieve, through trial and error, time-series data, cross-section data, and attribute data from the CODASYL type data base. This MU outputs data from the data base to the workspace.

(2) Management science MU's; these include, as an independent MU, time-series forecasting techniques such as exponential smoothing, the CENSUS method, and multi-variate analysis techniques, such as multi-regression analysis, principal factor analysis, etc. These MU's are applied to retrieved data and/or interim data in the workspace.

(3) Data manipulation MU's; these perform arithmetic/logical operations on retrieved and/or interim data. These MU can build and execute simple simulation models.

(4) Data input MU; this assimilates external data in the workspace, as needed, when data in the data base is not sufficient.

(5) List MU's; these are used for listing data processed by other MU's in the workspace.

(6) Graph representation MU's; these output data from the workspace in graphic form. They include the representation of a bar graph, a line graph, a radar chart, etc.

All these MU's are stored in the model base and are used by managers. However, some ad-hoc problems may need more than the above MU's. Such problems require preparation and storage of new MU's in the model base. (The work required to incorporate a new MU involves the programming of its algorithm and using a compiler). All additional MU's can be used in combination with existing ones. Since a new MU can be easily and quickly prepared with the help of the functional modules and the system files, the system based on the DSS architecture evolves along with the capabilities of its users.

## 5. Realization of Ease of Use

## 5.1. Coping with Varying Levels of Skill/Familiarity

General methods for realizing interactions with a computer include command and menu methods. A system-driven interaction mode can be realized using a menu method. With this method, beginners are able to give instructions to the system while receiving information about interaction. On the other hand, a command method is not only applicable to a user-driven interaction mode, but also can realize more flexible types of interaction, generally more suited to specialists.

In another sense, interaction with the system can generally be categorized into two parts: interaction where the MU demends input from users, and interaction where the user informs the system of his intentions. The former is defined exclusively by the algorithm inherent in the relevant MU, so the kind of conversational input required and the conversational procedure can be predefined. On the other hand, the latter interaction makes it possible for the user to interrupt the system, so it is impossible for the interaction to be fixed; thus high flexibility is required.

We prepared, as part of the DSS architecture, a composite interaction mode which enables DSS to cope with varying levels of skill (from low to high). This was achieved by applying the menu method to the former and the command method to the latter; we thus exploited the merits of each method.

Normal conversation with MU's is based on consecutive input by the menu method as shown in Table 1, which will be further described later (responses are normally made in codes, but for convenience they are expressed in words in order to make the meaning clear). In this mode, the system displays conversational guidance messages to solicit input from the user, and the user responds. This conversational form is designed for a user with a low level of skill. The illustration shows how the data base query MU is selected, and how the conversation control module successively demands necessary input from the user for the relevant MU, as well as how the user responds.

For users with a high level of skill (i.e., ones who have gained experience in using MU's and learned all necessary input items and their sequence), we have prepared a special conversation method in which DSS allows collective input and blocks the presentation of the related conversational guidance messages. This stops interaction following the user's response.

Both consecutive input and collective input can be used for all MU's. The conversation control module can automatically transfer from one type of input to another, freeing the user from making the adjustment.

Unless the user knows input code systems, he may still not be able to use the system when the necessary input is required. Therefore, we prepared, along with the command method, a comprehensive cascaded aid function called the HELP function. This informs the user of codes necessary for input. This function serves as, or is even more effective than, a simple operation manual. The HELP command also enables the user to refer to the types and characteristics of MU's stored in the model base, in addition to any code systems.

Other than the aid function, conversations prepared using the command method include conversational control operations (such as the restart or reoperation of conversational input by trial and error), and output control operations (such as output of any results to display or hard copy devices). These all increase the flexibility of system operation.

Conversations using the menu method (consecutive input and collective input) and conversations using the command method can be freely combined. Having a flexible interaction capacity, a system based on the DSS architecture is capable of aiding all users, from beginners to experts, and coping with varying levels of skill and familiarity.

## 5.2. Coping with Problem Structuring

In the DSS architecture, we prepared two functions which follow problem structuring: unit and consecutive macro functions. For problem solving to be structured in a MU, a unit macro function is prepared. Structuring problem solving begins with the MU. The fixing of MU use allows the incorporation of a series of already known conversational input images, with their name, into the system file.

When a user wishes to perform the same task, he only has to designate this unit macro name. Then the conversation control module, instead of the user, provides the input. If some input items are not included in the conversation, the system automatically requests them from the user.

As problem structuring progresses, further steps may result in the combination of MU's. The information on their combination is incorporated into the system file, and a consecutive macro function is prepared for processing the information. A user can combine MU's by only designating a consecutive macro name and then build the decision support model.

As the unit macro and consecutive macro functions facilitate problem structuring, a user can therefore be relieved from providing a series of routine inputs.

## 6. An Example of the System's Use

The DSS architecture was programmed on UNIVAC 1100 series computers and called DSS-1100. A city bank in Japan introduced the software product with a banking data base to create a DSS for branch management. As an example, we will describe a bank decision support model. It was built with only the standard MU's of section 4.3. This model was designed for forecasting of the deposits. The problem is: 'When will the target deposit balance be achieved if the total deposit balance (sum of ordinary, current, and time deposits) of the Tokyo branch increases without major change?'

At each branch, the deposit transaction data is collected and aggregated every day. It is then incorporated into the CODASYL database. In addition, each branch's target total deposit balance is also put into the data base and stored as time-series data.

Using the interactive capability of DSS1100, a manager retrieves the necessary data from the database and builds a decision support model for forecasting deposit growth. Conversation used to build the model is shown in Table 1. This interaction is carried out by consecutive input interaction using the menu method.

First, the system asks 'Which MU do you wish to select?'; the manager selects the database query MU and retrieves the original time-series data on each deposit of the Tokyo branch. These retrieved data are named A001, A002, and A003, and are output into the workspace.

Subsequently, the system asks, 'Which MU do you wish to select?', then the manager selects the database query MU again and retrieves, in the same manner as before, the target total deposit balance. The result, named PLAN, is output into the workspace.

The system asks for the selection of a MU again, and the manager selects the data manipulation MU. Subsequently, the total deposit balance is obtained from A001, A002 and A003 (i.e., ordinary deposit, current deposit, and time deposit); which were previously stored in the workspace as output. The resultant sum is named TOTL and output into the workspace.

Then the manager selects the time series forecasting MU using an exponential smoothing method. With the MU the manager applies the method to the data TOTL in the workspace. The result is stored (back in the workspace) and named FCST.

![](/api/attachments/PRT6R4SB/fulltext/images/3d0cba00f6a9be20cd70846993b26fd67a5f18b821cb42e3e94ce14e533756b5.jpg)  
Fig. 4. Building Process of a Decision Support Model.

Table 1
Conversation for the Forecast of Deposit Balance

<table><tr><td rowspan="3">MU Selection</td><td>DSS</td><td>DSS starts.</td></tr><tr><td>DSS</td><td>Which MU do you wish to select?</td></tr><tr><td>Manager</td><td>Data base query MU.</td></tr><tr><td rowspan="12">Data base query MU</td><td>DSS</td><td>Which data do you wish to retrieve?</td></tr><tr><td>Manager</td><td>Branch management data (actual).</td></tr><tr><td>DSS</td><td>Which branch do you need?</td></tr><tr><td>Manager</td><td>Tokyo.</td></tr><tr><td>DSS</td><td>Which kind of deposits do you need?</td></tr><tr><td>Manager</td><td>Ordinary, current, and time deposits.</td></tr><tr><td>DSS</td><td>For what dates?</td></tr><tr><td>Manager</td><td>From April of 1978 to March of 1981.</td></tr><tr><td>DSS</td><td>What name do you assign to the retrieved result?</td></tr><tr><td>Manager</td><td>A.</td></tr><tr><td>DSS</td><td>Retrieved data have been assigned names: ‘A001’, ‘A002’ and ‘A003’.</td></tr><tr><td>DSS</td><td>Query has ended.</td></tr><tr><td rowspan="2">MU Selection</td><td>DSS</td><td>Which MU do you wish to select?</td></tr><tr><td>Manager</td><td>Data base query MU.</td></tr><tr><td rowspan="5">Data base query MU</td><td>DSS</td><td>Which data do you wish to retrieve?</td></tr><tr><td>Manager</td><td>Branch management data (planned).</td></tr><tr><td></td><td>(Similar conversation to the above is made.)</td></tr><tr><td>DSS</td><td>Retrieved data has been assigned a name ‘PLAN’.</td></tr><tr><td>DSS</td><td>Query has ended.</td></tr><tr><td rowspan="2">MU selection</td><td>DSS</td><td>Which MU do you wish to select?</td></tr><tr><td>Manager</td><td>Data manipulation MU.</td></tr><tr><td rowspan="5">Data manipulation MU</td><td>DSS</td><td>What calculation is to be used?</td></tr><tr><td>Manager</td><td>TOTL = A001 + A002 + A003</td></tr><tr><td>DSS</td><td>Do you have further input?</td></tr><tr><td>Manager</td><td>No.</td></tr><tr><td>DSS</td><td>Data processing has ended.</td></tr><tr><td rowspan="2">MU Selection</td><td>DSS</td><td>Which MU do you wish to select?</td></tr><tr><td>Manager</td><td>Exponential smoothing MU.</td></tr><tr><td rowspan="8">Exponential smoothing MU</td><td>DSS</td><td>What is the name of data for the forecast?</td></tr><tr><td>Manager</td><td>‘TOTL’.</td></tr><tr><td>DSS</td><td>How many terms do you want to forecast?</td></tr><tr><td>Manager</td><td>To twelve months later.</td></tr><tr><td>DSS</td><td>What name do you assign to forecasted result?</td></tr><tr><td>Manager</td><td>‘FCST’.</td></tr><tr><td>DSS</td><td>Forecasted data has been assigned a name ‘FCST’.</td></tr><tr><td>DSS</td><td>Forecasting work has ended.</td></tr><tr><td rowspan="2">MU Selection</td><td>DSS</td><td>Which MU do you wish to select?</td></tr><tr><td>Manager</td><td>Line graph MU.</td></tr><tr><td rowspan="7">Line graph MU</td><td>DSS</td><td>What is the name of data to be presented in the graph?</td></tr><tr><td>Manager</td><td>‘FCST’ and ‘PLAN’.</td></tr><tr><td>DSS</td><td>How many terms do you want in the presentation?</td></tr><tr><td>Manager</td><td>All.</td></tr><tr><td>DSS</td><td>The data will be presented on a graph.</td></tr><tr><td></td><td>Graphic output</td></tr><tr><td>DSS</td><td>Drawing the graph is completed.</td></tr><tr><td rowspan="3">MU Selection</td><td>DSS</td><td>Which MU do you wish to select?</td></tr><tr><td>Manager</td><td>Finish.</td></tr><tr><td>DSS</td><td>DSS has finished.</td></tr></table>

With use of the line graph MU, the manager finally obtained a time series graph from the target data PLAN and the forecast data FCST.

As a result of the above operations, the manager can determine when the target of total deposit balance in the Tokyo branch will be achieved. The process for building the decision support model is conceptualized in Fig. 4.

This example is an actual case. In the field of practical management decision making, branch management, budgeting and other problems are dealt with by using DSS1100 with other combinations of MU's.

## 7. Conclusion

Our DSS architecture realizes the flexibility and the ease of use that promotes user learning and system evolution.

A system based on the DSS architecture expects only that users have some knowledge about model units (MU); that is, the means and methods used in problem solving. Users are not required to have a detailed knowledge of operations. Ease of use makes it possible for a manager to use the system without intermediates. In addition, the flexibility of the system makes it possible for a manager to combine MU's of a single function to build up his/her own decision support model for an unstructured/semi-structured problem through trial and error. Therefore, users can intervene in the process of model building whenever they like. As the result, users can find the solution while learning the nature of the problem and the possible procedures.

In the DSS architecture, the MU itself, which contains only an intrinsic algorithm, is not required to include processing functions common to all MU's. The MU's are built on a common basis of model base and workspace relating to model and data. Accordingly, the DSS architecture can be flexible, incorporating new MU's and evolving the system without making it complex. Under this DSS architecture, the creation and incorporation of new MU's takes only a few days: the time required depends solely on the complexity of the algorithms.

DSS1100 is an actual software product based on the DSS architecture. It was developed in Japan and runs on UNIVAC 1100 Series Computers. At present this system is being used in the fields of budgeting, marketing management, protofolio management, and others, in nine banks, a security company, and a chemical company.

## References

[1] H.A. Simon, 'The New Science of Management Decisions,' Revised edition, (Prentice-hall, New Jersey, 1977).

[2] P.G.W. Keen, 'Decision Support Systems: Translating Analytic Techniques into Useful Tools', Sloan Management Review, (Spring, 1980).

[3] G.A. Gorry and M.S. Scott Morton, 'A Framework for Management Information Systems', Sloan Management Review, (Fall, 1971).

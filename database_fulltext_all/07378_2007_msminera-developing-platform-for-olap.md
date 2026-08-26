---
otero_id: 7378
otero_key: "8WAB4Q5B"
title: "MSMiner—a developing platform for OLAP"
authors: "Zhongzhi Shi; Youping Huang; Qing He; Lida Xu; Shaohui Liu; Liangxi Qin; Ziyan Jia; Jiayou Li; Huijing Huang; Lei Zhao"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.11.006"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# MSMiner—a developing platform for OLAP<sup>B</sup>

Zhongzhi Shi <sup>a,\*</sup>, Youping Huang <sup>a,b</sup>, Qing He <sup>a</sup>, Lida Xu <sup>a,b,c</sup>, Shaohui Liu <sup>a</sup>, Liangxi Qin <sup>a,b</sup>, Ziyan Jia <sup>a,b</sup>, Jiayou Li <sup>a,b</sup>, Huijing Huang <sup>a</sup>, Lei Zhao

<sup>a</sup> Institute of Computing Technology, Chinese Academy of Sciences, Beijing 100080, China

Graduate School of the Chinese Academy of Sciences, Beijing 100039, China

<sup>c</sup> Department of Information Technology and Decision Sciences, Old Dominion University, Norfolk, VA 23529, USA

Available online 29 December 2004

## Abstract

Since the early 1970s, decision support systems (DSS) have evolved significantly. In this paper, the design and implementation of MSMiner, a developing platform for DSS, is introduced. The system is constructed on a data warehouse and integrated with a number of data mining algorithms. It is well suited for on-line analytical processing (OLAP). The characteristics of MSMiner include the ability to support multiple data sources and data mining strategies, additional organizational flexibility in regard to data and mining strategies, and the powerful expansibility of data mining tasks. <sup>D</sup> 2004 Published by Elsevier B.V.

Keywords: DSS; Business intelligence; OLAP; Data mining; Data warehouse; ETL

## 1. Introduction

In the early 1970s, pioneer scholars including Morton, Sprague, and Whinston developed a concept called decision support systems (DSS) [3,5,18]. As a result, a discipline called DSS was born. The birth of model-oriented DSS marked the beginning of information systems specifically for decision support in complex environments. In the late 1960s, research on model-oriented DSS began. In the 1970s, progress was made in both DSS theory and practice. In the mid 1980s, through integration with networking technology, artificial intelligence, and enterprise information systems, DSS such as distributed DSS, intelligent DSS, and integrated DSS appeared. In the 1980s, the concept of executive information systems (EIS) was developed. In the 1990s, the concept of on-line analytical processing (OLAP) systems was developed [1,11–15,18,19,21]. In the mid 1990s, web-based DSS became an active research topic [21].

As mentioned above, in the 1990s, the concept of OLAP was developed. In fact, in the 1990s, new technologies such as data warehouse, OLAP, and data mining consecutively emerged for DSS development; in which data warehouse concept emerged first. Following the introduction of data warehouses, OLAP and data mining appeared [7,9,17]. Now, an increasing number of DSS have adopted data warehousing and data mining techniques. Organizations are taking advantage of data mining technology to leverage vast amounts of data for making competitive business decisions [2]. Many data mining systems have been developed in recent years including SPSS Clementine [22], Intelligent Miner [23], Enterprise Miner [24], and MineSet [25]. Such systems have been successfully employed in web intelligence [4], scientific research, marketing, financial investment, telecommunications, manufacturing, and health care [15,18]. In general, these systems can be classified into general or special applicationoriented systems coupled with databases and/or data warehouses.

MSMiner [26] is a generic data mining platform for decision support. The goal of research and development is to implement an integrated, extensible decision support tool by employing data warehousing and data mining technologies. In this system, the integration of an entire decision-making process on an interactive basis is emphasized. The functions of the system include database access, data modeling, data preprocessing, data mining, and data visualization. Therefore, the system provides a complete solution for decision making. In addition to this, emphasis has been put on the extensibility characteristics of the system. As a multistrategy data mining platform, MSMiner not only provides convenient tools to develop new data mining algorithms, but also includes many build-in algorithms such as SOM and C4.5. MSMiner has an open interface for adding data preprocessing function and can access a variety of databases such as SQL Server, Oracle, and Informix. Efficiency is an important consideration, too. In the system, a task scheduling algorithm based on directed acyclic graph (DAG) was developed, which ensures that the data mining task and data preprocessing task can be executed concurrently.

The rest of this paper is structured as follows. Section 2 introduces the design requirements of MSMiner. Section 3 presents an overall architecture of the system. Section 4 describes the subsystems in MSMiner including the data warehouse subsystem, data mining subsystem, ETL (data extraction, data transformation, and data loading) subsystem, OLAP subsystem, and metadata management subsystem. In Section 5, an application example of MSMiner is presented. Discussion and directions for future work are provided in Section 6.

## 2. Design requirements

In order to develop a useful generic data mining platform, the following characteristics were taken into consideration in designing the MSMiner system:

Integrality: MSMiner is expected to support the entire decision-making process, from data collection to data visualization. The system includes tools such as ETL, data mining, and OLAP.

Extensibility: The system is expected to accommodate the easy addition of new data mining algorithms, as well as new data preprocessing functions and new data sources.

Scalability: The expected increase in the amount of data requires the system be scalable in order to handle large volumes of data.

Flexibility: The system is expected to allow dynamically defined, complicated data mining tasks and data preprocessing tasks. A data mining task may integrate with several mining algorithms, so does ETL task.

Maintainability: The object-oriented features provided by the C++ language will be fully employed, together with suitable advanced object-oriented design patterns. This promotes software component reuse and significantly contributes to the maintainability, flexibility, and extensibility of the library.

Modularity: The system is expected to be composed of several individual subsystems with rules concerning their interdependencies. This minimizes recompilation and clarifies the overall library architecture.

Efficiency: Efficient implementation is expected for the system. The data mining tasks should be processed concurrently, and the steps in a single task should be processed concurrently as well.

User-friendliness: The interface is expected to be intuitive, perspicuous, easy to use, and conform to the standard Windows GUI norms. Furthermore, the GUI should be object-oriented in the sense that the objects being manipulated should be represented as distinct and individual items in the interface, with operations that are natural to perform on the objects available directly from the objects themselves.

## 3. System architecture

MSMiner is developed using C++ language on Microsoft Windows 2000. The architecture of this system is shown in Fig. 1.

MSMiner consists of five parts: ETL subsystem, metadata management subsystem, data warehouse management subsystem, OLAP subsystem, and data mining subsystem. Cooperating with the ETL subsystem, the data warehouse subsystem creates a data warehouse from relational data sources, which is managed and maintained by metadata management subsystem. Based on this data warehouse, MSMiner supports OLAP and data mining tasks. The data mining subsystem includes several algorithms, and provides a task manager and a task processing engine for data mining. It provides the function of data mining and decision making in the form of an objectoriented task model.

## 4. Subsystems in MSMiner

## 4.1. Data warehouse

A data warehouse is <sup>b</sup>a subject-oriented, integrated, time-variant, nonvolatile collection of data in support of management decisions<sup>Q</sup> [6]. The function of the data warehouse is to provide a general data warehouse environment, by which users can create and maintain their data warehouse in accordance with different needs to finish data analysis and processing, and provide preparation for data mining tasks.

The data warehouse in MSMiner is able to accommodate many subjects. As the data warehouse is created, users determine subjects based upon the application, and the system helps users extract data for each subject and organize them with star schema. The data warehouse is equipped with a multidimension data cube and OLAP, and is able to validate data for data mining and decision-making purposes. The analysis results may be shown through the use of visualization tools [8].

![](/api/attachments/8WAB4Q5B/fulltext/images/d0e851ccfdb2970a2d76f5c75f3d9a9a991616bbe9e64ac2f2ba2794b91904c4.jpg)  
Fig. 1. Architecture of MSMiner.

The data in the data warehouse in MSMiner are modeled by star schema. The system extracts the data from source tables, or views and builds multiple fact tables through data extraction, transformation, and loading. A star schema is made of one fact table and several dimension tables related to the fact table, in which the fact table includes multiple dimensions and measures. The dimension stands for the special visual angle for viewing data, such as a time dimension, distribution dimension, product dimension, and so on. The measure is data’s real meaning and describes the true value of the data. Each dimension table describes a certain dimension and its values, and each dimension consists of several levels. For example, a time dimension may be divided into three levels: year, season, and month, as each describes different query layers. One or several star-schema structures form a subject, which is the basic unit of a data warehouse.

## 4.1.1. Star-schema creation in MSMiner

The process of creating star-schema cube in MSMiner is shown in Fig. 2:

Create shared dimensions: A shared dimension is a dimension available to multiple cubes in a database. Shared dimensions are usually created for common dimensions, such as time, that will be added to multiple cubes. Users can create a shared dimension quickly and easily by using the dimension wizard in MSMiner. The wizard takes the user through several steps to specify parameters (such as dimension table, dimension levels, etc.) for the shared dimension

Select fact table: The table is the result of applying a cube operator to the table that contains the detailed atomic records. It has one column for each level in each dimension of the cube. The value column has the actual data value.

Select shared dimensions: Users can select the created shared dimensions for the cube. One cube can have one or more shared dimensions.

Create private dimensions: The private dimension is a dimension for just one cube. Users can create one or more private dimensions while creating cubes. However, one cube must have an equal number of dimensions or more than two dimensions, whether for shared dimensions or private dimensions.

![](/api/attachments/8WAB4Q5B/fulltext/images/fb575ad5eb3a5d46960f3e35e3ae48401eaeea02fec49de7aee20a19dfb6d37c.jpg)  
Fig. 2. Process of creating star schema model.

Select measures: One cube must have one or more measures. The measures selected depend upon the types of information requested by the users. Some common measures are sales, cost, expenditures, and production count.

## 4.2. Data mining

The data mining subsystem organizes and executes the data mining task in the object-oriented form and its data sources are obtained from the data warehouse. It includes many data mining algorithms and possesses flexible expandability.

Data mining subsystems generally include an algorithm manager, task manager, and task process ing engine for data mining. An algorithm manager is in charge of registering new or unregistered existing data mining algorithms, those of which can be called by data mining tasks. the Task manager helps users select data sources and mining algorithms, and build corresponding task models by providing a task wizard. The task processing engine’s function is to schedule and execute tasks. It achieves high efficiency by using multithread technology. After the results are explained and evaluated, it is stored in a data warehouse and can be visualized or exported to files. The basic architecture of the data mining subsystem is shown in Fig. 3.

## 4.2.1. Expandable algorithm base

In this subsystem, the core algorithms for data mining are realized in the form of a dynamic linked library (DLL). A set of standard interfaces has been defined for the DLLs that embed data mining algorithms. Any algorithm, if encapsulated according to those interfaces, can be integrated into the system conveniently. Thus, users can develop their own data mining algorithm modules easily in this system. In addition, there are some add-in algorithms in this subsystem. Users can use them directly to accomplish some data mining tasks (Fig. 4).

At present, the system provides a variety of algorithms, such as decision trees, backpropagation, SVM, fuzzy clustering, SOM, multiple regression analysis, CBR, and association rules discovery [16]. They are applied to classification, prediction, clustering, and data reduction purposes.

Users may develop new algorithms and add them into an algorithm base; then they can be called by data mining tasks flexibly. Only a DLL for the algorithm needs to be developed. The DLL of data mining algorithm can implement the following major interfaces:

General information interface: GetAlgorithmInformation( ). This function presents the information of the algorithm itself, such as the name, author, version, etc.

Parameters setting interface: SetAlgorithmParameter( ). This function is used to set the parameter of the algorithm when the user is interested in using it. Parameters include the data source, the position to save result, and other necessary parameter to run the algorithm.

Parameter modifying interface: ModifyAlgorithm-Parameter( ). This function is used to modify the parameter that the user has established.

Executing interface: ExecuteAlgorithm( ). Users can call this function to run the algorithm.

## 4.2.2. Data mining task

In MSMiner, a data mining task consists of one or more data mining steps; a data mining step corresponds to a data mining algorithm and the parameters of the algorithm. The description in an object-orient method is as follows:

![](/api/attachments/8WAB4Q5B/fulltext/images/1de570d157f8457d8964e0e22900022258892b007a7985b03bfba62248118b2a.jpg)  
Fig. 3. Data mining subsystem architecture.

![](/api/attachments/8WAB4Q5B/fulltext/images/e889d62185f7597e79c3b5238e7ca3256d3eee7ebd3cccfca93705c5af13b228.jpg)  
Fig. 4. An example of data mining task.

Definition 1. A data mining task is defined as: TaskDM=(V,R):

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$V = \{x|x\in \text{StepObjectS}\};$ $R = \{&lt; x,y &gt; |P(x,y)\wedge x,y\in V\} .$ $P(x,y)\left\{ \begin{array}{ll}1 &amp; \text{if the output of } x\text{ is the input of } y\\ 0 &amp; \text{else} \end{array} \right.$
</div>

StepObject represents the data mining step, and StepObjectS represents the collection of the StepObject. BNF can be used to describe the data mining step:

```txt
<StepObject>::=<Attribute_List>;<Method_List>
<Attribute_List>::=[<Attribute>\<Attribute>;<Attribute_List>]
<Attribute>::=<Name>,<Value>
<Method_List>::=[<Method>\<Method>;<Method_List>]
<Method>::=<Name>,<Script>
<Name>::=[<char>\<string>]
<Value>::=[<char>\<string>\<integer>\<float>]
<Script>::=<InterfaceS of DLL of Data Mining Algorithm>*
```

where <sup>b</sup>char<sup>N</sup>, <sup>b</sup>string<sup>N</sup>, <sup>b</sup>integer<sup>N</sup>, and <sup>b</sup>float<sup>N</sup> represent constants of the corresponding type.

In the data mining steps, one step can have null or more prior steps and null or more succeeding steps. A task can have one or more beginning steps (the step that has no prior steps) and just one ending step (the step that has no succeeding steps). The output of the ending step is the output of the whole task.

## 4.2.3. Data mining task wizard

As mentioned above, a data mining task consists of several mining steps, each step corresponds to a data mining algorithm module (a DLL) and requires some parameters. In order to build mining tasks more conveniently, the system provides a mining task wizard. Through the wizard the users may select mining algorithms by steps, set parameters of the algorithms and select the data sources. Therefore, adaptive task models are constructed for all data mining algorithms provided by the subsystem.

## 4.2.4. Flexible task scheduling

A flexible task scheduling module has been developed in this subsystem. Users can schedule a task conveniently using this function. Users can let a task be executed at designated times through configuring several parameters, or they can let a task be executed by a specified period.

Assume that there is a data mining task to predict the turnover of a company. As the new data are added into the system every month, the data source of the task will be updated frequently. In order to get the updated output anytime, users can set the schedule parameters of the task (for instance, execute at the last day of the month, and repeat per month), and the task process engine will perform the function automatically.

## 4.2.5. Efficient task processing

There could be many tasks in a mining system, and a mining task may include many steps. Such tasks or steps can be executed concurrently. In the system, multithread technology has been employed to achieve concurrent processing. The task processing engine is in charge of checking all tasks in the system; if one task is to be executed, the system will create a new thread to process the task.

The steps involved in one task are executed concurrently. The order of steps in one task may have some restrictions (commonly is a DAG): the algorithm for executing steps is as follows:

/\*\*\*\*procedure for executing data mining task\*\*\*\*\*\*/

Procedure exec\_mining\_task( )

BEGIN

Calculate the prior step count of all steps.

IF (has steps whose prior step count is 0) THEN Create a new thread for every step whose prior step count is 0

ELSE IF (all step is executed) THEN Return ELSE

Error (has cycle in the steps)

ENDIF

Wait 3 s/\*\*wait while the step executing\*\*\*\*/

END

/\*\*\*\*\*\*\*\*\*In the thread of step executing, if the executing step is finished, then for all steps whose prior steps include this step, the prior step count will decrease for one amount\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

## 4.2.6. Evaluation and interpretation of the mining results

The results from data mining are usually in the form of abstract models or data. They are difficult to be understood by general users. The system provides a tutorial to help users understand the results. The tutorial can present and explain mining results in various visual forms.

Different mining methods have different features. Validity and efficiency are very important to mining algorithms. MSMiner provides evaluation tools, which can provide corresponding evaluation mechanisms to differing mining algorithms and help users evaluate results, update data, improve mining performance, or compare and synthesize results for better decision support. For mining algorithms, explanation and evaluation are relatively independent since many similar results may use the same method for explanation and evaluation. In the system, only the format of the result and standard rather than the methods for result explanation, estimation, and visualization are emphasized. The mining results are saved in the data warehouse to let users query them conveniently at any time.

## 4.2.7. Create and run a data mining task using MSMiner

Creating or running a data mining task is very convenient by using MSMiner. A straightforward wizard is provided to help the user create a complicated data mining task easily. The process of creating a data mining task is described in Fig. 5:

! <sub>Start task wizard: As mentioned in Section 4.2.3, a</sub> straightforward wizard is provided to help the user create data mining tasks. The mining task wizard is based on dialogs.

! <sub>Input the general information: Users can establish</sub> some general information for this task, such as the task name, author, description of the task, etc.

![](/api/attachments/8WAB4Q5B/fulltext/images/e5f0eb8a85038a16dfafeab64104ccea6ad7f8e603f08a32301805dad11f0d43.jpg)  
Fig. 5. Process of creating data mining task.

! <sub>Add data mining steps: A data mining task must</sub> have one or more mining steps. A mining step corresponds to a data mining algorithm (DLL).

! <sub>Set</sub> <sub>step</sub> <sub>parameters:</sub> <sub>The</sub> <sub>parameters</sub> <sub>of</sub> <sub>a</sub> <sub>mining</sub> step consist of two parts: one is general information, such as step name, step description, etc.; the other is parameters of the algorithm, such as input table(s), output table(s), some parameters for the given algorithm $\mathrm { ( e . g . , } $ support ratio), and reliability for an associate rule algorithm (see Fig. 6).

! <sub>Set the relationship of data mining steps: A</sub> mining task has one or more mining steps. Users can set the relationship between steps while creating a mining task. If the input to a step is the output of another step, then the user should set the second step to the prior step of the first step.

! <sub>Close the wizard: Closing the task wizard to</sub> finish the task building process after the user has added all mining steps required in the task. Then, the task is created, and the user can run it at anytime.

MSMiner provides two ways to run a data mining task. One is to execute a task immediately; the other is to schedule the task for later execution.

![](/api/attachments/8WAB4Q5B/fulltext/images/270f1b98a9c3dcf4b3c3a890fa9666240a93af3eac9d418937d113a1400c1741.jpg)  
Fig. 6. Setting parameters for a mining step.

## 4.3. ETL

An ETL subsystem is an important subsystem of MSMiner. The main objective of the ETL function module is to transform the operational data from source database to analytical data in the data warehouse. It is known that the data in a data warehouse are extracted and integrated from diverse database platforms such as Oracle, SQL Server, DB2, etc., and there are many differences between the operational data in the source database and the analytical data in a data warehouse; therefore, it is not practical to load the data from various data sources into a data warehouse directly. In simple words, to obtain the clean data for a data warehouse, the data from source databases must be cleaned and transformed before being integrated into a data warehouse. It is a key and complex step for building data warehouses. Generally speaking, the ETL subsystem is expected to finish the following tasks:

(1) Due to data redundancy and inconsistency in the source data from diverse sources, the subsystem is expected to eliminate data inconsistency.

(2) To obtain required data for the data warehouse, the subsystem is expected to convert the original data structures from application-oriented to subject-oriented and perform certain computations. The basic architecture of an ETL subsystem is shown in Fig. 7 in which four modules are included.

(3) User friendly interface: Users can request any ETL operations expediently by using the interface including designing ETL tasks, registering new ETL DLL functions, scheduling and executing ETL tasks, and evaluating the results of ETL tasks.

(4) Integrated ETL function management and ETL task management: This module helps to register new ETL DLL functions, build new ETL tasks, and schedule and process ETL tasks.

(5) Consistent and integrated metadata management: The whole subsystem is developed in a metadata-oriented way. Namely, all information of this subsystem, including data sources, algorithms and results, is managed by metadata.

(6) Database server: An ETL subsystem supports diverse database platforms such as Oracle, SQL

![](/api/attachments/8WAB4Q5B/fulltext/images/6669b88fd4c29d4a7149c2ffd9260000f1b143347aabf1f20cf2f65ddb34bca7.jpg)  
Fig. 7. Basic architecture of the ETL subsystem.

Server, DB2, Access, Excel, and Foxpro. The subsystem also supports the expandable ETL function base. The main algorithms of the ETL function are realized in the form of a DLL with unified interfaces. Users can design the ETL task according to their needs by choosing the relevant ETL DLLs. At present, the subsystem provides 30 types of ETL DLLs. In addition, users can develop some new ETL DLLs in accordance with unified interfaces, and add them into the ETL function base. In order to improve efficiency, ETL tasks can be scheduled at designated times or processed concurrently.

## 4.4. OLAP

The OLAP is realized by two ways: creating special multidimensional OLAP (MOLAP) and simulating the multidimensional data by using the relational OLAP (ROLAP). MSMiner supports ROLAP, which is based on the star schema. The star structure related to multidimensional tables facilitates the use of the multidimension data cube because the dimensions and measures in data cubes are from dimensions and measures in star schema. When OLAP operations are executed in the data cube, multidimensional analysis translates the request into SQL statements, and queries in fact tables, then the results in the form of multidimension are shown.

Currently, the system supports standard OLAP operations, such as slice, dice, roll up, drill down, and pivot; the results may be displayed in many forms such as cross-tabulation tables, bar charts, pie charts, or other forms of graphical output.

## 4.4.1. Material view

Material views are precalculated summaries of data that improve query response time by having the answers ready before the questions are asked. For example, a query requesting the weekly sales totals for a particular product line from a data warehouse fact table that contains hundreds of thousands of rows of transactions can take a long time to answer if the fact table has to be scanned and the answer has to be computed. The answer could be almost immediately available if the summarized data for responding to the query have been precalculated. Precalculation of summary data is one of the features provided by rapid response in OLAP technology.

MSMiner creates material views for each cube, each dimension in a cube, and each level in a dimension automatically after a cube is created by users, and users can rebuild material views for a cube manually.

## 4.4.2. Using OLAP in MSMiner

MSMiner provides two modes to help users explore cube data: cross-table mode and graphic mode.

4.4.2.1. Using cross-table mode. A screen of a cross table to view cube is shown in Fig. 8. Users can slice, dice, roll up, drill down, and pivot using this cross-table.

![](/api/attachments/8WAB4Q5B/fulltext/images/771184238ed4e6690a1aade9f9cabfe569a95599898b0bbc6c732678147cffb6.jpg)  
Fig. 8. A screen of a cross table to view cube.

4.4.2.2. Using graphical mode. To view data in graphic mode:

n Select the data area to view in cross-table

n Right-click it

n Select graphic mode in the pop-up menu.

Users can select many kinds of graphic modes to view the data, such as two-dimensional bar, threedimensional bar, two-dimensional line, two-dimensional pie, etc. An example of a two-dimensional bar graphic is shown in Fig. 9.

## 4.5. Metadata

Metadata are data about data that describe the content, quality, condition, and other characteristics of data. They play an important role not only in the design, implementation, and maintenance of the data warehouse, but also in data organizing, information querying, and output interpretation [10]. It usually records the location and the description of warehouse system components. In this system, the scope of the metadata has been expanded; the metadata are also used to describe and manage the data and environment of the whole system, which includes not only the data in the data warehouse platform but also the task model and algorithms or functions in ETL and data mining. Metadata hold a key position within the entire system since they integrate the ETL, data warehouse, and data mining tools. They control the whole flow from ETL, to data warehouse, to data mining, so users can define and execute ETL and data mining tasks more conveniently and effectively. In MSMiner, the contents of the metadata are as follows:

(1) Description of the external data source: The external data source can be a relational database or another kind of data, such as Excel data, plain text, XML text, etc. In metadata, it contains allocated position and environment information of the external data source, data structure, and description of the contents.

(2) Descriptions of the subject, including the name and remark of the subject, the time when the subject is created and updated, etc.

(3) Description of databases under a subject, including the name, type and remark of database, log-in information, and other information.

(4) Description of tables in a database including fact tables, dimensional tables, and temporary tables. It contains table information and field information.

(5) Description of the ETL task, including organization and steps of the tasks, data source, selection of transformation functions, assumption of the parameters, and creation and execution history of the task.

![](/api/attachments/8WAB4Q5B/fulltext/images/d7af8308cf0b152c06fa6bfcf1465e70d7408df8fcad7eba33de549d287b1eda.jpg)  
Fig. 9. An example of a two-dimensional bar graphic.

(6) Description of the data mining task, including organization and steps of the tasks, data source, selection of the mining algorithms, assumption of the parameters, evaluation and output of the results, and creation and execution history of the task.

(7) Description of the data cube, including dimension and measure of extracted information, and information of the star structure.

(8) Management of the algorithm base for data mining includes the registration and management of mining algorithms.

(9) Management of the functions for ETL, including the registration and management of the functions.

(10) User information, including users’ basic information, authorization, operational history, and so on.

The corresponding metadata classes are developed using object-oriented methods. In the three-tier system architecture, the metadata management subsystem is at the middle tier position. It can be regarded as a metadata management server. The upper tier accesses and manages metadata with the help of middle tier. Metadata are automatically generated while every component of the system is created. Changes are made to metadata during daily maintenance of the system. MSMiner provides special metadata manager subsystems that can maintain the metadata directly and manage the whole system more effectively.

The metadata management subsystem exchanges information with other systems through XML string. For example, an ETL task can be represented as:

```txt
<ETLTaskModel>
    <TaskName>taskTest</TaskName>
    <TaskID>a6f0b7e3-c698-cd89-8809</TaskID>
    <author>jzy</author>
    ....
    <ETLStep>
    <StepName>step1</StepName>
    <StepID>a6f0f34-564r-f5e667-y56456
    </StepID>
    ....
    <PreStep>{Steps}</PreStep>
    <StepDLL>filter</StepDLL>
    <StepPara>
```

```xml
<para1>
<paraName>SourceDataName</paraName>
<paraType>String</paraType>
<paraValue>sourceTest</paraValue>
</para1>
.....
</StepPara>
.....
</ETLStep>
</ETLTaskModel>
```

## 5. An application example

MSMiner has been applied to many application areas including tax evasion, analysis of fishery information, and analysis of very important persons (VIPs) for telecommunications corporations. In this paper, an example of how to solve the problem of discovering tax evasion is introduced. Taxation is a complicated process. Many factors must be taken into account for decision making. Among such factors, some are more important than others, and some are more difficult to define than others. Therefore, conventional decision tree algorithms do not fit such problems well. In this study, a method that takes advantage of the tax experts’ knowledge is used to provide an appropriate assessment of related factors.

Two coefficients, cost coefficient and preference coefficient, are used to construct an attribute selection function. Next, using the given tax data sets, decision trees are generated using GSD algorithm [20]. A production rule set is converted from the decision trees and stored into a knowledge base. These rules are stored in the knowledge base to form SQL statements, which are then used to search taxpayers’ records that meet a given criteria. All of the records retrieved from the tax database are records of those taxpayers facing possible auditing or investigation. It is an automatic evasion discovery process.

## 6. Conclusions

MSMiner is a developing platform for DSS. Based on data warehouse technology, the system is able to support multiple data sources and OLAP. The system adopts object-oriented methods to represent metadata and describes mining task and procedure, integrates data and mining algorithms, and possesses powerful generality and expandability. Based on this platform, some specialized DSS have been developed. In order to improve system performance and intelligence, current research will expand the scope of the system to adjust mining steps automatically, and develop more strategies and algorithms for handling a large quantity of data.

## References

[1] E. Blanzieri, P. Giorgini, P. Massa, S. Recla, Data mining, decision support and meta-learning: towards an implicit culture architecture for KDD, Proceedings of the Workshop on Positions, Developments and Future Directions in Connection with IDDM-2001, September, 2001.

[2] W. Fan, H. Lu, S.E. Madnick, D. Cheung, DIRECT: a system for mining data value conversion rules from disparate data sources, Decision Support Systems 34 (2002) 19–39.

[3] M.S. Gorry, Scott Morton, A framework for management information systems, Sloan Management Review 13 (1) (1971) 50–70.

[4] J. Han, K. Chang, Data mining for web intelligence, IEEE Computer 35 (11) (2002) 64– 70.

[5] C.W. Holsapple, A.B. Whinston, A decision support system for area-wide water quality planning, Socio-Economic Planning Sciences 10 (6) (1976) 265– 273.

[6] W. Inmon, Building the Data Warehouse, QED Technical Publishing Group, 1992.

[7] H.X. Li, L. Xu, Feature space theory—a mathematical foundation for data mining, Knowledge-Based Systems 14 (2001) 253– 258.

[8] T. Li, S. Feng, X. Li, Information visualization for intelligent decision support systems, Knowledge-Based Systems 14 (5–6) (2001) 259–262.

[9] H.X. Li, L. Xu, J. Wang, Z. Mo, Feature space theory in data mining, Expert Systems 20 (2003) 60 – 71.

[10] O. Mangisengi, M. Tjoa, R.R. Wagner, Metadata for data warehouses using extended relational models, Proceedings of the Third IEEE Computer Society Metadata Conference, Bethesda, MD, April, 1999.

[11] S. Miksch, Artificial intelligence for decision support: needs, possibilities, and limitations in ICU, in: A. Gullo (Ed.), Anaesthesia, Pain, Intensive Care, and Emergency Medicine (APICE-95), Proceedings of the 10th Postgraduate Course in Critical Care Medicine, Springer, Berlin, 1995, pp. 901–908.

[12] R.H. Mohring, R. Muller, F.J. Radermacher, Advanced DSS For Scheduling: Software Engineering Aspects and the Role of Eigenmodels, Proceedings of the 27th Annual Hawaii International Conference on System Sciences, Maui, HI, 1994.

[13] A. Needamangala, A library decision support system built on data warehousing and data mining concepts and techniques, Thesis for Master’s Degree, University of Florida, 2000.

[14] J.L. Pollock, OSCAR-DSS, OSCAR Project Technical Report, 1997.

[15] M. Postema, T. Menzies, X. Wu, A decision support tool for tuning parameters in a machine learning algorithm, PACES/ SPICIS ’97 Proceedings, Nanyang Technological University, Singapore, 1997, pp. 227 – 235.

[16] Z. Shi, Knowledge Discovery, Tsinghua University Press, 2001.

[17] P. Shim, M. Warkentin, J.F. Courtney, D.J. Power, R. Sharda, C. Carlsson, Past, present, and future of decision support technology, Decision Support Systems 33 (2002) 111 –126.

[18] J. Tian, Y.L. Wang, H.Z. Li, L.X. Li, K.L. Wang, DSS development and applications in China, Decision Support Systems (in preparation).

[19] F. Zelezny, J. Zidek, O. Stepankova, A learning system for decision support in telecommunications, Proceedings of the of the 1st International Conference on Computing in an Imperfect World, Belfast, April, 2002.

[20] Y. Zhang, Z. Shi, N. Tan, X. You, S. Ye, Applying data mining to tax deviation, Proceedings of the PAKDD’99 Workshop, 1999.

[21] Y. Zhu, C. Bornh<sup>f</sup>vd, D. Sautner, A. Buchmann, Materializing web data for OLAP and DSS, 1st International Conference on Web-Age Information Management, WAIM’00, Shanghai, China, June 21–23, 2000.

[22] http://www.spss.com/spssbi/clementine/.

[23] http://www-3.ibm.com/software/data/iminer/.

[24] http://www.sas.com/products.miner/.

[25] http://www.sgi.com/software/mineset.html.

[26] http://www.intsci.ac.cn/.

Zhongzhi Shi is a Professor at the Key Laboratory of Intelligent Information Processing, Institute of Computing Technology, Chinese Academy of Sciences, IEEE Senior member, AAAI member. He is the Chair of WG 12.2 of IFIP. He also serves as Vice President of the Chinese Association for Artificial Intelligence. He received the 2nd Grade National Award of Science and Technology Progress in 2002. In 1998 and 2001, he received the 2nd Grade Award of Science and Technology Progress from the Chinese Academy of Sciences. His research interests include intelligence science, data mining, multiagent systems, and Semantic Web. He published 10 books and edited 11 books and more than 300 technical papers. Contact him at shizz@ics.ict.ac.cn. Homepage is http://www.intsci.ac.cn/en/shizz/.

Youping Huang was born in the province JiangXi, China, in 1975. He recieved the BS degree in Application-Mathematic from the TsingHua University, Beijing, China, in 1996, and the MS degree in computer software from the Beijing University of Posts and Telecommunications, Beijing, China, in 2002. He is currently pursuing the PhD degree at the Institute of Computing Technology of Chinese Academy of Sciences. His current research includes data mining, data warehouse, artificial intelligence, information geometry, and Bayesian network.

Qing He received his BSc degree from Department of Mathematics, Hebei Normal University in China, and MSc degree from the Department of Mathematics, Zhengzhou University, and the PhD degree from Beijing Normal University in 2000. He has been an Associate Professor of the Key Laboratory of Intelligent Information Processing, Institute of Computing Technology, Chinese Academic of Sciences (KLIIP, ICT, CAS) since 2000. His research interests are in the areas on machine learning, data mining artificia intelligence, neural computing, and cognitive science.

Ziyan Jia was born in the province ShanDong, China, in 1971. She recieved the BS degree in Computer Science from the ShanDong University, ShanDong, China, in 1995, and the MS degree in Computer Software from the Beijing University of Technology, Beijing, China, in 2001, and the PhD degree in Computer Science from the Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China, in 2004. Her research includes data mining, information retrieval, web search engine, and artificial intelligence.

Liangxi Qin received his BSc degree from the Guangxi University in 1983. He also finished MSc courses in Guangxi University in 1992, and now he is a PhD candidate in the graduate school of the Chinese Academy of Sciences. He has been an Associate Professor in the Guangxi University since 1997. His research interests include data mining, evolutionary computation and software engineering.

Huijing Huang received his BS degree from Peking University in 1996, and will be awarded an MS degree in 2005 by the Institute of Computing Technology, Chinese Academy of Sciences. Currently he is an engineer and a project manager at the Bureau of Personnel and Education, Chinese Academy of Sciences, Beijing, China. His research interests include network administration, data mining, and software engineering.

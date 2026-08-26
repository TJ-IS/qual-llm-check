---
otero_id: 18088
otero_key: "CK36J6V4"
title: "An effective database formation for decision support systems"
authors: "Tetsuo Hirouchi; Takeshi Kosaka"
year: "1984"
journal: "Information & Management"
doi: "10.1016/0378-7206(84)90018-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An Effective Database Formation for Decision Support Systems

Tetsuo Hirouchi

Bunkyo University, Faculty of Informatics, 3337

Minami-ogishima, Koshigayashi, Saitamaken, 343 Japan

and

Takeshi Kosaka

Nippon Univac Kaisha, Ltd., Applications Software Dept., 17-51, 2-chome, Akasaka, Minatoku, Tokyo, 107 Japan

Managers' tasks have two aspects: to monitor (control) business activities and to plan the future based upon the monitored results. Thus a decision Support System (DSS) must have two kinds of databases appropriate for its needs.

A management database, i.e., one for monitoring activities, is constructed mainly from the existing operational databases. A data cube should be employed for the logical data structure of the management database so that managers can share it and access it in multiple ways.

Planning databases, i.e., those for planning activities, are constructed mostly from the management database. A table form should be employed for its logical data structure so that managers will find it easy to use.

The management and planning databases should be connected through DSS's system architecture [1]. This makes the operational data (indicating business activities) directly and immediately available for management decision making.

We have previously presented the DSS architecture. This paper discusses the management and planning databases from the viewpoint of it.

Keywords: CODASYL database, Database, Database formation, Data oriented DSS, Data structure, Decision making, Decision support model, Decision Support System, DSS, Information resources, Management information, Model oriented DSS, Relational database.

## 1. Introduction

Computer based information systems have been useful for clerks in charge of operational control and planners using financial accounting models for strategic planning. However, these systems are utilized by only a few managers engaged in management control. This may be due to lack of user-friendly, highly flexible software suitable for managers, but is probably more related to lack of suitable databases that were created with particular emphasis on management information needs.

![](/api/attachments/CK36J6V4/fulltext/images/baaccf651fd12dbfc480860d130e33e4cfddfe12c8f82989baecff0591588652.jpg)

Tetsuo Hirouchi is a researcher in the Faculty of Informatics at Bunkyo University (Japan). He received a M.S. in molecular science majoring in theoretical studies from Tokyo University of Education. His research interests focus on the field of computer-based information systems (systems analysis, systems design, systems implementation, database systems, and Decision Support Systems). He is the author of more than 10 technical papers in these subjects. Prior to joining Bunkyo University, Mr. Hirouchi worked for Nippon Univac Kaisha as a chief systems designer. His working effort was mainly in the areas of Decision Support Systems. He is a member of Information Processing Society, Office Automation Society, Operations Research Society, and Simulation Society in Japan.

![](/api/attachments/CK36J6V4/fulltext/images/fb2ad4718cb137fb40edcbf8eaf93ad439d922f7ac0f265384aaa5c0dffd1936.jpg)

Takeshi Kosaka is a systems analyst at Nippon Univac Kaisha, Ltd., in Tokyo. He received his B.S. in electronics engineering from Sophia University. With his industrial experience in systems design, he has presented numerous papers on Decision Support Systems, database design, systems implementation, scheduling techniques and office automation. His research interests include information analysis, managerial accounting and information systems implementation. Also in the DSS working group of the Operations Research Society of Japan, Mr. Kosaka is currently active in working out the characteristics of information systems essential to japanese Management.

Management data used in management control mainly concerns business operations and factors which influence business activities. Therefore, it differs from either transaction data for operational control or financial data for strategic planning. This suggests that managers' needs can not be met by existing databases.

Managers have two main tasks: monitoring and planning. These tasks have the mutually different aspects with respect to managers' information needs and data manipulation. This suggests that, in order to meet managers' such needs, two kinds of databases must be supplied: one is for monitoring and the other is for planning. Hereinafter, the former is called 'management database' (management DB) and the latter, 'planning database' (planning DB).

Decision support systems (DSS) improve management decision making by assiting in solving problem and by facilitating intra-company communication. The purpose of this paper is to discuss the roles of management DB and planning DB suitable for the DSS and the methods for constructing them.

## 2. Management Database

## 2.1. Characteristics of Management Database

In order to monitor their business activities, managers need such data as [2]:

1) Marketing data: indicating the company's sales achievements (e.g., total sales and breakdowns according to customers or regions).

2) Planning data: showing the strategic business plan broken down into units, such the sales plan for a particular product.

3) Competitive data: on competitors' activities (e.g., competitors' sales figures and market share).

4) Economic data: concerning relevant economic factors (e.g., on the regional economy, including population, the number of households and incomes, and market trends).

The above data have to be stored in a management DB. Although most companies need such data, specific data varies, depending upon the industry, company, and managers. Therefore, it is not easy to describe it in general. Thus, data selection must not be made by conventional computer specialists but by information specialists with knowledge of specific managers' view. They should observe and forecast changes in requirements and thus store data of lasting value.

Managers often project performance by studying past activity. If the management DB is fragmentary, managers' needs will not be satisfied. The need is ultimately for a single, large-scale management DB because the database is shared by so managers engaged in different aspects of functional management. A DBMS must be available to aid in sharing and manipulating the data efficiently.

## 2.2. Database Linkage System

Manamement data is related to the operational data as shown in Fig. 1. This needs an interface system to summarize and transcribe the data – called a 'database linkage system'. This sorts out the data in the operational databases (operational DBs), classifies, summarizes, and stores it in the management DB.

A management DB must be designed by information specialists. They determine the data extraction procedure for the database linkage system. The procedure is not always stable permanently after it is established. The contents of operational DBs gradually change according to changes in merchandise and in the business environment. Therefore, they must adjust the data extraction procedure to absorb the above changes so that management DB should not be affected directly by changes in the contents of operational DBs and it should be a stable information resource.

Competitive and economic data are obtained by: purchasing data from market research companies, transcribing data from periodicals, direct investigation, etc. Such data must be systematically arranged and stored, as shown in Fig. 1. Business plans can also be input.

Management DB must be maintained and kept up-to-date by the database linkage system; however, since it is not generally time critical, it may be updated during “slow periods”, – e.g., after business hours.

## 2.3. Data Structure

Management data is required to be available in many different ways. This has been recognized for many years, but Rockart recently suggested a 'data cube' as a useful form for expressing management data [3]. There are three axes: business unit, business variable, and time. We present an expansion of Rockart's data cube - with five dimensions:

![](/api/attachments/CK36J6V4/fulltext/images/c5741f2607fd6d339f5e2e358f0707193bb857be053bd33faba11b3b111938ed.jpg)  
Fig. 1. The management DB environment.

management view, business unit, business variable, attribute, and time.

A ‘management view’ usually corresponds to a sub-segment of functional management, such as production management, sales management, and financial management. Each management view can be considered to have its own data cube. A management view is then the name for one of many data cubes.

![](/api/attachments/CK36J6V4/fulltext/images/c0bfdc6468a89d9db097afcd5fd9fb5e0099d3040cc24f94bea7c255c894089e.jpg)  
Fig. 2. A data cube representing the management view.

Business unit, business variable, and time are the three axes of the data cube. 'Business unit' is a segment responsible for a specific business (generally, an organization in a company). 'Business variable' pertains to the company's activities, such as goods, products, raw materials, and money. 'Time' is a unit of progress in a business activity (e.g., annual, monthly, or daily units).

The entry in a cube location is termed ‘data element’. It is usually atomic but sometimes is a group of data classifies by ‘attributes’; e.g., planned and actual sales data are both sales data. The attribute “planned” or “actual” defines which is which.

As an example, consider a car sales company. The management view focuses on car sales management, and the data cube shown in Fig. 2 may be constructed. The business unit is a branch, and the business variable is the kind of cars being sold. There are two sorts of attributes for each data element: actual and planned.

Expressing data in this way makes it easy to analyze business activities, because various cross sections of the data cube show various aspects of the business. Cross section A in Fig. 2 indicates the branch sales figures as a time-series for a specific type of car. Cross section B shows sales figures as a time-series classifies by types of cars at a specific branch. Cross section C indicates sales figures for each branch classifies by types of cars at a specific time.

## 2.4. Flexibility of Access

In the example of car sales management, a sales manager may concentrate on one specific branch, and wish to analyze sales trends for all types of cars throughout the preceding year, whereas a supervisory manager (at head office) may need to know the total number of cars sold at each branch at a specific time. The first requires time-series data and the second, cross-section data. However, the information requirements are identical as far as the information source is concerned: the difference is in how it is observed.

Flexibility of management DB required when managers need specific information is nothing but the flexibility of database query facilities of DSS. It should be understood that flexibility must be implemented on the side of the facilities not but on the side of the management DB. DSS should have the capability to freely derive any cross section of the data cube (e.g., cross sections A, B and C in Fig. 2), and must be able to arrange the data as either time-series data or cross-section data in the form of tables.

## 2.5. The Realization Method and Some Examples

A CODASYL type network data model is used here, because it allows efficient manipulation of a large amount of data, with a structure independent of a particular usage.

When data was stored on the CODASYL database, we used different record types for business units and business variables. For a business variable, time-series data was included within an attribute. As in the real world, we made business variable a member record of a business unit, because the business variables involve the products and the business units indicate organizations that deal with the products. Therefore data cube was represented as two record types interconnected by a set.

The car sales management example can be expressed as shown in Fig. 3. Axes are business unit (branches) and business variable (kind of car), which are the keys for the two record. The axis of time is included in the second record. In this example, a data element within the data cube has two attributes, i.e., planned and actual. Therefore, both time-series are included in the second record type. Thus, a data cube may generally be represented as a combination of two record types.

Generally, management data requires more than one data cube. In a CODASYL system, such databases are realized by producing a schema of network structure with such sets of two record types as the nucleus. This process is indicated in Fig. 4.

When producing such a schema, record types with the same business unit, if exist, are incorporated into a single unit. This is illustrated in the customer record type being shared by two data cubes. For convenience, in this way, if there is a useful relationship between different business units, an extra set type may be established between them (see the branch to customer link).

In DSS1100, i.e., the system we have built on the UNIVAC DMS1100 DBMS, various information about data cubes are stored in the data dictionary which is a component of DSS1100. In order to make it easy to deal with time-series data, the start time and periodicity of such data can be defined either in the record occurrence or else in this dictionary. The DSS1100 database query facilities allow users to obtain any cross section of a data cube. Complicated searches into management DB refer to the data dictionary.

A series of examples using the car sales management will be used to show the process. The communication between users and DSS1100 and the output result are shown in Fig. 5.

In Case 1, sales figures for each branch of the selected type of car, Comet, with respect to a time-sequence is determined by using cross section A. In Case 2, the actual and the planned using values of sales figures for various types of cars at the Tokyo branch in March 1984, is determined by selection from cross section B.

![](/api/attachments/CK36J6V4/fulltext/images/17e02615e731f4432890d887ce56cc7193c87e1e290192ac59452f3874a50745.jpg)  
Fig. 3. A data cube and its corresponding record combination.

Users must input the management view, business unit, business variable, attribute, and time; however, the cross sections of the data cube are automatically identified within the database query facilities. Users may also transpose a cross section in their tables.

## 3. Planning Database

## 3.1. Characteristics of Planning Database

The data used for planning is usually more diverse than that for monitoring. It is difficult to predict what kind of data will be needed, and once used, it is often discarded. Also external data (e.g., economic and competitive data) are often more sensitive.

![](/api/attachments/CK36J6V4/fulltext/images/b17dc79f9d447c307b9a8834414dbae76a16c1e977c2b61ea91d90b9599cceb9.jpg)  
Fig. 4. Creation of a database schema.

It is difficult to meet information requirements with only a relatively fixed management DB. Therefore, managers who use DSS for planning need a more flexible database, i.e., planning DB. It is not generally necessary to share a planning DB throughout the company; planning DBs are diversified and used less frequently. If each planning DB is independent, but all planning DBs have a common data structure, managers can use their planning DBs, to relate their planning DBs with others.

![](/api/attachments/CK36J6V4/fulltext/images/85c03c6863bf5af089c3b0c3a8cb2d3f1a7cc02ad88197ad7deaeacce4c9eb1f.jpg)  
Fig. 5. Examples of the management DB retrieval.

## 3.2. DSS Cooperation

We suggest that planning DB needs the DSS's system architecture in Fig. 6. The 'DSS architecture' was discussed in our previous paper [1]. There, many functional model components of the DSS (e.g., modules for database, query, graphic representation, data manipulation, data analysis) are prepared as independent programs and built into the DSS. These functional model components are designed to communicate with each other in a workspace.

In this environment, the database query component takes data from the management DB and puts them into the workspace; the external data assimilation component takes external data not stored in the management DB, from outside the system and puts it into the workspace. These data are processed in the same way in the workspace by the various functional model components. The data that have been processed by one model component are transferred to another model component through the workspace. The order of processing is decided dynamically by a user.

The workspace is a reusable data area which depends on and is specific to the DSS, from the viewpoint of the DSS realization. The workspace is saved by a workspace save component as a small database for a specific purpose (such as private use or project use so that it can be reused later). Thus the user may create a “personal” planning DB for future use. When the user wishes to reuse the data, it is returned by workspace load component. Management of an individual planning DB is thus entrusted to an individual user or project.

![](/api/attachments/CK36J6V4/fulltext/images/018ded5310f4d413ccfd1c7c3187c574ddc30e2940170c482f4a3d13ab2f0140.jpg)  
Fig. 6. Realization of Planning DBs.

The characteristic of planning DBs is that individual planning DBs are connected loosely by the DSS to made an aggregate. Planning DBs can be interconnected with management DB through the use of the DSS database query component, and the management DB can be interconnected with operational DBs by the database linkage system. Therefore planning DBs are indirectly interconnected with operational DBs that reflect actual business activities, making it relatively easy to collect and distribute data.

## 3.3. Data Structure and Examples

People usually represent and understand data in the form of tables. Tables facilitate their understanding of a group of data by making it easy for them to compare data items. Tables are also very natural for data manipulation. Therefore, the form of table is appropriate to the basic data structure of the planning DB. The content of planning DB is created by incorporating cross sections of a data cube through the use of the database query component with additional external data provided through the external data assimilation component. These are produced in the workspace in the form of tables. Therefore, the workspace must function as a simple relational database.

The DSS1100 workspace stores a number of data groups in the form of tables. This is 'matrix data'; a column of this is called 'Vector data', - see Fig. 7. Vector data is then composed of scalar data. Operations are performed on vector data, because normally users perform arithmetic operations on columns rather than the entire table.

Matrix data becomes time-series or cross-section data, depending on the way of deriving the cross sections from the data cubes of the management DB, etc.

As an example, using the data cube of car sales management, a data element of the data cube in the management DB contains actual sales and planning data. In addition, a company's total monthly car sales plan is stored in the planning DB. A sales strategy matrix data can be created to answer the following question: "Is our company X likely achieve its goal of total number of cars said?" To do this, the user investigates sales for the Comet against the plan to date and then wishes to estimate sales of a competitive model of company Y.

Procedures for forming the sales strategy matrix data T are outlined in Fig. 8. Key words indicated by capital letters show DSS1100's functional model components that are used for the procedures.

Step 1: RETRIEVE

Data concerning monthly sales results of individual branches for the Comet is retrieved from the cross section A of the data cube in the management DB shown in Fig. 2. This matrix data M is saved in the workspace. M001 to M00m are vector data indicating individual branches' sales.

Step 2: LOAD

Data on X's monthly total sales plan for the Comet in the planning DB are loaded. It is saved as vector data T001.

![](/api/attachments/CK36J6V4/fulltext/images/870e64b39a560a4ee688fc78396b2ad0e76b106112c16e170066a1950085142e.jpg)  
Fig. 7. Matrix data in the planning DB.

![](/api/attachments/CK36J6V4/fulltext/images/a640991bcc822272a7958d2e483485cc455c9e92e1bef926c5d31b8ca11f9a88.jpg)  
Fig. 8. Matrix data manipulation in workspace.

## Step 3: CALCULATE

X's monthly total sales of the Comet are calculated by adding all branches' monthly sales (as stored in the matrix data M). The result is saved as vector data T002 (i.e., $\mathrm{T}002 = \mathrm{M}001 + \mathrm{M}002 + \ldots + \mathrm{M}00\mathrm{m}$ ).

Step 4: FORECAST

The monthly sales forecast is obtained by using vector data T002 to predict next year. The data obtained is saved as vector data T003.

## Step 5: INPUT

The monthly sales of company Y (with the product that is the biggest competitor of the Comet) is gathered (e.g., from periodicals) and input into the workspace. This is saved as vector data T004.

Step 6: FORECAST

Y's future sales is forecasted using vector data T004. The result is saved as vector data T005.

## Step 7: GRAPH

Sales plan (T001), actual sales (T002), and forecast sales (T003) of company X, and actual sales (T004) and forecasted sales (T005) of company Y are displayed as time-series graphs.

Step 8: SAVE

Vector data (T001 to T005) concerning car sales are stored in the planning DB as the sales strategy matrix data T. Matrix data M (X's sales result) can also be stored in another planning DB.

These planning DBs can be used by other users, as necessary. Users can also create their ‘decision support models’ by combining functional model components. (The significance of the decision support model is dealt with in our previous paper [1].)

## 4. Conclusion

We have shown how the two types of databases, management and planning, are essential for DSS. Their differences are presented in Table 1.

The management DB is organized/designed to allow easy use for managers: it is shared by many managers. It is created with data collected principally from operational DBs. It exhibits a three-dimensional data structure – a data cube – which can accurately describe the nature of the management information.

In contrast, planning DBs must act as personal databases. Managers, during the decision making process, sometimes find data from management

Table 1  
Characteristics of Management DB and Planning DB

<table><tr><td></td><td>Management DB</td><td>Planning DB</td></tr><tr><td>Type of use</td><td>Shared use</td><td>Personal use</td></tr><tr><td>Key purpose</td><td>Data retrieval</td><td>Data analysis</td></tr><tr><td>Data source</td><td>Operational DBs</td><td>Management DB and external data source</td></tr><tr><td>Data volume</td><td>Large</td><td>Small</td></tr><tr><td>Stored data</td><td>Aggregated</td><td>Processed</td></tr><tr><td>Logical structure</td><td>Cubic</td><td>Tabular</td></tr><tr><td>Nature of DB</td><td>Stable</td><td>Flexible</td></tr><tr><td>Builder of DB</td><td>Information Specialist</td><td>End user</td></tr></table>

DB insufficient. Although the major part of the data is provided from the management DB, the remaining part is formed by introducing data from outside the ssystem. Therefore, the DSS must be able to assimilate external data. The planning DB must have a two-dimensional data structure to allow managers to use it as easily as table.

Alter divides traditional DSS into two types: data-oriented and model-oriented [4]. The data-oriented DSS mainly concerns data retrieval. However, managers have failed to use the ample data stored in the DSS satisfactorily to cope with actual problems. This is because the DSS does not have an area where the data stored in the database can be processed effectively. Managers have done nothing more than observe relatively “unprocessed” data. DSS1100 has planning DBs, areas where the data stored in management DB can be processed and modified to cope with a specific problem, enabling managers to process and summarize data.

Though a major role of the model-oriented DSS is model building, managers are, in fact, occupied mostly with data collection and data management for their model: they are continuously obliged to operate their model on incomplete data. With our DSS architecture, data management is a unification of management DB and planning DBs, relieving managers of such task.

Incorporating the two features in one system, our DSS is a multi-purpose DSS with extensive functions, which neither a single data-oriented DSS nor a single model-oriented DSS can acquire.

In conclusion, both the management DB and planning DBs we propose can build a stable and effective information network and simultaneously, create an environment for the system that provide a flexible support to managers' individual decision making.

We think that a future information system will be based on a combination of “centralized” management DB and “distributed” planning DBs. It should improve an individual managers’ decision making ability and the performance of an organization.

## References

[1] T. Kosaka, and T. Hirouchi, “An effective architecture of decision support systems”, Information and Management, vol. 5, no. 1, 1982.

[2] J.F. Rockart, “Chief executives define their own data needs”, Harvard Business Review, March – April, 1979.

[3] J.F. Rockart, and M.E. Treacy, “The CEO goes on-line”, Harvard Business Review, January – February, 1982.

[4] S.L. Alter, “A taxonomy of decision support systems” Sloan Management Review, Fall, 1977.

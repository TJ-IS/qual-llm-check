---
otero_id: 18316
otero_key: "K4PSDPJ2"
title: "A DSS generator for district planning"
authors: "S.C. Bhatnagar; B.H. Jajoo"
year: "1987"
journal: "Information & Management"
doi: "10.1016/0378-7206(87)90029-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A dss Generator for District Planning

S.C. Bhatnagar and B.H. Jajoo

Indian Institute of Management, Vastrapur,

Ahmedabad 380 015, India

This paper describes the experience of the authors in designing a decision support system (DSS) for district planning. The iterative nature of the planning process, the need for flexible analysis of large volume of detailed data, the need for frequent interaction with the database, and the potential use of interactive graphics make the context ideal for design of a DSS. The evolution of a DSS Generator through several stages of software designs is highlighted. A proposal is then made for a DSS Generator which will add enough power to existing software that already provides the flexibility needed to cover many application domains in district planning.

Keywords: Decision Support Systems, DSS generators, Computer graphics, Locational planning, Development informatics.

![](/api/attachments/K4PSDPJ2/fulltext/images/9792be1c689e1d96937a3412234d5b8330136c23bb3d61306d38bd288a98227a.jpg)

S.C. Bhatnagar (41 years) holds a doctorate in Management. He is a Professor at IIMA where he heads a major UNDP sponsored research project on computer applications. His research interests are in developing MIS and DSS for enterprises and Public Systems. He has done consultancy in India and in many developing countries. He currently chairs working groups on computers in IFIP TC9 and Data for Development. Prof. Bhatnagar has published more than 30 articles

in journals, books and conference proceedings.  
![](/api/attachments/K4PSDPJ2/fulltext/images/c4037cd7091b9caf44fdd083d701042b0e9e9d012d4b0f5d4ef95a6e90ee3018.jpg)

B.H. Jajoo is an Associate Professor in Computers and Information Systems Group at Indian Institute of Management, Ahmedabad, India. He holds a Ph.D. degree in Computer Science from Indian Institute of Technology, Kanpur, India. His research has focused on Programming Environments, Programming Languages, Software Engineering, Decision Support Systems, Computer-aided Instruction, End-user Computing and Development Informatics. He has published several articles and presented invited papers in professional conferences. Prof. Jajoo is a member of IEEE Computer Society and a senior member of Computer Society of India, and the current Chairman of Computer Society of India, Ahmedabad Chapter.

## 1. District Planning

Planning in India operates within a five year framework. Each ministry of the Central Government and each State Government prepares a plan which is then dovetailed into the national five year plan. Within these, an annual plan is prepared to conform to the specified objectives and the given resource constraints.

The focal point of infrastructure planning is a district. A district has a population of about 1 million. A functionary from each of the key departments in which an infrastructure must be created is located in the district. The planning process is essentially sectoral, in which the budgetary allocations for each sector amongst different districts are made known to the district about 7 to 8 months in advance. The district level officers in consultation with elected representatives prepare a plan for new facilities to be created at specific villages. Such plans take into account the ongoing schemes and resources already committed. For choosing specific locations, village level data may sometimes have to be collected as the norms of choosing potential sites are quite detailed; e.g. a new school can be located in a village which has a population of at least 300 and has no other primary school within 2 km. Invariably, potential locations are more than the actual number to be created, because of the lack of resources. Ultimately, the elected representatives have the dominant say.

District level plans for each sector are passed upwards to the state level, where they are consolidated for all districts. The financial outlay of such proposals must be incorporated in the state budget, which is passed by the legislature before the beginning of the financial year. In the existing system, the above exercise of to-and-fro communications between the state headquarters and the districts in order to finalize the plan may take 7 to 8 months.

Two key decisions in this planning process are made quite arbitrarily, because information is not available to make these decisions rationally. The first major decision is a district-wise allocation of the total available budget for the department. The second important decision is in terms of making a specific location choice for a particular facility. Both these decisions work in favour of those districts with some political clout. Therefore, instead of creating equity, they tend to favour areas which are already well served.

The working group on district planning identified several pre-requisites for strengthened district planning $[6]$ . Foremost amongst these is the need to strengthen the methodology of planning at the district level. It emphasized the fact that thematic maps ought to be the instrument in developing area plans and that adequate data must be collected to portray the initial status of the area on thematic maps.

## 2. Why is a Decision Support System Needed for District Planning?

The type of detailed data that is required to support district planning and the nature of the flexible analysis that needs to be performed requires the development of a DSS for district planning.

## 2.1 The Nature of Data for Planning

In most planning tasks, the need to understand the existing resource and skill base in a village, taluka, or district is a pre-condition to designing suitable schemes. They require detailed and good quality data about the basic unit for which planning is being done. The basic unit may be a household in the case of an Integrated Rural Development Programme (designed to lift individuals above the poverty line), or a village for basic and social infrastructure, or a cluster of villages for some large production infrastructures. Not only should detailed data be available, but it should be presented as thematic maps if it is to be comprehended by planners, who will design schemes and specify locations for them. In a typical district there may be hundreds of villages and the number of households which may be below the poverty line may run into thousands. If the focus of planning is to be on such entities, data has to be collected and stored on computers so that ready access to the data is possible. In addition, access to data has to be provided across departments, if efforts of one department are not to be negated through non-availability of complementary services from other departments. Computers facilitate integration of data and its easy accessibility if the data can be structured appropriately.

## 2.2 Nature of Analysis

Planning at the district level has several actors: District Collector, Departmental Officers (owning allegiance to their parent department), and the elected representatives of the people. Even though structural changes may be contemplated, diverse interest will continue to be represented. Today, the finalised plan essentially represents the opinions of one of these parties, whichever happens to be strong in a particular district: this happens because there is no common basis for discussion that is data based, reflecting a true status of the district. The capability of computers to analyse data and aid in evaluating the end results of various (simulated) courses of action suggested by different actors would provide a common ground for discussing where trade-offs could be made and consensus developed.

Planning is a creative exercise of devising appropriate programmes and schemes to exploit the existing resources in a region. It requires flexible (exploratory) analysis of a large volume of detailed data. It requires tools which can present data in the form of maps and graphs so that the data is easily comprehensible to the various actors involved. The planning process is interactive, requiring re-analysis at each stage. Qualitative data and judgement of the decision makers play an important role in making choices where multiple objectives are involved. The need for interaction with the data and models is apparent. The context seems to be ideal for the use of a Decision Support System [5, p. 4].

These DSS need to be developed on inexpensive microcomputers which a district can afford. Since the annual expenditure on plan and non-plan schemes in a district runs into millions of rupees, the cost of a micro at about hundred thousand rupees is in no way prohibitive.

## 3. Past Experience of Developing DSS for District Planning

Recognizing the potential of computer graphics in a problem of locating service centres [2], we sought support from the Department of Electronics to develop an interactive graphic system for infrastructure planning at the district level.

## 3.1 An Early Version of DSS

In 1982, software was developed using Tetronics 40/12 storage tube graphics terminals connected to a PDP-11/70 host. It allowed planners to build a village-wise data bank on infrastructure availability for a district and provided interactive capability of analysing data to produce different types of maps [1]. Planners could use the software for plotting the locations of existing facilities and for understanding the dispersion of “Unserved” villages in the region. Unserved villages are defined as those villages which are beyond a specified distance from each type of facility being considered. The software allowed selection of a subset of villages in a region that met certain specified attributes. For example, potential locations for a primary health centre could include villages which already had a dispensary; did not have a primary health centre; were connected by road, had electricity and drinking water, and contained a population of at least five thousand. For a given budget, the new facilities could be chosen from all potential villages (fulfilling the above criteria), giving the ones that would serve the largest number of previously unserved villages. Data was collected from census books for the district of Kheda in Gujarat and the software was demonstrated to health department functionaries and to various other district level administrators attending training programmes at the Institute.

The software demonstration had a good effect. Almost everyone who saw it recognized its potential for planning infrastructure facilities for a region. The Gujarat Government considered active use of the software and set into motion a machinery to collect and integrate the basic data. However, it was recognized that such applications could be developed only if computers supporting graphic facilities were available within the state/district. In 1982, the availability of appropriate hardware appeared to be an overriding constraint. Today, several microcomputers offer reasonable graphic facilities.

## 3.2 A More Generalised DSS

Our own interaction with the software revealed several design changes that could have been made. A second version was created with vastly improved interaction capabilities. It was more general in terms of its data structures and had a command language structure to simplify interaction. The commands allowed selection of villages from a table on the basis of their attributes, like the existence of a particular type of facility or the distance from it. Other sets of commands display a set of villages on a map, allow interaction with the displayed map, and produce a printed report on the selected villages. The software was table driven, offering the flexibility of carrying out various types of analysis by using the commands in an appropriate sequences. It offered the facility of superimposing the output of several analyses on the same map. At any stage of analysis the planner could revert to analysing the entire set of data. Table 1 shows the commands.

To test the value of this software, a Workshop was organised in collaboration with the Government of Rajasthan [3]. Data was collected from Udaipur district consisting of 3,167 villages from various departmental functionaries like health, education, public health engineering department, and PWD. Officers from these departments and a few from the state level were invited for a two-day Workshop to interact with the software and prepare their annual plan for 1983–84 in terms of specifying locations of new facilities. Fig. 1 illustrates a typical lesson with the software, in which the user has plotted all villages that are out of reach of health facilities. District level officers took to computers easily, disproving the myth that such technology will scare non-computer people; the participants worked extensively on the software and with great enthusiasm. The following important potential benefits were identified:

<table><tr><td colspan="2">Table 1Basic commands</td></tr><tr><td>Commands</td><td>Description</td></tr><tr><td>BOUNDARY</td><td>Draws the boundary of the district</td></tr><tr><td>CLEAN</td><td>Clears the screen</td></tr><tr><td>DISPLAY</td><td>Displays the geographical location of chosen villages</td></tr><tr><td>EXIT</td><td>Terminates the session on the terminal</td></tr><tr><td>HELP</td><td>Explains the purpose of each command</td></tr><tr><td>INITIALIZE</td><td>Reverts further analysis to the original set of villages</td></tr><tr><td>LOCATE</td><td>Locates a specified facility at each of the currently chosen set of villages</td></tr><tr><td>OPTIMIZE</td><td>Provides a menu of commands for optimal locations of a specified facility</td></tr><tr><td>QUERY</td><td>Chooses a set of villages satisfying criteria by the user</td></tr><tr><td>SELECT</td><td>Chooses a set of villages specified by their geographical location through a cursor</td></tr><tr><td>TABULATE</td><td>Prints tables for chosen set of villages on specified attributes</td></tr></table>

1. The software, with its output of thematic maps, provides a kind of understanding (particularly of unserved villages) which was much beyond what district level officers could normally determine, though they were in constant touch with the field.

2. It provides integration across departments. For example, public health department officers could not only identify villages that needed tubewells but also determine which of them had the road connections to carry heavy machinery to the boring sites.

3. It enhances the quality of decisions regarding location or upgrading of new facilities and would cut down the time taken by districts to prepare such plans manually. It could provide a common basis around which an administrator and elected representatives could converge to an acceptable solution.

4. The integrated data offered an easy tool to determine relative allocations amongst departments on the basis of existing status of facilities in the district rather than on the basis of a national norm. Disparities amongst various regions could then be resolved and relative allocations amongst different types of infrastructure facilities traded off with one another.

![](/api/attachments/K4PSDPJ2/fulltext/images/bec28f71020386af1fd4efaa335d5349ffe49d72497c1b5dd85d56aea46f7b98.jpg)  
Note: The figure is indicative and not an exact replica of the screen image  
Fig. 1. A typical session with DSS software.

5. It could provide accurate assessment of a district's "backwardness indicator", which is often used for allocating funds for each district.

## 4. Move towards a DSS Generator

Enthused by the reaction of workshop participants we began to look forward to actual field implementation of the software. We were also able to demonstrate the use of the software in other contexts. For example, in the design of an MIS for a programme to control prices of essential commodities, we were able to use the software for analysing time-series data on prices of 10 commodities collected from about 70 centres in India, and to present the output graphically by displaying cities which had unusually high price variations. Similarly, we are using the software for Chuk (a group of farms) level analysis of command area in a canal irrigation project. We are also working with data from a district in Karnataka in which the software is being used to analyse villages and beneficiaries covered under a rural development programme. From some of these exercises, we have discovered the need to provide additional capability in the software. For example, we have added commands which allow computation on a column, creation of new columns, and enable the operations of software on two tables within a session. A need to enhance the graphics capability has also been felt.

## 5. Design of a DSS Generator

The second version of software offered a great deal of flexibility in terms of analysis, prompting us to use the software in other application domains. However, in each such trial, we felt the need to enhance its power. It contained the kernel of a DSS Generator [4] in terms of a table driven query and retrieval software integrated with spatial graphics. We are in process of adding and revising modules to enhance its power, to make it a complete DSS Generator for district planning (see Fig. 2).

## 5.1 The Database

In terms of the database, the requirement at a district level is to be able to create, update, and retrieve data on several entities. For example, data would be needed on villages, households, beneficiaries of different programmes, schools, teachers, fair-price shops, roads and development schemes. Data elements from these several entities would be independently retrieved but it would also be necessary to build relationships amongst a maximum of 3 to 4 entities for each application. For example, for rural development programmes, it would be important to relate data on clients, villages, and households. In an application for education, data on schools, teachers, and villages may be related.

If our software could provide the ability to model an hierarchy amongst entities, allow selective retrieval of member data for each owner entity, and offer an ability to aggregate and sort such data, it would provide the planners enough flexibility to perform varied analysis.

## 5.2 Graphics

The second important aspect is in terms of data presentation. In addition to the usual tabular presentation of any analysis, the output should be provided on a map. The ability to define various kinds of maps, in which boundaries and other fixed information can be displayed (in addition to locations of villages, roads, etc.), was provided by the earlier version. Such a presentation should also include the capability of drawing maps which display statistical information. For example, it should be possible to display locations through symbols which represent a particular attribute of the village and perhaps the size and shape of the symbol should represent a quantitative measure of the attribute. It should also be possible to present such data as maps in which averages are displayed for regions in terms of clusters of villages, talukas, or districts. For example, average yield for a crop for different talukas could be displayed by using various forms of shading. The capability of drawing graphs, bar charts, and pie charts could also be provided in terms of presentation of data contained in a relation. It should also be possible to print or plot such output through a command.

## 5.3 Textual Data

In addition to a database which would essentially consist of quantitative data on different attributes, there would be a strong need for textual data to be associated with relations and entities. There are, for example, reports of field visits to households and beneficiary which are qualitative in nature. Such observations from the field on village or taluka would be equally important to consider when schemes are being designed. It should be possible to retrieve and manipulate such textual data for any entity.

![](/api/attachments/K4PSDPJ2/fulltext/images/abc135c576baa966d25ac916369272bde82c2b54cde859c15040c27a863c2919.jpg)  
Fig. 2. Software structure of a DSS generator.

## 5.4 Data Analysis & Models

Simple functions could be available to compute average, standard deviation, maximum or minimum for any given attribute in a relation. Functions should be available to sort a relation on a given attribute or combination of attributes. Models which could be important in terms of district planning are algorithms for location and allocation, and determining shortest path on a road network.

In terms of dialogue, the most important consideration is that of user-friendliness. A menu-driven software with extensive HELP support and prompts would be required to facilitate use of such complex software by non-computer professionals. It is our opinion that the ability of district level officers to work with computer is most often underrated. With user-friendly software, one to two days of intensive training should be sufficient to enable a non-computer professional to use the software.

## 6. Overall Architecture

Many of the enhancements of the proposed DSS system have been implemented. The software is driven by tables which capture the description of different entities and attributes that characterize the district level data. Its internal architecture has been designed in a manner which allows addition of modules to enhance the power of the DSS Generator, or to add to the capabilities of the individual modules.

Our experience of developing a DSS Generator has underscored the evolutionary nature of the development and the importance of modular architecture. The software is currently being implemented in a district of Gujarat. The power of the software appears to be more than adequate, but the user-interface has been modified to minimize the typing requirement. Motivation to use the software is primarily because of the graphics.

## References

[1] S.C. Bhatnagar: Interactive Graphics Software for District Planning, Research Report, IIM, Ahmedabad, April 1982.

[2] S.C. Bhatnagar: “On Locating Social Service Centres Using Interactive Graphics”, OMEGA, Vol. II, No. 2, 1983.

[3] S.C. Bhatnagar, B.H. Jajoo and I. Khanna: “Computers in Infrastructure Planning: a Field Study”, CISG Research Report, IIM, Ahmedabad, June 1984.

[4] K.B.C. Saxena and M. Kaul: "A Conceptual Architecture for DSS Generators". Information and Management, Vol. 10, No. 3, March 1986, pp. 149–157.

[5] R.H. Sprague and E.D. Carlson: Building Effective Decision Support Systems. Prentice-Hall, Englewood Cliffs, N.J., 1982.

[6] Report of the working group on District Planning, Vol-I, Government of India, Planning Commission, May 1984.

---
otero_id: 21848
otero_key: "QQ74VZHS"
title: "Management issues in data warehousing: insights from the Housing and Development Board"
authors: "James Ang; Thompson S.H Teo"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00085-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Management issues in data warehousing: insights from the Housing and Development Board

James Ang, Thompson S.H. Teo )

Department of Decision Sciences, Faculty of Business Administration, National UniÕersity of Singapore, 10 Kent Ridge Crescent, Singapore 119260, Singapor

Accepted 6 December 1999

## Abstract

Data warehousing has emerged as one of the most powerful tools in delivering information to users. In this paper, we examine data warehousing at the Housing and Development Board HDB , which is responsible for providing affordable,Ž . high-quality public housing to Singapore citizens. The HDB embarked on building a data warehouse because access to the diverse and large amount of data in its operational systems, was becoming increasingly cumbersome and time consuming. By building a data warehouse, the HDB aims to facilitate users’ access to corporate information for planning and decision making. The experiences and lessons learned from building a data warehouse at HDB are discussed. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: Data warehouse; Lessons; Singapore; HDB

## 1. Introduction

Over the years, firms have accumulated a large volume of data that potentially contain valuable information about their business. These data, which are stored in operational databases, are not easily accessible to decision makers due to most firms’ existing information technology IT infrastructure. Further,Ž .

these operational databases are likely to be geograph ically or logically dispersed, thereby making it difficult and inconvenient to access.

Traditionally, the information systems IS depart- Ž . ments are the sole interface to firms’ data stored in computer systems. Executives from various departments rely on the IS department to satisfy their needs for information that is necessary for decision making. The turnaround time is usually long and information is often not delivered on time to users, which in turn reduces the value of the information. Further, reports produced by the IS departments usually provide a one-dimensional rather than multidimen-Ž sional view of the data. For example, sales can be. broken up into geographical districts, regions and countries. It can also be presented by product lines rather than by geographical dimensions. Executives will require different reports showing information in various dimensions e.g., by product lines or byŽ region . Further, the ability to change dimensions. and drill down enables more effective data analysis and decision making.

However, since senior executives tend to ask for whatever they need, it is usually time consuming for the IS departments to deliver different reports customized to different executives. Consequently, only a subset of reports may be delivered on time. Even if the reports are delivered on time, it may not be exactly what the executive wants due to miscommunication or lack of clarity in specifying the information he<sup>r</sup>she needs. Further, on receiving the reports, the executive may discover that he<sup>r</sup>she needs further detailed information, which in turn may require more time for the IS department to provide. Even if further information is not needed, the executive may still need to seek clarification from the IS department regarding various aspects of the information provided. This is likely to result in further delay, thereby hindering timely and effective decision making.

The situation would have been different if the company had implemented data warehouse technology, which has emerged as one of the most powerful tools to solve the problem of access to information for decision makers. Basically, this technology enables information to be easily accessed by staff members for decision making, without much reliance on the IS departments. With the appropriate userfriendly query tools, staff members can experiment with different views of the data, thereby enabling him<sup>r</sup>her to understand the situation and make better decisions. Further, if necessary, staff members can drill down to obtain more detailed data about certain areas. This ability to change views and drill down greatly enhances the value of a data warehouse for decision making since detailed data can be readily accessed, whenever required.

Past research has often focused on the technology required to establish and support data warehouses <sup>w</sup> <sup>x</sup> 2,5,18 . Previous work has also provided both technical 5,20,21 and non-technical prescriptions 10,19 <sup>w</sup> <sup>x</sup> <sup>w x</sup> for building and implementing data warehouses. The factors affecting data warehouse implementation 14 ,<sup>w</sup> <sup>x</sup> warehouse issues 1,4,6,17 , as well as the pitfalls of <sup>w</sup> <sup>x</sup> data warehouse development 11,22 have also been<sup>w</sup> <sup>x</sup> investigated. In addition, comparative cases of data warehousing 13 and businesses, which successfully<sup>w</sup> <sup>x</sup> deploy data warehouse, are often described, e.g., Mastercard International 12 , Wal-Mart Stores 11 ,<sup>w x</sup> <sup>w x</sup> Cable Vision Systems, Victoria Secrets and Mercantile Stores 9 .<sup>w</sup> <sup>x</sup>

Relatively less research has been done on data warehousing projects in the public sectors such as statutory boards and government agencies, which are likely to have large repositories of data. Further, most researches have focused on companies in America or Europe rather than Asia. Hence, this research examines the development of a data warehouse by the Housing and Development Board Ž . HDB , a statutory board in Singapore. Data were gathered through interviews with the relevant persons in HDB as well as through historical records. The impact of the data warehouse and the management issues in data warehousing are examined. NoteŽ that we have a close working relationship with Mr. Alex Siow, although we did not take part in the data warehouse project. Mr. Siow and his IS staff kindly allowed us to interview the relevant personnel and view pertinent non-sensitive materials. This paper was based on the interviews and the materials provided..

## 2. Background of HDB

The HDB in Singapore is a statutory board whose main mission is to provide affordable high-quality homes for citizens. The HDB plans the towns comprehensively, ensuring that the towns are supported by commercial, sports and recreational facilities. In doing so, the HDB also helps to build cohesive multiracial communities among the population of Singapore.

The Singapore Government developed a vision in the early 1960s, brought together key people, and scraped together enough funds to launch the public housing program. Formed in 1960, the HDB has so far built 800,000 flats apartments , 20,000 commer- Ž . cial properties, 12,000 industrial properties and many other communal facilities. It has been experiencing an extended period of sustained growth, reflecting its successful efforts to fulfil its mission. In fact, when the public housing program was launched in 1960, only 9% of Singapore’s population lived in public housing and many others lived in overcrowded and unsanitary conditions. Currently, 86% of the population lives in HDB homes that are built to high-quality standards with convenient amenities such as food and shopping centers, schools, and community centers nearby.

The task that the HDB faced was daunting. It had to forecast the number of three-, four-, and five-room apartments, executive flats apartments , car parkingŽ . lots, and commercial complexes to be built. It also had to work out different rental schemes for those who could not afford to purchase their flats. For every precinct, it had to determine the number of car park lots and commercial facilities needed. It was, therefore, not a straightforward build-and-build task. Much planning had to be done. What were the development constraints? How much land had to be cleared and freed for public housing development? How could the rising expectations of Singaporeans be managed? The HDB realized that it had to introduce continually fresh and innovative ideas in landuse planning and housing designs to meet the rising aspirations of Singaporeans for better-quality homes. To support the HDB in its mission, a substantial amount of data had to be collected, distinct operational systems set up each geared to specific needs ,Ž . and interfacing mechanisms developed so that the systems would not operate as pockets of automation.

Besides its list of responsibilities, it now undertakes an Estate Renewal Strategy which includes Upgrading Program, Selective En-Block Redevelopment Scheme SERS and other improvement pro- Ž . grams for the older HDB towns. This is to ensure that all HDB estates provide an aesthetically pleasing environment, with the necessary amenities for its residents. This means upgrading the older estates to turn them into modern and thriving towns comparable to the newer ones. ‘‘With Singapore’s land scarcity problem an ever present challenge, HDB must develop more efficient and integrated towns and upgrade its mature estates to maximize land use and yield’’ 15 . Today, the HDB functions as a<sup>w</sup> <sup>x</sup> well-oiled holistic organization so much so that regional governments are seeking its assistance to house their people. For example, the HDB is currently helping China to plan and build a new town In-Ž tegrated Housing Community in Shanghai. Due to. the success of the HDB in providing housing for citizens coupled with various government schemes to encourage home ownership, Singapore has the highest percentage of people in the world who own their homes.

## 3. Using IS at the HDB

Given the HDB’s objective of providing high-quality, affordable public housing for citizens, it had to rely on IS not only to handle the routine, structured activities such as the sales and rental of flats and complexes, but also strategic activities such as forecasting the number of three-, four-, and five-room apartments, executive flats, car parks, and commercial complexes to be built.

The HDB is supported by 120 operational systems, each with its own database. These systems helped the HDB manage the links in sales and rental of flats and complexes, mortgage schemes, and the continual streamlining of the HDB application procedures. Over the years, the HDB has accumulated a large volume of data that potentially contain valuable information about various aspects of its business. These data are not easily accessible to the relevant users in the HDB due to its existing database setup. Hence, it was increasingly difficult to generate timely management and status reports because one had to access several databases to piece things together. Moreover, individual departments zealously guarded their control over their respective databases.

The HDB’s challenge was in dealing with all the disparate data and the changing exogenous factors Že.g., public demand for flats, shifting population trends , and be able to put them together in a coher- . ent report as and when needed by top management for planning and decision making. For example, users should be able to extract resident information and correlate that with geographical IS to generate reports that would be extremely useful to town planners. But with 120 application systems, the situation was sufficiently complex that its Chief Information Officer CIO , Alex Siow, did not know of any Ž . off-the-shelf tools that could make things easier.

Most software products look exciting and good with simple data, but the HDB had huge databases.

A data warehouse is a repository of summarized data current as well as historical assembled in aŽ . simplified format tailored for easy end-user access. These data are culled from existing operational systems and are structured for analysis and decision making. Closely linked to the data warehouse is a set of meta-data providing information e.g., the opera-Ž tional systems from which data are extracted, the transformation logic, owner of the data, reliability, and frequency of update . At the HDB, Lotus Notes . was used to develop the meta-data.

Developing a data warehouse is not a simple, straightforward matter of data field conversion or mapping because the conversion of one field may depend on the value of another field or may depend on the value of the same field in another record. Data have to be cleansed, and transformed using a common transformation logic. Custom programs have to be written and business rules have to be rationalized to ensure consistencies. The ‘‘clean’’ data are then stored in the data warehouse together with meta-data. Access to the data warehouse is made available through various end-user data retrieval tools such as QMF, SAS<sup>r</sup>DB2 and Lotus Notes. The components and steps for building a data warehouse are shown in Fig. 1.

Moreover, a data warehouse requires detailed planning involving internal operational procedures and workflow reconfiguration, and the IS staff, with their sufficiently detailed knowledge of the HDB’s modus operandi, were in a better position to win the continuing support of the end-users than a team of outside IS consultants<sup>r</sup>vendors. Outside consultants<sup>r</sup>vendors may not share the same goals and commitment as the IS staff. Consequently, the Information Services Department under Alex Siow decided to develop and maintain a customized data warehouse. The objective was to build a scalable data warehouse because scalability is a critical component in ensuring that the data warehouse is able to evolve with changing needs and expectations. Alex Siow wanted to develop a data warehouse that was business-driven, involved top management, and userled. He and his senior IS staff used the conventional Systems Development Life Cycle SDLC approach. Ž . As the SDLC approach is geared more for operational systems rather than data warehouses, Alex Siow and his team had to modify the approach to reflect the different requirement study, data modelling and the design of the system functional processes.

In just 4 years, the HDB data warehouse, called the Information Center Database ICDB , has grownŽ . from a proof-of-the-concept warehouse to the current

![](/api/attachments/QQ74VZHS/fulltext/images/897c9ee82e7b6f7491612ca9e339917e95dd4dfa46bafd3288c590f4428e758f.jpg)  
Fig. 1. Components of a data warehouse.

IBM’s mainframe DBMS DB2, consisting of 3 GB of data.

Alex Siow, CIO at the HDB, defines the ICDB data warehouse as follows:

It is a repository of data summarized or aggregated in simplified form from operational systems. Enduser oriented data access and reporting tools let users get the data for decision support. Also, a data warehouse is informational, not operational. It is analysis- and decision-support-oriented, not transaction-processing-oriented. It is usually client<sup>r</sup> server, and not legacy- or host-based 8, p. 16 .

Treating data as a corporate resource meant that the data warehouse should be a repository for corporate information, and in any thriving enterprise, data never stop growing. The model that guided the data warehouse was based on subject rather than project orientation. A data warehouse that is subject-oriented, integrated, time-variant, and non-volatile is more appropriate for supporting the management decision making process 16 see Table 1 . The data<sup>w</sup> <sup>x</sup> Ž . warehousing project was conceptualized late 1993 with the objective of facilitating end-users’ access to accurate and consistent information needed for planning and decision making. Development efforts got under way in June 1994, and the data warehouse was implemented in August 1995. Now, all user groups can access the same timely, consistent, and accurate data to ensure that high-quality decisions are made.

Table 1  
Characteristics of data

<table><tr><td>Subject-oriented</td><td>Data are grouped by subjects. For example, data on customers are grouped and stored as an interrelated set.</td></tr><tr><td>Integrated</td><td>Data are stored in a globally consistent format. This implies cleansing the data so that data have consistent naming conventions and physical attributes.</td></tr><tr><td>Time-variant</td><td>Data captured are for long-term use (often 5–10 years), so they are captured in a series of snap shots.</td></tr><tr><td>Non-volatile</td><td>Once data at a particular time, say  $t_1$ , are captured and stored, their attributes are preserved.</td></tr></table>

## 4. Impact of data warehouse

The key impacts of the data warehouse developed by the HDB are the following.

## 4.1. Easy access to consistent and reliable data

The data warehouse enables users to have access to consistent and reliable data in a timely fashion. About 90% of users uses pre-canned queries and reports while the remaining 10% often codes new queries. This has facilitated forecasting and planning efforts and improved decision making. For example, managers are now able to obtain the necessary reports from their staff in, say, 1 day instead of 3 days. This has enabled them to be more responsive to changing environmental conditions.

Furthermore, the data warehouse brings out information that was previously hidden or that would require the cumbersome process of accessing different operational databases to obtain it. For example, the data warehouse enables users to extract resident information and correlate with the geographical IS in order to analyze demographic profiles at various HDB estates. This enables better decisions to be made pertaining to the types of shops you need to set up there, location of MRT lines, etc.

## 4.2. Create new demands for new types of data

When users become proficient in accessing the data warehouse, they realize that some types of data are not available and they may have to obtain them from operational systems. Hence, there is a need for the data warehouse to be constantly upgraded and improved based on users’ feedback on new types of data that should be included. However, it is important that users understand the differences between operational and decision-support data as the aim of a data warehouse is not to store all the data available, but to selectively store those data that are essential for planning and decision making. Hence, all requests for additional data to be included in the data warehouse are formally evaluated and discussed with the relevant user departments.

## 4.3. Stabilize requests for ad hoc reports

Although requests for IS reports may decrease as the result of users being able to obtain results of pre-canned queries directly, requests for IS reports may also increase as users demand more customized information. As a result, there may be an overall increase in the quantity of reports generated. Whether or not this is desirable is debatable. If the additional reports are helpful in facilitating better planning and decision making, then it is desirable. On the other hand, having more reports may actually slow down planning and decision making since more time is spent on analyzing them.

A significant benefit of the data warehouse to Alex Siow is that it helped to stabilize the increase in the number of ad hoc requests from user departments since users can now generate many of the ad hoc reports themselves. This has helped Alex focus his attention on managing about 120 existing applications and about 20 new application development projects per year.

## 5. Management issues in data warehouse

This section discusses the important management issues pertaining to the HDB’s efforts in the data warehousing project. These issues provide important considerations for project teams working on data warehousing and help them to avoid costly pitfalls.

5.1. Management issue no. 1 — identifying the processes

Implementing a system is a major event and is likely to cause organizational perturbations. This is even more so in the case of developing a data warehouse. How then did the HDB go about developing its data warehouse? It went back to the basics and identified the business processes that the data warehouse was built to support. Each step in the process was examined in detail. Organizational rules to rationalize inconsistencies had to be established. If the processes had to be reengineered, they were reengineered. Reengineering worked to establish a stable and streamlined operating environment. All processes were examined to make sure that they would reap benefits from the proposed data warehouse.

Problems associated with processes cannot be solved just by concentrating on the data themselves or by running the data through a new and better system. If the problems are not fixed, they come with you to the new system. If external data are needed, then such data have to be captured in the data warehouse.

## 5.2. Management issue no. 2 — choosing deÕelopment options

Often, one is baffled by the wide range of software options. It is very tempting to go along with a vendor who packages his software with quick-fix and easy-to-maintain solutions e.g., Information Ž Builders’ SmartMart and SAS Institute’s SAS Warehouse Administrator . But there are just no simple . and easy solutions. Data from the existing operational systems existed in multiple formats. These had to be cleansed, transformed, and standardized for end-user access. All similar data of different formats have to be redefined to a single format or through use of a single line set of codes. By developing the data warehouse in-house, the IS staff started with a framework that was acceptable and comprehensible to the user departments. That was a significant first step since it led to the development of an enterprise model which guided the data warehousing effort.

Clean data are an important determinant of the efficiency and effectiveness of a data warehouse. This is expected because clean data with character-Ž istics of data consistency, integrity and accuracy. affect the quality of management reports generated, which, in turn, affects the quality of the decisions made. All these tend to raise the users’ level of confidence in and acceptance of the data warehouse. Unless the data warehouse is perceived to be credible, users will hesitate to exploit its full potential. ‘‘Our in-house effort paid off, though with some difficulty. We managed to get users to discuss such issues as ownership of data and frequency of update candidly. I do not think we would be able to achieve what we wanted if we had just bought any off-theshelf products. Our situation was so complex that we did not know of any off-the-shelf-tool that could make our job easier,’’ said the Head of Database Development Unit.

No outside consultants were involved. In MRP II research, more failures were reported in cases where outside consultants were used 7 . Consultants often <sup>w</sup> <sup>x</sup> assume technical leadership, but more important than that is a deep understanding of the users’ needs and expectations. Often, we come across stories of software vendors advising clients to install all the features their software provides. But more importantly, we have to ask ourselves if that sort of take-all attitude is helpful in moving the company ahead. ‘‘Software loaded with so many features can lead you astray’’ 3 . In this case, the IS staff, working <sup>w</sup> <sup>x</sup> with the users, had a unique opportunity to understand them, their needs, their apprehensions, and their expectations, and to encapsulate these in the system. The resulting system was much more useful.

## 5.3. Management issue no. 3 — adopting incremental change approach

An examination of the data warehouse development process revealed an incremental development approach coupled with an overall architecture to ensure that components of the data warehouse would be integrated. A data warehouse is a complex undertaking. A data warehouse is, in fact, always sitting on existing operational systems, getting its cleansed and transformed data from these systems. If one of these systems from which data are drawn changes, the bridge program has to be updated speedily. Organizations that do not have the necessary integration of warehouse management tools find themselves racked with headaches over maintenance issues. Warehouse maintenance can be a costly process.

It is therefore advisable to start small and focused. Large-scale change efforts are fraught with risks because too many variables have to be managed, and the odds of successfully implementing the project are small. On the other hand, small, highly focused warehouse development projects can demonstrate technical considerations and prove that the data warehouse is feasible and productive for the organization. Other benefits of this incremental approach include:

1. contained risk since smaller projects are moreŽ manageable and less risky ;.

2. opportunity to learn by doing since both users Ž and IT staff can concentrate on important issues ;.

3. frequent delivery since benefits can be obtainedŽ earlier ; and.

4. minimized disruption to existing operational systems since development is carried out in phases .Ž .

## 5.4. Management issue no. 4 — oÕercoming resistance

It is important to make the users part of the development effort, even though the data warehousing project already had very staunch top management support. At each stage, user involvement is crucial because the more involved they are, the deeper their understanding will be regarding the issues and the obstacles encountered in the developmental process. They will understand the limitations and capabilities of the data warehouse and, in the process, be able to provide valuable input into future enhancements. Users who are part of the team will be more patient and proactive in helping to exploit the technology put in place. The users and the IS staff should be viewed as members of an ongoing team and as partners with a common objective of creating a useful and reliable data warehouse.

The data warehousing project provided the IS staff with an intimate insight into the fears and apprehensions of end-users on this issue. There was an immense reluctance on the part of individual departments to share data. Over the years, individual departments, each taking charge of their operational systems, had come to regard certain data classes as theirs to collect, store, and maintain. Although they were told that they would be able to use the data warehouse to access timely, consistent, and accurate information to ensure that decisions of the highest quality would be made, resistance still persisted.

That is understandable. People just do not like to share data. Usually, the user department owns both the system and its data.

The HDB staff had to devise a mechanism of dual ownership in which the CIO owns the data warehouse architecture, and the respective user departments own the data in it. Access to the data warehouse would be granted to the various users only if the data owner authorizes it. The authorization list is reviewed annually, and individual departments are then at liberty to add or delete users to the list.

Since the data warehousing project started in 1994, Alex Siow has been actively promoting the spirit of cooperative learning and doing among the various departments. Departments are now more willing to share data, because over time, they have learned that the data actually belong to the HDB. Their all-important role is to capture, preserve and store them so that relevant parties could access and use them for the common good of the HDB.

## 5.5. Management issue no. 5 — choosing project leader

In addition to getting a good combination of people in the project team, getting the right person to lead the data warehousing effort is crucial for its success. The project leader must not only be technically competent, but should have adequate business knowledge as well as good interpersonal skills. This is because people issues which deal with conflict Ž and politics are often more difficult to resolve than. technical issues which deal with problems that can Ž be solved by technical solutions . In fact, the Head . of the Database Development Unit commented that ‘‘technical issues are within our control. It is getting different user groups to agree on how different data should be defined that is difficult. Hence, it is very important that the project leader has good interpersonal skills.’’

Previous literature has emphasized the importance of a project leader who is able to motivate the team to channel their energies to achieve the project objectives. This is because a data warehousing project can be viewed as introducing change in the organization. As such, some parties may benefit or lose power as the result of the change. A good project leader would be able to explain and convince the necessary parties of the need for change as well as mediate between various parties if disputes or disagreement arises. Consequently, interpersonal skills and willingness to listen to users’ concerns are essential prerequisites of a good project leader and may determine the cohesion and cooperation of members of the project team.

## 5.6. Management issue no. 6 — proÕiding formal, systematic training

Developing a data warehouse is a difficult endeavor, but realizing significant benefits is much more difficult. As such, users must undergo continual, formal, systematic training to get the most from the data warehouse. In the case of the HDB, for instance, the Head of Database Development Unit said, ‘‘Besides putting in many hours of formal training, we also follow up with regular ‘hand-holding’ sessions to help users to take full advantage of the data warehouse.’’ Two factors underlie the need for user training: 1 the users have a better under-Ž . standing of the functions that the data warehouse will support; and 2 they will be accountable for Ž . making the data warehouse produce timely and accurate information. Technical system quality is important, but just as important, if not more so, is the need to understand the human issues in technical change. A formal, systematic training program helps to raise user awareness vis a vis the possibilities and limita-\` tions of the data warehouse. ‘‘At the HDB, we treat training costs as investments, not costs. Viewed it from the investment perspective, management is more than willing to release training resources,’’ said Alex Siow.

At the HDB, training is every bit as critical a path from data warehouse project perspective as having the warehouse firmly in place. Management realized this and funded the best training process possible.

## 5.7. Management issue no. 7 — scalability and data warehouse maintenance

The HDB operates in a changing environment. Rules and procedures are rendered obsolete and new ones implemented. There is no end in the data warehousing process in that new capabilities and functionalities are continually added. Data warehouses grow from datamarts to mega-datamarts to big data warehouses. The IS staff wanted the system to be ‘‘flexible’’ so that they could customize the configuration or scale up when the need arises, and they were proven right. Data grow faster than one thinks, and they never stop growing. As of May 1996, the HDB had some 5.5 million records 8 and<sup>w</sup> <sup>x</sup> is expected to continue to grow.

A related issue is data warehousing maintenance, which can be a costly exercise as data increase in volume. Although the data warehouse is not timecritical for the HDB, it is nevertheless critical. Sustained commitment to excellence in warehousing maintenance is achieved at the HDB with the development of an in-house data warehousing expertise. Alex Siow did not use outside experts. For the HDB, data warehousing capability, both in development and maintenance, is essential for the HDB has to respond to rapid organizational changes and shifting external demand. As information about the HDB changes and that is very frequent , so too must theŽ . data warehouse, adding new capabilities. Moreover, a scalable data warehouse is a never-ending journey.

## 6. Concluding remarks

The data warehousing project is one of the many successful projects undertaken by the Information Services Department at the HDB. In November 1995, as the result of the success of numerous IT projects, the Information Services Department received the ISO 9001 Certification for Analysis, Design, Development, Implementation and Support of In-house Information Systems. In 1996, HDB’s CIO, Alex Siow, was rated by Computerworld as one of the top 10 most influential IT personnels in Singapore and the HDB was bestowed the National IT award for the public sector and the National IT Training award. These awards give due recognition to HDB’s leadership and innovative use of IT. For example, the HDB was among the first government agencies to successfully develop a data warehouse. It serves as a role model for other government agencies to emulate. Indeed, many other government agencies have embarked on similar data warehousing projects in order to enhance users access to pertinent information that will result in an efficient and effective civil service. Overall, this will make Singapore more competitive as well as an ideal place for foreign multinational corporations to locate their operational or regional headquarters.

## References

<sup>w</sup> <sup>x</sup> 1 N. Alur, Missing links in data warehousing, Database Programming and Design 1995 21–23, September.Ž .

<sup>w</sup> <sup>x</sup> 2 E. Appleton, The right server for your data warehouse, Datamation 41 5 1995 56–58, March.Ž . Ž .

<sup>w</sup> <sup>x</sup> 3 E.L. Appleton, How to survive ERP, Datamation 1997Ž . 50–53, March.

<sup>w</sup> <sup>x</sup> 4 S. Atre, Rules for data cleansing, Computerworld 1998 Ž . 69–72, March 8.

<sup>w</sup> <sup>x</sup> 5 D.P. Ballou, G.K. Tayi, Enhancing data quality in data warehouse environments, Communications of the ACM 42 Ž . Ž . 1 1999 73–78.

<sup>w</sup> <sup>x</sup> 6 J. Bischoff, Achieving warehouse success, Database Programming and Design 1994 27–33, July. Ž .

<sup>w</sup> <sup>x</sup> 7 O.M. Burns, D. Turnipseed, W.E. Riggs, Critical success factors in manufacturing resource planning implementation, International Journal of Operations and Production Management 11 4 1991 5–19.Ž . Ž .

<sup>w</sup> <sup>x</sup> 8 Computerworld, Round Table — Data Warehousing, May 31–June 6, 1996, pp. 14–21.

<sup>w</sup> <sup>x</sup> <sup>)</sup> 9 G. Conlon, What the !@a! !! is a data warehouse, Sales and Marketing Management 149 4 1997 40–48.Ž . Ž .

<sup>w</sup> <sup>x</sup> 10 S. Deck, Data warehouses: plan well, start small, Computerworld 1998 9, August 3.Ž .

<sup>w</sup> <sup>x</sup>11 J. Foley, Data warehouse pitfalls, Informationweek 1997Ž . 93–96, May 19.

<sup>w</sup> <sup>x</sup> 12 E. Freeman, Birth of a terabyte data warehouse, Datamation 43 4 1997 80–84, April.Ž . Ž .

<sup>w</sup> <sup>x</sup> 13 R.K. Griffin, Data warehousing, Cornell Hotel and Restaurant Administration Quarterly 39 4 1998 28–40.Ž . Ž .

<sup>w</sup> <sup>x</sup>14 S. Hong, K. Siau, Information warehouse — the success factors, in: 1988 IRMA International Conference, Boston, MA, May 17–20, 1998, pp. 868–872.

<sup>w</sup> <sup>x</sup> 15 Hsuan Owyang, Chairman’s Statement, HDB Annual Report 1995<sup>r</sup>1996, p. 14.

<sup>w</sup> <sup>x</sup> 16 W.H. Inmon, Building the Data Warehouse, 2nd edn., Wiley, New York, 1996.

<sup>w</sup> <sup>x</sup> 17 K. Joshi, M. Curtis, Issues in building a successful data warehouse, Information Strategy: The Executive’s Journal Ž .1999 28–35, Winter.

<sup>w</sup> <sup>x</sup> 18 J. McElreath, An architectural perspective of data warehouses, Information Strategy: The Executive’s Journal 12 4Ž . Ž . 1996 30–41.

<sup>w</sup> <sup>x</sup> 19 V. Poe, Clear, careful, and realistic: guidelines for warehouse development, Database Programming and Design 1994 60–Ž . 64, September.

<sup>w</sup> <sup>x</sup> 20 C. Rautenstrauch, Modeling and implementation of data warehouse systems, in: 1998 IRMA International Conference, Boston, MA, May 17–20, 1998, pp. 325–333.

<sup>w</sup> <sup>x</sup> 21 C. Speier, J.W. Palmer, D. Bergman, Applying business framework analysis to the analysis and design of a data warehouse at Corporate Express, Journal of Data Warehousing 3 3 1998 52–59, Fall.Ž . Ž .

<sup>w</sup> <sup>x</sup> 22 T. Watson, The power and danger of warehousing, Computer Dealer News 1998 8, March 30.Ž .

![](/api/attachments/QQ74VZHS/fulltext/images/a956425214cd03794889534f7807f7ccb9b7f3058de3ad47eb82e2905733434e.jpg)

James S.K. Ang is Head of Departmen of Decision Sciences at National University of Singapore. He received his PhD from University of Waterloo. His research interests include Petri nets, data warehousing and IS planning. His works have been published in Database, Decision Sciences, European Journal of Information Systems, IEEE Transactions on Knowledge and Data Engineering, IEEE Transactions on Systems, Man and Cybernetics, Information and Manage-

ment, INFOR, International Journal of Production Economics and Journal of Operations Management.

![](/api/attachments/QQ74VZHS/fulltext/images/771511ed93abea7fdeaf0bf58273447e1b23d3ec02ea72088728a181e2bc7d3d.jpg)

Thompson S.H. Teo is Information Systems Area Coordinator in the Department of Decision Sciences at Nationa University of Singapore. He received his PhD from University of Pittsburgh. His research interests include data warehousing, electronic commerce, IS planning and strategic use of IT. He has published more than 40 papers in journals such as Accounting Management and Information Technologies, Communications of the ACM, Communications

of the AIS, Database, Decision Sciences, European Journal of Information Systems, Information and Management, Information Technology and People, International Journal of Electronic Commerce, Journal of MIS and Omega.
